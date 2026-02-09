# ARIA Team Workflow: 510(k) Submission Preparation

## Purpose

Prepare FDA 510(k) submissions through parallel team-based development with distinct section ownership and coordination.

## Prerequisites

- Device specifications and intended use documented
- Target market identified (US FDA)
- workflow.team.enabled: true
- CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
- Triggered by: /aria 510k prepare OR auto-detected complexity (5+ sections)

## Team Composition

### FDA Researcher (team-researcher, haiku)
- **Role**: Research FDA requirements and predicate devices
- **File Ownership**: `.aria/510k/research/**`, `.aria/510k/predicate-devices/**`
- **Tools**: Read, Grep, Glob, WebSearch, WebFetch
- **Permission Mode**: plan (read-only)

### Predicate Analyst (team-analyst, sonnet)
- **Role**: Analyze device specifications and comparisons
- **File Ownership**: `.aria/510k/comparison/**`, `.aria/510k/technological-characteristics/**`
- **Tools**: Read, Grep, Glob, Write, Edit
- **Permission Mode**: plan

### Submission Writer (team-writer, sonnet)
- **Role**: Draft submission sections per FDA eCopy templates
- **File Ownership**: `.aria/510k/submission/**`, `.aria/510k/sections/**`
- **Tools**: Read, Write, Edit, Grep
- **Permission Mode**: acceptEdits

## Phase 0: Task Decomposition

1. Analyze submission requirements:
   - Identify all required sections per FDA eCopy template
   - Determine predicate device research needs
   - Map technological characteristics for comparison

2. Create team:
   ```typescript
   TeamCreate({
     team_name: "aria-510k-prep-{submission_id}",
     description: "510(k) Submission Preparation for {device_name}",
     teammates: [
       { name: "fda-researcher", model: "haiku", ... },
       { name: "predicate-analyst", model: "sonnet", ... },
       { name: "submission-writer", model: "sonnet", ... }
     ],
     sharedTaskBoard: true
   })
   ```

3. Create shared task list:
   ```typescript
   TaskCreate({ subject: "Research predicate device 510(k) summaries", assignee: "fda-researcher" })
   TaskCreate({ subject: "Analyze device specifications vs predicate", assignee: "predicate-analyst", blockedBy: ["fda-researcher"] })
   TaskCreate({ subject: "Draft Indications for Use section", assignee: "submission-writer", blockedBy: ["predicate-analyst"] })
   TaskCreate({ subject: "Validate cross-reference consistency", assignee: "submission-writer", blockedBy: ["submission-writer"] })
   ```

## Phase 1: Spawn Team

Spawn all teammates in parallel:

```typescript
Task(
  subagent_type: "team-researcher",
  team_name: "aria-510k-prep-{submission_id}",
  name: "fda-researcher",
  prompt: "You are the FDA Researcher for 510(k) submission preparation.
    Device: {device_name}
    Your responsibilities: Research predicate devices, identify FDA guidance, document substantial equivalence criteria.
    File ownership: .aria/510k/research/**, .aria/510k/predicate-devices/**
    Coordinate with predicate-analyst for device specification comparisons.
    Mark tasks complete via TaskUpdate."
)

Task(
  subagent_type: "team-analyst",
  team_name: "aria-510k-prep-{submission_id}",
  name: "predicate-analyst",
  prompt: "You are the Predicate Device Analyst for 510(k) submission.
    Device: {device_name}
    Your responsibilities: Compare device specifications, analyze technological characteristics, justify substantial equivalence.
    File ownership: .aria/510k/comparison/**, .aria/510k/technological-characteristics/**
    Wait for predicate device research from fda-researcher.
    Mark tasks complete via TaskUpdate."
)

Task(
  subagent_type: "team-writer",
  team_name: "aria-510k-prep-{submission_id}",
  name: "submission-writer",
  prompt: "You are the Submission Writer for 510(k) preparation.
    Device: {device_name}
    Your responsibilities: Draft submission sections per FDA eCopy templates, format for submission.
    File ownership: .aria/510k/submission/**, .aria/510k/sections/**
    Wait for analysis from predicate-analyst before drafting.
    Ensure cross-reference consistency before finalization.
    Mark tasks complete via TaskUpdate."
)
```

## Phase 2: Parallel Execution

### Research Phase (fda-researcher)

1. **Predicate Device Research**
   - Search FDA database for potential predicate devices
   - Download and analyze 510(k) summaries
   - Identify key similarities and differences
   - Document in `.aria/510k/predicate-devices/`

2. **Regulatory Guidance**
   - Identify applicable FDA guidance documents
   - Research device-specific requirements
   - Document substantial equivalence criteria
   - Store in `.aria/510k/research/`

3. **Coordination**
   - SendMessage to predicate-analyst: "Predicate device research complete. Key findings: {summary}"
   - Update TaskList status

### Analysis Phase (predicate-analyst)

1. **Specification Comparison**
   - Compare device specifications to predicate
   - Identify technological characteristics
   - Document differences and similarities
   - Store in `.aria/510k/comparison/`

2. **Substantial Equivalence Analysis**
   - Justify substantial equivalence
   - Address any differences with safety/effectiveness rationale
   - Document in `.aria/510k/technological-characteristics/`

3. **Coordination**
   - SendMessage to submission-writer: "Analysis complete. Technological characteristics: {summary}"
   - Update TaskList status

### Drafting Phase (submission-writer)

1. **Section Drafting**
   - Draft Indications for Use
   - Draft Device Description
   - Draft Substantial Equivalence Summary
   - Format per FDA eCopy requirements
   - Store in `.aria/510k/sections/`

2. **Cross-Reference Validation**
   - Validate all cross-references between sections
   - Ensure consistency with predicate device analysis
   - Verify technological characteristics alignment
   - Request validation from predicate-analyst if inconsistencies found

3. **Coordination**
   - SendMessage to team: "Section {name} complete. Dependent sections: {list}"
   - Update TaskList status

## Phase 3: Coordination Patterns

### Predicate Device Change Notification

**Trigger**: Predicate device selection changes

**Action**:
```typescript
SendMessage({
  type: "broadcast",
  content: "PREDICATE DEVICE CHANGE: New predicate device selected. Affected sections: technological-characteristics, substantial-equivalence, indications-for-use, device-description. Please review and update as needed.",
  summary: "Predicate device changed - update affected sections"
})
```

**Flagged Sections**:
- technological-characteristics
- substantial-equivalence
- indications-for-use
- device-description

### Section Completion Notification

**Trigger**: Section drafting completed

**Action**:
```typescript
SendMessage({
  type: "broadcast",
  content: "SECTION COMPLETE: {section_name} is ready for cross-reference review. Dependent sections: {dependent_sections}.",
  summary: "Section {section_name} complete"
})
```

### Cross-Reference Consistency Check

**Trigger**: Before finalization

**Action**:
```typescript
SendMessage({
  type: "message",
  recipient: "predicate-analyst",
  content: "CROSS-REFERENCE REVIEW: Please validate that all technological characteristics in submission sections align with analysis.",
  summary: "Request cross-reference validation"
})
```

## Phase 4: Quality Validation

After all sections complete, run validation:

1. **Substantial Equivalence Check**
   - Verify substantial equivalence rationale complete
   - Confirm all differences addressed
   - Validate safety/effectiveness justification

2. **Cross-Reference Check**
   - Validate all internal cross-references
   - Ensure consistency across sections
   - Confirm predicate device alignment

3. **eCopy Format Check**
   - Verify FDA eCopy template compliance
   - Check formatting requirements
   - Validate document structure

4. **Regulatory Citation Check**
   - Verify all regulatory citations accurate
   - Confirm FDA guidance references
   - Check citation formatting

## Phase 5: Team Shutdown

After validation complete:

```typescript
// Notify team of completion
SendMessage({
  type: "broadcast",
  content: "510(k) SUBMISSION COMPLETE: All sections validated and ready for submission. Location: .aria/510k/submission/",
  summary: "510(k) preparation complete"
})

// Shutdown team
TeamDelete()
```

## Escalation Paths

| Condition | Escalate To | Action |
|-----------|-------------|--------|
| Substantial equivalence unclear | regulatory-strategy | Request regulatory pathway reassessment |
| New predicate device needed | regulatory-affairs | Request alternative predicate search |
| Technological characteristics require input | engineering-lead | Request technical specs verification |
| eCopy formatting issues | submission-specialist | Request formatting guidance |

## Quality Gates

- [ ] Predicate device identified and researched
- [ ] Substantial equivalence documented and justified
- [ ] All sections complete and formatted
- [ ] Cross-references validated and consistent
- [ ] eCopy format compliant
- [ ] Regulatory citations verified

## Completion Markers

- All sections complete
- Cross-references validated
- eCopy format verified
- Regulatory review approved

## Fallback Strategy

If team mode fails:
1. Graceful fallback to aria-orchestrator
2. Continue from last completed section
3. Sequential execution via expert-submission

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**SPEC**: SPEC-ARIA-005 (SR-001 to SR-007)
