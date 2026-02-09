#!/bin/bash
# ARIA Quality Check Hook - PreToolUse
# Validates regulatory compliance before document changes
# SPEC-ARIA-005 Milestone 7: Hook System Integration

# Configuration
HOOK_NAME="aria-quality-check"
HOOK_VERSION="1.0.0"
TIMEOUT_MS=100

# Get project directory from environment or fallback
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
AUDIT_LOG="${PROJECT_DIR}/.claude/logs/aria-quality.log"

# Create directories (silently fail if read-only)
mkdir -p "$(dirname "$AUDIT_LOG")" 2>/dev/null || true

# Log function (silently fail if cannot write)
log_event() {
    local level="$1"
    local message="$2"
    [[ -w "$(dirname "$AUDIT_LOG")" ]] && \
        echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] [$level] [aria-quality-check] $message" >> "$AUDIT_LOG"
}

# Measure execution time (macOS compatible)
if date +%s%3N >/dev/null 2>&1; then
    start_time=$(date +%s%3N)
else
    start_time=$(python3 -c "import time; print(int(time.time()*1000))" 2>/dev/null || echo "0")
fi

# Read stdin JSON
input=$(cat)

# Extract relevant fields
tool_name=$(echo "$input" | jq -r '.toolName // empty' 2>/dev/null)
session_cwd=$(echo "$input" | jq -r '.session.cwd // empty' 2>/dev/null)
project_dir=$(echo "$input" | jq -r '.session.projectDir // empty' 2>/dev/null)

log_event "INFO" "Tool: $tool_name, CWD: $session_cwd"

# Validation result
validation_status="pass"
validation_errors=()

# Only validate Write/Edit operations on documents
if [[ "$tool_name" =~ ^(Write|Edit)$ ]]; then
    # Get file path from toolInput (handle missing jq)
    if command -v jq >/dev/null 2>&1; then
        file_path=$(echo "$input" | jq -r '.toolInput.file_path // .toolInput.path // empty' 2>/dev/null)
    else
        file_path=$(echo "$input" | grep -o '"file_path":"[^"]*"' | cut -d'"' -f4)
    fi

    # Skip if not a document file
    if [[ -n "$file_path" && "$file_path" =~ \.(md|txt|docx?|pdf?)$ ]]; then
        log_event "INFO" "Validating document: $file_path"

        # Check if file exists for Edit operations
        if [[ "$tool_name" == "Edit" && -f "$file_path" ]]; then
            # Read existing content
            existing_content=$(cat "$file_path" 2>/dev/null)

            # Regulatory Citation Format Check
            # Valid formats: "21 CFR 820.30", "EU MDR Annex I", "IEC 62304"
            citation_pattern="(21 CFR [0-9]+\.?[0-9]*|EU MDR (Annex|Article) [XVI]+|IEC [0-9]+(?:-[0-9]+)?)"

            if ! echo "$existing_content" | grep -qE "$citation_pattern"; then
                # Check if content contains regulatory references
                if echo "$existing_content" | grep -qiE "(regulation|standard|citation|reference|compliance|CFR|MDR|IEC|ISO)"; then
                    validation_errors+=("Regulatory citations may not follow required format (e.g., '21 CFR 820.30')")
                    validation_status="warning"
                    log_event "WARN" "Citation format check failed for $file_path"
                fi
            fi

            # VALID Framework Compliance Check
            # V = Verified, A = Accurate, L = Linked, I = Inspectable, D = Deliverable
            valid_keywords=("verified" "accurate" "linked" "inspectable" "deliverable")

            for keyword in "${valid_keywords[@]}"; do
                if echo "$existing_content" | grep -qiE "(validation|verification|accuracy|traceability|review|approval)"; then
                    if ! echo "$existing_content" | grep -qi "$keyword"; then
                        validation_errors+=("VALID framework: '$keyword' attribute may be missing")
                        validation_status="warning"
                        log_event "WARN" "VALID framework check: $keyword missing in $file_path"
                    fi
                fi
            done
        fi

        # Document Structure Check
        # Required sections: Purpose, Scope, References, Procedure
        required_sections=("Purpose|Scope|References|Procedure|Documentation")

        # For new documents, check template compliance
        if [[ "$tool_name" == "Write" ]]; then
            log_event "INFO" "New document creation: checking template compliance"
            # Template validation would be done by template-verification hook
        fi
    fi
fi

# Calculate execution time (macOS compatible)
if date +%s%3N >/dev/null 2>&1; then
    end_time=$(date +%s%3N)
    duration=$((end_time - start_time))
else
    end_time=$(python3 -c "import time; print(int(time.time()*1000))" 2>/dev/null || echo "$start_time")
    duration=$((end_time - start_time))
fi

log_event "INFO" "Validation completed in ${duration}ms with status: $validation_status"

# Build response JSON
if [[ "$validation_status" == "pass" ]]; then
    # Allow operation to proceed
    echo '{"status": "ok"}'
    exit 0
elif [[ "$validation_status" == "warning" ]]; then
    # Allow with warning
    response=$(cat <<EOF
{
  "status": "ok",
  "systemMessage": "⚠️ ARIA Quality Warning:\n$(printf ' - %s\n' "${validation_errors[@]}")\n\nConsider these issues before proceeding."
}
EOF
)
    echo "$response"
    exit 0
else
    # Block operation
    response=$(cat <<EOF
{
  "status": "error",
  "reason": "ARIA quality validation failed:\n$(printf ' - %s\n' "${validation_errors[@]}")"
}
EOF
)
    echo "$response"
    exit 2
fi
