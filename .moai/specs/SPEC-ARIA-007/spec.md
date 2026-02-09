# SPEC-ARIA-007: SPEC 태깅 형식 통일

**TAG:** SPEC-ARIA-007
**Status:** Completed
**Priority:** High
**Created:** 2026-02-09
**Completed:** 2026-02-09
**Assigned:** manager-spec
**Related SPECs:** SPEC-ARIA-001, SPEC-ARIA-002, SPEC-ARIA-003, SPEC-ARIA-004, SPEC-ARIA-005, SPEC-ARIA-006

---

## 1. 서론 (Introduction)

### 1.1 배경 (Background)

ARIA 프로젝트의 SPEC-001부터 SPEC-006까지 다양한 태깅 형식이 사용되었습니다. 이로 인해 요구사항 추적, 검색, 관리에 어려움이 발생하고 있습니다.

**현재 태깅 형식 현황:**

- **SPEC-001**: `[UR-001]`, `[ER-001]`, `[SR-001]`, `[WR-001]`, `[OR-001]` (도메인별 접두사 형식)
- **SPEC-002**: `REQ-001` ~ `REQ-073` (단순 순차 형식)
- **SPEC-003**: WHEN/IF/WHERE prose (태그 없음)
- **SPEC-004**: WHEN/IF prose (태그 없음)
- **SPEC-005**: `[REQ-1.1.1]` 계층 형식

이러한 형식 불일치는 다음과 같은 문제를 야기합니다:
1. 요구사항 추적 매트릭스 생성 어려움
2. 도메인별 요구사항 분석 불가능
3. SPEC 간 참조 및 관계 파악 어려움
4. 자동화된 품질 검증 도구 적용 불가

### 1.2 목적 (Purpose)

SPEC-ARIA-007의 목적은 다음과 같습니다:

1. **형식 통일**: 모든 SPEC 문서의 태깅 형식을 SPEC-001의 도메인별 접두사 형식으로 통일
2. **범위 정의**: 대상 SPEC 문서(SPEC-002~005)의 재작성 범위 및 방법 정의
3. **자동화 지원**: 태그 변환 자동화 스크립트/도구 개발 가이드 제공
4. **품질 보증**: 변환 후 요구사항 누락 방지 및 정합성 검증

### 1.3 범위 (Scope)

**포함 (In Scope):**
- SPEC-002: `REQ-001` ~ `REQ-073` → 도메인별 태그로 변환
- SPEC-003: prose 요구사항 → EARS 형식 + 도메인별 태그로 변환
- SPEC-004: prose 요구사항 → EARS 형식 + 도메인별 태그로 변환
- SPEC-005: `[REQ-1.1.1]` → 도메인별 태그로 변환

**제외 (Out of Scope):**
- SPEC-001: 이미 올바른 형식 사용 중
- SPEC-006: Phase 5 Advanced Features (분석 대상에서 제외)
- 새로운 요구사항 추가 (기존 요구사항의 형식만 변경)

---

## 2. 환경 및 가정 (Environment & Assumptions)

### 2.1 환경 (Environment)

**시스템 환경:**
- Claude Code v2.1.32+
- MoAI-ADK v1.3.0+ (EARS format support)
- Git 형상 관리 시스템

**개발 환경:**
- Markdown + YAML frontmatter
- `.moai/specs/SPEC-XXX/spec.md` 파일 구조

**문서 형식:**
- EARS (Easy Approach to Requirements Syntax)
- 도메인별 접두사: UR, ER, SR, WR, OR

### 2.2 가정 (Assumptions)

**기술적 가정:**
- 모든 SPEC 문서가 `.moai/specs/` 디렉토리에 존재
- Git 이력을 통한 변경 추적 가능
- 원본 요구사항 내용은 변경하지 않고 태그만 변환

**비즈니스 가정:**
- 요구사항의 의미와 내용은 유지되어야 함
- 요구사항 간의 관계 및 추적성은 보존되어야 함
- 변환 후 모든 요구사항이 누락 없이 존재해야 함

**리스크 요소:**
- 대규모 텍스트 변환 시 오타/오변환 가능성
- 복잡한 prose 요구사항의 EARS 변환 모호성
- 요구사항 간 참조 관계 파손 위험

---

## 3. 요구사항 (Requirements)

### 3.1 EARS 형식 요구사항

#### **Ubiquitous Requirements (시스템 전체)**

**[UR-001]** 시스템은 **항상** SPEC-001의 도메인별 접두사 형식을 태깅 표준으로 준수해야 한다.

- **접두사 정의**:
  - `[UR-###]`: Ubiquitous Requirements (항상 활성)
  - `[ER-###]`: Event-Driven Requirements (WHEN-THEN)
  - `[SR-###]`: State-Driven Requirements (IF-THEN)
  - `[WR-###]`: Unwanted Requirements (금지 사항)
  - `[OR-###]`: Optional Requirements (선택 사항)

**[UR-002]** 모든 태그는 **항상** 대괄호 `[]`로 감싸져야 한다.

**[UR-003]** 태그 번호는 **항상** 각 도메인 내에서 순차적으로 할당되어야 한다.

#### **Event-Driven Requirements (이벤트 기반)**

**[ER-001]** **WHEN** 태그 변환 작업이 시작되면, 시스템은 **SHALL** 기존 태그를 인벤토리해야 한다.

- **대상:** SPEC-002~005의 모든 요구사항 태그
- **출력:** 현재 태그 형식 및 개수 보고서

**[ER-002]** **WHEN** 기존 태그가 분류되면, 시스템은 **SHALL** 새로운 도메인별 태그로 매핑해야 한다.

- **매핑 규칙:**
  - "시스템은 항상" → `[UR-###]`
  - "WHEN" 또는 "사용자가"로 시작 → `[ER-###]`
  - "IF" 또는 "조건" 관련 → `[SR-###]`
  - "절대", "안 된다" → `[WR-###]`
  - "가능하면", "제공" → `[OR-###]`

**[ER-003]** **WHEN** prose 요구사항을 변환하면, 시스템은 **SHALL** EARS 형식으로 변환해야 한다.

- **SPEC-003, SPEC-004 대상:**
  - WHEN 요구사항 → `[ER-###]` 태그 + EARS 형식
  - IF 요구사항 → `[SR-###]` 태그 + EARS 형식
  - WHERE 요구사항 → `[OR-###]` 태그 + EARS 형식

**[ER-004]** **WHEN** 태그가 변환되면, 시스템은 **SHALL** 관련 참조를 업데이트해야 한다.

- **참조 업데이트:** spec.md, plan.md, acceptance.md 내 태그 참조
- **검증:** 모든 참조가 유효한지 확인

#### **State-Driven Requirements (상태 기반)**

**[SR-001]** **IF** 기존 태그가 도메인별 분류에 적합하지 않으면, 시스템은 **SHALL** 사용자 검토를 요청해야 한다.

- **예시:** "WHEN 조건이 충족되면 IF 동작을 수행한다"와 같은 복합 요구사항

**[SR-002]** **IF** 요구사항이 누락된 것으로 발견되면, 시스템은 **SHALL** 원본 문서와 대조해야 한다.

**[SR-003]** **IF** 태그 번호 충돌이 발생하면, 시스템은 **SHALL** 재번호 할당을 수행해야 한다.

#### **Optional Requirements (선택적)**

**[OR-001]** **가능하면** 시스템은 태그 변환 스크립트를 제공해야 한다.

- **목적:** 반복적 변환 작업 자동화
- **구현:** Python 또는 Bash 스크립트

**[OR-002]** **가능하면** 시스템은 변환前后 비교 보고서를 생성해야 한다.

- **내용:** 변환 전/후 태그 매핑 테이블

#### **Unwanted Requirements (금지 사항)**

**[WR-001]** 시스템은 **절대** 요구사항의 내용을 변경하면 안 된다.

- **허용:** 태그 형식, EARS 구조 변환만
- **금지:** 요구사항 의미, 내용, 범위 변경

**[WR-002]** 시스템은 **절대** 태그를 누락하면 안 된다.

- **검증:** 변환 전/후 요구사항 총수 비교

**[WR-003]** 시스템은 **절대** 기존 태그 형식과 혼합된 태그를 사용하면 안 된다.

- **금지:** `[REQ-001]`, `[ER-001]` 혼합 사용
- **요구:** 순수 도메인별 접두사 형식만 사용

### 3.2 기능적 요구사항

#### 3.2.1 SPEC-002 변환 (REQ-001 ~ REQ-073)

**[FR-001]** `REQ-001` ~ `REQ-073` 태그를 도메인별 태그로 재분류해야 한다.

- **분류 기준:** 요구사항 내용의 EARS 패턴 분석
- **예시 변환:**
  - `REQ-001`: "시스템은 항상 VALID 품질 프레임워크를 준수해야 한다" → `[UR-001]`
  - `REQ-004`: "WHEN 사용자가 /aria brief를 실행하면" → `[ER-001]`
  - `REQ-008`: "IF 에이전트가 read-only 작업을 수행하면" → `[SR-001]`
  - `REQ-013`: "시스템은 절대 직접 구현을 수행하면 안 된다" → `[WR-001]`
  - `REQ-011`: "가능하면 Context7 MCP를 통해" → `[OR-001]`

**[FR-002]** 각 도메인 내에서 순차적 번호를 재할당해야 한다.

- **번호 할당:**
  - `[UR-001]`, `[UR-002]`, ... (Ubiquitous 요구사항만)
  - `[ER-001]`, `[ER-002]`, ... (Event-Driven 요구사항만)
  - `[SR-001]`, `[SR-002]`, ... (State-Driven 요구사항만)
  - `[WR-001]`, `[WR-002]`, ... (Unwanted 요구사항만)
  - `[OR-001]`, `[OR-002]`, ... (Optional 요구사항만)

#### 3.2.2 SPEC-003 변환 (Prose → EARS + 태그)

**[FR-003]** WHEN/IF/WHERE prose 요구사항을 EARS 형식으로 변환해야 한다.

- **변환 규칙:**
  - "WHEN 사용자가 규제 전략을 요청하면, THE 시스템은 SHALL 적용 시장별 요구사항을 분석한다"
  - → **[ER-001]** WHEN 사용자가 규제 전략을 요청하면, 시스템은 **SHALL** 적용 시장별 요구사항을 분석한다.

**[FR-004]** 각 prose 요구사항에 적절한 도메인별 태그를 할당해야 한다.

- **할당 기준:**
  - WHEN 시작 → `[ER-###]`
  - IF 시작 → `[SR-###]`
  - WHERE 시작 → `[OR-###]`

#### 3.2.3 SPEC-004 변환 (Prose → EARS + 태그)

**[FR-005]** WHEN/IF prose 요구사항을 EARS 형식으로 변환해야 한다.

- **SPEC-004 특이사항:** 주로 Event-Driven (WHEN) 요구사항
- **변환 예시:**
  - "WHEN ARIA가 초기화되면, THE 시스템은 SHALL Notion 데이터베이스 스키마를 자동 생성한다"
  - → **[ER-001]** WHEN ARIA가 초기화되면, 시스템은 **SHALL** Notion 데이터베이스 스키마를 자동 생성한다.

#### 3.2.4 SPEC-005 변환 (계층 태그 → 도메인별 태그)

**[FR-006]** `[REQ-1.1.1]` 계층 형식 태그를 도메인별 태그로 변환해야 한다.

- **변환 규칙:**
  - 1.x.x 섹션 → 해당 도메인별 태그
  - 계층 구조는 평탄화하여 순차적 번호 할당

---

## 4. 상세 명세 (Specifications)

### 4.1 태깅 형식 표준 (SPEC-001 기반)

**도메인별 접두사 정의:**

| 접두사 | 도메인 | EARS 패턴 | 예시 |
|--------|--------|-----------|------|
| `[UR-###]` | Ubiquitous Requirements | 시스템은 항상 ~ 해야 한다 | [UR-001] 시스템은 항상 한국어로 응답해야 한다 |
| `[ER-###]` | Event-Driven Requirements | WHEN ~ THEN/S | [ER-001] WHEN 사용자가 명령을 입력하면 |
| `[SR-###]` | State-Driven Requirements | IF ~ THEN | [SR-001] IF Phase 1이 진행 중이면 |
| `[WR-###]` | Unwanted Requirements | ~ 하면 안 된다 | [WR-001] 시스템은 절대 기술 용어로 오류를 보고하면 안 된다 |
| `[OR-###]` | Optional Requirements | 가능하면 ~ 제공해야 한다 | [OR-001] 가능하면 진행 상황을 시각적으로 표시해야 한다 |

### 4.2 변환 매핑 테이블

**SPEC-002 변환 매핑 (일부 예시):**

| 기존 태그 | 요구사항 내용 (요약) | 새로운 태그 | 분류 근거 |
|----------|---------------------|------------|-----------|
| REQ-001 | 시스템은 항상 VALID 준수 | [UR-001] | "항상" 키워드 |
| REQ-002 | 모든 에이전트는 항상 YAML 준수 | [UR-002] | "항상" 키워드 |
| REQ-004 | WHEN /aria brief 실행 | [ER-001] | "WHEN" 키워드 |
| REQ-008 | IF read-only 작업 | [SR-001] | "IF" 키워드 |
| REQ-013 | 시스템은 절대 직접 구현 금지 | [WR-001] | "절대" 키워드 |
| REQ-011 | 가능하면 Context7 자동 조회 | [OR-001] | "가능하면" 키워드 |

**SPEC-003 변환 매핑 (expert-regulatory 예시):**

| 기존 형식 | 새로운 형식 | 변환 규칙 |
|----------|-------------|-----------|
| WHEN 사용자가 규제 전략을 요청하면 | **[ER-001]** WHEN 사용자가 규제 전략을 요청하면 | WHEN 접두사 유지, 태그 추가 |
| IF 제품이 Class III이면 | **[SR-001]** IF 제품이 Class III이면 | IF 접두사 유지, 태그 추가 |
| 시스템은 항상 모든 규제 주장에 출처를 인용 | **[UR-001]** 시스템은 항상 모든 규제 주장에 출처를 인용 | Ubiquitous 분류 |

### 4.3 변환 프로세스

**Phase 1: 분석 (Analysis)**

1. **태그 인벤토리:**
   - 각 SPEC 문서의 모든 태그 추출
   - 형식별 분류 (REQ-###, prose, [REQ-x.y.z])
   - 도메인 분류 (UR, ER, SR, WR, OR)

2. **요구사항 매핑:**
   - 각 요구사항의 EARS 패턴 식별
   - 적절한 도메인별 태그 결정
   - 번호 할당 계획 수립

**Phase 2: 변환 (Transformation)**

1. **태그 변환:**
   - 기존 태그 제거
   - 새로운 도메인별 태그 추가
   - EARS 형식 강조 적용 (**볼드체**)

2. **참조 업데이트:**
   - spec.md 내 태그 참조 업데이트
   - plan.md 내 태그 참조 업데이트
   - acceptance.md 내 태그 참조 업데이트

**Phase 3: 검증 (Verification)**

1. **정합성 검증:**
   - 변환 전/후 요구사항 총수 비교
   - 태그 번호 연속성 검증
   - 도메인별 분류 정확성 검증

2. **품질 검증:**
   - EARS 형식 준수 여부
   - 태그 형식 표준 준수 여부
   - 참조 무결성 검증

---

## 5. 추적성 (Traceability)

### 5.1 요구사항-대상 SPEC 매핑

| 요구사항 그룹 | 대상 SPEC | 변환 범위 |
|--------------|-----------|-----------|
| UR-001 ~ UR-003 | SPEC-002, SPEC-003, SPEC-004, SPEC-005 | 전체 |
| ER-001 ~ ER-004 | SPEC-002, SPEC-003, SPEC-004 | 전체 |
| SR-001 ~ SR-003 | SPEC-002, SPEC-003, SPEC-004 | 전체 |
| FR-001 ~ FR-002 | SPEC-002 | REQ-001 ~ REQ-073 |
| FR-003 ~ FR-004 | SPEC-003 | 전체 prose 요구사항 |
| FR-005 | SPEC-004 | 전체 prose 요구사항 |
| FR-006 | SPEC-005 | [REQ-x.y.z] 형식 전체 |

### 5.2 변환 영향 분석

| 대상 SPEC | 기존 태그 형식 | 변환 태그 수 | 영향받는 파일 |
|-----------|----------------|-------------|---------------|
| SPEC-002 | REQ-### | 73개 | spec.md, plan.md, acceptance.md |
| SPEC-003 | Prose (WHEN/IF/WHERE) | ~40개 (예상) | spec.md (주요) |
| SPEC-004 | Prose (WHEN/IF) | ~30개 (예상) | spec.md (주요) |
| SPEC-005 | [REQ-1.1.1] | ~20개 (예상) | spec.md, plan.md, acceptance.md |
| **합계** | - | **~163개** | **12개 파일** |

---

## 6. 참조 (References)

### 6.1 입력 문서

- `.moai/specs/SPEC-ARIA-001/spec.md` - 태깅 형식 표준
- `.moai/specs/SPEC-ARIA-002/spec.md` - REQ-### 형식
- `.moai/specs/SPEC-ARIA-003/spec.md` - prose 형식
- `.moai/specs/SPEC-ARIA-004/spec.md` - prose 형식
- `.moai/specs/SPEC-ARIA-005/spec.md` - [REQ-x.y.z] 형식

### 6.2 관련 SPEC

- SPEC-ARIA-006: Phase 5 Advanced Features (본 SPEC과 무관)

### 6.3 표준 및 프레임워크

- EARS (Easy Approach to Requirements Syntax)
- MoAI-ADK SPEC-First DDD 워크플로우

---

## 7. 부록 (Appendix)

### 7.1 용어 정의

- **EARS**: Easy Approach to Requirements Syntax (요구사항 정의 표준)
- **도메인별 접두사**: UR, ER, SR, WR, OR 태그 접두사
- **태그 형식 표준**: SPEC-001에서 정의한 [XX-###] 형식
- **Prose 요구사항**: WHEN/IF/WHERE로 시작하는 서술형 요구사항

### 7.2 변경 이력

| 버전 | 날짜 | 변경 사항 | 작성자 |
|------|------|----------|--------|
| 1.0.0 | 2026-02-09 | 초기 SPEC 작성 | manager-spec |

---

**TAG BLOCK END**

**다음 단계:**
1. `plan.md` - 구현 계획 및 마일스톤
2. `acceptance.md` - 인수 조건 및 테스트 시나리오
