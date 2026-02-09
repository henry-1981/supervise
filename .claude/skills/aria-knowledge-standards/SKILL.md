---
name: aria-knowledge-standards
description: >
  의료기기 표준(ISO, IEC) 전문 지식 스킬. ISO 13485 QMS, IEC 62304 소프트웨어, ISO 14971 위험관리 등 주요 의료기기 표준에 대한 상세 지식을 제공합니다.
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
  tags: "iso13485, iec62304, iso14971, iec60601, iec62366, qms, software-safety"
  author: "ARIA Core Team"
  context7-libraries: "iso-13485-2016, iec-62304-2006, iso-14971-2019"
  related-skills: "aria-domain-raqa, aria-risk-management"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - ISO 13485
    - IEC 62304
    - ISO 14971
    - IEC 60601
    - IEC 62366
    - harmonized standard
    - safety class
  agents:
    - expert-standards
    - expert-design-control
    - expert-risk
  phases:
    - plan
    - run
---

# Medical Device Standards Knowledge

## Overview

의료기기 산업의 주요 표준인 ISO 13485, IEC 62304, ISO 14971 등의 요구사항과 적용 방법을 제공합니다.

## ISO 13485:2016 - Medical Device Quality Management Systems

### Structure Overview

**Clause 4: Quality Management System (4.1-4.2.3)**
- 4.1: General requirements
- 4.2: Requirements (applicable statutory and regulatory requirements)
- 4.2.1: Quality management system
- 4.2.2: Quality manual
- 4.2.3: Medical device file

**Clause 5: Management Responsibility (5.1-5.6)**
- 5.1: Management commitment
- 5.2: Customer focus
- 5.3: Quality policy
- 5.4: Planning (quality objectives, QMS planning)
- 5.5: Responsibility, authority and communication
  - 5.5.1: Responsibility and authority
  - 5.5.2: Management representative
  - 5.5.3: Internal communication
- 5.6: Management review
  - 5.6.1: General
  - 5.6.2: Review input
  - 5.6.3: Review output

**Clause 6: Resource Management (6.1-6.3)**
- 6.1: Provision of resources
- 6.2: Human resources (competence, awareness, training)
- 6.3: Infrastructure
- 6.4: Work environment

**Clause 7: Product Realization (7.1-7.5.9)**
- 7.1: Planning of product realization
- 7.2: Processes related to customers
  - 7.2.1: Determination of requirements
  - 7.2.2: Review of requirements
  - 7.2.3: Communication
- 7.3: Design and development
  - 7.3.1: Design and development planning
  - 7.3.2: Design and development inputs
  - 7.3.3: Design and development outputs
  - 7.3.4: Design and development review
  - 7.3.5: Design and development verification
  - 7.3.6: Design and development validation
  - 7.3.7: Design and development changes
- 7.4: Purchasing
  - 7.4.1: Purchasing process
  - 7.4.2: Purchasing information
  - 7.4.3: Verification of purchased product
- 7.5: Production and service provision
  - 7.5.1: Control of production and service provision
  - 7.5.2: Validation of processes for production and service provision
  - 7.5.3: Identification and traceability
  - 7.5.4: Customer property
  - 7.5.5: Preservation of product
  - 7.5.6: Control of monitoring and measuring equipment
  - 7.5.7: Control of monitoring and measuring equipment (repealed)
  - 7.5.8: Release of product
  - 7.5.9: Control of nonconforming product

**Clause 8: Measurement, Analysis and Improvement (8.1-8.5.3)**
- 8.1: General
- 8.2: Monitoring and measurement
  - 8.2.1: Feedback
  - 8.2.2: Complaints
  - 8.2.3: Reporting to regulatory authorities
  - 8.2.4: Internal audit
  - 8.2.5: Monitoring and measurement of processes
  - 8.2.6: Monitoring and measurement of product
- 8.3: Control of nonconforming product
- 8.4: Analysis of data
- 8.5: Improvement
  - 8.5.1: Continual improvement
  - 8.5.2: Corrective action
  - 8.5.3: Preventive action

### Key Changes from ISO 13485:2003/ISO 9001

- Emphasis on risk-based approach
- Requirement for risk management file
- Requirement for medical device file
- Requirement for validation of sterile barrier
- Requirement for pseudo-homologation testing

## IEC 62304:2006 - Medical Device Software - Software Life Cycle Processes

### Safety Classification

**Class A (No injury or damage):**
- No injury or damage to health possible
- Example: Data logging only

**Class B (Non-serious injury):**
- Non-serious injury possible
- Example: Display errors, measurement errors

**Class C (Death or serious injury):**
- Death or serious injury possible
- Example: Life-support, drug delivery

### Software Life Cycle Processes

**Process 1: Software Development Planning**
- Software development plan
- Risk management activities
- Verification and validation activities

**Process 2: Software Requirement Analysis**
- Software requirements specification (SRS)
- Input to design
- Traceability to system requirements

**Process 3: Software Architecture Design**
- Software architecture description
- Identification of software items
- Traceability to requirements

**Process 4: Software Detailed Design**
- Detailed design of each software item
- Traceability to architecture

**Process 5: Software Unit Implementation**
- Coding standards
- Unit verification
- Code reviews

**Process 6: Software Integration**
- Integration strategy
- Integration testing
- Regression testing

**Process 7: Software Testing**
- Integration test plan and report
- Verification of requirements
- Coverage analysis

### Class-Specific Requirements

| Class | Documentation | Testing |
|-------|--------------|---------|
| A | SRS, Architecture, Unit test results | Unit testing |
| B | + Design, Integration test results | + Integration testing |
| C | + Verification, Validation, Config management | + System testing, Coverage 100% |

## ISO 14971:2019 - Medical Device Risk Management

### Risk Management Process (Clause 4-10)

**Clause 4: Risk Management Process (4.1-4.3)**
- 4.1: Risk management process
- 4.2: Risk management file
- 4.3: Roles and responsibilities

**Clause 5: Risk Analysis (5.1-5.5)**
- 5.1: Risk analysis
- 5.2: Intended use and reasonably foreseeable misuse
- 5.3: Identification of hazards
- 5.4: Estimation of risk
- 5.5: Risk evaluation

**Clause 6: Risk Evaluation (6.1)**
- 6.1: Risk evaluation criteria
- Acceptability thresholds

**Clause 7: Risk Control (7.1-7.6)**
- 7.1: Risk control options
  - Inherent safety by design
  - Protective measures
  - Information for safety
- 7.2: Risk control process
- 7.3: Residual risk evaluation
- 7.4: Overall residual risk evaluation
- 7.5: Risk-benefit analysis
- 7.6: Risk management review

**Clause 8: Evaluation of Overall Residual Risk (8.1)**
- 8.1: Criteria for acceptability

**Clause 9: Risk Management Report (9.1)**
- 9.1: Risk management report

**Clause 10: Production and Post-Production Information (10.1-10.3)**
- 10.1: Information gathering
- 10.2: Review of information
- 10.3: Feedback to risk management

### Risk Analysis Methods

**FMEA (Failure Mode and Effects Analysis):**
- Bottom-up approach
- Component-level failure modes
- Effects analysis

**FTA (Fault Tree Analysis):**
- Top-down approach
- Undesired event
- Logic gates (AND, OR)

**PHA (Preliminary Hazard Analysis):**
- Early design phase
- Hazard identification
- Initial risk assessment

## IEC 60601-1:2005 - Medical Electrical Equipment

### General Requirements

**Clause 8: Basic Safety**
- 8.1: Electrical shock hazard
- 8.2: Mechanical hazard
- 8.3: Radiation hazard
- 8.4: Temperature hazard
- 8.5: Hazardous flammable substances

**Essential Performance (Clause 3)**
- Performance necessary for safe use
- Defined by manufacturer
- Test methods required

### Risk Management Application

- ISO 14971 required
- Risk management file
- Essential performance linked to risk
- Safety testing based on risk

## IEC 62366-1:2015 - Usability Engineering

### Usability Process

1. **Use Specification**: Intended use, user profile, use environment
2. **Hazard Identification**: Use-related hazards
3. **User Interface Design**: Based on risk
4. **Validation**: Usability testing
5. **Formative Evaluation**: Ongoing testing

### Use-Related Risk Analysis

- Use scenarios
- Use errors
- Harm sequences
- Control measures

## Harmonized Standards

### EU Harmonized Standards (MDR)

- EN ISO 13485:2016
- EN ISO 14971:2019
- EN IEC 62304:2006
- EN IEC 60601-1:2006
- EN IEC 62366-1:2015

### FDA Recognized Standards

- Consensus standards database
- Use of standards creates presumption of conformity
- Standards not mandatory but recommended

## References

- ISO: https://www.iso.org
- IEC: https://www.iec.ch
- AAMI: https://www.aami.org
