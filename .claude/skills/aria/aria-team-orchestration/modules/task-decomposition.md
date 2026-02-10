# Task Decomposition Module

Algorithms and patterns for breaking complex regulatory requests into independent subtasks suitable for parallel execution.

## Decomposition Principles

### 1. Domain Independence Principle

Tasks in different regulatory domains can execute in parallel because they:
- Operate on different regulations (FDA vs EU MDR vs Korea MFDS)
- Work with different document types
- Use different expert knowledge bases
- Write to different output files

**Example**: FDA analysis and EU analysis can run simultaneously

### 2. File Non-Overlap Principle

ARIA agents have clear file ownership boundaries:

| Agent | File Ownership | No Overlap With |
|--------|---------------|------------------|
| expert-writer | *.docx, templates | expert-analyst (reports) |
| expert-analyst | Analysis reports | expert-regulatory (strategy docs) |
| expert-regulatory | Strategy documents | expert-risk (risk files) |
| expert-risk | Risk files | expert-clinical (clinical docs) |

**Result**: These agents can write simultaneously without conflicts.

### 3. Dependency Awareness Principle

Some tasks naturally depend on others:

- Synthesis tasks depend on analysis tasks
- Risk assessment may depend on clinical data
- Compliance checks depend on document drafts

These must execute sequentially.

## Decomposition Algorithm

```python
def decompose_regulatory_request(request):
    """
    Decompose a complex regulatory request into parallel subtasks

    Args:
        request: User's natural language request

    Returns:
        execution_plan: Ordered list of execution waves
    """

    # Step 1: Parse request for key phrases
    keywords = extract_keywords(request)

    # Step 2: Identify task types
    task_types = classify_task_type(keywords)

    # Step 3: Extract subtasks
    subtasks = extract_subtasks(request, task_types)

    # Step 4: Check independence
    for subtask in subtasks:
        subtask.independent = check_file_overlap(subtask)

    # Step 5: Identify dependencies
    dependencies = identify_dependencies(subtasks)

    # Step 6: Assign agents
    for subtask in subtasks:
        subtask.agent = select_aria_agent(subtask.domain, subtask.task_type)

    # Step 7: Build execution waves
    waves = build_execution_waves(subtasks, dependencies)

    # Step 8: Create synthesis task
    synthesis_task = create_synthesis_task(subtasks)
    waves.append([synthesis_task])

    return waves
```

## Common Request Patterns

### Pattern 1: Multi-Market Analysis

**Triggers**: "multi-market", "FDA and EU", "global strategy", "US, Europe, Asia"

**Template**:
```yaml
subtasks:
  - market: "FDA"
    agent: "expert-regulatory"
    focus: "US requirements"

  - market: "EU MDR"
    agent: "expert-regulatory"
    focus: "European requirements"

  - market: "Korea MFDS"
    agent: "expert-regulatory"
    focus: "Korean requirements"

  - synthesis: true
    agent: "aria-team-coordinator"
    depends_on: ["FDA", "EU MDR", "Korea MFDS"]
```

### Pattern 2: Document Package Preparation

**Triggers**: "submission package", "prepare documents", "complete CER"

**Template**:
```yaml
subtasks:
  - task: "literature_review"
    agent: "expert-researcher"
    output: "literature_review.md"

  - task: "clinical_data"
    agent: "expert-clinical"
    output: "clinical_data.md"

  - task: "risk_assessment"
    agent: "expert-risk"
    output: "risk_analysis.md"

  - task: "main_document"
    agent: "expert-writer"
    depends_on: ["literature_review", "clinical_data", "risk_assessment"]

  - task: "compliance_review"
    agent: "expert-reviewer"
    depends_on: ["main_document"]
```

### Pattern 3: Gap Analysis + Action Plan

**Triggers**: "gap analysis", "compliance check", "audit preparation"

**Template**:
```yaml
subtasks:
  - task: "requirements_extraction"
    agent: "expert-analyst"
    output: "applicable_requirements.md"

  - task: "current_state_assessment"
    agent: "expert-audit"
    output: "current_state.md"

  - task: "gap_identification"
    agent: "expert-analyst"
    depends_on: ["requirements_extraction", "current_state_assessment"]
    output: "gap_analysis.md"

  - task: "action_plan"
    agent: "expert-regulatory"
    depends_on: ["gap_identification"]
    output: "action_plan.md"
```

## Task Specification Format

Each subtask must have:

```yaml
subtask_spec:
  subtask_id: string           # Unique identifier
  description: string           # Human-readable description
  assigned_agent: string        # ARIA agent name
  domain: string                # Regulatory domain
  task_type: string            # Type of regulatory task
  dependencies: [string]        # List of subtask_ids this depends on
  input_requirements: []        # Required inputs
  expected_output: string       # Output file/description
  estimated_duration: integer   # Minutes
  critical: boolean             # Whether overall success depends on this
```

## Decomposition Quality Checks

### Check 1: Completeness

- [ ] All user requirements covered by subtasks
- [ ] No orphaned requirements
- [ ] Deliverable clearly specified

### Check 2: Independence

- [ ] Parallel tasks have no file overlap
- [ ] Parallel tasks have no data dependencies
- [ ] Agent capabilities match task requirements

### Check 3: Dependencies

- [ ] All dependencies are necessary
- [ ] No circular dependencies
- [ ] Dependency graph is acyclic

### Check 4: Agent Availability

- [ ] All required agents exist in ARIA
- [ ] Agent capabilities match task needs
- [ ] No agent overloaded by too many tasks
