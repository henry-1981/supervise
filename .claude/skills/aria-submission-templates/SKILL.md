---
name: aria-submission-templates
description: >
  의료기기 규제 제출(Regulatory Submission) 템플릿 전문 스킬.
  FDA 510(k), PMA, CE Marking 등 주요 제출 유형별 템플릿과
  eCopy format 요구사항, RTA criteria 등 제출 준비 과정을
  포괄적으로 지원합니다.

license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
user-invocable: false

metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "submission, 510k, pma, ce-marking, technical-file, ecopy, regulatory"
  context7-libraries: "fda-21-cfr-807, fda-21-cfr-814, eu-mdr-2017-745"
  related-skills: "aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr"
  aliases: "regulatory-submission, fda-submission, ce-submission"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "510(k)"
    - "submission"
    - "PMA"
    - "CE marking"
    - "technical file"
    - "eCopy"
    - "premarket notification"
    - "regulatory submission"
  agents:
    - "expert-submission"
  phases:
    - "run"
  languages: []
---

# Regulatory Submission Templates

의료기기 규제 기관 제출을 위한 템플릿과 가이드라인입니다.

## Submission Types

### FDA 제출

1. **510(k) Premarket Notification**
   - Class II 기기 주요
   - Substantial Equivalence (SE) 증명
   - 90일 심사 기간

2. **PMA (Premarket Approval)**
   - Class III 기기 필수
   - 안전성/유효성 입증
   - 180일 심사 기간 (평균)

### EU 제출

1. **CE Marking**
   - MDR 2017/745 준수
   - Technical File 필수
   - Notified Body 심사

## 510(k) Submission

### 510(k) Submission Types

| Type | Description | Requirements |
|------|-------------|--------------|
| Traditional | Full 510(k) | Predicate device, substantial equivalence |
| Abbreviated | Simplified | Special 510(k), well-established technology |
| Special | Special 510(k)| Guideline-based, well-understood risks |

### 510(k) Package Structure (eCopy Format)

```
510(k)-[Device Name]-[Date].pdf
├── Section 1: User Fee Cover Sheet
├── Section 2: Indications for Use
├── Section 3: 510(k) Statement
├── Section 4: Device Description
├── Section 5: Truthful and Accuracy Statement
├── Section 6: Class III Summary (if applicable)
├── Section 7: Financial Certifications
├── Section 8: Declarations
├── Section 9: Class II Special Controls (if applicable)
├── Section 10: Proposed Label
├── Section 11: Sterility and Pyrogenicity (if applicable)
├── Section 12: Biocompatibility (if applicable)
├── Section 13: 510(k) Summary
└── Section 14: Attachments
```

### Section-by-Section Guide

#### Section 1: User Fee Cover Sheet

**Contents**:
- Device name
- 510(k) type (Traditional/Abbreviated/Special)
- Fee payment confirmation
- Contact information

**Template**:
```markdown
USER FEE COVER SHEET

Device Name: [Name]
510(k) Type: [Traditional/Abbreviated/Special]
Applicant: [Company Name]
Contact: [Name, Email, Phone]

Fee Payment:
- Fee paid: [Yes/No]
- Payment Date: YYYY-MM-DD
- Payment Amount: $[Amount]
- Small Business: [Yes/No]

Certification:
I certify that the user fee has been paid in accordance with 21 CFR 807.80.
```

#### Section 2: Indications for Use

**Contents**:
- Intended use
- Contraindications
- Warnings
- Precautions

**Template**:
```markdown
INDICATIONS FOR USE

Intended Use:
[Describe the intended use of the device]

Contraindications:
- [List contraindications]

Warnings:
- [List warnings]

Precautions:
- [List precautions]
```

#### Section 3: 510(k) Statement

**Contents**:
- Substantial equivalence statement
- Predicate device identification

**Template**:
```markdown
510(k) STATEMENT

I certify that the device named above is substantially equivalent to the predicate device(s) identified in this submission.

Predicate Device(s):
- [Device Name, 510(k) Number]

Substantial Equivalence Summary:
[Brief summary of SE demonstration]
```

#### Section 4: Device Description

**Contents**:
- Device specifications
- Technology type
- Principles of operation

**Template**:
```markdown
DEVICE DESCRIPTION

Device Name: [Name]
Device Type: [Type]
Technology: [Description]

Specifications:
- Dimensions: [Dimensions]
- Weight: [Weight]
- Materials: [List]
- Components: [List]

Principles of Operation:
[Describe how device works]
```

#### Section 13: 510(k) Summary

**Contents**:
- Device identification
- Intended use
- Predicate device
- Substantial equivalence
- Risks
- Benefits

### RTA (Refuse to Accept) Criteria

**Common RTA Triggers**:

| Trigger | Description | Prevention |
|---------|-------------|------------|
| Missing Sections | Required sections incomplete | Pre-submission checklist |
| Incorrect Format | Non-compliant eCopy | eCopy validation tool |
| Missing Fees | User fee not paid | Fee payment verification |
| Invalid Predicate | Predicate not 510(k) cleared | Predicate search validation |
| Incomplete Information | Critical information missing | Completeness review |

**Pre-Submission Checklist**:
- [ ] All 14 sections included
- [ ] eCopy format compliant
- [ ] PDF/A format
- [ ] File size < 10MB (unless justified)
- [ ] All attachments included
- [ ] User fee paid
- [ ] Digital signature ready
- [ ] Predicate device valid

## PMA Submission

### PMA Format Options

| Format | Description | When to Use |
|--------|-------------|-------------|
| Original PMA | Single submission | Class III devices |
| Modular PMA | Split into modules | Large applications |
| Supplemental PMA | Update to PMA | Post-approval changes |

### Original PMA Structure

```
Volume 1: User Fee, Administrative
├── Cover Sheet
├── User Fee
├── Administrative Information
└── Certifications

Volume 2: Nonclinical Lab Studies
├── Bench Testing
├── Animal Studies
└── Literature Reviews

Volume 3: Clinical Studies
├── Clinical Investigation Plan
├── Clinical Data
└── Statistical Analysis

Volume 4: Manufacturing
├── Facilities
├── Processes
├── Quality Controls
└── Supplier Controls

Volume 5: Case Histories
├── Clinical Cases
├── Adverse Events
└── Complications
```

### Modular PMA Structure

```
Module 1: User Fee Cover Sheet and Administrative Information
Module 2: Table of Contents and Module Information
Module 3: Device Description and Classification
Module 4: Nonclinical Studies
Module 5: Clinical Studies
Module 6: Manufacturing Information
Module 7: Proprietary Information and Objections
Module 8: Executive Summary
```

## CE Marking Technical File

### Technical File Structure (MDR Annex II)

```
Technical File
├── 1. Device Description and Specification
│   ├── Device name, model, version
│   ├── Intended use
│   ├── Contraindications
│   ├── Technical specifications
│   └── Software description (if applicable)
├── 2. Labeling and IFU
│   ├── Labels
│   ├── Instructions for Use
│   └── Symbols
├── 3. Risk Analysis
│   ├── ISO 14971 Risk Management File
│   ├── Risk-benefit analysis
│   └── Residual risk assessment
├── 4. Clinical Evaluation
│   ├── CER (Annex XV)
│   ├── Clinical investigation data
│   └── PMCF plan
├── 5. Product Verification and Validation
│   ├── Verification reports
│   ├── Validation reports
│   └── Traceability matrix
├── 6. Design Control Documentation
│   ├── DHF summary
│   ├── Design reviews
│   └── Design transfer
└── 7. Manufacturing Processes
    ├── Process validation
    ├── Quality controls
    └── Supplier controls
```

### Essential Requirements (Annex I) Checklist

| ER | Requirement | Evidence | Status |
|----|------------|----------|--------|
| ER 1 | General requirements | [Evidence] | [ ] |
| ER 2 | Requirements regarding essential characteristics | [Evidence] | [ ] |
| ER 3 | Requirements regarding clinical evaluation | [Evidence] | [ ] |
| ER 4 | Requirements regarding labelling | [Evidence] | [ ] |
| ER 5 | Requirements regarding information supplied | [Evidence] | [ ] |
| ER 6 | Requirements regarding clinical investigation | [Evidence] | [ ] |
| ... | ... | ... | ... |

### Annex III: Summary of Safety and Performance (SSP)

**Safety Section**:
- Residual risks
- Risk control measures
- Risk-benefit ratio
- Overall safety conclusion

**Performance Section**:
- Clinical performance
- Technical performance
- Usability performance
- Overall performance conclusion

## eCopy Format Requirements

### File Format Specifications

| Requirement | Specification |
|-------------|---------------|
| Format | PDF/A-1a (ISO 19005-1) |
| File Size | < 10MB (unless justified) |
| Naming | [510(k) Number]-[Device Name]-[Date].pdf |
| OCR | Searchable (not image-only) |
| Bookmarks | Required for each section |
| Navigation | Hyperlinks to sections |
| Attachments | Embedded in single file |

### eCopy Creation Steps

1. **Document Assembly**
   - Complete all sections
   - Include all attachments
   - Review for completeness

2. **PDF Conversion**
   - Convert to PDF/A-1a format
   - Verify OCR capability
   - Check file size

3. **Final Validation**
   - RTA criteria check
   - Bookmark verification
   - Link validation

## Submission Readiness Review

### Pre-Submission Checklist (510(k))

- [ ] User fee paid
- [ ] Section 1-14 complete
- [ ] eCopy format compliant
- [ ] PDF/A format
- [ ] Digital signature ready
- [ ] Predicate device identified
- [ ] Substantial equivalence demonstrated
- [ ] Truthful and Accuracy statement signed
- [ ] All required attachments included
- [ ] RTA criteria passed

### Pre-Submission Checklist (PMA)

- [ ] User fee paid
- [ ] Modules 1-8 complete
- [ ] Nonclinical data complete
- [ ] Clinical data complete
- [ ] Manufacturing data complete
- [ ] Case histories included
- [ ] Executive summary complete

### Pre-Submission Checklist (CE)

- [ ] Classification complete
- [ ] Technical File complete
- [ ] Essential Requirements met
- [ ] Risk analysis complete
- [ ] Clinical Evaluation Report complete
- [ ] Declaration of Conformity signed
- [ ] NB review complete

## Common Submission Errors

### Error 1: RTA Trigger

**Problem**: Submission refused for acceptance

**Solution**:
- Comprehensive pre-submission review
- RTA criteria checklist
- Peer review process

### Error 2: Incorrect Format

**Problem**: Non-compliant format

**Solution**:
- Use official template
- Format validation tool
- Peer review

### Error 3: Incomplete Information

**Problem**: Missing critical data

**Solution**:
- Completeness checklist
- Subject matter expert review
- Pre-submission meeting

## Best Practices

### 1. Early Planning

- Start submission preparation early
- Identify predicate device early
- Plan clinical data collection

### 2. Template Usage

- Use official templates
- Follow format guidelines
- Include all required sections

### 3. Pre-Submission Review

- Conduct internal review
- External expert review
- Mock FDA review

### 4. Electronic Format

- Verify PDF/A compliance
- Test file size
- Check bookmarks/links

---

## Modules

자세한 내용은 각 모듈을 참조하세요:

- `modules/510k-template.md` - 510(k) 템플릿
- `modules/pma-template.md` - PMA 템플릿
- `modules/ce-marking.md` - CE Marking 템플릿
- `modules/e-copy.md` - eCopy format 가이드

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Reference**: [FDA 21 CFR 807], [FDA 21 CFR 814], [MDR 2017/745]
