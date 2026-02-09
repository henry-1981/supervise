#!/bin/bash
# ARIA Environment Switch Script
# Purpose: Switch between ARIA development, pure test, and MoAI-ADK main environments
# Usage: .moai/scripts/switch-env.sh [aria-dev|pure-test|moai-main]

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

# Worktree paths
ARIA_DEV_PATH="$PARENT_DIR/agent-skills-aria-dev"
PURE_TEST_PATH="$PARENT_DIR/agent-skills-pure-test"
MOAI_MAIN_PATH="$PROJECT_ROOT"

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

# Function to check if directory exists
check_directory() {
    if [ ! -d "$1" ]; then
        print_error "Directory not found: $1"
        print_info "Please create the worktree first using create-worktree.sh"
        return 1
    fi
    return 0
}

# Function to display environment info
show_env_info() {
    local env_name=$1
    local env_path=$2
    local branch_name=$3

    echo ""
    print_success "Switched to: $env_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📁 Path:        $env_path"
    echo "🌿 Branch:      $branch_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # Check for ARIA files
    if [ -d "$env_path/.claude/agents/aria" ]; then
        echo "✅ ARIA Agents: Present ($(ls -1 "$env_path/.claude/agents/aria" | wc -l | tr -d ' ') files)"
    else
        echo "❌ ARIA Agents: Not present"
    fi

    if [ -d "$env_path/.claude/skills" ]; then
        local aria_skills=$(find "$env_path/.claude/skills" -maxdepth 1 -type d -name "aria-*" | wc -l | tr -d ' ')
        if [ "$aria_skills" -gt 0 ]; then
            echo "✅ ARIA Skills: Present ($aria_skills directories)"
        else
            echo "❌ ARIA Skills: Not present"
        fi
    fi

    # Check CLAUDE.md
    if [ -f "$env_path/CLAUDE.md" ]; then
        local claude_type=$(head -1 "$env_path/CLAUDE.md" | grep -o "ARIA\|MoAI" || echo "Unknown")
        echo "📄 CLAUDE.md:   $claude_type"
    fi

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

# Function to get current branch
get_branch() {
    local path=$1
    (cd "$path" && git branch --show-current)
}

# Main switch logic
switch_environment() {
    local env_name=$1

    case "$env_name" in
        aria-dev)
            if check_directory "$ARIA_DEV_PATH"; then
                cd "$ARIA_DEV_PATH"
                show_env_info "ARIA Development Environment" "$ARIA_DEV_PATH" "$(get_branch "$ARIA_DEV_PATH")"
                print_info "To start Claude Code in this environment, run:"
                echo "  cd $ARIA_DEV_PATH"
                echo "  claude"
            else
                exit 1
            fi
            ;;
        pure-test)
            if check_directory "$PURE_TEST_PATH"; then
                cd "$PURE_TEST_PATH"
                show_env_info "Pure Test Environment (No ARIA)" "$PURE_TEST_PATH" "$(get_branch "$PURE_TEST_PATH")"
                print_info "To start Claude Code in this environment, run:"
                echo "  cd $PURE_TEST_PATH"
                echo "  claude"
            else
                exit 1
            fi
            ;;
        moai-main)
            if check_directory "$MOAI_MAIN_PATH"; then
                cd "$MOAI_MAIN_PATH"
                show_env_info "MoAI-ADK Main Environment" "$MOAI_MAIN_PATH" "$(get_branch "$MOAI_MAIN_PATH")"
                print_info "To start Claude Code in this environment, run:"
                echo "  cd $MOAI_MAIN_PATH"
                echo "  claude"
            else
                exit 1
            fi
            ;;
        *)
            print_error "Invalid environment: $env_name"
            echo ""
            echo "Usage: $0 [aria-dev|pure-test|moai-main]"
            echo ""
            echo "Available environments:"
            echo "  aria-dev    - ARIA Development Environment (with ARIA files)"
            echo "  pure-test   - Pure Test Environment (without ARIA files)"
            echo "  moai-main   - MoAI-ADK Main Environment (without ARIA files)"
            echo ""
            echo "First time setup:"
            echo "  Run .moai/scripts/create-worktree.sh to create worktrees"
            exit 1
            ;;
    esac
}

# Check if an argument was provided
if [ $# -eq 0 ]; then
    print_error "No environment specified"
    echo ""
    echo "Usage: $0 [aria-dev|pure-test|moai-main]"
    echo ""
    echo "Available environments:"
    echo "  aria-dev    - ARIA Development Environment (with ARIA files)"
    echo "  pure-test   - Pure Test Environment (without ARIA files)"
    echo "  moai-main   - MoAI-ADK Main Environment (without ARIA files)"
    echo ""
    echo "First time setup:"
    echo "  Run .moai/scripts/create-worktree.sh to create worktrees"
    exit 1
fi

# Perform the switch
switch_environment "$1"
