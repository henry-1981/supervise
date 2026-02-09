#!/bin/bash
# ARIA Template Verification Hook - SessionStart

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
TEMPLATE_DIR="${PROJECT_DIR}/.claude/templates"
TEMPLATE_CACHE="${PROJECT_DIR}/.claude/cache/template-status.json"
AUDIT_LOG="${PROJECT_DIR}/.claude/logs/aria-template.log"

mkdir -p "$(dirname "$AUDIT_LOG")" 2>/dev/null || true
mkdir -p "$(dirname "$TEMPLATE_CACHE")" 2>/dev/null || true

log_event() {
    local level="$1"
    local message="$2"
    [[ -w "$(dirname "$AUDIT_LOG")" ]] && \
        echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] [$level] [aria-template] $message" >> "$AUDIT_LOG"
}

TEMPLATE_VERSIONS=(
    "510k-submission:2.1.0"
    "technical-file:3.0.1"
    "risk-analysis:1.5.2"
    "design-history:2.3.0"
    "clinical-evaluation:1.8.0"
)

log_event "INFO" "Template verification started"

input=$(cat)

if command -v jq >/dev/null 2>&1; then
    session_id=$(echo "$input" | jq -r '.sessionId // empty' 2>/dev/null)
else
    session_id=$(echo "$input" | grep -o '"sessionId":"[^"]*"' | cut -d'"' -f4)
fi

if [[ ! -d "$TEMPLATE_DIR" ]]; then
    log_event "WARN" "Template directory not found"
    echo '{"status": "skip"}'
    exit 0
fi

current_templates=()
outdated_templates=()
missing_templates=()

for template_entry in "${TEMPLATE_VERSIONS[@]}"; do
    template_name="${template_entry%%:*}"
    expected_version="${template_entry##*:}"
    template_file="${TEMPLATE_DIR}/${template_name}.md"

    if [[ -f "$template_file" ]]; then
        template_version=$(grep -m1 "^version:" "$template_file" | sed 's/version: *//' | tr -d '"' 2>/dev/null)
        [[ -z "$template_version" ]] && template_version="unknown"

        if [[ "$template_version" != "$expected_version" ]]; then
            outdated_templates+=("$template_name:$template_version:$expected_version")
            log_event "WARN" "Template outdated: $template_name"
        else
            current_templates+=("$template_name:$template_version")
            log_event "INFO" "Template current: $template_name"
        fi
    else
        missing_templates+=("$template_name")
        log_event "WARN" "Template missing: $template_name"
    fi
done

# Write simple cache
if [[ -w "$(dirname "$TEMPLATE_CACHE")" ]]; then
    ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    cur=${#current_templates[@]}
    out=${#outdated_templates[@]}
    mis=${#missing_templates[@]}
    printf '{"timestamp":"%s","session_id":"%s","current":%d,"outdated":%d,"missing":%d}' "$ts" "$session_id" "$cur" "$out" "$mis" > "$TEMPLATE_CACHE"
fi

# Build response
if [[ ${#outdated_templates[@]} -gt 0 || ${#missing_templates[@]} -gt 0 ]]; then
    log_event "WARN" "Template issues detected"
    echo '{"status":"warning","systemMessage":"ARIA templates need attention"}'
else
    log_event "INFO" "All templates current"
    echo '{"status":"ok","systemMessage":"All ARIA templates are current"}'
fi

exit 0
