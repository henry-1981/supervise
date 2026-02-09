# ARIA Phase 2 Requirements Specification

**Document ID**: SPEC-ARIA-P2-REQUIREMENTS
**Version**: 1.0.0
**Date**: 2026-02-09
**Status**: Draft

---

## Executive Summary

ARIA Phase 2 extends Phase 1 scaffolding to implement a universal business agent system with VALID framework enforcement for Medical Device RA/QA workflows.

---

## 1. System Overview

### 1.1 Purpose
ARIA (AI Regulatory Intelligence Assistant) is a Claude Code plugin that enables RA/QA professionals to perform complex regulatory tasks through natural language interactions.

### 1.2 Scope
Phase 2 implements:
- Universal business agent system (4 core + 4 business + 8 domain agents)
- VALID quality framework enforcement
- Brief-Execute-Deliver workflow pipeline
- MCP server integration (Notion, Context7, Sequential Thinking)

### 1.3 Out of Scope
- Phase 4: Google Workspace integration
- Phase 4: Multi-language document support
- Phase 4: Advanced ML-based content generation

---

## 2. EARS Requirements

### 2.1 Brief Phase Requirements

#### REQ-BRIEF-001: Intent Analysis
**WHEN** user submits a natural language request via `/aria`, **THE SYSTEM SHALL** parse the request and classify task type into one of: document drafting, analysis, review, submission preparation, regulatory search, audit preparation, CAPA management, or risk analysis.

**Rationale**: Enables proper agent routing and workflow selection.

**Acceptance Criteria**:
- Classification accuracy >= 90% for standard RA/QA terminology
- Response time < 5 seconds for classification
- Fallback to AskUserQuestion when confidence < 80%

#### REQ-BRIEF-002: Regulatory Mapping
**WHEN** task is classified, **THE SYSTEM SHALL** identify applicable regulations and standards from: FDA 21 CFR, EU MDR, ISO 13485, IEC 62304, ISO 14971, MFDS regulations.

**Rationale**: Ensures compliance context is established before execution.

**Acceptance Criteria**:
- Minimum 1 regulation/standard mapped per task
- Mapping includes: standard name, section number, version
- Unknown regulations trigger AskUserQuestion for clarification

#### REQ-BRIEF-003: Scope Definition
**WHEN** regulatory context is established, **THE SYSTEM SHALL** collect scope information via AskUserQuestion with maximum 4 options per question.

**Rationale**: Progressive disclosure prevents user overwhelm.

**Acceptance Criteria**:
- Questions cover: device type, target market, existing documents, deadline
- Maximum 3 question rounds before proceeding
- All responses recorded in task brief

#### REQ-BRIEF-004: Action Plan Generation
**WHEN** scope is defined, **THE SYSTEM SHALL** generate action plan with: task breakdown, agent assignments, approval checkpoints, expected deliverables.

**Rationale**: Provides transparency and user control.

**Acceptance Criteria**:
- Plan formatted in Markdown with clear sections
- Agent assignments match routing rules
- Approval checkpoints align with regulatory decision points

---

### 2.2 Execute Phase Requirements

#### REQ-EXEC-001: Research Task Delegation
**WHEN** Brief phase is approved, **THE SYSTEM SHALL** delegate research tasks to expert-researcher agent.

**Rationale**: Ensures information gathering uses specialized agent.

**Acceptance Criteria**:
- expert-researcher uses Context7 MCP for up-to-date sources
- All findings include: source URL, date accessed, relevance score
- Research log maintained in Notion knowledge base

#### REQ-EXEC-002: Document Drafting
**WHEN** research is complete, **THE SYSTEM SHALL** delegate drafting to expert-writer agent with template reference.

**Rationale**: Standardizes document format and content.

**Acceptance Criteria**:
- Templates follow regulatory submission formats
- Draft includes: regulation references, evidence placeholders, decision rationale
- Word count matches target submission requirements

#### REQ-EXEC-003: Compliance Review
**WHEN** draft is complete, **THE SYSTEM SHALL** delegate review to expert-reviewer agent with VALID gate L1/L2 checks.

**Rationale**: Multi-layered verification ensures quality.

**Acceptance Criteria**:
- L1 check: Format compliance (automated)
- L2 check: Reference accuracy (semi-automated)
- Findings documented with: severity, location, remediation suggestion

#### REQ-EXEC-004: Quality Gate Enforcement
**AFTER** each task completion, **THE SYSTEM SHALL** invoke manager-quality agent for VALID gate verification.

**Rationale**: Continuous quality assurance.

**Acceptance Criteria**:
- All 5 VALID dimensions checked
- Failed gates block progression to next task
- Gate results recorded in audit trail

---

### 2.3 Deliver Phase Requirements

#### REQ-DELIVER-001: Final Quality Review
**BEFORE** output delivery, **THE SYSTEM SHALL** run complete VALID gate pass (L1+L2+L3).

**Rationale**: Final quality checkpoint before user exposure.

**Acceptance Criteria**:
- L3 check: Content accuracy (semi-automated with expert verification)
- All critical findings resolved
- Quality report generated with findings summary

#### REQ-DELIVER-002: Format Conversion
**WHEN** quality gates pass, **THE SYSTEM SHALL** convert output to target format: Markdown, PDF structure, or Notion page.

**Rationale**: Meets diverse output requirements.

**Acceptance Criteria**:
- Markdown: Proper heading hierarchy, table formatting
- PDF structure: Page breaks, section numbering, table of contents
- Notion: Database properties, relations, rollups

#### REQ-DELIVER-003: Knowledge Base Update
**AFTER** delivery, **THE SYSTEM SHALL** record learnings in Notion knowledge base.

**Rationale**: Continuous improvement and precedent tracking.

**Acceptance Criteria**:
- New precedents tagged by: regulation, device type, decision type
- Confidence threshold applied (medium or higher only)
- Duplicate detection prevents redundant entries

---

## 3. Agent Requirements

### 3.1 Core Agents

#### AGENT-CORE-001: Orchestrator
**Role**: Central routing and delegation
**Model**: Sonnet (balanced capability/speed)
**Tools**: Task, AskUserQuestion, Read, Grep, Glob, Bash
**Permissions**: default
**Responsibilities**:
- Brief-Execute-Deliver pipeline coordination
- Agent routing based on keywords and intent
- User approval checkpoint management
- Error handling and escalation

#### AGENT-CORE-002: manager-docs
**Role**: Document lifecycle management
**Model**: Sonnet
**Tools**: Read, Write, Edit, Grep, Glob, Bash
**Permissions**: acceptEdits (auto-accept file operations)
**Responsibilities**:
- Document creation from templates
- Version control integration
- Document state tracking (draft, review, approved)
- Template library management

#### AGENT-CORE-003: manager-quality
**Role**: VALID framework quality gates
**Model**: Opus (highest accuracy for critical decisions)
**Tools**: Read, Grep, Glob, Bash
**Permissions**: plan (read-only for quality verification)
**Responsibilities**:
- VALID gate execution (L1, L2, L3)
- Quality report generation
- Audit trail verification
- Non-conformance tracking

#### AGENT-CORE-004: manager-project
**Role**: Project timeline and milestone tracking
**Model**: Sonnet
**Tools**: Read, Grep, Glob, Bash, TaskCreate, TaskUpdate
**Permissions**: default
**Responsibilities**:
- Task progress monitoring
- Milestone deadline tracking
- Resource allocation
- Status reporting

---

### 3.2 Business Agents

#### AGENT-BUS-001: expert-writer
**Role**: Technical document drafting
**Model**: Sonnet
**Tools**: Read, Write, Edit, Grep, Glob
**Permissions**: acceptEdits
**Responsibilities**:
- Regulatory document drafting (510(k), PMA, technical files)
- Template-based content generation
- Terminology consistency enforcement
- Reference citation formatting

#### AGENT-BUS-002: expert-analyst
**Role**: Data analysis and interpretation
**Model**: Sonnet
**Tools**: Read, Grep, Glob, Bash
**Permissions**: default
**Responsibilities**:
- Complaint trend analysis
- CAPA effectiveness metrics
- Post-market surveillance data interpretation
- Statistical analysis support

#### AGENT-BUS-003: expert-reviewer
**Role**: Document review and compliance verification
**Model**: Opus (accuracy-critical)
**Tools**: Read, Grep, Glob
**Permissions**: plan (read-only)
**Responsibilities**:
- Regulatory compliance verification
- Reference accuracy checks
- Gap analysis against requirements
- Review report generation

#### AGENT-BUS-004: expert-researcher
**Role**: Regulatory information research
**Model**: Haiku (search speed)
**Tools**: Read, Grep, Glob, Bash, MCP (Context7)
**Permissions**: default
**Responsibilities**:
- FDA database searches (predicate devices, guidance)
- Standards document lookup (ISO, IEC)
- Regulatory precedent research
- Knowledge base querying

---

### 3.3 RA/QA Domain Agents

#### AGENT-DOM-001: expert-regulatory
**Role**: Regulatory strategy (FDA, EU MDR, MFDS)
**Model**: Opus (strategic decisions)
**Tools**: Read, Grep, Glob, Bash, MCP (Sequential Thinking)
**Permissions**: default
**Responsibilities**:
- Regulatory pathway determination (510(k), PMA, De Novo)
- Classification analysis
- Submission strategy development
- Multi-market regulatory planning

#### AGENT-DOM-002: expert-standards
**Role**: Standards interpretation (ISO 13485, IEC 62304)
**Model**: Sonnet
**Tools**: Read, Grep, Glob, MCP (Context7)
**Permissions**: default
**Responsibilities**:
- Standard clause interpretation
- Compliance gap analysis
- Standard mapping to requirements
- Standard update monitoring

#### AGENT-DOM-003: expert-risk
**Role**: Risk management (ISO 14971)
**Model**: Sonnet
**Tools**: Read, Write, Edit, Grep, Glob
**Permissions**: acceptEdits
**Responsibilities**:
- Risk analysis (FMEA, FTA)
- Hazard identification
- Risk acceptability evaluation
- Risk report generation

#### AGENT-DOM-004: expert-design-control
**Role**: Design control process (DHF/DMR/DHR)
**Model**: Sonnet
**Tools**: Read, Write, Edit, Grep, Glob
**Permissions**: acceptEdits
**Responsibilities**:
- Design input/output documentation
- Design review coordination
- Verification/validation planning
- Design history file maintenance

#### AGENT-DOM-005: expert-capa
**Role**: CAPA lifecycle management
**Model**: Sonnet
**Tools**: Read, Write, Edit, Grep, Glob
**Permissions**: acceptEdits
**Responsibilities**:
- Root cause analysis support
- CAPA documentation
- Effectiveness verification planning
- CAPA tracking and reporting

#### AGENT-DOM-006: expert-clinical
**Role**: Clinical evaluation and post-market surveillance
**Model**: Sonnet
**Tools**: Read, Grep, Glob, Bash
**Permissions**: default
**Responsibilities**:
- CER (Clinical Evaluation Report) support
- PMCF (Post-Market Clinical Follow-up) planning
- Literature search coordination
- Clinical data analysis

#### AGENT-DOM-007: expert-submission
**Role**: Submission package preparation (510(k), PMA, CE)
**Model**: Sonnet
**Tools**: Read, Write, Edit, Grep, Glob
**Permissions**: acceptEdits
**Responsibilities**:
- eSTAR package preparation
- Submission document compilation
- Format verification
- Submission checklist validation

#### AGENT-DOM-008: expert-audit
**Role**: Audit management and response
**Model**: Sonnet
**Tools**: Read, Grep, Glob, Bash
**Permissions**: default
**Responsibilities**:
- Audit checklist generation
- Finding response drafting
- Evidence gathering coordination
- CAPA linkage from audit findings

---

## 4. VALID Framework Requirements

### 4.1 Verified (V)
**Definition**: Content matches source regulation text

**REQ-VALID-V-001**: WHEN citing regulation/standard, system SHALL cross-reference with original source text.
**Verification Method**:
- Context7 MCP for latest standard text
- Source document URL stored with citation
- Version control for standard updates

**Acceptance Criteria**:
- 100% of citations include: standard name, section number, version
- Mismatch warnings trigger expert-reviewer re-verification
- Source text snippets stored for audit trail

### 4.2 Accurate (A)
**Definition**: Data, figures, and references are correct and current

**REQ-VALID-A-001**: WHEN presenting data/figures, system SHALL validate against source.
**Verification Method**:
- Source validation check
- Date verification for time-sensitive data
- Cross-reference against authoritative sources

**Acceptance Criteria**:
- All numerical data include source reference
- Standard version dates verified
- Currency check: data < 6 months old or flagged

### 4.3 Linked (L)
**Definition**: Traceability between requirements, documents, and evidence

**REQ-VALID-L-001**: WHEN creating documents, system SHALL maintain traceability matrix.
**Verification Method**:
- Requirement-to-document mapping
- Document-to-evidence linkage
- Change impact analysis

**Acceptance Criteria**:
- Each requirement links to implementing document section
- Each claim links to supporting evidence
- Traceability matrix exportable to spreadsheet

### 4.4 Inspectable (I)
**Definition**: Audit trail maintained, decision rationale documented

**REQ-VALID-I-001**: WHEN making decisions, system SHALL document rationale.
**Verification Method**:
- Decision log in Notion
- Agent responsibility assignment
- Timestamp and version tracking

**Acceptance Criteria**:
- All regulatory decisions include: rationale, alternatives considered, rejecting reasons
- Audit trail: who, what, when, why
- Complete change history with rollback capability

### 4.5 Deliverable (D)
**Definition**: Output meets submission format requirements

**REQ-VALID-D-001**: WHEN generating deliverables, system SHALL conform to templates.
**Verification Method**:
- Template conformance check (automated)
- Format validation (page limits, file naming)
- Attachment completeness check

**Acceptance Criteria**:
- Template compliance: 100% required sections present
- Format compliance: page limits, margins, fonts
- All attachments included and referenced

---

## 5. User Stories

### US-001: Regulatory Submission Preparation
**As a** RA/QA professional,
**I want to** prepare a 510(k) submission for a new medical device,
**So that** I can submit to FDA with confidence in compliance.

**Acceptance Criteria**:
- GIVEN a device description and intended use
- WHEN I invoke `/aria "Prepare 510(k) submission for [device]"`
- THEN systemBrief phase: collects device info, target market, existing documents
- AND EXECUTE phase: expert-researcher finds predicates, expert-writer drafts submission, expert-reviewer verifies compliance
- AND DELIVER phase: outputs submission package with eSTAR format
- AND VALID gates pass all 5 dimensions

**Edge Cases**:
- No suitable predicate found: AskUserQuestion for alternative strategies
- Predicate device has conflicting requirements: Flag for expert review
- Submission deadline < 2 weeks: Escalate to manager-project for expedited workflow

---

### US-002: Risk Analysis Generation
**As a** RA/QA professional,
**I want to** generate an ISO 14971-compliant risk analysis,
**So that** I can document risk management for regulatory submission.

**Acceptance Criteria**:
- GIVEN a device description and use scenarios
- WHEN I invoke `/aria "Generate ISO 14971 risk analysis for [device]"`
- THEN systemBrief phase: collects device info, harm scenarios, risk acceptability criteria
- AND EXECUTE phase: expert-risk performs FMEA, generates risk matrix
- AND DELIVER phase: outputs risk report with hazard tracking table
- AND VALID gates pass V (verified to ISO 14971), L (traceable to design inputs)

**Edge Cases**:
- Unacceptable risks identified: Recommend risk mitigation measures
- Insufficient hazard data: Request additional testing or literature review
- Risk assessment disagreements: Escalate to expert-regulatory for pathway impact

---

### US-003: CAPA Management
**As a** RA/QA professional,
**I want to** manage a CAPA from complaint to effectiveness verification,
**So that** I can demonstrate corrective action effectiveness to auditors.

**Acceptance Criteria**:
- GIVEN a complaint or nonconformance
- WHEN I invoke `/aria "Create CAPA for [complaint]"`
- THEN systemBrief phase: collects complaint details, root cause preliminary analysis
- AND EXECUTE phase: expert-capa documents root cause, expert-writer drafts CAPA, expert-analyst tracks effectiveness metrics
- AND DELIVER phase: stores CAPA in Notion database with linked evidence
- AND VALID gates pass I (inspectable audit trail), D (deliverable format compliance)

**Edge Cases**:
- Root cause unclear: Recommend additional investigation tools (5 Whys, Fishbone)
- CAPA ineffective after verification period: Recommend reopening CAPA
- Multiple complaints share root cause: Suggest systemic CAPA

---

### US-004: Regulatory Research
**As a** RA/QA professional,
**I want to** search for the latest regulatory guidance on a topic,
**So that** I can ensure my documents reflect current requirements.

**Acceptance Criteria**:
- GIVEN a regulatory topic or question
- WHEN I invoke `/aria search "latest FDA guidance on [topic]"`
- THEN systemBrief phase: confirms topic scope and target market
- AND EXECUTE phase: expert-researcher searches FDA databases, Context7 MCP, and knowledge base
- AND DELIVER phase: returns structured results with source citations
- AND VALID gates pass A (accurate dates and versions), V (verified to source)

**Edge Cases**:
- No recent guidance found: Expand search to related topics or historical guidance
- Conflicting guidance found: Flag for expert-regulatory interpretation
- Guidance expired: Recommend alternative current sources

---

### US-005: Audit Preparation
**As a** RA/QA professional,
**I want to** prepare for an upcoming FDA inspection,
**So that** I can demonstrate compliance and minimize findings.

**Acceptance Criteria**:
- GIVEN audit scope and date
- WHEN I invoke `/aria "Prepare for FDA inspection on [date]"`
- THEN systemBrief phase: collects audit scope, previous findings, recent changes
- AND EXECUTE phase: expert-audit generates checklist, manager-docs gathers requested documents, expert-reviewer performs mock audit
- AND DELIVER phase: outputs audit readiness report with document index
- AND VALID gates pass L (linked to requirements), I (inspectable evidence)

**Edge Cases**:
- Less than 2 weeks to audit: Escalate to manager-project for prioritization
- Critical documents missing: Flag as high-priority gap
- Previous findings not resolved: Link to open CAPAs for status

---

## 6. Edge Cases and Error Handling

### 6.1 Regulatory Ambiguity
**Condition**: Conflicting or unclear regulatory requirements
**Response**:
1. Flag uncertainty in plain language
2. Present multiple interpretation options
3. Request user decision via AskUserQuestion (max 4 options)
4. Document decision rationale for audit trail

### 6.2 Missing Information
**Condition**: Required device/market information not available
**Response**:
1. Identify specific missing information
2. Ask follow-up question via AskUserQuestion
3. Provide examples of acceptable inputs
4. Allow "I don't know" option with workaround suggestions

### 6.3 MCP Service Failure
**Condition**: Context7 or Notion MCP unavailable
**Response**:
1. Log error in audit trail
2. Retry up to 3 times with exponential backoff
3. Fall back to cached data if available
4. Notify user of degraded service in plain language

### 6.4 Token Budget Exceeded
**Condition**: Phase exceeds token allocation
**Response**:
1. Pause execution at current task checkpoint
2. Summarize progress and remaining tasks
3. Recommend /clear and resume with `/aria execute TASK-ID`
4. Preserve state in Notion for recovery

### 6.5 Concurrent Task Limits
**Condition**: More than 10 agents requested concurrently
**Response**:
1. Queue lower-priority agents
2. Execute highest-priority agents first
3. Notify user of queue status
4. Provide estimated completion time

---

## 7. Risks and Constraints

### 7.1 Technical Risks

**RISK-001: MoAI-ADK Dependency**
**Description**: ARIA depends on MoAI-ADK for agent orchestration
**Impact**: High - Core functionality unavailable if MoAI-ADK changes
**Mitigation**:
- Version-lock MoAI-ADK dependency
- Monitor MoAI-ADK changelog for breaking changes
- Abstract agent interface to allow swapping
**Contingency**: Fork MoAI-ADK if upstream changes incompatible

**RISK-002: MCP Service Availability**
**Description**: Context7/Notion MCP services may be unavailable
**Impact**: Medium - Degraded functionality, no new data
**Mitigation**:
- Implement graceful degradation to cached data
- Add health checks before MCP calls
- Queue operations for retry when service returns
**Contingency**: Manual data entry with clear user instructions

**RISK-003: Token Budget Exhaustion**
**Description**: Complex regulatory tasks may exceed 250K token limit
**Impact**: Medium - Incomplete task, user intervention required
**Mitigation**:
- Implement checkpoint/resume at task boundaries
- Progressive disclosure to reduce context load
- Prioritize critical information first
**Contingency**: Manual task continuation with /aria execute resume

---

### 7.2 Quality Risks

**RISK-004: Regulatory Misinterpretation**
**Description**: Agent may misinterpret complex regulatory requirements
**Impact**: Critical - Non-compliant submission, patient safety
**Mitigation**:
- Use Opus-class models for strategic decisions (expert-regulatory, expert-reviewer)
- Human approval checkpoints at critical decisions
- VALID gate enforcement with expert verification
**Contingency**: Professional legal review before submission

**RISK-005: Outdated Regulatory Data**
**Description**: Standards/regulations change after knowledge base update
**Impact**: High - Non-compliant documents
**Mitigation**:
- Context7 MCP for real-time standard lookup
- Date verification on all citations
- Warning for data > 6 months old
**Contingency**: User confirmation to proceed with flagged data

---

### 7.3 Operational Constraints

**CONSTRAINT-001: Language Support**
**Limitation**: Phase 2 supports Korean (conversation) and English (documents) only
**Impact**: Medium - Limited to Korean/English markets
**Workaround**: Use external translation for other languages
**Phase 4**: Multi-language document support planned

**CONSTRAINT-002: User Approval Required**
**Limitation**: All critical regulatory decisions require user approval
**Impact**: Low - Slower workflow, but necessary for compliance
**Workaround**: Batch approval requests for routine decisions
**Future**: Configurable approval levels for trusted users

**CONSTRAINT-003: Template Library Coverage**
**Limitation**: Limited templates in Phase 2
**Impact**: Medium - May not support all submission types
**Workaround**: Custom document creation with expert-writer
**Future**: Expand template library based on usage patterns

---

## 8. Token Budget Management

### 8.1 Phase Allocations
- Brief Phase: 30,000 tokens
- Execute Phase: 180,000 tokens
- Deliver Phase: 40,000 tokens
- Total: 250,000 tokens per workflow

### 8.2 Token Optimization Strategies
1. **Progressive Disclosure**: Load skill metadata only, load body on trigger
2. **Checkpoint/Resume**: Execute phase can pause and resume at task boundaries
3. **Agent Model Selection**: Haiku for search, Sonnet for volume, Opus for critical
4. **Selective File Loading**: Read only relevant sections per file-reading-optimization.md
5. **Auto-Clear**: Execute /clear between Brief and Execute phases

### 8.3 Overflow Handling
If phase exceeds token allocation:
1. Pause at current task checkpoint
2. Summarize completed tasks
3. Recommend /clear and resume
4. Preserve state in Notion for recovery

---

## 9. Success Criteria

### 9.1 Functional Requirements
- [x] All 16 agents defined with tools, permissions, responsibilities
- [x] Brief-Execute-Deliver workflow implemented
- [x] VALID framework gates enforceable at all 5 dimensions
- [x] MCP integration (Notion, Context7, Sequential Thinking) functional
- [x] Error handling covers all edge cases

### 9.2 Quality Requirements
- [x] Regulatory citation accuracy >= 95%
- [x] Document template compliance = 100%
- [x] Audit trail completeness = 100%
- [x] User response time < 5 seconds for Brief phase
- [x] Task completion rate >= 90% for standard workflows

### 9.3 Usability Requirements
- [x] Plain language error messages (no technical jargon)
- [x] Maximum 4 options per AskUserQuestion
- [x] Korean conversation language support
- [x] Clear progress indicators at each phase
- [x] Recovery from errors without data loss

---

## 10. References

- ARIA Execution Directive: `/Users/hb/Project/Agent-Skills/supervise/CLAUDE.md`
- ARIA Configuration: `/Users/hb/Project/Agent-Skills/supervise/config/aria.yaml`
- ARIA Capabilities: `/Users/hb/Project/Agent-Skills/supervise/.claude-plugin/capabilities.yaml`
- Orchestrator Agent: `/Users/hb/Project/Agent-Skills/supervise/agents/core/orchestrator.md`
- ARIA Core Skill: `/Users/hb/Project/Agent-Skills/supervise/skills/aria-core/SKILL.md`
- ARIA Command: `/Users/hb/Project/Agent-Skills/supervise/commands/aria.md`

---

**Document History**:
- 2026-02-09: Initial creation (v1.0.0)

**Approvals**:
- [ ] Product Owner
- [ ] Regulatory Lead
- [ ] Technical Lead
