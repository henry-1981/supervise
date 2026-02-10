# ARIA Workflow Module

## Brief-Execute-Deliver Workflow

ARIA implements a three-phase workflow adapted from MoAI's Plan-Run-Sync, optimized for regulatory affairs workflows with database-driven analysis.

### Token Budget Allocation

| Phase | Tokens | Percentage | Purpose |
|-------|--------|------------|---------|
| BRIEF | 30,000 | 60% | Regulatory strategy analysis and planning |
| EXECUTE | 180,000 | 30% | Document preparation and validation |
| DELIVER | 40,000 | 10% | Final quality gates and output formatting |

The Brief-heavy allocation (60%) reflects the database-driven nature of regulatory work, where thorough research and strategy development prevent costly rework.

---

## BRIEF Phase

### Purpose

Understand the user's request, identify regulatory context, and create an execution plan with user approval checkpoint.

### Token Budget: 30,000 (60%)

### Steps

#### 1. Intent Analysis

Parse the natural language request and classify the task type:

**Task Categories:**
- **Document Drafting**: Creating regulatory documents, submissions, reports
- **Analysis**: Evaluating compliance, gaps, risks, or data
- **Review**: Verifying documents against requirements
- **Search**: Looking up regulatory information, precedents, guidance

**Classification Method:**
- Keyword matching for common regulatory terms
- Sequential Thinking MCP for complex queries
- Fallback to AskUserQuestion for ambiguous requests

**Regulation/Standard Mapping:**
Identify applicable regulations based on keywords:
- FDA: 510(k), PMA, De Novo, 21 CFR Part 820, QSR
- EU MDR: CE marking, Technical Documentation, Clinical Evaluation
- ISO Standards: ISO 13485, IEC 62304, ISO 14971, IEC 60601
- MFDS: Korean medical device classification, approval pathways

#### 2. Scope Definition

Collect necessary information via AskUserQuestion (maximum 4 options per question):

**Required Information:**
- Device/product type and classification
- Target regulatory markets (FDA, EU, MFDS, or multi-market)
- Existing documentation or data
- Timeline and deadline constraints

**Question Design Principles:**
- Maximum 4 options per question
- Use plain language, avoid technical jargon
- Provide context for each option
- Always include an "other" or "need more info" option

**Example Scope Questions:**
```
Q1: What is the device classification?
- [ ] Class I (Low risk)
- [ ] Class II (Moderate risk)
- [ ] Class III (High risk)
- [ ] Not sure / Need help determining

Q2: Which target markets?
- [ ] US only (FDA)
- [ ] EU only (CE Mark)
- [ ] US + EU (FDA + CE Mark)
- [ ] Other (MFDS, multi-market)
```

#### 3. Regulatory/Standards Mapping

Map the request to applicable regulations and standards:

**Mapping Process:**
1. Identify primary regulatory pathway (e.g., 510(k), PMA, CE Mark)
2. List applicable standards (e.g., ISO 13485, IEC 62304)
3. Identify data requirements (e.g., clinical data, bench testing)
4. Note submission format requirements (e.g., eSTAR, CER format)

**Output: Structured Regulatory Context**
- Applicable regulations with specific sections
- Required standards with version numbers
- Data and documentation requirements
- Submission authority guidelines

#### 4. Action Plan

Generate a task breakdown with agent assignments:

**Task Decomposition:**
- Break down the request into specific, actionable tasks
- Assign each task to appropriate specialized agents
- Define deliverables for each task
- Set approval checkpoints for critical decisions

**Agent Assignment Principles:**
- **expert-researcher**: Regulatory research, precedent search, guidance lookup
- **expert-writer**: Document drafting, template application, content creation
- **expert-reviewer**: Compliance verification, quality checks, gap analysis
- **expert-domain**: Domain-specific expertise (regulatory, standards, risk, etc.)

**Output: Structured Brief**
```
BRIEF SUMMARY
============

Task: [Clear task description]
Domain: [Regulatory domain identified]
Markets: [Target regulatory markets]

APPLICABLE REGULATIONS
=====================
- [Regulation 1 with sections]
- [Regulation 2 with sections]
- [Standards with versions]

ACTION PLAN
===========
1. [Task 1] → [Agent] → [Deliverable]
2. [Task 2] → [Agent] → [Deliverable]
3. [Task 3] → [Agent] → [Deliverable]

APPROVAL CHECKPOINTS
====================
- [Checkpoint 1]: [Decision needed]
- [Checkpoint 2]: [Decision needed]

ESTIMATED COMPLETION: [Time estimate]
```

### Transition to EXECUTE

**Gatekeeper Function**: Brief phase includes a mandatory user approval checkpoint.

**User Decision:**
- [ ] **Approve**: Proceed with the action plan
- [ ] **Modify**: Adjust specific aspects of the plan
- [ ] **Clarify**: Ask questions about the approach
- [ ] **Cancel**: Abort the task

Only after user approval does the workflow transition to EXECUTE phase.

---

## EXECUTE Phase

### Purpose

Perform the actual work through specialized agent delegation with quality gates.

### Token Budget: 180,000 (30%)

### Steps

#### 1. Research

**Agent: expert-researcher**

**Tasks:**
- Search regulatory databases for precedents and guidance
- Retrieve latest standards and regulations via Context7 MCP
- Compile relevant regulatory citations and references
- Gather clinical data, if applicable

**Output: Research Package**
- Applicable regulation excerpts with specific section references
- Standard requirements with version numbers and dates
- Predicate device information (for 510(k) submissions)
- Clinical evaluation references (for MDR CE marking)

#### 2. Draft

**Agent: expert-writer**

**Tasks:**
- Create document drafts using templates
- Populate sections with research data
- Ensure proper formatting and structure
- Apply regulatory terminology appropriately

**Output: Document Draft**
- Structured document following template
- Content populated with research data
- Proper citations and references
- Technical language appropriate for regulatory review

#### 3. Review

**Agents: expert-reviewer, manager-quality**

**Tasks:**
- **expert-reviewer**: Verify compliance against regulations and standards
- **manager-quality**: Run VALID quality gates

**Review Checks:**
- Regulation reference accuracy
- Standard compliance verification
- Data source traceability
- Document format compliance
- Terminology consistency

**Output: Review Report**
- Compliance status for each requirement
- Identified gaps or deficiencies
- Recommendations for improvement
- VALID quality gate results

#### 4. Refine

**Tasks:**
- Incorporate review feedback
- Address identified gaps
- Strengthen evidence and citations
- Finalize content

**Output: Refined Document**
- All review feedback addressed
- Gaps filled with additional evidence
- Citations complete and accurate
- Document ready for final quality gates

### Quality Checkpoints

Applied at each task completion:

**Regulation Reference Accuracy:**
- All cited regulations include standard name, section, and version
- Citations match actual source text
- References are current and applicable

**Data Source Traceability:**
- All data points have source citations
- Clinical data references are complete
- Test data links to supporting documentation

**Document Format Compliance:**
- Template structure followed correctly
- Submission authority format requirements met
- Section organization complies with guidelines

**Terminology Consistency:**
- Regulatory terms used correctly
- Technical terminology is consistent
- Language matches regulatory standards

### Transition to DELIVER

**Completion Criteria:**
- All tasks in action plan completed
- All VALID quality gates passed
- Review feedback incorporated
- Document ready for final delivery

---

## DELIVER Phase

### Purpose

Finalize outputs and deliver quality-validated results to the user.

### Token Budget: 40,000 (10%)

### Steps

#### 1. Final Quality Review

**Agent: manager-quality**

**Full VALID Gate Pass:**

**V - Verified:**
- Cross-reference all cited regulation/standard clauses with source text
- Verify regulatory interpretations align with current guidance
- Confirm technical claims are supported by evidence data

**A - Accurate:**
- Validate all numbers and data match sources
- Confirm referenced documents and standards are latest versions
- Check dates, version numbers, and identifiers are correct

**L - Linked:**
- Verify every requirement is linked to corresponding document/evidence
- Confirm traceability matrix is complete
- Check changes are reflected in all affected documents

**I - Inspectable:**
- Verify every decision has documented rationale
- Confirm change history is traceable
- Check review and approval records exist

**D - Deliverable:**
- Confirm output conforms to required template/format
- Verify submission authority format requirements are met
- Check all attachments and reference documents are included

**Output: VALID Quality Report**
- Score for each dimension (1-5 scale)
- Overall VALID score (average of 5 dimensions)
- Identified issues (if any)
- Recommendation (Pass/Fail)

#### 2. Format and Export

**Format Conversion:**
- Convert to required output format (Markdown, PDF, Word)
- Ensure proper rendering of tables, figures, and diagrams
- Validate formatting for submission authority requirements

**Output Formats:**
- **Markdown**: Default format, readable in Claude Code
- **PDF Structure**: Structured content ready for PDF generation
- **Notion Page**: Formatted for Notion MCP integration (Phase 4)

#### 3. Distribution

**Storage and Distribution:**
- Save to local file system
- Update Notion database (Phase 4)
- Notify stakeholders (Phase 4)
- Update knowledge base for future reference

**Audit Trail:**
- Log document creation and changes
- Record user approvals and decisions
- Maintain version history

#### 4. Knowledge Update

**Learning Capture:**
- Record successful regulatory strategies
- Document precedent device information
- Update template library with new patterns
- Capture lessons learned for future reference

---

## Workflow Visualization

```
┌─────────────────────────────────────────────────────────────┐
│                    BRIEF PHASE (60%)                         │
├─────────────────────────────────────────────────────────────┤
│ 1. Intent Analysis → Classify task, map regulations         │
│ 2. Scope Definition → Collect info via AskUserQuestion     │
│ 3. Regulatory Mapping → Identify applicable standards       │
│ 4. Action Plan → Generate task breakdown                   │
│                                                              │
│                    ┌──────────────┐                          │
│                    │ USER APPROVAL │ ◄──────── Gatekeeper    │
│                    └──────────────┘                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   EXECUTE PHASE (30%)                        │
├─────────────────────────────────────────────────────────────┤
│ 1. Research → expert-researcher gathers data               │
│ 2. Draft → expert-writer creates documents                 │
│ 3. Review → expert-reviewer + manager-quality validate     │
│ 4. Refine → Incorporate feedback, strengthen evidence      │
│                                                              │
│                   Quality Checkpoints at each step          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   DELIVER PHASE (10%)                        │
├─────────────────────────────────────────────────────────────┤
│ 1. Final Quality Review → Full VALID gate pass             │
│ 2. Format and Export → Convert to required format          │
│ 3. Distribution → Store, notify, update knowledge base     │
│ 4. Knowledge Update → Record learnings for future          │
└─────────────────────────────────────────────────────────────┘
```

---

## Error Handling

### Phase-Level Error Recovery

**Brief Phase Errors:**
- **Insufficient Information**: Ask specific follow-up questions
- **Regulatory Ambiguity**: Flag uncertainty, present options
- **Scope Confusion**: Request clarification via AskUserQuestion

**Execute Phase Errors:**
- **Agent Failure**: Retry with alternative agent (max 3 retries)
- **Data Inconsistency**: Flag to user, request clarification
- **Template Issues**: Fall back to standard format

**Deliver Phase Errors:**
- **VALID Gate Failure**: Return to Execute phase for refinement
- **Format Conversion Error**: Provide alternative format
- **Distribution Failure**: Store locally, notify user of issue

### Error Message Pattern

```
## Issue Description

[Plain language description of what went wrong]

### What Happened
[Explanation in user-friendly terms]

### What We're Doing
[Automatic recovery actions being taken]

### What You Can Do
[Manual options if automatic recovery fails]

### Status
[Current progress: Retry 1 of 3]
```

---

## Configuration

Workflow behavior is configured in `aria.yaml`:

```yaml
workflow:
  default: "brief-execute-deliver"
  brief_tokens: 30000
  execute_tokens: 180000
  deliver_tokens: 40000
  auto_clear: true
  approval_required: true

  brief:
    max_questions: 5
    require_approval: true

  execute:
    max_parallel_agents: 3
    quality_checkpoints: true

  deliver:
    enforce_valid: true
    formats:
      - markdown
      - pdf_structure
      - notion_page
```

---

## Success Criteria

**Brief Phase:**
- ✅ Intent correctly classified
- ✅ Scope defined with user input
- ✅ Regulatory context mapped
- ✅ Action plan generated and approved

**Execute Phase:**
- ✅ All tasks completed
- ✅ Quality checkpoints passed
- ✅ Review feedback incorporated
- ✅ Document ready for delivery

**Deliver Phase:**
- ✅ VALID gates passed with score ≥ 4.0
- ✅ Output formatted correctly
- ✅ Distribution completed
- ✅ Knowledge base updated

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Module**: ARIA Core Workflow
