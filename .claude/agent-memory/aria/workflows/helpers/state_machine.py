#!/usr/bin/env python3
"""
ARIA Workflow State Machine Helper

Manages workflow state transitions, context preservation, and persistence
for ARIA workflows (Clinical Evaluation, Internal Audit, Post-Market Surveillance).

Compatible with Claude Code MoAI-ADK framework.
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path


class WorkflowState:
    """Workflow state management class."""

    # Workflow type definitions
    WORKFLOW_TYPES = {
        "clinical_evaluation": {
            "stages": [
                "scope_definition",
                "literature_search",
                "data_analysis",
                "cer_generation"
            ],
            "prefix": "CE"
        },
        "internal_audit": {
            "stages": [
                "audit_planning",
                "audit_execution",
                "capa_planning",
                "verification"
            ],
            "prefix": "IA"
        },
        "post_market_surveillance": {
            "stages": [
                "data_collection",
                "trend_analysis",
                "reporting",
                "fsca_trigger"  # Conditional stage
            ],
            "prefix": "PMS"
        }
    }

    def __init__(self, workflow_type: str, storage_dir: str = None):
        """
        Initialize workflow state manager.

        Args:
            workflow_type: Type of workflow (clinical_evaluation, internal_audit, post_market_surveillance)
            storage_dir: Directory for storing workflow state files
        """
        if workflow_type not in self.WORKFLOW_TYPES:
            raise ValueError(f"Unknown workflow type: {workflow_type}")

        self.workflow_type = workflow_type
        self.stages = self.WORKFLOW_TYPES[workflow_type]["stages"]
        self.prefix = self.WORKFLOW_TYPES[workflow_type]["prefix"]

        # Set storage directory
        if storage_dir is None:
            # Default to project-relative path
            storage_dir = ".claude/agent-memory/aria/workflows"

        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def generate_workflow_id(self) -> str:
        """
        Generate unique workflow ID.

        Returns:
            Workflow ID in format WF-{TYPE}-{YEAR}-{SEQ}
        """
        year = datetime.now().year
        seq = self._get_next_sequence(year)
        return f"WF-{self.prefix}-{year}-{seq:03d}"

    def _get_next_sequence(self, year: int) -> int:
        """Get next sequence number for workflow ID."""
        # Count existing workflows for this year
        existing = list(self.storage_dir.glob(f"WF-{self.prefix}-{year}-*.json"))
        return len(existing) + 1

    def initialize(self, initial_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Initialize new workflow state.

        Args:
            initial_context: Optional initial context data

        Returns:
            Initialized workflow state
        """
        workflow_id = self.generate_workflow_id()
        first_stage = self.stages[0]

        state = {
            "workflow_id": workflow_id,
            "workflow_type": self.workflow_type,
            "current_stage": first_stage,
            "status": "not_started",
            "progress": 0,
            "context": initial_context or {},
            "stages": self._initialize_stages(),
            "history": [{
                "timestamp": datetime.now().isoformat(),
                "event": "workflow_initialized",
                "to_stage": first_stage
            }],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

        self.save(workflow_id, state)
        return state

    def _initialize_stages(self) -> Dict[str, Dict[str, Any]]:
        """Initialize stage states."""
        stages = {}
        for stage_name in self.stages:
            stages[stage_name] = {
                "status": "pending",
                "progress": 0,
                "steps": {}
            }
        return stages

    def start_stage(self, workflow_id: str, stage_name: str = None) -> Dict[str, Any]:
        """
        Start a workflow stage.

        Args:
            workflow_id: Workflow identifier
            stage_name: Stage to start (uses current stage if not specified)

        Returns:
            Updated workflow state
        """
        state = self.load(workflow_id)

        if stage_name is None:
            stage_name = state["current_stage"]

        if stage_name not in self.stages:
            raise ValueError(f"Unknown stage: {stage_name}")

        # Update stage status
        state["stages"][stage_name]["status"] = "in_progress"
        state["stages"][stage_name]["started_at"] = datetime.now().isoformat()

        # Update overall status
        state["status"] = "in_progress"

        # Update history
        state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "event": "stage_started",
            "stage": stage_name
        })

        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()

        self.save(workflow_id, state)
        return state

    def complete_stage(
        self,
        workflow_id: str,
        stage_name: str = None,
        outputs: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Complete a workflow stage.

        Args:
            workflow_id: Workflow identifier
            stage_name: Stage to complete (uses current stage if not specified)
            outputs: Stage outputs to preserve in context

        Returns:
            Updated workflow state
        """
        state = self.load(workflow_id)

        if stage_name is None:
            stage_name = state["current_stage"]

        if stage_name not in self.stages:
            raise ValueError(f"Unknown stage: {stage_name}")

        # Update stage status
        state["stages"][stage_name]["status"] = "completed"
        state["stages"][stage_name]["progress"] = 100
        state["stages"][stage_name]["completed_at"] = datetime.now().isoformat()

        # Store outputs
        if outputs:
            if "outputs" not in state["stages"][stage_name]:
                state["stages"][stage_name]["outputs"] = {}
            state["stages"][stage_name]["outputs"].update(outputs)

            # Also add to main context
            if "collected_data" not in state["context"]:
                state["context"]["collected_data"] = {}
            state["context"]["collected_data"].update(outputs)

        # Transition to next stage
        current_index = self.stages.index(stage_name)
        if current_index < len(self.stages) - 1:
            next_stage = self.stages[current_index + 1]
            state["current_stage"] = next_stage
        else:
            # Workflow complete
            state["status"] = "completed"
            state["progress"] = 100

        # Recalculate progress
        state["progress"] = self._calculate_progress(state)

        # Update history
        state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "event": "stage_completed",
            "stage": stage_name,
            "outputs_count": len(outputs) if outputs else 0
        })

        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()

        self.save(workflow_id, state)
        return state

    def skip_stage(
        self,
        workflow_id: str,
        stage_name: str = None,
        justification: str = None
    ) -> Dict[str, Any]:
        """
        Skip a workflow stage with justification.

        Args:
            workflow_id: Workflow identifier
            stage_name: Stage to skip (uses current stage if not specified)
            justification: Reason for skipping

        Returns:
            Updated workflow state
        """
        state = self.load(workflow_id)

        if stage_name is None:
            stage_name = state["current_stage"]

        if stage_name not in self.stages:
            raise ValueError(f"Unknown stage: {stage_name}")

        # Update stage status
        state["stages"][stage_name]["status"] = "skipped"
        state["stages"][stage_name]["justification"] = justification
        state["stages"][stage_name]["skipped_at"] = datetime.now().isoformat()

        # Transition to next stage
        current_index = self.stages.index(stage_name)
        if current_index < len(self.stages) - 1:
            next_stage = self.stages[current_index + 1]
            state["current_stage"] = next_stage
        else:
            # Workflow complete
            state["status"] = "completed"
            state["progress"] = 100

        # Recalculate progress
        state["progress"] = self._calculate_progress(state)

        # Update history
        state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "event": "stage_skipped",
            "stage": stage_name,
            "justification": justification
        })

        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()

        self.save(workflow_id, state)
        return state

    def go_back(
        self,
        workflow_id: str,
        to_stage: str,
        preserve_data: bool = True
    ) -> Dict[str, Any]:
        """
        Navigate back to a previous stage.

        Args:
            workflow_id: Workflow identifier
            to_stage: Stage to return to
            preserve_data: Whether to preserve current stage data

        Returns:
            Updated workflow state
        """
        state = self.load(workflow_id)

        if to_stage not in self.stages:
            raise ValueError(f"Unknown stage: {to_stage}")

        if to_stage == state["current_stage"]:
            return state  # Already at this stage

        # Store previous stage
        from_stage = state["current_stage"]

        # Update current stage
        state["current_stage"] = to_stage

        # Recalculate progress (going back reduces progress)
        state["progress"] = self._calculate_progress(state)

        # Update history
        state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "event": "stage_navigated_back",
            "from_stage": from_stage,
            "to_stage": to_stage,
            "preserve_data": preserve_data
        })

        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()

        self.save(workflow_id, state)
        return state

    def update_step_progress(
        self,
        workflow_id: str,
        stage_name: str = None,
        step_name: str = None,
        status: str = "in_progress"
    ) -> Dict[str, Any]:
        """
        Update progress of a step within a stage.

        Args:
            workflow_id: Workflow identifier
            stage_name: Stage containing the step
            step_name: Step name to update
            status: Step status (pending, in_progress, completed)

        Returns:
            Updated workflow state
        """
        state = self.load(workflow_id)

        if stage_name is None:
            stage_name = state["current_stage"]

        if step_name is None:
            raise ValueError("step_name must be specified")

        # Update step status
        if "steps" not in state["stages"][stage_name]:
            state["stages"][stage_name]["steps"] = {}

        state["stages"][stage_name]["steps"][step_name] = status

        # Recalculate stage progress
        stage_progress = self._calculate_stage_progress(state, stage_name)
        state["stages"][stage_name]["progress"] = stage_progress

        # Recalculate overall progress
        state["progress"] = self._calculate_progress(state)

        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()

        self.save(workflow_id, state)
        return state

    def add_flag(
        self,
        workflow_id: str,
        flag_type: str,
        severity: str,
        description: str
    ) -> Dict[str, Any]:
        """
        Add a flag to the workflow.

        Args:
            workflow_id: Workflow identifier
            flag_type: Type of flag (pmcf, repeat_finding, safety_issue, timeline_risk)
            severity: Flag severity (critical, major, minor)
            description: Flag description

        Returns:
            Updated workflow state
        """
        state = self.load(workflow_id)

        if "flags" not in state["context"]:
            state["context"]["flags"] = []

        flag = {
            "flag_type": flag_type,
            "severity": severity,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "resolved": False
        }

        state["context"]["flags"].append(flag)

        # Update history
        state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "event": "flag_added",
            "flag_type": flag_type,
            "severity": severity
        })

        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()

        self.save(workflow_id, state)
        return state

    def resolve_flag(
        self,
        workflow_id: str,
        flag_index: int,
        resolution: str = None
    ) -> Dict[str, Any]:
        """
        Resolve a flag.

        Args:
            workflow_id: Workflow identifier
            flag_index: Index of flag to resolve
            resolution: Resolution description

        Returns:
            Updated workflow state
        """
        state = self.load(workflow_id)

        if "flags" not in state["context"]:
            raise ValueError("No flags in workflow")

        if flag_index >= len(state["context"]["flags"]):
            raise ValueError(f"Flag index {flag_index} out of range")

        flag = state["context"]["flags"][flag_index]
        flag["resolved"] = True
        flag["resolved_at"] = datetime.now().isoformat()
        if resolution:
            flag["resolution"] = resolution

        # Update history
        state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "event": "flag_resolved",
            "flag_type": flag["flag_type"]
        })

        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()

        self.save(workflow_id, state)
        return state

    def save(self, workflow_id: str, state: Dict[str, Any]) -> None:
        """
        Save workflow state to file.

        Args:
            workflow_id: Workflow identifier
            state: Workflow state to save
        """
        file_path = self.storage_dir / f"{workflow_id}.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

    def load(self, workflow_id: str) -> Dict[str, Any]:
        """
        Load workflow state from file.

        Args:
            workflow_id: Workflow identifier

        Returns:
            Workflow state

        Raises:
            FileNotFoundError: If workflow state file not found
        """
        file_path = self.storage_dir / f"{workflow_id}.json"

        if not file_path.exists():
            raise FileNotFoundError(f"Workflow state not found: {workflow_id}")

        with open(file_path, 'r', encoding='utf-8') as f:
            state = json.load(f)

        return state

    def list_workflows(
        self,
        status: str = None,
        workflow_type: str = None
    ) -> List[Dict[str, Any]]:
        """
        List workflows with optional filters.

        Args:
            status: Filter by status (not_started, in_progress, completed, on_hold, cancelled)
            workflow_type: Filter by workflow type

        Returns:
            List of workflow summaries
        """
        workflows = []

        for file_path in self.storage_dir.glob("WF-*.json"):
            with open(file_path, 'r', encoding='utf-8') as f:
                state = json.load(f)

            # Apply filters
            if status and state.get("status") != status:
                continue
            if workflow_type and state.get("workflow_type") != workflow_type:
                continue

            # Create summary
            summary = {
                "workflow_id": state["workflow_id"],
                "workflow_type": state["workflow_type"],
                "status": state["status"],
                "current_stage": state["current_stage"],
                "progress": state["progress"],
                "created_at": state["created_at"],
                "updated_at": state["updated_at"]
            }
            workflows.append(summary)

        # Sort by creation date, newest first
        workflows.sort(key=lambda x: x["created_at"], reverse=True)

        return workflows

    def _calculate_progress(self, state: Dict[str, Any]) -> int:
        """
        Calculate overall workflow progress percentage.

        Args:
            state: Workflow state

        Returns:
            Progress percentage (0-100)
        """
        total_progress = 0
        stage_count = len(self.stages)

        for stage_name in self.stages:
            stage_data = state["stages"].get(stage_name, {})
            stage_progress = stage_data.get("progress", 0)

            # Weight stages equally
            total_progress += (stage_progress / stage_count)

        return int(total_progress)

    def _calculate_stage_progress(self, state: Dict[str, Any], stage_name: str) -> int:
        """
        Calculate stage progress based on completed steps.

        Args:
            state: Workflow state
            stage_name: Stage name

        Returns:
            Stage progress percentage (0-100)
        """
        stage_data = state["stages"].get(stage_name, {})
        steps = stage_data.get("steps", {})

        if not steps:
            return 0

        completed = sum(1 for status in steps.values() if status == "completed")
        total = len(steps)

        return int((completed / total) * 100) if total > 0 else 0


# Convenience functions for common operations

def create_workflow(workflow_type: str, storage_dir: str = None) -> tuple:
    """
    Create a new workflow and return its ID and initial state.

    Args:
        workflow_type: Type of workflow to create
        storage_dir: Storage directory for workflow files

    Returns:
        Tuple of (workflow_id, initial_state)
    """
    manager = WorkflowState(workflow_type, storage_dir)
    state = manager.initialize()
    return state["workflow_id"], state


def get_workflow(workflow_id: str, storage_dir: str = None) -> Dict[str, Any]:
    """
    Load an existing workflow.

    Args:
        workflow_id: Workflow identifier
        storage_dir: Storage directory for workflow files

    Returns:
        Workflow state
    """
    if storage_dir is None:
        storage_dir = ".claude/agent-memory/aria/workflows"

    manager = WorkflowState("", storage_dir)  # Type not needed for load
    return manager.load(workflow_id)


def list_active_workflows(storage_dir: str = None) -> List[Dict[str, Any]]:
    """
    List all active (in_progress) workflows.

    Args:
        storage_dir: Storage directory for workflow files

    Returns:
        List of active workflow summaries
    """
    if storage_dir is None:
        storage_dir = ".claude/agent-memory/aria/workflows"

    manager = WorkflowState("", storage_dir)  # Type not needed for list
    return manager.list_workflows(status="in_progress")
