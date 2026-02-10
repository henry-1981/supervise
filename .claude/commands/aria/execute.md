---
name: aria-execute
description: >
  Execute workflow for a briefed task with systematic implementation.
  Use this command to run the implementation phase after briefing is complete.
  Manages the execution loop with progress tracking and quality validation.
parameters:
  - name: task_id
    description: Task ID from brief phase
    required: true
  - name: mode
    description: Execution mode (sequential, parallel, hybrid)
    required: false
  - name: continue
    description: Continue from previous execution state
    required: false
examples:
  - /aria execute TASK-001
  - /aria execute TASK-002 --mode=parallel
  - /aria execute TASK-003 --continue
---

# ARIA Execute Command

## Purpose

The `/aria execute` command manages the implementation workflow, coordinating execution steps, tracking progress, and ensuring quality standards are met.

## When to Use

- After `/aria brief` is completed and validated
- Ready to begin implementation
- Continuing from paused execution
- Running automated workflow loops

## Execution Phases

### Phase 1: Preparation
```bash
# Load brief and validate prerequisites
aria-validate --task-id={task_id}

# Create execution workspace
mkdir -p .aria/execution/{task_id}

# Capture baseline state
aria-baseline --capture=lsp,tests,coverage
```

### Phase 2: Execution Loop
```python
while not task_complete:
    # Step planning
    plan_next_step(current_state, brief)

    # Execution
    implement_step(step_plan)

    # Validation
    validate_step(
        tests_pass=True,
        lsp_clean=True,
        coverage_met=True
    )

    # Progress update
    update_progress(step, status)

    # Loop prevention check
    if loops_detected(current_state):
        apply_recovery_strategy()
```

### Phase 3: Completion
```bash
# Final validation
aria-validate --task-id={task_id} --final

# Generate execution report
aria-report --task-id={task_id}

# Transition to deliver phase
aria-deliver --task-id={task_id}
```

## Progress Tracking

```markdown
# Execution Status: {task_id}

## Progress: 65%
┌────────────────────────────────────────┐
│ Preparation  │ ████████████████████ │ 100% │
│ Execution    │ ██████████░░░░░░░░░░ │  65% │
│ Validation   │ ░░░░░░░░░░░░░░░░░░░░ │   0% │
└────────────────────────────────────────┘

## Active Step
**Current**: Implementing user authentication
**Status**: In Progress
**Started**: 2025-02-09 14:30:00
**ETA**: 2025-02-09 16:00:00

## Quality Metrics
- Tests Passing: 42/45 (93%)
- LSP Errors: 0
- Coverage: 78% (target: 85%)
- Loops Detected: 0

## Recent Steps
- [x] Setup project structure
- [x] Implement data models
- [ ] Implement authentication logic ← Current
- [ ] Add API endpoints
- [ ] Write integration tests
```

## Loop Prevention

### Detection Mechanisms
1. **State Comparison**: Compare current state with previous iterations
2. **Error Pattern**: Detect repeated error messages
3. **Fix Attempts**: Track duplicate fix attempts
4. **Progress Stagnation**: No progress for N iterations

### Recovery Strategies
```python
recovery_strategies = {
    "error_repeat": "Alternative approach",
    "progress_stagnant": "Break down task",
    "fix_repeat": "Request user intervention",
    "max_iterations": "Preserve state and pause"
}
```

## Quality Gates

Each execution step must pass:

1. **Test Gate**: All unit tests pass
2. **LSP Gate**: Zero errors, zero type errors
3. **Coverage Gate**: Meet coverage target (default 85%)
4. **Build Gate**: Clean build with no warnings

## Execution Modes

### Sequential Mode
- Execute steps one at a time
- Maximum validation between steps
- Best for: Complex, interdependent tasks

### Parallel Mode
- Execute independent steps in parallel
- Requires clear step dependencies
- Best for: Well-defined, independent tasks

### Hybrid Mode
- Auto-select sequential vs parallel per step
- Balances speed and safety
- Best for: Mixed complexity tasks

## Integration

- Reads from: `.aria/briefs/`, `.aria/specs/`
- Writes to: `.aria/execution/`, `.aria/reports/`
- Triggers: `/aria deliver` on completion
- Uses: LSP quality gates, test runners
