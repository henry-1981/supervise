---
name: aria-knowledge-eumdr
description: >
  EU MDR (Medical Device Regulation 2017/745) 전문 지식 스킬. CE Marking, Technical File, Clinical Evaluation, PMS 등 유럽 의료기기 규제에 대한 상세 지식을 제공합니다.
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
  tags: "eu-mdr, ce-marking, technical-file, clinical-evaluation, pms, notified-body"
  author: "ARIA Core Team"
  context7-libraries: "eu-mdr-2017-745"
  related-skills: "aria-domain-raqa, aria-knowledge-fda"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - EU MDR
    - CE Marking
    - Technical File
    - Clinical Evaluation Report
    - PMS
    - Notified Body
    - Annex I
    - MDR 2017/745
  agents:
    - expert-regulatory
    - expert-clinical
    - expert-submission
  phases:
    - plan
    - run
---

# EU MDR Regulatory Knowledge

## Overview

유럽 MDR (Medical Device Regulation 2017/745)은 의료기기의 안전性和 성능을 보장하기 위한 규정입니다. 2021년 5월 26일부터 완전히 시행되었습니다.

## Device Classification

### Classification Rules (MDR Annex VIII)

**Rule 1-4:** Non-invasive devices
- Rule 1: Body orifice → Class I
- Rule 2: Channel/skin penetration → Class IIa or IIb
- Rule 3: Skin injury → Class IIa
- Rule 4: Skin surface, mechanical → Class I

**Rule 5-8:** Invasive devices
- Rule 5: Body orifice, surgically invasive → Class IIa
- Rule 6: Transient use (<60 min) → Class I, IIa
- Rule 7: Short-term use (≤30 days) → Class IIa, IIb
- Rule 8: Long-term use (>30 days) → Class IIb, III

**Rule 9-12:** Surgical invasive devices
- Rule 9: Short-term → Class IIa
- Rule 10: Long-term → Class IIb
- Rule 11: Joint replacement → Class III
- Rule 12: Implanted, long-term → Class III

**Rule 13-16:** Active devices
- Rule 13: Active therapeutic → Class IIa or IIb
- Rule 14: Active diagnostic → Class IIa
- Rule 15: Active, direct diagnosis → Class IIa or IIb
- Rule 16: Active, intended to administer energy → Class IIa or IIb

**Rule 17-22:** Special rules
- Rule 17: Nanomaterial → Class III
- Rule 18: Medicinal product → Class III
- Rule 19: Human/animal origin → Class III (except if contact with intact skin)
- Rule 20: Cell/tissue → Class III
- Rule 21: Combination product → Class III
- Rule 22: Reusable surgical instruments → Class I

## Annex I - General Safety and Performance Requirements (GSPR)

### Chapter I - General Requirements (Article 5)

**GSPR 1:** Safety and performance
- GSPR 1.1: Acceptable risk-benefit ratio
- GSPR 1.2: Intended use achieved
- GSPR 1.3: Safety and performance under normal conditions

**GSPR 2:** Risk management
- ISO 14971 principles applied
- Risks reduced as far as possible (AFAP)
- Residual risks acceptable

**GSPR 3:** Technical documentation
- Technical file complete
- Clinical evaluation positive
- Benefit-risk ratio favorable

**GSPR 4:** Randomized clinical trials (if applicable)
- GSPR 5: Side effects acceptable
- GSPR 6: Information for safety

### Chapter II - Requirements Regarding Design and Manufacture

**GSPR 7:** Chemical, physical and biological properties
- GSPR 7.1: Toxicological assessment
- GSPR 7.2: Biocompatibility (ISO 10993)
- GSPR 7.3: Software validation (IEC 62304)

**GSPR 8:** Infection and microbial contamination
- GSPR 8.1: Sterile
- GSPR 8.2: Microbial limits
- GSPR 8.3: Reusable devices: cleaning, disinfection, sterilization

**GSPR 9:** Properties regarding environment
- GSPR 9.1: Interference with other equipment
- GSPR 9.2: EMC compliance (IEC 60601-1-2)
- GSPR 9.3: Software and IT systems

**GSPR 10:** Devices with a measuring function
- GSPR 10.1: Accuracy within stated limits
- GSPR 10.2: Metrological requirements

**GSPR 11:** Radiation protection
- GSPR 11.1: Justification of radiation dose
- GSPR 11.2: Optimization (ALARA)

**GSPR 12:** Requirements for devices with an integrated or incorporated medicinal substance

**GSPR 13:** Requirements for devices manufactured utilising tissues or cells of human or animal origin

**GSPR 14:** Requirements regarding information supplied by the manufacturer

## Clinical Evaluation (Annex XIV, Article 61)

### CER (Clinical Evaluation Report) Requirements

**Section 1: Device Description**
- Intended purpose
- Target population
- Medical condition

**Section 2: Clinical Evaluation Report Summary**
- Scope
- Methodology
- Data sources

**Section 3: Methodology**
- Literature search (PRISMA)
- Appraisal of data
- Weighing of benefits vs risks

**Section 4: Search Strategy**
- Databases: PubMed, Cochrane, ClinicalTrials.gov
- Search terms
- Inclusion/exclusion criteria

**Section 5: Literature Search Results**
- PRISMA flow diagram
- Included studies
- Excluded studies with reasons

**Section 6: Appraisal of Data**
- Study quality assessment
- Relevance to device
- Weight of evidence

**Section 7: Analysis of Data**
- Clinical performance
- Safety profile
- Benefit-risk ratio

**Section 8: Qualitative and Quantitative Synthesis**
- Meta-analysis (if applicable)
- Forest plots

**Section 9: Overall Clinical Benefit-Risk Analysis**
- Clinical benefits
- Risks
- Uncertainties

**Section 10: Conclusions**
- Clinical evaluation positive
- GSPR compliance

**Section 11: Discussion**
- Strengths
- Limitations
- Residual concerns

**Section 12: Annexes**

### Equivalence (Article 61)

Three conditions for equivalence:
1. **Technical**: Same design, materials, specifications
2. **Biological**: Same body contact, tissues
3. **Clinical**: Same condition, population, user

## Technical File (Annex II)

### Required Documentation

**Section 1: Device description and specification**
- Intended use
- Variants and accessories
- Conformity assessment route

**Section 2: Labeling and IFU**
- Labels (primary, secondary, packaging)
- Instructions for Use

**Section 3: GSPR checklist**
- Reference to each GSPR
- Evidence of compliance

**Section 4: Risk management**
- ISO 14971 report
- Risk management file
- Summary of findings

**Section 5: Clinical evaluation**
- CER (Annex XIV)
- Clinical investigation report (if applicable)

**Section 6: Benefit-risk analysis**
- Overall benefit-risk determination

**Section 7: Product verification and validation**
- Testing reports
- Verification of conformity
- Validation of design

**Section 8: Lab data, sterilization, biocompatibility**
- Sterilization validation
- Biocompatibility assessment (ISO 10993)

**Section 9: Manufacturing**
- Manufacturing processes
- Quality management system (ISO 13485)

**Section 10: Pre-market clinical investigation**
- Clinical investigation report

**Section 11: Post-market clinical follow-up (PMCF)**
- PMCF protocol
- PMCF report

**Section 12: Declaration of interest**

## Post-Market Surveillance (Article 83-88)

### PMS Requirements

**PMS System (Article 83):**
- Proactive, systematic
- Collects experience from devices
- Provides information for:
  - Trend reporting (Article 88)
  - Preventive corrective action
  - Field safety corrective actions (FSCA)
  - Updates to benefit-risk determination
  - Updates to clinical evaluation

**Vigilance (Article 87):**
- Report serious incidents
- Report field safety corrective actions (FSCA)
- Report trend reporting
- Periodic safety update reports (PSUR)

**PSUR (Article 86):**
- Class III devices: Annually
- Class IIb: Every 2 years (if implantable or invasive)
- Class IIa: Every 3 years (if long-term monitoring)

## References

- MDR 2017/745 full text: https://health.ec.europa.eu/medical-devices-sector/new-regulations_en
- MDR guidelines: https://health.ec.europa.ca/medical-devices-sector/guidance_en
