# Workflow: ARIA Team Execute - Parallel Regulatory Task Execution

Purpose: Execute complex regulatory tasks through parallel team-based execution. Used when regulatory tasks benefit from multi-domain parallel analysis.

Flow: TeamCreate -> Parallel Execution -> Quality Gates -> Result Synthesis -> Shutdown

## Prerequisites

- workflow.team.enabled: true
- CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
- Triggered by: /aria execute --team OR auto-detected multi-market/multi-domain tasks

## Phase 0: Team Setup

1. Read configuration:
   - supervise/.aria/config/sections/workflow.yaml for team settings
   - supervise/.aria/config/sections/quality.yaml for VALID framework

2. Create team:
   ```
   TeamCreate(team_name: "aria-execute-{task-slug}")
   ```

3. Create shared task list:
   ```
   TaskCreate: "Regulatory pathway analysis for Market A"
   TaskCreate: "Regulatory pathway analysis for Market B"
   TaskCreate: "Clinical evaluation requirements"
   TaskCreate: "Risk management strategy"
   TaskCreate: "Synthesize multi-domain results" (blocked by above tasks)
   ```

## Phase 1: Spawn Execution Team

Spawn domain-specific teammates based on task requirements. All spawns MUST use Task() with `team_name` and `name` parameters. Launch independent tasks in parallel:

### Multi-Market Submission Example

```
Task(
  subagent_type: "expert-regulatory",
  team_name: "aria-execute-multi-market",
  name: "regulatory-fda",
  mode: "default",
  prompt: "You are a regulatory expert on team aria-execute-multi-market.
    Analyze FDA 510(k) regulatory pathway for {device_description}.
    Research predicates, identify submission requirements, assess timeline.
    Apply VALID framework quality gates.
    When done, mark your task as completed via TaskUpdate and send findings to orchestrator via SendMessage."
)

Task(
  subagent_type: "expert-regulatory",
  team_name: "aria-execute-multi-market",
  name: "regulatory-eu",
  mode: "default",
  prompt: "You are a regulatory expert on team aria-execute-multi-market.
    Analyze EU MDR CE Mark pathway for {device_description}.
    Identify technical documentation requirements, notified body selection, conformity assessment.
    Apply VALID framework quality gates.
    When done, mark your task as completed via TaskUpdate and send findings to orchestrator via SendMessage."
)

Task(
  subagent_type: "expert-clinical",
  team_name: "aria-execute-multi-market",
  name: "clinical-evaluation",
  mode: "default",
  prompt: "You are a clinical expert on team aria-execute-multi-market.
    Define clinical evaluation strategy for {device_description}.
    Literature review requirements, clinical data needs, post-market surveillance.
    Apply VALID framework quality gates.
    When done, mark your task as completed via TaskUpdate and send findings to orchestrator via SendMessage."
)
```

All teammates run in parallel. Messages from teammates are delivered automatically to ARIA orchestrator.

## Phase 2: Parallel Execution

Teammates work independently on domain-specific tasks:
- regulatory-fda: FDA pathway (market-specific)
- regulatory-eu: EU MDR pathway (market-specific)
- clinical-evaluation: Clinical strategy (cross-market)

ARIA orchestrator monitors:
- Receive progress messages automatically
- Coordinate dependencies (e.g., clinical data needed by regulatory)
- Resolve regulatory ambiguities via AskUserQuestion

## Phase 3: VALID Quality Gates

Each teammate applies VALID framework before completion:
- **Verified**: Content matches source regulation text
- **Accurate**: Data and references are correct
- **Linked**: Traceability maintained
- **Inspectable**: Decision rationale documented
- **Deliverable**: Output meets submission format

orchestrator validates aggregate compliance.

## Phase 4: Result Synthesis

After all execution tasks complete:
1. Collect findings from all teammates
2. Synthesize unified regulatory strategy:
   - Market-specific pathways
   - Common technical documentation
   - Timeline and dependencies
   - Risk mitigation strategies
3. Format per Brief-Execute-Deliver output requirements

Output location: supervise/.aria/outputs/{task-id}/

## Phase 5: User Approval

AskUserQuestion with options:
- Approve strategy and proceed to documentation
- Request modifications (specify which market/domain)
- Request additional analysis
- Cancel workflow

## Phase 6: Cleanup

```
TeamDelete(team_name: "aria-execute-{task-slug}")
```

Execute /clear if token budget exceeded.

## Domain-Based File Ownership

ARIA teammates have clear domain boundaries to prevent file conflicts:

| Teammate | File Ownership | Read-Only Access |
|----------|---------------|------------------|
| expert-regulatory | Strategy docs (pathway-*.md) | All |
| expert-clinical | Clinical docs (CER-*.md, clinical-*.md) | All |
| expert-risk | Risk files (FMEA-*.md, hazard-*.md) | All |
| expert-submission | Submission packages (510k-*.md, CE-*.md) | All |
| expert-writer | Draft documents (draft-*.md) | All |

No overlap ensures safe parallel execution.

## Error Handling

If a teammate fails:
1. **Log Failure**: Document which task and domain failed
2. **Notify User**: Explain impact on overall strategy
3. **Propose Options**: Continue with partial results or retry failed domain
4. **Update Strategy**: Adjust based on available information

## Completion Markers

AI uses markers to signal task completion:
- `<aria>DONE</aria>` - Domain task complete
- `<aria>COMPLETE</aria>` - Full execution complete

## Example Use Cases

### Multi-Market Submission Strategy
- Teammates: expert-regulatory (FDA), expert-regulatory (EU), expert-regulatory (Korea)
- Parallel execution reduces turnaround from 3 days to 1 day

### Clinical + Risk Evaluation
- Teammates: expert-clinical, expert-risk
- Concurrent analysis identifies clinical-risk dependencies early

### Document Review + Compliance
- Teammates: expert-reviewer (technical), expert-reviewer (regulatory)
- Parallel review with different perspectives

---

Version: 1.0.0
Created: 2026-02-10
Author: Backend Developer (MoAI Team)
Framework: ARIA (Medical Device RA/QA)
