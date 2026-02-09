---
name: aria-brief
description: >
  Analyze and understand task requirements, define scope, and create structured brief.
  Use this command when starting a new task to clarify objectives, identify constraints,
  and establish success criteria before execution.
parameters:
  - name: task
    description: Task description or identifier to brief
    required: true
  - name: scope
    description: Scope definition (narrow, medium, broad)
    required: false
examples:
  - /aria brief "Implement authentication system"
  - /aria brief "Refactor payment module" --scope=narrow
  - /aria brief SPEC-001
---

# ARIA Brief Command

## Purpose

The `/aria brief` command initiates the task understanding phase by analyzing requirements, defining scope, and creating a structured brief document.

## When to Use

- Starting a new task or feature implementation
- Beginning a refactoring effort
- Analyzing requirements from a SPEC document
- Clarifying ambiguous user requests

## Brief Template

```markdown
# Task Brief: {task_name}

## Overview
- **Task ID**: {auto-generated}
- **Created**: {timestamp}
- **Status**: Briefing
- **Scope**: {narrow|medium|broad}

## Objective
{Clear statement of what needs to be accomplished}

## Context
{Background information, relevant system context}

## Success Criteria
1. {Measurable criterion 1}
2. {Measurable criterion 2}
3. {Measurable criterion 3}

## Constraints
- **Technical**: {Technical limitations}
- **Time**: {Time constraints if any}
- **Resources**: {Resource limitations}

## Dependencies
- {External dependencies}
- {Prerequisite tasks}
- {Required resources}

## Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {risk} | {high|medium|low} | {high|medium|low} | {strategy} |

## Next Steps
1. [ ] Validate brief with stakeholder
2. [ ] Proceed to execution planning
3. [ ] Allocate resources
```

## Execution Flow

1. **Input Analysis**: Parse task description and scope parameters
2. **Context Gathering**: Read relevant SPEC documents, codebase context
3. **Brief Generation**: Create structured brief using template
4. **Validation**: Check for completeness and clarity
5. **Output**: Save brief to `.moai/briefs/{task_id}.md`

## Quality Gates

- [ ] Objective is clear and measurable
- [ ] Success criteria are specific
- [ ] Dependencies are identified
- [ ] Risks are assessed
- [ ] Scope is well-defined

## Integration

- Reads from: `.moai/specs/`, `.claude/rules/`
- Writes to: `.moai/briefs/`
- Triggers: `/aria execute` command
