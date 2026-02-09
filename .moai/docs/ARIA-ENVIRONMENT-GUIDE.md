# ARIA 환경 분리 가이드

## 개요

이 가이드는 ARIA 개발/테스트 환경을 MoAI-ADK 메인 환경과 분리하여 관리하는 방법을 설명합니다.

## 환경 구조

### 1. MoAI-ADK Main Environment
- **경로:** `~/Project/Agent-Skills/`
- **브랜치:** `main`
- **ARIA 파일:** 없음
- **목적:** MoAI-ADK 코어 개발

### 2. ARIA Development Environment
- **경로:** `~/Project/agent-skills-aria-dev/`
- **브랜치:** `aria/feature-env-setup`
- **ARIA 파일:** 모든 ARIA 파일 포함
- **목적:** ARIA 기능 개발

### 3. Pure Test Environment
- **경로:** `~/Project/agent-skills-pure-test/`
- **브랜치:** `aria/test-pure-env`
- **ARIA 파일:** 제외됨
- **목적:** ARIA 없는 "순수" 환경에서 ARIA 영향 테스트

## 초기 설정

### Step 1: Worktree 생성

```bash
# 모든 worktree 생성
.moai/scripts/create-worktree.sh all
```

이 명령은 다음을 수행합니다:
- `../agent-skills-aria-dev/` 디렉토리 생성
- `../agent-skills-pure-test/` 디렉토리 생성
- 각각에 해당 Git 브랜치 생성

### Step 2: Pure Test 환경 정리

```bash
# Pure test 환경에서 ARIA 파일 제거
.moai/scripts/clean-pure-env.sh
```

### Step 3: Worktree 확인

```bash
git worktree list
```

출력 예시:
```
/Users/hb/Project/Agent-Skills            2562078 [main]
/Users/hb/project/agent-skills-aria-dev   2562078 [aria/feature-env-setup]
/Users/hb/project/agent-skills-pure-test  2562078 [aria/test-pure-env]
```

## 일일 사용

### ARIA 개발

```bash
# ARIA 개발 환경으로 전환
.moai/scripts/switch-env.sh aria-dev

# Claude Code 시작
cd ~/Project/agent-skills-aria-dev
claude
```

### 순수 테스트

```bash
# 순수 테스트 환경으로 전환
.moai/scripts/switch-env.sh pure-test

# Claude Code 시작
cd ~/Project/agent-skills-pure-test
claude
```

### MoAI-ADK 개발

```bash
# MoAI-ADK 메인 환경으로 전환
.moai/scripts/switch-env.sh moai-main

# Claude Code 시작
cd ~/Project/Agent-Skills
claude
```

## 환경별 파일 포함 규칙

| 환경 | ARIA 에이전트 | ARIA 스킬 | ARIA 명령어 | ARIA 설정 | CLAUDE.md |
|------|--------------|-----------|-----------|----------|-----------|
| **MoAI-ADK Main** | ❌ | ❌ | ❌ | ❌ | MoAI-ADK |
| **ARIA 개발** | ✅ | ✅ | ✅ | ✅ | ARIA |
| **순수 테스트** | ❌ | ❌ | ❌ | ❌ | MoAI-ADK |

## Git 브랜치 전략

```
main (MoAI-ADK)
├── aria/feature-env-setup    # 환경 설정
├── aria/feature-*            # ARIA 기능 개발
├── aria/fix-*                # ARIA 버그 수정
└── aria/test-*               # ARIA 테스트 (순수 환경)
```

## 스크립트 참조

### create-worktree.sh
Git worktree를 생성합니다.

```bash
.moai/scripts/create-worktree.sh [aria-dev|pure-test|all]
```

### switch-env.sh
환경을 전환합니다.

```bash
.moai/scripts/switch-env.sh [aria-dev|pure-test|moai-main]
```

### clean-pure-env.sh
순수 테스트 환경에서 ARIA 파일을 제거합니다.

```bash
.moai/scripts/clean-pure-env.sh
```

## 유지 관리

### Worktree 정리

```bash
# 사용하지 않는 worktree 제거
git worktree prune

# 특정 worktree 제거
git worktree remove ../agent-skills-aria-dev
```

### 모든 Worktree 목록

```bash
git worktree list
```

## 문제 해결

### Issue: Worktree 디렉토리가 이미 존재

```bash
# 디렉토리 수동 제거
rm -rf ../agent-skills-aria-dev

# 재생성
.moai/scripts/create-worktree.sh aria-dev
```

### Issue: Claude Code가 새 환경을 로드하지 않음

```bash
# Claude Code 완전히 종료 후 재시작
cd ~/Project/agent-skills-aria-dev
claude
```

### Issue: Pure Test 환경에 ARIA 파일이 여전히 존재

```bash
# 정리 스크립트 실행
.moai/scripts/clean-pure-env.sh
```

## 이점

1. **완전한 격리:** 각 환경이 독립적인 working directory를 가짐
2. **동시 개발:** 여러 환경에서 동시 작업 가능
3. **빠른 전환:** 초 단위 환경 전환
4. **깔끔한 Git history:** 병합 커밋 없음, 명확한 브랜치 전략
5. **안전한 테스트:** 메인 개발에 영향 없이 ARIA 영향 테스트

## 참고 문서

- **SPEC-ARIA-008:** [환경 분리 사양](../specs/SPEC-ARIA-008/spec.md)
- **PLAN-ARIA-008:** [구현 계획](../specs/SPEC-ARIA-008/plan.md)
- **ACCEPT-ARIA-008:** [인수 조건](../specs/SPEC-ARIA-008/acceptance.md)

## 버전

버전: 1.0.0
최종 업데이트: 2026-02-09
