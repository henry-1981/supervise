---
name: aria-risk-management
description: >
  의료기기 위험관리(Risk Management) 스킬. ISO 14971 위험 분석 방법론(FMEA, FTA, STA), 위험-이익 분석, ALARP 원칙 등 위험관리 전 과정을 지원합니다.
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
  tags: "risk-management, fmea, fta, sta, risk-benefit, alarp, iso14971"
  author: "ARIA Core Team"
  context7-libraries: "iso-14971-2019"
  related-skills: "aria-domain-raqa, aria-knowledge-standards"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - risk management
    - FMEA
    - FTA
    - STA
    - risk assessment
    - risk control
    - residual risk
    - ALARP
    - risk-benefit analysis
  agents:
    - expert-risk
    - expert-design-control
    - expert-capa
  phases:
    - plan
    - run
---

# Medical Device Risk Management

## Overview

의료기기 위험관리는 ISO 14971:2019 표준에 따라 체계적으로 위험을 식별, 평가, 경감하고 잔여 위험을 평가하는 과정입니다.

## ISO 14971 Risk Management Process

### Phase 1: Risk Analysis (Clause 5)

#### 1.1 Intended Use and Foreseeable Misuse (5.2)

**Intended Use:**
- Manufacturer's specified use
- Indications for use
- Conditions of use

**Reasonably Foreseeable Misuse:**
- Intentionally incorrect use
- Inadvertent mistakes
- Use errors identified through usability testing

#### 1.2 Hazard Identification (5.3)

**Hazard Categories:**
- **Energy hazards**: Electrical, thermal, mechanical, radiation
- **Biological hazards**: Bioburden, toxicity, allergenicity
- **Environmental hazards**: Storage, transport, disposal
- **Use hazards**: Ergonomics, usability, interfaces
- **Functional failure hazards**: Software bugs, component failure

**Hazard Identification Methods:**
- Brainstorming
- Checklists
- FMEA (Failure Mode and Effects Analysis)
- FTA (Fault Tree Analysis)
- PHA (Preliminary Hazard Analysis)

#### 1.3 Risk Estimation (5.4)

**Risk Estimation Formula:**
```
Risk = Severity × Probability
```

**Severity Levels (ISO 14971 Annex C):**

| Level | Description | Example |
|-------|-------------|---------|
| Negligible | No noticeable effect | Temporary discomfort |
| Minor | Temporary injury | Outpatient treatment |
| Moderate | Serious injury | Hospitalization |
| Major | Life-threatening | ICU admission |
| Catastrophic | Patient death | Fatal outcome |

**Probability Levels (ISO 14971 Annex D):**

| Level | Description | Quantitative |
|-------|-------------|--------------|
| Frequent | > 10^-2 | > 1 in 100 |
| Probable | 10^-2 to 10^-3 | 1 in 100 to 1 in 1,000 |
| Occasional | 10^-3 to 10^-4 | 1 in 1,000 to 1 in 10,000 |
| Remote | 10^-4 to 10^-5 | 1 in 10,000 to 1 in 100,000 |
| Improbable | < 10^-5 | < 1 in 100,000 |

**Risk Matrix (Severity × Probability):**

| Severity \ Probability | Remote | Occasional | Probable | Frequent |
|------------------------|--------|------------|----------|----------|
| Catastrophic | High | High | High | High |
| Major | Medium | High | High | High |
| Moderate | Low | Medium | High | High |
| Minor | Low | Low | Medium | Medium |
| Negligible | Low | Low | Low | Low |

### Phase 2: Risk Evaluation (6.1)

**Acceptability Criteria:**

- **Acceptable**: No further risk control needed
- **ALARP** (As Low As Reasonably Practicable): Risk reduced as far as possible, benefit outweighs risk
- **Unacceptable**: Risk must be reduced

### Phase 3: Risk Control (7.1-7.5)

#### 3.1 Risk Control Options (Hierarchy)

**Option 1: Inherent Safety by Design**
- Eliminate hazard
- Reduce hazard severity
- Change design

**Option 2: Protective Measures**
- Alarms
- Interlocks
- Barriers
- Redundancy

**Option 3: Information for Safety**
- Labeling
- Instructions for Use
- Training
- Contraindications

#### 3.2 Risk Control Process

1. Identify risk control options
2. Evaluate options (effectiveness, feasibility)
3. Implement controls
4. Verify effectiveness

#### 3.3 Residual Risk Evaluation (7.3)

**Residual Risk Assessment:**
- Re-evaluate severity × probability
- Compare with acceptability criteria
- Document residual risk

#### 3.4 Overall Residual Risk Evaluation (7.4)

**Overall Residual Risk:**
- Sum of all residual risks
- Benefit-risk analysis
- Disclosure to users (if applicable)

### Phase 4: Risk-Benefit Analysis (7.5)

**Benefit-Risk Considerations:**

1. **Clinical Benefit**
   - Therapeutic effectiveness
   - Diagnostic accuracy
   - Patient outcomes

2. **Risk Factors**
   - Probability of harm
   - Severity of harm
   - Number of patients exposed

3. **Decision Criteria**
   - Benefit > Risk → Acceptable
   - Benefit ≈ Risk → ALARP evaluation
   - Benefit < Risk → Not acceptable

## Risk Analysis Methods

### FMEA (Failure Mode and Effects Analysis)

**FMEA Template:**

| Item | Failure Mode | Effect | Severity | Cause | Probability | RPN | Control |
|------|--------------|--------|----------|-------|-------------|-----|---------|
| Component A | Failure to open | Delayed treatment | 4 | Corrosion | 3 | 12 | Redundant path |
| Sensor B | Drift | Incorrect reading | 3 | Temperature | 2 | 6 | Calibration |

**RPN (Risk Priority Number) = Severity × Occurrence × Detection**

### FTA (Fault Tree Analysis)

**FTA Symbols:**
- AND gate: All inputs must occur
- OR gate: Any input causes output
- Basic event: Lowest level event
- Intermediate event: Result of logic

**FTA Example:**
```
                  Patient Injury
                        |
                 _______OR______
                 |              |
            Incorrect Dose    Device Failure
                 |
            ____OR____
            |         |
     Software    Hardware
     Error       Failure
```

### STA (Software Threat Analysis)

**STA Categories:**
- Input validation failures
- Output failures
- Data storage corruption
- Communication failures
- Timing failures
- Resource exhaustion

## ALARP Principle

**As Low As Reasonably Practicable:**

1. Reduce risk as far as possible
2. Consider:
   - Technical feasibility
   - Cost of reduction
   - Benefit of reduction
3. Document justification
4. Disclose residual risk (if applicable)

## Risk Management Documentation

### Risk Management File Contents (Clause 4.2)

1. **Risk Management Plan**
   - Scope, activities, responsibilities
   - Criteria for risk acceptability
   - Verification activities

2. **Risk Management Report**
   - Risk analysis results
   - Risk evaluation results
   - Risk control measures
   - Residual risk evaluation
   - Overall risk-benefit assessment

3. **Risk Analysis Records**
   - Hazard identification
   - Risk estimation
   - Risk evaluation

4. **Risk Control Records**
   - Control measures implemented
   - Verification of effectiveness

5. **Production and Post-Production Information**
   - Experience from devices in use
   - Relevant new information
   - Re-evaluation of risks

## Risk Register Structure

**Notion DB Risk Register Fields:**

- Risk ID (Auto-increment)
- Hazard (Text)
- Harm (Text)
- Causes (Text)
- Initial Severity (Select)
- Initial Probability (Select)
- Initial Risk Index (Formula)
- Control Measures (Text)
- Residual Severity (Select)
- Residual Probability (Select)
- Residual Risk Index (Formula)
- Risk Acceptability (Select)
- Benefit-Risk Analysis (Text)
- Related CAPA ID (Relation)
- Related Standard (Text)

## References

- ISO 14971:2019 - Medical devices — Application of risk management to medical devices
- ISO 13485:2016 - Medical devices — Quality management systems
- IEC 60601-1:2005 - Medical electrical equipment — General requirements
