# VALID Quality Framework Documentation

## Overview

VALID is a 5-dimensional quality framework for regulatory documentation in the medical device industry. It ensures regulatory submissions meet quality standards required by FDA, EU MDR, and other regulatory authorities.

**Framework Version:** 1.0.0
**Last Updated:** 2026-02-09
**Maintained By:** ARIA Team

## Framework Dimensions

| Dimension | Definition | Key Question |
|-----------|-----------|--------------|
| **V**erified | Content matches source regulation text | Does content match source regulation text? |
| **A**ccurate | Data, figures, and references are correct and current | Are all data, figures, and references current and correct? |
| **L**inked | Traceability between requirements, documents, and evidence | Can requirements be traced to evidence? |
| **I**nspectable | Audit trail maintained, decision rationale documented | Is decision rationale documented? |
| **D**eliverable | Output meets submission format requirements | Does output meet submission format requirements? |

---

## Dimension 1: Verified (검증됨)

### Definition

Content matches source regulation text and is traceable to authoritative sources.

### Regulatory Rationale

**FDA 21 CFR 820.40** requires "procedures to control all documents and data" to ensure accuracy and prevent use of obsolete documents.

**ISO 13485:2016 Section 4.2.4** requires records to be "legible, readily identifiable and retrievable."

### Verification Criteria

| Criterion | Weight | Verification Method |
|-----------|--------|---------------------|
| Regulatory citations present | 30% | Count citations, verify format |
| Citations are accurate | 40% | Cross-reference with source regulation via Context7 MCP |
| Citations are current | 20% | Verify regulation version and effective date |
| Regulatory claims supported | 10% | Each regulatory claim has corresponding citation |

### Scoring Formula

```
Verified Score = (Citations Present × 0.3) +
                 (Citations Accurate × 0.4) +
                 (Citations Current × 0.2) +
                 (Claims Supported × 0.1)
```

### Pass Threshold

**Minimum:** 70/100 (Critical dimension - auto-fail below 70)

### Checklist

- [ ] All regulatory claims have inline citations
- [ ] Citations use standard format (e.g., `[REG: 21 CFR 820.30(a)]`)
- [ ] General claims (e.g., "FDA requires") are avoided
- [ ] Citations are hyperlinked or footnoted for traceability
- [ ] ISO standards include year (e.g., ISO 13485:2016)
- [ ] FDA CFR citations reference current CFR edition
- [ ] EU MDR citations use correct regulation number (2017/745)
- [ ] Superseded regulations are not cited

### Common Failures

- Missing citations for regulatory claims
- Outdated regulation versions (e.g., citing superseded ISO 13485:2003 instead of ISO 13485:2016)
- Incorrect section references (e.g., "21 CFR 820.40" when correct is "21 CFR 820.30")
- Web URLs instead of official regulation identifiers

### Verification Methods

**Context7 MCP Usage:**
1. Resolve library ID: `mcp__context7__resolve-library-id("FDA 21 CFR 820")`
2. Get documentation: `mcp__context7__get-library-docs(library_id, section="820.30")`
3. Compare document text with retrieved regulation text
4. Score as accurate if exact match, inaccurate if mismatch

### Common Superseded Regulations

| Superseded | Current | Transition Date |
|------------|---------|-----------------|
| ISO 13485:2003 | ISO 13485:2016 | March 2019 |
| ISO 14971:2007 | ISO 14971:2019 | September 2019 |
| MDD 93/42/EEC | MDR 2017/745 | May 2021 |
| AIMDD 90/385/EEC | MDR 2017/745 | May 2021 |
| IVDD 98/79/EC | IVDR 2017/746 | May 2022 |

### Remediation Guidance

1. Use Context7 MCP to retrieve current regulation text
2. Add inline citations using format: `[REG: 21 CFR 820.30(a)]`
3. Verify effective dates for all cited regulations
4. Replace web links with official regulation identifiers
5. Update all superseded regulations to current versions

---

## Dimension 2: Accurate (정확함)

### Definition

Data, figures, references, and factual claims are correct and current.

### Regulatory Rationale

**ISO 13485:2016 Section 4.2.4** requires records to be "legible, readily identifiable and retrievable" and protected against loss, alteration, or damage.

**FDA 21 CFR 820.40(b)** requires document approval and distribution procedures.

### Verification Criteria

| Criterion | Weight | Verification Method |
|-----------|--------|---------------------|
| Data accuracy | 40% | Cross-check numerical values with source documents |
| Reference validity | 30% | Verify all references exist and are accessible |
| Currency of information | 20% | Check publication/update dates |
| Internal consistency | 10% | Ensure no conflicting statements |

### Scoring Formula

```
Accurate Score = (Data Accuracy × 0.4) +
                 (Reference Validity × 0.3) +
                 (Currency × 0.2) +
                 (Consistency × 0.1)
```

### Pass Threshold

**Minimum:** 70/100

### Checklist

- [ ] All numerical values cross-checked with source documents
- [ ] All dates are accurate (effective dates, publication dates, test dates)
- [ ] All external references are accessible and valid
- [ ] No broken links or missing references
- [ ] Statistics and data are from current sources
- [ ] No conflicting statements within document
- [ ] Units of measurement are consistent
- [ ] Product specifications match test reports

### Common Failures

- Incorrect numerical values (e.g., wrong test results)
- Broken or missing references
- Outdated statistics or data
- Conflicting statements within the document
- Inconsistent units of measurement
- Mismatched product specifications

### Verification Methods

**Data Accuracy Check:**
1. Extract all numerical values from document
2. Cross-reference with source documents using Read tool
3. Verify calculations are correct
4. Check units of measurement consistency

**Reference Validity Check:**
1. Extract all external references (URLs, DOIs, document IDs)
2. Test each reference for accessibility
3. Verify publication dates are current
4. Check for document version consistency

**Internal Consistency Check:**
1. Use Grep tool to find conflicting statements
2. Verify terminology consistency
3. Check document cross-references are valid
4. Validate data table consistency

### Remediation Guidance

1. Verify all numerical data against source documents
2. Test all external references for accessibility
3. Update dates to reflect current information
4. Perform consistency check across all sections
5. Standardize units of measurement
6. Cross-reference product specifications with test reports

---

## Dimension 3: Linked (연결됨)

### Definition

Requirements, documents, and evidence are traceable through a traceability matrix.

### Regulatory Rationale

**IEC 62304:2006+AMD1:2015 Section 5.1.1** requires "traceability between software requirements and software system test cases."

**ISO 14971:2019** requires traceability between risks and risk controls.

**FDA 21 CFR 820.30(d)** requires design procedures include "identification of the design and development inputs."

### Verification Criteria

| Criterion | Weight | Verification Method |
|-----------|--------|---------------------|
| Traceability matrix exists | 20% | Verify matrix is present |
| Forward traceability | 30% | Requirements → Implementation → Tests |
| Backward traceability | 30% | Tests → Implementation → Requirements |
| Coverage completeness | 20% | All requirements have at least one trace |

### Scoring Formula

```
Linked Score = (Matrix Exists × 0.2) +
               (Forward Trace × 0.3) +
               (Backward Trace × 0.3) +
               (Coverage × 0.2)
```

### Pass Threshold

**Minimum:** 70/100

### Checklist

- [ ] Traceability matrix is present and accessible
- [ ] All requirements have unique IDs (e.g., REQ-001)
- [ ] Each requirement maps to design elements
- [ ] Each design element maps to verification methods
- [ ] Each verification method maps to test cases
- [ ] All test cases trace back to requirements
- [ ] No orphan requirements (requirements without tests)
- [ ] No orphan tests (tests without requirements)
- [ ] Traceability relationships are bidirectional

### Common Failures

- No traceability matrix provided
- Requirements without corresponding tests
- Tests without requirements linkage
- Incomplete coverage (orphan requirements)
- Missing requirement IDs
- Broken traceability links

### Traceability Matrix Structure

| Requirement ID | Design Element | Verification Method | Test ID | Status |
|----------------|----------------|---------------------|---------|--------|
| REQ-001 | Software Module A | Unit Test | TST-001 | Verified |
| REQ-002 | Hardware Component B | Inspection | TST-002 | Verified |
| REQ-003 | User Interface C | Usability Test | TST-003 | Verified |

### Notion Database Integration

**Traceability Database:**
- Purpose: Maintain bidirectional traceability
- Properties:
  - Requirement ID (title)
  - Description (text)
  - Design Element (relation)
  - Verification Method (select)
  - Test ID (relation)
  - Status (select: Verified, Pending, Failed)
  - Last Verified (date)

**Relationships:**
- Requirements ↔ Design Elements
- Design Elements ↔ Tests
- Requirements ↔ Tests (direct trace)

### Verification Methods

**Forward Traceability Check:**
1. Start with requirement list
2. For each requirement, verify:
   - Design element is identified
   - Verification method is defined
   - Test case is linked
3. Score: (Traced Requirements / Total Requirements) × 100

**Backward Traceability Check:**
1. Start with test case list
2. For each test case, verify:
   - Requirement is identified
   - Design element is linked
3. Score: (Traced Tests / Total Tests) × 100

**Coverage Completeness Check:**
1. Count total requirements
2. Count requirements with at least one trace
3. Score: (Covered Requirements / Total Requirements) × 100

### Remediation Guidance

1. Create traceability matrix with columns: Requirement ID, Design Element, Verification Method, Test ID
2. Ensure bidirectional traceability
3. Use consistent ID schemes (e.g., REQ-001, TST-001)
4. Mark all requirements as verified
5. Eliminate orphan requirements and orphan tests
6. Set up Notion database for dynamic traceability management

---

## Dimension 4: Inspectable (검증 가능함)

### Definition

Audit trail is maintained and decision rationale is documented.

### Regulatory Rationale

**ISO 13485:2016 Section 7.3.4** requires "Design and development review records shall include... decisions and actions taken."

**FDA 21 CFR 820.40** requires document control procedures including approval and distribution.

**EU MDR Annex XV** requires "sufficient justification and explanation" for clinical evaluation conclusions.

### Verification Criteria

| Criterion | Weight | Verification Method |
|-----------|--------|---------------------|
| Change history documented | 30% | Version control, change log present |
| Decision rationale recorded | 40% | Justification for key decisions |
| Reviewer signatures/approvals | 20% | Approval evidence exists |
| Audit trail completeness | 10% | All changes tracked |

### Scoring Formula

```
Inspectable Score = (Change History × 0.3) +
                    (Decision Rationale × 0.4) +
                    (Approvals × 0.2) +
                    (Audit Trail × 0.1)
```

### Pass Threshold

**Minimum:** 70/100

### Checklist

- [ ] Version history table is present
- [ ] Each version has date, author, and change description
- [ ] Key decisions have documented rationale
- [ ] Design Decision Records (DDRs) are present
- [ ] Approval signatures are present
- [ ] Review dates and reviewers are documented
- [ ] Audit trail is complete
- [ ] All changes are tracked with timestamps
- [ ] Notion Audit Log database is updated

### Common Failures

- Missing change history or version control
- Decisions without rationale
- No approval signatures
- Incomplete audit trail
- Missing timestamps
- Undocumented design changes

### Version History Table Structure

| Version | Date | Author | Changes | Reviewed By | Approval |
|---------|------|--------|---------|-------------|----------|
| 1.0 | 2026-01-15 | J. Smith | Initial draft | M. Johnson | Approved |
| 1.1 | 2026-01-20 | J. Smith | Added clinical data | M. Johnson | Approved |
| 1.2 | 2026-02-01 | A. Lee | Updated risk analysis | M. Johnson | Pending |

### Design Decision Record (DDR) Structure

**DDR Template:**
1. Decision ID: DDR-001
2. Date: [Decision date]
3. Decision Maker: [Name, Role]
4. Decision: [What was decided]
5. Context: [Background and problem statement]
6. Alternatives Considered: [Options evaluated]
7. Rationale: [Why this decision was made]
8. Impact: [Consequences and dependencies]
9. References: [Regulatory citations, standards]

### Notion Audit Log Database

**Audit Log Properties:**
- Timestamp (date)
- Agent (text: agent name)
- Action (select: Created, Modified, Reviewed, Approved)
- Document (relation)
- Changes (text)
- Rationale (text)
- Outcome (select: Approved, Rejected, Pending)

### Verification Methods

**Change History Check:**
1. Verify version history table exists
2. Check each version has required fields (date, author, changes)
3. Verify version numbering is sequential
4. Score: (Complete Versions / Total Versions) × 100

**Decision Rationale Check:**
1. Identify key decisions in document
2. Verify each decision has DDR
3. Check DDR completeness (all sections filled)
4. Score: (Decisions with Rationale / Total Decisions) × 100

**Approval Check:**
1. Verify approval section is present
2. Check all required signatures are present
3. Verify signature dates are after document dates
4. Score: (Valid Approvals / Required Approvals) × 100

**Audit Trail Check:**
1. Verify Notion Audit Log database is updated
2. Check all changes are logged with timestamps
3. Verify audit trail completeness
4. Score: (Logged Changes / Total Changes) × 100

### Remediation Guidance

1. Add version history table with Date, Version, Author, Changes
2. Document decision rationale in Design Decision Records (DDRs)
3. Include approval section with Name, Role, Date, Signature
4. Maintain audit log in Notion Audit Log database
5. Ensure all changes are tracked with timestamps
6. Document all regulatory decision rationales

---

## Dimension 5: Deliverable (전달 가능함)

### Definition

Output meets submission format requirements and is ready for regulatory submission.

### Regulatory Rationale

**FDA eCTD Technical Conformance Guide v4.0** requires "submission must be in the format specified in the guidance."

**EU MDR Annex II** specifies Technical Documentation requirements.

**MFDS Notice** specifies submission format requirements for Korean market.

### Verification Criteria

| Criterion | Weight | Verification Method |
|-----------|--------|---------------------|
| Template compliance | 40% | Document follows required template |
| Format requirements met | 30% | PDF, structure, sections present |
| Completeness | 20% | All required sections filled |
| Submission readiness | 10% | Meets agency-specific requirements |

### Scoring Formula

```
Deliverable Score = (Template Compliance × 0.4) +
                    (Format Requirements × 0.3) +
                    (Completeness × 0.2) +
                    (Submission Ready × 0.1)
```

### Pass Threshold

**Minimum:** 70/100 (Critical dimension - auto-fail below 70)

### Checklist

- [ ] Document follows required template structure
- [ ] All required sections are present
- [ ] File format is correct (PDF/A, eCTD, etc.)
- [ ] File naming convention follows requirements
- [ ] Page numbering is correct
- [ ] Header/footer information is accurate
- [ ] Required annexes and appendices are included
- [ ] Digital signature requirements are met
- [ ] File size limits are respected
- [ ] Language requirements are met

### Common Failures

- Missing required sections
- Incorrect document structure
- Wrong file format (e.g., DOCX instead of PDF)
- Non-compliance with template
- Incorrect file naming
- Missing required annexes
- Incomplete required fields
- File size exceeds limits

### Agency-Specific Requirements

**FDA 510(k):**
- Format: eCopy (PDF with XML backbone)
- Template: FDA 510(k) Template
- Required Sections: 21 CFR 807.20
- File Naming: [510(k) Number]_[Document Type]_[Version].pdf
- Max File Size: 10 GB per submission

**FDA PMA:**
- Format: eCopy
- Template: FDA PMA Template
- Required Sections: 21 CFR 814.20
- File Naming: [PMA Number]_[Module]_[Version].pdf
- Max File Size: 10 GB per submission

**EU MDR Technical Documentation:**
- Format: PDF
- Template: Annex II Template
- Required Sections: Annex II, Chapters 1-6
- File Naming: [Device Name]_Technical Documentation_[Version].pdf
- Language: Official language of Member State

**MFDS Submission:**
- Format: PDF
- Template: MFDS Template
- Required Sections: Varies by submission type
- File Naming: [Applicant Name]_[Device]_[Submission Type]_[Date].pdf
- Language: Korean (with English translation for some documents)

### Verification Methods

**Template Compliance Check:**
1. Retrieve required template from aria-templates skill
2. Compare document structure with template
3. Verify all required sections are present
4. Check section ordering matches template
5. Score: (Matching Sections / Required Sections) × 100

**Format Requirements Check:**
1. Verify file format (PDF/A, eCTD, etc.)
2. Check file naming convention
3. Validate PDF properties (author, title, creation date)
4. Verify file size within limits
5. Score: (Format Requirements Met / Total Requirements) × 100

**Completeness Check:**
1. Check all required sections are filled
2. Verify no placeholder text remains
3. Ensure all required fields are populated
4. Check all required annexes are included
5. Score: (Complete Sections / Required Sections) × 100

**Submission Readiness Check:**
1. Verify agency-specific requirements
2. Check digital signature requirements
3. Validate language requirements
4. Review submission checklist
5. Score: (Ready Items / Total Checklist Items) × 100

### Remediation Guidance

1. Use aria-templates skill to retrieve correct template
2. Verify all required sections are present
3. Convert to required format (usually PDF/A)
4. Check against submission checklist
5. Ensure file naming convention compliance
6. Verify all required annexes are included
7. Validate file size and format requirements
8. Confirm language requirements are met

---

## Quality Score Calculation

### Overall Score Formula

```
Overall VALID Score = (Verified + Accurate + Linked + Inspectable + Deliverable) / 5
```

### Grade Assignment

| Score Range | Grade | Interpretation | Action Required |
|-------------|-------|----------------|-----------------|
| 90-100 | A | Excellent - Submission ready | No action required |
| 80-89 | B | Good - Minor improvements needed | Address minor findings |
| 70-79 | C | Acceptable - Moderate improvements needed | Address moderate findings |
| 60-69 | D | Poor - Significant improvements required | Major rework needed |
| 0-59 | F | Fail - Major rework required | Return to drafting |

### Automatic Rejection Criteria

A document is automatically rejected if ANY of the following conditions are met:

1. **Overall VALID score < 80** (Pre-Delivery Gate)
2. **Verified dimension score < 70** (Critical failure)
3. **Deliverable dimension score < 70** (Critical failure)
4. **Any dimension score < 60** (Severe deficiency)

### Quality Gate Thresholds

| Gate | Threshold | Focus Dimensions |
|------|-----------|------------------|
| Post-Draft (Execute Phase) | 70/100 overall | Verified, Accurate, Linked |
| Post-Review (Execute Phase) | 75/100 overall | All 5 dimensions |
| Pre-Delivery (Deliver Phase) | 80/100 overall | All 5 dimensions (critical gate) |

---

## Integration with ARIA Workflow

### BRIEF Phase

**VALID Application:** Not applicable (quality gates applied after content creation)

**Activities:**
- Define validation requirements in project plan
- Identify applicable regulations and standards
- Establish quality thresholds for deliverable

### EXECUTE Phase

**Post-Draft Gate:**
- Triggered after expert-writer completes initial document
- Focus: Verified, Accurate, Linked dimensions
- Pass threshold: 70/100 overall
- Action: Iterate with expert-writer if failed

**Post-Review Gate:**
- Triggered after expert-reviewer provides feedback
- Focus: All 5 dimensions
- Pass threshold: 75/100 overall
- Action: Address findings and re-validate

**Refinement Loop:**
- expert-writer incorporates feedback
- expert-reviewer performs preliminary VALID check
- Iterative refinement until quality threshold met
- Maximum 3 iterations before escalating to user

### DELIVER Phase

**Pre-Delivery Gate:**
- Triggered before final output to user
- Focus: Deliverable dimension, overall quality
- Pass threshold: 80/100 overall (critical gate)
- Action: Generate quality certificate if passed, reject if failed

**Final Validation:**
- manager-quality performs final VALID gate validation
- Generate quality report with findings
- Create quality certificate for audit trail
- Distribute if passing, reject if failing

---

## Quality Report Structure

### Report Sections

1. **Executive Summary**
   - Overall VALID score and grade
   - Pass/Fail status
   - Critical findings

2. **Dimension Scores**
   - Individual dimension scores
   - Dimension-specific findings
   - Comparison to thresholds

3. **Detailed Findings**
   - Failed criteria with details
   - Evidence of failures
   - Recommended remediation

4. **Compliance Summary**
   - Regulatory compliance status
   - Standard compliance status
   - Agency-specific requirements status

5. **Recommendations**
   - Specific improvement actions
   - Prioritized remediation steps
   - Estimated effort for corrections

### Quality Certificate

**Certificate Contents:**
- Document ID and version
- Validation date and validator
- VALID scores for all dimensions
- Overall grade and pass/fail status
- Regulatory authority acknowledgment
- Digital signature for audit trail

---

## Tool Integration

### Context7 MCP

**Purpose:** Retrieve current regulatory and standards documentation

**Usage:**
1. Resolve library ID: `mcp__context7__resolve-library-id("FDA 21 CFR 820")`
2. Get documentation: `mcp__context7__get-library-docs(library_id, section="820.30")`
3. Compare text for Verified dimension validation

**Supported Libraries:**
- FDA 21 CFR (Medical Devices)
- ISO 13485:2016
- ISO 14971:2019
- IEC 62304:2006+AMD1:2015
- EU MDR 2017/745

### Notion MCP

**Purpose:** Maintain audit trail and traceability

**Databases:**
- Audit Log: Track all document changes and decisions
- Document Registry: Track document versions and status
- Quality Reports: Store VALID validation results
- Traceability Matrix: Maintain bidirectional traceability

**Usage:**
1. Query database for document history
2. Create audit log entries for changes
3. Update quality report database
4. Maintain traceability relationships

### Sequential Thinking MCP

**Purpose:** Complex regulatory analysis

**Use Cases:**
- Multi-market regulatory strategy
- Substantial equivalence logic
- Risk-benefit analysis
- Regulatory pathway selection

**Activation:** Use `--ultrathink` flag for complex decisions

---

## Best Practices

### Verified Dimension

- Always use official regulation identifiers (not web URLs)
- Include year for ISO standards (e.g., ISO 13485:2016)
- Verify regulation currency before citing
- Use Context7 MCP for current regulation text
- Document superseded regulation transitions

### Accurate Dimension

- Cross-reference all numerical data with source documents
- Verify all external references are accessible
- Check for internal consistency
- Standardize units of measurement
- Validate dates and timeframes

### Linked Dimension

- Use consistent ID schemes (REQ-001, TST-001)
- Maintain bidirectional traceability
- Eliminate orphan requirements and tests
- Use Notion database for dynamic traceability
- Regularly update traceability matrix

### Inspectable Dimension

- Document all decision rationale
- Maintain complete audit trail
- Use Design Decision Records (DDRs)
- Update Notion Audit Log database
- Secure approval signatures

### Deliverable Dimension

- Use correct agency template
- Verify file format requirements
- Check file naming conventions
- Ensure all required sections are complete
- Validate against submission checklist

---

## Training and Resources

### Regulatory Affairs Certification

**RAC (Regulatory Affairs Certification):**
- Organization: RAPS
- Relevant Topics: Quality systems, documentation, submissions
- VALID Impact: Overall framework understanding

**CQA (Certified Quality Auditor):**
- Organization: ASQ
- Relevant Topics: Audit techniques, documentation review
- VALID Impact: Inspectable dimension expertise

### Online Courses

**Design Controls and 21 CFR 820.30:**
- Providers: FDA (free), OrielSTAT, Medical Device Academy
- Topics: DHF, traceability, design validation
- VALID Impact: Linked and Inspectable dimensions

**Clinical Evaluation Report Writing (EU MDR):**
- Providers: UL, TÜV SÜD, Emergo
- Topics: CER structure, MEDDEV 2.7/1 compliance
- VALID Impact: Verified, Accurate, Deliverable dimensions

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-02-09 | Initial VALID framework documentation | ARIA Team |

---

## Related ARIA Skills

- **aria-quality-valid** - VALID framework skill with detailed verification procedures
- **aria-writing-style** - Technical writing standards for regulatory documents
- **aria-templates** - Document template library for regulatory submissions
- **aria-research** - Research methodology for regulatory intelligence
- **aria-integration-context7** - Context7 MCP optimization for regulation lookup
- **aria-integration-notion** - Notion database integration for audit trail

---

**Last Reviewed:** 2026-02-09
**Next Review:** 2026-05-09 (Quarterly)
**Maintained By:** ARIA Team
