---
name: aria-domain-raqa
description: >
  RA/QA (Regulatory Affairs/Quality Assurance) 도메인 전문 지식 스킬. 의료기기 규제, 품질 관리, 위험 관리, 임상 평가 등 RA/QA 전문가를 위한 포괄적인 도메인 지식을 제공합니다.
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
  tags: "aria, ra, qa, regulatory, quality, medical-device, fda, mdr, iso13485, iso14971"
  author: "ARIA Core Team"
  context7-libraries: "fda-21-cfr-820, eu-mdr-2017-745, iso-13485-2016, iso-14971-2019, iec-62304-2006"
  related-skills: "aria-knowledge-fda, aria-knowledge-eumdr, aria-knowledge-standards, aria-risk-management"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - regulatory
    - FDA
    - MDR
    - CAPA
    - risk
    - standard
    - clinical
    - submission
    - audit
    - 규제
    - 품질
    - 위험
    - 임상
    - 감사
  agents:
    - expert-regulatory
    - expert-standards
    - expert-risk
    - expert-capa
    - expert-clinical
    - expert-submission
    - expert-audit
  phases:
    - plan
    - run
---

# ARIA RA/QA Domain Knowledge

## Overview

ARIA (AI Regulatory Intelligence Assistant)는 의료기기 RA/QA 전문가를 위한 AI 어시스턴트 시스템입니다. 이 스킬은 RA/QA 도메인의 핵심 개념과 워크플로우를 제공합니다.

## Regulatory Frameworks

### Primary Regulatory Authorities

| Authority | Region | Key Regulation | Device Classification |
|-----------|--------|----------------|----------------------|
| FDA | United States | 21 CFR Part 820 | Class I, II, III |
| European Commission | EU | MDR 2017/745 | Class I, IIa, IIb, III |
| MFDS | Korea | Medical Device Act | Class I, II, III, IV |

### Submission Pathways

**FDA:**
- 510(k) - Substantial Equivalence
- PMA - Pre-Market Approval (Class III)
- De Novo - New Class I/II
- Exempt - 510(k) exemption

**EU MDR:**
- CE Class I - Self-certification
- CE Class IIa - Notified Body involvement
- CE Class IIb - Full Notified Body assessment
- CE Class III - Full NB + clinical investigation

**MFDS:**
- Class I - Registration
- Class II - Notification/Approval
- Class III - Approval
- Class IV - Approval + clinical data

## Quality Management

### ISO 13485:2016 QMS Requirements

**Key Clauses:**
- Clause 4: Quality Management System
- Clause 5: Management Responsibility
- Clause 6: Resource Management
- Clause 7: Product Realization
- Clause 8: Measurement, Analysis, Improvement

### CAPA Process

1. **Issue Identification**: Non-conformance detection
2. **Root Cause Analysis**: 5 Whys, Fishbone
3. **Corrective Action**: Fix immediate issue
4. **Preventive Action**: Prevent recurrence
5. **Effectiveness Check**: Verify effectiveness

## Risk Management

### ISO 14971:2019 Process

```
Risk Analysis → Risk Evaluation → Risk Control → Residual Risk Evaluation
```

**Key Concepts:**
- Hazard: Potential source of harm
- Harm: Injury or damage to health
- Risk: Combination of probability and severity
- ALARP: As Low As Reasonably Practicable

### Risk Analysis Methods

- **FMEA**: Failure Mode and Effects Analysis
- **FTA**: Fault Tree Analysis
- **STA**: Software Threat Analysis (IEC 62304)

## VALID Quality Framework

### Verified (검증됨)
- 모든 규제 주장에 출처 인용: [Standard] Section [Number]
- Context7 MCP를 통한 규정 원문 대조

### Accurate (정확함)
- 데이터 출처 검증
- 모순 데이터 확인 및 해결

### Linked (연결됨)
- 요구사항 ↔ 문서 ↔ 증거 추적성
- Notion DB 관계 설정

### Inspectable (검증 가능함)
- 결정 근거 문서화
- 감사 추적 완전성

### Deliverable (전달 가능함)
- 제출 형식 준수
- 템플릿 적합성

## Notion DB Integration

### CAPA Tracker Fields
- CAPA ID, Issue Date, Source, Problem Description
- Root Cause, Corrective Action, Preventive Action
- Responsible Person, Target Date, Status

### Risk Register Fields
- Risk ID, Hazard, Harm, Causes
- Severity, Probability, Risk Index
- Control Measures, Residual Risk, Acceptability

### Document Registry Fields
- Document ID, Type, Title, Version
- Effective Date, Author, Approver, Status

## Language Notes

- 사용자 대면 응답: 한국어 (conversation_language: ko)
- 코드 주석: 한국어 (code_comments: ko)
- 내부 에이전트 통신: 영어
