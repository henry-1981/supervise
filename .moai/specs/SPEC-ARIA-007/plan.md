# SPEC-ARIA-007: 구현 계획 (Implementation Plan)

**TAG:** SPEC-ARIA-007
**Phase:** Plan
**Status:** Ready for Execution

---

## 1. 개요 (Overview)

본 계획은 SPEC-ARIA-002, SPEC-ARIA-003, SPEC-ARIA-004, SPEC-ARIA-005의 태깅 형식을 SPEC-ARIA-001의 도메인별 접두사 형식으로 통일하는 작업을 정의합니다.

**주요 목표:**
- 4개 SPEC 문서, 약 163개 요구사항 태그 변환
- EARS 형식 표준 준수
- 요구사항 내용 유지 (형식만 변경)
- 참조 무결성 보장

---

## 2. 마일스톤 (Milestones)

### Phase 1: 분석 (Analysis)

**목표:** 대상 SPEC 문서 분석 및 태그 인벤토리 작성

**작업 항목:**
- [ ] SPEC-002의 모든 REQ-### 태그 추출 및 분류
- [ ] SPEC-003의 모든 prose 요구사항 추출 및 분류
- [ ] SPEC-004의 모든 prose 요구사항 추출 및 분류
- [ ] SPEC-005의 모든 [REQ-x.y.z] 태그 추출 및 분류
- [ ] 태그 매핑 테이블 작성

**산출물:**
- `tag-inventory.csv`: 기존 태그 목록
- `tag-mapping.csv`: 새로운 태그 매핑 테이블

**성공 기준:**
- 모든 요구사항이 분류됨
- 각 요구사항의 도메인이 결정됨

### Phase 2: 변환 (Transformation)

**목표:** 태그 형식 변환 및 EARS 형식 적용

**작업 항목:**
- [ ] SPEC-002: REQ-### → 도메인별 태그 변환
- [ ] SPEC-003: prose → EARS + 도메인별 태그 변환
- [ ] SPEC-004: prose → EARS + 도메인별 태그 변환
- [ ] SPEC-005: [REQ-x.y.z] → 도메인별 태그 변환
- [ ] spec.md 파일 업데이트
- [ ] plan.md 파일 내 태그 참조 업데이트
- [ ] acceptance.md 파일 내 태그 참조 업데이트

**산출물:**
- 변환된 SPEC 문서 (spec.md, plan.md, acceptance.md)

**성공 기준:**
- 모든 태그가 새로운 형식으로 변환됨
- EARS 형식이 올바르게 적용됨

### Phase 3: 검증 (Verification)

**목표:** 변환 정합성 및 품질 검증

**작업 항목:**
- [ ] 변환 전/후 요구사항 총수 비교
- [ ] 태그 번호 연속성 검증
- [ ] 도메인별 분류 정확성 검증
- [ ] 참조 무결성 검증 (태그 참조가 유효한지)
- [ ] EARS 형식 준수 여부 검증

**산출물:**
- `verification-report.md`: 검증 보고서

**성공 기준:**
- 요구사항 누락 없음 (0% 손실)
- 모든 태그가 표준 형식을 준수함
- 모든 참조가 유효함

### Phase 4: 문서화 (Documentation)

**목표:** 변환 결과 보고서 작성

**작업 항목:**
- [ ] 변환前后 비교 보고서 작성
- [ ] 태그 매핑 테이블 최종화
- [ ] CHANGELOG.md 업데이트

**산출물:**
- `conversion-report.md`: 변환 보고서
- `CHANGELOG.md`: 변경 이력 업데이트

**성공 기준:**
- 모든 변환이 문서화됨
- 변경 이력이 기록됨

---

## 3. 기술 접근 (Technical Approach)

### 3.1 변환 전략

**자동화 + 수동 검토:**
1. **자동화:** 태그 추출, 분류, 매핑 자동화 스크립트 활용
2. **수동 검토:** 변환 결과 수동 검토 및 수정

### 3.2 도구 및 스크립트

**Python 스크립트 (선택적 구현):**

```python
# tag_converter.py
import re
from pathlib import Path

# 도메인별 태그 접두사
DOMAIN_PREFIXES = {
    'ubiquitous': 'UR',
    'event_driven': 'ER',
    'state_driven': 'SR',
    'unwanted': 'WR',
    'optional': 'OR'
}

def classify_requirement(text):
    """요구사항 텍스트를 분석하여 도메인 분류"""
    text_upper = text.upper()

    # Ubiquitous: "시스템은 항상", "항상"
    if '항상' in text_upper or 'ALWAYS' in text_upper:
        return 'ubiquitous'

    # Unwanted: "절대", "안 된다", "SHALL NOT"
    if '절대' in text_upper or 'SHALL NOT' in text_upper or '하지 않아야 한다' in text:
        return 'unwanted'

    # Optional: "가능하면", "제공해야 한다"
    if '가능하면' in text or '가능한 한' in text:
        return 'optional'

    # Event-Driven: "WHEN", "사용자가"
    if text.strip().startswith('WHEN') or '사용자가' in text:
        return 'event_driven'

    # State-Driven: "IF", "조건"
    if text.strip().startswith('IF') or 'IF' in text_upper:
        return 'state_driven'

    # 기본값: Event-Driven (가장 일반적)
    return 'event_driven'

def convert_tag(old_tag, requirement_text, domain_counters):
    """기존 태그를 새로운 도메인별 태그로 변환"""
    domain = classify_requirement(requirement_text)
    prefix = DOMAIN_PREFIXES[domain]
    number = domain_counters[domain] + 1
    domain_counters[domain] = number
    return f'[{prefix}-{number:03d}]'

def process_spec_file(file_path):
    """SPEC 파일 처리"""
    content = Path(file_path).read_text()
    lines = content.split('\n')

    domain_counters = {
        'ubiquitous': 0,
        'event_driven': 0,
        'state_driven': 0,
        'unwanted': 0,
        'optional': 0
    }

    converted_lines = []
    tag_mapping = {}

    for line in lines:
        # 기존 태그 패턴 감지
        old_tag_match = re.match(r'^(\[?REQ-[\d.]+\]?)', line)
        if old_tag_match:
            old_tag = old_tag_match.group(1)
            new_tag = convert_tag(old_tag, line, domain_counters)
            converted_line = line.replace(old_tag, new_tag, 1)
            converted_lines.append(converted_line)
            tag_mapping[old_tag] = new_tag
        else:
            converted_lines.append(line)

    return '\n'.join(converted_lines), tag_mapping

# 메인 실행
if __name__ == '__main__':
    spec_files = [
        '.moai/specs/SPEC-ARIA-002/spec.md',
        '.moai/specs/SPEC-ARIA-003/spec.md',
        '.moai/specs/SPEC-ARIA-004/spec.md',
        '.moai/specs/SPEC-ARIA-005/spec.md'
    ]

    for spec_file in spec_files:
        print(f'Processing {spec_file}...')
        converted_content, mapping = process_spec_file(spec_file)

        # 변환된 내용 저장
        output_path = spec_file.replace('.md', '_converted.md')
        Path(output_path).write_text(converted_content)

        # 매핑 저장
        mapping_path = spec_file.replace('.md', '_mapping.csv')
        with open(mapping_path, 'w') as f:
            f.write('Old Tag,New Tag\n')
            for old, new in mapping.items():
                f.write(f'{old},{new}\n')

        print(f'  Converted: {len(mapping)} tags')
        print(f'  Output: {output_path}')
```

### 3.3 수동 검토 체크리스트

**변환 후 검토 항목:**
- [ ] 모든 요구사항이 올바른 도메인으로 분류되었는가?
- [ ] 태그 번호가 연속적인가?
- [ ] EARS 형식이 올바르게 적용되었는가? (**볼드체** 사용)
- [ ] 요구사항 내용이 변경되지 않았는가?
- [ ] 참조가 올바르게 업데이트되었는가?

---

## 4. 위험 관리 (Risk Management)

### 4.1 식별된 위험

| 위험 | 확률 | 영향 | 완화 조치 |
|------|------|------|----------|
| 요구사항 누락 | 중 | 높 | 변환 전/후 총수 비교 검증 |
| 잘못된 도메인 분류 | 중 | 중 | 수동 검토 프로세스 포함 |
| 참조 관계 파손 | 중 | 중 | 참조 무결성 검증 스크립트 |
| EARS 형식 오류 | 낮 | 중 | 자동화 + 수동 검토 |

### 4.2 완화 전략

**요구사항 누락 방지:**
- 변환 전/후 요구사항 총수 비교
- 각 도메인별 태그 수 검증

**잘못된 도메인 분류 방지:**
- 자동 분류 후 수동 검토
- 불확실한 경우 사용자 검토 요청

**참조 관계 파손 방지:**
- 태그 참조 자동 검증 스크립트
- plan.md, acceptance.md 내 참조 업데이트

---

## 5. 성공 기준 (Success Criteria)

### 5.1 정량적 지표

- **변환 완료율:** 100% (모든 대상 태그 변환)
- **요구사항 보존율:** 100% (0% 손실)
- **형식 준수율:** 100% (모든 태그가 표준 형식 준수)
- **참조 무결성:** 100% (모든 참조가 유효)

### 5.2 정성적 지표

- **EARS 형식 준수:** 모든 요구사항이 올바른 EARS 패턴 따름
- **도메인 분류 정확성:** 요구사항이 올바른 도메인으로 분류됨
- **문서 가독성:** 태그 형식이 일관되어 가독성 향상

---

## 6. 다음 단계 (Next Steps)

### 6.1 즉시 실행

1. **분석 단계 시작:**
   - 대상 SPEC 문서 읽기
   - 태그 인벤토리 작성

2. **매핑 테이블 작성:**
   - 기존 태그 → 새로운 태그 매핑

### 6.2 후속 작업

1. **변환 실행:**
   - 자동화 스크립트 실행 또는 수동 변환
   - 수동 검토 및 수정

2. **검증 및 문서화:**
   - 변환 결과 검증
   - 변환 보고서 작성

---

**TAG BLOCK END**
