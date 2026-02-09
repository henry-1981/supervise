---
name: aria-team-coordination
description: >
  Team coordination and management for ARIA medical device RA/QA workflows.
  Handles team creation, task board sharing, teammate spawning, and graceful
  shutdown with fallback to sequential execution for 510(k) and audit workflows.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Task TeamCreate TeamDelete SendMessage TaskCreate TaskUpdate TaskList TaskGet Read Grep Glob Bash
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2025-02-09"
  modularized: "false"
  tags: "team, coordination, aria, medical-device, 510k, audit, capa"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 6000

# MoAI Extension: Triggers
triggers:
  keywords: ["510k", "audit", "capa", "aria", "medical-device", "regulatory"]
  agents: ["aria-teams-integrator"]
  phases: ["plan", "run"]
---

# ARIA Team Coordination

## Overview

This skill manages Agent Teams coordination for ARIA medical device RA/QA workflows, supporting 510(k) preparation and audit response scenarios with automatic fallback to sequential execution.

## Prerequisites

Agent Teams requires:
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.json env
- Claude Code v2.1.32 or later
- ARIA team configuration files in `.aria/teams/`

## Team Configurations

### 510(k) Preparation Team

**File**: `.aria/teams/team-510k-preparation.json`

**Teammates**:
- `fda-researcher` (haiku): FDA requirements research
- `predicate-analyst` (sonnet): Substantial equivalence analysis
- `submission-writer` (sonnet): eCopy template drafting

**Activation Threshold**: 5+ submission sections

**Workflow Phases**:
1. Research: FDA guidance and predicate device identification (parallel)
2. Analysis: Substantial equivalence assessment
3. Drafting: Submission section creation

### Audit Response Team

**File**: `.aria/teams/team-audit-response.json`

**Teammates**:
- `audit-researcher` (haiku): Audit finding analysis
- `capa-analyst` (sonnet): CAPA planning
- `capa-expert` (sonnet): Root cause and implementation

**Activation Threshold**: 3+ audit findings

**Workflow Phases**:
1. Investigation: Finding analysis (parallel)
2. Root Cause: Detailed analysis
3. CAPA Planning: Corrective and preventive action design
4. Implementation: CAPA execution and documentation

## Team Creation

### Activation Check

Before creating team, verify:

```python
# Pseudo-code for activation check
def should_activate_team_mode(workflow_type, complexity_score):
    # Check environment variable
    if not env.get("CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"):
        return False, "Agent Teams not enabled"

    # Check complexity threshold
    if workflow_type == "510k":
        threshold = load_team_config("team-510k-preparation")["complexity_threshold"]["min_sections"]
        return complexity_score >= threshold, f"Need {threshold}+ sections"

    if workflow_type == "audit":
        threshold = load_team_config("team-audit-response")["complexity_threshold"]["min_findings"]
        return complexity_score >= threshold, f"Need {threshold}+ findings"

    return False, "Unknown workflow type"
```

### Team Creation Pattern

```markdown
# 510(k) Team Creation Example

## Step 1: Load Team Configuration
```bash
cat .aria/teams/team-510k-preparation.json
```

## Step 2: Create Team
TeamCreate(team_name: "aria-510k-{submission-id}")

## Step 3: Create Shared Task Board
Load tasks from team config["workflow"]["task_board"]["shared_tasks"]
Create each task via TaskCreate with dependencies

## Step 4: Spawn Teammates
For each teammate in config["teammates"]:
  Task(
    subagent_type: teammate["agent_type"],
    team_name: "aria-510k-{submission-id}",
    name: teammate["name"],
    mode: teammate["permissions"]["mode"],
    prompt: assign_based_on_role(teammate)
  )
```

## Task Board Management

### Shared Task Creation

```python
# Create tasks from team config
config = load_team_config(team_id)
for task_spec in config["workflow"]["task_board"]["shared_tasks"]:
    TaskCreate(
        subject=task_spec["subject"],
        description=f"Assigned to {task_spec['assignee']}",
        metadata={
            "assignee": task_spec["assignee"],
            "priority": task_spec["priority"]
        }
    )
    if task_spec.get("depends_on"):
        TaskUpdate(
            taskId=task_id,
            addBlockedBy=task_spec["depends_on"]
        )
```

### Task Claiming

Teammates claim tasks by:
1. Reading TaskList for assigned tasks
2. Updating task status to in_progress
3. Marking completed when done

```python
# Teammate task claiming pattern
def claim_assigned_tasks(assignee_name):
    tasks = TaskList()
    my_tasks = [t for t in tasks if t.metadata.get("assignee") == assignee_name]

    for task in my_tasks:
        if task.status == "pending" and not task.blockedBy:
            TaskUpdate(taskId=task.id, status="in_progress")
            # Work on task...
            TaskUpdate(taskId=task.id, status="completed")
```

## Escalation Paths

### Escalation Triggers

When escalation conditions are met:

1. **Identify Escalation Type**
   ```python
   escalation = next(
       e for e in team_config["escalation_paths"]
       if matches_condition(e["condition"])
   )
   ```

2. **Notify Team Lead**
   ```python
   SendMessage(
       type="message",
       recipient="team-lead",
       content=f"Escalation: {escalation['condition']}",
       summary=f"Request {escalation['escalate_to']} intervention"
   )
   ```

3. **Request Expert Input**
   - Cross-functional: clinical-reviewer
   - Regulatory: regulatory-affairs
   - Technical: engineering-lead
   - Critical: crisis-management

## Completion Detection

### Phase Markers

Each phase completes when:

**510(k) Research Phase**:
- research-fda-guidance: completed
- identify-predicates: completed

**510(k) Analysis Phase**:
- analyze-equivalence: completed
- create-comparison-matrix: completed

**510(k) Drafting Phase**:
- All drafting tasks: completed

**Audit Investigation Phase**:
- analyze-finding: completed
- research-regulations: completed
- identify-standards: completed

**Audit Root Cause Phase**:
- conduct-root-cause: completed

**Audit CAPA Phase**:
- design-corrective: completed
- design-preventive: completed
- document-capa: completed
- verify-effectiveness: completed

### Quality Gates

Before phase transition, verify:

**510(k) Quality Gates**:
- sections_complete: All required sections drafted
- e_copy_format_compliant: eCopy template followed
- references_cited: All references properly cited
- consistency_check: Cross-references validated

**Audit Quality Gates**:
- root_cause_identified: True root cause, not symptom
- corrective_action_defined: Systemic change planned
- preventive_action_defined: Extension to similar issues
- effectiveness_check_planned: Verifiable metrics defined
- timeline_established: Realistic implementation schedule
- documentation_complete: Full audit trail

## Shutdown Sequence

### Graceful Shutdown

```python
def shutdown_team(team_name, teammates):
    # Step 1: Verify all tasks complete
    tasks = TaskList()
    pending = [t for t in tasks if t.status != "completed"]
    if pending:
        raise Exception(f"Tasks pending: {pending}")

    # Step 2: Send shutdown requests
    for teammate in teammates:
        SendMessage(
            type="shutdown_request",
            recipient=teammate["name"],
            content="Team workflow complete, shutting down"
        )

    # Step 3: Wait for approvals (timeout 60s)
    # System automatically processes responses

    # Step 4: Delete team
    TeamDelete()
```

## Fallback Strategy

### Fallback Triggers

Fallback to sequential execution when:
- TeamCreate fails (API unavailable)
- Teammate crashes repeatedly
- Environment variable not set
- Token limit approaching

### Fallback Execution

```python
def fallback_to_sequential(team_config, last_point):
    """Fall back to sequential agent execution"""

    # Map teammates to fallback agents
    agent_map = {
        "fda-researcher": "manager-spec",
        "predicate-analyst": "expert-backend",
        "submission-writer": "manager-docs",
        "audit-researcher": "manager-spec",
        "capa-analyst": "expert-debug",
        "capa-expert": "manager-quality"
    }

    # Resume from last completed task
    for task in team_config["workflow"]["task_board"]["shared_tasks"]:
        if task["id"] == last_point:
            continue  # Resume after this task

        # Execute with fallback agent
        fallback_agent = agent_map.get(
            task["assignee"],
            "manager-spec"
        )
        Task(
            subagent_type=fallback_agent,
            prompt=f"Execute task: {task['subject']}"
        )
```

### Fallback Configuration

```json
{
  "fallback_strategy": {
    "enabled": true,
    "mode": "sequential",
    "fallback_agents": [
      "manager-spec",
      "expert-backend",
      "manager-docs"
    ],
    "resume_point": "last_completed_task"
  }
}
```

## Coordination Messages

### Research Complete

```python
SendMessage(
    type="message",
    recipient="predicate-analyst",
    content="FDA research complete. Predicate devices identified:\n1. K123456 - Device A\n2. K789012 - Device B",
    summary="Research findings for analysis"
)
```

### Analysis Ready

```python
SendMessage(
    type="message",
    recipient="submission-writer",
    content="Substantial equivalence analysis complete. Comparison matrix available.",
    summary="Analysis ready for drafting"
)
```

### Drafting Complete

```python
SendMessage(
    type="message",
    recipient="team-lead",
    content="All submission sections drafted. Ready for review.",
    summary="Drafting complete"
)
```

## Error Recovery

### Teammate Crash

```python
def handle_teammate_crash(crashed_teammate, team_config):
    # Find teammate config
    config = next(
        t for t in team_config["teammates"]
        if t["name"] == crashed_teammate
    )

    # Spawn replacement
    Task(
        subagent_type=config["agent_type"],
        team_name=team_name,
        name=f"{config['name']}-replacement",
        mode=config["permissions"]["mode"],
        prompt=f"Resume work of {crashed_teammate}. Context: {get_task_context()}"
    )
```

### Task Stuck

```python
def handle_stuck_task(task_id, team_config):
    # Reassign to different teammate
    TaskUpdate(
        taskId=task_id,
        metadata={"reassign": True}
    )
    # Notify team lead for manual intervention
```

---

Version: 1.0.0
Last Updated: 2025-02-09
