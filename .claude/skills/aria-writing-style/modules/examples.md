# Writing Style Examples

Before and after examples demonstrating regulatory writing best practices.

## Active Voice Examples

### Example 1: Design Validation

**Before (Passive):**
"Design validation activities were conducted by the engineering team. Test protocols were developed and executed. Results were documented in the DHF."

**After (Active):**
"The engineering team conducted design validation activities. The team developed and executed test protocols. The team documented results in the DHF per 21 CFR 820.30(g)."

### Example 2: Risk Management

**Before (Passive):**
"Hazards were identified through FMEA. Risk levels were calculated using the risk matrix. Mitigation measures were implemented where necessary."

**After (Active):**
"The risk management team identified hazards through FMEA per ISO 14971:2019. The team calculated risk levels using the risk matrix defined in the Risk Management Plan. The team implemented mitigation measures for all Medium and High risks."

## Clarity Examples

### Example 3: Ambiguous Pronouns

**Before (Unclear):**
"The device interfaces with the software application. It must maintain data integrity during transmission. It should display error messages when communication fails."

**After (Clear):**
"The device interfaces with the software application. The device must maintain data integrity during transmission per IEC 62304 Section 5.2. The software application should display error messages when communication fails."

### Example 4: Complex Sentences

**Before (Complex):**
"The clinical evaluation report, which was prepared in accordance with MEDDEV 2.7/1 rev 4 and includes literature review, clinical investigation results, and post-market clinical follow-up data collected over the past 3 years, demonstrates that the device meets safety and performance requirements for the intended use as defined in the Instructions for Use."

**After (Simplified):**
"The clinical evaluation report demonstrates that the device meets safety and performance requirements for the intended use. The report was prepared per MEDDEV 2.7/1 rev 4. The report includes:
- Literature review per MEDDEV 2.7/1 Section 6
- Clinical investigation results (n=200, 6-month follow-up)
- Post-market clinical follow-up data (2023-2025)

The intended use is defined in the Instructions for Use, Section 2."

## Regulatory Language Examples

### Example 5: Requirement Levels

**Before (Inconsistent):**
"The manufacturer needs to establish a QMS. Design controls have to be implemented. Documentation must be maintained. It's recommended to perform internal audits."

**After (Consistent):**
"The manufacturer shall establish a Quality Management System per ISO 13485:2016.

The manufacturer shall implement design controls per 21 CFR 820.30.

The manufacturer shall maintain documentation per ISO 13485:2016 Section 4.2.

The manufacturer should perform internal audits per ISO 13485:2016 Section 8.2.2."

### Example 6: Citation Format

**Before (Incomplete):**
"The device complies with applicable standards including ISO 13485, IEC 60601, and ISO 14971."

**After (Complete):**
"The device complies with the following standards:
- ISO 13485:2016, Medical devices — Quality management systems
- IEC 60601-1:2012+AMD1:2020, Medical electrical equipment — Part 1: General requirements
- ISO 14971:2019, Medical devices — Application of risk management"

## Professional Tone Examples

### Example 7: Objective Language

**Before (Subjective):**
"Our innovative device uses cutting-edge technology to provide superior patient outcomes. The elegant design ensures maximum user satisfaction. Clinical results are impressive and demonstrate excellent performance."

**After (Objective):**
"The device achieves a 95% success rate (95% CI: 91-98%, n=200) per clinical investigation protocol CIP-2024-001. User satisfaction score is 4.2/5.0 (n=50 representative users) per IEC 62366-1 summative evaluation. Performance characteristics meet all essential performance requirements defined in IEC 60601-1-8:2020."

### Example 8: Evidence-Based Claims

**Before (Unsupported):**
"The device is safe for home use and easy to operate. Users can quickly learn the interface. The device rarely malfunctions."

**After (Evidence-Based):**
"Human factors validation demonstrates safe home use:
- 15/15 representative users (per IEC 62366-1 Table D.1) completed all critical tasks without use errors
- Mean task time: 3.2 minutes (SD = 0.8)
- System Usability Scale: 82/100 (Good usability per industry benchmark)

Reliability testing demonstrates 99.2% uptime over 10,000 operating hours (MTBF = 8,760 hours) per IEC 60601-1 testing protocol."

## Formatting Examples

### Example 9: List Usage

**Before (Paragraph):**
"Risk controls include double insulation to prevent electric shock, automatic shutoff after 30 minutes to prevent overheating, audible alarm for low battery, and visual indicator for fault conditions."

**After (List):**
"Risk controls implemented per ISO 14971:2019:

1. **Electric shock prevention**: Double insulation per IEC 60601-1 Section 8.6
2. **Overheating prevention**: Automatic shutoff after 30 minutes
3. **Power loss warning**: Audible alarm when battery < 10%
4. **Fault detection**: Visual indicator for error conditions per IEC 60601-1 Section 6.8"

### Example 10: Table Usage

**Before (Paragraph):**
"Software risk analysis identified three critical hazards. Incorrect dosage calculation has severity Catastrophic and probability Remote, resulting in Medium risk. Database corruption has severity Critical and probability Occasional, resulting in High risk. UI freezing has severity Marginal and probability Probable, resulting in Medium risk."

**After (Table):**

| Hazard ID | Hazard Description | Severity | Probability | Risk Level | Mitigation |
|-----------|-------------------|----------|-------------|------------|------------|
| SH-001 | Incorrect dosage calculation | Catastrophic | Remote | Medium | Input validation, calculation verification, unit test coverage 100% |
| SH-002 | Database corruption | Critical | Occasional | High | Transactional writes, automated backup every 1 hour, data integrity checks |
| SH-003 | UI freezing | Marginal | Probable | Medium | Async operations, timeout handling, user notification |

*Risk analysis per ISO 14971:2019 and IEC 62304:2006+AMD1:2015 Section 7.1*

## Document-Specific Examples

### Example 11: Executive Summary

**Before (Verbose):**
"This document has been created to provide a comprehensive overview of the clinical evaluation that was performed for the XYZ-100 device. The purpose of this evaluation was to assess whether the device is safe and performs as intended when used according to the manufacturer's instructions. A variety of data sources were examined including published literature, our own clinical investigation, and information gathered from users after the product launched."

**After (Concise):**
"This clinical evaluation report assesses the safety and performance of the XYZ-100 device per EU MDR Annex XIV.

**Scope**: Home-use blood glucose monitor for Type 2 diabetes patients

**Data Sources**:
- Literature review (15 relevant studies, 2018-2025)
- Clinical investigation (n=200, 6-month follow-up, CIP-2024-001)
- Post-market clinical follow-up (2,000 devices, 12 months)

**Conclusion**: Clinical data demonstrates the device meets safety and performance requirements for the intended use. Benefit-risk ratio is favorable per ISO 14971:2019."

### Example 12: Technical Specification

**Before (Ambiguous):**
"The device should be able to measure glucose levels accurately. It needs to work in normal room temperatures. Battery life should be reasonable. Results should display quickly."

**After (Specific):**
"Performance Specifications:

**REQ-001**: The device shall measure blood glucose concentration in the range 20-600 mg/dL.
- Acceptance Criteria: ±15 mg/dL for readings <100 mg/dL, ±15% for readings ≥100 mg/dL per ISO 15197:2013

**REQ-002**: The device shall operate at ambient temperature 10-40°C.
- Acceptance Criteria: All specifications met within temperature range per IEC 60601-1 testing

**REQ-003**: The device shall provide ≥500 measurements on a single battery charge.
- Acceptance Criteria: 500 consecutive measurements at 23°C ± 2°C

**REQ-004**: The device shall display measurement results within 5 seconds.
- Acceptance Criteria: Time from sample application to result display ≤ 5.0 seconds (95% CI)"

### Example 13: Review Report

**Before (Subjective):**
"I reviewed the design verification report and found a few issues. Some tests look incomplete and the data doesn't seem right. More work is needed before approval."

**After (Objective):**
"Design Verification Report Review - DVR-2024-002

**Review Date**: 2024-12-15
**Reviewer**: John Smith, Senior Design Engineer
**Document Version**: 1.0

**Findings**:

1. **Non-Conformance**: Test protocol TP-001 Section 3.2 missing acceptance criteria
   - Requirement: All test protocols shall define pass/fail criteria per 21 CFR 820.30(e)
   - Action Required: Add quantitative acceptance criteria to TP-001 Section 3.2

2. **Non-Conformance**: Table 4 battery life data shows n=3, specification requires n=10
   - Requirement: REQ-003 specifies minimum sample size n=10 per DVP-2024-001
   - Action Required: Complete additional 7 units testing

**Decision**: Conditional approval pending resolution of findings 1 and 2

**Next Steps**:
- Engineering to address findings by 2024-12-30
- Re-review scheduled for 2025-01-05"

## Common Mistakes - Corrected

### Example 14: Inconsistent Terminology

**Before:**
"The product was designed following QMS procedures. The medical equipment underwent testing. The item passed all specifications."

**After:**
"The medical device was designed per Quality Management System procedures defined in SOP-001. The medical device underwent verification testing per DVP-2024-001. The medical device passed all acceptance criteria per 21 CFR 820.30(f)."

### Example 15: Missing Traceability

**Before:**
"The device includes an alarm for low battery. This feature was tested and works correctly."

**After:**
"[REQ-015] The device shall activate an audible alarm when battery level drops below 10%.

**Verification**:
- Test Protocol: TP-003, Section 2.4
- Test Report: TR-003-2024, dated 2024-11-20
- Result: PASS - Alarm activated at 9.8% ± 0.2% battery level (n=10)
- Traceability: REQ-015 → TP-003 → TR-003-2024 → DHF Section 4.2"

### Example 16: Vague Risk Assessment

**Before:**
"The risk of data loss is low. We implemented backup systems to mitigate this risk. The residual risk is acceptable."

**After:**
"**Hazard H-012**: Patient data loss during device malfunction

**Risk Analysis** (per ISO 14971:2019):
- Severity: Critical (S3) - Loss of treatment history affects clinical decisions
- Probability: Remote (P2) - MTBF 8,760 hours based on reliability testing
- Initial Risk: Medium (Risk Index = 6)

**Risk Controls**:
1. Automatic cloud backup every 5 minutes (SRS-042)
2. Local storage redundancy (SRS-043)
3. Data integrity verification on device startup (SRS-044)

**Residual Risk Assessment**:
- Post-mitigation Probability: Improbable (P1)
- Residual Risk: Low (Risk Index = 3)
- Conclusion: Residual risk is acceptable per risk acceptability criteria (Risk Index ≤ 4) defined in Risk Management Plan RMP-2024-001"

## Review Checklist Application

### Example 17: Complete Document Review

**Document**: Clinical Evaluation Report v1.0

**Checklist Results**:

- [x] Active voice used consistently (3 passive voice instances corrected in Section 4.2)
- [x] No ambiguous pronouns (replaced "it" with specific nouns in 8 locations)
- [x] One idea per sentence (split 12 complex sentences)
- [x] Correct requirement levels (standardized shall/should/may usage)
- [x] Complete citations (added versions to 15 standard references)
- [x] Objective language (removed promotional language in Section 2.1)
- [x] Consistent terminology ("device" used consistently, not "product"/"equipment")
- [x] Proper heading hierarchy (6 levels corrected)
- [x] Lists and tables formatted correctly
- [x] Document version and date on title page

**Overall Assessment**: PASS - Document meets writing standards per this style guide
