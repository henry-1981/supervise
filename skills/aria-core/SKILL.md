---
name: aria-core
description: >
  Core skill for ARIA orchestrator. Defines Brief-Execute-Deliver workflow,
  VALID quality framework, agent routing, and user interaction patterns
  for Medical Device RA/QA business workflows.
license: MIT
compatibility: Designed for Claude Code
allowed-tools: Task AskUserQuestion Read Glob Grep
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "false"
  tags: "aria, orchestrator, workflow, valid, quality, raqa, regulatory"
  author: "ARIA Team"
  related-skills: "aria-domain-raqa, aria-quality-valid, aria-templates"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "aria"
    - "workflow"
    - "brief"
    - "execute"
    - "deliver"
    - "regulatory"
    - "quality"
    - "valid framework"
  agents:
    - "orchestrator"
  phases:
    - "brief"
    - "execute"
    - "deliver"
---

# ARIA Core Skill

## Brief-Execute-Deliver Workflow

ARIA uses a three-phase workflow adapted from MoAI's Plan-Run-Sync for business contexts.

### BRIEF Phase (Token Budget: 30,000)

Purpose: Understand the user's request, identify regulatory context, and create an execution plan.

Steps:
1. Intent Analysis - Parse natural language, classify task type, map to regulations
2. Scope Definition - Collect device info, target market, existing data via AskUserQuestion
3. Action Plan - Generate task list, assign agents, define approval checkpoints

Output: A structured brief with task breakdown, agent assignments, and approval checkpoints.

Transition to EXECUTE: User approves the action plan.

### EXECUTE Phase (Token Budget: 180,000)

Purpose: Perform the actual work through specialized agent delegation.

Steps:
1. Research - expert-researcher gathers regulatory information and precedents
2. Draft - expert-writer creates document drafts using templates
3. Review - expert-reviewer verifies compliance; manager-quality runs VALID gates
4. Refine - Incorporate review feedback, strengthen evidence

Quality Checkpoints (applied at each task completion):
- Regulation reference accuracy
- Data source traceability
- Document format compliance
- Terminology consistency

Transition to DELIVER: All tasks complete, VALID gates passed.

### DELIVER Phase (Token Budget: 40,000)

Purpose: Finalize outputs and deliver to the user.

Steps:
1. Final Quality Review - Full VALID gate pass
2. Format and Export - Convert to required format (Markdown, PDF structure, Notion page)
3. Distribution - Store in Notion, notify stakeholders
4. Knowledge Update - Record learnings for future reference

## VALID Quality Framework

The VALID framework ensures regulatory document quality across five dimensions.

### V - Verified
- All cited regulation/standard clauses match the actual source text
- Regulatory interpretations align with current guidance
- Technical claims are supported by evidence data

### A - Accurate
- All numbers and data match their sources
- Referenced documents and standards are the latest version
- Dates, version numbers, and identifiers are correct

### L - Linked
- Every requirement is linked to its corresponding document/evidence
- Traceability matrix is complete
- Changes are reflected in all affected documents

### I - Inspectable
- Every decision has a documented rationale
- Change history is traceable
- Review and approval records exist

### D - Deliverable
- Output conforms to the required template/format
- Submission authority format requirements are met
- All attachments and reference documents are included

## Agent Routing Rules

The orchestrator routes requests using keyword matching and intent classification.

Routing priority:
1. Explicit agent request - User names a specific capability
2. Domain keyword match - Regulatory terms trigger domain agents
3. Task type classification - Document writing, analysis, review, search
4. Fallback - Ask user for clarification via AskUserQuestion

Agent selection principles:
- Accuracy-critical tasks (regulatory interpretation, strategy) use opus-class agents
- Volume tasks (drafting, data processing) use sonnet-class agents
- Search and screening tasks use haiku-class agents
- Results from lower-tier agents are always verified by higher-tier agents

## User Interaction Patterns

### Question Design
- Maximum 4 options per AskUserQuestion call
- Use plain language, avoid technical jargon where possible
- Provide context for each option
- Always include a "need more information" or "other" escape option

### Approval Checkpoints
Regulatory decisions that require explicit user approval:
- Regulatory pathway selection (510(k) vs PMA vs De Novo)
- Predicate device selection
- Risk acceptability determination
- Substantial equivalence argument
- Final document approval before submission

### Progress Communication
- Report current phase and step clearly
- Indicate what was completed and what comes next
- Highlight any decisions or actions needed from the user
- Use structured Markdown with headings and bullet points

## Error Handling Patterns

### For Users
- Describe the issue in plain, non-technical language
- Explain what is being done automatically (retries, fallback)
- Provide a clear action the user can take if needed
- Show retry progress (e.g., "Retry 1 of 3")

### For Agents
- Maximum 3 retries per operation
- Escalate to orchestrator after retry exhaustion
- Log errors for audit trail
- Never expose internal errors to users
