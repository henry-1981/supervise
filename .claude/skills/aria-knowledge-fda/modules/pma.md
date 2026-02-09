# FDA PMA - Premarket Approval

## Overview

PMA is the most rigorous FDA premarket review process for Class III medical devices that support or sustain human life.

## PMA Applicability

### When is PMA Required?

**Class III Devices:**
- High-risk devices
- Life-sustaining or life-supporting devices
- Devices with insufficient 510(k) predicate
- Novel technologies

**Examples:**
- Implantable pacemakers
- Ventricular assist devices
- Artificial hearts
- Many diagnostic devices

## PMA Application Structure

### Volume Organization

**Volume 1: User Fee and Administrative**
- Form FDA 3514
- User fee payment
- Administrative information

**Volume 2: Nonclinical Laboratory Studies**
- Animal studies
- Bench testing
- Engineering testing
- Biocompatibility studies

**Volume 3: Clinical Studies**
- Clinical investigation data
- Statistical analysis
- Clinical study reports

**Volume 4: Manufacturing**
- Manufacturing processes
- Facilities
- Quality systems
- Controls

**Volume 5: Case Histories**
- Summary of safety and effectiveness
- Adverse reactions
- Complications

## PMA Submission Contents

### Required Elements

**1. Administrative Information**
- Manufacturer information
- Device description
- Indications for use

**2. Device Description**
- Principles of operation
- Specifications
- Components and materials

**3. Nonclinical Studies**
- Animal studies
- Bench testing
- Engineering performance
- Biocompatibility

**4. Clinical Studies**
- Study design and methodology
- Clinical data
- Statistical analysis
- Adverse events

**5. Manufacturing**
- Process validation
- Quality control procedures
- Facilities and equipment

**6. Labeling**
- Draft labeling
- Instructions for use
- Patient labeling

**7. Safety and Effectiveness**
- Summary of data
- Benefit-risk analysis
- Conclusions

## PMA Review Process

### FDA Review Timeline

**1. Filing Review (30 days)**
- Determine if submission is complete
- Accept for filing or refuse to file

**2. Substantive Review (180 days)**
- Detailed review of submission
- Advisory committee meeting (if needed)
- Approval or not-approval decision

**3. Post-Approval**
- Post-approval studies
- Annual reports
- Condition of approval

### Advisory Committee

**When:**
- First-of-a-kind device
- High-risk technology
- Controversial safety/effectiveness

**Process:**
- Panel of expert advisors
- Public meeting
- Recommendation to FDA

## PMA Supplements

### Types

**1. 180-Day Supplement**
- Major changes affecting safety or effectiveness
- New indications
- Major design changes

**2. Real-Time Supplement**
- Manufacturing location changes
- Certain labeling changes

**3. 30-Day Notice**
- Minor changes to device or process
- Not requiring prior FDA approval

**4. 135-Day Supplement**
- Moderate changes
- Between 30-day and 180-day

## User Fees

### FY 2026 Fees

| Submission Type | Fee |
|----------------|-----|
| PMA | $385,950 |
| Small Business PMA | $96,488 |
| PMA Supplement | $96,488 |

## Context7 Integration

```yaml
# PMA lookup
mcp__context7__resolve-library-id(query="FDA PMA guidance")
mcp__context7__get-library-docs(topics=["clinical-studies", "manufacturing"])
```

## Key References

- 21 CFR 814: Premarket Approval
- 21 CFR 814.20: PMA application contents
- FDA Guidance: Device Advice Program

---

**Version:** 1.0.0
**Last Updated:** 2026-02-09
**Citation Standard:** [21 CFR 814] Section [Number]
