#!/bin/bash
# ARIA Worktree Creation Script
# Purpose: Create Git worktrees for ARIA development and pure test environments
# Usage: .moai/scripts/create-worktree.sh [aria-dev|pure-test|all]

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

# Worktree configuration
ARIA_DEV_PATH="$PARENT_DIR/agent-skills-aria-dev"
ARIA_DEV_BRANCH="aria/feature-env-setup"
PURE_TEST_PATH="$PARENT_DIR/agent-skills-pure-test"
PURE_TEST_BRANCH="aria/test-pure-env"

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

# Function to check if worktree already exists
check_worktree_exists() {
    local path=$1
    if [ -d "$path" ]; then
        print_warning "Worktree already exists: $path"
        return 0
    fi
    return 1
}

# Function to create ARIA development worktree
create_aria_dev_worktree() {
    print_info "Creating ARIA Development Worktree..."

    if check_worktree_exists "$ARIA_DEV_PATH"; then
        print_info "Skipping ARIA dev worktree creation (already exists)"
        return 0
    fi

    # Check if branch already exists
    if git show-ref --verify --quiet "refs/heads/$ARIA_DEV_BRANCH"; then
        print_info "Branch $ARIA_DEV_BRANCH already exists, using it"
        # Create worktree with existing branch (no -b flag)
        git worktree add "$ARIA_DEV_PATH" "$ARIA_DEV_BRANCH"
    else
        print_info "Creating new branch: $ARIA_DEV_BRANCH"
        # Create worktree with new branch directly (more efficient)
        git worktree add "$ARIA_DEV_PATH" -b "$ARIA_DEV_BRANCH"
    fi

    # Setup .gitignore for pure test environment (will be used later)
    cat > "$ARIA_DEV_PATH/.gitignore" << 'EOF'
# ARIA files (for pure test environment)
# Note: These files are EXCLUDED in pure test environment only
# .claude/agents/aria/
# .claude/skills/aria-*/
# .claude/commands/aria.md
# .moai/config/aria.yaml
EOF

    print_success "ARIA Development Worktree created at: $ARIA_DEV_PATH"
    print_info "Branch: $ARIA_DEV_BRANCH"
    print_info "This environment includes ALL ARIA files"
}

# Function to create pure test worktree
create_pure_test_worktree() {
    print_info "Creating Pure Test Worktree..."

    if check_worktree_exists "$PURE_TEST_PATH"; then
        print_info "Skipping pure test worktree creation (already exists)"
        return 0
    fi

    # Check if branch already exists
    if git show-ref --verify --quiet "refs/heads/$PURE_TEST_BRANCH"; then
        print_info "Branch $PURE_TEST_BRANCH already exists, using it"
        # Create worktree with existing branch (no -b flag)
        git worktree add "$PURE_TEST_PATH" "$PURE_TEST_BRANCH"
    else
        print_info "Creating new branch: $PURE_TEST_BRANCH"
        # Create worktree with new branch directly (more efficient)
        git worktree add "$PURE_TEST_PATH" -b "$PURE_TEST_BRANCH"
    fi

    # Setup .gitignore to exclude ARIA files
    cat > "$PURE_TEST_PATH/.gitignore.pure-test" << 'EOF'
# ARIA files (excluded in pure test environment)
.claude/agents/aria/
.claude/skills/aria-*/
.claude/commands/aria.md
.moai/config/aria.yaml
.claude/agents/README-ARIA.md
.claude/skills/README-ARIA.md
EOF

    # Add to main .gitignore
    if [ -f "$PURE_TEST_PATH/.gitignore" ]; then
        if ! grep -q ".gitignore.pure-test" "$PURE_TEST_PATH/.gitignore"; then
            echo "" >> "$PURE_TEST_PATH/.gitignore"
            echo "# Include pure test exclusions" >> "$PURE_TEST_PATH/.gitignore"
            echo ".gitignore.pure-test" >> "$PURE_TEST_PATH/.gitignore"
        fi
    else
        echo "# Include pure test exclusions" > "$PURE_TEST_PATH/.gitignore"
        echo ".gitignore.pure-test" >> "$PURE_TEST_PATH/.gitignore"
    fi

    print_success "Pure Test Worktree created at: $PURE_TEST_PATH"
    print_info "Branch: $PURE_TEST_BRANCH"
    print_info "This environment EXCLUDES ARIA files"
}

# Function to list all worktrees
list_worktrees() {
    print_info "Current Git Worktrees:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    git worktree list
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

# Function to show worktree summary
show_summary() {
    echo ""
    print_success "Worktree Setup Complete!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Available Environments:"
    echo ""
    echo "  1. MoAI-ADK Main (Current)"
    echo "     Path: $PROJECT_ROOT"
    echo "     Branch: main"
    echo "     ARIA: No"
    echo ""
    if [ -d "$ARIA_DEV_PATH" ]; then
        echo "  2. ARIA Development"
        echo "     Path: $ARIA_DEV_PATH"
        echo "     Branch: $ARIA_DEV_BRANCH"
        echo "     ARIA: Yes (All ARIA files included)"
        echo ""
    fi
    if [ -d "$PURE_TEST_PATH" ]; then
        echo "  3. Pure Test Environment"
        echo "     Path: $PURE_TEST_PATH"
        echo "     Branch: $PURE_TEST_BRANCH"
        echo "     ARIA: No (ARIA files excluded)"
        echo ""
    fi
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    print_info "Switch between environments using:"
    echo "  .moai/scripts/switch-env.sh [aria-dev|pure-test|moai-main]"
    echo ""
    print_info "Or use the shorthand:"
    echo "  switch-env aria-dev"
    echo "  switch-env pure-test"
    echo "  switch-env moai-main"
    echo ""
}

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not a Git repository"
    exit 1
fi

# Check if an argument was provided
if [ $# -eq 0 ]; then
    print_error "No worktree type specified"
    echo ""
    echo "Usage: $0 [aria-dev|pure-test|all]"
    echo ""
    echo "Options:"
    echo "  aria-dev   - Create ARIA development worktree only"
    echo "  pure-test  - Create pure test worktree only"
    echo "  all        - Create both worktrees (recommended)"
    echo ""
    exit 1
fi

# Create worktrees based on argument
case "$1" in
    aria-dev)
        create_aria_dev_worktree
        list_worktrees
        show_summary
        ;;
    pure-test)
        create_pure_test_worktree
        list_worktrees
        show_summary
        ;;
    all)
        create_aria_dev_worktree
        create_pure_test_worktree
        list_worktrees
        show_summary
        ;;
    *)
        print_error "Invalid option: $1"
        echo ""
        echo "Usage: $0 [aria-dev|pure-test|all]"
        echo ""
        echo "Options:"
        echo "  aria-dev   - Create ARIA development worktree only"
        echo "  pure-test  - Create pure test worktree only"
        echo "  all        - Create both worktrees (recommended)"
        echo ""
        exit 1
        ;;
esac
