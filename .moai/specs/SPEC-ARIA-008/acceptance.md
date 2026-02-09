---
spec_id: SPEC-ARIA-008
version: 3.0.0
created: 2025-02-09
updated: 2025-02-10
author: ARIA Development Team
status: In Progress
related-specs: SPEC-ARIA-008, PLAN-ARIA-008
tags: acceptance-criteria, test-scenarios, quality-gates, environment-separation
---

# ACCEPT-ARIA-008: ARIA 개발/테스트 환경 분리 인수 조건

## HISTORY

| 버전 | 날짜 | 변경사항 | 작성자 |
|------|------|----------|--------|
| 1.0.0 | 2025-02-09 | 초기 인수 조건 작성 | ARIA Development Team |
| 2.0.0 | 2025-02-10 | 팀 분석 기반 대규모 업데이트: 실제 파일 구조 반영, 신규 시나리오 추가, 품질 게이트 강화, Definition of Done 재평가 | ARIA Development Team |
| 3.0.0 | 2025-02-10 | 아키텍처 반전에 따른 전면 재작성. 2-환경 구조(main + moai-dev) 기준. 순수 테스트 환경 관련 시나리오 제거. main=ARIA 유지 검증 추가. 품질 게이트 단순화 | ARIA Development Team |

---

## 1. Test Scenarios (Given-When-Then Format)

### Scenario 1: moai-dev 환경으로 전환 (ARIA 배제 확인)

**Given:** 사용자가 main 브랜치(ARIA + MoAI-ADK 통합 환경)에 있다

**When:** 사용자가 moai-dev worktree로 전환한다 (`cd ../agent-skills-moai-dev` 또는 `source .moai/scripts/switch-env.sh && switch-env moai-dev`)

**Then:**
- moai-dev worktree 디렉토리에 위치해야 한다
- EARS-020의 모든 ARIA 파일 패턴에 해당하는 파일이 존재하지 않아야 한다:
  - `.claude/agents/aria/` 디렉토리 없음
  - `.claude/agents/aria-workflow-guide.md` 파일 없음
  - `.claude/skills/aria/` 디렉토리 없음
  - `.claude/skills/aria-*/` 디렉토리 없음
  - `.claude/commands/aria/` 디렉토리 없음
  - `.claude/commands/aria.md` 파일 없음
  - `.claude/hooks/aria/` 디렉토리 없음
  - `.moai/config/aria.yaml` 파일 없음
- `CLAUDE.md`에 "MoAI Execution Directive"가 포함되어야 한다
- `CLAUDE.md`에 "ARIA Execution Directive"가 포함되지 않아야 한다
- MoAI-ADK 에이전트와 스킬은 정상 존재해야 한다

### Scenario 2: main 환경으로 복귀 (ARIA 존재 확인)

**Given:** 사용자가 moai-dev worktree에 있다

**When:** 사용자가 main worktree로 전환한다 (`cd ../Agent-Skills` 또는 `source .moai/scripts/switch-env.sh && switch-env main`)

**Then:**
- main 저장소 디렉토리에 위치해야 한다
- `.claude/agents/aria/` 디렉토리가 존재해야 한다 (33개 에이전트)
- `.claude/skills/aria/` 디렉토리가 존재해야 한다
- `.claude/skills/aria-*/` 디렉토리들이 존재해야 한다
- `.claude/commands/aria/` 디렉토리가 존재해야 한다
- `.moai/config/aria.yaml` 파일이 존재해야 한다
- `CLAUDE.md`에 "ARIA Execution Directive"가 포함되어야 한다
- Claude Code가 ARIA + MoAI-ADK 관련 에이전트와 스킬을 모두 로드해야 한다

### Scenario 3: moai-dev -> main MoAI-ADK 변경사항 병합

**Given:** 사용자가 moai-dev worktree에서 MoAI-ADK 관련 파일을 수정하고 커밋했다

**When:** moai/develop 브랜치에서 main으로 PR을 생성하고 병합한다

**Then:**
- MoAI-ADK 변경사항이 main에 정상 반영되어야 한다
- main 브랜치의 ARIA 파일이 변경되지 않아야 한다 (무영향)
- Git history에 불필요한 merge commit이 최소화되어야 한다
- CLAUDE.md는 main에서 여전히 "ARIA Execution Directive"여야 한다

### Scenario 4: ARIA 파일이 moai-dev 병합으로 삭제되지 않음

**Given:** moai-dev worktree에서 ARIA 파일이 제거된 상태로 커밋되어 있다

**When:** moai/develop -> main 병합이 수행된다

**Then:**
- main 브랜치의 ARIA 파일이 삭제되지 않아야 한다 (EARS-023)
- ARIA 에이전트, 스킬, 명령어, 훅, 설정이 모두 유지되어야 한다
- 병합은 MoAI-ADK 변경사항만 반영해야 한다

### Scenario 5: 환경 전환 시간 측정

**Given:** 사용자가 현재 환경에서 다른 환경으로 전환하려고 한다

**When:** 사용자가 환경 전환 명령을 실행하고 전환 시간을 측정한다

**Then:**
- 환경 전환이 30초 이내에 완료되어야 한다 (EARS-011)
- 전환 완료 후 Claude Code가 정상적으로 작동해야 한다
- 파일 손실이나 데이터 손실이 없어야 한다 (EARS-014)

### Scenario 6: 환경별 CLAUDE.md 일치 검증

**Given:** main과 moai-dev 두 환경이 존재한다

**When:** 각 환경의 CLAUDE.md 내용을 확인한다

**Then:**
- main의 CLAUDE.md: "ARIA Execution Directive" 포함 (EARS-018)
- moai-dev의 CLAUDE.md: "MoAI Execution Directive" 포함, "ARIA Execution Directive" 없음 (EARS-018)

### Scenario 7: clean-moai-dev.sh 멱등성 검증

**Given:** moai-dev worktree에서 clean-moai-dev.sh가 이미 실행된 상태이다

**When:** clean-moai-dev.sh를 다시 실행한다

**Then:**
- 에러 없이 정상 종료해야 한다 (exit code 0)
- 이미 존재하지 않는 파일/디렉토리 삭제 시 에러가 발생하지 않아야 한다
- 실행 결과가 이전 실행과 동일해야 한다 (EARS-022)
- 잔여 ARIA 파일이 0개임을 자동 검증해야 한다

---

## 2. Edge Cases

### Edge Case 1: 환경 전환 중 Claude Code 실행 중

**상황:** 사용자가 Claude Code 세션 중 환경을 전환하려고 한다

**예상 동작:**
- 시스템이 Claude Code 재시작을 안내해야 한다
- 재시작 전 현재 세션 저장을 권장해야 한다
- 재시작 후 새 환경이 적용되어야 한다

### Edge Case 2: moai-dev -> main 병합 시 ARIA 삭제 포함

**상황:** moai-dev에서 ARIA 파일이 삭제된 커밋이 main으로 병합되려고 한다

**예상 동작:**
- PR 리뷰에서 ARIA 파일 변경(삭제)이 감지되어야 한다
- 병합 전에 ARIA 파일 삭제가 포함되지 않도록 주의 안내
- 필요 시 `git checkout main -- .claude/agents/aria/` 등으로 복원 가능

### Edge Case 3: moai-dev CLAUDE.md가 ARIA 버전으로 덮어쓰기

**상황:** main에서 moai-dev로 merge/rebase 시 CLAUDE.md가 ARIA 버전으로 덮어쓰여진다

**예상 동작:**
- 충돌 해결 시 moai-dev의 MoAI CLAUDE.md를 유지해야 한다
- clean-moai-dev.sh에 CLAUDE.md 교체 로직이 포함되어 복원 가능
- 환경 감지 훅이 CLAUDE.md 불일치를 경고해야 한다

### Edge Case 4: 디스크 공간 부족

**상황:** moai-dev worktree를 생성할 디스크 공간이 부족하다

**예상 동작:**
- 시스템이 디스크 공간 부족을 알려야 한다
- v3.0.0에서는 worktree 1개만 필요하므로 v2.0.0 대비 디스크 사용량 감소
- sparse checkout 대안을 제시할 수 있다

### Edge Case 5: 네트워크 연결 없이 환경 전환

**상황:** 오프라인 상태에서 환경을 전환하려고 한다

**예상 동작:**
- Git worktree 전환은 로컬에서 작동해야 한다
- 네트워크 의존성이 없어야 한다
- 오프라인 상태에서도 모든 기능이 작동해야 한다

### Edge Case 6: worktree 경로 대소문자 불일치

**상황:** `Project/Agent-Skills` vs `project/agent-skills-moai-dev` 처럼 경로 대소문자가 다르다

**예상 동작:**
- switch-env 스크립트가 대소문자 일관성을 유지해야 한다 (EARS-021)
- 경로 불일치 시 경고 메시지를 출력해야 한다
- 새 worktree 생성 시 기존 경로의 대소문자를 따라야 한다

### Edge Case 7: clean-moai-dev.sh가 새 ARIA 파일을 놓침

**상황:** ARIA 개발 중 EARS-020 패턴에 포함되지 않은 새로운 위치에 ARIA 파일이 추가됨

**예상 동작:**
- 잔여 파일 검증 단계에서 `*aria*` 패턴으로 추가 파일을 감지해야 한다
- 감지된 파일 경로를 출력하여 EARS-020 패턴 업데이트를 안내해야 한다
- 스크립트가 실패하지 않되, 경고를 출력해야 한다

---

## 3. Quality Gates

### 품질 게이트 1: moai-dev ARIA 배제 검증

**목적:** moai-dev worktree에서 ARIA 파일이 완전히 제거되었는지 확인

**검증 항목:**
- [ ] EARS-020의 모든 패턴에 해당하는 파일이 moai-dev에 없는지
- [ ] `*aria*` 패턴으로 추가 검색 시 잔여 파일이 없는지
- [ ] CLAUDE.md가 MoAI Execution Directive인지

**통과 기준:**
- moai-dev worktree에서 ARIA 관련 파일/디렉토리 0개
- CLAUDE.md에 "ARIA" 키워드 없음

**검증 명령:**

```bash
# moai-dev worktree에서 실행
cd ../agent-skills-moai-dev

# EARS-020 패턴별 검증 (모두 존재하지 않아야 함)
test -d .claude/agents/aria && echo "FAIL" || echo "PASS"
test -f .claude/agents/aria-workflow-guide.md && echo "FAIL" || echo "PASS"
test -d .claude/skills/aria && echo "FAIL" || echo "PASS"
ls -d .claude/skills/aria-* 2>/dev/null | wc -l  # 0이어야 함
test -d .claude/commands/aria && echo "FAIL" || echo "PASS"
test -f .claude/commands/aria.md && echo "FAIL" || echo "PASS"
test -d .claude/hooks/aria && echo "FAIL" || echo "PASS"
test -f .moai/config/aria.yaml && echo "FAIL" || echo "PASS"

# 추가 검증: aria 키워드 포함 파일 (0이어야 함)
find .claude -path "*aria*" 2>/dev/null | wc -l

# CLAUDE.md 검증
grep -c "ARIA Execution Directive" CLAUDE.md  # 0이어야 함
grep -c "MoAI Execution Directive" CLAUDE.md  # 1 이상이어야 함
```

---

### 품질 게이트 2: main ARIA 유지 검증

**목적:** main 브랜치에서 ARIA 파일이 정상적으로 유지되는지 확인

**검증 항목:**
- [ ] `.claude/agents/aria/` 디렉토리가 존재하는지 (33개 에이전트)
- [ ] `.claude/skills/aria/` 디렉토리가 존재하는지
- [ ] `.claude/skills/aria-*/` 디렉토리들이 존재하는지
- [ ] `.moai/config/aria.yaml`이 존재하는지
- [ ] CLAUDE.md가 ARIA Execution Directive인지

**통과 기준:**
- main 브랜치에서 모든 ARIA 파일 정상 존재
- CLAUDE.md에 "ARIA Execution Directive" 포함

**검증 명령:**

```bash
# main worktree에서 실행
cd ../Agent-Skills

# ARIA 파일 존재 확인 (모두 존재해야 함)
test -d .claude/agents/aria && echo "PASS" || echo "FAIL"
test -d .claude/skills/aria && echo "PASS" || echo "FAIL"
ls -d .claude/skills/aria-* 2>/dev/null | wc -l  # 20 이상이어야 함
test -f .moai/config/aria.yaml && echo "PASS" || echo "FAIL"

# CLAUDE.md 검증
grep -c "ARIA Execution Directive" CLAUDE.md  # 1 이상이어야 함
```

---

### 품질 게이트 3: CLAUDE.md 분화 검증

**목적:** 각 환경의 CLAUDE.md가 올바른 내용을 가지고 있는지 확인

**검증 항목:**
- [ ] main: "ARIA Execution Directive" 포함
- [ ] moai-dev: "MoAI Execution Directive" 포함
- [ ] moai-dev: "ARIA Execution Directive" 없음

**통과 기준:**
- 모든 환경에서 CLAUDE.md 내용 기대값 100% 일치

**검증 명령:**

```bash
# main 검증
grep -c "ARIA Execution Directive" ../Agent-Skills/CLAUDE.md      # 1 이상
# moai-dev 검증
grep -c "MoAI Execution Directive" ../agent-skills-moai-dev/CLAUDE.md  # 1 이상
grep -c "ARIA Execution Directive" ../agent-skills-moai-dev/CLAUDE.md  # 0
```

---

### 품질 게이트 4: moai-dev -> main 병합 안전성

**목적:** moai-dev에서 main으로 병합 시 ARIA 파일이 영향받지 않는지 확인

**검증 항목:**
- [ ] 병합 후 main에서 ARIA 파일 수가 변하지 않았는지
- [ ] 병합 후 main의 CLAUDE.md가 여전히 ARIA Execution Directive인지
- [ ] MoAI-ADK 변경사항만 반영되었는지

**통과 기준:**
- 병합 전후 main의 ARIA 파일 수 동일
- CLAUDE.md 내용 변경 없음

**검증 명령:**

```bash
# 병합 전 ARIA 파일 수 기록
BEFORE=$(git ls-tree -r --name-only main | grep -E "^\.claude/(agents/aria/|agents/aria-|skills/aria/|skills/aria-|commands/aria|hooks/aria/)" | wc -l)

# 병합 수행
git merge moai/develop

# 병합 후 ARIA 파일 수 확인
AFTER=$(git ls-tree -r --name-only HEAD | grep -E "^\.claude/(agents/aria/|agents/aria-|skills/aria/|skills/aria-|commands/aria|hooks/aria/)" | wc -l)

# 비교
[ "$BEFORE" -eq "$AFTER" ] && echo "PASS" || echo "FAIL: ARIA files changed"
```

---

### 품질 게이트 5: 환경 전환 성능

**목적:** 환경 전환이 30초 이내에 완료되는지 확인

**검증 항목:**
- [ ] 평균 전환 시간이 30초 이내인지
- [ ] 전환 후 Claude Code가 정상 작동하는지
- [ ] 데이터 손실이 없는지

**통과 기준:**
- 평균 전환 시간 <= 30초
- 전환 실패율 0%

---

## 4. Definition of Done (v3.0.0)

**기능 완료 기준:**

- [ ] moai-dev worktree 생성 및 moai/develop 브랜치 설정됨
- [ ] moai-dev worktree에서 ARIA 파일 완전 제거됨 (EARS-020)
- [ ] moai-dev CLAUDE.md가 MoAI Execution Directive로 설정됨 (EARS-018)
- [ ] main 브랜치에 ARIA + MoAI-ADK 파일 모두 유지됨 (EARS-023)
- [ ] clean-moai-dev.sh 스크립트 작성 및 멱등성 검증됨 (EARS-022)
- [ ] 기존 pure-test worktree 제거됨
- [ ] aria/test-pure-env 브랜치 제거됨
- [ ] switch-env.sh가 2-환경(main, moai-dev) 대응으로 수정됨

**품질 기준:**

- [ ] 품질 게이트 1 통과 (moai-dev ARIA 배제)
- [ ] 품질 게이트 2 통과 (main ARIA 유지)
- [ ] 품질 게이트 3 통과 (CLAUDE.md 분화)
- [ ] 품질 게이트 4 통과 (병합 안전성)
- [ ] 품질 게이트 5 통과 (전환 성능 30초 이내)
- [ ] Edge case 테스트 통과

**문서화 기준:**

- [ ] 환경 전환 가이드 문서 작성
- [ ] 2-환경 구조 설명 문서 작성

**배포 기준:**

- [ ] 내부 파일럿 테스트 완료
- [ ] 환경 전환 정상 작동 확인
- [ ] 병합 흐름 검증 완료

---

## 5. Test Automation

### 환경 격리 검증 스크립트 (v3.0.0)

```bash
#!/bin/bash
# test_env_isolation.sh - v3.0.0 (2-환경 구조)

echo "=== Environment Isolation Test (v3.0.0) ==="

ARIA_PATTERNS=(
  ".claude/agents/aria"
  ".claude/agents/aria-workflow-guide.md"
  ".claude/skills/aria"
  ".claude/commands/aria"
  ".claude/commands/aria.md"
  ".claude/hooks/aria"
  ".moai/config/aria.yaml"
)

ARIA_GLOB_PATTERNS=(
  ".claude/skills/aria-*"
)

check_aria_absent() {
  local env_name=$1
  local env_path=$2
  local failed=0

  for pattern in "${ARIA_PATTERNS[@]}"; do
    if [ -e "$env_path/$pattern" ]; then
      echo "  FAIL: $pattern exists in $env_name"
      failed=1
    fi
  done

  for pattern in "${ARIA_GLOB_PATTERNS[@]}"; do
    local matches=$(ls -d "$env_path"/$pattern 2>/dev/null | wc -l)
    if [ "$matches" -gt 0 ]; then
      echo "  FAIL: $pattern matches found in $env_name ($matches)"
      failed=1
    fi
  done

  return $failed
}

check_aria_present() {
  local env_name=$1
  local env_path=$2
  local failed=0

  if [ ! -d "$env_path/.claude/agents/aria" ]; then
    echo "  FAIL: .claude/agents/aria/ missing in $env_name"
    failed=1
  fi

  if [ ! -d "$env_path/.claude/skills/aria" ]; then
    echo "  FAIL: .claude/skills/aria/ missing in $env_name"
    failed=1
  fi

  local skill_count=$(ls -d "$env_path"/.claude/skills/aria-* 2>/dev/null | wc -l)
  if [ "$skill_count" -lt 20 ]; then
    echo "  FAIL: Expected 20+ aria-* skill dirs, found $skill_count in $env_name"
    failed=1
  fi

  return $failed
}

check_claude_md() {
  local env_name=$1
  local env_path=$2
  local expected=$3  # "moai" or "aria"

  if [ "$expected" = "moai" ]; then
    if grep -q "ARIA Execution Directive" "$env_path/CLAUDE.md"; then
      echo "  FAIL: $env_name CLAUDE.md contains ARIA directive (expected MoAI)"
      return 1
    fi
    if ! grep -q "MoAI Execution Directive" "$env_path/CLAUDE.md"; then
      echo "  FAIL: $env_name CLAUDE.md missing MoAI directive"
      return 1
    fi
  elif [ "$expected" = "aria" ]; then
    if ! grep -q "ARIA Execution Directive" "$env_path/CLAUDE.md"; then
      echo "  FAIL: $env_name CLAUDE.md missing ARIA directive"
      return 1
    fi
  fi
  return 0
}

# Test 1: Main Environment (ARIA + MoAI-ADK)
echo ""
echo "[Test 1] Main (main branch - ARIA + MoAI-ADK)"
MAIN_PATH="../Agent-Skills"
if [ ! -d "$MAIN_PATH" ]; then
  MAIN_PATH="../agent-skills"
fi

if check_aria_present "main" "$MAIN_PATH" && check_claude_md "main" "$MAIN_PATH" "aria"; then
  echo "  PASS: Main correctly has ARIA + MoAI-ADK"
else
  echo "  FAIL: Main environment incorrect"
fi

# Test 2: MoAI-ADK Dev Environment (MoAI-ADK only)
echo ""
echo "[Test 2] moai-dev (moai/develop branch - MoAI-ADK only)"
MOAI_PATH="../agent-skills-moai-dev"

if [ ! -d "$MOAI_PATH" ]; then
  echo "  SKIP: moai-dev worktree not found at $MOAI_PATH"
else
  if check_aria_absent "moai-dev" "$MOAI_PATH" && check_claude_md "moai-dev" "$MOAI_PATH" "moai"; then
    echo "  PASS: moai-dev correctly has MoAI-ADK only"
  else
    echo "  FAIL: moai-dev has ARIA contamination"
  fi
fi

echo ""
echo "=== Test Complete ==="
```

### clean-moai-dev.sh 멱등성 테스트

```bash
#!/bin/bash
# test_idempotency.sh - v3.0.0

echo "=== Idempotency Test (v3.0.0) ==="

cd ../agent-skills-moai-dev || { echo "FAIL: moai-dev worktree not found"; exit 1; }

# 1차 실행
echo "[Run 1]"
bash .moai/scripts/clean-moai-dev.sh
exit1=$?

# 잔여 파일 확인
count1=$(find .claude -path "*aria*" 2>/dev/null | wc -l)
config1=$(test -f .moai/config/aria.yaml && echo 1 || echo 0)

# 2차 실행
echo "[Run 2]"
bash .moai/scripts/clean-moai-dev.sh
exit2=$?

# 잔여 파일 확인
count2=$(find .claude -path "*aria*" 2>/dev/null | wc -l)
config2=$(test -f .moai/config/aria.yaml && echo 1 || echo 0)

total1=$((count1 + config1))
total2=$((count2 + config2))

if [ "$exit1" -eq 0 ] && [ "$exit2" -eq 0 ] && [ "$total1" -eq 0 ] && [ "$total2" -eq 0 ]; then
  echo "PASS: Idempotent execution verified"
else
  echo "FAIL: exit1=$exit1 exit2=$exit2 aria_count1=$total1 aria_count2=$total2"
  exit 1
fi
```

### 병합 안전성 테스트

```bash
#!/bin/bash
# test_merge_safety.sh - v3.0.0

echo "=== Merge Safety Test (v3.0.0) ==="

cd ../Agent-Skills || { echo "FAIL: main worktree not found"; exit 1; }

# 병합 전 ARIA 파일 수 기록
BEFORE=$(git ls-tree -r --name-only HEAD | grep -cE "^\.claude/(agents/aria/|agents/aria-|skills/aria/|skills/aria-|commands/aria|hooks/aria/)")
BEFORE_CONFIG=$(git ls-tree -r --name-only HEAD | grep -cE "^\.moai/config/aria\.yaml$")
TOTAL_BEFORE=$((BEFORE + BEFORE_CONFIG))

echo "ARIA files before merge: $TOTAL_BEFORE"

# Dry-run 병합 테스트
echo "[Dry-run merge test]"
git merge --no-commit --no-ff moai/develop 2>/dev/null
MERGE_EXIT=$?

if [ "$MERGE_EXIT" -eq 0 ]; then
  # 병합 후 ARIA 파일 수 확인 (staged 상태)
  AFTER=$(git diff --cached --name-only | grep -cE "^\.claude/(agents/aria/|agents/aria-|skills/aria/|skills/aria-|commands/aria|hooks/aria/)")

  if [ "$AFTER" -eq 0 ]; then
    echo "PASS: No ARIA files affected by merge"
  else
    echo "FAIL: $AFTER ARIA files would be changed"
    git diff --cached --name-only | grep -E "aria"
  fi

  # 병합 취소
  git merge --abort
else
  echo "INFO: Merge conflict or no changes to merge"
  git merge --abort 2>/dev/null
fi

echo "=== Test Complete ==="
```

---

## 6. Success Metrics

### 정량적 지표 (v3.0.0)

| 지표 | 목표 | 비고 |
|------|------|------|
| moai-dev ARIA 파일 수 | 0개 | 필수 |
| main ARIA 파일 수 | 현재 유지 (~130개) | 필수 (제거 금지) |
| CLAUDE.md 환경별 일치율 | 100% | main=ARIA, moai-dev=MoAI |
| 환경 전환 시간 (평균) | <= 30초 | 목표 |
| worktree 수 | 2개 (main + moai-dev) | 목표 |
| clean 스크립트 패턴 커버리지 | 100% | EARS-020 완전 준수 |
| 병합 시 ARIA 파일 영향 | 0개 | 필수 |
| 환경 전환 실패율 | 0% | 목표 |

### 정성적 지표

| 지표 | 목표 |
|------|------|
| 사용자 만족도 | >= 80% |
| 아키텍처 자연스러움 | main=ARIA 프로젝트 구조와 일치 |
| 유지보수 용이성 | 2-환경으로 단순화 |
| 개발 생산성 | MoAI-ADK 개발 시 ARIA 간섭 없음 |

---

## Traceability

### SPEC-ARIA-008 연계

- **EARS-001:** 시나리오 1, 2로 2-환경 분리 검증
- **EARS-003:** 시나리오 5로 전환 시간 검증
- **EARS-009:** 시나리오 1, 품질 게이트 1로 moai-dev ARIA 배제 검증
- **EARS-011:** 시나리오 5, 품질 게이트 5로 전환 성능 검증
- **EARS-014:** 시나리오 5로 데이터 손실 방지 검증
- **EARS-018:** 시나리오 6, 품질 게이트 3으로 CLAUDE.md 분화 검증
- **EARS-020:** 시나리오 1, 7, 품질 게이트 1로 ARIA 패턴 완전성 검증
- **EARS-021:** Edge Case 6으로 경로 대소문자 검증
- **EARS-022:** 시나리오 7로 멱등성 검증
- **EARS-023:** 시나리오 2, 4, 품질 게이트 2로 main ARIA 유지 검증
- **EARS-024:** 시나리오 3, 4, 품질 게이트 4로 단방향 병합 검증

### TAG 참조

- **SPEC-ARIA-008:** 요구사항 정의
- **PLAN-ARIA-008:** 구현 계획
- **ACCEPT-ARIA-008:** 현재 문서 (인수 조건)
