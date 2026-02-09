# ARIA Workflow Module

## Brief-Execute-Deliver Detailed Specifications

This module provides detailed specifications for each phase of the ARIA Brief-Execute-Deliver workflow.

---

## BRIEF Phase Specifications

### Phase Entry

Trigger: User invokes `/aria brief` or natural language request indicating new regulatory task.

### Objectives

1. **Intent Analysis**: Understand user's regulatory objectives and constraints
2. **Scope Definition**: Establish clear boundaries and deliverables
3. **Regulatory Mapping**: Identify applicable regulations and standards
4. **Action Planning**: Create structured plan with agent assignments

### Detailed Process

#### 1. Intent Analysis

**Tasks:**
- Parse natural language request for regulatory intent
- Classify task type using decision tree:
  - Document creation: Protocols, reports, submissions
  - Analysis: Gap assessment, compliance verification, interpretation
  - Review: Document review, approval, audit preparation
  - Submission: 510(k), PMA, CE, MFDS package preparation
- Identify domain keywords (FDA, MDR, ISO, risk, design control, CAPA)
- Detect urgency and timeline constraints
- Flag any ambiguities requiring clarification

**Output:**
- Task classification (document/analysis/review/submission)
- Primary domain identification
- Initial complexity assessment (low/medium/high)
- List of clarifying questions (if any)

#### 2. Scope Definition

**Tasks:**
- Ask targeted questions via AskUserQuestion (max 4 options each)
- Define deliverables and acceptance criteria
- Establish timeline and milestone requirements
- Identify dependencies and prerequisites
- Document assumptions and constraints

**Clarification Questions:**
- Device type and intended use
- Target markets (US FDA, EU CE, Korea MFDS, other)
- Existing documentation status
- Timeline constraints and submission deadlines

**Output:**
- Defined scope statement
- Deliverable list with acceptance criteria
- Timeline with key milestones
- Assumptions and constraints documented

#### 3. Regulatory/Standards Mapping

**Tasks:**
- Identify applicable regulations by market:
  - US: 21 CFR Part 820 (QSR), 21 CFR Part 807/812 (Submissions)
  - EU: MDR 2017/745, IVDR 2017/746
  - Korea: MFDS Medical Device Act, Enforcement Rules
- Identify applicable standards:
  - QMS: ISO 13485:2016
  - Risk: ISO 14971:2019
  - Software: IEC 62304:2006/A1:2010
  - Usability: IEC 62366-1:2015
  - Safety: IEC 60601 series (if electrical)
  - Biocompatibility: ISO 10993 series
- Map regulatory requirements to task objectives
- Identify requirement conflicts or gaps

**Output:**
- Regulatory requirement matrix
- Standard applicability list
- Requirement mapping to deliverables
- Identified gaps or conflicts

#### 4. Action Planning

**Tasks:**
- Determine required agent sequence and dependencies
- Plan approval checkpoints (mandatory checkpoints identified)
- Assign VALID quality gate verification points
- Create task breakdown with assignments
- Estimate effort and timeline
- Get user approval to proceed

**Approval Checkpoints:**
- Regulatory pathway selection
- Predicate device selection (if applicable)
- Risk acceptability criteria
- Clinical evaluation strategy
- Final deliverable approval

**Output:**
- Detailed action plan
- Agent assignment sequence
- Approval checkpoint schedule
- VALID verification schedule
- User approval obtained

### Phase Exit Criteria

- [ ] Task scope clearly defined and documented
- [ ] Applicable regulations and standards identified
- [ ] Action plan created and approved by user
- [ ] All assumptions documented
- [ ] Regulatory requirements mapped to deliverables
- [ ] Approval checkpoints scheduled

### Deliverables

- Scope definition document
- Regulatory requirement matrix
- Action plan with agent assignments
- User approval record

---

## EXECUTE Phase Specifications

### Phase Entry

Trigger: User invokes `/aria execute` or Brief phase completes with user approval.

### Objectives

1. **Research**: Gather regulatory information and precedents
2. **Draft**: Create regulatory content using templates
3. **Review**: Verify compliance against regulations
4. **Refine**: Incorporate feedback and strengthen evidence

### Detailed Process

#### 1. Research

**Agent:** expert-researcher + domain agent

**Tasks:**
- Search regulatory databases for current requirements
- Find predicate devices and precedents (via Context7 MCP)
- Retrieve regulatory guidance and standards (via Context7 MCP)
- Research regulatory interpretations and enforcement trends
- Compile relevant regulatory citations

**Data Sources:**
- FDA website (Device databases, guidance documents)
- EUDAMED and EU regulatory notices
- MFDS website and Korean regulations
- ISO and IEC standard publications (via Context7 MCP)
- Regulatory agency enforcement manuals

**Output:**
- Regulatory research summary
- Relevant citation list with full references
- Predicate device analysis (if applicable)
- Interpretation notes and precedents

#### 2. Draft

**Agent:** expert-writer + domain agent

**Tasks:**
- Select appropriate document template
- Translate regulatory requirements into document content
- Ensure regulatory citation compliance (all claims cited)
- Maintain clear, concise technical writing
- Establish traceability (requirements to sections)
- Create cross-references between documents

**Template Types:**
- Protocols: Validation, verification, clinical investigation
- Reports: Test reports, summary reports, evaluation reports
- Submissions: 510(k), PMA, CE Technical File, MFDS
- Records: DHF, DMR, DHR, risk files, CAPA files

**Citation Format:**
```
[Standard/Regulation Name], Section [X.Y]: [Requirement text]
Reference: [Full citation with version/date]
```

**Output:**
- Draft document with regulatory citations
- Traceability matrix (requirements to document sections)
- Cross-reference list
- Figures/tables with source citations

#### 3. Review

**Agent:** expert-reviewer + domain agent

**Tasks:**
- Verify compliance against source regulations
- Check regulatory citation accuracy and completeness
- Validate technical content accuracy
- Verify traceability matrix completeness
- Identify gaps, inconsistencies, or ambiguities
- Cross-check against templates and precedents

**Review Checklist:**
- [ ] All regulatory claims cited correctly
- [ ] Citations are current and accurate
- [ ] Technical content is accurate
- [ ] Traceability matrix is complete
- [ ] No gaps or inconsistencies
- [ ] Cross-references are valid
- [ ] Template compliance verified

**Output:**
- Review findings document
- Discrepancy list with recommendations
- Updated regulatory citations (if needed)
- Approval/rejection determination

#### 4. Refine

**Agent:** expert-writer + domain agent (iterative)

**Tasks:**
- Incorporate review feedback
- Strengthen evidence and rationale
- Update regulatory citations
- Improve clarity and completeness
- Re-verify after changes
- Iterate until VALID criteria met

**Refinement Criteria:**
- Address all review findings
- Strengthen weak or unsupported claims
- Update outdated or incorrect citations
- Improve document flow and clarity
- Ensure VALID dimension compliance

**Output:**
- Refined document meeting VALID criteria
- Updated traceability matrix
- Change log documenting revisions
- Ready for DELIVER phase

### Phase Exit Criteria

- [ ] All regulatory requirements addressed
- [ ] Regulatory citations complete and accurate
- [ ] Content validated against source regulations
- [ ] Document traceability established
- [ ] All review findings resolved
- [ ] VALID draft quality achieved

### Deliverables

- Research summary with citations
- Draft regulatory document
- Review findings and resolutions
- Refined document ready for validation
- Traceability matrix
- Change log

---

## DELIVER Phase Specifications

### Phase Entry

Trigger: User invokes `/aria deliver` or Execute phase completes with VALID draft.

### Objectives

1. **VALID Verification**: Verify all five quality dimensions
2. **Format Conversion**: Apply required submission formats
3. **Distribution**: Export to Notion and distribute to stakeholders
4. **Knowledge Update**: Update knowledge base with learnings

### Detailed Process

#### 1. VALID Verification

**Agent:** manager-quality + expert-reviewer

**Verification Process:**

**V - Verified**
- Cross-reference all content with regulation originals
- Verify no misinterpretation or misquotation
- Check that all claims match source text
- Validate citation accuracy and completeness

**Checks:**
- [ ] All regulatory text matches source
- [ ] Citations reference correct sections
- [ ] No quotes taken out of context
- [ ] Interpretations are defensible

**A - Accurate**
- Validate all data, figures, and references
- Confirm currency as of verification date
- Check calculations and analyses
- Verify dates and version numbers

**Checks:**
- [ ] Data sources validated
- [ ] Figures and tables accurate
- [ ] References are current
- [ ] Calculations verified
- [ ] Dates and versions correct

**L - Linked**
- Verify traceability matrix completeness
- Check cross-references between documents
- Validate requirement-to-evidence links
- Ensure document interdependencies documented

**Checks:**
- [ ] Traceability matrix complete
- [ ] Cross-references valid
- [ ] Requirement links established
- [ ] Document interdependencies mapped

**I - Inspectable**
- Confirm audit trail maintained
- Verify decision rationale documented
- Check change tracking and justification
- Ensure revision history complete

**Checks:**
- [ ] Audit trail maintained
- [ ] Decisions documented with rationale
- [ ] Changes tracked and justified
- [ ] Revision history complete

**D - Deliverable**
- Check template conformance
- Verify required format compliance
- Confirm annexes and appendices complete
- Validate submission package structure

**Checks:**
- [ ] Template conformance verified
- [ ] Format requirements met
- [ ] Annexes/appendices complete
- [ ] Package structure correct

**Output:**
- VALID verification report
- Discrepancy list (if any)
- Approval for delivery

#### 2. Format Conversion

**Agent:** expert-writer + manager-docs

**Tasks:**
- Apply submission-specific formatting:
  - 510(k): eCopy format, Section 10-12 structure
  - PMA: Modular PMA format, specific organization
  - CE: Annex II/Annex VII Technical Documentation structure
  - MFDS: Korean submission format requirements
- Generate required annexes and appendices
- Create submission package with proper organization
- Generate review package for user

**Format Specifications:**

**510(k) Submission:**
- Section 10: Indications for Use
- Section 11: Substantial Equivalence Discussion
- Section 12: Truthful and Accurate Statement
- Attachments: Declarations, certifications, 510(k) Statement

**PMA Submission:**
- Administrative information
- Device description and classification
- Nonclinical studies
- Clinical studies
- Manufacturing information

**CE Technical Documentation:**
- Annex II: Technical Documentation
- Annex VII: Summary of Safety and Clinical Performance
- Essential requirements checklist
- Clinical evaluation report

**MFDS Submission:**
- Application form
- Technical documentation
- Clinical data (if required)
- Quality management system documentation

**Output:**
- Formatted submission package
- Review package for user approval
- Format compliance checklist

#### 3. Distribution

**Agent:** manager-docs + orchestrator

**Tasks:**
- Export to Notion knowledge hub:
  - Create document pages with proper hierarchy
  - Update document registry
  - Link to related documents and requirements
- Distribute to stakeholders (if configured):
  - Email notification
  - Assign reviewers
  - Set due dates
- Archive supporting materials:
  - Research notes
  - Reference documents
  - Calculation files
- Create delivery record

**Notion Integration:**
- Document Registry Database
- CAPA Tracker (if applicable)
- Risk Register (if applicable)
- Project Timeline Database
- Submission Package Storage

**Output:**
- Documents exported to Notion
- Document registry updated
- Stakeholders notified (if applicable)
- Delivery record created

#### 4. Knowledge Base Update

**Agent:** expert-researcher + manager-docs

**Tasks:**
- Extract key learnings and insights
- Update precedents database:
  - Predicate device information
  - Successful regulatory strategies
  - Enforcement trends
- Log regulatory interpretations:
  - New interpretations discovered
  - Ambiguities clarified
  - Agency feedback incorporated
- Record citations for future reference:
  - New citation templates
  - Updated citation versions
  - Reusable content blocks

**Knowledge Base Components:**
- Precedents Database
- Regulatory Interpretations Log
- Citation Library
- Lessons Learned Repository
- Best Practices Archive

**Output:**
- Knowledge base updated
- Precedents logged
- Interpretations recorded
- Citations archived

### Phase Exit Criteria

- [ ] VALID quality gates passed
- [ ] User approval obtained
- [ ] Deliverable in required format
- [ ] Knowledge base updated
- [ ] Audit trail complete
- [ ] Documents stored in Notion

### Deliverables

- VALID verification report
- Formatted submission package
- Review package for user
- Documents in Notion knowledge hub
- Updated knowledge base
- Delivery confirmation

---

## Phase Transition Rules

### Brief to Execute

**Trigger:** User approves action plan

**Conditions:**
- Scope clearly defined
- Regulations/standards mapped
- Action plan approved
- Checkpoints scheduled

**Handoff:**
- Scope document
- Regulatory matrix
- Action plan
- Approval record

### Execute to Deliver

**Trigger:** Draft passes VALID preliminary check

**Conditions:**
- All requirements addressed
- Regulatory citations complete
- Content validated
- Traceability established

**Handoff:**
- Refined document
- Traceability matrix
- Change log
- Research summary

### Deliver to Complete

**Trigger:** User approves final deliverable

**Conditions:**
- VALID verification passed
- Format conversion complete
- Distribution successful
- Knowledge base updated

**Handoff:**
- Final deliverable package
- VALID verification report
- Delivery confirmation
- Lessons learned

---

## Error Handling by Phase

### Brief Phase Errors

**Ambiguous User Request:**
- Ask targeted clarification questions
- Provide examples of similar tasks
- Offer multiple interpretation options

**Regulatory Conflict:**
- Identify conflicting requirements
- Research regulatory precedence
- Present options to user for decision

**Insufficient Information:**
- Request specific missing information
- Provide examples of required information
- Allow user to proceed with assumptions

### Execute Phase Errors

**Research Gaps:**
- Use Sequential Thinking MCP for complex analysis
- Consult multiple regulatory sources
- Document assumptions clearly

**Template Issues:**
- Select most appropriate alternative template
- Customize template with user approval
- Document template modifications

**Review Failures:**
- Identify specific non-compliance areas
- Provide corrective guidance
- Re-review after corrections

### Deliver Phase Errors

**VALID Failures:**
- Identify failed dimension(s)
- Provide specific corrective requirements
- Re-verify after corrections

**Format Issues:**
- Identify specific format non-compliance
- Provide formatting corrections
- Re-check format compliance

**Distribution Errors:**
- Retry distribution with exponential backoff
- Verify Notion connection and permissions
- Fall back to local storage if needed

---

## Module Status

- BRIEF Phase: Fully specified (Phase 1)
- EXECUTE Phase: Fully specified (Phase 1)
- DELIVER Phase: Fully specified (Phase 1)
- Transitions: Fully specified (Phase 1)
- Error Handling: Fully specified (Phase 1)

---

Version: 1.0.0 (Phase 1 Scaffold)
Last Updated: 2026-02-09
