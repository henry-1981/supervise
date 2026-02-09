# SPEC-ARIA-002: Implementation Plan

**TAG:** SPEC-ARIA-002
**Related:** spec.md, acceptance.md
**Created:** 2025-02-09

---

## 1. 구현 전략 (Implementation Strategy)

### 1.1 단계적 접근 (Phased Approach)

ARIA Phase 2는 3개의 하위 단계로 나누어 구현합니다:

**Phase 2.1: Core Layer + aria-core 스킬**
- manager-docs, manager-quality, manager-project 에이전트
- aria-quality-valid 스킬 확장
- 기본 워크플로우 구현

**Phase 2.2: Business Layer + 품질 스킬**
- expert-writer, expert-analyst, expert-reviewer, expert-researcher 에이전트
- aria-writing-style, aria-templates 스킬
- Brief-Execute-Deliver 워크플로우 완성

**Phase 2.3: 리서치/분석 스킬 + MCP 통합**
- aria-research, aria-analysis 스킬
- Context7, Sequential Thinking MCP 연동
- Notion MCP 통합

### 1.2 기술 원칙 (Technical Principles)

1. **MoAI-ADK 호환성**: 모든 에이전트/스킬은 MoAI 표준 준수
2. **Progressive Disclosure**: 스킬 모듈화 및 레벨별 로딩
3. **YAML 스키마 준수**: 에이전트 정의 표준화
4. **품질 우선**: TRUST 5 및 VALID 프레임워크 적용

---

## 2. 마일스톤 (Milestones)

### 2.1 Phase 2.1: Core Layer

**목표 (Priority High):**
- Core Layer 에이전트 3개 구현
- VALID 프레임워크 스킬 구현
- 기본 워크플로우 동작

**작업 항목:**
1. manager-docs 에이전트 구현
   - 문서 수명 주기 관리
   - 템플릿 기반 생성
   - 다중 형식 내보내기

2. manager-quality 에이전트 구현
   - VALID 프레임워크 구현
   - 품질 검증 로직
   - 개선 권장사항 생성

3. manager-project 에이전트 구현
   - 마일스톤 추적
   - 작업 상태 모니터링
   - 진행 상황 보고

4. aria-quality-valid 스킬 구현
   - VALID 5차원 정의
   - 검증 기준 구현
   - 품질 점수 계산

**완료 기준:**
- 모든 Core 에이전트가 단위 테스트 통과
- VALID 프레임워크가 규제 문서 검증에 적용 가능
- 기본 BriefExecute 프로세스가 작동

### 2.2 Phase 2.2: Business Layer

**목표 (Priority High):**
- Business Layer 에이전트 4개 구현
- 문서 작성/검토 스킬 구현
- 워크플로우 완성

**작업 항목:**
1. expert-writer 에이전트 구현
   - 기술 문서 작성
   - 템플릿 활용
   - 문체 가이드 준수

2. expert-analyst 에이전트 구현
   - 데이터 분석 방법론 적용
   - 통계 분석 수행
   - 시각화 제공

3. expert-reviewer 에이전트 구현
   - 문서 검토 수행
   - 규제 준수성 검증
   - 구체적 피드백 제공

4. expert-researcher 에이전트 구현
   - 규제 정보 수집
   - 출처 인용
   - 정보 품질 평가

5. aria-writing-style 스킬 구현
   - 기술 문서 스타일 가이드
   - 용어 사용 일관성
   - 문장 구조 가이드라인

6. aria-templates 스킬 구현
   - 템플릿 라이브러리 제공
   - 템플릿 사용 가이드
   - 사용자 정의 템플릿 지원

**완료 기준:**
- 모든 Business 에이전트가 단위 테스트 통과
- 문서 작성-검토 워크플로우가 작동
- 템플릿 기반 문서 생성 가능

### 2.3 Phase 2.3: MCP Integration

**목표 (Priority Medium):**
- 리서치/분석 스킬 구현
- MCP 서버 통합 완료
- 지식 베이스 연동

**작업 항목:**
1. aria-research 스킬 구현
   - 리서치 방법론 정의
   - 출처 인용 표준
   - 정보 품질 평가 기준

2. aria-analysis 스킬 구현
   - 데이터 분석 방법론
   - 통계 기법 정의
   - 결과 해석 가이드

3. Context7 MCP 통합
   - 규제 문서 조회
   - 표준 문서 검색
   - 라이브러리 문서 접근

4. Sequential Thinking MCP 통합
   - 복잡한 규제 경로 분석
   - 다중 시장 전략 수립

5. Notion MCP 통합
   - 중앙 지식 허브 연결
   - 문서 레지스트리 동기화
   - CAPA 추적기 연동

**완료 기준:**
- 모든 MCP 연결이 정상 작동
- 리서치/분석 워크플로우가 작동
- Notion 데이터 동기화 가능

---

## 3. 기술 접근 (Technical Approach)

### 3.1 에이전트 구조

**YAML 프론트매터 표준:**

```yaml
---
name: {agent-name}
description: >
  Clear description of when to invoke this agent, written in third person,
  maximum 1024 characters.
model: sonnet
permissionMode: acceptEdits|plan|default
tools: Read Write Edit Grep Glob Bash Task
skills:
  - skill-name-1
  - skill-name-2
mcpServers:
  - server-name-1
  - server-name-2
memory: project
---
```

**도구 권한 매트릭스:**

| 에이전트 타입 | permissionMode | 도구 제한 |
|--------------|----------------|-----------|
| Manager (구현) | acceptEdits | Read, Write, Edit, Bash |
| Manager (검토) | plan | Read, Grep, Glob |
| Expert (구현) | acceptEdits | Read, Write, Edit, Bash |
| Expert (분석) | plan | Read, Grep, Glob |

### 3.2 스킬 아키텍처

**Progressive Disclosure 구조:**

```
skills/aria-{name}/
├── SKILL.md (Level 1: Metadata, ~100 tokens)
├── modules/
│   ├── quick-reference.md (Level 2: Quick Start, ~1000 tokens)
│   ├── implementation.md (Level 2: Implementation Guide, ~3000 tokens)
│   └── advanced.md (Level 3: Advanced Topics, ~5000 tokens)
├── examples.md (Level 3: Working Examples)
└── reference.md (Level 3: External Resources)
```

**SKILL.md 구조:**

```markdown
---
name: aria-{name}
description: >
  Purpose description, maximum 1024 characters.
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2025-02-09"
  modularized: "true"
  tags: "aria, business, {specific-tags}"
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000
triggers:
  keywords: ["{trigger-words}"]
  agents: ["{related-agents}"]
  phases: ["brief", "execute", "deliver"]
---
```

### 3.3 커맨드 구조

**커맨드 YAML 정의:**

```yaml
---
name: aria-{command}
description: >
  Command description in folded scalar format.
parameters:
  - name: task
    description: Task description or identifier
    required: true
  - name: options
    description: Additional options
    required: false
examples:
  - /aria {command} "task description"
  - /aria {command} SPEC-001 --format=pdf
---
```

**커맨드 구현 패턴:**

1. **brief**: 작업 이해 및 범위 정의
   - 사용자 질문으로 명확성 확보
   - 실행 계획 생성
   - 승인 요청

2. **execute**: 워크플로우 실행
   - 에이전트 협업 조율
   - 진행 상황 보고
   - 오류 처리 및 복구

3. **deliver**: 최종 산출물 배포
   - 품질 검증
   - 형식 변환
   - 배포 채널 전송

4. **template**: 템플릿 관리
   - 목록 표시
   - 검색
   - 미리보기

5. **knowledge**: 지식 베이스 관리
   - Notion 동기화
   - 검색
   - 태깅

### 3.4 MCP 통합 전략

**Context7 MCP:**

```python
# 사용 예시 (의사 코드)
library_id = resolve_library_id("FDA 21 CFR Part 820")
docs = get_library_docs(library_id, topics=["quality-system"])
```

**Sequential Thinking MCP:**

```python
# 사용 예시 (의사 코드)
analysis = sequential_thinking(
    prompt="Analyze regulatory pathway for medical device software",
    steps=5,
    context={"device_type": "SaMD", "market": "US", "EU"}
)
```

**Notion MCP:**

```python
# 사용 예시 (의사 코드)
notion.create_page(
    database_id="CAPA_TRACKER",
    properties={
        "title": "CAPA-001",
        "status": "Open",
        "priority": "High",
        "related_spec": "SPEC-ARIA-002"
    }
)
```

---

## 4. 위험 관리 (Risk Management)

### 4.1 잠재적 장애 요소

**위험 1: 에이전트 도구 권한 설정 오류**
- **확률**: Medium
- **영향**: High
- **완화**: permissionMode 매트릭스 문서화 및 검증
- **계획**: Phase 2.1 시작 전 권한 가이드라인 확정

**위험 2: MCP 서버 연결 불안정**
- **확률**: Medium
- **영향**: Medium
- **완화**: 폴백 메커니즘 구현, 로컬 캐시 활용
- **계획**: Phase 2.3에서 연결 안정성 테스트

**위험 3: 스킬 Progressive Disclosure 구현 복잡성**
- **확률**: High
- **영향**: Medium
- **완화**: 모듈 구조 템플릿 제공, 코드 예시 작성
- **계획**: Phase 2.1에서 기본 패턴 확립

**위험 4: 에이전트 간 협업 패턴 복잡성**
- **확률**: Medium
- **영향**: High
- **완화**: 협업 패턴 문서화, 시퀀스 다이어그램 작성
- **계획**: Phase 2.2에서 협업 테스트

**위험 5: 설정 파일 로드 순서 문제**
- **확률**: Low
- **영향**: Medium
- **완화**: 로드 순서 명시, 의존성 그래프 작성
- **계획**: Phase 2.1 시작 전 설정 구조 확정

### 4.2 완화 전략

**코드 품질:**
- 단위 테스트 커버리지 85%+ 목표
- 통합 테스트로 에이전트 협업 검증
- E2E 테스트로 워크플로우 검증

**문서화:**
- 모든 에이전트/스킬에 명확한 설명
- 협업 패턴 다이어그램
- MCP 통합 가이드

**테스트:**
- 각 Phase 완료 시 품질 게이트 통과
- 테스트 실패 시 해당 Phase 재작업

---

## 5. 품질 보증 (Quality Assurance)

### 5.1 TRUST 5 적용

**Tested:**
- 모든 에이전트 단위 테스트
- 스킬 기능 테스트
- 워크플로우 통합 테스트

**Readable:**
- 명확한 에이전트/스킬 이름
- 일관된 코드 스타일
- 포괄적인 주석

**Unified:**
- YAML 스키마 준수
- 일관된 파일 구조
- 표준화된 도구 사용

**Secured:**
- permissionMode 적용
- MCP 연결 보안
- 데이터 처리 보안

**Trackable:**
- Git 커밋 메시지 표준화
- 이슈 트래킹
- 변경 로그 유지

### 5.2 테스트 전략

**단위 테스트:**
- 각 에이전트별 기능 테스트
- 스킬별 메서드 테스트
- MCP 연결 테스트

**통합 테스트:**
- 에이전트 간 협업 테스트
- 워크플로우 단계 테스트
- MCP 데이터 흐름 테스트

**E2E 테스트:**
- Brief-Execute-Deliver 전체 흐름
- 실제 규제 문서 작성 시나리오
- 다중 에이전트 협업 시나리오

---

## 6. 성공 기준 (Success Criteria)

### 6.1 Phase 2.1 완료 기준

- [ ] manager-docs가 문서 생성 및 버전 관리를 수행
- [ ] manager-quality가 VALID 프레임워크로 품질 검증
- [ ] manager-project가 마일스톤 추적 및 진행 상황 보고
- [ ] aria-quality-valid 스킬이 5차원 검증 제공
- [ ] Core Layer 에이전트 간 기본 협업 작동

### 6.2 Phase 2.2 완료 기준

- [ ] expert-writer가 템플릿 기반 문서 작성
- [ ] expert-analyst가 데이터 분석 및 시각화 제공
- [ ] expert-reviewer가 규제 준수성 검토 및 피드백
- [ ] expert-researcher가 규제 정보 수집 및 인용
- [ ] aria-writing-style, aria-templates 스킬이 문서 품질 보장
- [ ] Brief-Execute-Deliver 워크플로우가 완전히 작동

### 6.3 Phase 2.3 완료 기준

- [ ] aria-research, aria-analysis 스킬이 방법론 제공
- [ ] Context7 MCP로 규제 문서 조회 가능
- [ ] Sequential Thinking MCP로 복잡한 분석 수행
- [ ] Notion MCP로 지식 베이스 동기화
- [ ] 전체 시스템이 실제 RA/QA 워크플로우 지원

---

## 7. 다음 단계 (Next Steps)

### 7.1 즉시 작업

1. **Spec 검토**: 이 SPEC 문서를 이해관계자가 검토
2. **우선순위 확정**: 각 Phase의 우선순위 및 일정 조정
3. **개발 환경 설정**: 필요한 도구 및 MCP 서버 설정

### 7.2 Phase 2.1 시작

1. **manager-docs 구현**: 문서 관리 에이전트 개발
2. **aria-quality-valid 구현**: VALID 프레임워크 스킬 개발
3. **기본 워크플로우 테스트**: Brief-Execute-Deliver 기본 흐름 검증

### 7.3 향후 계획

1. **Phase 2.2**: Business Layer 에이전트 및 스킬 개발
2. **Phase 2.3**: MCP 통합 및 고급 기능
3. **Phase 3**: RA/QA 전문 도메인 에이전트 (다음 SPEC)

---

**TAG BLOCK END**

**관련 문서:**
- spec.md - 요구사항 및 명세
- acceptance.md - 인수 조건 및 테스트 시나리오
