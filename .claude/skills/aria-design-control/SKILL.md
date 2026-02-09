---
name: aria-design-control
description: >
  의료기기 Design Control 전문 스킬. FDA 21 CFR 820.30 Design Control 요구사항을 기반으로
  DHF(Design History File), DMR(Device Master Record), DHR(Device History Record) 관리,
  설계 추적성 매트릭스(Traceability Matrix) 작성 등 설계 통제 전 과정을 지원합니다.

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
  tags: "design-control, dhf, dmr, dhr, traceability, fda, medical-device"
  context7-libraries: "fda-21-cfr-820"
  related-skills: "aria-domain-raqa, aria-risk-management"
  aliases: "design-control, fda-design, dhf-management"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "design history file"
    - "design control"
    - "DHF"
    - "DMR"
    - "DHR"
    - "design input"
    - "design output"
    - "design verification"
    - "design validation"
    - "traceability matrix"
    - "design transfer"
    - "21 CFR 820.30"
  agents:
    - "expert-design-control"
  phases:
    - "run"
  languages: []
---

# Design Control (설계 통제)

의료기기 설계 통제(Design Control)에 대한 포괄적인 지식을 제공합니다. FDA 21 CFR 820.30 요구사항을 중심으로 DHF, DMR, DHR 관리 및 추적성 확보 방법을 다룹니다.

## Design Control 개요

### Purpose (목적)

Design Control은 의료기기 설계 및 개발 과정을 체계적으로 관리하여:

- 제품이 사용자 요구사항과 의도된 용도를 충족하는지 보장
- 설계 프로세스가 규제 요구사항을 준수하는지 확인
- 설계 변경이 통제되고 문서화되도록 관리

### Regulatory Requirements (규제 요구사항)

- **FDA 21 CFR 820.30**: Design Control (미국)
- **ISO 13485:2016 Section 7.3**: Design and Development (국제)
- **EU MDR Annex IX**: Technical Documentation (유럽)

## DHF (Design History File)

### DHF Purpose

DHF는 설계 프로젝트의 전체 이력을 문서화합니다:

1. **Design Plan**: 설계 계획
2. **Design Input**: 설계 입력 요구사항
3. **Design Output**: 설계 출력 명세서
4. **Design Review**: 설계 검토 기록
5. **Design Verification**: 설계 검증
6. **Design Validation**: 설계 유효성 확인
7. **Design Transfer**: 설계 이관
8. **Design Changes**: 설계 변경 관리

### DHF Template Structure

```
DHF-XXX-XXX: [Device Name] Design History File
├── 1.0 Design Plan
│   ├── 1.1 Project Overview
│   ├── 1.2 Development Schedule
│   ├── 1.3 Team Roles and Responsibilities
│   └── 1.4 Risk Management Integration
├── 2.0 Design Inputs
│   ├── 2.1 User Needs
│   ├── 2.2 Intended Use
│   ├── 2.3 Clinical Benefits
│   ├── 2.4 Regulatory Requirements
│   └── 2.5 Risk Management Inputs
├── 3.0 Design Outputs
│   ├── 3.1 Product Specifications
│   ├── 3.2 Software Requirements (IEC 62304)
│   ├── 3.3 Hardware Specifications
│   ├── 3.4 Labeling and IFU
│   └── 3.5 Packaging Specifications
├── 4.0 Design Reviews
│   ├── 4.1 Concept Review
│   ├── 4.2 Critical Design Review
│   ├── 4.3 Verification Review
│   └── 4.4 Validation Review
├── 5.0 Design Verification
│   ├── 5.1 Test Protocols
│   ├── 5.2 Test Results
│   └── 5.3 Analysis Reports
├── 6.0 Design Validation
│   ├── 6.1 Clinical Evaluation
│   ├── 6.2 Usability Testing (IEC 62366-1)
│   └── 6.3 Validation Summary
├── 7.0 Design Transfer
│   ├── 7.1 DMR Completion
│   ├── 7.2 Process Validation
│   └── 7.3 Production Readiness
└── 8.0 Design Changes
    ├── 8.1 Change Requests
    ├── 8.2 Impact Analysis
    └── 8.3 Change Approvals
```

### Design Input Checklist

| 항목 | 내용 | 출처 |
|------|------|------|
| User Needs | 사용자 요구사항 | Market research, User interviews |
| Intended Use | 의도된 사용 | Clinical definition |
| Clinical Benefits | 임상적 이점 | Literature, Expert opinion |
| Regulatory Requirements | 규제 요구사항 | FDA, ISO, MDR |
| Safety Requirements | 안전 요구사항 | ISO 14971 Risk Analysis |
| Performance Requirements | 성능 요구사항 | Technical specifications |
| Interface Requirements | 인터페이스 요구사항 | System integration |
| Environmental Requirements | 환경 요구사항 | IEC 60601-1 |

### Design Output Checklist

| 항목 | 내용 | 검증 방법 |
|------|------|----------|
| Product Specifications | 제품 명세서 | Testing, Inspection |
| Software Code | 소프트웨어 코드 | Review, Static analysis |
| Hardware Drawings | 하드웨어 도면 | Measurement, Analysis |
| Labeling | 라벨링 | Visual inspection |
| IFU (Instructions for Use) | 사용 설명서 | Usability testing |
| Packaging | 패키징 | Drop test, Seal test |

## DMR (Device Master Record)

### DMR Purpose

DMR은 제품 제조를 위한 완전한 명세서와 절차를 포함합니다:

1. **Production Specifications**: 생산 명세서
2. **Quality Procedures**: 품질 보증 절차
3. **Packaging Specifications**: 패키징 명세서
4. **Labeling Specifications**: 라벨링 명세서
5. **Installation Procedures**: 설치 절차
6. **Servicing Procedures**: 유지보수 절차

### DMR Template Structure

```
DMR-XXX-XXX: [Device Name] Device Master Record
├── 1.0 Production Specifications
│   ├── 1.1 Bill of Materials
│   ├── 1.2 Assembly Drawings
│   ├── 1.3 Component Specifications
│   └── 1.4 Process Specifications
├── 2.0 Quality Procedures
│   ├── 2.1 Acceptance Activities
│   ├── 2.2 In-Process Testing
│   ├── 2.3 Final Product Testing
│   └── 2.4 Quality Assurance Records
├── 3.0 Packaging and Labeling
│   ├── 3.1 Packaging Specifications
│   ├── 3.2 Labeling Specifications
│   └── 3.3 Shelf-Life Requirements
└── 4.0 Installation and Servicing
    ├── 4.1 Installation Procedures
    └── 4.2 Servicing Procedures
```

## DHR (Device History Record)

### DHR Purpose

DHR는 각 생산 배치(Batch/Lot)에 대한 제조 이력을 추적합니다:

1. **Manufacturing Dates**: 제조 날짜
2. **Quantities Produced**: 생산 수량
3. **Acceptance Records**: 검수 기록
4. **Primary Identification Label**: 식별 라벨
5. **Batch/Lot Number**: 배치 번호

### DHR Template Structure

```
DHR-XXX-XXX-LOT-001: [Device Name] Device History Record
├── 1.0 Production Information
│   ├── 1.1 Manufacturing Dates
│   ├── 1.2 Quantities Produced
│   ├── 1.3 Batch/Lot Number
│   └── 1.4 Primary Identification Label
├── 2.0 Component Traceability
│   ├── 2.1 Bill of Materials Used
│   ├── 2.2 Supplier Lot Numbers
│   └── 2.3 Expiration Dates
├── 3.0 Process Records
│   ├── 3.1 In-Process Testing
│   ├── 3.2 Acceptance Activities
│   └── 3.3 Final Product Testing
└── 4.0 Quality Records
    ├── 4.1 Nonconformance Reports
    ├── 4.2 Rework Records
    └── 4.3 Final Release
```

## Traceability Matrix (추적성 매트릭스)

### Purpose

추적성 매트릭스는 요구사항부터 검증까지의 양방향 추적성을 확보합니다:

```
User Needs → Design Inputs → Design Outputs → Verification → Validation
    ↓            ↓              ↓               ↓             ↓
[UN-001]    [DI-001]       [DO-001]        [VT-001]      [VD-001]
```

### Traceability Matrix Template

| Requirement ID | Requirement | Design Output | Verification Method | Test ID | Validation Method | Result |
|----------------|-------------|---------------|---------------------|---------|-------------------|--------|
| DI-001 | Blood glucose accuracy ±5% | Sensor spec | Lab testing | VT-001 | Clinical study | Pass |
| DI-002 | Battery life 7 days | Battery spec | Life cycle test | VT-002 | User validation | Pass |
| DI-003 | Data transmission secure | Wireless spec | Penetration test | VT-003 | Security audit | Pass |

### Traceability Validation Rules

1. **Completeness**: 모든 요구사항이 최소 하나의 출력과 연결
2. **Verification Coverage**: 모든 출력이 검증 방법과 연결
3. **Validation Coverage**: 모든 사용자 요구가 유효성 확인과 연결
4. **Bidirectional**: 양방향 추적 가능 (요구사항 ↔ 테스트 결과)

## Design Control Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    Design Control Process                    │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌───────────────┐
│ 1. Design Plan │ - Project scope, schedule, resources
└───────┬───────┘
        │
        ▼
┌───────────────────┐
│ 2. Design Inputs  │ - User needs, regulatory requirements
└───────┬───────────┘
        │
        ▼
┌────────────────────┐
│ 3. Design Outputs  │ - Specifications, drawings, code
└───────┬────────────┘
        │
        ▼
┌───────────────────┐
│ 4. Design Review  │ - Formal reviews at each stage
└───────┬───────────┘
        │
        ▼
┌─────────────────────┐
│ 5. Design Verification │ - Testing outputs meet inputs
└───────┬──────────────┘
        │
        ▼
┌─────────────────────┐
│ 6. Design Validation  │ - Clinical use confirms needs met
└───────┬──────────────┘
        │
        ▼
┌─────────────────────┐
│ 7. Design Transfer   │ - Production readiness
└───────┬──────────────┘
        │
        ▼
┌─────────────────────┐
│ 8. Ongoing Change     │ - Controlled change process
│      Management       │
└─────────────────────┘
```

## Design Transfer Checklist

### Pre-Production Review

Before production release:

- [ ] **DMR Complete**
  - [ ] Production specifications approved
  - [ ] Quality procedures established
  - [ ] Packaging and labeling approved

- [ ] **Process Validation**
  - [ ] Manufacturing processes validated
  - [ ] Equipment qualified (IQ/OQ/PQ)
  - [ ] Process capability confirmed

- [ ] **Staff Training**
  - [ ] Operators trained on procedures
  - [ ] Quality inspectors trained
  - [ ] Training records documented

- [ ] **Supplier Qualification**
  - [ ] Critical suppliers qualified
  - [ ] Incoming inspection procedures
  - [ ] Supplier agreements in place

- [ ] **DHR Process**
  - [ ] DHR template established
  - [ ] Batch tracking system ready
  - [ ] Label printing system ready

## Design Change Control

### Change Control Process

1. **Change Request**
   - Identify need for change
   - Document change justification
   - Submit change request

2. **Impact Analysis**
   - Assess design impact
   - Assess regulatory impact
   - Assess risk impact (ISO 14971)

3. **Verification & Validation**
   - Verify changed design
   - Validate changed design
   - Update risk analysis

4. **Review & Approval**
   - Design review of change
   - Regulatory review (if needed)
   - Final approval

5. **Documentation**
   - Update DHF
   - Update DMR (if production affected)
   - Update Document Registry

### Change Classification

| Class | Description | Approval Required |
|-------|-------------|-------------------|
| Minor | No impact on safety/efficacy | Design engineer |
| Major | Potential impact on safety/efficacy | Design control committee |
| Critical | Impact on safety/efficacy | Regulatory notification may be required |

## Integration with Other Processes

### Risk Management (ISO 14971)

Design Control integrates with Risk Management:

- Risk analysis inputs to Design Input
- Risk control measures in Design Output
- Risk evaluation in Verification/Validation
- Residual risk assessment in Validation

### Software Development (IEC 62304)

For Software as Medical Device (SaMD):

- Software requirements in Design Input
- Software architecture in Design Output
- Unit testing in Verification
- Integration testing in Verification
- System testing in Validation

### Clinical Evaluation (MDR Annex XV)

For clinical evidence:

- Clinical investigation planning in Design Plan
- Clinical data collection in Validation
- Clinical evaluation report in Design History

## Common Pitfalls

### 1. Incomplete Design Inputs

**Problem**: Missing user needs or regulatory requirements

**Solution**: Use comprehensive input checklist covering:
- User needs
- Intended use
- Clinical benefits
- Regulatory requirements
- Safety requirements
- Performance requirements
- Interface requirements
- Environmental requirements

### 2. Broken Traceability

**Problem**: Orphaned requirements or unlinked tests

**Solution**: Implement automated traceability validation:
- Every requirement linked to output
- Every output linked to verification
- Every verification linked to result
- Bidirectional traceability confirmed

### 3. Insufficient Verification

**Problem**: Testing doesn't cover all outputs

**Solution**: Verify completeness:
- All outputs have test methods
- All acceptance criteria defined
- All test protocols documented
- All test results recorded

### 4. Incomplete Validation

**Problem**: Clinical use not adequately tested

**Solution**: Comprehensive validation:
- Clinical scenario coverage
- Usability testing (IEC 62366-1)
- Clinical evaluation (MDR Annex XV)
- Post-market surveillance plan

## Best Practices

### 1. Early Planning

- Establish DHF structure early
- Define review checkpoints
- Plan verification strategy
- Plan validation studies

### 2. Documentation First

- Document as you go
- Never skip documentation
- Use templates consistently
- Maintain version control

### 3. Continuous Review

- Regular design reviews
- Independent reviewers
- Document all decisions
- Track action items

### 4. Change Control

- All changes documented
- Impact analysis required
- Re-verification when needed
- Regulatory assessment when needed

---

## Modules

자세한 내용은 각 모듈을 참조하세요:

- `modules/dhf.md` - Design History File 상세 가이드
- `modules/dmr.md` - Device Master Record 상세 가이드
- `modules/dhr.md` - Device History Record 상세 가이드
- `modules/traceability.md` - 추적성 매트릭스 상세 가이드

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Reference**: [FDA 21 CFR 820.30] Design Controls
