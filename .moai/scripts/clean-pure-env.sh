#!/bin/bash
# Clean ARIA files from Pure Test Environment
# Purpose: Remove ARIA files from pure test environment to create isolation
# Usage: .moai/scripts/clean-pure-env.sh

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(dirname "$PROJECT_ROOT")"

# Determine parent directory for worktrees
PARENT_DIR="$(dirname "$PROJECT_ROOT")"

# Pure test path
PURE_TEST_PATH="$PARENT_DIR/agent-skills-pure-test"

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if pure test environment exists
if [ ! -d "$PURE_TEST_PATH" ]; then
    print_error "Pure test environment not found: $PURE_TEST_PATH"
    print_info "Run create-worktree.sh first"
    exit 1
fi

cd "$PURE_TEST_PATH"

print_info "Cleaning ARIA files from Pure Test Environment..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Count files before
aria_agents_before=$(find .claude/agents/aria -type f 2>/dev/null | wc -l | tr -d ' ')
aria_skills_before=$(find .claude/skills -type d -name "aria-*" 2>/dev/null | wc -l | tr -d ' ')

print_info "ARIA files before cleanup:"
echo "  - ARIA Agents: $aria_agents_before files"
echo "  - ARIA Skills: $aria_skills_before directories"
echo ""

# Remove ARIA directories
print_info "Removing ARIA directories..."

# Remove ARIA agents
if [ -d ".claude/agents/aria" ]; then
    rm -rf .claude/agents/aria
    print_success "Removed .claude/agents/aria/"
fi

# Remove ARIA skills
find .claude/skills -type d -name "aria-*" -exec rm -rf {} + 2>/dev/null || true
print_success "Removed ARIA skill directories"

# Remove ARIA command file
if [ -f ".claude/commands/aria.md" ]; then
    rm -f .claude/commands/aria.md
    print_success "Removed .claude/commands/aria.md"
fi

# Remove ARIA config
if [ -f ".moai/config/aria.yaml" ]; then
    rm -f .moai/config/aria.yaml
    print_success "Removed .moai/config/aria.yaml"
fi

# Remove ARIA README files
if [ -f ".claude/agents/README-ARIA.md" ]; then
    rm -f .claude/agents/README-ARIA.md
    print_success "Removed .claude/agents/README-ARIA.md"
fi

if [ -f ".claude/skills/README-ARIA.md" ]; then
    rm -f .claude/skills/README-ARIA.md
    print_success "Removed .claude/skills/README-ARIA.md"
fi

echo ""
print_success "Cleanup complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Count files after
aria_agents_after=$(find .claude/agents/aria -type f 2>/dev/null | wc -l | tr -d ' ')
aria_skills_after=$(find .claude/skills -type d -name "aria-*" 2>/dev/null | wc -l | tr -d ' ')

print_info "ARIA files after cleanup:"
echo "  - ARIA Agents: $aria_agents_after files"
echo "  - ARIA Skills: $aria_skills_after directories"
echo ""

# Verify cleanup
if [ "$aria_agents_after" -eq 0 ] && [ "$aria_skills_after" -eq 0 ]; then
    print_success "✅ Pure Test Environment is clean (no ARIA files)"
else
    print_warning "⚠️  Some ARIA files may still exist"
fi

echo ""
print_info "Pure Test Environment is ready for testing ARIA's impact"
print_info "on MoAI-ADK without ARIA files loaded."
echo ""
