#!/bin/bash
# ARIA Hook Performance Monitor
# Monitors hook execution times and performance metrics
# SPEC-ARIA-005 Milestone 7

set -e

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
PERF_LOG="$PROJECT_DIR/.claude/logs/aria-performance.log"
METRICS_FILE="$PROJECT_DIR/.claude/cache/hook-metrics.json"

# Create directories
mkdir -p "$(dirname "$PERF_LOG")"
mkdir -p "$(dirname "$METRICS_FILE")"

# Configuration
ARIA_HOOKS_DIR="$PROJECT_DIR/.claude/hooks/aria"
WARN_THRESHOLD_MS=100
CRITICAL_THRESHOLD_MS=500

# Initialize metrics
if [[ ! -f "$METRICS_FILE" ]]; then
    cat > "$METRICS_FILE" <<'EOF'
{
  "hooks": {
    "quality-check": {"calls": 0, "total_time_ms": 0, "avg_time_ms": 0},
    "audit-trail": {"calls": 0, "total_time_ms": 0, "avg_time_ms": 0},
    "template-verification": {"calls": 0, "total_time_ms": 0, "avg_time_ms": 0}
  },
  "last_updated": null
}
EOF
fi

# Log function
log_performance() {
    local hook_name="$1"
    local duration_ms="$2"
    local status="$3"
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    echo "[$timestamp] hook=$hook_name duration=${duration_ms}ms status=$status" >> "$PERF_LOG"

    # Update metrics
    if command -v jq &> /dev/null; then
        jq --arg hook "$hook_name" --argjson time "$duration_ms" \
           '.hooks[$hook].calls += 1 | .hooks[$hook].total_time_ms += $time | .hooks[$hook].avg_time_ms = (.hooks[$hook].total_time_ms / .hooks[$hook].calls | floor) | .last_updated = now | .last_updated |= strftime("%Y-%m-%dT%H:%M:%SZ")' \
           "$METRICS_FILE" > "${METRICS_FILE}.tmp" && mv "${METRICS_FILE}.tmp" "$METRICS_FILE"
    fi
}

# Measure hook execution
measure_hook() {
    local hook_name="$1"
    local hook_script="$2"
    local input="$3"

    local start_time=$(date +%s%N)
    local output
    local exit_code

    output=$(echo "$input" | "$hook_script" 2>&1)
    exit_code=$?

    local end_time=$(date +%s%N)
    local duration_ms=$(( (end_time - start_time) / 1000000 ))

    # Determine status
    local status="ok"
    if [[ $exit_code -eq 2 ]]; then
        status="blocked"
    elif [[ $exit_code -ne 0 ]]; then
        status="error"
    fi

    # Log performance
    log_performance "$hook_name" "$duration_ms" "$status"

    # Check thresholds
    if [[ $duration_ms -gt $CRITICAL_THRESHOLD_MS ]]; then
        echo "⚠️ CRITICAL: $hook_name took ${duration_ms}ms (exceeds ${CRITICAL_THRESHOLD_MS}ms threshold)" >&2
    elif [[ $duration_ms -gt $WARN_THRESHOLD_MS ]]; then
        echo "⚠️ WARNING: $hook_name took ${duration_ms}ms (exceeds ${WARN_THRESHOLD_MS}ms threshold)" >&2
    fi

    # Return output and exit code
    echo "$output"
    return $exit_code
}

# Display metrics
show_metrics() {
    echo "=== ARIA Hook Performance Metrics ==="
    echo ""

    if command -v jq &> /dev/null && [[ -f "$METRICS_FILE" ]]; then
        echo "Summary:"
        jq -r '
          "Last Updated: \(.last_updated // "Never")\n" +
          "\nQuality Check Hook:\n" +
          "  Calls: \(.hooks["quality-check"].calls // 0)\n" +
          "  Avg Time: \(.hooks["quality-check"].avg_time_ms // 0)ms\n" +
          "  Total Time: \(.hooks["quality-check"].total_time_ms // 0)ms\n" +
          "\nAudit Trail Hook:\n" +
          "  Calls: \(.hooks["audit-trail"].calls // 0)\n" +
          "  Avg Time: \(.hooks["audit-trail"].avg_time_ms // 0)ms\n" +
          "  Total Time: \(.hooks["audit-trail"].total_time_ms // 0)ms\n" +
          "\nTemplate Verification Hook:\n" +
          "  Calls: \(.hooks["template-verification"].calls // 0)\n" +
          "  Avg Time: \(.hooks["template-verification"].avg_time_ms // 0)ms\n" +
          "  Total Time: \(.hooks["template-verification"].total_time_ms // 0)ms\n"
        ' "$METRICS_FILE"
    else
        echo "Metrics file not available or jq not installed"
        echo "Metrics file: $METRICS_FILE"
    fi

    echo ""
    echo "Performance Log: $PERF_LOG"
}

# Main execution
case "${1:-monitor}" in
    monitor)
        # Continuous monitoring mode
        echo "Monitoring ARIA hook performance..."
        echo "Press Ctrl+C to stop"
        echo ""

        tail -f "$PERF_LOG" 2>/dev/null || echo "Waiting for performance data..."
        ;;
    metrics)
        # Show current metrics
        show_metrics
        ;;
    test)
        # Test hook performance
        echo "Testing hook performance..."
        echo ""

        # Test Quality Check
        echo "Testing quality-check-pre-tool.sh..."
        input='{"toolName":"Write","session":{"cwd":"'"$PROJECT_DIR"'"},"toolInput":{"file_path":"test.md"}}'
        measure_hook "quality-check" "$ARIA_HOOKS_DIR/quality-check-pre-tool.sh" "$input" > /dev/null
        echo ""

        # Test Audit Trail
        echo "Testing audit-trail-post-tool.sh..."
        input='{"toolName":"Write","session":{"id":"test","cwd":"'"$PROJECT_DIR"'","user":"test"},"toolInput":{"file_path":"test.md"},"toolOutput":"test"}'
        measure_hook "audit-trail" "$ARIA_HOOKS_DIR/audit-trail-post-tool.sh" "$input" > /dev/null
        echo ""

        # Test Template Verification
        echo "Testing template-verification-session-start.sh..."
        input='{"sessionId":"test","projectDir":"'"$PROJECT_DIR"'"}'
        measure_hook "template-verification" "$ARIA_HOOKS_DIR/template-verification-session-start.sh" "$input" > /dev/null
        echo ""

        echo "Test complete. Showing metrics..."
        echo ""
        show_metrics
        ;;
    reset)
        # Reset metrics
        echo "Resetting metrics..."
        cat > "$METRICS_FILE" <<'EOF'
{
  "hooks": {
    "quality-check": {"calls": 0, "total_time_ms": 0, "avg_time_ms": 0},
    "audit-trail": {"calls": 0, "total_time_ms": 0, "avg_time_ms": 0},
    "template-verification": {"calls": 0, "total_time_ms": 0, "avg_time_ms": 0}
  },
  "last_updated": null
}
EOF
        echo "Metrics reset complete"
        ;;
    *)
        echo "Usage: $0 {monitor|metrics|test|reset}"
        echo ""
        echo "Commands:"
        echo "  monitor  - Continuously monitor performance log (tail -f)"
        echo "  metrics  - Display current performance metrics"
        echo "  test     - Run performance tests on all hooks"
        echo "  reset    - Reset all metrics to zero"
        exit 1
        ;;
esac
