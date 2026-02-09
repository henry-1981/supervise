# VALID Verification Procedures

## Overview

This module provides step-by-step verification procedures for each VALID dimension. Use these checklists when performing quality gate validation.

---

## Verified Dimension Verification

### Step 1: Extract Regulatory Claims

**Objective:** Identify all regulatory claims in the document.

**Procedure:**
1. Read document sections that reference regulations
2. Extract claims such as:
   - "This device complies with..."
   - "Per FDA guidance..."
   - "According to ISO 13485..."
   - "As required by 21 CFR 820..."

**Tool:** Use Grep tool with pattern `"comply|complies|according to|per|as required by|FDA|ISO|IEC|CFR"`

### Step 2: Verify Citation Presence

**Objective:** Ensure each claim has a corresponding citation.

**Checklist:**
- [ ] Each regulatory claim has inline citation
- [ ] Citations use standard format (e.g., `[REG: 21 CFR 820.30(a)]`)
- [ ] General claims (e.g., "FDA requires") are avoided
- [ ] Citations are hyperlinked or footnoted for traceability

**Scoring:** Count claims with citations / Total claims × 100

### Step 3: Verify Citation Accuracy

**Objective:** Confirm citations point to correct regulation sections.

**Procedure:**
1. Use Context7 MCP to retrieve regulation text:
   ```
   mcp__context7__resolve-library-id("FDA 21 CFR 820")
   mcp__context7__get-library-docs(library_id, section="820.30")
   ```
2. Compare cited text with source regulation
3. Verify section numbers are correct
4. Check subsection accuracy (e.g., (a), (b), (1), (2))

**Scoring:** Accurate citations / Total citations × 100

### Step 4: Verify Currency

**Objective:** Ensure regulations cited are current versions.

**Checklist:**
- [ ] ISO standards include year (e.g., ISO 13485:2016, not ISO 13485)
- [ ] FDA CFR citations reference current CFR edition
- [ ] EU MDR citations use correct regulation number (2017/745)
- [ ] Superseded regulations are not cited

**Common Superseded Regulations:**
- ISO 13485:2003 → ISO 13485:2016
- ISO 14971:2007 → ISO 14971:2019
- MDD 93/42/EEC → MDR 2017/745 (as of May 2021)

**Scoring:** Current citations / Total citations × 100

### Step 5: Calculate Verified Score

**Formula:**
```
Verified Score = (Citations Present × 0.3) +
                 (Citations Accurate × 0.4) +
                 (Citations Current × 0.2) +
                 (Claims Supported × 0.1)
```

**Pass:** Score >= 70

---

## Accurate Dimension Verification

### Step 1: Extract Factual Data

**Objective:** Identify all numerical data, dates, and references.

**Categories:**
- Numerical values (test results, specifications, measurements)
- Dates (effective dates, publication dates, test dates)
- References (external documents, standards, studies)
- URLs and hyperlinks

### Step 2: Verify Data Accuracy

**Procedure:**
1. Cross-reference numerical values with source documents
2. Use Read tool to access source files
3. Compare values for exact match
4. Flag discrepancies for correction

**Checklist:**
- [ ] Test results match lab reports
- [ ] Specifications match design documents
- [ ] Measurements match test records
- [ ] Calculations are correct

**Scoring:** Accurate data points / Total data points × 100

### Step 3: Verify Reference Validity

**Procedure:**
1. Test all external references for accessibility
2. For URLs: Use WebFetch to verify link is active
3. For documents: Use Read or Glob to verify file exists
4. For standards: Use Context7 to verify standard exists

**Checklist:**
- [ ] All URLs are accessible (HTTP 200)
- [ ] All file references exist in repository
- [ ] All standard references are valid
- [ ] All citations have corresponding bibliography entry

**Scoring:** Valid references / Total references × 100

### Step 4: Verify Currency

**Procedure:**
1. Check publication/update dates for all referenced documents
2. Flag documents older than 3 years for review
3. Verify standards are current editions
4. Update statistics to latest available data

**Checklist:**
- [ ] References include publication dates
- [ ] Standards are current editions
- [ ] Statistics are from recent data (< 3 years)
- [ ] Clinical data is from approved studies

**Scoring:** Current references / Total references × 100

### Step 5: Verify Internal Consistency

**Procedure:**
1. Read document sections for conflicting statements
2. Compare claims across different sections
3. Verify consistency of terminology
4. Check that conclusions match data

**Checklist:**
- [ ] No conflicting claims
- [ ] Terminology is consistent throughout
- [ ] Conclusions align with data
- [ ] Cross-references are accurate

**Scoring:** Consistent statements / Total statements × 100

### Step 6: Calculate Accurate Score

**Formula:**
```
Accurate Score = (Data Accuracy × 0.4) +
                 (Reference Validity × 0.3) +
                 (Currency × 0.2) +
                 (Consistency × 0.1)
```

**Pass:** Score >= 70

---

## Linked Dimension Verification

### Step 1: Locate Traceability Matrix

**Objective:** Find traceability matrix in document.

**Common Locations:**
- Dedicated traceability section
- Appendix or annex
- Separate traceability matrix file
- Embedded tables throughout document

**Verification:**
- [ ] Traceability matrix exists
- [ ] Matrix has required columns (Requirement ID, Design, Verification, Test ID)
- [ ] Matrix is complete (no empty cells)

**Scoring:** 100 if exists, 0 if missing

### Step 2: Verify Forward Traceability

**Objective:** Ensure all requirements trace to implementation and tests.

**Procedure:**
1. Extract all requirement IDs from matrix
2. For each requirement:
   - Verify design element exists
   - Verify verification method specified
   - Verify test ID linked
3. Use Grep to find requirement references in design docs
4. Use Grep to find test IDs in test documentation

**Checklist:**
- [ ] Every requirement has design linkage
- [ ] Every requirement has verification method
- [ ] Every requirement has test ID
- [ ] Design elements reference requirements

**Scoring:** Requirements with complete forward trace / Total requirements × 100

### Step 3: Verify Backward Traceability

**Objective:** Ensure all tests trace back to requirements.

**Procedure:**
1. Extract all test IDs from test documentation
2. For each test:
   - Find corresponding entry in traceability matrix
   - Verify requirement ID exists
   - Verify design element linked
3. Use Grep to find test references in implementation

**Checklist:**
- [ ] Every test has requirement linkage
- [ ] Every test has design linkage
- [ ] No orphan tests (tests without requirements)
- [ ] Test coverage is complete

**Scoring:** Tests with complete backward trace / Total tests × 100

### Step 4: Verify Coverage Completeness

**Objective:** Ensure no orphan requirements (requirements without tests).

**Procedure:**
1. Cross-reference requirements list with traceability matrix
2. Identify requirements without test coverage
3. Flag orphan requirements for remediation

**Checklist:**
- [ ] All requirements appear in matrix
- [ ] All requirements have at least one test
- [ ] Critical requirements have multiple tests
- [ ] Coverage percentage >= 100%

**Scoring:** Requirements with tests / Total requirements × 100

### Step 5: Calculate Linked Score

**Formula:**
```
Linked Score = (Matrix Exists × 0.2) +
               (Forward Trace × 0.3) +
               (Backward Trace × 0.3) +
               (Coverage × 0.2)
```

**Pass:** Score >= 70

---

## Inspectable Dimension Verification

### Step 1: Verify Change History

**Objective:** Ensure document has complete change history.

**Procedure:**
1. Locate version history table
2. Verify all required fields present:
   - Version number
   - Date
   - Author
   - Description of changes
3. Check that changes are sequential
4. Verify current version matches document header

**Checklist:**
- [ ] Version history table exists
- [ ] All fields populated
- [ ] Changes are sequential (v1.0 → v1.1 → v2.0)
- [ ] Current version is correct

**Scoring:** 100 if complete, 50 if partial, 0 if missing

### Step 2: Verify Decision Rationale

**Objective:** Ensure key decisions have documented rationale.

**Procedure:**
1. Identify decision points in document (e.g., design choices, risk acceptance)
2. Check for rationale documentation:
   - Design Decision Records (DDRs)
   - Justification sections
   - Risk-benefit analysis
3. Verify rationale is clear and sufficient

**Checklist:**
- [ ] All design decisions have rationale
- [ ] Risk acceptance decisions justified
- [ ] Alternative approaches considered
- [ ] Rationale is clear and detailed

**Scoring:** Decisions with rationale / Total decisions × 100

### Step 3: Verify Approvals

**Objective:** Ensure document has required approvals.

**Procedure:**
1. Locate approval section
2. Verify required approvers:
   - Author
   - Reviewer
   - Approver (usually QA or RA manager)
3. Check signature/approval evidence
4. Verify approval dates are present

**Checklist:**
- [ ] Approval section exists
- [ ] All required roles signed
- [ ] Signatures/approvals are dated
- [ ] Approval dates are sequential

**Scoring:** Required approvals present / Total required approvals × 100

### Step 4: Verify Audit Trail

**Objective:** Ensure all changes are tracked in audit trail.

**Procedure:**
1. Query Notion Audit Log database for document entries
2. Verify audit log completeness:
   - All changes logged
   - Change timestamps present
   - Change authors recorded
   - Change descriptions clear
3. Cross-reference with version history

**Checklist:**
- [ ] Audit log entries exist
- [ ] All changes logged
- [ ] Timestamps are present
- [ ] Authors are identified

**Scoring:** Changes in audit log / Changes in version history × 100

### Step 5: Calculate Inspectable Score

**Formula:**
```
Inspectable Score = (Change History × 0.3) +
                    (Decision Rationale × 0.4) +
                    (Approvals × 0.2) +
                    (Audit Trail × 0.1)
```

**Pass:** Score >= 70

---

## Deliverable Dimension Verification

### Step 1: Verify Template Compliance

**Objective:** Ensure document follows required template.

**Procedure:**
1. Use aria-templates skill to retrieve correct template
2. Compare document structure with template:
   - Section headers match
   - Section order is correct
   - Required subsections present
3. Use Grep to find section headers
4. Create checklist of template sections

**Checklist:**
- [ ] All required sections present
- [ ] Sections in correct order
- [ ] Section numbering matches template
- [ ] No extra sections (unless justified)

**Scoring:** Template sections present / Total template sections × 100

### Step 2: Verify Format Requirements

**Objective:** Ensure document meets format specifications.

**Procedure:**
1. Check file format (should be PDF or PDF/A)
2. Verify document structure:
   - Table of contents
   - Page numbers
   - Headers/footers
   - Watermarks (if required)
3. Check formatting consistency:
   - Font sizes
   - Margins
   - Line spacing

**Checklist:**
- [ ] Correct file format (PDF/PDF-A)
- [ ] Table of contents present
- [ ] Page numbers continuous
- [ ] Headers/footers consistent
- [ ] Formatting follows template

**Scoring:** Format requirements met / Total format requirements × 100

### Step 3: Verify Completeness

**Objective:** Ensure all required sections are filled.

**Procedure:**
1. Review document for placeholder text (e.g., "[INSERT]", "TBD")
2. Check that all sections have content
3. Verify minimum content length requirements
4. Flag empty or stub sections

**Checklist:**
- [ ] No placeholder text
- [ ] All sections have content
- [ ] Content meets minimum length
- [ ] No stub sections

**Scoring:** Complete sections / Total sections × 100

### Step 4: Verify Submission Readiness

**Objective:** Ensure document meets agency-specific requirements.

**Procedure:**
1. Check against submission checklist (FDA/EU/MFDS)
2. Verify regulatory-specific requirements:
   - FDA: eCTD format, validation report
   - EU: Notified Body requirements, CE declaration
   - MFDS: Korean language summary, local agent
3. Confirm all required attachments present

**Checklist:**
- [ ] Submission checklist items complete
- [ ] Agency-specific requirements met
- [ ] Required attachments present
- [ ] Submission package ready

**Scoring:** Submission requirements met / Total requirements × 100

### Step 5: Calculate Deliverable Score

**Formula:**
```
Deliverable Score = (Template Compliance × 0.4) +
                    (Format Requirements × 0.3) +
                    (Completeness × 0.2) +
                    (Submission Ready × 0.1)
```

**Pass:** Score >= 70 (Critical dimension - auto-fail below 70)

---

## Quality Report Generation

### Report Structure

A quality report should include:

1. **Executive Summary**
   - Overall VALID score
   - Grade assignment (A/B/C/D/F)
   - Pass/Fail determination
   - Critical issues

2. **Dimension Scores**
   - Score for each dimension
   - Pass/Fail for each dimension
   - Detailed findings

3. **Failed Criteria**
   - List of failed verification criteria
   - Impact assessment
   - Remediation recommendations

4. **Action Items**
   - Specific improvement steps
   - Assigned owners
   - Target completion dates

5. **Approval**
   - Quality reviewer signature
   - Date of review
   - Approval decision

### Report Template

```markdown
# VALID Quality Report

**Document:** [Document Title]
**Version:** [Version Number]
**Review Date:** [Date]
**Reviewer:** [Name/Agent]

## Executive Summary

**Overall VALID Score:** [Score]/100 (Grade: [A/B/C/D/F])
**Status:** [PASS/FAIL]

**Critical Issues:** [Count]
**Major Issues:** [Count]
**Minor Issues:** [Count]

## Dimension Scores

| Dimension | Score | Status | Critical Failures |
|-----------|-------|--------|-------------------|
| Verified | [Score]/100 | [PASS/FAIL] | [Count] |
| Accurate | [Score]/100 | [PASS/FAIL] | [Count] |
| Linked | [Score]/100 | [PASS/FAIL] | [Count] |
| Inspectable | [Score]/100 | [PASS/FAIL] | [Count] |
| Deliverable | [Score]/100 | [PASS/FAIL] | [Count] |

## Detailed Findings

### Verified Dimension
[Findings]

### Accurate Dimension
[Findings]

### Linked Dimension
[Findings]

### Inspectable Dimension
[Findings]

### Deliverable Dimension
[Findings]

## Action Items

1. [Action Item 1] - Owner: [Name] - Due: [Date]
2. [Action Item 2] - Owner: [Name] - Due: [Date]

## Approval

**Reviewer:** [Name]
**Date:** [Date]
**Decision:** [APPROVE/REJECT/CONDITIONAL APPROVAL]
```

---

## Common Verification Mistakes

### Mistake 1: Skipping Context7 Verification

**Problem:** Assuming citations are accurate without cross-referencing.
**Impact:** Verified dimension score artificially inflated.
**Solution:** Always use Context7 MCP to verify regulation text.

### Mistake 2: Accepting Partial Traceability

**Problem:** Accepting traceability matrix with gaps.
**Impact:** Linked dimension passes when it should fail.
**Solution:** Enforce 100% traceability coverage.

### Mistake 3: Ignoring Audit Trail

**Problem:** Not querying Notion Audit Log database.
**Impact:** Inspectable dimension score incorrect.
**Solution:** Always query audit log as part of verification.

### Mistake 4: Template Mismatch

**Problem:** Using wrong template for document type.
**Impact:** Deliverable dimension fails unnecessarily.
**Solution:** Verify template selection before validation.

---

## Automation Opportunities

### Automated Checks

The following verification steps can be automated:

1. **Citation Extraction:** Use Grep with regex patterns
2. **Reference Validation:** Use WebFetch for URLs, Read for files
3. **Traceability Coverage:** Script to compare requirement lists
4. **Template Compliance:** Section header matching with Grep
5. **Placeholder Detection:** Grep for common placeholder patterns

### Manual Review Required

The following require human judgment:

1. **Citation Accuracy:** Semantic comparison with source
2. **Decision Rationale Quality:** Sufficiency assessment
3. **Data Interpretation:** Correctness of conclusions
4. **Submission Readiness:** Agency-specific nuances
