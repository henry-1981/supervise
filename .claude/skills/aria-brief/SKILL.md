---
name: aria-brief
description: >
  ARIA Brief Phase skill for task understanding and scope definition.
  Analyzes user requests, identifies applicable regulations, collects
  necessary information, and creates actionable execution plans.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA orchestrator
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, phase, brief, planning, scope"
  author: "ARIA Phase 2 Implementation Team"

progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

triggers:
  keywords: ["brief", "understand", "scope", "plan", "task"]
  agents: ["orchestrator", "manager-docs", "expert-writer"]
  phases: ["brief"]
---

# ARIA Brief Phase Skill

## 개요 (Overview)

Brief Phase는 사용자의 요청을 분석하고 작업 범위를 정의하는 ARIA의 첫 단계입니다. 이 스킬은 다음을 제공합니다:

- 사용자 요청 분석 및 도메인 분류
- 적용 가능한 규제/표준 자동 매핑
- 정보 수집을 위한 구조화된 질문 (최대 4개)
- 실행 계획 수립 및 제시
- 사용자 승인 워크플로우

## Brief Phase 프로세스

```
1단계: 요청 분석 (Request Analysis)
   ├─ 도메인 식별 (FDA/EU MDR/MFDS)
   ├─ 작업 유형 분류 (문서 작성/검토/분석)
   └─ 복잡도 평가

2단계: 정보 수집 (Information Gathering)
   ├─ 필수 정보 파악
   ├─ 사용자 질의 (4개 이하)
   └─ 사용자 응답 통합

3단계: 규제 매핑 (Regulatory Mapping)
   ├─ 적용 규제 식별
   ├─ 적용 표준 식별
   └─ 선례 (precedents) 조회

4단계: 계획 수립 (Plan Creation)
   ├─ 에이전트 역할 할당
   ├─ 실행 단계 정의
   ├─ 예상 시간 및 리소스 추정
   └─ 리스크 식별

5단계: 사용자 승인 (User Approval)
   ├─ 계획 프레젠테이션
   ├─ 수정 옵션 제시
   └─ 최종 승인 획득
```

## 핵심 기능

### 1. 자동 도메인 분류

사용자 입력에서 다음을 자동 감지:

| 신호 | 도메인 | 예시 |
|------|--------|------|
| 510(k), PMA, De Novo | FDA (US) | "Prepare 510(k) for monitor" |
| CE, Technical File, MDR | EU MDR | "Prepare CE marking technical file" |
| MFDS, 품목허가, K-수출 | MFDS (Korea) | "의료기기 품목허가 준비" |
| ISO 13485, ISO 14971 | Quality/Risk | "Risk analysis per ISO 14971" |
| CAPA, Internal Audit | Quality | "Create CAPA for complaint trend" |

### 2. 구조화된 질문 (Max 4 Questions)

예시 질문 세트:

```
1. 장치 분류: Class I / II / III?
2. 대상 시장: US / EU / 기타?
3. 핵심 성능 지표: 어떤 규제 요구사항이 가장 중요?
4. 타임라인: 목표 제출 일자?
```

### 3. 실행 계획 템플릿

```yaml
Plan:
  ID: "BRIEF-{timestamp}"
  Task: "작업 제목"
  Status: "Pending User Approval"

  Regulations:
    - "FDA 21 CFR 820"
    - "ISO 13485:2016"

  Agents:
    - Role: expert-researcher
      Task: "규제 정보 수집"
      Owner: expert-researcher

    - Role: expert-writer
      Task: "문서 작성"
      Owner: expert-writer

    - Role: expert-reviewer
      Task: "규제 준수 검토"
      Owner: expert-reviewer

  Deliverables:
    - "Regulatory Pathway Document"
    - "Submission Checklist"
    - "Risk Assessment"

  EstimatedTime: "2-3 days"
  Risks:
    - "Missing documentation"
    - "Regulatory interpretation ambiguity"
```

## 인수 조건 (Acceptance Criteria)

### AC-CMD-001: 작업 이해

```gherkin
Given: 사용자가 새 작업을 시작
When: /aria brief 커맨드 실행
Then:
  ✅ 작업 목적이 명확해짐
  ✅ 범위가 정의됨
  ✅ 제약 조건이 식별됨
  ✅ 실행 계획이 제시됨
```

**성공 기준:**
- 작업 이해가 5분 이내에 완료
- 실행 계획이 실행 가능
- 명확성이 90% 이상 확보

### AC-CMD-002: 사용자 질의

```gherkin
Given: 작업 범위가 불명확
When: /aria brief가 명확성 확보
Then:
  ✅ 최대 4개 옵션의 질문 제시
  ✅ 질문이 명확함
  ✅ 사용자 선택 가능
  ✅ 선택 후 계획 업데이트
```

## 관련 문서

- `.moai/specs/SPEC-ARIA-002/plan.md` - Phase 정의
- `.moai/specs/SPEC-ARIA-002/acceptance.md` - 인수 조건
- `aria-templates` - 템플릿 가이드
- `aria-quality-valid` - VALID 프레임워크
