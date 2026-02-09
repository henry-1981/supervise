---
id: SPEC-ARIA-008
version: 1.0.0
status: Planned
created: 2025-02-09
updated: 2025-02-09
author: ARIA Development Team
priority: High
domain: aria-infrastructure
related-specs:
tags: infrastructure, environment-separation, testing, development-workflow
---

# SPEC-ARIA-008: ARIA 개발/테스트 환경 분리

## HISTORY

| 버전 | 날짜 | 변경사항 | 작성자 |
|------|------|----------|--------|
| 1.0.0 | 2025-02-09 | 초기 SPEC 작성 | ARIA Development Team |

---

## Environment

### 현재 상황

**ARIA 파일 구조:**
- `.claude/agents/aria/`: ARIA 에이전트 정의 (orchestrator, regulatory, clinical, risk, capa 등)
- `.claude/skills/aria/`: ARIA 스킬 정의 (analysis, brief, execute, deliver, knowledge, integration, templates 등)
- `.claude/commands/aria.md`: ARIA 명령어
- `.moai/config/aria.yaml`: ARIA 설정
- `CLAUDE.md`: ARIA 실행 지시어 (버전 3.0.0)

**MoAI-ADK 구조:**
- `.claude/hooks/moai/`: MoAI 훅 시스템
- `.claude/rules/moai/`: MoAI 규칙
- `.moai/config/`: MoAI 설정 (config.yaml, quality.yaml, language.yaml, workflow.yaml)

### 문제점

1. ARIA 스킬과 에이전트가 현재 메인 브랜치(main)에 이미 반영됨
2. Claude Code 시작 시 ARIA가 자동으로 로드됨
3. MoAI-ADK 개발 시 ARIA가 영향을 줄 수 있음
4. "순수 환경"에서 ARIA를 테스트하기 어려움

---

## Assumptions

### 기술적 가정

- [A1] Git 기반의 버전 관리 시스템을 사용함
- [A2] Claude Code가 `.claude/` 디렉토리 구조를 자동으로 로드함
- [A3] MoAI-ADK와 ARIA가 동일한 코드베이스에 존재함
- [A4] 사용자가 Git worktree 또는 branch 전환에 익숙함

### 비즈니스 가정

- [B1] ARIA는 MoAI-ADK와 독립적으로 개발되어야 함
- [B2] ARIA 테스트는 MoAI-ADK 없는 "순수 환경"에서 수행되어야 함
- [B3] 개발자는 두 환경 간에 자주 전환해야 함

---

## Requirements

### Wholes (전역 요구사항)

**EARS-001:** 시스템은 항상 ARIA 개발 환경과 MoAI-ADK 개발 환경을 완전히 분리해야 한다.

**EARS-002:** 시스템은 항상 Git history를 깔끔하게 유지해야 한다.

**EARS-003:** 시스템은 항상 두 환경 간 전환을 쉽게 지원해야 한다.

### Features (기능 요구사항)

**EARS-004 (Event-Driven):** WHEN 사용자가 ARIA 개발을 시작할 때, 시스템은 ARIA 개발 환경으로 전환해야 한다.

**EARS-005 (Event-Driven):** WHEN 사용자가 ARIA 테스트를 시작할 때, 시스템은 순수 Claude 환경(ARIA 미로드)으로 전환해야 한다.

**EARS-006 (Event-Driven):** WHEN 사용자가 MoAI-ADK 개발을 시작할 때, 시스템은 MoAI-ADK 환경으로 전환해야 한다.

**EARS-007 (State-Driven):** IF ARIA 브랜치에 있을 때, 시스템은 ARIA 관련 파일만 포함해야 한다.

**EARS-008 (State-Driven):** IF 순수 테스트 환경에 있을 때, 시스템은 ARIA 파일을 포함하지 않아야 한다.

### Goals (목표)

**EARS-009:** 시스템은 개발/테스트 환경 분리를 통해 MoAI-ADK 개발 시 ARIA의 영향을 받지 않아야 한다.

**EARS-010:** 시스템은 ARIA 기능 테스트 시 MoAI-ADK 개발 환경의 영향을 받지 않아야 한다.

**EARS-011:** 시스템은 환경 전환 시간을 최소화해야 한다 (목표: 30초 이내).

### Behaviors (동작 요구사항)

**EARS-012 (Event-Driven):** WHEN 환경 전환이 발생할 때, 시스템은 Claude Code 세션을 자동으로 재시작해야 한다.

**EARS-013 (Event-Driven):** WHEN Git worktree가 생성될 때, 시스템은 해당 worktree를 자동으로 설정해야 한다.

**EARS-014 (Unwanted):** 시스템은 환경 전환 시 데이터 손실을 일으키면 안 된다.

**EARS-015 (Unwanted):** 시스템은 Git history에 불필요한 merge commit을 생성하면 안 된다.

### Ideas (선택적 요구사항)

**EARS-016 (Optional):** WHERE 가능하면, 시스템은 환경 전환 스크립트를 제공해야 한다.

**EARS-017 (Optional):** WHERE 가능하면, 시스템은 환경 전환 상태를 시각적으로 표시해야 한다.

---

## Specifications

### 아키텍처 옵션 비교

| 옵션 | 장점 | 단점 | 복잡도 | 권장 |
|------|------|------|--------|------|
| **Git Worktree** | 완전한 격리, 동시 개발 가능, 빠른 전환 | 디스크 공간 2배 소요 | 중간 | ✅ 권장 |
| Feature Branch | 간단한 구현 | 브랜치 전환 필요, 동시 개발 불가 | 낮음 |
| Config Switching | 빠른 전환 | 불완전한 격리, 파일 로드 문제 | 낮음 |
| Docker/Container | 완전한 격리 | 높은 복잡도, 무거움 | 높음 |

### 권장 솔루션: Git Worktree 기반 환경 분리

**구조:**

```
agent-skills/                    # 메인 저장소 (MoAI-ADK)
├── .claude/                     # MoAI-ADK 설정
│   ├── agents/moai/
│   ├── skills/moai/
│   └── rules/moai/
├── .git/
└── ...                          # MoAI-ADK 소스

../agent-skills-aria-dev/        # Git Worktree 1 (ARIA 개발)
├── .claude/
│   ├── agents/aria/             # ARIA 에이전트
│   ├── skills/aria/             # ARIA 스킬
│   ├── commands/aria.md
│   └── rules/moai/              # MoAI-ADK 규칙 (공유)
├── CLAUDE.md                    # ARIA 실행 지시어
├── .moai/config/aria.yaml
└── ...

../agent-skills-pure-test/       # Git Worktree 2 (순수 테스트)
├── .claude/
│   ├── agents/                  # ARIA 없음
│   ├── skills/                  # ARIA 없음
│   └── rules/moai/              # MoAI-ADK 규칙만
├── CLAUDE.md                    # MoAI-ADK 실행 지시어만
└── ...
```

### 브랜치 전략

```
main (MoAI-ADK 메인)
├── aria/feature-*    (ARIA 기능 개발 브랜치)
├── aria/fix-*        (ARIA 버그 수정 브랜치)
└── aria/test-*       (ARIA 테스트 브랜치 - 순수 환경)
```

### 환경별 파일 포함 규칙

**ARIA 개발 환경 (aria/feature-*, aria/fix-*):**
- 포함: 모든 ARIA 파일 + MoAI-ADK 파일
- CLAUDE.md: ARIA 실행 지시어
- 목적: ARIA 기능 개발 및 테스트

**순수 테스트 환경 (aria/test-*):**
- 포함: MoAI-ADK 파일만
- 제외: 모든 ARIA 파일 (.claude/agents/aria/, .claude/skills/aria/, aria.md, aria.yaml)
- CLAUDE.md: MoAI-ADK 실행 지시어만
- 목적: ARIA 없는 "순수" 환경에서 ARIA 영향 테스트

**MoAI-ADK 개발 환경 (main):**
- 포함: MoAI-ADK 파일만
- 제외: 모든 ARIA 파일
- CLAUDE.md: MoAI-ADK 실행 지시어만
- 목적: MoAI-ADK 개발 (ARIA 영향 없음)

### 구현 세부사항

**1. Git Worktree 생성 스크립트:**

```bash
# ARIA 개발용 worktree
git worktree add ../agent-skills-aria-dev -b aria/feature-new-skill

# 순수 테스트용 worktree
git worktree add ../agent-skills-pure-test -b aria/test-pure-env
```

**2. 환경 전환 스크립트 (.moai/scripts/switch-env.sh):**

```bash
#!/bin/bash
ENV_NAME=$1
case $ENV_NAME in
  "aria-dev")
    cd ../agent-skills-aria-dev
    echo "Switched to ARIA Development Environment"
    ;;
  "pure-test")
    cd ../agent-skills-pure-test
    echo "Switched to Pure Test Environment"
    ;;
  "moai-main")
    cd ../agent-skills
    echo "Switched to MoAI-ADK Main Environment"
    ;;
  *)
    echo "Usage: switch-env [aria-dev|pure-test|moai-main]"
    ;;
esac
```

**3. .gitignore 규칙 (순수 테스트 환경):**

```
# ARIA files (순수 테스트 환경에서 제외)
.claude/agents/aria/
.claude/skills/aria/
.claude/commands/aria.md
.moai/config/aria.yaml
```

### 데이터 흐름

```
개발자 요청
    ↓
환경 선택 (aria-dev / pure-test / moai-main)
    ↓
Git worktree 전환
    ↓
Claude Code 세션 재시작
    ↓
환경별 파일 로드
    ↓
개발/테스트 작업 수행
    ↓
완료 시 메인 브랜치로 병합 (PR)
```

---

## Traceability

### 요구사항-설계 매핑

| 요구사항 | 설계 요소 | 검증 방법 |
|----------|----------|----------|
| EARS-001, EARS-007 | Git worktree 구조 | worktree 목록 확인 |
| EARS-002 | 브랜치 전략 | Git history 검증 |
| EARS-003 | 환경 전환 스크립트 | 스크립트 실행 테스트 |
| EARS-004 ~ EARS-006 | 환경별 파일 포함 규칙 | 파일 목록 검증 |
| EARS-011 | 전환 시간 측정 | 벤치마크 테스트 |
| EARS-014, EARS-015 | Git 전략 | merge commit 확인 |

### TAG 참조

- **SPEC-ARIA-008** 현재 문서
- **PLAN-ARIA-008** 구현 계획 (plan.md)
- **ACCEPT-ARIA-008** 인수 조건 (acceptance.md)
