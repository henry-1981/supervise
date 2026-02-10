"""
Test Suite for ARIA Team Mode Implementation

Tests the ARIA Team Coordinator and Team Execute workflow
using Claude Code Agent Teams API.

Test Coverage:
- Team creation and deletion
- Teammate spawning with proper parameters
- Domain-based file ownership validation
- VALID framework quality gates
- Multi-market submission scenarios
"""

import pytest
from pathlib import Path


class TestAriaTeamCoordinator:
    """Test ARIA Team Coordinator agent definition."""

    def test_coordinator_agent_exists(self):
        """Verify aria-team-coordinator agent file exists."""
        agent_path = Path("supervise/.claude/agents/aria/aria-team-coordinator.md")
        assert agent_path.exists(), "aria-team-coordinator.md should exist"

    def test_coordinator_has_team_tools(self):
        """Verify aria-team-coordinator has TeamCreate, TeamDelete, SendMessage tools."""
        agent_path = Path("supervise/.claude/agents/aria/aria-team-coordinator.md")
        content = agent_path.read_text()

        assert "TeamCreate" in content, "Should have TeamCreate tool"
        assert "TeamDelete" in content, "Should have TeamDelete tool"
        assert "SendMessage" in content, "Should have SendMessage tool"

    def test_coordinator_permission_mode(self):
        """Verify aria-team-coordinator uses delegate permission mode."""
        agent_path = Path("supervise/.claude/agents/aria/aria-team-coordinator.md")
        content = agent_path.read_text()

        assert "permissionMode: delegate" in content, "Should use delegate mode for team coordination"

    def test_coordinator_loads_team_workflow_skill(self):
        """Verify aria-team-coordinator loads aria-workflows-team-execute skill."""
        agent_path = Path("supervise/.claude/agents/aria/aria-team-coordinator.md")
        content = agent_path.read_text()

        assert "aria-workflows-team-execute" in content, "Should load team execute workflow skill"


class TestAriaTeamExecuteWorkflow:
    """Test ARIA Team Execute workflow implementation."""

    def test_workflow_file_exists(self):
        """Verify team-execute.md workflow file exists."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        assert workflow_path.exists(), "team-execute.md workflow should exist"

    def test_skill_definition_exists(self):
        """Verify aria-workflows-team-execute skill definition exists."""
        skill_path = Path("supervise/.claude/skills/aria-workflows-team-execute/SKILL.md")
        assert skill_path.exists(), "SKILL.md should exist"

    def test_workflow_uses_team_api(self):
        """Verify workflow uses TeamCreate, TeamDelete, SendMessage API."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        content = workflow_path.read_text()

        assert "TeamCreate" in content, "Should use TeamCreate"
        assert "TeamDelete" in content, "Should use TeamDelete"
        assert "SendMessage" in content, "Should use SendMessage"

    def test_workflow_has_valid_framework(self):
        """Verify workflow integrates VALID quality framework."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        content = workflow_path.read_text()

        assert "VALID" in content, "Should reference VALID framework"
        assert "Verified" in content, "Should define Verified dimension"
        assert "Accurate" in content, "Should define Accurate dimension"
        assert "Linked" in content, "Should define Linked dimension"
        assert "Inspectable" in content, "Should define Inspectable dimension"
        assert "Deliverable" in content, "Should define Deliverable dimension"

    def test_workflow_defines_domain_boundaries(self):
        """Verify workflow defines clear domain-based file ownership."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        content = workflow_path.read_text()

        assert "expert-regulatory" in content, "Should assign regulatory expert"
        assert "expert-clinical" in content, "Should assign clinical expert"
        assert "expert-risk" in content, "Should assign risk expert"
        assert "File Ownership" in content, "Should define file ownership"


class TestMultiMarketScenario:
    """Test multi-market submission scenario."""

    def test_workflow_supports_multi_market(self):
        """Verify workflow supports multi-market parallel execution."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        content = workflow_path.read_text()

        assert "Multi-Market" in content, "Should support multi-market scenarios"
        assert "FDA" in content, "Should reference FDA market"
        assert "EU MDR" in content or "EU" in content, "Should reference EU market"

    def test_workflow_has_parallel_execution_pattern(self):
        """Verify workflow uses Task() with team_name and name parameters."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        content = workflow_path.read_text()

        assert "team_name:" in content, "Should use team_name parameter"
        assert 'name:' in content, "Should use name parameter"
        assert "Task(" in content, "Should use Task() for teammate spawning"


class TestQualityGates:
    """Test VALID quality gates integration."""

    def test_skill_metadata_has_framework_tag(self):
        """Verify skill metadata identifies ARIA framework."""
        skill_path = Path("supervise/.claude/skills/aria-workflows-team-execute/SKILL.md")
        content = skill_path.read_text()

        assert 'framework: "aria"' in content, "Should tag as ARIA framework"
        assert 'domain: "medical-device-ra-qa"' in content, "Should identify medical device domain"

    def test_workflow_requires_quality_validation(self):
        """Verify workflow requires quality validation before synthesis."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        content = workflow_path.read_text()

        assert "Quality Gates" in content, "Should have quality gates phase"
        assert "validates" in content or "validation" in content, "Should validate before completion"


class TestConfiguration:
    """Test configuration requirements."""

    def test_workflow_checks_prerequisites(self):
        """Verify workflow checks for required configuration."""
        workflow_path = Path("supervise/.claude/skills/aria/workflows/team-execute.md")
        content = workflow_path.read_text()

        assert "Prerequisites" in content, "Should list prerequisites"
        assert "workflow.team.enabled" in content, "Should check team enabled setting"
        assert "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS" in content, "Should require agent teams env"


# Integration Test Markers
pytestmark = pytest.mark.aria_team_mode


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
