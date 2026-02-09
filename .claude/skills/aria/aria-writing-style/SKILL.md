---
name: aria-writing-style
description: >
  Technical documentation style guide for ARIA regulatory and technical documentation.
  Provides writing standards, terminology consistency, and sentence structure guidelines
  for creating clear, concise, and compliant documentation.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, technical-writing, documentation, style, regulatory"

# ARIA Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# ARIA Extension: Triggers
triggers:
  keywords: ["documentation", "writing", "style", "technical writing", "regulatory document"]
  agents: ["manager-docs", "expert-writer"]
  phases: ["brief", "execute", "deliver"]
  languages: ["en", "ko"]
---

# ARIA Writing Style Guide

## Overview

The ARIA Writing Style Guide provides standards for creating clear, concise, and compliant regulatory and technical documentation.

## Core Principles

1. **Clarity**: Write in simple, direct language
2. **Consistency**: Use terminology consistently throughout documents
3. **Compliance**: Follow regulatory documentation requirements
4. **Conciseness**: Eliminate unnecessary words and phrases

## Document Structure

### Header Section
- Document identifier
- Version number
- Date of issue
- Author/Approver information

### Body Section
- Clear section headings
- Logical content flow
- Numbered requirements
- Supporting tables and figures

### Footer Section
- Change history
- References
- Approval signatures

## Writing Guidelines

### Sentence Structure
- Use active voice when possible
- Keep sentences under 25 words
- One idea per sentence
- Avoid jargon and acronyms (define on first use)

### Terminology
- Use established regulatory terminology
- Create a glossary for project-specific terms
- Maintain consistency across all documents
- Use terms as defined in applicable standards

### Numbering and Formatting
- Use decimal numbering for hierarchical structure (1.0, 1.1, 1.1.1)
- Use tables for structured data
- Use figures for diagrams and illustrations
- Apply consistent formatting throughout

## Common Patterns

### Requirement Statements
- Use SHALL for mandatory requirements
- Use SHOULD for recommendations
- Use MAY for optional practices
- Use MUST NOT for prohibitions

### Procedures
- Write in imperative mood
- Use step-by-step format
- Include decision points
- Provide expected outcomes

### Reports
- Executive summary
- Methodology description
- Results presentation
- Conclusions and recommendations

## Quality Checklist

- [ ] Active voice used where appropriate
- [ ] Sentences are clear and concise
- [ ] Terminology is consistent
- [ ] Acronyms are defined on first use
- [ ] Formatting follows document template
- [ ] Sections are properly numbered
- [ ] References are accurately cited

## Templates and Examples

See the aria-templates skill for document templates that implement this style guide.
