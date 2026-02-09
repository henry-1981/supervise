# DHR (Device History Record)

Device History Record 상세 가이드.

## DHR Purpose

DHR는 각 생산 배치(Batch/Lot)에 대한 제조 이력을 문서화합니다.

### Regulatory Requirements

| 규제 | 요구사항 |
|------|----------|
| FDA 21 CFR 820.184 | DHR에 포함될 내용 및 준비/유지 |

## DHR Structure

### 1. Production Information

#### Purpose
제조 기본 정보를 문서화합니다.

#### Contents

**1.1 Manufacturing Dates**
- Production start date
- Production completion date
- Shift information
- Operator information

**1.2 Quantities Produced**
- Batch/Lot size
- Good quantity
- Reject quantity
- Rework quantity

**1.3 Batch/Lot Number**
- Unique identifier
- Expiration date
- Manufacturing location

**1.4 Primary Identification Label**
- Device identification
- Batch/Lot number
- Expiration date
- Manufacturing date

### 2. Component Traceability

#### Purpose
사용된 모든 구성요소를 추적합니다.

#### Contents

**2.1 Bill of Materials Used**
- Actual components used
- Lot numbers of components
- Supplier information
- Expiration dates

**2.2 Supplier Lot Numbers**
- Traceability to supplier
- Component certificates
- Material certifications

**2.3 Expiration Dates**
- Component expiration
- Device expiration calculation
- Shelf-life validation

### 3. Process Records

#### Purpose
제조 공정 기록을 유지합니다.

#### Contents

**3.1 In-Process Testing**
- Test results
- Inspections performed
- Measurements recorded
- Pass/Fail determination

**3.2 Acceptance Activities**
- Final testing results
- Quality checks
- Release authorization
- Nonconformance reports

**3.3 Final Product Testing**
- Functional tests
- Performance tests
- Safety tests
- Reliability tests

### 4. Quality Records

#### Purpose
품질 관련 기록을 유지합니다.

#### Contents

**4.1 Nonconformance Reports**
- Defect identification
- Root cause analysis
- Disposition decisions
- Corrective actions

**4.2 Rework Records**
- Rework performed
- Rework verification
- Rework acceptance

**4.3 Final Release**
- Release authorization
- Release date
- Released by
- Quantity released

## DHR Template

```markdown
# DHR-[DEVICE-ID]-LOT-[LOT-NUMBER]: [Device Name] Device History Record

## 1.0 Production Information
### 1.1 Manufacturing Dates
- Production Start: YYYY-MM-DD HH:MM
- Production Complete: YYYY-MM-DD HH:MM
- Shift: [Morning/Afternoon/Night]
- Operator: [Name]

### 1.2 Quantities Produced
- Batch Size: [Quantity]
- Good Quantity: [Quantity]
- Reject Quantity: [Quantity]
- Rework Quantity: [Quantity]

### 1.3 Batch/Lot Information
- Lot Number: [LOT-XXX]
- Expiration Date: YYYY-MM-DD
- Manufacturing Location: [Facility]

### 1.4 Primary Identification
- Device Name: [Name]
- Model Number: [Model]
- Serial Number Range: [Start - End]
- Manufacturing Date: YYYY-MM-DD

## 2.0 Component Traceability
### 2.1 Bill of Materials Used
| Component | Part Number | Lot Number | Quantity | Expiration |
|-----------|-------------|------------|----------|------------|
| [Name] | [PN-XXX] | [LOT-XXX] | [Qty] | YYYY-MM-DD |

### 2.2 Supplier Certifications
- Certificate [C-001]: Material Certification
- Certificate [C-002]: Component Testing

## 3.0 Process Records
### 3.1 In-Process Testing
| Test ID | Test | Result | Operator | Time |
|---------|------|--------|----------|------|
| [IP-001] | [Test] | [Pass/Fail] | [Name] | HH:MM |

### 3.2 Acceptance Activities
- Acceptance [AC-001]: Visual Inspection - Pass
- Acceptance [AC-002]: Functional Test - Pass

### 3.3 Final Product Testing
| Test | Specification | Result | Pass/Fail |
|------|---------------|--------|-----------|
| [Test] | [Spec] | [Measured] | Pass |

## 4.0 Quality Records
### 4.1 Nonconformance
- NCR [NCR-XXX]: [Description] - [Disposition]

### 4.2 Rework
- Rework [RW-XXX]: [Description] - Verified

### 4.3 Final Release
- Release Authorization: [Name]
- Release Date: YYYY-MM-DD
- Quantity Released: [Quantity]
- Storage Location: [Location]
```

## DHR Requirements

### Traceability

DHR는 다음 추적성을 제공해야 합니다:

1. **Forward Traceability**
   - DHR → DMR
   - DHR → Customer
   - DHR → Field

2. **Backward Traceability**
   - DHR → Supplier lots
   - DHR → Manufacturing date
   - DHR → Operators

### Completeness

DHR는 다음을 포함해야 합니다:

1. **Production Information**
   - Manufacturing dates
   - Quantities produced
   - Batch/Lot numbers

2. **Component Traceability**
   - Components used
   - Supplier lot numbers
   - Expiration dates

3. **Process Records**
   - In-process testing
   - Acceptance activities
   - Final testing

4. **Quality Records**
   - Nonconformance
   - Rework
   - Final release

## DHR Best Practices

### Real-Time Documentation

1. **Document as you go**
   - 생산 중 기록
   - 즉시 검증
   - 지체 방지

2. **Electronic Records**
   - 자동화된 수집
   - 실시간 검증
   - 오류 감소

3. **Batch Tracking**
   - 고유 식별
   - 시간 소인
   - 연산자 기록

### Quality Integration

1. **Testing Integration**
   - 자동 데이터 수집
   - 즉시 판정
   - 추세 분석

2. **Nonconformance Management**
   - 즉시 보고
   - 신속한 처분
   - 근본 원인 분석

3. **Release Control**
   - 자동 승인 기준
   - 다단계 승인
   - 감사 추적

## References

- FDA 21 CFR 820.184 - Device History Record
- ISO 13485:2016 Section 7.5.8 - Traceability
