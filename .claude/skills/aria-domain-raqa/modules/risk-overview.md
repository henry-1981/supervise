# Risk Management Overview

## ISO 14971 Risk Management Framework

ISO 14971:2019 provides the internationally recognized framework for medical device risk management.

## Risk Management Principles

1. **Risk is inherent in all medical devices**
2. **Risk must be reduced as far as possible (AFAP)**
3. **Residual risk must be acceptable**
4. **Risk management is continuous**

## Risk Definitions

- **Hazard**: Potential source of harm
- **Harm**: Physical injury or damage to health
- **Hazardous Situation**: Circumstance with exposure to hazard(s)
- **Risk**: Combination of probability of harm and severity
- **Risk Acceptability**:
  - Acceptable: Further reduction not practically possible
  - ALARP: As Low As Reasonably Practicable
  - Unacceptable: Must be reduced

## Risk Management Process

### Step 1: Risk Analysis

#### 1.1 Hazard Identification

**Identification Methods:**
- Brainstorming
- Literature review
- Standards review (ISO 14971 Annex C)
- FMEA, FTA

**Common Hazard Categories:**
- Energy hazards (electrical, thermal, radiation)
- Biological hazards (bioburden, toxicity)
- Environmental hazards
- Functional failures

#### 1.2 Risk Estimation

For each hazardous situation, estimate:
- **Severity**: 1 (Negligible) to 5 (Catastrophic)
- **Probability**: 1 (Remote) to 5 (Frequent)
- **Risk Index**: Severity × Probability

### Step 2: Risk Evaluation

Compare estimated risks against acceptability criteria.

**Risk Matrix:**

| Severity \ Probability | Remote (1) | Low (2) | Medium (3) | High (4) | Frequent (5) |
|----------------------|-----------|---------|-----------|---------|-------------|
| Catastrophic (5) | 5 | 10 | 15 | 20 | 25 |
| Serious (4) | 4 | 8 | 12 | 16 | 20 |
| Moderate (3) | 3 | 6 | 9 | 12 | 15 |
| Minor (2) | 2 | 4 | 6 | 8 | 10 |
| Negligible (1) | 1 | 2 | 3 | 4 | 5 |

**Acceptability:**
- 1-3: Generally Acceptable
- 4-8: Acceptable with routine review
- 9-15: ALARP - mitigation required
- 16-25: Unacceptable - mitigation mandatory

### Step 3: Risk Control

#### 3.1 Risk Control Options (in order of preference)

**1. Inherent Safety by Design**
- Eliminate hazard through design

**2. Protective Measures**
- Add safety mechanisms

**3. Information for Safety**
- Warnings, precautions, contraindications

### Step 4: Overall Residual Risk Evaluation

Aggregate all residual risks and evaluate overall acceptability.

## Risk Management Tools

### FMEA (Failure Mode and Effects Analysis)

**Purpose:** Bottom-up analysis of component failures

**RPN = Severity × Occurrence × Detection**

### FTA (Fault Tree Analysis)

**Purpose:** Top-down analysis of system failures

## Notion DB Integration

### Risk Register Fields

**Required:**
- Risk ID, Hazard, Harm, Severity, Probability
- Risk Index (Formula: Severity × Probability)
- Risk Acceptability (Acceptable, ALARP, Unacceptable)
- Control Measures, Residual Risk Index

---

**Version:** 1.0.0
**Last Updated:** 2026-02-09
