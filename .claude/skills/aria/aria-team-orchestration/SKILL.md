---
name: aria-team-orchestration
description: >
  Team coordination system for ARIA enabling parallel execution of multiple regulatory agents.
  Provides task decomposition, dependency resolution, parallel execution management, and result
  synthesis using ARIA's Brief-Execute-Deliver workflow and VALID quality framework.
license: Apache-2.0
compatibility: Designed for ARIA (supervise/.claude/)
allowed-tools: Task TaskCreate TaskUpdate TaskList TaskGet AskUserQuestion Read Grep Glob Bash
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-10"
  modularized: "true"
  tags: "team-orchestration, parallel-execution, regulatory, multi-market"
  author: "ARIA Team"
  context: "SPEC-DEPS-001 Phase 6: Team Mode Reimplementation"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 150
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords: ["multi-market", "parallel", "team coordination", "simultaneous", "concurrent"]
  agents: ["aria-team-coordinator", "orchestrator"]
  phases: ["execute"]
---

# ARIA Team Orchestration

Team coordination system for ARIA enabling parallel execution of multiple regulatory agents for complex multi-market, multi-document, or multi-disciplinary tasks.

## Team Coordination State Machine

### State Definition

```yaml
aria_team_state:
  session_id: string
  parent_request: string
  status: "planning" | "executing" | "synthesizing" | "completed" | "failed"

  subtasks:
    - subtask_id: string
      description: string
      assigned_agent: string
      status: "pending" | "in_progress" | "completed" | "failed"
      dependencies: [string]  # IDs of tasks this depends on
      output_location: string
      started_at: timestamp
      completed_at: timestamp

  synthesis:
    status: "pending" | "in_progress" | "completed"
    template: string
    output_location: string

  quality_gates:
    valid_verified: boolean
    all_subtasks_completed: boolean
    user_approval: boolean

  created_at: timestamp
  updated_at: timestamp
```

### State Transitions

```
planning → executing: Task decomposition complete, execution ready
executing → synthesizing: All subtasks completed
synthesizing → completed: Result synthesis complete, quality gates passed
executing → failed: Critical subtask failure
any → completed: User requested early completion with available results
```

## Task Decomposition

### Decomposition Principles

1. **Domain Independence**: Tasks in different regulatory domains can run in parallel
2. **File Non-Overlap**: Agents with different file ownership can write simultaneously
3. **Dependency Awareness**: Tasks with dependencies must execute sequentially

### Decomposition Algorithm

```python
# Pseudocode for task decomposition

def decompose_request(request):
    """Break complex request into independent subtasks"""

    # Step 1: Identify natural subtasks
    subtasks = identify_subtasks(request)

    # Step 2: Check independence
    for subtask in subtasks:
        subtask.independent = check_file_overlap(subtask)

    # Step 3: Identify dependencies
    dependencies = identify_dependencies(subtasks)

    # Step 4: Assign agents
    for subtask in subtasks:
        subtask.agent = select_aria_agent(subtask.domain)

    # Step 5: Build execution waves
    waves = build_execution_waves(subtasks, dependencies)

    return waves

def build_execution_waves(subtasks, dependencies):
    """Group subtasks into waves based on dependencies"""

    waves = []
    remaining = subtasks.copy()

    while remaining:
        # Find tasks with no pending dependencies
        ready = [t for t in remaining if all_dependencies_completed(t)]

        if not ready:
            raise CircularDependencyError()

        waves.append(ready)
        mark_as_completed(ready)
        remaining = [t for t in remaining if t not in ready]

    return waves
```

### Common Decomposition Patterns

#### Pattern 1: Multi-Market Regulatory Research

**Request**: "Analyze regulatory requirements for FDA, EU MDR, and Korea MFDS"

```yaml
subtasks:
  - subtask_id: "fda-analysis"
    description: "FDA 21 CFR Part 820 requirements analysis"
    assigned_agent: "expert-regulatory"
    domain: "US FDA"
    dependencies: []

  - subtask_id: "eu-analysis"
    description: "EU MDR 2017/745 requirements analysis"
    assigned_agent: "expert-regulatory"
    domain: "EU MDR"
    dependencies: []

  - subtask_id: "korea-analysis"
    description: "Korea MFDS requirements analysis"
    assigned_agent: "expert-regulatory"
    domain: "Korea MFDS"
    dependencies: []

  - subtask_id: "synthesis"
    description: "Consolidated multi-market requirements document"
    assigned_agent: "aria-team-coordinator"
    dependencies: ["fda-analysis", "eu-analysis", "korea-analysis"]

execution_waves:
  - wave_1: ["fda-analysis", "eu-analysis", "korea-analysis"]  # Parallel
  - wave_2: ["synthesis"]  # After all analyses complete
```

#### Pattern 2: Clinical Evaluation Report

**Request**: "Prepare Clinical Evaluation Report for orthopedic implant"

```yaml
subtasks:
  - subtask_id: "literature-search"
    description: "Systematic literature search for clinical evidence"
    assigned_agent: "expert-researcher"
    dependencies: []

  - subtask_id: "clinical-data"
    description: "Clinical data analysis and interpretation"
    assigned_agent: "expert-clinical"
    dependencies: []

  - subtask_id: "predicate-analysis"
    description: "Predicate device analysis for substantial equivalence"
    assigned_agent: "expert-analyst"
    dependencies: []

  - subtask_id: "risk-assessment"
    description: "Risk assessment integration for clinical evaluation"
    assigned_agent: "expert-risk"
    dependencies: ["clinical-data"]

  - subtask_id: "cer-drafting"
    description: "CER document drafting with all annexes"
    assigned_agent: "expert-writer"
    dependencies: ["literature-search", "predicate-analysis", "risk-assessment"]

  - subtask_id: "compliance-check"
    description: "Regulatory compliance verification"
    assigned_agent: "expert-regulatory"
    dependencies: ["cer-drafting"]

execution_waves:
  - wave_1: ["literature-search", "clinical-data", "predicate-analysis"]  # Parallel research
  - wave_2: ["risk-assessment"]  # Needs clinical data
  - wave_3: ["cer-drafting"]  # Needs all research
  - wave_4: ["compliance-check"]  # Can review draft in parallel with wave_3
```

## Parallel Execution Management

### Execution Wave Protocol

```python
# Pseudocode for parallel execution

def execute_parallel_waves(waves):
    """Execute task waves in dependency order"""

    for wave_num, wave in enumerate(waves, 1):
        logger.info(f"Executing Wave {wave_num}: {len(wave)} tasks")

        # Execute all tasks in current wave in parallel
        results = execute_in_parallel(wave)

        # Update task states
        for result in results:
            update_subtask_state(result)

        # Check for failures
        failed_tasks = [r for r in results if r.status == "failed"]

        if failed_tasks:
            handle_wave_failures(failed_tasks)
            # Decide: continue with partial results or abort

    return collect_all_results()

def execute_in_parallel(tasks):
    """Execute independent tasks in parallel via Task tool"""

    # Launch all tasks via parallel Task calls
    task_calls = [
        Task(subagent_type=task.agent, prompt=task.prompt)
        for task in tasks
    ]

    # Wait for all to complete
    results = wait_for_all(task_calls)

    return results
```

### Progress Tracking

Use TaskCreate/TaskUpdate/TaskList for state management:

```python
# Create tasks
for subtask in subtasks:
    TaskCreate(
        subject=subtask.description,
        description=subtask.full_spec,
        activeForm=f"Executing {subtask.subtask_id}"
    )

# Monitor progress
while any_in_progress():
    status = TaskList()
    update_team_state(status)

# Mark completion
for subtask in completed_subtasks:
    TaskUpdate(taskId=subtask.id, status="completed")
```

## Result Synthesis

### Synthesis Template

```yaml
synthesis_template:
  multi_market_strategy:
    sections:
      - title: "Executive Summary"
        source: "synthesis"
      - title: "FDA 510(k) Strategy"
        source: "fda-analysis"
      - title: "EU MDR CE Mark Strategy"
        source: "eu-analysis"
      - title: "Korea MFDS Strategy"
        source: "korea-analysis"
      - title: "Unified Timeline"
        source: "synthesis"

  clinical_evaluation:
    sections:
      - title: "Executive Summary"
        source: "synthesis"
      - title: "Literature Search Results"
        source: "literature-search"
      - title: "Clinical Data Analysis"
        source: "clinical-data"
      - title: "Predicate Device Analysis"
        source: "predicate-analysis"
      - title: "Risk Assessment Summary"
        source: "risk-assessment"
      - title: "CER Main Document"
        source: "cer-drafting"
      - title: "Compliance Verification"
        source: "compliance-check"
```

### VALID Framework Integration

Ensure synthesized outputs meet all VALID dimensions:

| Dimension | Verification | Synthesis Check |
|-----------|-------------|------------------|
| **V**erified | Source regulation cross-reference | All claims cite source regulations |
| **A**ccurate | Data and reference validation | Cross-check data across subtasks |
| **L**inked | Traceability matrix | Document inter-references maintained |
| **I**nspectable | Audit trail completeness | All decisions documented with rationale |
| **D**eliverable | Template conformance | Output matches required format |

## Quality Gates

### Pre-Execution Gates

- [ ] All subtasks have assigned agents
- [ ] Dependencies correctly identified
- [ ] No circular dependencies
- [ ] File ownership boundaries verified

### During Execution Gates

- [ ] All tasks in wave started
- [ ] Progress tracking active
- [ ] Failures detected and handled

### Post-Synthesis Gates

- [ ] All subtasks completed
- [ ] Results collected and validated
- [ ] Synthesis template applied
- [ ] VALID framework compliance verified
- [ ] User approval obtained

## Usage Examples

### Example 1: Multi-Market Submission Strategy

**Input**:
```
"Create submission strategy for orthopedic implant device targeting:
- US FDA 510(k) pathway
- EU MDR CE Mark
- Korea MFDS approval"
```

**Team Coordinator Processing**:
1. Decompose into 5 subtasks (3 market analysis + device analysis + synthesis)
2. Execute 3 market analyses in parallel (Wave 1)
3. Execute device analysis (Wave 2)
4. Execute synthesis (Wave 3)
5. Generate unified strategy document

**Output**: Single document with all three market strategies plus unified timeline

### Example 2: Concurrent Audit Preparation

**Input**:
```
"Prepare for ISO 13485 internal audit:
- Conduct gap analysis
- Prepare documentation
- Train staff"
```

**Team Coordinator Processing**:
1. Decompose into parallel tasks:
   - Gap analysis (expert-analyst)
   - Documentation review (expert-reviewer)
   - Training material prep (expert-writer)
2. Execute all in parallel (no dependencies)
3. Synthesize into audit readiness report

## Error Handling

### Subtask Failure Strategy

```python
def handle_subtask_failure(failed_task, context):
    """Decide how to handle task failure"""

    # Check if task is critical
    if failed_task.critical:
        # Stop execution, notify user
        notify_user(f"Critical task {failed_task.id} failed")
        request_decision(continue_with_partial=True)

    # Check if partial results acceptable
    if context.can_proceed_partial:
        # Mark alternative strategy
        log_warning(f"Task {failed_task.id} failed, using partial results")
        adjust_synthesis_template(exclude=failed_task.id)

    # Otherwise, retry task
    else:
        retry_task(failed_task)
```

### Recovery Options

Present user with options when failures occur:

1. **Continue with Partial Results**: Use available data, note gaps
2. **Retry Failed Task**: Attempt execution again with modified parameters
3. **Skip Dependency**: Proceed without failed subtask output
4. **Abort Execution**: Stop and request user guidance

## Configuration

### Team Coordinator Settings

```yaml
# In aria-team-coordinator agent

max_parallel_tasks: 5      # Maximum concurrent tasks
task_timeout: 300          # Per-task timeout in seconds
wave_timeout: 600          # Maximum wave execution time
retry_attempts: 1           # Number of retries for failed tasks
quality_check: true         # Enable VALID framework verification
user_approval: true         # Require approval before synthesis
```

---

## Modules

- **task-decomposition**: Algorithms for breaking down complex requests
- **parallel-execution**: Wave-based parallel task execution
- **dependency-resolution**: Dependency graph management
- **result-synthesis**: Multi-agent output consolidation
