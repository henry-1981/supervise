# SPEC-ARIA-005: ARIA Phase 5 - Advanced Features

## TAG BLOCK

```
SPEC-ID: SPEC-ARIA-005
Title: Advanced Features Implementation
Created: 2026-02-09
Status: Planned
Priority: High
Assigned: manager-spec
Phase: Phase 5 of 5
Dependencies: SPEC-ARIA-004 (MCP Integrations)
```

## Environment

### System Context

ARIA (AI Regulatory Intelligence Assistant) is a Claude Code plugin specialized for Medical Device RA/QA (Regulatory Affairs / Quality Assurance) professionals. Phase 5 implements advanced features that build upon the completed Phase 4 MCP integrations.

### Technical Environment

- **Platform**: Claude Code Plugin System
- **Language**: English (technical documentation), Korean (user-facing responses per language.yaml)
- **Dependencies**:
  - Notion MCP (Phase 4) - Must be fully functional
  - Google Workspace MCP (Phase 4) - Must be configured
  - Context7 MCP (Phase 4) - Must be optimized
  - Agent Teams (Claude Code v2.1.32+)
  - MoAI-ADK Hooks System
- **Storage**:
  - Agent Memory: Project scope (`.claude/agent-memory/` via VCS)
  - Knowledge Base: Notion MCP integration
- **Compliance**: VALID Quality Framework (Verified, Accurate, Linked, Inspectable, Deliverable)

### Stakeholders

- **Primary**: RA/QA professionals requiring advanced automation and analytics
- **Secondary**: Regulatory managers overseeing compliance workflows
- **Tertiary**: Clinical evaluation teams and audit preparation teams

## Assumptions

### Technical Assumptions

- [A1] Claude Code Agent Teams v2.1.32+ is available and stable
  - **Confidence**: High (documented feature)
  - **Evidence**: Official Claude Code documentation
  - **Risk if Wrong**: Agent Teams features would need alternative implementation
  - **Validation**: Test TeamCreate API availability before implementation

- [A2] Notion MCP maintains connection stability for memory operations
  - **Confidence**: Medium (network-dependent)
  - **Evidence**: Phase 4 MCP integration completed
  - **Risk if Wrong**: Agent Memory operations may fail intermittently
  - **Validation**: Implement retry logic with exponential backoff

- [A3] Project scope agent memory is shared via VCS without conflicts
  - **Confidence**: Medium (team coordination required)
  - **Evidence**: MoAI-ADK memory documentation
  - **Risk if Wrong**: Memory corruption or merge conflicts in shared memory
  - **Validation**: Document VCS workflow for memory files

### Business Assumptions

- [B1] RA/QA teams require persistent learning across sessions
  - **Confidence**: High (user feedback from Phases 1-4)
  - **Evidence**: Repeated requests for "remember my preferences"
  - **Risk if Wrong**: Agent Memory features would see low adoption
  - **Validation**: Conduct user survey before final implementation

- [B2] Parallel agent teams provide measurable efficiency gains
  - **Confidence**: Medium (theoretical benefit)
  - **Evidence**: Agent Teams documentation promising parallel execution
  - **Risk if Wrong**: Complexity may outweigh benefits for small teams
  - **Validation**: Implement A/B testing for sequential vs parallel workflows

- [B3] Advanced analytics features require cross-session data accumulation
  - **Confidence**: High (domain requirement)
  - **Evidence**: Complaint trend analysis requires historical data
  - **Risk if Wrong**: Features would not function until sufficient data accumulates
  - **Validation**: Design with synthetic data generation for testing

## Requirements

### 1. Agent Memory System (Project Scope)

#### 1.1 Regulatory Decision Memory

**Ubiquitous Requirements**:
- [REQ-1.1.1] The system **shall** maintain a persistent memory of regulatory decisions and interpretations across sessions
- [REQ-1.1.2] The system **shall** store decision rationale, source regulations, and applicability context for each remembered decision
- [REQ-1.1.3] The system **shall** organize memory entries by regulatory domain (FDA, EU MDR, MFDS)

**Event-Driven Requirements**:
- [REQ-1.1.4] **WHEN** a regulatory decision is made during document drafting, the system **shall** prompt to store the decision in memory
- [REQ-1.1.5] **WHEN** a similar regulatory question is encountered, the system **shall** retrieve and present relevant past decisions

**State-Driven Requirements**:
- [REQ-1.1.6] **IF** a stored regulatory decision becomes obsolete due to regulation changes, the system **shall** flag the entry for review
- [REQ-1.1.7] **WHERE** company-specific regulatory interpretations exist, the system **shall** tag them as "company-specific" and segregate from general regulatory guidance

#### 1.2 Company Preference Learning

**Ubiquitous Requirements**:
- [REQ-1.2.1] The system **shall** learn and remember company-specific preferences for document formatting and terminology
- [REQ-1.2.2] The system **shall** maintain preferred templates for each document type (510(k), CE Technical File, etc.)
- [REQ-1.2.3] The system **shall** track user-approved vs user-rejected suggestions to improve future recommendations

**Event-Driven Requirements**:
- [REQ-1.2.4] **WHEN** a user rejects a generated suggestion, the system **shall** record the rejection reason to avoid similar suggestions
- [REQ-1.2.5] **WHEN** a user accepts a suggestion with modifications, the system **shall** learn from the modifications

**State-Driven Requirements**:
- [REQ-1.2.6] **IF** conflicting preferences are detected (e.g., two users prefer different formats), the system **shall** prompt for preference resolution
- [REQ-1.2.7] **WHERE** user-specific preferences conflict with company-wide standards, the system **shall** flag the conflict for admin review

#### 1.3 Repetitive Task Pattern Recognition

**Ubiquitous Requirements**:
- [REQ-1.3.1] The system **shall** identify and remember repetitive task patterns in RA/QA workflows
- [REQ-1.3.2] The system **shall** maintain a library of common task sequences (e.g., quarterly audit preparation workflow)
- [REQ-1.3.3] The system **shall** suggest automation for identified repetitive patterns

**Event-Driven Requirements**:
- [REQ-1.3.4] **WHEN** a task sequence is repeated 3+ times with similar parameters, the system **shall** suggest creating a reusable workflow template
- [REQ-1.3.5] **WHEN** a user initiates a recognized repetitive task, the system **shall** offer to execute the learned pattern

**State-Driven Requirements**:
- [REQ-1.3.6] **IF** a task pattern varies significantly between executions, the system **shall** not suggest automation until consistency improves
- [REQ-1.3.7] **WHERE** task patterns overlap significantly, the system **shall** merge them into generalized templates

### 2. Agent Teams Mode (Experimental)

#### 2.1 510(k) Submission Preparation Team

**Ubiquitous Requirements**:
- [REQ-2.1.1] The system **shall** support parallel execution of 510(k) submission preparation using Agent Teams
- [REQ-2.1.2] The system **shall** coordinate team members for distinct submission sections (Indications for Use, Comparison, Predicate Device Analysis)
- [REQ-2.1.3] The system **shall** maintain shared task board for section ownership and progress tracking

**Event-Driven Requirements**:
- [REQ-2.1.4] **WHEN** 510(k) preparation is initiated, the system **shall** create a team with researcher, analyst, and writer agents
- [REQ-2.1.5] **WHEN** a team member completes a section, the system **shall** notify other members and update the shared task board

**State-Driven Requirements**:
- [REQ-2.1.6] **IF** predicate device selection changes during preparation, the system **shall** notify all team members and flag affected sections
- [REQ-2.1.7] **WHERE** multiple team members work on related sections, the system **shall** enforce cross-reference consistency

#### 2.2 Audit Response Team

**Ubiquitous Requirements**:
- [REQ-2.2.1] The system **shall** support parallel execution of audit response preparation using Agent Teams
- [REQ-2.2.2] The system **shall** coordinate team members for audit finding categorization (Critical, Major, Minor)
- [REQ-2.2.3] The system **shall** assign CAPA planning to specialized team members based on finding severity

**Event-Driven Requirements**:
- [REQ-2.2.4] **WHEN** audit findings are received, the system **shall** create a team with researcher, analyst, and capa expert agents
- [REQ-2.2.5] **WHEN** a CAPA plan is drafted, the system **shall** route it for validation before finalizing

**State-Driven Requirements**:
- [REQ-2.2.6] **IF** an audit finding requires cross-functional input (e.g., R&D, Manufacturing), the system **shall** escalate to appropriate experts
- [REQ-2.2.7] **WHERE** CAPA deadlines are at risk, the system **shall** alert the team and suggest escalation paths

### 3. Advanced Analytics Features

#### 3.1 Complaint Trend Analysis and Alerts

**Ubiquitous Requirements**:
- [REQ-3.1.1] The system **shall** automatically analyze complaint data for trends and patterns
- [REQ-3.1.2] The system **shall** detect statistically significant increases in complaint frequency or severity
- [REQ-3.1.3] The system **shall** correlate complaint trends with product changes, lot numbers, or geographical clusters

**Event-Driven Requirements**:
- [REQ-3.1.4] **WHEN** a significant complaint trend is detected, the system **shall** generate an alert with actionable recommendations
- [REQ-3.1.5] **WHEN** complaint trends correlate with specific product lots, the system **shall** flag for CAPA investigation

**State-Driven Requirements**:
- [REQ-3.1.6] **IF** complaint frequency exceeds predefined thresholds, the system **shall** escalate to regulatory reporting requirements
- [REQ-3.1.7] **WHERE** geographical clusters are detected, the system **shall** flag for potential regional regulatory notifications

#### 3.2 Regulatory Change Impact Analysis

**Ubiquitous Requirements**:
- [REQ-3.2.1] The system **shall** monitor regulatory changes (FDA guidance updates, EU MDR amendments)
- [REQ-3.2.2] The system **shall** assess the impact of regulatory changes on existing documentation and submissions
- [REQ-3.2.3] The system **shall** maintain a mapping between regulations and affected documents

**Event-Driven Requirements**:
- [REQ-3.2.4] **WHEN** a relevant regulatory change is detected, the system **shall** identify all affected documents in the knowledge base
- [REQ-3.2.5] **WHEN** regulatory changes impact pending submissions, the system **shall** flag for review before submission

**State-Driven Requirements**:
- [REQ-3.2.6] **IF** a regulatory change invalidates previously stored decisions, the system **shall** flag those decisions for re-evaluation
- [REQ-3.2.7] **WHERE** regulatory changes create new requirements, the system **shall** update template libraries and validation checklists

#### 3.3 Cross-Submission Knowledge Utilization

**Ubiquitous Requirements**:
- [REQ-3.3.1] The system **shall** maintain a knowledge base of successful regulatory arguments and evidence
- [REQ-3.3.2] The system **shall** enable search and retrieval of relevant content from previous submissions
- [REQ-3.3.3] The system **shall** tag knowledge entries with regulatory outcome (approved, approvable, not approved)

**Event-Driven Requirements**:
- [REQ-3.3.4] **WHEN** drafting a new submission, the system **shall** suggest relevant content from successful previous submissions
- [REQ-3.3.5] **WHEN** a submission receives approval, the system **shall** archive successful arguments for future reference

**State-Driven Requirements**:
- [REQ-3.3.6] **IF** a previous submission argument is reused, the system **shall** flag for context validation (product differences, regulation changes)
- [REQ-3.3.7] **WHERE** similar submissions faced regulatory challenges, the system **shall** warn about potential pitfalls

### 4. Complete Workflows

#### 4.1 Clinical Evaluation Workflow

**Ubiquitous Requirements**:
- [REQ-4.1.1] The system **shall** provide a complete clinical evaluation workflow per MEDDEV 2.7.1 rev 4
- [REQ-4.1.2] The system **shall** support CER (Clinical Evaluation Report) document generation with literature search integration
- [REQ-4.1.3] The system **shall** maintain clinical data traceability from literature to conclusion

**Event-Driven Requirements**:
- [REQ-4.1.4] **WHEN** clinical evaluation is initiated, the system **shall** guide through Stage 1 (Scope), Stage 2 (Literature Search), Stage 3 (Data Analysis), Stage 4 (CER Generation)
- [REQ-4.1.5] **WHEN** literature gaps are identified, the system **shall** flag for additional clinical investigation requirements

**State-Driven Requirements**:
- [REQ-4.1.6] **IF** clinical data does not demonstrate safety and performance, the system **shall** flag for PMCF (Post-Market Clinical Follow-up) requirements
- [REQ-4.1.7] **WHERE** equivalent device data is used, the system **shall** maintain equivalence justification traceability

#### 4.2 Internal Audit Workflow

**Ubiquitous Requirements**:
- [REQ-4.2.1] The system **shall** provide a complete internal audit workflow per ISO 13485 requirements
- [REQ-4.2.2] The system **shall** support audit planning, execution, finding documentation, and CAPA tracking
- [REQ-4.2.3] The system **shall** maintain audit history and trend analysis for continuous improvement

**Event-Driven Requirements**:
- [REQ-4.2.4] **WHEN** internal audit is scheduled, the system **shall** generate audit agenda based on previous findings and risk areas
- [REQ-4.2.5] **WHEN** audit findings are documented, the system **shall** route for CAPA planning and track resolution

**State-Driven Requirements**:
- [REQ-4.2.6] **IF** repeat findings are detected across multiple audits, the system **shall** flag for systemic quality issues
- [REQ-4.2.7] **WHERE** CAPA effectiveness is not demonstrated, the system **shall** extend CAPA verification timelines

#### 4.3 Post-Market Surveillance Workflow

**Ubiquitous Requirements**:
- [REQ-4.3.1] The system **shall** provide a complete post-market surveillance workflow per EU MDR Article 83-85
- [REQ-4.3.2] The system **shall** support PMS data collection, analysis, trend reporting, and PSUR generation
- [REQ-4.3.3] The system **shall** maintain PMS data traceability from source to regulatory report

**Event-Driven Requirements**:
- [REQ-4.3.4] **WHEN** PMS data indicates safety issues, the system **shall** trigger field safety corrective action (FSCA) workflow
- [REQ-4.3.5] **WHEN** PSUR submission is due, the system **shall** compile relevant PMS data and generate PSUR draft

**State-Driven Requirements**:
- [REQ-4.3.6] **IF** trend reporting indicates significant changes in benefit-risk profile, the system **shall** flag for regulatory notification
- [REQ-4.3.7] **WHERE** serious incidents are reported, the system **shall** ensure timeline compliance with regional reporting requirements

### 5. Multi-Country Regulatory Strategy Comparison

**Ubiquitous Requirements**:
- [REQ-5.1.1] The system **shall** support comparison of regulatory requirements across FDA (US), EU MDR (Europe), MFDS (South Korea), PMDA (Japan), ANVISA (Brazil), Health Canada
- [REQ-5.1.2] The system **shall** maintain a matrix of requirement differences by device classification and intended use
- [REQ-5.1.3] The system **shall** identify regulatory pathway conflicts and suggest harmonization strategies

**Event-Driven Requirements**:
- [REQ-5.1.4] **WHEN** multi-country submission is planned, the system **shall** generate a comparison matrix highlighting requirement differences
- [REQ-5.1.5] **WHEN** a requirement conflict exists between markets, the system **shall** suggest approaches for maintaining compliance

**State-Driven Requirements**:
- [REQ-5.1.6] **IF** a device is approved in one market but faces challenges in another, the system **shall** analyze the difference and document lessons learned
- [REQ-5.1.7] **WHERE** regulatory timelines differ significantly, the system **shall** suggest submission sequencing strategies

### 6. Additional Templates

#### 6.1 Clinical Templates

**Ubiquitous Requirements**:
- [REQ-6.1.1] The system **shall** provide CER (Clinical Evaluation Report) template per MEDDEV 2.7.1 rev 4
- [REQ-6.1.2] The system **shall** provide PMCF Plan template with post-market clinical follow-up protocol
- [REQ-6.1.3] The system **shall** provide Clinical Investigation Plan template per ISO 14155

#### 6.2 Quality Management System Templates

**Ubiquitous Requirements**:
- [REQ-6.2.1] The system **shall** provide Quality Manual template per ISO 13485
- [REQ-6.2.2] The system **shall** provide CAPA procedure template with root cause analysis framework
- [REQ-6.2.3] The system **shall** provide Management Review template with KPI tracking

#### 6.3 Audit Templates

**Ubiquitous Requirements**:
- [REQ-6.3.1] The system **shall** provide Internal Audit Checklist template per ISO 13485 clauses
- [REQ-6.3.2] The system **shall** provide Audit Report template with finding categorization
- [REQ-6.3.3] The system **shall** provide Supplier Audit template for supplier qualification

#### 6.4 EU MDR Templates

**Ubiquitous Requirements**:
- [REQ-6.4.1] The system **shall** provide Technical File template per Annex II and Annex III
- [REQ-6.4.2] The system **shall** provide PSUR (Periodic Safety Update Report) template per Annex XIII
- [REQ-6.4.3] The system **shall** provide SSR (Summary of Safety and Performance) template per Annex I

### 7. Hook System Integration

#### 7.1 Quality Check Hooks

**Ubiquitous Requirements**:
- [REQ-7.1.1] The system **shall** implement PreToolUse hooks for document quality validation before Write/Edit operations
- [REQ-7.1.2] The system **shall** validate regulatory citations and references in documents before completion
- [REQ-7.1.3] The system **shall** check VALID framework compliance before marking documents as complete

**Event-Driven Requirements**:
- [REQ-7.1.4] **WHEN** a quality check hook fails, the system **shall** prevent document completion and provide specific improvement guidance
- [REQ-7.1.5] **WHEN** regulatory citations are missing or outdated, the system **shall** flag and request updates

**State-Driven Requirements**:
- [REQ-7.1.6] **IF** a document fails quality checks, the system **shall** maintain a checklist of pending corrections
- [REQ-7.1.7] **WHERE** quality check patterns repeat, the system **shall** suggest template updates to prevent future issues

#### 7.2 Audit Trail Hooks

**Ubiquitous Requirements**:
- [REQ-7.2.1] The system **shall** implement PostToolUse hooks for audit trail logging of all document changes
- [REQ-7.2.2] The system **shall** track change author, timestamp, and rationale for all regulatory document modifications
- [REQ-7.2.3] The system **shall** maintain audit trail integrity per 21 CFR Part 11 electronic signature requirements

**Event-Driven Requirements**:
- [REQ-7.2.4] **WHEN** a regulatory document is modified, the system **shall** log the change with user attribution and change summary
- [REQ-7.2.5] **WHEN** audit trail logging fails, the system **shall** prevent the operation and alert the user

**State-Driven Requirements**:
- [REQ-7.2.6] **IF** audit trail continuity is broken (e.g., system restart), the system **shall** create a resumption entry
- [REQ-7.2.7] **WHERE** audit trail data is exported, the system **shall** maintain chain of custody documentation

#### 7.3 Template Verification Hooks

**Ubiquitous Requirements**:
- [REQ-7.3.1] The system **shall** implement SessionStart hooks for template version verification
- [REQ-7.3.2] The system **shall** validate template currency against regulatory requirements on session initialization
- [REQ-7.3.3] The system **shall** alert users to outdated templates before document generation begins

**Event-Driven Requirements**:
- [REQ-7.3.4] **WHEN** a template is updated, the system **shall** notify users of changes and migration requirements
- [REQ-7.3.5] **WHEN** template currency check fails, the system **shall** offer to update templates before proceeding

**State-Driven Requirements**:
- [REQ-7.3.6] **IF** template validation fails due to network issues (Context7 MCP unavailable), the system **shall** cache last known good status and retry later
- [REQ-7.3.7] **WHERE** templates are customized per company, the system **shall** validate customizations against base template requirements

### 8. Output Styles

#### 8.1 Report Format Customization

**Ubiquitous Requirements**:
- [REQ-8.1.1] The system **shall** support multiple output formats for regulatory reports (Markdown, HTML, PDF, Word)
- [REQ-8.1.2] The system **shall** maintain company-specific branding templates for formatted reports
- [REQ-8.1.3] The system **shall** enable output style selection via configuration

**Event-Driven Requirements**:
- [REQ-8.1.4] **WHEN** a report is generated, the system **shall** apply the configured output style formatting
- [REQ-8.1.5] **WHEN** output format conversion fails, the system **shall** fall back to Markdown and alert the user

**State-Driven Requirements**:
- [REQ-8.1.6] **IF** multiple output formats are requested, the system **shall** generate all formats in parallel where possible
- [REQ-8.1.7] **WHERE** PDF generation requires external tools (e.g., Pandoc, wkhtmltopdf), the system **shall** verify tool availability before attempting conversion

#### 8.2 Accessibility and Readability

**Ubiquitous Requirements**:
- [REQ-8.2.1] The system **shall** ensure output formats meet accessibility standards (WCAG 2.1 AA for HTML, tagged PDF for PDF)
- [REQ-8.2.2] The system **shall** maintain document structure consistency across output format conversions
- [REQ-8.2.3] The system **shall** preserve regulatory citation formatting and hyperlinking in all output formats

**Event-Driven Requirements**:
- [REQ-8.2.4] **WHEN** HTML output is generated, the system **shall** include semantic markup for screen reader compatibility
- [REQ-8.2.5] **WHEN** PDF output is generated, the system **shall** include document outline and metadata for navigation

**State-Driven Requirements**:
- [REQ-8.2.6] **IF** output format limitations prevent full feature parity (e.g., Markdown lacks advanced formatting), the system **shall** document the limitations
- [REQ-8.2.7] **WHERE** regulatory submission requires specific format (e.g., PDF for FDA eCopy), the system **shall** validate output format compliance before submission

## Specifications

### Agent Memory Architecture

**Memory Storage Structure**:
```
.claude/agent-memory/aria/
├── regulatory-decisions.json
├── company-preferences.json
├── task-patterns.json
└── learning-metrics.json
```

**Memory Entry Schema** (regulatory-decisions.json):
```json
{
  "decision_id": "DEC-2026-001",
  "question": "Is software as a medical device (SaMD) subject to FDA 510(k) for minor bug fixes?",
  "answer": "Bug fixes that do not affect device safety or effectiveness are typically not subject to 510(k)...",
  "regulation": "21 CFR 807.81(a)",
  "rationale": "FDA guidance on SaMD updates...",
  "applicability": ["SaMD", "Software Updates"],
  "company_specific": false,
  "valid_until": null,
  "created_at": "2026-01-15T10:30:00Z",
  "last_reviewed": "2026-01-15T10:30:00Z",
  "confidence_score": 0.95
}
```

**Memory VCS Integration**:
- Memory files committed to repository with `.gitattributes` for merge conflict resolution
- Team synchronization via pull requests for company-specific preferences
- Memory integrity validation on session start

### Agent Teams Configuration

**Team Creation API** (Claude Code v2.1.32+):
```typescript
// 510(k) Preparation Team
TeamCreate({
  name: "510k-prep-team",
  teammates: [
    {
      name: "researcher",
      model: "haiku",
      tools: ["Read", "Grep", "Glob", "WebSearch", "WebFetch"],
      prompt: "Research FDA 510(k) requirements, predicate devices, and substantial equivalence criteria"
    },
    {
      name: "analyst",
      model: "sonnet",
      tools: ["Read", "Write", "Edit", "Grep"],
      prompt: "Analyze device specifications and predicate device comparisons for substantial equivalence"
    },
    {
      name: "writer",
      model: "sonnet",
      tools: ["Read", "Write", "Edit"],
      prompt: "Draft 510(k) submission sections following FDA eCopy templates"
    }
  ],
  sharedTaskBoard: true
})
```

**Team Coordination**:
- Task decomposition via TaskCreate with file ownership boundaries
- Teammates self-claim tasks from shared board
- Quality validation via team-quality agent after all implementation completes

### Hook Integration Points

**Hook Configuration** (`.claude/settings.json`):
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-pre-tool.sh\"",
      "timeout": 5
    }],
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-post-tool.sh\"",
      "timeout": 10
    }],
    "SessionStart": [{
      "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-session-start.sh\"",
      "timeout": 5
    }]
  }
}
```

**Quality Check Hook Actions**:
- Validate regulatory citation format (e.g., "21 CFR 820.30", "EU MDR Annex I")
- Check document structure compliance with template requirements
- Verify VALID framework dimensions (Verified, Accurate, Linked, Inspectable, Deliverable)

### Analytics Implementation

**Complaint Trend Analysis Algorithm**:
```
1. Aggregate complaint data by month, product, and complaint type
2. Calculate statistical baseline (mean ± 2σ) for each category
3. Flag data points exceeding baseline threshold
4. Correlate with product changes (lot numbers, manufacturing dates)
5. Generate alert with actionable recommendations
```

**Regulatory Change Monitoring**:
- WebSearch for "FDA guidance updates [current month]"
- Context7 MCP for updated regulation text
- Impact analysis against stored document mappings
- Automatic flagging of affected documents in Notion knowledge base

### Template Organization

**Template Directory Structure**:
```
.claude/templates/aria/
├── clinical/
│   ├── cer-template.md
│   ├── pmcf-plan-template.md
│   └── clinical-investigation-plan-template.md
├── qms/
│   ├── quality-manual-template.md
│   ├── capa-procedure-template.md
│   └── management-review-template.md
├── audit/
│   ├── internal-audit-checklist-template.md
│   ├── audit-report-template.md
│   └── supplier-audit-template.md
└── eu-mdr/
    ├── technical-file-template.md
    ├── psur-template.md
    └── ssr-template.md
```

### Output Style System

**Format Conversion Pipeline**:
```
Markdown (Source)
    ↓ Pandoc / wkhtmltopdf
HTML (Web Preview)
    ↓ PDF Generation
PDF (Regulatory Submission)
    ↓ docx conversion
Word (Internal Review)
```

**Configuration** (`.moai/config/sections/output.yaml`):
```yaml
output:
  default_format: markdown
  formats:
    markdown:
      extension: ".md"
      encoding: "utf-8"
    html:
      extension: ".html"
      css_theme: "regulatory-standard"
      accessibility: "wcag-2.1-aa"
    pdf:
      extension: ".pdf"
      page_size: "letter"
      margins: "0.75in"
      toc: true
      bookmarks: true
    word:
      extension: ".docx"
      template: "regulatory-template.dotx"
```

## Traceability

| Requirement | Agent(s) | Skills | Templates | Test Scenario |
|-------------|----------|--------|-----------|---------------|
| REQ-1.1.x | orchestrator, expert-researcher | moai-workflow-jit-docs | regulatory-decisions.json | TC-1.1.1: Store and retrieve regulatory decision |
| REQ-1.2.x | orchestrator, expert-writer | moai-workflow-spec | company-preferences.json | TC-1.2.1: Learn and apply company formatting preference |
| REQ-1.3.x | orchestrator, expert-analyst | moai-foundation-philosopher | task-patterns.json | TC-1.3.1: Detect and suggest repetitive task automation |
| REQ-2.1.x | orchestrator (TeamCreate) | moai-foundation-claude | 510k-team-config.json | TC-2.1.1: Parallel 510(k) preparation with 3 agents |
| REQ-2.2.x | orchestrator (TeamCreate) | moai-foundation-claude | audit-team-config.json | TC-2.2.1: Parallel audit response with CAPA expert |
| REQ-3.1.x | expert-analyst | moai-platform-database-cloud | complaint-trend-query.sql | TC-3.1.1: Detect and alert complaint trend spike |
| REQ-3.2.x | expert-researcher | moai-workflow-jit-docs | regulation-mapping.json | TC-3.2.1: Flag documents affected by FDA guidance update |
| REQ-3.3.x | expert-writer, expert-researcher | Notion MCP | knowledge-base-schema.json | TC-3.3.1: Suggest relevant content from previous submission |
| REQ-4.1.x | expert-clinical, orchestrator | moai-workflow-spec | cer-workflow.md | TC-4.1.1: Complete CER generation workflow |
| REQ-4.2.x | expert-audit, orchestrator | moai-workflow-spec | audit-workflow.md | TC-4.2.1: Complete internal audit workflow |
| REQ-4.3.x | expert-clinical, orchestrator | moai-workflow-spec | pms-workflow.md | TC-4.3.1: Complete post-market surveillance workflow |
| REQ-5.1.x | expert-regulatory | moai-workflow-jit-docs | regulatory-matrix.md | TC-5.1.1: Compare requirements across FDA, EU MDR, MFDS |
| REQ-6.1.x | expert-writer | Clinical templates | cer-template.md | TC-6.1.1: Generate CER from template |
| REQ-6.2.x | expert-writer | QMS templates | quality-manual-template.md | TC-6.2.1: Generate quality manual from template |
| REQ-6.3.x | expert-audit | Audit templates | internal-audit-checklist-template.md | TC-6.3.1: Generate audit checklist from template |
| REQ-6.4.x | expert-regulatory | EU MDR templates | technical-file-template.md | TC-6.4.1: Generate technical file from template |
| REQ-7.1.x | manager-quality | moai-foundation-core | quality-check-hook.sh | TC-7.1.1: Validate regulatory citations before document completion |
| REQ-7.2.x | manager-quality | moai-foundation-claude | audit-trail-hook.sh | TC-7.2.1: Log all document changes with attribution |
| REQ-7.3.x | orchestrator | moai-workflow-spec | template-verify-hook.sh | TC-7.3.1: Verify template currency on session start |
| REQ-8.1.x | manager-docs | Pandoc/wkhtmltopdf | output-config.yaml | TC-8.1.1: Generate PDF report with company branding |
| REQ-8.2.x | manager-docs | WCAG 2.1 AA standards | html-output-template.html | TC-8.2.1: Generate accessible HTML output |

## Dependencies

### Internal Dependencies
- **SPEC-ARIA-001**: Core Framework (agents, skills, VALID framework)
- **SPEC-ARIA-002**: Business Agents (expert-writer, expert-analyst, expert-reviewer, expert-researcher)
- **SPEC-ARIA-003**: RA/QA Domain Agents (8 specialized agents)
- **SPEC-ARIA-004**: MCP Integrations (Notion, Context7, Google Workspace, Sequential Thinking)

### External Dependencies
- **Claude Code v2.1.32+**: Agent Teams API
- **MoAI-ADK Hooks System**: Event-driven automation
- **Notion MCP**: Knowledge base and agent memory persistence
- **Context7 MCP**: Regulatory documentation lookup
- **Google Workspace MCP**: Collaboration features (from Phase 4)

### Technical Constraints
- Agent Teams requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` environment variable
- Hook scripts must be compatible with shell environments (bash/zsh)
- Output format conversion requires external tools (Pandoc, wkhtmltopdf)

---

**END OF SPEC-ARIA-005/spec.md**
