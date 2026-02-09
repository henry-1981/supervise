---
name: aria-knowledge
description: >
  Manage ARIA knowledge base including best practices, patterns, and lessons learned.
  Use this command to capture, retrieve, and apply accumulated knowledge from workflows.
  Enables continuous improvement through organizational learning.
parameters:
  - name: action
    description: Action to perform (capture, query, apply, list, update)
    required: true
  - name: topic
    description: Knowledge topic or category
    required: false
  - name: tags
    description: Knowledge tags for classification
    required: false
examples:
  - /aria knowledge query "test-driven development"
  - /aria knowledge capture --tags=loop-prevention,quality
  - /aria knowledge apply "authentication patterns"
  - /aria knowledge list --tags=best-practices
---

# ARIA Knowledge Command

## Purpose

The `/aria knowledge` command manages the organizational knowledge base, capturing insights from workflows and making them available for future tasks.

## When to Use

- Capturing lessons learned after task completion
- Searching for best practices before starting a task
- Applying proven patterns to current work
- Building organizational knowledge

## Knowledge Base Structure

```
.moai/knowledge/
├── patterns/                  # Design and implementation patterns
│   ├── authentication.md
│   ├── error-handling.md
│   └── state-management.md
├── best-practices/            # Best practice guides
│   ├── testing.md
│   ├── documentation.md
│   └── code-review.md
├── lessons-learned/           # Lessons from completed tasks
│   ├── loop-prevention.md
│   ├── quality-gates.md
│   └── refactoring-strategies.md
├── anti-patterns/             # Things to avoid
│   ├── common-mistakes.md
│   ├── performance-issues.md
│   └── security-pitfalls.md
└── context/                   # Domain-specific knowledge
    ├── web-development.md
    ├── api-design.md
    └── database-optimization.md
```

## Knowledge Schema

```yaml
id: {unique_identifier}
title: {Knowledge title}
category: {pattern|best-practice|lesson|anti-pattern}
tags: [{tag1}, {tag2}, {tag3}]
created: {timestamp}
updated: {timestamp}
author: {creator}
related: [{related_id1}, {related_id2}]

content: |
  {Markdown content}

examples:
  - description: {Example description}
    code: {Code example}
    outcome: {Result}

references:
  - {External reference 1}
  - {External reference 2}

metrics:
  usage_count: {number}
  success_rate: {percentage}
  last_applied: {timestamp}
```

## Knowledge Actions

### Capture Knowledge
```bash
/aria knowledge capture --tags=loop-prevention,quality
```
Captures insights from the current workflow or task.

Interactive capture mode:
```markdown
# Knowledge Capture

## Title
{Enter knowledge title}

## Category
[ ] Pattern
[ ] Best Practice
[ ] Lesson Learned
[ ] Anti-pattern

## Content
{Describe the knowledge in detail}

## Examples
{Provide concrete examples}

## Tags
{Add relevant tags for searchability}
```

### Query Knowledge
```bash
/aria knowledge query "test-driven development"
/aria knowledge query --tags=loop-prevention
/aria knowledge query --category=best-practice
```
Searches the knowledge base for relevant information.

Query types:
- **Text search**: Full-text search across all content
- **Tag search**: Find knowledge by tags
- **Category search**: Filter by knowledge category
- **Related search**: Find related knowledge items

### Apply Knowledge
```bash
/aria knowledge apply "authentication patterns"
```
Applies a knowledge pattern to the current task.

Application process:
1. Retrieves knowledge item
2. Validates applicability to current context
3. Generates implementation guidance
4. Tracks application for metrics

### List Knowledge
```bash
/aria knowledge list
/aria knowledge list --category=pattern
/aria knowledge list --tags=testing,quality
```
Lists available knowledge items with filtering options.

### Update Knowledge
```bash
/aria knowledge update {knowledge_id}
```
Updates an existing knowledge item with new insights.

## Knowledge Categories

### Patterns
Reusable solutions to common problems:
- **Design Patterns**: Architectural and design patterns
- **Implementation Patterns**: Coding patterns and idioms
- **Workflow Patterns**: Process and methodology patterns

### Best Practices
Proven approaches for quality outcomes:
- **Testing**: Test strategies and coverage
- **Documentation**: Documentation standards
- **Code Review**: Review practices
- **Quality Gates**: Quality validation approaches

### Lessons Learned
Insights from completed workflows:
- **Success Factors**: What led to success
- **Failure Analysis**: What went wrong
- **Recovery Strategies**: How issues were resolved
- **Optimization**: Performance and efficiency gains

### Anti-patterns
Common mistakes to avoid:
- **Code Smells**: Indicators of poor code
- **Process Issues**: Workflow problems
- **Quality Risks**: Common quality pitfalls
- **Security Issues**: Security vulnerabilities

## Knowledge Metrics

Track knowledge usage and effectiveness:

```yaml
metrics:
  total_items: {count}
  by_category:
    patterns: {count}
    best_practices: {count}
    lessons_learned: {count}
    anti_patterns: {count}
  most_used:
    - {item_id}: {usage_count}
  success_rates:
    {item_id}: {percentage}
  recent_updates:
    - {item_id}: {timestamp}
```

## Knowledge Relationships

Knowledge items can reference each other:

```yaml
related:
  - {related_item_id}
  - {related_item_id}

see_also:
  - {see_also_item_id}
  - {see_also_item_id}
```

## Knowledge Quality

Knowledge items are quality-rated:

```yaml
quality:
  accuracy: {1-5}
  relevance: {1-5}
  completeness: {1-5}
  clarity: {1-5}
  overall_score: {1-5}
```

## Auto-Capture from Workflows

Knowledge can be automatically captured:

```yaml
auto_capture:
  enabled: true
  triggers:
    - task_completion
    - loop_prevention_event
    - quality_gate_failure
    - user_initiated
  filters:
    - min_quality_score: 3
    - require_validation: true
```

## Integration

- Reads from: `.moai/knowledge/`, `.moai/execution/`
- Writes to: `.moai/knowledge/`
- Used by: All ARIA commands for context
- Output: Knowledge items and application results
