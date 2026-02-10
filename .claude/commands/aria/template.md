---
name: aria-template
description: >
  Manage ARIA workflow templates for brief, execution, and delivery phases.
  Use this command to create, update, list, or apply workflow templates.
  Templates standardize workflows and ensure consistency across tasks.
parameters:
  - name: action
    description: Action to perform (create, list, apply, update, delete)
    required: true
  - name: template
    description: Template name or identifier
    required: false
  - name: phase
    description: Phase to apply template to (brief, execute, deliver)
    required: false
examples:
  - /aria template list
  - /aria template create custom-workflow --phase=execute
  - /aria template apply web-app --phase=brief
  - /aria template update api-workflow --phase=execute
---

# ARIA Template Command

## Purpose

The `/aria template` command manages workflow templates that standardize ARIA processes across different task types and domains.

## When to Use

- Creating reusable workflow patterns
- Standardizing team workflows
- Onboarding new team members
- Ensuring consistency across projects

## Template Structure

```
.aria/templates/
├── brief/
│   ├── default.md           # Default brief template
│   ├── web-app.md           # Web application template
│   ├── api.md               # API development template
│   └── refactoring.md       # Refactoring template
├── execute/
│   ├── default.md           # Default execution template
│   ├── tdd.md               # TDD workflow template
│   ├── ddd.md               # DDD workflow template
│   └── hybrid.md            # Hybrid workflow template
└── deliver/
    ├── default.md           # Default delivery template
    ├── open-source.md       # Open source delivery template
    └── enterprise.md        # Enterprise delivery template
```

## Template Schema

### Brief Template
```yaml
name: {template_name}
description: {Template description}
phase: brief
sections:
  - name: overview
    required: true
    template: |
      # Task Brief: {{task_name}}
      ## Overview
      - **Task ID**: {{task_id}}
      - **Scope**: {{scope}}
  - name: success_criteria
    required: true
    template: |
      ## Success Criteria
      {{success_criteria_list}}
  - name: constraints
    required: false
    template: |
      ## Constraints
      {{constraints_list}}
```

### Execute Template
```yaml
name: {template_name}
description: {Template description}
phase: execute
workflow:
  mode: {sequential|parallel|hybrid}
  steps:
    - name: {step_name}
      required: true
      validation:
        - tests_pass
        - lsp_clean
      dependencies: []
    - name: {step_name}
      required: true
      validation:
        - coverage_met
      dependencies: [{previous_step}]
  quality_gates:
    test_coverage: 85
    lsp_errors: 0
    max_warnings: 10
```

### Deliver Template
```yaml
name: {template_name}
description: {Template description}
phase: deliver
artifacts:
  - name: summary
    format: markdown
    required: true
    template: templates/deliver/summary.md
  - name: quality_report
    format: markdown
    required: true
    template: templates/deliver/quality.md
  - name: documentation
    format: {html|pdf}
    required: false
    template: templates/deliver/docs.md
```

## Template Actions

### Create Template
```bash
/aria template create my-workflow --phase=execute
```
Creates a new template from the default schema with customizations.

### List Templates
```bash
/aria template list
/aria template list --phase=brief
```
Lists available templates, optionally filtered by phase.

### Apply Template
```bash
/aria template apply web-app --phase=brief
```
Applies a template to the current task phase.

### Update Template
```bash
/aria template update api-workflow --phase=execute
```
Updates an existing template with current workflow configuration.

### Delete Template
```bash
/aria template delete old-workflow
```
Removes a template from the library.

## Built-in Templates

### Brief Templates
- **default**: General-purpose brief template
- **web-app**: Web application development
- **api**: API development and integration
- **refactoring**: Code refactoring tasks
- **feature**: New feature implementation
- **bugfix**: Bug fixing workflow

### Execute Templates
- **default**: Standard sequential execution
- **tdd**: Test-driven development workflow
- **ddd**: Domain-driven development workflow
- **hybrid**: Hybrid TDD/DDD workflow
- **parallel**: Parallel execution for independent tasks
- **fast-track**: Accelerated workflow for simple tasks

### Deliver Templates
- **default**: Standard delivery package
- **open-source**: Open source project delivery
- **enterprise**: Enterprise delivery with compliance
- **internal**: Internal team delivery
- **client**: Client-facing delivery package

## Template Variables

Templates support variable substitution:

```yaml
variables:
  task_name: "{{task.name}}"
  task_id: "{{task.id}}"
  timestamp: "{{datetime.now()}}"
  user: "{{user.name}}"
  project: "{{project.name}}"
```

## Template Validation

Templates are validated before use:

```bash
# Validate template syntax
aria-template validate my-template

# Test template application
aria-template test my-template --phase=execute

# Check template completeness
aria-template check my-template
```

## Template Inheritance

Templates can extend base templates:

```yaml
extends: default
overrides:
  workflow:
    mode: parallel
  quality_gates:
    test_coverage: 90
```

## Integration

- Reads from: `.aria/templates/`
- Writes to: `.aria/templates/`, `.aria/briefs/`, `.aria/execution/`
- Used by: All ARIA commands
- Output: Template application results
