#!/bin/bash
# ARIA Audit Trail Hook - PostToolUse
# Logs all Write/Edit operations per 21 CFR Part 11
# SPEC-ARIA-005 Milestone 7: Hook System Integration

# Configuration
HOOK_NAME="aria-audit-trail"
HOOK_VERSION="1.0.0"

# Get project directory from environment or fallback
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
AUDIT_DIR="${PROJECT_DIR}/.claude/audit"
AUDIT_LOG="${AUDIT_DIR}/audit-trail.log"
CHAIN_OF_CUSTODY="${AUDIT_DIR}/chain-of-custody.json"

# Create audit directory (silently fail if read-only)
mkdir -p "$AUDIT_DIR" 2>/dev/null || true

# Log function with timestamp
log_audit() {
    local event_type="$1"
    local details="$2"
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    echo "[$timestamp] [$event_type] $details" >> "$AUDIT_LOG"
}

# Read stdin JSON
input=$(cat)

# Extract event data (handle missing jq)
if command -v jq >/dev/null 2>&1; then
    tool_name=$(echo "$input" | jq -r '.toolName // empty' 2>/dev/null)
    tool_output=$(echo "$input" | jq -r '.toolOutput // empty' 2>/dev/null)
    session_id=$(echo "$input" | jq -r '.session.id // empty' 2>/dev/null)
    session_cwd=$(echo "$input" | jq -r '.session.cwd // empty' 2>/dev/null)
    user=$(echo "$input" | jq -r '.session.user // "unknown"' 2>/dev/null)
else
    tool_name=$(echo "$input" | grep -o '"toolName":"[^"]*"' | cut -d'"' -f4)
    session_id=$(echo "$input" | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)
    session_cwd=$(echo "$input" | grep -o '"cwd":"[^"]*"' | cut -d'"' -f4)
    user="unknown"
    tool_output=""
fi

# Only log Write/Edit operations
if [[ "$tool_name" =~ ^(Write|Edit)$ ]]; then
    # Extract file information (handle missing jq)
    if command -v jq >/dev/null 2>&1; then
        file_path=$(echo "$input" | jq -r '.toolInput.file_path // .toolInput.path // empty' 2>/dev/null)
    else
        file_path=$(echo "$input" | grep -o '"file_path":"[^"]*"' | cut -d'"' -f4)
    fi
    operation_type="$tool_name"

    # Generate change summary
    change_summary=""

    if [[ "$tool_name" == "Write" ]]; then
        change_summary="Created new file"
        file_size=$(echo "$tool_output" | wc -c 2>/dev/null || echo "unknown")
        change_summary="$change_summary (size: $file_size bytes)"
    elif [[ "$tool_name" == "Edit" ]]; then
        if command -v jq >/dev/null 2>&1; then
            old_string=$(echo "$input" | jq -r '.toolInput.old_string // empty' 2>/dev/null)
            new_string=$(echo "$input" | jq -r '.toolInput.new_string // empty' 2>/dev/null)
        else
            old_string=""
            new_string=""
        fi
        old_length=${#old_string}
        new_length=${#new_string}
        change_summary="Modified file (delta: $((new_length - old_length)) chars)"
    fi

    # Log to audit trail
    log_audit "FILE_OPERATION" "User: $user | Session: $session_id | Operation: $operation_type | File: $file_path | Summary: $change_summary"

    # Update chain of custody JSON
    custody_entry=$(cat <<EOF
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "event_type": "file_operation",
  "session_id": "$session_id",
  "user": "$user",
  "operation": "$operation_type",
  "file_path": "$file_path",
  "change_summary": "$change_summary",
  "working_directory": "$session_cwd"
}
EOF
)

    # Initialize chain of custody file if needed
    if [[ ! -f "$CHAIN_OF_CUSTODY" ]]; then
        echo '{"audit_trail": []}' > "$CHAIN_OF_CUSTODY"
    fi

    # Append entry using jq
    if command -v jq &> /dev/null; then
        jq ".audit_trail += [$custody_entry]" "$CHAIN_OF_CUSTODY" > "${CHAIN_OF_CUSTODY}.tmp" && mv "${CHAIN_OF_CUSTODY}.tmp" "$CHAIN_OF_CUSTODY"
    else
        # Fallback without jq
        echo "$custody_entry," >> "${CHAIN_OF_CUSTODY}.log"
    fi

    # Create resumption entry for crash recovery
    resumption_file="${AUDIT_DIR}/resumption-${session_id}.json"
    resumption_entry=$(cat <<EOF
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "session_id": "$session_id",
  "last_operation": "$operation_type",
  "last_file": "$file_path",
  "working_directory": "$session_cwd",
  "status": "completed"
}
EOF
)
    echo "$resumption_entry" > "$resumption_file"

    # Cleanup old resumption files (older than 24 hours)
    find "$AUDIT_DIR" -name "resumption-*.json" -mtime +1 -delete 2>/dev/null
fi

# Return success
echo '{"status": "logged"}'
exit 0
