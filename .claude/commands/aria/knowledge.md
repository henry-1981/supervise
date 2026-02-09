---
name: aria-knowledge
description: >
  ARIA knowledge base query command with Context7 fallback - Query Notion Knowledge Base
  for regulatory best practices, patterns, and lessons learned. Falls back to Context7 MCP
  for up-to-date regulatory documents when local knowledge is insufficient. Auto-saves new
  knowledge items with source attribution (per SPEC-ARIA-004 ER-014, ER-015, UR-010).
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "2.1.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, knowledge, context7, fallback, best-practices, auto-save, source-attribution"
  argument-hint: "\"query\" [--context7-fallback] [--save] [--list]"
---

# ARIA Knowledge Command

## Purpose

Query Notion Knowledge Base for regulatory best practices, patterns, and lessons learned. Automatically falls back to Context7 MCP for up-to-date regulatory documents when local knowledge is insufficient, with auto-save functionality (SPEC-ARIA-004 ER-014, ER-015).

## Usage

```
/aria knowledge "510(k) substantial equivalence"
/aria knowledge "ISO 14971 risk analysis" --context7-fallback
/aria knowledge "design validation" --save
/aria knowledge list --category best-practices
```

## Knowledge Base Structure

```
.moai/knowledge/
├── patterns/                  # Design and implementation patterns
│   ├── regulatory-submission.md
│   ├── risk-assessment.md
│   └── validation-strategy.md
├── best-practices/            # Best practice guides
│   ├── documentation.md
│   ├── audit-preparation.md
│   └── capa-management.md
├── lessons-learned/           # Lessons from completed workflows
│   ├── submission-delays.md
│   ├── nb-audit-findings.md
│   └── validation-failures.md
├── anti-patterns/             # Things to avoid
│   ├── common-mistakes.md
│   ├── compliance-issues.md
│   └── documentation-gaps.md
└── context/                   # Domain-specific knowledge
    ├── fda-regulations.md
    ├── eu-mdr-requirements.md
    └── iso-standards.md
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

regulatory_references:
  - standard: "ISO 13485"
    section: "8.5.2"
    version: "2016"
  - standard: "21 CFR 820"
    section: "820.30"
    version: "current"

examples:
  - description: {Example description}
    scenario: {Real-world scenario}
    outcome: {Result}

metrics:
  usage_count: {number}
  success_rate: {percentage}
  last_applied: {timestamp}
```

## Query Process

### Step 1: Local Knowledge Search

Search local knowledge base first:

```
Input: "510(k) substantial equivalence criteria"

Search Process:
1. Full-text search across .moai/knowledge/
2. Semantic similarity scoring
3. Filter by category, tags
4. Rank by relevance and recency
```

### Step 2: Context7 Fallback (SPEC-ARIA-004 ER-015)

If local knowledge is insufficient (< 70% relevance or no results):

```
Fallback Trigger:
  - No local results found
  - Best relevance score < 70%
  - User explicitly requests --context7-fallback

Context7 Query (per SPEC-ARIA-004 ER-015):
  1. mcp__context7__resolve-library-id("fda-21-cfr-820")
  2. mcp__context7__get-library-docs(topic="510(k) substantial equivalence")
  3. Extract relevant sections with source citation
  4. Auto-save to Notion Knowledge Base with KB- prefix
  5. Notify user of new knowledge item
```

### Step 3: Result Integration

Combine local knowledge and Context7 results:

```markdown
## Knowledge Results: "510(k) substantial equivalence criteria"

### Local Knowledge (3 results)

1. **[PAT-012] 510(k) Predicate Device Selection** (Relevance: 92%)
   - Category: Pattern
   - Summary: Systematic approach to predicate device identification
   - Tags: [510k, predicate-device, substantial-equivalence]
   - Usage: Applied 15 times, 87% success rate

### Context7 Results (2 new items)

2. **[KB-NEW-001] 21 CFR 807.85 - Substantial Equivalence Criteria** (Context7)
   - Source: FDA 21 CFR 820 via Context7
   - Summary: Regulatory requirements for demonstrating substantial equivalence
   - Action: Auto-saved to Knowledge Base
   - Link: [View in Knowledge Base](https://notion.so/kb-new-001)

3. **[KB-NEW-002] FDA 510(k) Guidance - Substantial Equivalence** (Context7)
   - Source: FDA Guidance via Context7
   - Summary: Practical guidance on substantial equivalence determination
   - Action: Auto-saved to Knowledge Base
   - Link: [View in Knowledge Base](https://notion.so/kb-new-002)
```

## Knowledge Categories

### Patterns

Reusable solutions to common regulatory challenges:

- **Submission Patterns**: 510(k), PMA, CE marking workflows
- **Risk Assessment Patterns**: ISO 14971 implementation strategies
- **Validation Patterns**: Design verification and validation approaches
- **Documentation Patterns**: Regulatory document structures

### Best Practices

Proven approaches for quality outcomes:

- **CAPA Management**: Effective CAPA lifecycle management
- **Audit Preparation**: NB audit and FDA inspection preparation
- **Documentation**: Regulatory documentation standards
- **Submission Strategy**: Multi-market submission strategies

### Lessons Learned

Insights from completed regulatory workflows:

- **Success Factors**: What led to successful submissions
- **Failure Analysis**: Root causes of submissions failures
- **Recovery Strategies**: How issues were resolved
- **Optimization**: Process efficiency improvements

### Anti-patterns

Common mistakes to avoid:

- **Compliance Risks**: Regulatory violations and consequences
- **Documentation Issues**: Common documentation problems
- **Process Failures**: Workflow breakdown scenarios
- **Audit Findings**: Typical non-conformities

## Command Options

### Basic Query

```
/aria knowledge "510(k) submission requirements"
```

### Context7 Fallback

```
/aria knowledge "MDR classification rules" --context7-fallback
```

Automatically queries Context7 if local knowledge is insufficient.

### Save Results

```
/aria knowledge "design control requirements" --save
```

Saves query results to a new knowledge item.

### List Knowledge

```
/aria knowledge list
/aria knowledge list --category pattern
/aria knowledge list --tags 510k,submission
```

Lists available knowledge items with filtering.

### Apply Knowledge

```
/aria knowledge apply "risk assessment pattern"
```

Applies a knowledge pattern to current workflow.

## Auto-Save from Context7 (SPEC-ARIA-004 ER-015, UR-010)

When Context7 fallback is triggered:

```yaml
Conditions for Auto-Save (per SPEC-ARIA-004 ER-015):
  - Relevance score >= 75%
  - Content not in Notion Knowledge Base
  - Source is authoritative regulatory document

Auto-Save Process (per SPEC-ARIA-004 UR-010):
  1. Generate KB-NEW-XXX identifier
  2. Create knowledge item in Notion Knowledge Base DB
  3. Save with Context7 content and source citation
  4. Tag with "context7", "auto-imported"
  5. Set TTL: 30 days (per SPEC-ARIA-004 UR-005)
  6. Notify user of new knowledge item

Notification:
  "New knowledge item added from Context7:
   KB-NEW-001: 21 CFR 807.85 - Substantial Equivalence Criteria
   Source: FDA 21 CFR 820 via Context7
   View: /aria knowledge KB-NEW-001"
```

## Knowledge Quality Metrics

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
  context7_imports:
    total: {count}
    this_month: {count}
  success_rates:
    {item_id}: {percentage}
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

regulatory_hierarchy:
  parent: {parent_standard_id}
  children: [{child_standard_id1}, {child_standard_id2}]
```

## Usage Examples

### Example 1: Query with Fallback

```
/aria knowledge "EU MDR classification rules" --context7-fallback

Results:
1. Local: [PAT-025] MDR Classification Flowchart (85% relevance)
2. Context7: [KB-NEW-003] EU MDR Annex IX Classification Rules (new)

Action: KB-NEW-003 auto-saved to Knowledge Base
```

### Example 2: Best Practice Query

```
/aria knowledge "CAPA effectiveness verification"

Results:
- [BP-008] CAPA Effectiveness Check Methodology (92% relevance)
- Applied 23 times, 91% success rate
- Related to ISO 13485 Clause 8.5.2
```

### Example 3: Lesson Learned

```
/aria knowledge "510(k) submission delays"

Results:
- [LL-015] Common 510(k) Submission Delay Causes
- Lessons: Early predicate device search, complete testing package
- Related patterns: [PAT-012] Predicate Device Selection
```

### Example 4: Pattern Application

```
/aria knowledge apply "design validation strategy"

Applied:
- Pattern: PAT-018
- Steps: 9-step design validation process
- Checklist: 42 validation items
- Success rate: 88%
```

## Error Handling

### No Knowledge Found

```
Knowledge Query: No results found for "xyz abc"

Suggestions:
1. Try broader search terms
2. Enable Context7 fallback with --context7-fallback
3. Request knowledge capture from expert
```

### Context7 Unavailable

```
Warning: Context7 MCP unavailable for fallback query

Resolution:
1. Check .mcp.json configuration
2. Verify Context7 API key
3. Proceed with local knowledge only
```

### Invalid Knowledge ID

```
Error: Knowledge item KB-XXX not found

Available items:
- KB-001: 510(k) Submission Process
- KB-002: Risk Assessment Guide

Use /aria knowledge list to see all available items.
```

## Completion Marker

Add `<aria:knowledge:complete results=N context7=M>` marker when query completes. (N: local results, M: Context7 results)

## Notes

- Knowledge base is stored in .moai/knowledge/ for version control
- Context7 fallback is automatic when relevance < 70% or explicitly requested
- Auto-saved items from Context7 are tagged for tracking
- Knowledge usage metrics track effectiveness and guide improvements
- All knowledge queries are logged to Audit Log for compliance

---

**Version:** 2.1.0 (Phase 4 - SPEC-ARIA-004 Milestone 5)
**Last Updated:** 2026-02-09
**Language:** English
**Core Principle:** Notion Knowledge Base query with intelligent Context7 fallback for comprehensive coverage
**Spec Compliance:** SPEC-ARIA-004 ER-014, ER-015, UR-010
