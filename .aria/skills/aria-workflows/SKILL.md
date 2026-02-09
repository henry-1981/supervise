---
name: aria-workflows
description: >
  Integrated workflow skills for ARIA medical device RA/QA system supporting
  510(k) preparation and audit response with Agent Teams mode and sequential
  fallback. Implements SPEC-ARIA-005 Milestone 2 requirements.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Task TeamCreate TeamDelete SendMessage TaskCreate TaskUpdate TaskList TaskGet Read Grep Glob Bash AskUserQuestion
user-invocable: true
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2025-02-09"
  modularized: "false"
  tags: "aria, 510k, audit, capa, medical-device, regulatory"
  argument-hint: "Specify workflow type: 510k or audit"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 8000

# MoAI Extension: Triggers
triggers:
  keywords: ["aria", "510k", "fda", "audit", "capa", "submission", "regulatory"]
  agents: ["aria-teams-integrator"]
  phases: ["plan", "run"]
---

# ARIA Workflows

Medical device RA/QA workflow system with Agent Teams support.

## Workflow Types

### 1. 510(k) Preparation Workflow

**Purpose**: Prepare FDA 510(k) submission for medical device clearance

**Input**: Device description and intended use

**Output**: Complete 510(k) submission package

**Complexity Threshold**: 5+ sections triggers team mode

### 2. Audit Response Workflow

**Purpose**: Respond to FDA/ISO audit findings with CAPA

**Input**: Audit observations or findings

**Output**: Complete CAPA documentation

**Complexity Threshold**: 3+ findings triggers team mode

## Execution Mode Selection

```
┌─────────────────────────────────────────────────────┐
│              MODE SELECTION LOGIC                    │
├─────────────────────────────────────────────────────┤
│ 1. Check CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS env   │
│    ├─ Not set → Sequential mode                     │
│    └─ Set → Continue to step 2                      │
│                                                      │
│ 2. Check complexity threshold                        │
│    ├─ Below threshold → Sequential mode             │
│    └─ At/Above threshold → Team mode                │
│                                                      │
│ 3. Attempt TeamCreate                               │
│    ├─ Success → Team mode execution                 │
│    └─ Failure → Fallback to sequential              │
└─────────────────────────────────────────────────────┘
```

## 510(k) Workflow

### Sequential Mode (Simple submissions)

```
┌──────────────────────────────────────────────────────┐
│ 510(k) SEQUENTIAL WORKFLOW                          │
├──────────────────────────────────────────────────────┤
│                                                      │
│ Step 1: FDA Research                                 │
│   └─ manager-spec → Research FDA requirements        │
│                                                      │
│ Step 2: Predicate Analysis                           │
│   └─ expert-backend → Analyze predicates            │
│                                                      │
│ Step 3: Substantial Equivalence                      │
│   └─ expert-backend → Document equivalence          │
│                                                      │
│ Step 4: Submission Drafting                          │
│   └─ manager-docs → Draft sections                  │
│                                                      │
│ Step 5: Quality Review                               │
│   └─ manager-quality → Review and validate          │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Team Mode (Complex submissions, 5+ sections)

```
┌──────────────────────────────────────────────────────┐
│ 510(k) TEAM WORKFLOW                                │
├──────────────────────────────────────────────────────┤
│                                                      │
│ PHASE 1: RESEARCH (Parallel)                         │
│   ├─ fda-researcher (haiku)                         │
│   │  └─ FDA guidance & predicates                   │
│   └─ predicate-analyst (sonnet)                      │
│      └─ Initial comparison planning                  │
│                                                      │
│ PHASE 2: ANALYSIS                                    │
│   └─ predicate-analyst (sonnet)                      │
│      ├─ Substantial equivalence                      │
│      └─ Comparison matrix                            │
│                                                      │
│ PHASE 3: DRAFTING                                    │
│   └─ submission-writer (sonnet)                      │
│      ├─ Cover letter                                 │
│      ├─ Device description                           │
│      ├─ Substantial equivalence                      │
│      ├─ Conformity to standards                      │
│      └─ Labeling                                     │
│                                                      │
│ PHASE 4: QUALITY REVIEW                              │
│   └─ manager-quality (sub-agent)                     │
│      └─ TRUST 5 validation                           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Task Decomposition (510(k))

```python
tasks = [
    {
        "id": "research-fda-guidance",
        "subject": "Research FDA 510(k) guidance documents",
        "assignee": "fda-researcher",
        "priority": "high",
        "output": ".aria/research/fda-guidance.md"
    },
    {
        "id": "identify-predicates",
        "subject": "Identify applicable predicate devices",
        "assignee": "fda-researcher",
        "priority": "high",
        "depends_on": ["research-fda-guidance"],
        "output": ".aria/research/predicates.md"
    },
    {
        "id": "analyze-equivalence",
        "subject": "Analyze substantial equivalence to predicates",
        "assignee": "predicate-analyst",
        "priority": "high",
        "depends_on": ["identify-predicates"],
        "output": ".aria/analysis/equivalence.md"
    },
    {
        "id": "create-comparison-matrix",
        "subject": "Create device comparison matrix",
        "assignee": "predicate-analyst",
        "priority": "medium",
        "depends_on": ["analyze-equivalence"],
        "output": ".aria/analysis/comparison-matrix.md"
    },
    {
        "id": "draft-cover-letter",
        "subject": "Draft 510(k) cover letter",
        "assignee": "submission-writer",
        "priority": "medium",
        "depends_on": ["create-comparison-matrix"],
        "output": ".aria/submissions/cover-letter.md"
    },
    {
        "id": "draft-device-description",
        "subject": "Draft device description section",
        "assignee": "submission-writer",
        "priority": "high",
        "depends_on": ["analyze-equivalence"],
        "output": ".aria/submissions/device-description.md"
    },
    {
        "id": "draft-comparisons",
        "subject": "Draft substantial equivalence comparison",
        "assignee": "submission-writer",
        "priority": "high",
        "depends_on": ["create-comparison-matrix"],
        "output": ".aria/submissions/comparison.md"
    },
    {
        "id": "draft-conformity",
        "subject": "Draft conformity to standards section",
        "assignee": "submission-writer",
        "priority": "medium",
        "depends_on": ["analyze-equivalence"],
        "output": ".aria/submissions/conformity.md"
    }
]
```

## Audit Response Workflow

### Sequential Mode (Single findings)

```
┌──────────────────────────────────────────────────────┐
│ AUDIT SEQUENTIAL WORKFLOW                           │
├──────────────────────────────────────────────────────┤
│                                                      │
│ Step 1: Finding Analysis                             │
│   └─ manager-spec → Analyze observation             │
│                                                      │
│ Step 2: Root Cause                                   │
│   └─ expert-debug → Root cause analysis             │
│                                                      │
│ Step 3: CAPA Planning                                │
│   └─ manager-spec → Plan CAPA                       │
│                                                      │
│ Step 4: Implementation                                │
│   └─ expert-debug → Implement CAPA                  │
│                                                      │
│ Step 5: Effectiveness Check                           │
│   └─ manager-quality → Verify effectiveness         │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Team Mode (Multiple findings, 3+)

```
┌──────────────────────────────────────────────────────┐
│ AUDIT TEAM WORKFLOW                                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│ PHASE 1: INVESTIGATION (Parallel)                    │
│   ├─ audit-researcher (haiku)                       │
│   │  ├─ Observation analysis                        │
│   │  └─ Regulatory requirements                     │
│   └─ capa-analyst (sonnet)                           │
│      └─ Initial CAPA approach                       │
│                                                      │
│ PHASE 2: ROOT CAUSE                                  │
│   └─ capa-expert (sonnet)                            │
│      ├─ 5-Whys / Fishbone analysis                  │
│      └─ Root cause verification                      │
│                                                      │
│ PHASE 3: CAPA PLANNING                               │
│   └─ capa-analyst (sonnet)                           │
│      ├─ Corrective action design                     │
│      └─ Preventive action design                     │
│                                                      │
│ PHASE 4: IMPLEMENTATION                              │
│   └─ capa-expert (sonnet)                            │
│      ├─ Implement corrections                        │
│      ├─ Implement corrective actions                 │
│      ├─ Implement preventive actions                 │
│      └─ Document all actions                         │
│                                                      │
│ PHASE 5: EFFECTIVENESS                               │
│   └─ capa-expert (sonnet)                            │
│      └─ Verify CAPA effectiveness                   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Task Decomposition (Audit)

```python
tasks = [
    {
        "id": "analyze-finding",
        "subject": "Analyze audit observation details",
        "assignee": "audit-researcher",
        "priority": "high",
        "output": ".aria/findings/analysis.md"
    },
    {
        "id": "research-regulations",
        "subject": "Research applicable regulatory requirements",
        "assignee": "audit-researcher",
        "priority": "high",
        "depends_on": ["analyze-finding"],
        "output": ".aria/findings/regulations.md"
    },
    {
        "id": "identify-standards",
        "subject": "Identify relevant FDA/ISO standards",
        "assignee": "audit-researcher",
        "priority": "medium",
        "depends_on": ["analyze-finding"],
        "output": ".aria/findings/standards.md"
    },
    {
        "id": "plan-root-cause",
        "subject": "Plan root cause analysis approach",
        "assignee": "capa-analyst",
        "priority": "high",
        "depends_on": ["research-regulations"],
        "output": ".aria/root-cause/plan.md"
    },
    {
        "id": "conduct-root-cause",
        "subject": "Conduct root cause analysis",
        "assignee": "capa-expert",
        "priority": "high",
        "depends_on": ["plan-root-cause"],
        "output": ".aria/root-cause/analysis.md"
    },
    {
        "id": "design-corrective",
        "subject": "Design corrective actions",
        "assignee": "capa-analyst",
        "priority": "high",
        "depends_on": ["conduct-root-cause"],
        "output": ".aria/capa/corrective.md"
    },
    {
        "id": "design-preventive",
        "subject": "Design preventive measures",
        "assignee": "capa-analyst",
        "priority": "high",
        "depends_on": ["conduct-root-cause"],
        "output": ".aria/capa/preventive.md"
    },
    {
        "id": "document-capa",
        "subject": "Document CAPA plan and implementation",
        "assignee": "capa-expert",
        "priority": "high",
        "depends_on": ["design-corrective", "design-preventive"],
        "output": ".aria/capa/record.md"
    },
    {
        "id": "verify-effectiveness",
        "subject": "Verify effectiveness of corrective actions",
        "assignee": "capa-expert",
        "priority": "medium",
        "depends_on": ["document-capa"],
        "output": ".aria/capa/effectiveness.md"
    }
]
```

## Fallback Implementation

### Fallback Function

```python
def execute_workflow(workflow_type, input_data):
    """Execute ARIA workflow with automatic fallback"""

    # Step 1: Determine mode
    team_mode, reason = should_use_team_mode(workflow_type, input_data)

    if team_mode:
        # Step 2: Attempt team creation
        try:
            return execute_team_workflow(workflow_type, input_data)
        except TeamCreationError as e:
            log_warning(f"Team mode failed: {e}. Falling back to sequential.")
            return execute_sequential_workflow(workflow_type, input_data)
        except TeammateCrashError as e:
            log_warning(f"Teammate crash: {e}. Falling back to sequential.")
            return execute_sequential_workflow(workflow_type, input_data)
    else:
        # Sequential mode
        log_info(f"Using sequential mode: {reason}")
        return execute_sequential_workflow(workflow_type, input_data)
```

### Resume Point Tracking

```python
def get_resume_point(workflow_type):
    """Get last completed task for resume capability"""

    checkpoint_file = f".aria/checkpoints/{workflow_type}-progress.json"

    if os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            data = json.load(f)
            return data.get("last_completed_task")

    return None

def save_checkpoint(workflow_type, task_id):
    """Save progress for potential resume"""

    checkpoint_file = f".aria/checkpoints/{workflow_type}-progress.json"
    os.makedirs(os.path.dirname(checkpoint_file), exist_ok=True)

    with open(checkpoint_file, "w") as f:
        json.dump({"last_completed_task": task_id}, f)
```

## Quality Gates

### 510(k) Quality Gates

```python
def validate_510k_submission():
    """Validate 510(k) submission completeness"""

    checks = {
        "sections_complete": check_all_sections_present(),
        "e_copy_format_compliant": check_ecopy_format(),
        "references_cited": check_references_complete(),
        "consistency_check": check_cross_references()
    }

    return all(checks.values()), checks
```

### Audit Quality Gates

```python
def validate_capa():
    """Validate CAPA completeness"""

    checks = {
        "root_cause_identified": check_root_cause(),
        "corrective_action_defined": check_corrective_action(),
        "preventive_action_defined": check_preventive_action(),
        "effectiveness_check_planned": check_effectiveness_plan(),
        "timeline_established": check_timeline(),
        "documentation_complete": check_documentation()
    }

    return all(checks.values()), checks
```

## Usage Examples

### Example 1: Simple 510(k) (Sequential)

```
User: Prepare a 510(k) submission for a new blood pressure monitor

System:
- Analyzing complexity: 3 sections needed
- Below threshold (5), using sequential mode
- Executing: manager-spec → expert-backend → manager-docs
- Complete: Submission package in .aria/submissions/
```

### Example 2: Complex 510(k) (Team)

```
User: Prepare a 510(k) submission for a new AI-based diagnostic

System:
- Analyzing complexity: 8 sections needed
- Above threshold (5), attempting team mode
- Team created: aria-510k-ai-diagnostic
- Spawning 3 teammates in parallel...
- Progress: FDA research [100%], Analysis [60%], Drafting [0%]
- Complete: Submission package in .aria/submissions/
- Shutdown: All teammates closed
```

### Example 3: Audit Response (Team)

```
User: Respond to FDA 483 with 5 observations

System:
- Analyzing complexity: 5 findings
- Above threshold (3), attempting team mode
- Team created: aria-audit-response-2025Q1
- Spawning 3 teammates in parallel...
- Complete: All CAPAs documented in .aria/capa/
- Shutdown: All teammates closed
```

---

Version: 1.0.0
Last Updated: 2025-02-09
SPEC: SPEC-ARIA-005 Milestone 2
