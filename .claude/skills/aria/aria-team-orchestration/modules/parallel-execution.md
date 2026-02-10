# Parallel Execution Module

Manages wave-based parallel execution of independent regulatory tasks with progress tracking and failure handling.

## Wave-Based Execution Model

Tasks are grouped into "waves" where:
- All tasks in a wave execute in parallel
- Waves execute sequentially (Wave N+1 starts after Wave N completes)
- This respects dependencies while maximizing parallelism

### Wave Structure

```yaml
execution_waves:
  - wave_id: 1
    tasks: [task_1, task_2, task_3]    # Execute in parallel
    status: "pending"
    started_at: null
    completed_at: null

  - wave_id: 2
    tasks: [task_4]                   # Execute after wave 1
    status: "pending"
    started_at: null
    completed_at: null
```

## Execution Protocol

### Phase 1: Wave Initialization

```python
def initialize_wave(wave):
    """Prepare wave for execution"""

    # Create task tracking
    for subtask in wave.tasks:
        TaskCreate(
            subject=subtask.description,
            description=subtask.full_spec,
            activeForm=f"Executing {subtask.subtask_id}"
        )

    # Mark wave as in-progress
    wave.status = "in_progress"
    wave.started_at = current_timestamp()

    return wave
```

### Phase 2: Parallel Task Launch

```python
def launch_wave_parallel(wave):
    """Launch all tasks in wave via parallel Task calls"""

    # Build parallel Task invocations
    task_invocations = []

    for subtask in wave.tasks:
        # Build prompt for agent
        prompt = build_agent_prompt(subtask)

        # Create Task invocation
        task_invocations.append({
            "tool": "Task",
            "subagent_type": subtask.assigned_agent,
            "prompt": prompt,
            "description": f"Execute {subtask.subtask_id}"
        })

    # Execute all tasks in parallel
    # (Claude Code automatically runs parallel Task calls)
    results = execute_parallel_tasks(task_invocations)

    return results
```

### Phase 3: Progress Monitoring

```python
def monitor_wave_progress(wave):
    """Monitor task execution in current wave"""

    while wave_not_complete(wave):
        # Check task status via TaskList
        task_status = TaskList()

        # Update individual task states
        for subtask in wave.tasks:
            task_info = task_status[subtask.id]
            update_subtask_state(subtask, task_info)

        # Check for failures
        failed_tasks = [t for t in wave.tasks if t.status == "failed"]

        if failed_tasks:
            handle_failures(failed_tasks)

        # Check for completions
        if all_tasks_completed(wave):
            wave.status = "completed"
            wave.completed_at = current_timestamp()

        # Wait before next check (avoid busy polling)
        await asyncio.sleep(5)
```

## Parallel Execution Constraints

### Maximum Concurrent Tasks

```yaml
team_coordinator:
  max_parallel_tasks: 5     # Maximum agents running simultaneously
  per_agent_timeout: 300    # Timeout per task in seconds
  wave_timeout: 600        # Timeout for entire wave
```

### Resource Management

When `max_parallel_tasks` is limited:

1. **Priority Queue**: Tasks prioritized by criticality
2. **Wave Subdivision**: Large waves split into smaller sub-waves
3. **Agent Pooling**: Reuse agents across waves (not applicable for ARIA)

### File Write Safety

ARIA agents have non-overlapping file ownership, but additional safety:

```python
def verify_file_safety(tasks):
    """Verify no file write conflicts between parallel tasks"""

    file_owners = {}
    for task in tasks:
        for file in task.output_files:
            if file in file_owners:
                raise ConflictError(f"File {file} claimed by {file_owners[file]} and {task.agent}")
            file_owners[file] = task.agent

    return True  # No conflicts
```

## Failure Handling

### Task Failure Detection

```python
def detect_task_failure(task_result):
    """Determine if a task failed"""

    # Check exit code
    if task_result.exit_code != 0:
        return True, "process_error"

    # Check for error markers in output
    if "ERROR" in task_result.output or "FAILED" in task_result.output:
        return True, "content_error"

    # Check for incomplete output
    if not task_has_required_outputs(task_result):
        return True, "incomplete_output"

    return False, None
```

### Failure Recovery Strategies

#### Strategy 1: Retry Task

```yaml
retry_config:
  max_attempts: 2
  backoff: "exponential"
  retry_on:
    - "process_error"
    - "timeout_error"
```

#### Strategy 2: Continue with Partial Results

```yaml
partial_results:
  allowed: true
  require_user_approval: true
  exclude_failed: true
```

#### Strategy 3: Abort Execution

```yaml
abort_on_failure:
  critical_tasks: true
  user_notification: true
```

## Progress Reporting

### Wave Status Summary

```yaml
wave_status:
  wave_id: 1
  total_tasks: 3
  completed: 2
  failed: 0
  in_progress: 1
  pending: 0
  progress_percent: 67

tasks:
  - subtask_id: "fda-analysis"
    status: "completed"
    duration: "5 min"

  - subtask_id: "eu-analysis"
    status: "completed"
    duration: "7 min"

  - subtask_id: "korea-analysis"
    status: "in_progress"
    elapsed: "3 min"
```

### User Notifications

Significant events trigger user notifications:

1. **Wave Started**: "Starting Wave 1: 3 parallel tasks"
2. **Task Completed**: "FDA analysis complete (5 min)"
3. **Task Failed**: "EU analysis failed: [error details]"
4. **Wave Completed**: "Wave 1 complete: 2/3 tasks succeeded"
5. **Synthesis Started**: "Synthesizing results from completed tasks"
