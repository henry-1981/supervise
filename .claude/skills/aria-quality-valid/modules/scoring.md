# VALID Scoring Methodology

## Overview

This module defines the scoring methodology for VALID quality validation, including calculation formulas, grade assignment, and pass/fail determination.

---

## Dimension Scoring

### General Scoring Principles

1. **0-100 Scale:** All dimensions scored on a 0-100 point scale
2. **Weighted Criteria:** Each dimension has weighted sub-criteria
3. **Independent Scoring:** Dimensions are scored independently
4. **Objective Criteria:** Scores based on quantifiable metrics when possible
5. **Consistent Application:** Same criteria applied across all documents

### Verified Dimension Scoring

**Formula:**
```
Verified Score = (Citations Present × 0.3) +
                 (Citations Accurate × 0.4) +
                 (Citations Current × 0.2) +
                 (Claims Supported × 0.1)
```

**Sub-Criteria Calculation:**

**Citations Present (0-100):**
```
Score = (Sections with Citations / Total Regulatory Sections) × 100
```

**Citations Accurate (0-100):**
```
Score = (Accurate Citations / Total Citations) × 100
```
*Accurate = citation verified via Context7 MCP cross-reference*

**Citations Current (0-100):**
```
Score = (Current Citations / Total Citations) × 100
```
*Current = regulation version is not superseded*

**Claims Supported (0-100):**
```
Score = (Claims with Citations / Total Regulatory Claims) × 100
```

**Example Calculation:**

Document with:
- 10 regulatory sections, 9 have citations → Citations Present = 90
- 20 total citations, 18 verified accurate → Citations Accurate = 90
- 20 total citations, 19 are current versions → Citations Current = 95
- 15 regulatory claims, 14 have citations → Claims Supported = 93

```
Verified Score = (90 × 0.3) + (90 × 0.4) + (95 × 0.2) + (93 × 0.1)
               = 27 + 36 + 19 + 9.3
               = 91.3
```

### Accurate Dimension Scoring

**Formula:**
```
Accurate Score = (Data Accuracy × 0.4) +
                 (Reference Validity × 0.3) +
                 (Currency × 0.2) +
                 (Consistency × 0.1)
```

**Sub-Criteria Calculation:**

**Data Accuracy (0-100):**
```
Score = (Correct Data Points / Total Data Points) × 100
```

**Reference Validity (0-100):**
```
Score = (Valid References / Total References) × 100
```
*Valid = URL accessible (HTTP 200) OR file exists OR standard verified*

**Currency (0-100):**
```
Score = (Current References / Total References) × 100
```
*Current = publication date < 3 years OR standard is latest edition*

**Consistency (0-100):**
```
Score = 100 - (Conflicting Statements / Total Statements × 100)
```

**Example Calculation:**

Document with:
- 50 data points, 48 verified correct → Data Accuracy = 96
- 30 references, 28 valid → Reference Validity = 93
- 30 references, 25 current → Currency = 83
- 100 statements, 2 conflicts detected → Consistency = 98

```
Accurate Score = (96 × 0.4) + (93 × 0.3) + (83 × 0.2) + (98 × 0.1)
               = 38.4 + 27.9 + 16.6 + 9.8
               = 92.7
```

### Linked Dimension Scoring

**Formula:**
```
Linked Score = (Matrix Exists × 0.2) +
               (Forward Trace × 0.3) +
               (Backward Trace × 0.3) +
               (Coverage × 0.2)
```

**Sub-Criteria Calculation:**

**Matrix Exists (0 or 100):**
```
Score = 100 if traceability matrix present, else 0
```

**Forward Trace (0-100):**
```
Score = (Requirements with Complete Forward Trace / Total Requirements) × 100
```
*Complete = Requirement → Design → Verification → Test*

**Backward Trace (0-100):**
```
Score = (Tests with Complete Backward Trace / Total Tests) × 100
```
*Complete = Test → Verification → Design → Requirement*

**Coverage (0-100):**
```
Score = (Requirements with Tests / Total Requirements) × 100
```

**Example Calculation:**

Document with:
- Traceability matrix exists → Matrix Exists = 100
- 50 requirements, 47 have complete forward trace → Forward Trace = 94
- 60 tests, 58 have complete backward trace → Backward Trace = 97
- 50 requirements, 50 have tests → Coverage = 100

```
Linked Score = (100 × 0.2) + (94 × 0.3) + (97 × 0.3) + (100 × 0.2)
             = 20 + 28.2 + 29.1 + 20
             = 97.3
```

### Inspectable Dimension Scoring

**Formula:**
```
Inspectable Score = (Change History × 0.3) +
                    (Decision Rationale × 0.4) +
                    (Approvals × 0.2) +
                    (Audit Trail × 0.1)
```

**Sub-Criteria Calculation:**

**Change History (0-100):**
```
Score = 100 if complete, 50 if partial, 0 if missing
```
*Complete = all fields (version, date, author, changes) populated*

**Decision Rationale (0-100):**
```
Score = (Decisions with Rationale / Total Decisions) × 100
```

**Approvals (0-100):**
```
Score = (Required Approvals Present / Total Required Approvals) × 100
```

**Audit Trail (0-100):**
```
Score = (Changes in Audit Log / Changes in Version History) × 100
```

**Example Calculation:**

Document with:
- Complete version history table → Change History = 100
- 10 decisions, 9 have rationale → Decision Rationale = 90
- 3 required approvals, 3 present → Approvals = 100
- 8 version changes, 8 in audit log → Audit Trail = 100

```
Inspectable Score = (100 × 0.3) + (90 × 0.4) + (100 × 0.2) + (100 × 0.1)
                  = 30 + 36 + 20 + 10
                  = 96
```

### Deliverable Dimension Scoring

**Formula:**
```
Deliverable Score = (Template Compliance × 0.4) +
                    (Format Requirements × 0.3) +
                    (Completeness × 0.2) +
                    (Submission Ready × 0.1)
```

**Sub-Criteria Calculation:**

**Template Compliance (0-100):**
```
Score = (Template Sections Present / Total Template Sections) × 100
```

**Format Requirements (0-100):**
```
Score = (Format Requirements Met / Total Format Requirements) × 100
```
*Common requirements: correct file format, TOC, page numbers, headers/footers*

**Completeness (0-100):**
```
Score = (Complete Sections / Total Sections) × 100
```
*Complete = no placeholders, sufficient content*

**Submission Ready (0-100):**
```
Score = (Submission Requirements Met / Total Submission Requirements) × 100
```

**Example Calculation:**

Document with:
- 15 template sections, 15 present → Template Compliance = 100
- 5 format requirements, 5 met → Format Requirements = 100
- 20 sections, 19 complete → Completeness = 95
- 10 submission requirements, 9 met → Submission Ready = 90

```
Deliverable Score = (100 × 0.4) + (100 × 0.3) + (95 × 0.2) + (90 × 0.1)
                  = 40 + 30 + 19 + 9
                  = 98
```

---

## Overall VALID Score Calculation

### Simple Average Method

**Formula:**
```
Overall VALID Score = (V + A + L + I + D) / 5
```

**Example:**
```
Verified = 91.3
Accurate = 92.7
Linked = 97.3
Inspectable = 96.0
Deliverable = 98.0

Overall VALID Score = (91.3 + 92.7 + 97.3 + 96.0 + 98.0) / 5
                    = 475.3 / 5
                    = 95.06
```

### Weighted Average Method (Optional)

For critical submissions, apply dimension weights:

**Formula:**
```
Overall VALID Score = (V × 0.25) + (A × 0.20) + (L × 0.20) + (I × 0.15) + (D × 0.20)
```

**Rationale:**
- Verified: 25% (most critical - regulatory compliance)
- Accurate: 20% (data integrity)
- Linked: 20% (traceability)
- Inspectable: 15% (audit trail)
- Deliverable: 20% (submission readiness)

**Example:**
```
Weighted Score = (91.3 × 0.25) + (92.7 × 0.20) + (97.3 × 0.20) + (96.0 × 0.15) + (98.0 × 0.20)
               = 22.825 + 18.54 + 19.46 + 14.4 + 19.6
               = 94.825
```

---

## Grade Assignment

### Grade Scale

| Score Range | Grade | Interpretation | Action |
|-------------|-------|----------------|--------|
| 90-100 | A | Excellent | Approve for submission |
| 80-89 | B | Good | Approve with minor notes |
| 70-79 | C | Acceptable | Conditional approval, address findings |
| 60-69 | D | Poor | Reject, significant rework required |
| 0-59 | F | Fail | Reject, major rework required |

### Grade Determination Logic

```
IF Overall Score >= 90 THEN Grade = A
ELSE IF Overall Score >= 80 THEN Grade = B
ELSE IF Overall Score >= 70 THEN Grade = C
ELSE IF Overall Score >= 60 THEN Grade = D
ELSE Grade = F
```

### Grade Modifiers

**Plus/Minus Modifiers (Optional):**

Within each grade band, apply plus/minus:
- Top third of band: + (e.g., B+ for 87-89)
- Middle third: No modifier (e.g., B for 84-86)
- Bottom third: - (e.g., B- for 80-83)

**Example:**
- Score 95 → A (no plus, already at top)
- Score 87 → B+
- Score 84 → B
- Score 81 → B-

---

## Pass/Fail Determination

### Automatic Pass Criteria

A document PASSES if ALL of the following are true:

1. Overall VALID Score >= 80
2. Verified Dimension Score >= 70
3. Deliverable Dimension Score >= 70
4. All other dimensions >= 60
5. No critical failures detected

### Automatic Fail Criteria

A document FAILS if ANY of the following are true:

1. Overall VALID Score < 80
2. Verified Dimension Score < 70
3. Deliverable Dimension Score < 70
4. Any dimension score < 60
5. Critical failure detected

### Critical Failures

Critical failures trigger automatic rejection regardless of score:

| Failure Type | Description | Example |
|--------------|-------------|---------|
| Missing Regulation Citation | Regulatory claim without source | "FDA requires..." with no CFR reference |
| Incorrect Format | Wrong file format for submission | DOCX instead of PDF for eCTD |
| No Traceability Matrix | Complete absence of traceability | No requirement-test linkage |
| Missing Approvals | Required signature missing | No QA manager approval |
| Superseded Regulation | Citing outdated regulation | ISO 13485:2003 instead of :2016 |

### Conditional Approval

Conditional approval may be granted if:

1. Overall Score >= 75
2. All critical dimensions >= 70
3. Findings are minor and addressable
4. User acknowledges required corrections

**Conditional Approval Template:**
```
CONDITIONAL APPROVAL

Overall Score: [Score] (Grade: [Grade])

Conditions:
1. [Condition 1]
2. [Condition 2]

Action Required:
- [Action 1] by [Date]
- [Action 2] by [Date]

Re-validation Required: [YES/NO]
```

---

## Score Interpretation Guidelines

### Score Ranges and Meaning

**90-100 (Grade A):**
- Document is submission-ready
- Minor improvements optional
- Proceed to delivery phase
- Minimal risk of rejection

**80-89 (Grade B):**
- Document is near submission-ready
- Address minor findings
- Low risk of rejection
- Typical for first-pass documents

**70-79 (Grade C):**
- Document needs improvement
- Moderate findings to address
- Medium risk of rejection
- Requires revision cycle

**60-69 (Grade D):**
- Document has significant issues
- Major findings to address
- High risk of rejection
- Requires substantial rework

**0-59 (Grade F):**
- Document not suitable for submission
- Fundamental issues present
- Very high risk of rejection
- Requires complete rework

### Dimension-Specific Interpretation

**Verified Dimension:**
- Score < 70: Regulatory compliance at risk
- Score 70-85: Acceptable but needs citation improvements
- Score 85-95: Good regulatory foundation
- Score > 95: Excellent regulatory documentation

**Accurate Dimension:**
- Score < 70: Data integrity concerns
- Score 70-85: Acceptable but verify critical data
- Score 85-95: Good data quality
- Score > 95: Excellent data integrity

**Linked Dimension:**
- Score < 70: Traceability gaps exist
- Score 70-85: Acceptable but improve coverage
- Score 85-95: Good traceability
- Score > 95: Excellent traceability

**Inspectable Dimension:**
- Score < 70: Audit trail deficiencies
- Score 70-85: Acceptable but improve documentation
- Score 85-95: Good audit readiness
- Score > 95: Excellent audit trail

**Deliverable Dimension:**
- Score < 70: Format non-compliance
- Score 70-85: Acceptable but address format issues
- Score 85-95: Good submission readiness
- Score > 95: Excellent deliverable quality

---

## Quality Trends and Improvement

### Tracking Scores Over Time

For each document, track VALID scores across revisions:

| Version | Overall | V | A | L | I | D | Grade | Status |
|---------|---------|---|---|---|---|---|-------|--------|
| v0.1 | 65 | 60 | 70 | 65 | 70 | 60 | D | FAIL |
| v0.2 | 75 | 72 | 80 | 75 | 75 | 73 | C | CONDITIONAL |
| v0.3 | 85 | 85 | 88 | 82 | 85 | 85 | B | PASS |
| v1.0 | 92 | 92 | 95 | 90 | 92 | 93 | A | PASS |

### Improvement Velocity

**Calculation:**
```
Improvement Velocity = (Current Score - Previous Score) / Revision Cycle Time
```

**Example:**
- v0.1 score: 65
- v0.2 score: 75
- Cycle time: 3 days

```
Improvement Velocity = (75 - 65) / 3 = 3.33 points/day
```

**Healthy Velocity:**
- 5+ points/day: Excellent progress
- 3-5 points/day: Good progress
- 1-3 points/day: Acceptable progress
- < 1 point/day: Slow progress, review approach

### Quality Benchmarks

**Industry Benchmarks (Typical):**
- First draft: 60-70 (Grade D/C)
- Second revision: 75-85 (Grade C/B)
- Final submission: 85-95 (Grade B/A)

**ARIA Target Benchmarks:**
- First draft: 75+ (Grade C+)
- Second revision: 85+ (Grade B)
- Final submission: 90+ (Grade A-)

---

## Scoring Examples

### Example 1: 510(k) Submission

**Document:** Substantial Equivalence Determination
**Type:** FDA 510(k) Premarket Notification

**Dimension Scores:**
- Verified: 88 (18 of 20 FDA citations accurate, all current)
- Accurate: 92 (46 of 50 data points verified, all references valid)
- Linked: 85 (45 of 50 requirements traced to predicate)
- Inspectable: 90 (complete change history, all approvals present)
- Deliverable: 95 (eCTD format, all sections complete)

**Overall Score:** 90.0
**Grade:** A
**Decision:** PASS - Approve for submission

### Example 2: EU Technical File

**Document:** Clinical Evaluation Report
**Type:** EU MDR Technical File Component

**Dimension Scores:**
- Verified: 72 (EU MDR citations present but some inaccurate)
- Accurate: 85 (clinical data verified but some references outdated)
- Linked: 80 (traceability good but some gaps)
- Inspectable: 88 (good audit trail)
- Deliverable: 92 (format compliant)

**Overall Score:** 83.4
**Grade:** B
**Decision:** PASS - Minor improvements recommended

### Example 3: Design Control Document

**Document:** Design History File (DHF)
**Type:** Internal QMS Document

**Dimension Scores:**
- Verified: 65 (missing many regulatory citations)
- Accurate: 78 (data mostly accurate)
- Linked: 55 (incomplete traceability matrix)
- Inspectable: 75 (partial change history)
- Deliverable: 70 (template followed but incomplete)

**Overall Score:** 68.6
**Grade:** D
**Decision:** FAIL - Significant rework required

**Critical Failures:**
- Verified < 70
- Linked < 60

---

## Score Calibration

### Calibration Guidelines

To ensure consistent scoring across reviewers:

1. **Use Reference Examples:** Compare to benchmark documents
2. **Apply Criteria Strictly:** Avoid subjective adjustments
3. **Document Rationale:** Explain scoring decisions
4. **Peer Review Scores:** Have second reviewer validate
5. **Calibrate Quarterly:** Review scoring consistency

### Inter-Rater Reliability

**Target:** 90% agreement within ±5 points

**Measurement:**
```
Agreement Rate = (Scores within ±5 points / Total Comparisons) × 100
```

**Example:**
- Reviewer A: 85
- Reviewer B: 82
- Difference: 3 points (within ±5) → Agreement

### Scoring Audits

Periodically audit VALID scores:
- Random sample 10% of documents
- Independent re-scoring
- Compare scores
- Investigate discrepancies > 10 points
- Update calibration if needed

---

## References

- ISO 13485:2016 Section 4.2.4 - Control of Records
- FDA 21 CFR 820.40 - Document Controls
- IEC 62304:2006 - Software Lifecycle Processes
- ISO 14971:2019 - Risk Management
- FDA Guidance: eCTD Technical Conformance Guide v4.0
