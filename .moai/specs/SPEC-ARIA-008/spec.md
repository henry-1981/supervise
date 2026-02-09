---
id: SPEC-ARIA-008
version: 3.0.0
status: In Progress
created: 2025-02-09
updated: 2025-02-10
author: ARIA Development Team
priority: High
domain: aria-infrastructure
related-specs:
tags: infrastructure, environment-separation, development-workflow, branch-strategy, worktree
---

# SPEC-ARIA-008: ARIA 개발/테스트 환경 분리

## HISTORY

| 버전 | 날짜 | 변경사항 | 작성자 |
|------|------|----------|--------|
| 1.0.0 | 2025-02-09 | 초기 SPEC 작성 | ARIA Development Team |
| 2.0.0 | 2025-02-10 | 팀 분석 기반 대규모 업데이트: 치명적 결함 발견 및 신규 요구사항 추가 (EARS-018~022), 브랜치 전략 개선, 구현 우선순위 재정의 | ARIA Development Team |
| 3.0.0 | 2025-02-10 | 근본적 아키텍처 반전: Agent-Skills 프로젝트가 곧 ARIA 프로젝트이므로 main에 ARIA가 존재하는 것이 자연스럽다는 핵심 인사이트 반영. 3-환경(main/aria-dev/pure-test)에서 2-환경(main/moai-dev)으로 단순화. main에서 ~130개 ARIA 파일 제거 작업 제거(가장 큰 단순화). Rebase 불필요. Priority Critical에서 High로 하향 | ARIA Development Team |

---

## Environment

### 현재 상황 (v3.0.0 재평가)

**핵심 인사이트: Agent-Skills 프로젝트 = ARIA 프로젝트**

Agent-Skills 저장소는 ARIA 프로젝트 자체이다. 따라서 main 브랜치에 ARIA 파일이 존재하는 것은 문제가 아니라 올바른 상태이다. v2.0.0에서 "치명적 문제"로 분류했던 main 브랜치의 ARIA 파일 존재는 실제로는 자연스러운 상태였다.

**main 브랜치 현재 상태 (정상):**
- `.claude/agents/aria/`: 33개 ARIA 에이전트 파일 (정상)
- `.claude/skills/aria/`: ARIA 스킬 파일 (정상)
- `.claude/skills/aria-*/`: 23개 이상 ARIA 스킬 디렉토리 (정상)
- `.claude/commands/aria/`: ARIA 명령어 디렉토리 (정상)
- `.claude/agents/aria-workflow-guide.md`: ARIA 워크플로우 가이드 (정상)
- `.moai/config/aria.yaml`: ARIA 설정 파일 (정상)
- `CLAUDE.md`: "ARIA Execution Directive" (정상 - ARIA 프로젝트이므로)

**실제 문제 재정의:**
- MoAI-ADK 개발 시 ARIA 파일이 간섭하는 문제 (환경 분리 필요)
- MoAI-ADK 전용 개발 worktree가 필요함
- 기존 pure-test worktree는 불필요 (제거 대상)

**MoAI-ADK 구조 (정상):**
- `.claude/hooks/moai/`: MoAI 훅 시스템
- `.claude/rules/moai/`: MoAI 규칙
- `.moai/config/`: MoAI 설정 (config.yaml, quality.yaml, language.yaml, workflow.yaml)

### 목표 상태

**main 브랜치 (ARIA + MoAI-ADK 통합 환경) - PRIMARY:**
- 모든 ARIA 파일 + MoAI-ADK 파일 포함
- `CLAUDE.md`: ARIA Execution Directive
- 목적: ARIA 개발, ARIA 테스트, 통합 환경

**moai-dev worktree (MoAI-ADK 전용 환경) - DEVELOPMENT:**
- MoAI-ADK 파일만 포함 (ARIA 파일 배제)
- `CLAUDE.md`: MoAI Execution Directive
- 목적: MoAI-ADK 개발 (ARIA 간섭 없음)

---

## Assumptions

### 기술적 가정

- [A1] Git 기반의 버전 관리 시스템을 사용함
- [A2] Claude Code가 `.claude/` 디렉토리 구조를 자동으로 로드함
- [A3] MoAI-ADK와 ARIA가 동일한 코드베이스에 존재함
- [A4] 사용자가 Git worktree 또는 branch 전환에 익숙함
- [A5] (v3.0.0 수정) Agent-Skills 저장소 = ARIA 프로젝트이므로 main에 ARIA가 존재하는 것이 자연스러움
- [A6] (v3.0.0 수정) moai-dev worktree에서만 ARIA 파일 정리가 필요함 (main이 아님)
- [A7] switch-env.sh의 `cd` 명령은 서브셸에서 실행되므로 부모 셸의 디렉토리를 변경하지 못함

### 비즈니스 가정

- [B1] (v3.0.0 수정) ARIA는 main 브랜치에서 직접 개발됨 (main이 ARIA 프로젝트이므로)
- [B2] (v3.0.0 수정) MoAI-ADK 개발은 ARIA 간섭 없는 별도 worktree에서 수행되어야 함
- [B3] 개발자는 두 환경 간에 자주 전환해야 함
- [B4] (v3.0.0 수정) 병합 방향은 moai-dev -> main (단방향, MoAI-ADK 변경사항만)

---

## Requirements

### Wholes (전역 요구사항)

**EARS-001 (v3.0.0 재정의):** 시스템은 항상 ARIA 통합 환경(main)과 MoAI-ADK 전용 환경(moai-dev)을 분리해야 한다.

**EARS-002:** 시스템은 항상 Git history를 깔끔하게 유지해야 한다.

**EARS-003 (v3.0.0 단순화):** 시스템은 항상 main과 moai-dev 두 환경 간 전환을 쉽게 지원해야 한다.

### Features (기능 요구사항)

**EARS-006 (v3.0.0 재정의):** WHEN 사용자가 MoAI-ADK 개발을 시작할 때, 시스템은 moai-dev worktree로 전환해야 한다.

**EARS-007 (v3.0.0 재정의):** IF main 브랜치에 있을 때, 시스템은 ARIA + MoAI-ADK 모든 파일을 포함해야 한다.

### Goals (목표)

**EARS-009 (v3.0.0 재정의):** 시스템은 moai-dev worktree에서 MoAI-ADK 개발 시 ARIA의 영향을 받지 않아야 한다.

**EARS-011:** 시스템은 환경 전환 시간을 최소화해야 한다 (목표: 30초 이내).

### Behaviors (동작 요구사항)

**EARS-012 (v3.0.0 단순화):** WHEN 환경 전환이 발생할 때, 시스템은 Claude Code 세션을 재시작해야 한다.

**EARS-013 (v3.0.0 재정의):** WHEN moai-dev worktree가 생성될 때, 시스템은 ARIA 파일 정리를 자동으로 수행해야 한다.

**EARS-014:** 시스템은 환경 전환 시 데이터 손실을 일으키면 안 된다.

**EARS-015:** 시스템은 Git history에 불필요한 merge commit을 생성하면 안 된다.

### Ideas (선택적 요구사항)

**EARS-016:** WHERE 가능하면, 시스템은 환경 전환 스크립트를 제공해야 한다.

**EARS-017:** WHERE 가능하면, 시스템은 환경 전환 상태를 시각적으로 표시해야 한다.

### 유지된 요구사항 (v2.0.0에서 계승)

**EARS-018 (v3.0.0 재정의):** IF main 브랜치에 있을 때, CLAUDE.md는 ARIA Execution Directive를 포함해야 한다. IF moai-dev worktree에 있을 때, CLAUDE.md는 MoAI Execution Directive를 포함해야 한다.

**EARS-020 (v3.0.0 재정의):** 시스템은 항상 moai-dev worktree에서 ARIA 파일 정리 시 다음의 완전한 패턴 목록을 사용해야 한다:
- `.claude/agents/aria/` (디렉토리)
- `.claude/agents/aria-workflow-guide.md` (agents 루트의 독립 파일)
- `.claude/skills/aria/` (디렉토리, `aria-*` 패턴으로는 매칭되지 않음)
- `.claude/skills/aria-*/` (접두사가 있는 디렉토리들)
- `.claude/commands/aria/` (디렉토리) 및 `.claude/commands/aria.md` (단일 파일)
- `.claude/hooks/aria/` (디렉토리)
- `.moai/config/aria.yaml`

**EARS-021:** 시스템은 항상 worktree 경로의 대소문자를 통일해야 한다 (예: `Project/Agent-Skills` vs `project/agent-skills-*` 불일치 방지).

**EARS-022:** WHEN moai-dev worktree가 설정될 때, clean 스크립트는 멱등적(idempotent)으로 실행되어야 한다. 여러 번 실행해도 동일한 결과를 보장해야 한다.

### 신규 요구사항 (v3.0.0 추가)

**EARS-023 (Ubiquitous):** 시스템은 항상 main 브랜치에 ARIA + MoAI-ADK 모든 파일을 유지해야 한다. main은 ARIA 프로젝트의 통합 환경이다.

**EARS-024 (Ubiquitous):** 시스템은 항상 moai-dev -> main 단방향 병합 흐름을 유지해야 한다. MoAI-ADK 변경사항만 main으로 병합되며, ARIA 파일은 영향받지 않는다.

**EARS-025 (Event-Driven):** WHEN ARIA 기능 개발이 필요할 때, main 브랜치에서 직접 또는 aria/feature-* 단기 브랜치를 생성하여 main으로 병합해야 한다.

### 제거된 요구사항 (v3.0.0)

다음 요구사항은 아키텍처 반전으로 인해 더 이상 필요하지 않아 제거되었다:

| 제거된 요구사항 | 제거 사유 |
|----------------|----------|
| **EARS-004** (ARIA 개발 환경 전환) | ARIA 개발은 main에서 직접 수행, 별도 전환 불필요 |
| **EARS-005** (순수 테스트 환경 전환) | 순수 테스트 환경 제거 |
| **EARS-008** (순수 환경 ARIA 미포함) | 순수 테스트 환경 제거 |
| **EARS-010** (ARIA 테스트 독립성) | 별도 ARIA 테스트 환경 불필요 |
| **EARS-019** (main에서 ARIA 제거) | main에 ARIA가 존재하는 것이 정상 (가장 큰 단순화) |

---

## Specifications

### 아키텍처 (v3.0.0 - 2-환경 구조)

**핵심 원칙: "ARIA 프로젝트이므로 main에 ARIA가 있는 것이 자연스럽다"**

```
Agent-Skills/                       # 메인 저장소 (main 브랜치, ARIA + MoAI-ADK)
+-- .claude/
|   +-- agents/
|   |   +-- aria/                   # ARIA 에이전트 (33개)
|   |   +-- aria-workflow-guide.md  # ARIA 워크플로우 가이드
|   |   +-- moai/                   # MoAI-ADK 에이전트
|   +-- skills/
|   |   +-- aria/                   # ARIA 스킬 (디렉토리)
|   |   +-- aria-*/                 # ARIA 스킬 (접두사)
|   |   +-- moai-*/                 # MoAI-ADK 스킬
|   +-- commands/aria/              # ARIA 명령어
|   +-- hooks/
|   |   +-- aria/                   # ARIA 훅
|   |   +-- moai/                   # MoAI-ADK 훅
|   +-- rules/moai/                 # MoAI-ADK 규칙
+-- .moai/config/aria.yaml          # ARIA 설정
+-- CLAUDE.md                       # ARIA Execution Directive
+-- ...

../agent-skills-moai-dev/           # Git Worktree (moai/develop 브랜치)
+-- .claude/
|   +-- agents/moai/                # MoAI-ADK 에이전트만 (ARIA 없음)
|   +-- skills/moai-*/              # MoAI-ADK 스킬만 (ARIA 없음)
|   +-- hooks/moai/                 # MoAI-ADK 훅만
|   +-- rules/moai/                 # MoAI-ADK 규칙
+-- CLAUDE.md                       # MoAI Execution Directive
+-- ...                             # ARIA 파일 없음
```

### 브랜치 전략 (v3.0.0)

```
main (ARIA + MoAI-ADK, 통합 환경)
+-- aria/feature-* (ARIA 기능 개발, short-lived -> main)
+-- moai/develop worktree (MoAI-ADK만, ARIA 배제)
```

### 병합 흐름

```
moai/develop --> main  (MoAI-ADK 변경사항만, ARIA 파일 무영향)
aria/feature-* --> main  (ARIA 변경사항, PR 통해)
```

**핵심 차이 (v2.0.0 대비):**
- main에서 ARIA 파일 제거 불필요 (가장 큰 단순화)
- Rebase 불필요 (main이 항상 superset)
- 3-환경에서 2-환경으로 축소
- 순수 테스트 환경 제거
- `aria/develop` 장기 통합 브랜치 제거 (main이 통합 브랜치 역할)

### 환경별 파일 포함 규칙

| 환경 | ARIA 파일 | MoAI-ADK 파일 | CLAUDE.md | 목적 |
|------|----------|--------------|-----------|------|
| **main** | 모두 포함 | 모두 포함 | ARIA Execution Directive | ARIA 개발, 통합, 테스트 |
| **moai-dev** | 모두 제외 | 모두 포함 | MoAI Execution Directive | MoAI-ADK 개발 (ARIA 간섭 없음) |

### ARIA 파일 정리 패턴 (moai-dev 전용, EARS-020)

| 패턴 | 유형 | 비고 |
|------|------|------|
| `.claude/agents/aria/` | 디렉토리 | 33개 에이전트 파일 |
| `.claude/agents/aria-workflow-guide.md` | 단일 파일 | agents 루트의 독립 파일 |
| `.claude/skills/aria/` | 디렉토리 | `aria-*` glob으로 매칭 안됨 |
| `.claude/skills/aria-*/` | 디렉토리 | 23개 이상 스킬 디렉토리 |
| `.claude/commands/aria/` | 디렉토리 | 명령어 디렉토리 |
| `.claude/commands/aria.md` | 단일 파일 | 단일 명령어 파일 |
| `.claude/hooks/aria/` | 디렉토리 | 훅 디렉토리 |
| `.moai/config/aria.yaml` | 단일 파일 | ARIA 설정 |

### 구현 우선순위

| 우선순위 | 변경 내용 | 위험도 | 근거 |
|----------|----------|--------|------|
| 1 (높음) | moai-dev worktree 생성 및 ARIA 정리 | 낮음 | EARS-001, EARS-009 충족 |
| 2 (높음) | clean 스크립트 패턴 수정 (EARS-020 준수) | 낮음 | moai-dev의 ARIA 완전 제거 |
| 3 (높음) | moai-dev용 MoAI CLAUDE.md 생성 | 낮음 | EARS-018 충족 |
| 4 (중간) | pure-test worktree 제거 | 낮음 | 불필요 환경 정리 |
| 5 (중간) | switch-env.sh 2-환경 대응으로 수정 | 낮음 | EARS-003, EARS-016 |
| 6 (낮음) | SessionStart 환경 감지 훅 | 낮음 | EARS-012, EARS-017 |
| 7 (낮음) | 상태 관리 (.moai/state/environment.json) | 낮음 | 선택적 기능 |

### 데이터 흐름

```
개발자 요청
    |
    v
환경 선택 (main / moai-dev)
    |
    v
디렉토리 이동 (cd 또는 switch-env)
    |
    v
Claude Code 세션 시작/재시작
    |
    v
환경별 CLAUDE.md 로드 (ARIA 또는 MoAI)
    |
    v
개발 작업 수행
    |
    v
완료 시 병합:
  - MoAI-ADK 변경: moai/develop --> main (PR)
  - ARIA 변경: aria/feature-* --> main (PR) 또는 main 직접 커밋
```

---

## Traceability

### 요구사항-설계 매핑

| 요구사항 | 설계 요소 | 검증 방법 |
|----------|----------|----------|
| EARS-001 | 2-환경 worktree 구조 (main + moai-dev) | worktree 목록 확인 |
| EARS-002 | 단방향 병합 흐름 (moai-dev -> main) | Git history 검증 |
| EARS-003 | 환경 전환 스크립트 (2-환경) | 스크립트 실행 테스트 |
| EARS-006 | moai-dev worktree 전환 | worktree 전환 검증 |
| EARS-007 | main 브랜치 파일 포함 규칙 | 파일 목록 검증 |
| EARS-009 | moai-dev에서 ARIA 배제 | ARIA 파일 0개 확인 |
| EARS-011 | 전환 시간 측정 | 벤치마크 테스트 |
| EARS-014, EARS-015 | Git 전략 | merge commit 확인 |
| EARS-018 | CLAUDE.md 환경별 분화 (main=ARIA, moai-dev=MoAI) | 내용 비교 검증 |
| EARS-020 | 완전한 ARIA 패턴 목록 (moai-dev 정리용) | 패턴별 파일 존재 여부 검증 |
| EARS-021 | worktree 경로 대소문자 통일 | 경로 비교 |
| EARS-022 | 멱등적 clean 스크립트 | 2회 연속 실행 후 동일 결과 확인 |
| EARS-023 | main 브랜치 ARIA 유지 | main에서 ARIA 파일 존재 확인 |
| EARS-024 | 단방향 병합 흐름 | 병합 방향 검증 |
| EARS-025 | ARIA 기능 개발 흐름 | aria/feature-* -> main 병합 검증 |

### TAG 참조

- **SPEC-ARIA-008** 현재 문서
- **PLAN-ARIA-008** 구현 계획 (plan.md)
- **ACCEPT-ARIA-008** 인수 조건 (acceptance.md)
