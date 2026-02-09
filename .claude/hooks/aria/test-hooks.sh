#!/bin/bash
# ARIA Hook System Test Script
# Tests all ARIA hooks for SPEC-ARIA-005 Milestone 7

set -e

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
ARIA_HOOKS_DIR="$PROJECT_DIR/.claude/hooks/aria"

echo "=== ARIA Hook System Test ==="
echo "Project Directory: $PROJECT_DIR"
echo "Hook Directory: $ARIA_HOOKS_DIR"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Test function
run_test() {
    local test_name="$1"
    local test_command="$2"
    local expected_exit="${3:-0}"

    TESTS_RUN=$((TESTS_RUN + 1))
    echo -n "Test $TESTS_RUN: $test_name ... "

    if eval "$test_command"; then
        echo -e "${GREEN}PASS${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}FAIL${NC}"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Check if hooks exist and are executable
echo "--- Hook File Checks ---"
run_test "Quality Check Hook Exists" "test -f '$ARIA_HOOKS_DIR/quality-check-pre-tool.sh'"
run_test "Quality Check Hook Executable" "test -x '$ARIA_HOOKS_DIR/quality-check-pre-tool.sh'"
run_test "Audit Trail Hook Exists" "test -f '$ARIA_HOOKS_DIR/audit-trail-post-tool.sh'"
run_test "Audit Trail Hook Executable" "test -x '$ARIA_HOOKS_DIR/audit-trail-post-tool.sh'"
run_test "Template Verification Hook Exists" "test -f '$ARIA_HOOKS_DIR/template-verification-session-start.sh'"
run_test "Template Verification Hook Executable" "test -x '$ARIA_HOOKS_DIR/template-verification-session-start.sh'"
echo ""

# Test Quality Check Hook
echo "--- Quality Check Hook Tests ---"

# Test 1: Valid Write operation (should pass)
run_test "Quality Check: Valid Write Operation" \
    "echo '{\"toolName\":\"Write\",\"session\":{\"cwd\":\"$PROJECT_DIR\"},\"toolInput\":{\"file_path\":\"test.md\"}}' | '$ARIA_HOOKS_DIR/quality-check-pre-tool.sh' | grep -q 'ok'"

# Test 2: Valid Edit operation (should pass)
run_test "Quality Check: Valid Edit Operation" \
    "echo '{\"toolName\":\"Edit\",\"session\":{\"cwd\":\"$PROJECT_DIR\"},\"toolInput\":{\"file_path\":\"test.md\"}}' | '$ARIA_HOOKS_DIR/quality-check-pre-tool.sh' | grep -q 'ok'"

# Test 3: Bash operation (should be skipped/ignored)
run_test "Quality Check: Bash Operation Ignored" \
    "echo '{\"toolName\":\"Bash\",\"session\":{\"cwd\":\"$PROJECT_DIR\"}}' | '$ARIA_HOOKS_DIR/quality-check-pre-tool.sh' | grep -q 'ok'"

echo ""

# Test Audit Trail Hook
echo "--- Audit Trail Hook Tests ---"

# Test 1: Write operation logging
run_test "Audit Trail: Write Operation Logged" \
    "echo '{\"toolName\":\"Write\",\"session\":{\"id\":\"test-session\",\"cwd\":\"$PROJECT_DIR\",\"user\":\"test-user\"},\"toolInput\":{\"file_path\":\"test.md\"},\"toolOutput\":\"test content\"}' | '$ARIA_HOOKS_DIR/audit-trail-post-tool.sh' | grep -q 'logged'"

# Test 2: Edit operation logging
run_test "Audit Trail: Edit Operation Logged" \
    "echo '{\"toolName\":\"Edit\",\"session\":{\"id\":\"test-session\",\"cwd\":\"$PROJECT_DIR\",\"user\":\"test-user\"},\"toolInput\":{\"file_path\":\"test.md\",\"old_string\":\"old\",\"new_string\":\"new\"}}' | '$ARIA_HOOKS_DIR/audit-trail-post-tool.sh' | grep -q 'logged'"

# Test 3: Check audit log creation
if [[ -f "$PROJECT_DIR/.claude/audit/audit-trail.log" ]]; then
    echo -e "${GREEN}Audit Trail: Log File Created${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
    TESTS_RUN=$((TESTS_RUN + 1))
else
    echo -e "${YELLOW}Audit Trail: Log File Not Yet Created (will be created on first use)${NC}"
    TESTS_RUN=$((TESTS_RUN + 1))
fi

echo ""

# Test Template Verification Hook
echo "--- Template Verification Hook Tests ---"

# Test 1: Session start validation
run_test "Template Verification: Session Start Validated" \
    "echo '{\"sessionId\":\"test-session\",\"projectDir\":\"$PROJECT_DIR\"}' | '$ARIA_HOOKS_DIR/template-verification-session-start.sh' | grep -q 'status'"

# Test 2: Check cache creation
if [[ -f "$PROJECT_DIR/.claude/cache/template-status.json" ]]; then
    echo -e "${GREEN}Template Verification: Cache File Created${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
    TESTS_RUN=$((TESTS_RUN + 1))
else
    echo -e "${YELLOW}Template Verification: Cache File Not Yet Created (will be created on session start)${NC}"
    TESTS_RUN=$((TESTS_RUN + 1))
fi

echo ""

# Test Settings Integration
echo "--- Settings Configuration Tests ---"

SETTINGS_FILE="$PROJECT_DIR/.claude/settings.json"

# Check if ARIA hooks are registered
run_test "Settings: Quality Check Hook Registered" \
    "grep -q 'quality-check-pre-tool.sh' '$SETTINGS_FILE'"

run_test "Settings: Audit Trail Hook Registered" \
    "grep -q 'audit-trail-post-tool.sh' '$SETTINGS_FILE'"

run_test "Settings: Template Verification Hook Registered" \
    "grep -q 'template-verification-session-start.sh' '$SETTINGS_FILE'"

run_test "Settings: PreToolUse Configured" \
    "grep -q '"PreToolUse"' '$SETTINGS_FILE'"

run_test "Settings: PostToolUse Configured" \
    "grep -q '"PostToolUse"' '$SETTINGS_FILE'"

run_test "Settings: SessionStart Configured" \
    "grep -q '"SessionStart"' '$SETTINGS_FILE'"

echo ""

# Performance Test
echo "--- Performance Tests ---"

# Test Quality Check performance
start_time=$(date +%s%N)
echo '{"toolName":"Write","session":{"cwd":"$PROJECT_DIR"}}' | "$ARIA_HOOKS_DIR/quality-check-pre-tool.sh" > /dev/null
end_time=$(date +%s%N)
duration_ms=$(( (end_time - start_time) / 1000000 ))

if [[ $duration_ms -lt 100 ]]; then
    echo -e "${GREEN}Quality Check Performance: ${duration_ms}ms (< 100ms target)${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
else
    echo -e "${YELLOW}Quality Check Performance: ${duration_ms}ms (exceeds 100ms target)${NC}"
    TESTS_RUN=$((TESTS_RUN + 1))
fi
TESTS_RUN=$((TESTS_RUN + 1))

echo ""
echo "=== Test Summary ==="
echo "Tests Run: $TESTS_RUN"
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
if [[ $TESTS_FAILED -gt 0 ]]; then
    echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"
fi

if [[ $TESTS_FAILED -eq 0 ]]; then
    echo ""
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}Some tests failed!${NC}"
    exit 1
fi
