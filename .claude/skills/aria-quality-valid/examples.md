# VALID Framework Examples

## Overview

This document provides real-world examples of VALID quality validation for regulatory documentation.

---

## Example 1: FDA 510(k) Premarket Notification

### Document Context

**Document Type:** Substantial Equivalence Determination
**Submission:** FDA 510(k) Premarket Notification
**Device Class:** Class II Medical Device
**Intended Use:** Blood glucose monitoring system

### VALID Validation Results

#### Verified Dimension (Score: 88/100)

**Findings:**

✅ **Pass Criteria:**
- 18 of 20 FDA citations verified accurate via Context7 MCP
- All citations use current CFR edition (2024)
- Regulatory claims properly supported with citations

❌ **Failed Criteria:**
- 2 citations reference incorrect subsections:
  - Document cites "21 CFR 820.30(g)" but should be "21 CFR 820.30(h)"
  - Document cites "21 CFR 862.1345" but device is not IVD

**Remediation:**
1. Correct 21 CFR 820.30(g) → 21 CFR 820.30(h) (Design Validation)
2. Remove 21 CFR 862.1345 citation (not applicable for this device class)
3. Re-verify with Context7 MCP

**After Remediation:** 20/20 accurate → Score: 95/100

#### Accurate Dimension (Score: 92/100)

**Findings:**

✅ **Pass Criteria:**
- 46 of 50 data points verified against source documents
- All external references accessible
- Clinical data from approved studies (< 2 years old)
- No conflicting statements detected

❌ **Failed Criteria:**
- 4 numerical errors:
  - Table 3 shows sensitivity 95.2% (source document: 95.4%)
  - Section 4.3 states "n=150" (actual sample size: n=153)
  - Figure 2 shows wrong statistical significance (p=0.04 vs p=0.042)
  - Appendix B has transcription error in device weight (180g vs 185g)

**Remediation:**
1. Update Table 3 sensitivity value: 95.4%
2. Correct sample size in Section 4.3: n=153
3. Fix p-value in Figure 2: p=0.042
4. Correct device weight in Appendix B: 185g

**After Remediation:** 50/50 accurate → Score: 100/100

#### Linked Dimension (Score: 85/100)

**Findings:**

✅ **Pass Criteria:**
- Traceability matrix present (Appendix C)
- 45 of 50 requirements have complete forward trace
- Good backward traceability (58/60 tests linked)
- All critical requirements traced

❌ **Failed Criteria:**
- 5 requirements lack test coverage:
  - REQ-012: Battery life specification (no test)
  - REQ-023: Display brightness range (no test)
  - REQ-034: Storage temperature limits (no verification)
  - REQ-041: User manual clarity (no usability test reference)
  - REQ-048: Packaging integrity (no transit test)
- 2 tests without requirement linkage:
  - TST-045: Acoustic noise test (no requirement)
  - TST-052: Color accuracy test (no requirement)

**Remediation:**
1. Add verification methods for orphan requirements:
   - REQ-012 → TST-063 (Battery endurance test)
   - REQ-023 → TST-064 (Display luminance measurement)
   - REQ-034 → TST-065 (Environmental stress test)
   - REQ-041 → TST-066 (Formative usability study)
   - REQ-048 → TST-067 (ISTA 2A transit test)
2. Link orphan tests to requirements or justify removal:
   - TST-045 → Document as "nice-to-have" test, not regulatory requirement
   - TST-052 → Link to REQ-027 (Display specifications)

**After Remediation:** 50/50 traced → Score: 95/100

#### Inspectable Dimension (Score: 90/100)

**Findings:**

✅ **Pass Criteria:**
- Complete version history table present
- All approvals present (Author, Reviewer, QA Manager)
- Good decision rationale documentation
- Audit trail complete in Notion database

❌ **Failed Criteria:**
- 1 design decision lacks rationale:
  - Decision to use Bluetooth 5.0 instead of 5.2 (no justification documented)

**Remediation:**
1. Add Design Decision Record (DDR-003):
   ```
   Decision: Use Bluetooth 5.0 instead of 5.2
   Rationale: Bluetooth 5.0 offers sufficient range (40m) and data rate (2 Mbps)
   for glucose meter application. Bluetooth 5.2 features (LE Audio, Enhanced
   Attribute Protocol) not required. Cost savings: $1.50/unit. Predicate device
   uses Bluetooth 5.0, maintaining substantial equivalence.
   Date: 2025-03-15
   Approver: J. Smith, Design Lead
   ```

**After Remediation:** 10/10 decisions documented → Score: 96/100

#### Deliverable Dimension (Score: 95/100)

**Findings:**

✅ **Pass Criteria:**
- eCTD format compliant (PDF/A-1b)
- All template sections present
- Table of contents accurate
- Page numbering continuous
- Submission checklist complete

❌ **Failed Criteria:**
- 1 format issue:
  - Figure 5 embedded as JPEG instead of vector format (quality degradation)

**Remediation:**
1. Re-embed Figure 5 as vector graphic (SVG or EPS converted to PDF)

**After Remediation:** All format requirements met → Score: 100/100

### Overall Assessment

**Initial Scores:**
- Verified: 88
- Accurate: 92
- Linked: 85
- Inspectable: 90
- Deliverable: 95
- **Overall: 90.0 (Grade A)**
- **Decision: PASS** (with recommended improvements)

**Post-Remediation Scores:**
- Verified: 95
- Accurate: 100
- Linked: 95
- Inspectable: 96
- Deliverable: 100
- **Overall: 97.2 (Grade A)**
- **Decision: APPROVE FOR SUBMISSION**

---

## Example 2: EU MDR Technical File

### Document Context

**Document Type:** Clinical Evaluation Report (CER)
**Submission:** EU MDR Technical File
**Device Class:** Class IIa Medical Device
**Intended Use:** Non-invasive patient monitoring system

### VALID Validation Results

#### Verified Dimension (Score: 72/100)

**Findings:**

✅ **Pass Criteria:**
- EU MDR citations present throughout document
- ISO 14155:2020 clinical investigation standard referenced

❌ **Failed Criteria:**
- 8 of 25 citations reference incorrect MDR articles:
  - Document cites "Article 52" for clinical evaluation (should be Article 61)
  - Multiple references to "Annex XIII" instead of "Annex XIV" (Clinical Evaluation)
  - Document cites superseded ISO 14971:2007 instead of current :2019
- 3 citations lack specific clause references:
  - "Per EU MDR requirements" without article number (3 instances)

**Remediation:**
1. Update all Article 52 references → Article 61 (Clinical Evaluation)
2. Correct Annex XIII → Annex XIV throughout document
3. Update ISO 14971:2007 → ISO 14971:2019 (current edition)
4. Add specific citations for general "EU MDR requirements" claims
5. Verify all corrections with Context7 MCP

**Impact:** Critical dimension - score must reach 70+ to pass

**After Remediation:** 25/25 accurate citations → Score: 92/100

#### Accurate Dimension (Score: 85/100)

**Findings:**

✅ **Pass Criteria:**
- Clinical data verified from published studies
- Device specifications match technical file
- Statistical analysis correct

❌ **Failed Criteria:**
- 5 of 30 references are outdated (> 5 years):
  - Reference 12: Clinical study from 2017 (8 years old)
  - Reference 18: Meta-analysis from 2016 (9 years old)
  - Reference 22: Guideline from 2015 (superseded by 2022 version)
- 2 broken links:
  - Reference 8: PMC article URL returns 404
  - Reference 14: Regulatory guidance URL changed

**Remediation:**
1. Update outdated references with recent equivalents:
   - Search for updated studies via Context7 or medical databases
2. Fix broken links:
   - Reference 8: Update to current PMC URL
   - Reference 14: Update to new guidance URL
3. Add note for irreplaceable older references justifying retention

**After Remediation:** 30/30 references valid and current → Score: 94/100

#### Linked Dimension (Score: 80/100)

**Findings:**

✅ **Pass Criteria:**
- Clinical evaluation plan linked to CER
- Essential requirements traced to clinical data
- Risk-benefit analysis linked to clinical evidence

❌ **Failed Criteria:**
- 10 of 50 essential requirements lack clinical data linkage:
  - General Safety and Performance Requirements (GSPR) from Annex I not fully traced
- Clinical endpoints in CEP not all addressed in CER

**Remediation:**
1. Create comprehensive traceability matrix:
   - Column 1: GSPR Item (Annex I)
   - Column 2: Clinical Evidence Source
   - Column 3: CER Section Reference
2. Address all clinical endpoints from CEP in CER findings section

**After Remediation:** 50/50 requirements linked → Score: 95/100

#### Inspectable Dimension (Score: 88/100)

**Findings:**

✅ **Pass Criteria:**
- Document control version history present
- CER author qualifications documented
- Independent clinical evaluation reviewer identified
- Approval signatures present

❌ **Failed Criteria:**
- 2 clinical decisions lack documented rationale:
  - Decision to exclude pediatric population (no justification)
  - Decision to use historical controls instead of RCT (not explained)

**Remediation:**
1. Add clinical decision rationale:
   ```
   Decision: Exclude pediatric population
   Rationale: Device intended use specifies adults (18+). Pediatric physiology
   differs significantly (smaller body surface area, different vital sign
   ranges). Separate clinical evaluation required for pediatric indication per
   MDR Article 61(4). Currently no pediatric indication sought.
   ```
2. Document historical control rationale:
   ```
   Decision: Use historical controls
   Rationale: Well-established technology (monitoring via ECG). Equivalent
   predicate device clinical data available. Prospective RCT not ethically
   justified given known safety profile. Compliant with MDR Annex XIV Part A
   Section 1 for established technologies.
   ```

**After Remediation:** All decisions documented → Score: 96/100

#### Deliverable Dimension (Score: 92/100)

**Findings:**

✅ **Pass Criteria:**
- MEDDEV 2.7/1 Rev 4 template followed
- All required CER sections present
- Document structure compliant

❌ **Failed Criteria:**
- 2 sections incomplete:
  - Section 5.3 (Clinical data from equivalent devices) - placeholder text present
  - Section 7.2 (Post-Market Clinical Follow-up plan) - abbreviated content

**Remediation:**
1. Complete Section 5.3 with equivalent device clinical data analysis
2. Expand Section 7.2 PMCF plan with:
   - PMCF objectives
   - Data collection methods
   - Follow-up schedule
   - Success criteria

**After Remediation:** All sections complete → Score: 98/100

### Overall Assessment

**Initial Scores:**
- Verified: 72 ⚠️
- Accurate: 85
- Linked: 80
- Inspectable: 88
- Deliverable: 92
- **Overall: 83.4 (Grade B)**
- **Decision: CONDITIONAL PASS** (Verified dimension critical)

**Post-Remediation Scores:**
- Verified: 92
- Accurate: 94
- Linked: 95
- Inspectable: 96
- Deliverable: 98
- **Overall: 95.0 (Grade A)**
- **Decision: APPROVE FOR NOTIFIED BODY SUBMISSION**

---

## Example 3: Design History File (DHF)

### Document Context

**Document Type:** Design History File
**Submission:** Internal QMS documentation (FDA 21 CFR 820.30 compliance)
**Device Class:** Class II Medical Device
**Purpose:** Design control evidence for regulatory inspection

### VALID Validation Results

#### Verified Dimension (Score: 65/100) ❌ FAIL

**Findings:**

❌ **Critical Failures:**
- Only 8 of 25 design control activities reference 21 CFR 820.30 requirements
- Missing citations for:
  - Design validation requirements (21 CFR 820.30(g))
  - Design transfer requirements (21 CFR 820.30(h))
  - Design review requirements (21 CFR 820.30(e))
- Generic claims like "FDA requires design controls" without specific CFR reference (12 instances)

**Impact:** Critical dimension failure - score below 70 triggers automatic rejection

**Remediation Required:**
1. Add specific 21 CFR 820.30 citations to all design control activities
2. Replace generic "FDA requires" with specific CFR references:
   - Design planning → 21 CFR 820.30(b)
   - Design input → 21 CFR 820.30(c)
   - Design output → 21 CFR 820.30(d)
   - Design review → 21 CFR 820.30(e)
   - Design verification → 21 CFR 820.30(f)
   - Design validation → 21 CFR 820.30(g)
   - Design transfer → 21 CFR 820.30(h)
   - Design changes → 21 CFR 820.30(i)
   - Design history file → 21 CFR 820.30(j)

**Estimated Remediation Time:** 2-3 days

#### Linked Dimension (Score: 55/100) ❌ FAIL

**Findings:**

❌ **Critical Failures:**
- Incomplete traceability matrix (only 30 of 50 requirements traced)
- 20 requirements without test coverage
- 15 tests without requirement linkage (orphan tests)
- No bidirectional traceability established

**Remediation Required:**
1. Create comprehensive Requirements Traceability Matrix (RTM)
2. Add test coverage for all 50 requirements
3. Link orphan tests to requirements or justify removal
4. Establish bidirectional traceability verification process

**Estimated Remediation Time:** 1-2 weeks

### Overall Assessment

**Initial Scores:**
- Verified: 65 ❌
- Accurate: 78
- Linked: 55 ❌
- Inspectable: 75
- Deliverable: 70
- **Overall: 68.6 (Grade D)**
- **Decision: FAIL - SIGNIFICANT REWORK REQUIRED**

**Critical Issues:**
- 2 dimensions below 60 threshold
- Overall score below 80 minimum
- Not suitable for regulatory inspection

**Recommended Action:**
1. Escalate to design team and QA manager
2. Allocate 2-3 weeks for comprehensive DHF revision
3. Re-validate after remediation
4. Consider external QMS consultant review

---

## Example 4: Risk Management File

### Document Context

**Document Type:** Risk Management Report
**Standard:** ISO 14971:2019 Medical Device Risk Management
**Device Class:** Class III Medical Device (High Risk)

### VALID Validation Results

#### Verified Dimension (Score: 94/100)

**Findings:**

✅ **Excellent Performance:**
- 48 of 50 ISO 14971:2019 references verified accurate
- All risk analysis methods cited to standard annexes
- Risk acceptability criteria linked to ISO 14971 requirements

❌ **Minor Issues:**
- 2 references cite ISO 14971 without year designation (should specify :2019)

**Remediation:**
1. Add year designation: ISO 14971 → ISO 14971:2019 (2 instances)

**After Remediation:** Score: 98/100

#### Linked Dimension (Score: 98/100)

**Findings:**

✅ **Excellent Performance:**
- Complete Risk Traceability Matrix present
- All identified hazards traced to risk control measures
- All risk control measures traced to verification activities
- Residual risk evaluation linked to risk-benefit analysis

❌ **Minor Issues:**
- 1 hazardous situation (HS-045: User confusion due to similar buttons) lacks verification activity

**Remediation:**
1. Add verification activity: VER-089 (Formative usability study, Task 3)

**After Remediation:** Score: 100/100

### Overall Assessment

**Final Scores:**
- Verified: 98
- Accurate: 96
- Linked: 100
- Inspectable: 94
- Deliverable: 97
- **Overall: 97.0 (Grade A)**
- **Decision: APPROVE - EXCELLENT QUALITY**

---

## Key Lessons from Examples

### Common Failure Patterns

1. **Missing Specific Citations:** Generic claims like "FDA requires" without CFR reference
2. **Outdated Regulations:** Citing superseded standards (e.g., ISO 13485:2003 instead of :2016)
3. **Incomplete Traceability:** Requirements without test coverage
4. **Placeholder Text:** Sections with "[INSERT]" or "TBD" in final documents
5. **Broken References:** URLs that return 404 errors

### Best Practices

1. **Use Context7 MCP:** Always verify regulation text before citing
2. **Maintain Traceability from Start:** Don't defer traceability matrix to end
3. **Document Decisions Immediately:** Capture rationale when decision is made
4. **Review Before Quality Gate:** Self-review against VALID criteria before submission
5. **Iterative Improvement:** Expect 2-3 revision cycles to reach Grade A

### Typical Score Progression

**First Draft (Expected):** 65-75 (Grade D/C)
**After Initial Review:** 75-85 (Grade C/B)
**After Remediation:** 85-95 (Grade B/A)
**Final Submission:** 90-100 (Grade A)

### Remediation Time Estimates

| Issue Type | Typical Remediation Time |
|------------|-------------------------|
| Missing citations | 1-2 days |
| Outdated references | 2-3 days |
| Incomplete traceability | 1-2 weeks |
| Missing approvals | 1-3 days |
| Format non-compliance | 1-2 days |
| Fundamental gaps | 2-4 weeks |
