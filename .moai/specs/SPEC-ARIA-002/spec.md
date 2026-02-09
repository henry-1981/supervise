# SPEC-ARIA-002: ARIA Phase 2 - Universal Business Agents

**TAG:** SPEC-ARIA-002
**Status:** Planned
**Priority:** High
**Created:** 2025-02-09
**Assigned:** manager-spec, expert-backend, expert-frontend

---

## 1. 서론 (Introduction)

### 1.1 배경 (Background)

ARIA (AI Regulatory Intelligence Assistant) Phase 1이 완료되어 기본 오케스트레이션, 메인 커맨드, 코어 스킬이 구현되었습니다. Phase 2에서는 비즈니스 워크플로우 자동화를 위한 범용 비즈니스 에이전트 시스템을 구축합니다.

Phase 2는 다음과 같은 비즈니스 요구를 충족합니다:

- **문서 중심 워크플로우**: 규제 문서, 기술 문서, 검토 보고서의 작성 및 관리
- **품질 관리**: VALID 프레임워크 기반의 체계적인 품질 보증
- **프로젝트 관리**: 마일스톤 추적 및 진행 상황 모니터링
- **비즈니스 에이전트 협업**: 작성, 분석, 검토, 리서치 전문가의 협업

### 1.2 목적 (Purpose)

ARIA Phase 2의 목적은 다음과 같습니다:

1. **Core Layer 구축**: 문서, 품질, 프로젝트 관리 에이전트 개발
2. **Business Layer 구축**: 작성, 분석, 검토, 리서치 전문가 에이전트 개발
3. **스킬 시스템 구현**: VALID 프레임워크, 문서 작성 스타일, 템플릿 관리, 리서치 방법론, 데이터 분석 스킬 개발
4. **커맨드 확장**: Brief, Execute, Deliver, Template, Knowledge 커맨드 구현
5. **MCP 통합**: Context7, Sequential Thinking, Notion MCP 연동

### 1.3 범위 (Scope)

**포함 (In Scope):**
- Core Layer 에이전트 3개 (manager-docs, manager-quality, manager-project)
- Business Layer 에이전트 4개 (expert-writer, expert-analyst, expert-reviewer, expert-researcher)
- 스킬 5개 (aria-quality-valid, aria-writing-style, aria-templates, aria-research, aria-analysis)
- 커맨드 5개 (brief, execute, deliver, template, knowledge)
- MCP 서버 통합 (Context7, Sequential Thinking, Notion)

**제외 (Out of Scope):**
- RA/QA 전문 도메인 에이전트 (Phase 2.3)
- 외부 서비스 통합 (Phase 4)
- 고급 분석 기능 (Phase 3+)

---

## 2. 환경 및 가정 (Environment & Assumptions)

### 2.1 환경 (Environment)

**시스템 환경:**
- Claude Code v2.1.32+
- MoAI-ADK v1.3.0+ (SPEC-First DDD, TRUST 5, Progressive Disclosure)
- Git 워크트리 지원
- 200K 토큰 컨텍스트 윈도우

**개발 환경:**
- Python 3.13+ (CLI 도구)
- TypeScript 5.9+ (스킬/에이전트 정의)
- YAML 프론트매터 스키마 호환

**MCP 서버:**
- Context7 (규제/표준 문서 조회)
- Sequential Thinking (복잡한 분석)
- Notion MCP (지식 베이스 연동)

### 2.2 가정 (Assumptions)

**기술적 가정:**
- Phase 1 컴포넌트(orchestrator, aria-core)가 정상 작동
- MCP 서버가 안정적으로 연결 가능
- Git 워크트리가 활성화되어 있음

**비즈니스 가정:**
- 사용자는 RA/QA 도메인 지식을 보유
- 영어/한국어 이중 언어 지원 필요
- 문서 템플릿이 사전에 정의되어 있음

**리스크 요소:**
- 에이전트 도구 권한 설정 오류로 인한 작업 실패
- MCP 서버 연결 불안정성
- 스킬 Progressive Disclosure 구현 복잡성

---

## 3. 요구사항 (Requirements)

### 3.1 EARS 형식 요구사항

#### **Ubiquitous Requirements (시스템 전체)**

**REQ-001:** 시스템은 **항상** MoAI-ADK의 TRUST 5 품질 프레임워크를 준수해야 한다.

**REQ-002:** 모든 에이전트는 **항상** YAML 프론트매터 스키마를 따라야 한다.

**REQ-003:** 시스템은 **항상** 사용자의 conversation_language로 응답해야 한다.

#### **Event-Driven Requirements (이벤트 기반)**

**REQ-004:** **WHEN** 사용자가 `/aria brief` 커맨드를 실행하면, 시스템은 작업 이해 및 범위 정의 프로세스를 시작해야 한다.

**REQ-005:** **WHEN** 사용자가 `/aria execute` 커맨드를 실행하면, 시스템은 연구-작성-검토-정제 워크플로우를 실행해야 한다.

**REQ-006:** **WHEN** 사용자가 `/aria deliver` 커맨드를 실행하면, 시스템은 최종 산출물을 생성하고 배포해야 한다.

**REQ-007:** **WHEN** 문서가 생성되면, manager-quality는 VALID 프레임워크 품질 게이트를 실행해야 한다.

#### **State-Driven Requirements (상태 기반)**

**REQ-008:** **IF** 에이전트가 read-only 작업을 수행하면, permissionMode를 'plan'으로 설정해야 한다.

**REQ-009:** **IF** 에이전트가 구현 작업을 수행하면, permissionMode를 'acceptEdits'로 설정해야 한다.

**REQ-010:** **IF** 문서가 품질 기준을 충족하지 못하면, system은 피드백과 재검토를 요청해야 한다.

#### **Optional Requirements (선택적)**

**REQ-011:** **가능하면** Context7 MCP를 통해 최신 규제 문서를 자동으로 조회해야 한다.

**REQ-012:** **가능하면** Sequential Thinking MCP를 사용하여 복잡한 규제 경로를 분석해야 한다.

#### **Unwanted Requirements (금지 사항)**

**REQ-013:** 시스템은 **절대** 직접 구현을 수행하면 안 된다 (모든 작업은 에이전트 위임).

**REQ-014:** 에이전트는 **절대** XML 태그를 사용자 응답에 표시하면 안 된다.

**REQ-015:** 시스템은 **절대** 규제 출처 인용 없이 규제 주장을 하면 안 된다.

### 3.2 기능적 요구사항

#### 3.2.1 Core Layer 에이전트

**manager-docs (문서 관리자):**

**REQ-016:** manager-docs는 문서 수명 주기(작성-검토-승인-배포)를 관리해야 한다.

**REQ-017:** manager-docs는 템플릿 기반 문서 생성을 지원해야 한다.

**REQ-018:** manager-docs는 다중 형식(Markdown, PDF, Word) 내보내기를 지원해야 한다.

**REQ-019:** manager-docs는 버전 관리 및 변경 추적을 제공해야 한다.

**manager-quality (품질 관리자):**

**REQ-020:** manager-quality는 VALID 프레임워크를 구현해야 한다.

**REQ-021:** manager-quality는 각 차원(Verified, Accurate, Linked, Inspectable, Deliverable)을 검증해야 한다.

**REQ-022:** manager-quality는 품질 보고서를 생성해야 한다.

**REQ-023:** manager-quality는 개선 권장사항을 제공해야 한다.

**manager-project (프로젝트 관리자):**

**REQ-024:** manager-project는 마일스톤 추적을 제공해야 한다.

**REQ-025:** manager-project는 작업 상태 모니터링을 지원해야 한다.

**REQ-026:** manager-project는 리스크 레지스터를 유지해야 한다.

**REQ-027:** manager-project는 진행 상황 보고서를 생성해야 한다.

#### 3.2.2 Business Layer 에이전트

**expert-writer (기술 작성 전문가):**

**REQ-028:** expert-writer는 기술 문서 작성 표준을 따라야 한다.

**REQ-029:** expert-writer는 aria-writing-style 스킬을 활용해야 한다.

**REQ-030:** expert-writer는 템플릿을 기반으로 문서를 생성해야 한다.

**REQ-031:** expert-writer는 명확하고 간결한 문체를 유지해야 한다.

**expert-analyst (데이터 분석 전문가):**

**REQ-032:** expert-analyst는 데이터 분석 방법론을 적용해야 한다.

**REQ-033:** expert-analyst는 aria-analysis 스킬을 활용해야 한다.

**REQ-034:** expert-analyst는 통계 분석 및 추세 식별을 수행해야 한다.

**REQ-035:** expert-analyst는 시각화를 제공해야 한다.

**expert-reviewer (문서 검토 전문가):**

**REQ-036:** expert-reviewer는 문서 검토 체크리스트를 따라야 한다.

**REQ-037:** expert-reviewer는 규제 준수성을 검증해야 한다.

**REQ-038:** expert-reviewer는 일관성 검사를 수행해야 한다.

**REQ-039:** expert-reviewer는 구체적인 피드백을 제공해야 한다.

**expert-researcher (규제 리서치 전문가):**

**REQ-040:** expert-researcher는 규제 정보를 체계적으로 수집해야 한다.

**REQ-041:** expert-researcher는 aria-research 스킬을 활용해야 한다.

**REQ-042:** expert-researcher는 Context7 MCP를 사용하여 문서를 조회해야 한다.

**REQ-043:** expert-researcher는 출처를 명확하게 인용해야 한다.

#### 3.2.3 스킬 시스템

**aria-quality-valid 스킬:**

**REQ-044:** aria-quality-valid는 VALID 프레임워크를 정의해야 한다.

**REQ-045:** aria-quality-valid는 각 차원별 검증 기준을 제공해야 한다.

**REQ-046:** aria-quality-valid는 품질 점수 계산 방법을 정의해야 한다.

**aria-writing-style 스킬:**

**REQ-047:** aria-writing-style은 기술 문서 작성 스타일 가이드를 제공해야 한다.

**REQ-048:** aria-writing-style은 용어 사용 일관성을 보장해야 한다.

**REQ-049:** aria-writing-style은 문장 구조 가이드라인을 제공해야 한다.

**aria-templates 스킬:**

**REQ-050:** aria-templates은 문서 템플릿 라이브러리를 제공해야 한다.

**REQ-051:** aria-templates은 템플릿 사용 가이드를 포함해야 한다.

**REQ-052:** aria-templates은 사용자 정의 템플릿을 지원해야 한다.

**aria-research 스킬:**

**REQ-053:** aria-research는 리서치 방법론을 정의해야 한다.

**REQ-054:** aria-research는 출처 인용 표준을 제공해야 한다.

**REQ-055:** aria-research는 정보 품질 평가 기준을 정의해야 한다.

**aria-analysis 스킬:**

**REQ-056:** aria-analysis는 데이터 분석 방법론을 제공해야 한다.

**REQ-057:** aria-analysis는 통계 기법을 정의해야 한다.

**REQ-058:** aria-analysis는 결과 해석 가이드를 제공해야 한다.

#### 3.2.4 커맨드 시스템

**brief 커맨드:**

**REQ-059:** brief는 작업 이해 및 범위 정의를 지원해야 한다.

**REQ-060:** brief는 사용자 질문을 통해 명확성을 확보해야 한다.

**REQ-061:** brief는 실행 계획을 생성해야 한다.

**execute 커맨드:**

**REQ-062:** execute는 워크플로우를 실행해야 한다.

**REQ-063:** execute는 에이전트 간 협업을 조율해야 한다.

**REQ-064:** execute는 진행 상황을 보고해야 한다.

**deliver 커맨드:**

**REQ-065:** deliver는 최종 산출물을 생성해야 한다.

**REQ-066:** deliver는 형식 변환을 지원해야 한다.

**REQ-067:** deliver는 배포 채널로 전송해야 한다.

**template 커맨드:**

**REQ-068:** template은 템플릿 목록을 표시해야 한다.

**REQ-069:** template은 템플릿 검색을 지원해야 한다.

**REQ-070:** template은 템플릿 미리보기를 제공해야 한다.

**knowledge 커맨드:**

**REQ-071:** knowledge는 지식 베이스를 관리해야 한다.

**REQ-072:** knowledge는 Notion과 동기화해야 한다.

**REQ-073:** knowledge는 검색 기능을 제공해야 한다.

---

## 4. 상세 명세 (Specifications)

### 4.1 아키텍처

#### 4.1.1 에이전트 계층 구조

```
┌─────────────────────────────────────────────────────────────┐
│                    orchestrator (Phase 1)                   │
│                  - Brief-Execute-Deliver                    │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌───────▼──────┐    ┌────────▼────────┐    ┌───────▼──────┐
│  Core Layer  │    │ Business Layer  │    │ RA/QA Layer  │
│              │    │                 │    │   (Phase 3)  │
│ manager-docs │    │ expert-writer   │    │ expert-       │
│ manager-     │    │ expert-analyst  │    │   regulatory  │
│   quality    │    │ expert-reviewer │    │ expert-       │
│ manager-     │    │ expert-         │    │   standards   │
│   project    │    │   researcher    │    │ ...           │
└──────────────┘    └──────────────────┘    └──────────────┘
        │                     │
        └─────────────────────┼─────────────────────┐
                              │                     │
                    ┌─────────▼─────────┐   ┌──────▼──────┐
                    │   Skill System    │   │   Commands  │
                    │                   │   │             │
                    │ aria-quality-valid│   │ brief       │
                    │ aria-writing-style│   │ execute     │
                    │ aria-templates    │   │ deliver     │
                    │ aria-research     │   │ template    │
                    │ aria-analysis     │   │ knowledge   │
                    └───────────────────┘   └─────────────┘
```

#### 4.1.2 에이전트 정의

**manager-docs:**

```yaml
---
name: manager-docs
description: >
  Document lifecycle management agent responsible for document creation,
  review, approval, and distribution. Coordinates document workflows
  using templates and ensures consistency across all documentation.
model: sonnet
permissionMode: acceptEdits
tools: Read Write Edit Grep Glob Bash Task
skills:
  - aria-writing-style
  - aria-templates
mcpServers:
  - notion
---
```

**manager-quality:**

```yaml
---
name: manager-quality
description: >
  Quality assurance agent implementing VALID framework (Verified, Accurate,
  Linked, Inspectable, Deliverable). Performs quality gate validation
  and generates improvement recommendations.
model: sonnet
permissionMode: plan
tools: Read Grep Glob Bash
skills:
  - aria-quality-valid
---
```

**expert-writer:**

```yaml
---
name: expert-writer
description: >
  Technical writing expert specializing in regulatory and technical
  documentation. Creates clear, concise, and compliant documents
  using established templates and style guides.
model: sonnet
permissionMode: acceptEdits
tools: Read Write Edit Grep Glob Bash
skills:
  - aria-writing-style
  - aria-templates
mcpServers:
  - context7
---
```

### 4.2 VALID 프레임워크

| 차원 | 정의 | 검증 기준 |
|------|------|----------|
| **V**erified | 내용이 원본 규정 텍스트와 일치 | 원본 규정 교차 참조 |
| **A**ccurate | 데이터, 수치, 참조가 정확하고 최신 | 출처 검증, 날짜 확인 |
| **L**inked | 요구사항-문서-증거 간 추적 가능 | 추적성 행렬 검증 |
| **I**nspectable | 감사 추적 유지, 결정 근거 문서화 | 감사 추적 완전성 검사 |
| **D**eliverable | 산출물이 제출 형식 요구사항 충족 | 템플릿 적합성 검사 |

### 4.3 Brief-Execute-Deliver 워크플로우

```
┌──────────┐
│  BRIEF   │ 60% - Task Understanding & Planning
│  Phase   │
└─────┬────┘
      │
      ▼
┌──────────┐
│ EXECUTE  │ 30% - Research, Draft, Review, Refine
│  Phase   │
└─────┬────┘
      │
      ▼
┌──────────┐
│ DELIVER  │ 10% - Validation & Distribution
│  Phase   │
└──────────┘
```

### 4.4 MCP 통합

**Context7 MCP:**
- 규제 문서 최신 버전 조회
- 표준 문서 검색 및 인용
- 라이브러리 문서 접근

**Sequential Thinking MCP:**
- 복잡한 규제 경로 분석
- 다중 시장 전략 수립
- 위험 평가

**Notion MCP:**
- 중앙 지식 허브
- 문서 레지스트리
- CAPA 추적기
- 위험 레지스트리

---

## 5. 추적성 (Traceability)

### 5.1 요구사항-에이전트 매핑

| 요구사항 그룹 | 관련 에이전트 |
|--------------|-------------|
| REQ-016 ~ REQ-019 | manager-docs |
| REQ-020 ~ REQ-023 | manager-quality |
| REQ-024 ~ REQ-027 | manager-project |
| REQ-028 ~ REQ-031 | expert-writer |
| REQ-032 ~ REQ-035 | expert-analyst |
| REQ-036 ~ REQ-039 | expert-reviewer |
| REQ-040 ~ REQ-043 | expert-researcher |

### 5.2 요구사항-스킬 매핑

| 요구사항 그룹 | 관련 스킬 |
|--------------|----------|
| REQ-044 ~ REQ-046 | aria-quality-valid |
| REQ-047 ~ REQ-049 | aria-writing-style |
| REQ-050 ~ REQ-052 | aria-templates |
| REQ-053 ~ REQ-055 | aria-research |
| REQ-056 ~ REQ-058 | aria-analysis |

### 5.3 요구사항-커맨드 매핑

| 요구사항 그룹 | 관련 커맨드 |
|--------------|-----------|
| REQ-059 ~ REQ-061 | brief |
| REQ-062 ~ REQ-064 | execute |
| REQ-065 ~ REQ-067 | deliver |
| REQ-068 ~ REQ-070 | template |
| REQ-071 ~ REQ-073 | knowledge |

---

## 6. 참조 (References)

### 6.1 입력 문서

- `docs/specs/ARCHITECTURE-REDESIGN.md` - 전체 아키텍처 설계
- `docs/context.md` - 프로젝트 컨텍스트
- `CLAUDE.md` - ARIA 실행 지시문

### 6.2 관련 SPEC

- SPEC-ARIA-001: Phase 1 코어 시스템 (완료)

### 6.3 표준 및 프레임워크

- MoAI-ADK SPEC-First DDD 워크플로우
- MoAI TRUST 5 품질 프레임워크
- EARS (Easy Approach to Requirements Syntax)
- Agent Skills Open Standard (agentskills.io)

---

## 7. 부록 (Appendix)

### 7.1 용어 정의

- **VALID Framework**: Verified, Accurate, Linked, Inspectable, Deliverable 품질 차원
- **Brief-Execute-Deliver**: ARIA의 3단계 워크플로우
- **Progressive Disclosure**: 3단계 지식 전달 시스템
- **MCP**: Model Context Protocol

### 7.2 변경 이력

| 버전 | 날짜 | 변경 사항 | 작성자 |
|------|------|----------|--------|
| 1.0.0 | 2025-02-09 | 초기 SPEC 작성 | manager-spec |

---

**TAG BLOCK END**

**다음 단계:**
1. `plan.md` - 구현 계획 및 마일스톤
2. `acceptance.md` - 인수 조건 및 테스트 시나리오
