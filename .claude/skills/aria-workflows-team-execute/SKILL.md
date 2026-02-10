---
name: aria-workflows-team-execute
description: >
  ARIA Team Execute workflow for parallel regulatory task execution.
  Enables multi-market submissions, concurrent domain analysis, and parallel compliance checking
  using Claude Code Agent Teams API (TeamCreate, TeamDelete, SendMessage).
license: Apache-2.0
compatibility: Designed for Claude Code with CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-10"
  tags: "aria, team, parallel, regulatory, multi-market"
  framework: "aria"
  domain: "medical-device-ra-qa"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 3000

# MoAI Extension: Triggers
triggers:
  keywords: ["team", "parallel", "multi-market", "concurrent"]
  agents: ["aria-team-coordinator", "aria-orchestrator"]
  phases: ["execute"]
---

# ARIA Team Execute Workflow

For full workflow documentation, see:
- `supervise/.claude/skills/aria/workflows/team-execute.md`

## Quick Reference

### Team Creation
```
TeamCreate(team_name: "aria-execute-{task-slug}")
```

### Teammate Spawn
```
Task(
  subagent_type: "expert-{domain}",
  team_name: "aria-execute-{task-slug}",
  name: "{domain}-{specialization}",
  prompt: "You are {role} on team {...}. {task_description}..."
)
```

### Team Deletion
```
TeamDelete(team_name: "aria-execute-{task-slug}")
```

## VALID Framework Integration

All teammates must apply VALID quality gates:
- **V**erified: Content matches source regulations
- **A**ccurate: Data and references correct
- **L**inked: Traceability maintained
- **I**nspectable: Decision rationale documented
- **D**eliverable: Submission-ready format

## Domain Boundaries

| Expert Agent | File Ownership | Purpose |
|--------------|---------------|---------|
| expert-regulatory | pathway-*.md | Market-specific strategies |
| expert-clinical | CER-*.md, clinical-*.md | Clinical evaluation |
| expert-risk | FMEA-*.md, hazard-*.md | Risk management |
| expert-submission | 510k-*.md, CE-*.md | Submission packages |

## Use Cases

1. **Multi-Market Submissions**: FDA + EU + Korea in parallel
2. **Clinical + Risk**: Concurrent evaluation
3. **Document Review**: Parallel technical + regulatory review

---

Version: 1.0.0
Created: 2026-02-10
Framework: ARIA (Medical Device RA/QA)
