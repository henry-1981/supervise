---
name: aria-deliver
description: >
  Generate final deliverables including documentation, reports, and artifacts.
  Use this command after successful execution to package and present results.
  Creates comprehensive delivery package with all required outputs.
parameters:
  - name: task_id
    description: Task ID to deliver
    required: true
  - name: format
    description: Output format (markdown, pdf, html, all)
    required: false
  - name: include
    description: Additional artifacts (tests, docs, reports)
    required: false
examples:
  - /aria deliver TASK-001
  - /aria deliver TASK-002 --format=pdf
  - /aria deliver TASK-003 --include=tests,docs,reports
---

# ARIA Deliver Command

## Purpose

The `/aria deliver` command generates the final deliverable package, consolidating all outputs into a comprehensive delivery format.

## When to Use

- After `/aria execute` completes successfully
- All quality gates have passed
- Ready to package and present results
- Creating handoff artifacts

## Deliverable Package Structure

```
.aria/deliveries/{task_id}/
├── README.md                    # Delivery overview
├── summary.md                   # Executive summary
├── implementation/              # Implementation artifacts
│   ├── code/                    # Produced code
│   ├── tests/                   # Test files
│   └── configs/                 # Configuration changes
├── documentation/               # Generated documentation
│   ├── api/                     # API documentation
│   ├── user/                    # User guides
│   └── technical/               # Technical specs
├── reports/                     # Quality and execution reports
│   ├── execution_report.md      # Execution summary
│   ├── quality_report.md        # TRUST 5 validation
│   ├── coverage_report.md       # Coverage analysis
│   └── lsp_report.md            # LSP diagnostics
└── artifacts/                   # Additional artifacts
    ├── changelog.md             # Change log
    ├── migration_guide.md       # Migration notes
    └── rollout_plan.md          # Deployment plan
```

## Summary Template

```markdown
# Delivery Summary: {task_id}

## Overview
- **Task**: {task_name}
- **Delivered**: {timestamp}
- **Status**: {Success|Partial|Failed}
- **Duration**: {execution_time}

## Deliverables
| Artifact | Location | Format | Status |
|----------|----------|--------|--------|
| {name} | {path} | {format} | {status} |

## Implementation Summary
{Brief description of what was implemented}

## Quality Metrics
- **Test Coverage**: {percentage}%
- **Tests Passing**: {count}/{total}
- **LSP Status**: {clean|warnings|errors}
- **TRUST 5 Score**: {score}/5

## Changes
{Summary of changes made}

## Next Steps
1. {Recommended next action 1}
2. {Recommended next action 2}
3. {Recommended next action 3}

## Handoff Notes
{Additional context for recipients}
```

## Report Generation

### Execution Report
```markdown
# Execution Report: {task_id}

## Timeline
| Phase | Start | End | Duration | Status |
|-------|-------|-----|----------|--------|
| Brief | {start} | {end} | {duration} | {status} |
| Execute | {start} | {end} | {duration} | {status} |
| Deliver | {start} | {end} | {duration} | {status} |

## Steps Executed
{List of all execution steps with status}

## Loop Prevention
{Loop detection events and resolutions}

## Resource Usage
- **Total Tokens**: {count}
- **Peak Memory**: {amount}
- **Execution Time**: {duration}
```

### Quality Report (TRUST 5)
```markdown
# Quality Report: {task_id}

## TRUST 5 Validation

### Tested
- Unit Tests: {passing}/{total} ({percentage}%)
- Integration Tests: {passing}/{total} ({percentage}%)
- Coverage: {percentage}% (target: {target}%)

### Readable
- Naming Conventions: {status}
- Code Comments: {status}
- Documentation: {status}

### Understandable
- Code Complexity: {score}
- Modularity: {score}
- Design Patterns: {status}

### Secured
- Security Scan: {status}
- Input Validation: {status}
- OWASP Compliance: {status}

### Trackable
- Commits: {count} with conventional messages
- Issue References: {status}
- Change Log: {status}

## Overall Score: {score}/5
```

## Format Options

### Markdown (default)
- Human-readable format
- Direct file access
- Version control friendly

### PDF
- Professional presentation
- Fixed formatting
- Best for: External sharing

### HTML
- Interactive navigation
- Web-ready format
- Best for: Documentation sites

### All
- Generate all formats
- Maximum flexibility
- Larger output size

## Validation Before Delivery

```bash
# Pre-delivery validation checklist
aria-validate --task-id={task_id} --delivery

# Checks:
- [ ] All quality gates passed
- [ ] Documentation complete
- [ ] Tests passing
- [ ] Artifacts generated
- [ ] Change log updated
```

## Integration

- Reads from: `.aria/briefs/`, `.aria/execution/`
- Writes to: `.aria/deliveries/`
- Requires: Completed execution phase
- Outputs: Multi-format deliverable package
