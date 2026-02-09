# Design Traceability Matrix (설계 추적성 매트릭스)

추적성 매트릭스 상세 가이드.

## Purpose

추적성 매트릭스는 설계 입력부터 검증/유효성 확인까지의 양방향 추적성을 확보합니다.

### Regulatory Requirements

| 규제 | 요구사항 |
|------|----------|
| FDA 21 CFR 820.30 | 각 설계 단계별 추적성 |
| FDA 21 CFR 820.30(d) | 설계 검토에서 추적성 확인 |
| ISO 13485:2016 7.3.9 | 설계 출력 간 추적성 |

## Traceability Chain

```
User Needs → Design Inputs → Design Outputs → Verification → Validation
    ↓            ↓              ↓               ↓             ↓
[UN-001]    [DI-001]       [DO-001]        [VT-001]      [VD-001]
```

## Traceability Matrix Structure

### Forward Traceability (Requirement → Test)

| Requirement ID | Requirement | Design Output | Verification Method | Test ID | Result |
|----------------|-------------|---------------|---------------------|---------|--------|
| DI-001 | Blood glucose accuracy ±5% | Sensor spec | Lab testing | VT-001 | Pass |
| DI-002 | Battery life 7 days | Battery spec | Life cycle test | VT-002 | Pass |
| DI-003 | Data transmission secure | Wireless spec | Penetration test | VT-003 | Pass |

### Backward Traceability (Test → Requirement)

| Test ID | Test | Requirement | Design Output | Result |
|---------|------|-------------|---------------|--------|
| VT-001 | Accuracy test | DI-001 | DO-001 | Pass |
| VT-002 | Battery test | DI-002 | DO-002 | Pass |
| VT-003 | Security test | DI-003 | DO-003 | Pass |

## Traceability Categories

### 1. Requirements Traceability

**Design Inputs → Design Outputs**

| Design Input | Design Output | Link Type |
|--------------|---------------|-----------|
| User need UN-001 | Requirement DI-001 | Derived from |
| Requirement DI-001 | Specification DO-001 | Satisfies |
| Specification DO-001 | Test VT-001 | Verifies |

### 2. Verification Traceability

**Design Outputs → Verification**

| Design Output | Verification Method | Test Protocol | Test Result |
|---------------|---------------------|---------------|-------------|
| DO-001: Sensor accuracy | Lab testing | TP-001 | Pass |
| DO-002: Battery life | Life cycle test | TP-002 | Pass |
| DO-003: Wireless security | Penetration test | TP-003 | Pass |

### 3. Validation Traceability

**User Needs → Validation**

| User Need | Validation Method | Clinical Study | Result |
|-----------|-------------------|----------------|--------|
| UN-001: Accurate glucose | Clinical study | CS-001 | Pass |
| UN-002: Easy to use | Usability test | UT-001 | Pass |
| UN-003: Safe to use | Safety study | SS-001 | Pass |

## Traceability Validation Rules

### Rule 1: Completeness

모든 요구사항이 최소 하나의 출력과 연결되어야 합니다.

**Check**:
```sql
SELECT DI_ID FROM Design_Inputs
WHERE DI_ID NOT IN (SELECT DISTINCT DI_ID FROM Design_Outputs)
```

**Expected**: Empty set

### Rule 2: Verification Coverage

모든 출력이 검증 방법과 연결되어야 합니다.

**Check**:
```sql
SELECT DO_ID FROM Design_Outputs
WHERE DO_ID NOT IN (SELECT DISTINCT DO_ID FROM Verification_Methods)
```

**Expected**: Empty set

### Rule 3: Validation Coverage

모든 사용자 요구가 유효성 확인과 연결되어야 합니다.

**Check**:
```sql
SELECT UN_ID FROM User_Needs
WHERE UN_ID NOT IN (SELECT DISTINCT UN_ID FROM Validation_Methods)
```

**Expected**: Empty set

### Rule 4: Bidirectional Linkage

모든 링크가 양방향으로 작동해야 합니다.

**Check**:
- Forward: Requirement → Output → Test
- Backward: Test → Output → Requirement

**Expected**: All links valid

## Traceability Matrix Template

```markdown
# Design Traceability Matrix: [Device Name]

## Forward Traceability (Requirements → Tests)

| Req ID | Requirement | Output ID | Output | Test ID | Test | Result |
|--------|-------------|-----------|--------|---------|------|--------|
| DI-001 | [Description] | DO-001 | [Desc] | VT-001 | [Test] | Pass |
| DI-002 | [Description] | DO-002 | [Desc] | VT-002 | [Test] | Pass |

## Backward Traceability (Tests → Requirements)

| Test ID | Test | Output ID | Output | Req ID | Requirement | Result |
|---------|------|-----------|--------|--------|-------------|--------|
| VT-001 | [Test] | DO-001 | [Desc] | DI-001 | [Description] | Pass |

## Validation Traceability

| User Need | Validation | Clinical Study | Result |
|-----------|------------|----------------|--------|
| UN-001 | [Method] | CS-001 | Pass |

## Summary Statistics
- Total Requirements: [N]
- Requirements with Outputs: [N] ([%] coverage)
- Outputs with Verification: [N] ([%] coverage)
- User Needs with Validation: [N] ([%] coverage)
- Overall Traceability: [%]
```

## Automated Traceability Validation

### Validation Script

```python
def validate_traceability(traceability_matrix):
    """
    Validate traceability matrix completeness
    """
    # Rule 1: All requirements have outputs
    req_without_outputs = find_orphaned_requirements()
    if req_without_outputs:
        raise ValueError(f"Requirements without outputs: {req_without_outputs}")

    # Rule 2: All outputs have verification
    output_without_verification = find_unverified_outputs()
    if output_without_verification:
        raise ValueError(f"Outputs without verification: {output_without_verification}")

    # Rule 3: All user needs have validation
    need_without_validation = find_unvalidated_needs()
    if need_without_validation:
        raise ValueError(f"User needs without validation: {need_without_validation}")

    # Rule 4: Bidirectional links
    broken_links = find_broken_links()
    if broken_links:
        raise ValueError(f"Broken links: {broken_links}")

    return True
```

## Traceability Best Practices

### 1. Early Establishment

- 설계 초기부터 추적성 매트릭스 작성
- 요구사항 정의와 동시에 링크 생성
- 지속적인 유지보수

### 2. Tool Support

- 자동화된 추적성 관리 도구 사용
- 실시간 검증
- 경고 알림

### 3. Regular Review

- 정기적인 추적성 검토
- 설계 검토 시 확인
- 변경 시 업데이트

### 4. Documentation

- 추적성 매트릭스 문서화
- 링크 근거 유지
- 변경 추적

## Common Traceability Issues

### Issue 1: Orphaned Requirements

**Problem**: 요구사항이 출력에 연결되지 않음

**Solution**:
- 모든 요구사항에 출력 할당
- 불필요한 요구사항 제거
- 명확한 연결 정의

### Issue 2: Unverified Outputs

**Problem**: 출력이 검증되지 않음

**Solution**:
- 모든 출력에 검증 방법 정의
- 검증 프로토콜 작성
- 검증 실행 및 문서화

### Issue 3: Unvalidated Needs

**Problem**: 사용자 요구가 유효성 확인되지 않음

**Solution**:
- 모든 사용자 요구에 유효성 확인 방법 정의
- 임상 평가 계획 수립
- 사용자 테스트 수행

### Issue 4: Broken Links

**Problem**: 링크가 단방향 또는 깨짐

**Solution**:
- 양방향 링크 확인
- 자동화된 검증 도구 사용
- 정기적인 링크 점검

## References

- FDA 21 CFR 820.30 - Design Controls
- ISO 13485:2016 Section 7.3 - Design and Development
