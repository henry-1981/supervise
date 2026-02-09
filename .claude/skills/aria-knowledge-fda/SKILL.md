---
name: aria-knowledge-fda
description: >
  FDA (Food and Drug Administration) 규정 전문 지식 스킬. 21 CFR Part 820 QSR, 510(k), PMA, De Novo 등 미국 의료기기 규제에 대한 상세 지식을 제공합니다.
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
  tags: "fda, 21-cfr-820, 510k, pma, de-novo, qsr, design-control, us-regulatory"
  author: "ARIA Core Team"
  context7-libraries: "fda-21-cfr-820, fda-510k, fda-pma"
  related-skills: "aria-domain-raqa, aria-knowledge-eumdr"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - FDA
    - 21 CFR 820
    - 510(k)
    - PMA
    - De Novo
    - QSR
    - Premarket notification
    - design control
  agents:
    - expert-regulatory
    - expert-submission
  phases:
    - plan
    - run
---

# FDA Regulatory Knowledge

## Overview

미국 FDA (Food and Drug Administration) 의료기기 규제 체계에 대한 포괄적인 지식을 제공합니다. CDRH (Center for Devices and Radiological Health)가 관할하는 의료기기 규제를 다룹니다.

## Device Classification

### Class-Based Requirements

| Class | Risk | Example | Requirements |
|-------|------|---------|--------------|
| Class I | Low | Bandages, glasses | General controls |
| Class II | Moderate | Infusion pumps, catheters | General + Special controls |
| Class III | High | Implants, life-support | General + Special + PMA |

### Classification Database

- FDA Product Classification Database: https://www.fda.gov/medical-devices/device-advisory-committees/product-classification-database
- 3-letter product code identifies device type
- 7-digit regulation number maps to requirements

## 21 CFR Part 820 - Quality System Regulation

### Key Subparts

**Subpart A - General Provisions (820.1-820.5)**
- 820.3: Definitions
- 820.5: Quality system

**Subpart B - Quality System Requirements (820.20-820.25)**
- 820.20: Management responsibility
- 820.22: Quality audit
- 820.25: Personnel

**Subpart C - Design Controls (820.30)**
- 820.30(a): Design and development planning
- 820.30(b): Design and development input
- 820.30(c): Design and development output
- 820.30(d): Design review
- 820.30(e): Design verification
- 820.30(f): Design validation
- 820.30(g): Design transfer
- 820.30(h): Design changes
- 820.30(i): Design history file

**Subpart D - Purchasing Controls (820.40-820.50)**
- 820.40: Purchasing controls
- 820.50: Purchasing data

**Subpart E - Identification and Traceability (820.60-820.70)**
- 820.60: Identification
- 820.65: Traceability

**Subpart F - Production and Process Controls (820.70-820.75)**
- 820.70: Production and process controls
- 820.72: Inspection, measuring, and test equipment
- 820.75: Process validation

**Subpart G - Acceptance Activities (820.80-820.90)**
- 820.80: Receiving, in-process, and finished device acceptance
- 820.86: Acceptance status
- 820.90: Finished device acceptance

**Subpart H - Nonconforming Product (820.100)**
- 820.100: Nonconforming product

**Subpart I - Corrective and Preventive Action (820.100)**
- 820.100: Corrective and preventive action

**Subpart J - Labeling and Packaging Control (820.120-820.130)**
- 820.120: Device labeling
- 820.130: Device packaging

**Subpart K - Handling, Storage, Distribution, and Installation (820.140-820.170)**
- 820.140: Handling
- 820.150: Storage
- 820.160: Distribution
- 820.170: Installation

**Subpart L - Records (820.180-820.198)**
- 820.180: General records
- 820.181: Device master record
- 820.184: Device history record
- 820.186: Quality system record
- 820.198: Complaint files

**Subpart M - Servicing (820.200)**
- 820.200: Servicing

**Subpart N - Statistical Techniques (820.250)**
- 820.250: Statistical techniques

## Premarket Submissions

### 510(k) - Premarket Notification

**Pathway Selection:**
- Traditional 510(k)
- Special 510(k) - device modification
- Abbreviated 510(k) - use of guidance documents

**Substantial Equivalence Criteria:**
1. Same intended use
2. Technological characteristics OR
3. New technology with safety/effectiveness data

**Required Elements:**
- Device description
- Indications for use
- 510(k) summary or statement
- Truthful and accurate statement
- Certifications
- Financial disclosure
- Proprietary information

**Timeline:**
- FDA RTA (Refuse to Accept) screening: 15 days
- FDA review goal: 90 days (MDUFA V)
- Average: 3-6 months

### PMA - Pre-Market Approval

**Applicability:**
- Class III devices
- Class II devices requiring PMA
- Substantially equivalent devices requiring PMN

**Required Sections (Original PMA):**
1. User fee information
2. Indications for use
3. Device description
4. Alternatives and rationale
5. Non-clinical studies
6. Clinical studies
7. Marketing history (foreign)
8. Probable benefits/risks
9. Patient population
10. Conditions of use
11. Components, materials, etc.
12. Manufacturing
13. Conformance to standards
14. Draft labeling
15. Summary and conclusions

**Timeline:**
- FDA filing decision: 30 days
- FDA review goal: 180 days (MDUFA V)
- Average: 6-12+ months

### De Novo Classification

**Applicability:**
- Novel devices
- Low-moderate risk
- No predicate
- Not Class III

**Process:**
1. Submit 510(k) - found not substantially equivalent
2. Request De Novo classification within 30 days
3. FDA evaluates for Class I or II

**Timeline:**
- FDA review goal: 120 days
- Average: 3-6 months

## Post-Market Requirements

### MDR (Medical Device Reporting) - 21 CFR Part 803

**Reportable Events:**
- Death: Within 5 working days
- Serious injury: Within 10 working days
- Malfunction: Within 30 days (annual report)

### Corrections and Removals - 21 CFR Part 806

**Reportable Actions:**
- To reduce risk to health
- Recall (Class I, II, III)
- Report within 10 working days

### 522 Postmarket Surveillance Studies

**Required Studies:**
- Ordered by FDA at time of approval
- Orders for specific device types
- 522 study orders on FDA website

## References

- FDA CDRH website: https://www.fda.gov/medical-devices
- CFR Title 21 database: https://www.ecfr.gov/current/title-21
- Device databases: https://www.fda.gov/medical-devices/device-databases
