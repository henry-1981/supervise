---
name: aria-writing-style
description: >
  Technical document writing style guide for medical device regulatory documentation.
  Provides terminology consistency standards and sentence structure guidelines
  for professional regulatory documents.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA
user-invocable: false
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, regulatory, writing, documentation, style-guide"
  author: "MoAI-ADK Team"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 200
  level2_tokens: 2000

# MoAI Extension: Triggers
triggers:
  keywords: ["writing", "document", "style", "terminology", "regulatory"]
  agents: ["expert-writer", "expert-reviewer", "manager-docs"]
  phases: ["execute", "deliver"]
---

# ARIA Writing Style Guide

Technical document writing standards for medical device regulatory documentation.

## Quick Reference

### Core Principles

**Clarity**
- Use active voice
- Avoid ambiguous pronouns
- One idea per sentence

**Precision**
- Use defined terminology consistently
- Cite specific regulation sections
- Include version numbers for standards

**Professional Tone**
- Formal but accessible
- Objective language
- Evidence-based statements

### Common Terminology

| Term | Use | Avoid |
|------|-----|-------|
| Medical device | ✓ | Product, item, equipment |
| Intended use | ✓ | Purpose, function |
| Essential performance | ✓ | Key function |
| Risk management | ✓ | Risk assessment |
| Post-market surveillance | ✓ | Post-launch monitoring |

### Sentence Structure

**Requirement statements:**
```
The [subject] shall [action] [object].
Example: The device shall perform self-test at startup.
```

**Recommendation statements:**
```
The [subject] should [action] [object].
Example: The manufacturer should maintain device history records.
```

**Conditional statements:**
```
When [condition], the [subject] shall [action].
Example: When power fails, the device shall save current state.
```

## Detailed Guidelines

For comprehensive writing guidelines, see `modules/style-guide.md`.

For standard terminology list, see `modules/terminology.md`.

For before/after examples, see `modules/examples.md`.

For external style references, see `reference.md`.

## Usage

This skill is automatically loaded when:
- Writing regulatory documents
- Reviewing technical documentation
- Standardizing terminology across documents

Agents that use this skill:
- expert-writer: Document drafting
- expert-reviewer: Compliance verification
- manager-docs: Documentation management
