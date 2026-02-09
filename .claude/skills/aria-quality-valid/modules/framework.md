# VALID Framework - Detailed Dimensions

## Overview

The VALID framework provides 5 quality dimensions for regulatory documentation validation. Each dimension is scored independently on a 0-100 scale, with specific verification criteria.

## Dimension 1: Verified

**Definition:** Content matches source regulation text and is traceable to authoritative sources.

**Regulatory Rationale:** FDA 21 CFR 820.40 requires "procedures to control all documents and data" to ensure accuracy and prevent obsolete documents.

### Verification Criteria

| Criterion | Weight | Check Method |
|-----------|--------|--------------|
| Regulatory citations present | 30% | Count citations, verify format (e.g., "21 CFR 820.30(a)") |
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

### Common Failures

- Missing citations for regulatory claims
- Outdated regulation versions (e.g., citing superseded ISO 13485:2003 instead of ISO 13485:2016)
- Incorrect section references (e.g., "21 CFR 820.40" when correct is "21 CFR 820.30")
- Web URLs instead of official regulation identifiers

### Remediation Guidance

1. Use Context7 MCP to retrieve current regulation text
2. Add inline citations using format: `[REG: 21 CFR 820.30(a)]`
3. Verify effective dates for all cited regulations
4. Replace web links with official regulation identifiers

---

## Dimension 2: Accurate

**Definition:** Data, figures, references, and factual claims are correct and current.

**Regulatory Rationale:** ISO 13485:2016 Section 4.2.4 requires records to be "legible, readily identifiable and retrievable."

### Verification Criteria

| Criterion | Weight | Check Method |
|-----------|--------|--------------|
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

### Common Failures

- Incorrect numerical values (e.g., wrong test results)
- Broken or missing references
- Outdated statistics or data
- Conflicting statements within the document

### Remediation Guidance

1. Verify all numerical data against source documents
2. Test all external references for accessibility
3. Update dates to reflect current information
4. Perform consistency check across all sections

---

## Dimension 3: Linked

**Definition:** Requirements, documents, and evidence are traceable through a traceability matrix.

**Regulatory Rationale:** IEC 62304 Section 5.1.1 requires "traceability between software requirements and software system test cases."

### Verification Criteria

| Criterion | Weight | Check Method |
|-----------|--------|--------------|
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

### Common Failures

- No traceability matrix provided
- Requirements without corresponding tests
- Tests without requirements linkage
- Incomplete coverage (orphan requirements)

### Remediation Guidance

1. Create traceability matrix with columns: Requirement ID, Design Element, Verification Method, Test ID
2. Ensure bidirectional traceability
3. Use consistent ID schemes (e.g., REQ-001, TST-001)
4. Mark all requirements as verified

---

## Dimension 4: Inspectable

**Definition:** Audit trail is maintained and decision rationale is documented.

**Regulatory Rationale:** ISO 13485:2016 Section 7.3.4 requires "Design and development review records shall include... decisions and actions taken."

### Verification Criteria

| Criterion | Weight | Check Method |
|-----------|--------|--------------|
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

### Common Failures

- Missing change history or version control
- Decisions without rationale
- No approval signatures
- Incomplete audit trail

### Remediation Guidance

1. Add version history table with Date, Version, Author, Changes
2. Document decision rationale in Design Decision Records (DDRs)
3. Include approval section with Name, Role, Date, Signature
4. Maintain audit log in Notion Audit Log database

---

## Dimension 5: Deliverable

**Definition:** Output meets submission format requirements and is ready for regulatory submission.

**Regulatory Rationale:** FDA eCTD guidance requires "submission must be in the format specified in the guidance."

### Verification Criteria

| Criterion | Weight | Check Method |
|-----------|--------|--------------|
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

### Common Failures

- Missing required sections
- Incorrect document structure
- Wrong file format (e.g., DOCX instead of PDF)
- Non-compliance with template

### Remediation Guidance

1. Use aria-templates skill to retrieve correct template
2. Verify all required sections are present
3. Convert to required format (usually PDF/A)
4. Check against submission checklist

---

## Quality Score Calculation

### Overall Score

```
Overall VALID Score = (V + A + L + I + D) / 5
```

### Grade Assignment

| Score Range | Grade | Interpretation |
|-------------|-------|----------------|
| 90-100 | A | Excellent - Submission ready |
| 80-89 | B | Good - Minor improvements needed |
| 70-79 | C | Acceptable - Moderate improvements needed |
| 60-69 | D | Poor - Significant improvements required |
| 0-59 | F | Fail - Major rework required |

### Automatic Rejection Criteria

A document is automatically rejected if ANY of the following conditions are met:

1. Overall VALID score < 80
2. Verified dimension score < 70
3. Deliverable dimension score < 70
4. Any dimension score < 60

---

## Integration with Quality Gates

### Gate Execution Points

**Post-Draft Gate (Execute Phase):**
- Triggered after expert-writer completes initial document
- Focus on Verified, Accurate, Linked dimensions
- Pass threshold: 70/100 overall

**Post-Review Gate (Execute Phase):**
- Triggered after expert-reviewer provides feedback
- Focus on all 5 dimensions
- Pass threshold: 75/100 overall

**Pre-Delivery Gate (Deliver Phase):**
- Triggered before final output to user
- Focus on Deliverable dimension
- Pass threshold: 80/100 overall (critical gate)

### Gate Failure Response

When a gate fails:

1. **Generate detailed report** listing failed criteria
2. **Assign remediation owner** (usually expert-writer)
3. **Create action items** with specific improvement steps
4. **Re-validate** after remediation complete
5. **Maximum 3 iterations** before escalating to user

---

## References

- FDA 21 CFR 820.40 - Document Controls
- ISO 13485:2016 Section 4.2.4 - Control of Records
- IEC 62304:2006 Section 5.1.1 - Requirements Traceability
- ISO 14971:2019 Risk Management File requirements
- FDA eCTD Technical Conformance Guide v4.0
