#!/usr/bin/env python3
"""
Simple validation script for ARIA Team Mode implementation.
Does not require pytest.
"""

from pathlib import Path
import sys


def validate_file_exists(path, description):
    """Validate that a file exists."""
    if path.exists():
        print(f"✅ PASS: {description}")
        return True
    else:
        print(f"❌ FAIL: {description} - File not found: {path}")
        return False


def validate_content(path, search_terms, description):
    """Validate that file contains required content."""
    if not path.exists():
        print(f"❌ FAIL: {description} - File not found: {path}")
        return False

    content = path.read_text()
    missing = [term for term in search_terms if term not in content]

    if not missing:
        print(f"✅ PASS: {description}")
        return True
    else:
        print(f"❌ FAIL: {description} - Missing: {', '.join(missing)}")
        return False


def main():
    print("=" * 60)
    print("ARIA Team Mode Validation")
    print("=" * 60)

    results = []

    # Test 1: Agent file exists
    results.append(validate_file_exists(
        Path("supervise/.claude/agents/aria/aria-team-coordinator.md"),
        "aria-team-coordinator agent exists"
    ))

    # Test 2: Agent has Team API tools
    results.append(validate_content(
        Path("supervise/.claude/agents/aria/aria-team-coordinator.md"),
        ["TeamCreate", "TeamDelete", "SendMessage"],
        "aria-team-coordinator has Team API tools"
    ))

    # Test 3: Agent uses delegate mode
    results.append(validate_content(
        Path("supervise/.claude/agents/aria/aria-team-coordinator.md"),
        ["permissionMode: delegate"],
        "aria-team-coordinator uses delegate mode"
    ))

    # Test 4: Workflow file exists
    results.append(validate_file_exists(
        Path("supervise/.claude/skills/aria/workflows/team-execute.md"),
        "team-execute workflow exists"
    ))

    # Test 5: Workflow uses Team API
    results.append(validate_content(
        Path("supervise/.claude/skills/aria/workflows/team-execute.md"),
        ["TeamCreate", "TeamDelete", "team_name:"],
        "team-execute workflow uses Team API"
    ))

    # Test 6: Workflow has VALID framework
    results.append(validate_content(
        Path("supervise/.claude/skills/aria/workflows/team-execute.md"),
        ["VALID", "Verified", "Accurate", "Linked", "Inspectable", "Deliverable"],
        "team-execute workflow integrates VALID framework"
    ))

    # Test 7: Skill definition exists
    results.append(validate_file_exists(
        Path("supervise/.claude/skills/aria-workflows-team-execute/SKILL.md"),
        "aria-workflows-team-execute skill exists"
    ))

    # Test 8: Skill has proper metadata
    results.append(validate_content(
        Path("supervise/.claude/skills/aria-workflows-team-execute/SKILL.md"),
        ['framework: "aria"', 'domain: "medical-device-ra-qa"'],
        "aria-workflows-team-execute has proper metadata"
    ))

    # Test 9: Workflow supports multi-market
    results.append(validate_content(
        Path("supervise/.claude/skills/aria/workflows/team-execute.md"),
        ["Multi-Market", "FDA", "EU"],
        "team-execute workflow supports multi-market scenarios"
    ))

    # Test 10: Workflow defines domain boundaries
    results.append(validate_content(
        Path("supervise/.claude/skills/aria/workflows/team-execute.md"),
        ["expert-regulatory", "expert-clinical", "File Ownership"],
        "team-execute workflow defines domain boundaries"
    ))

    print("=" * 60)
    passed = sum(results)
    total = len(results)
    percentage = (passed / total) * 100 if total > 0 else 0

    print(f"\nResults: {passed}/{total} tests passed ({percentage:.1f}%)")

    if passed == total:
        print("\n✅ All validations passed!")
        return 0
    else:
        print(f"\n❌ {total - passed} validation(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
