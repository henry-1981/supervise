# SPEC-ARIA-007: 인수 조건 (Acceptance Criteria)

**TAG:** SPEC-ARIA-007
**Phase:** Acceptance
**Status:** Ready for Validation

---

## 1. 개요 (Overview)

본 문서는 SPEC-ARIA-007의 인수 조건을 정의합니다. 태깅 형식 통일 작업이 완료되기 위한 검증 기준과 테스트 시나리오를 제공합니다.

---

## 2. 품질 게이트 (Quality Gates)

### 2.1 필수 조건 (Mandatory Criteria)

모든 작업이 완료되기 위해 **반드시** 충족해야 하는 조건입니다:

- [QG-1] 모든 대상 SPEC 문서의 태그가 변환되어야 한다
- [QG-2] 변환 후 요구사항 총수가 변환 전과 동일해야 한다 (0% 손실)
- [QG-3] 모든 태그가 도메인별 접두사 형식을 준수해야 한다
- [QG-4] 모든 태그가 대괄호 `[]`로 감싸져야 한다
- [QG-5] 각 도메인 내에서 태그 번호가 순차적이어야 한다

### 2.2 EARS 형식 준수 (EARS Compliance)

- [QG-6] Ubiquitous Requirements: "시스템은 항상 ~ 해야 한다" 형식
- [QG-7] Event-Driven Requirements: "WHEN ~ THEN/S **SHALL**" 형식
- [QG-8] State-Driven Requirements: "IF ~ THEN/S **SHALL**" 형식
- [QG-9] Unwanted Requirements: "~ 하면 안 된다" 형식
- [QG-10] Optional Requirements: "가능하면 ~ 제공해야 한다" 형식

### 2.3 참조 무결성 (Reference Integrity)

- [QG-11] spec.md 내의 모든 태그 참조가 유효해야 한다
- [QG-12] plan.md 내의 모든 태그 참조가 유효해야 한다
- [QG-13] acceptance.md 내의 모든 태그 참조가 유휘해야 한다

---

## 3. 테스트 시나리오 (Test Scenarios)

### 3.1 Given-When-Then 형식

#### Scenario 1: SPEC-002 태그 변환

**Given:** SPEC-002에 `REQ-001` ~ `REQ-073` 태그가 존재

**When:** 태그 변환이 수행되면

**Then:**
- And 모든 `REQ-###` 태그가 도메인별 태그로 변환되어야 한다
- And 각 요구사항이 올바른 도메인으로 분류되어야 한다
- And 태그 번호가 각 도메인 내에서 순차적이어야 한다
- And 요구사항 총수가 73개로 유지되어야 한다

**Examples:**

| 기존 태그 | 요구사항 내용 (요약) | 새로운 태그 | 도메인 |
|----------|---------------------|------------|--------|
| REQ-001 | 시스템은 항상 VALID 준수 | [UR-001] | Ubiquitous |
| REQ-004 | WHEN /aria brief 실행 | [ER-001] | Event-Driven |
| REQ-008 | IF read-only 작업 | [SR-001] | State-Driven |
| REQ-013 | 시스템은 절대 직접 구현 금지 | [WR-001] | Unwanted |
| REQ-011 | 가능하면 Context7 자동 조회 | [OR-001] | Optional |

#### Scenario 2: SPEC-003 prose → EARS 변환

**Given:** SPEC-003에 WHEN/IF/WHERE prose 요구사항이 존재

**When:** EARS 형식 변환이 수행되면

**Then:**
- And 모든 WHEN 요구사항이 `[ER-###]` 태그를 가져야 한다
- And 모든 IF 요구사항이 `[SR-###]` 태그를 가져야 한다
- And 모든 WHERE 요구사항이 `[OR-###]` 태그를 가져야 한다
- And "**SHALL**" 강조가 올바르게 적용되어야 한다
- And 요구사항 내용이 변경되지 않아야 한다

**Examples:**

| 기존 형식 | 새로운 형식 |
|----------|-------------|
| WHEN 사용자가 규제 전략을 요청하면, THE 시스템은 SHALL 적용 시장별 요구사항을 분석한다 | **[ER-001]** WHEN 사용자가 규제 전략을 요청하면, 시스템은 **SHALL** 적용 시장별 요구사항을 분석한다 |
| IF 제품이 Class III이면, THE 시스템은 SHALL PMA 경로를 제안한다 | **[SR-001]** IF 제품이 Class III이면, 시스템은 **SHALL** PMA 경로를 제안한다 |

#### Scenario 3: SPEC-004 prose → EARS 변환

**Given:** SPEC-004에 WHEN/IF prose 요구사항이 존재

**When:** EARS 형식 변환이 수행되면

**Then:**
- And 모든 WHEN 요구사항이 `[ER-###]` 태그를 가져야 한다
- And 모든 IF 요구사항이 `[SR-###]` 태그를 가져야 한다
- And EARS 형식이 올바르게 적용되어야 한다

**Examples:**

| 기존 형식 | 새로운 형식 |
|----------|-------------|
| WHEN ARIA가 초기화되면, THE 시스템은 SHALL Notion DB 스키마를 자동 생성한다 | **[ER-001]** WHEN ARIA가 초기화되면, 시스템은 **SHALL** Notion DB 스키마를 자동 생성한다 |

#### Scenario 4: SPEC-005 계층 태그 변환

**Given:** SPEC-005에 `[REQ-1.1.1]` 계층 형식 태그가 존재

**When:** 태그 변환이 수행되면

**Then:**
- And 모든 `[REQ-x.y.z]` 태그가 도메인별 태그로 변환되어야 한다
- And 계층 구조가 평탄화되어야 한다
- And 태그 번호가 순차적이어야 한다

**Examples:**

| 기존 태그 | 새로운 태그 (예시) |
|----------|-------------------|
| [REQ-1.1.1] | [UR-001] 또는 [ER-001] (내용에 따라) |
| [REQ-1.2.1] | [UR-002] 또는 [ER-002] (내용에 따라) |

### 3.2 검증 시나리오 (Verification Scenarios)

#### Scenario 5: 요구사항 누락 방지

**Given:** 변환이 완료된 SPEC 문서

**When:** 요구사항 총수를 비교하면

**Then:**
- And 변환 전 요구사항 총수와 변환 후 요구사항 총수가 동일해야 한다
- And 각 도메인별 태그 수 합계가 총 요구사항 수와 일치해야 한다

**Validation Script:**

```python
def verify_requirement_count(original_spec, converted_spec):
    """요구사항 총수 비교 검증"""
    original_count = count_requirements(original_spec)
    converted_count = count_requirements(converted_spec)

    assert original_count == converted_count, \
        f'요구사항 수 불일치: 원본={original_count}, 변환={converted_count}'

    return True
```

#### Scenario 6: 태그 형식 준수 검증

**Given:** 변환된 SPEC 문서

**When:** 모든 태그를 검증하면

**Then:**
- And 모든 태그가 `[XX-###]` 형식을 준수해야 한다
- And XX는 UR, ER, SR, WR, OR 중 하나여야 한다
- And ###는 3자리 숫자여야 한다

**Validation Script:**

```python
import re

def verify_tag_format(spec_content):
    """태그 형식 준수 검증"""
    tag_pattern = r'\[(UR|ER|SR|WR|OR)-\d{3}\]'
    tags = re.findall(tag_pattern, spec_content)

    assert len(tags) > 0, '태그가 발견되지 않음'

    for tag in tags:
        assert re.match(tag_pattern, tag), f'잘못된 태그 형식: {tag}'

    return True
```

#### Scenario 7: 참조 무결성 검증

**Given:** 변환된 SPEC 문서 (spec.md, plan.md, acceptance.md)

**When:** 모든 태그 참조를 검증하면

**Then:**
- And spec.md의 모든 태그가 유효해야 한다
- And plan.md의 모든 태그 참조가 spec.md의 태그와 일치해야 한다
- And acceptance.md의 모든 태그 참조가 spec.md의 태그와 일치해야 한다

**Validation Script:**

```python
def verify_reference_integrity(spec_md, plan_md, acceptance_md):
    """참조 무결성 검증"""
    # spec.md에서 모든 태그 추출
    spec_tags = extract_tags(spec_md)

    # plan.md에서 모든 태그 참조 추출
    plan_refs = extract_tag_references(plan_md)

    # acceptance.md에서 모든 태그 참조 추출
    acceptance_refs = extract_tag_references(acceptance_md)

    # 모든 참조가 spec.md의 태그와 일치하는지 검증
    for ref in plan_refs + acceptance_refs:
        assert ref in spec_tags, f'유효하지 않은 참조: {ref}'

    return True
```

---

## 4. Definition of Done (완료 정의)

### 4.1 필수 완료 조건

다음 조건이 **모두** 충족되어야 작업이 완료된 것으로 간주됩니다:

1. **변환 완료:**
   - [ ] SPEC-002의 모든 태그가 변환됨
   - [ ] SPEC-003의 모든 prose 요구사항이 EARS + 태그로 변환됨
   - [ ] SPEC-004의 모든 prose 요구사항이 EARS + 태그로 변환됨
   - [ ] SPEC-005의 모든 태그가 변환됨

2. **정합성 검증:**
   - [ ] 요구사항 총수가 변환 전과 동일함 (0% 손실)
   - [ ] 모든 태그가 표준 형식을 준수함
   - [ ] 태그 번호가 순차적임

3. **품질 검증:**
   - [ ] EARS 형식이 올바르게 적용됨
   - [ ] 도메인 분류가 정확함
   - [ ] 참조 무결성이 보장됨

4. **문서화:**
   - [ ] 변환 보고서가 작성됨
   - [ ] 태그 매핑 테이블이 작성됨
   - [ ] CHANGELOG.md가 업데이트됨

### 4.2 자동화 검증 (Automated Validation)

**실행 가능한 검증 스크립트:**

```python
#!/usr/bin/env python3
"""SPEC-ARIA-007 변환 검증 스크립트"""

import re
from pathlib import Path

def count_requirements(content):
    """요구사항 수 계산"""
    # 태그 패턴: [XX-###]
    tag_pattern = r'\[(UR|ER|SR|WR|OR)-\d{3}\]'
    tags = re.findall(tag_pattern, content)
    return len(tags)

def verify_tag_format(content):
    """태그 형식 검증"""
    tag_pattern = r'\[(UR|ER|SR|WR|OR)-\d{3}\]'
    tags = re.findall(tag_pattern, content)

    for tag in tags:
        if not re.match(r'^\[UR|ER|SR|WR|OR-\d{3}\]$', tag):
            print(f'ERROR: 잘못된 태그 형식: {tag}')
            return False

    print(f'PASS: {len(tags)}개 태그가 올바른 형식')
    return True

def extract_tags(content):
    """모든 태그 추출"""
    tag_pattern = r'\[(UR|ER|SR|WR|OR)-\d{3}\]'
    return set(re.findall(tag_pattern, content))

def extract_tag_references(content):
    """태그 참조 추출 (텍스트에서 언급된 태그)"""
    tag_pattern = r'\[(UR|ER|SR|WR|OR)-\d{3}\]'
    return set(re.findall(tag_pattern, content))

def verify_reference_integrity(spec_md, plan_md, acceptance_md):
    """참조 무결성 검증"""
    spec_tags = extract_tags(spec_md)
    plan_refs = extract_tag_references(plan_md)
    acceptance_refs = extract_tag_references(acceptance_md)

    all_refs = plan_refs | acceptance_refs
    invalid_refs = all_refs - spec_tags

    if invalid_refs:
        print(f'ERROR: 유효하지 않은 참조: {invalid_refs}')
        return False

    print(f'PASS: {len(all_refs)}개 참조가 모두 유효')
    return True

def main():
    """메인 검증 실행"""
    spec_files = {
        'SPEC-002': '.moai/specs/SPEC-ARIA-002/spec.md',
        'SPEC-003': '.moai/specs/SPEC-ARIA-003/spec.md',
        'SPEC-004': '.moai/specs/SPEC-ARIA-004/spec.md',
        'SPEC-005': '.moai/specs/SPEC-ARIA-005/spec.md'
    }

    print('=== SPEC-ARIA-007 변환 검증 ===\n')

    all_passed = True

    for spec_name, spec_path in spec_files.items():
        print(f'검증 중: {spec_name}')

        if not Path(spec_path).exists():
            print(f'  SKIP: 파일 없음 ({spec_path})')
            continue

        content = Path(spec_path).read_text()

        # 태그 형식 검증
        if not verify_tag_format(content):
            all_passed = False

        # 요구사항 수 보고
        count = count_requirements(content)
        print(f'  INFO: 요구사항 수 = {count}\n')

    print('=== 검증 완료 ===')
    if all_passed:
        print('RESULT: PASS')
    else:
        print('RESULT: FAIL')

if __name__ == '__main__':
    main()
```

---

## 5. 검증 보고서 (Validation Report)

### 5.1 보고서 구조

변환 완료 후 다음 내용을 포함하는 검증 보고서를 작성해야 합니다:

```markdown
# SPEC-ARIA-007 변환 검증 보고서

## 1. 변환 요약

- 대상 SPEC: SPEC-002, SPEC-003, SPEC-004, SPEC-005
- 변환 전 요구사항 총수: ###개
- 변환 후 요구사항 총수: ###개
- 변환 성공륨: 100%

## 2. 도메인별 분포

| 도메인 | 태그 수 | 비율 |
|--------|--------|------|
| Ubiquitous (UR) | ## | ##% |
| Event-Driven (ER) | ## | ##% |
| State-Driven (SR) | ## | ##% |
| Unwanted (WR) | ## | ##% |
| Optional (OR) | ## | ##% |
| 합계 | ### | 100% |

## 3. 품질 게이트 검증 결과

- [QG-1] 모든 태그 변환 완료: PASS/FAIL
- [QG-2] 요구사항 수 보존: PASS/FAIL
- [QG-3] 태그 형식 준수: PASS/FAIL
- [QG-4] 대괄호 사용: PASS/FAIL
- [QG-5] 순차적 번호: PASS/FAIL
- [QG-6~10] EARS 형식 준수: PASS/FAIL
- [QG-11~13] 참조 무결성: PASS/FAIL

## 4. 발견된 문제 및 해결

(문제가 없으면 "없음"으로 표시)

## 5. 결론

(변환이 성공적으로 완료되었는지 확인)
```

### 5.2 검증 실행 절차

1. **변환 전 상태 저장:**
   - 각 SPEC 문서의 요구사항 총수 기록
   - 기존 태그 목록 저장

2. **변환 실행:**
   - 태그 변환 수행
   - EARS 형식 적용

3. **변환 후 검증:**
   - 요구사항 총수 비교
   - 태그 형식 검증
   - 참조 무결성 검증

4. **검증 보고서 작성:**
   - 검증 결과 기록
   - 문제 및 해결 사항 기록

---

**TAG BLOCK END**

**다음 단계:**
1. 변환 작업 시작
2. 검증 스크립트 실행
3. 검증 보고서 작성
