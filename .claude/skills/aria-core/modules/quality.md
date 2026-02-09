# ARIA Quality Framework Module

## VALID Framework Implementation

This module provides detailed implementation guidance for the VALID quality framework used across all ARIA regulatory deliverables.

---

## VALID Framework Overview

VALID is ARIA's quality framework ensuring all regulatory deliverables meet the highest standards of regulatory compliance and audit readiness.

| Dimension | Definition | Verification Method | Critical Attributes |
|-----------|-----------|-------------------|-------------------|
| **V**erified | Content matches source regulation text | Cross-reference with regulation originals | Citations, accuracy, completeness |
| **A**ccurate | Data, figures, and references are correct and current | Source validation, date checks | Currency, precision, sources |
| **L**inked | Traceability between requirements, documents, and evidence | Traceability matrix verification | Links, cross-references, dependencies |
| **I**nspectable | Audit trail maintained, decision rationale documented | Audit trail completeness check | History, rationale, change tracking |
| **D**eliverable | Output meets submission format requirements | Template conformance check | Format, structure, completeness |

---

## V - Verified

### Definition

Content matches source regulation text without misinterpretation or misquotation.

### Verification Criteria

**Citation Completeness:**
- All regulatory claims include citations
- Citations follow standard format
- No uncited regulatory statements

**Citation Accuracy:**
- Standard/regulation name correct
- Section/paragraph identifier accurate
- Version/date information current

**Content Accuracy:**
- Quotations match source text exactly
- Interpretations are defensible
- No quotes taken out of context

**Source Verification:**
- Cross-reference with original regulations
- Use Context7 MCP for up-to-date sources
- Verify against official agency publications

### Verification Process

1. **Automated Checks (via manager-quality):**
   - Scan for uncited regulatory claims
   - Validate citation format consistency
   - Check citation completeness

2. **Manual Review (via expert-reviewer):**
   - Cross-reference sample citations with originals
   - Verify critical regulatory statements
   - Validate interpretation accuracy

3. **Source Validation (via expert-researcher):**
   - Verify source currency via Context7 MCP
   - Check for regulatory updates
   - Confirm official publication status

### Citation Standard Format

```
[Standard/Regulation Name], Section [X.Y]: [Requirement text]
Reference: [Full citation with version/date, URL if applicable]

Examples:
- FDA 21 CFR Part 820, Section 820.30: "Each manufacturer shall establish and maintain procedures for design control."
- ISO 13485:2016, Clause 8.3: "The organization shall document a procedure for design and development..."
- EU MDR 2017/745, Annex I, 23.1(u): "Demonstration of conformity with the general safety and performance requirements..."
```

### Common Verification Failures

- Missing citations for regulatory claims
- Outdated regulatory versions
- Incorrect section/paragraph references
- Misquotations or out-of-context quotes
- Unsupported interpretations

### Success Metrics

- 100% of regulatory claims cited
- 100% of citations match source text
- 100% of sources current (within 6 months or latest version)
- Zero unsupported interpretations

---

## A - Accurate

### Definition

Data, figures, tables, calculations, and references are correct, current, and properly sourced.

### Verification Criteria

**Data Accuracy:**
- Numerical values correct
- Units of measure correct
- Calculations verified
- Statistical analysis valid

**Figure/Table Accuracy:**
- Figures accurately represent data
- Tables correctly organized
- Labels and legends clear
- Source data traceable

**Reference Currency:**
- References are current
- Latest versions cited
- Publication dates verified
- URLs/access paths valid

**Source Validation:**
- Primary sources preferred
- Secondary sources validated
- Source reliability confirmed
- Conflicting sources resolved

### Verification Process

1. **Data Validation (via expert-analyst):**
   - Verify calculations and statistical analyses
   - Cross-check numerical values
   - Validate units and conversions
   - Review statistical methodology

2. **Figure/Table Review (via expert-reviewer):**
   - Verify figure accuracy
   - Check table calculations
   - Validate labels and legends
   - Confirm source data references

3. **Reference Check (via expert-researcher):**
   - Verify reference currency
   - Check source reliability
   - Validate URLs and access paths
   - Confirm latest versions cited

4. **Cross-Reference Validation (via manager-quality):**
   - Check internal consistency
   - Verify cross-references
   - Validate data flow between sections
   - Confirm table/figure references

### Accuracy Standards

**Numerical Data:**
- Significant figures appropriate
- Rounding consistent
- Units clearly stated
- Calculations shown or referenced

**Figures and Tables:**
- Clear, readable format
- Properly labeled axes/columns
- Legends explain all elements
- Source cited where applicable

**References:**
- Primary sources preferred
- Latest version cited
- Publication date included
- Access information provided

### Common Accuracy Failures

- Calculation errors
- Unit conversion mistakes
- Outdated references
- Misleading figures/charts
- Inconsistent data across sections

### Success Metrics

- 100% of calculations verified
- 100% of figures/tables accurate
- 100% of references current (within acceptable period)
- Zero data inconsistencies

---

## L - Linked

### Definition

Traceability established between requirements, documents, evidence, and related artifacts.

### Verification Criteria

**Traceability Matrix:**
- Requirements mapped to document sections
- Document sections linked to evidence
- Test methods linked to requirements
- Changes linked to justification

**Cross-References:**
- Document cross-references valid
- Section references accurate
- Figure/table references correct
- External references accessible

**Dependency Mapping:**
- Upstream dependencies identified
- Downstream impacts documented
- Prerequisite requirements linked
- Related documents cross-referenced

**Evidence Links:**
- Requirements linked to evidence
- Test results linked to requirements
- Compliance statements supported
- Decisions supported by evidence

### Verification Process

1. **Traceability Matrix Creation (via manager-docs):**
   - Map requirements to document sections
   - Link sections to evidence
   - Connect test methods to requirements
   - Establish change traceability

2. **Cross-Reference Validation (via expert-reviewer):**
   - Verify all cross-references valid
   - Check section references accurate
   - Confirm figure/table references correct
   - Test external references accessible

3. **Dependency Analysis (via domain agents):**
   - Identify upstream dependencies
   - Document downstream impacts
   - Map prerequisite relationships
   - Link related documents

4. **Evidence Link Verification (via manager-quality):**
   - Verify requirement-evidence links
   - Confirm test-result links
   - Validate compliance statement support
   - Check decision evidence support

### Traceability Matrix Structure

**Standard Template:**
```
| Requirement ID | Requirement Summary | Document Section | Evidence Location | Status |
|----------------|-------------------|------------------|-------------------|---------|
| REQ-001 | Device shall meet ISO 13485 Clause 8.3 | Section 4.2 | QMS Manual, Section 8.3 | Verified |
| REQ-002 | Software lifecycle per IEC 62304 | Section 5.1 | Software Lifecycle Plan | Verified |
```

**Link Types:**
- Requirement to Document Section
- Document Section to Evidence
- Test Method to Requirement
- Change to Justification
- Dependency to Dependent Item

### Common Link Failures

- Orphan requirements (no document section mapped)
- Unsubstantiated claims (no evidence linked)
- Broken cross-references
- Missing dependency documentation
- Unexplained changes

### Success Metrics

- 100% of requirements linked to document sections
- 100% of compliance statements supported by evidence
- 100% of cross-references valid
- 100% of dependencies documented

---

## I - Inspectable

### Definition

Audit trail maintained, decision rationale documented, and change history complete.

### Verification Criteria

**Audit Trail:**
- All changes tracked and dated
- Change authors identified
- Change justification documented
- Approval history maintained

**Decision Rationale:**
- Regulatory decisions explained
- Trade-offs documented
- Alternatives considered
- Risk-based rationale included

**Revision History:**
- Version numbers sequential
- Change descriptions clear
- Revision dates recorded
- Previous versions archived

**Approvals:**
- Reviewers identified
- Approval dates recorded
- Approval criteria documented
- Rejections with reasons

### Verification Process

1. **Audit Trail Review (via manager-quality):**
   - Verify all changes tracked
   - Confirm change documentation complete
   - Check approval history
   - Validate version control

2. **Decision Rationale Check (via expert-reviewer):**
   - Verify regulatory decisions explained
   - Check trade-off documentation
   - Confirm alternatives considered
   - Validate risk-based rationale

3. **Revision History Audit (via manager-docs):**
   - Confirm version sequence correct
   - Check change descriptions clear
   - Verify revision dates recorded
   - Confirm previous versions archived

4. **Approval Verification (via manager-project):**
   - Verify reviewer identification
   - Check approval dates recorded
   - Confirm approval criteria documented
   - Validate rejection reasons (if any)

### Audit Trail Requirements

**Change Documentation:**
- Change description (what changed)
- Rationale (why changed)
- Author (who changed)
- Date (when changed)
- Approval (who approved)

**Decision Documentation:**
- Decision statement
- Regulatory basis
- Alternatives considered
- Risk assessment
- Rationale justification

**Revision Control:**
- Version numbering (e.g., 1.0, 1.1, 2.0)
- Change log
- Version dates
- Previous version archive

### Common Inspectability Failures

- Undocumented changes
- Missing decision rationale
- Incomplete revision history
- Unapproved changes
- Missing approval records

### Success Metrics

- 100% of changes documented with rationale
- 100% of decisions explained
- 100% of revisions tracked
- 100% of approvals recorded

---

## D - Deliverable

### Definition

Output meets submission format requirements, template compliance, and completeness standards.

### Verification Criteria

**Template Compliance:**
- Correct template used
- Template sections complete
- Template formatting followed
- Required content included

**Format Requirements:**
- Submission format correct (eCopy, PDF, etc.)
- File naming convention followed
- File structure requirements met
- Submission organization correct

**Completeness:**
- All required sections present
- All annexes/appendices included
- All required forms attached
- All declarations included

**Submission Readiness:**
- Package structure verified
- File integrity confirmed
- Submission checklist complete
- Review package prepared

### Verification Process

1. **Template Compliance Check (via expert-writer):**
   - Verify correct template used
   - Check all template sections complete
   - Confirm template formatting followed
   - Validate required content included

2. **Format Validation (via manager-docs):**
   - Verify submission format correct
   - Check file naming convention
   - Validate file structure
   - Confirm submission organization

3. **Completeness Review (via expert-reviewer):**
   - Check all required sections present
   - Verify all annexes/appendices included
   - Confirm all required forms attached
   - Validate all declarations included

4. **Submission Readiness (via manager-quality):**
   - Verify package structure
   - Confirm file integrity
   - Complete submission checklist
   - Prepare review package

### Format Specifications

**510(k) Submission:**
- eCopy format with Section 10-12 structure
- PDF with searchable text
- Specific file naming: [510(k) Number]_[Device Name]_Submission
- Organized by FDA 510(k) format requirements

**PMA Submission:**
- Modular PMA format
- PDF with bookmarks and hyperlinks
- Specific organization: Administrative, Nonclinical, Clinical
- Module-specific file naming

**CE Technical Documentation:**
- Annex II structure
- PDF with hyperlinked table of contents
- Essential Requirements checklist
- Clinical Evaluation Report

**MFDS Submission:**
- Korean language requirements
- Specific form structure
- PDF with bookmarks
- Organized per MFDS guidelines

### Common Deliverable Failures

- Wrong template used
- Missing required sections
- Incorrect format
- Incomplete annexes/appendices
- Missing required forms

### Success Metrics

- 100% template compliance
- 100% format requirements met
- 100% required content included
- 100% submission checklist complete

---

## VALID Verification Workflow

### Overall Process

1. **Pre-Verification (manager-quality):**
   - Verify document complete
   - Check preliminary VALID compliance
   - Identify potential issues

2. **Dimension-Specific Verification (expert agents):**
   - V: expert-researcher + expert-reviewer
   - A: expert-analyst + expert-reviewer
   - L: manager-docs + expert-reviewer
   - I: manager-quality + manager-docs
   - D: expert-writer + manager-docs

3. **Integration Verification (manager-quality):**
   - Verify overall VALID compliance
   - Check cross-dimension consistency
   - Identify residual issues

4. **Final Approval (orchestrator):**
   - Review VALID verification report
   - Confirm all dimensions passed
   - Obtain user approval

### Verification Report Structure

**Executive Summary:**
- Overall VALID status (Pass/Fail)
- Critical issues (if any)
- Recommendations (if needed)

**Dimension Results:**
- V: Verified - Status, findings, metrics
- A: Accurate - Status, findings, metrics
- L: Linked - Status, findings, metrics
- I: Inspectable - Status, findings, metrics
- D: Deliverable - Status, findings, metrics

**Detailed Findings:**
- Issue description
- Severity level
- Recommended action
- Responsible agent

**Approval Status:**
- Dimension approvals
- Overall approval
- User approval required

---

## Quality Metrics and Reporting

### Key Performance Indicators

**VALID Pass Rate:**
- Target: 100% on first submission
- Measurement: Dimension pass rate at final verification

**Verification Cycle Time:**
- Target: < 2 hours for typical document
- Measurement: Time from Execute complete to Deliver approved

**Defect Rate:**
- Target: < 5% of documents require rework
- Measurement: Documents requiring post-verification corrections

**User Satisfaction:**
- Target: > 90% approval rate on first review
- Measurement: User approval at Deliver phase

### Reporting

**Quality Dashboard (via Notion):**
- VALID pass rate by document type
- Verification cycle time trends
- Defect rate by dimension
- User approval trends

**Quality Reports:**
- Monthly VALID summary
- Quarterly quality review
- Annual quality improvement plan

---

## Continuous Improvement

### Feedback Collection

- User feedback at approval checkpoints
- Post-delivery quality surveys
- Audit finding analysis
- Regulatory agency feedback

### Improvement Process

1. Identify improvement opportunities from feedback
2. Analyze root causes of VALID failures
3. Implement corrective actions
4. Update VALID verification procedures
5. Train agents on updated procedures

---

## Module Status

- V - Verified: Fully specified (Phase 1)
- A - Accurate: Fully specified (Phase 1)
- L - Linked: Fully specified (Phase 1)
- I - Inspectable: Fully specified (Phase 1)
- D - Deliverable: Fully specified (Phase 1)
- Workflow: Fully specified (Phase 1)
- Metrics: Fully specified (Phase 1)

---

Version: 1.0.0 (Phase 1 Scaffold)
Last Updated: 2026-02-09
