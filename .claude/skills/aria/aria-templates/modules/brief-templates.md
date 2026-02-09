# Brief Templates

## Overview

Standardized templates for the brief phase of ARIA workflow.

## Template Categories

### Default Brief Template

Standard template for general tasks:
- Overview and objectives
- Success criteria
- Constraints and dependencies
- Risk assessment

### Domain-Specific Templates

**Web Application**
- UI/UX requirements
- Frontend/backend considerations
- Deployment specifics

**API Development**
- Endpoint definitions
- Authentication requirements
- Documentation standards

**Refactoring**
- Current state analysis
- Target state definition
- Migration strategy

## Template Structure

```yaml
name: {template_name}
phase: brief
sections:
  - overview
  - objectives
  - success_criteria
  - constraints
  - dependencies
  - risks
variables:
  task_name: "{{task.name}}"
  scope: "{{task.scope}}"
  timestamp: "{{now()}}"
```

## Usage

1. Select appropriate template
2. Fill in variables
3. Customize sections as needed
4. Validate completeness
5. Save to briefs directory
