# DMR (Device Master Record)

Device Master Record 상세 가이드.

## DMR Purpose

DMR은 의료기기 제조를 위한 완전한 명세서와 절차를 포함하는 공식 문서 집합입니다.

### Regulatory Requirements

| 규제 | 요구사항 |
|------|----------|
| FDA 21 CFR 820.181 | DMR에 포함될 내용 및 준비/유지 |

## DMR Structure

### 1. Production Specifications

#### Purpose
제품 제조를 위한 명세서를 정의합니다.

#### Contents

**1.1 Bill of Materials (BOM)**
- Component list
- Part numbers
- Quantities
- Suppliers
- Material specifications

**1.2 Assembly Drawings**
- Assembly instructions
- Assembly sequence
- Tools required
- Quality checks

**1.3 Component Specifications**
- Material specifications
- Tolerance requirements
- Approval status
- Supplier qualifications

**1.4 Process Specifications**
- Manufacturing processes
- Process parameters
- Equipment requirements
- Environmental conditions

### 2. Quality Procedures

#### Purpose
품질 보증 절차를 정의합니다.

#### Contents

**2.1 Acceptance Activities**
- Incoming inspection procedures
- In-process testing
- Final product testing
- Acceptance criteria

**2.2 In-Process Testing**
- Test points
- Test methods
- Test equipment
- Acceptance limits

**2.3 Final Product Testing**
- Functional testing
- Performance testing
- Safety testing
- Reliability testing

**2.4 Quality Assurance Records**
- Test records
- Inspection records
- Calibration records
- Nonconformance records

### 3. Packaging and Labeling

#### Purpose
패키징과 라벨링 명세서를 정의합니다.

#### Contents

**3.1 Packaging Specifications**
- Primary packaging materials
- Secondary packaging materials
- Packaging process
- Packaging validation

**3.2 Labeling Specifications**
- Device labels
- Usage labels
- Warning labels
- Symbol labels

**3.3 Shelf-Life Requirements**
- Expiration dating
- Storage conditions
- Stability data
- Aging studies

### 4. Installation and Servicing

#### Purpose
설치 및 유지보수 절차를 정의합니다.

#### Contents

**4.1 Installation Procedures**
- Site requirements
- Installation steps
- Verification tests
- User training

**4.2 Servicing Procedures**
- Preventive maintenance
- Corrective maintenance
- Calibration procedures
- Replacement parts

## DMR Template

```markdown
# DMR-[DEVICE-ID]-[REVISION]: [Device Name] Device Master Record

## 1.0 Production Specifications
### 1.1 Bill of Materials
| Item | Part Number | Description | Quantity | Supplier |
|------|-------------|-------------|----------|----------|
| 1 | [PN-001] | [Description] | [Qty] | [Supplier] |

### 1.2 Assembly Drawings
- Drawing [DWG-001]: Assembly View
- Drawing [DWG-002]: Component Layout
- Drawing [DWG-003]: Wiring Diagram

### 1.3 Process Specifications
| Process ID | Process | Parameters | Equipment |
|------------|---------|------------|-----------|
| PR-001 | [Name] | [Settings] | [Equipment] |

## 2.0 Quality Procedures
### 2.1 Acceptance Activities
| Step | Activity | Method | Criteria |
|------|----------|--------|----------|
| 1 | [Activity] | [Method] | [Accept/Reject] |

### 2.2 Test Procedures
- Test [TP-001]: Functional Test
- Test [TP-002]: Performance Test
- Test [TP-003]: Safety Test

## 3.0 Packaging and Labeling
### 3.1 Packaging
- Primary: [Material]
- Secondary: [Material]
- Sterilization: [Method]

### 3.2 Labeling
- Label [LBL-001]: Device Label
- Label [LBL-002]: Usage Label
- Label [LBL-003]: Warning Label

## 4.0 Installation and Servicing
### 4.1 Installation
- Procedure [INST-001]: Site Preparation
- Procedure [INST-002]: Device Installation

### 4.2 Servicing
- Procedure [SVC-001]: Preventive Maintenance
- Procedure [SVC-002]: Calibration
```

## DMR Requirements

### Completeness

DMR은 다음을 포함해야 합니다:

1. **Production Specifications**
   - Bill of Materials
   - Assembly drawings
   - Component specifications
   - Process specifications

2. **Quality Procedures**
   - Acceptance activities
   - Testing procedures
   - Quality assurance records

3. **Packaging and Labeling**
   - Packaging specifications
   - Labeling specifications
   - Shelf-life requirements

4. **Installation and Servicing**
   - Installation procedures
   - Servicing procedures

### Control

DMR 변경은 다음을 통해 통제됩니다:

1. **Change Request**
   - 변경 이유
   - 영향 평가
   - 승인

2. **Revision Control**
   - 버전 번호
   - 변경 일자
   - 변경 사유

3. **Distribution Control**
   - 승인된 사본만 사용
   - 구 버전 회수
   - 변경 통지

## DMR Best Practices

### Documentation

1. **Complete Specifications**
   - 모든 구성요소 명세
   - 공차 명시
   - 재료 사양

2. **Clear Procedures**
   - 단계별 절차
   - 검증 지점
   - 승인 기준

3. **Version Control**
   - 모든 변경 추적
   - 개정 이력 유지
   - 변경 사유 문서화

### Quality Integration

1. **Quality Points**
   - 주요 공정마다 검증
   - 승인 기준 정의
   - 불일치 보고

2. **Testing**
   - 기능 테스트
   - 성능 테스트
   - 안전 테스트

3. **Records**
   - 모든 품질 기록 유지
   - 추적성 확보
   - 보관 기간 준수

## References

- FDA 21 CFR 820.181 - Device Master Record
- ISO 13485:2016 Section 7.5.1 - Production and Service Provision
