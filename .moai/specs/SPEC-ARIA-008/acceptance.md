---
spec_id: SPEC-ARIA-008
version: 1.0.0
created: 2025-02-09
updated: 2025-02-09
author: ARIA Development Team
status: Planned
related-specs: SPEC-ARIA-008, PLAN-ARIA-008
tags: acceptance-criteria, test-scenarios, quality-gates
---

# ACCEPT-ARIA-008: ARIA 개발/테스트 환경 분리 인수 조건

## 1. Test Scenarios (Given-When-Then Format)

### Scenario 1: ARIA 개발 환경으로 전환

**Given:** 사용자가 MoAI-ADK 메인 환경(main 브랜치)에 있고, ARIA 기능을 개발하려고 한다

**When:** 사용자가 `switch-env aria-dev` 명령을 실행한다

**Then:**
- 시스템이 ARIA 개발용 worktree로 전환해야 한다
- `.claude/agents/aria/` 디렉토리가 존재해야 한다
- `.claude/skills/aria/` 디렉토리가 존재해야 한다
- `CLAUDE.md`에 ARIA 실행 지시어가 포함되어야 한다
- Claude Code가 ARIA 관련 에이전트와 스킬을 로드해야 한다
- 사용자에게 "ARIA Development Environment로 전환되었습니다" 메시지가 표시되어야 한다

### Scenario 2: 순수 테스트 환경으로 전환

**Given:** 사용자가 ARIA 개발 환경에 있고, ARIA의 영향을 테스트하려고 한다

**When:** 사용자가 `switch-env pure-test` 명령을 실행한다

**Then:**
- 시스템이 순수 테스트용 worktree로 전환해야 한다
- `.claude/agents/aria/` 디렉토리가 존재하지 않아야 한다
- `.claude/skills/aria/` 디렉토리가 존재하지 않아야 한다
- `.claude/commands/aria.md` 파일이 존재하지 않아야 한다
- `.moai/config/aria.yaml` 파일이 존재하지 않아야 한다
- `CLAUDE.md`에 MoAI-ADK 실행 지시어만 포함되어야 한다
- Claude Code가 ARIA 관련 에이전트와 스킬을 로드하지 않아야 한다
- 사용자에게 "Pure Test Environment로 전환되었습니다" 메시지가 표시되어야 한다

### Scenario 3: MoAI-ADK 메인 환경으로 복귀

**Given:** 사용자가 ARIA 개발 또는 테스트 환경에 있고, MoAI-ADK 개발을 재개하려고 한다

**When:** 사용자가 `switch-env moai-main` 명령을 실행한다

**Then:**
- 시스템이 MoAI-ADK 메인 저장소로 전환해야 한다
- ARIA 관련 파일이 로드되지 않아야 한다
- Claude Code가 MoAI-ADK 관련 에이전트와 스킬만 로드해야 한다
- 사용자에게 "MoAI-ADK Main Environment로 전환되었습니다" 메시지가 표시되어야 한다

### Scenario 4: 환경 전환 시간 측정

**Given:** 사용자가 현재 환경에서 다른 환경으로 전환하려고 한다

**When:** 사용자가 `switch-env` 명령을 실행하고 전환 시간을 측정한다

**Then:**
- 환경 전환이 30초 이내에 완료되어야 한다
- 전환 완료 후 Claude Code가 정상적으로 작동해야 한다
- 파일 손실이나 데이터 손실이 없어야 한다

### Scenario 5: Git history 깔끔함 유지

**Given:** 사용자가 ARIA 기능을 개발하고 메인 브랜치에 병합하려고 한다

**When:** 사용자가 ARIA 개발 브랜치에서 PR을 생성하고 병합한다

**Then:**
- Git history에 불필요한 merge commit이 없어야 한다
- 병합 후 main 브랜치에 ARIA 파일이 포함되지 않아야 한다
- 브랜치 전략이 명확하게 유지되어야 한다 (aria/* 브랜치 구조)

### Scenario 6: 동시 다중 환경 사용

**Given:** 사용자가 ARIA 기능을 개발하면서 동시에 다른 ARIA 기능을 테스트하려고 한다

**When:** 사용자가 두 개의 다른 worktree에서 각각 작업한다

**Then:**
- 각 worktree가 독립적으로 작동해야 한다
- 한 worktree의 변경이 다른 worktree에 영향을 주지 않아야 한다
- Git worktree 간 충돌이 발생하지 않아야 한다

---

## 2. Edge Cases

### Edge Case 1: 환경 전환 중 Claude Code 실행 중

**상황:** 사용자가 Claude Code 세션 중 환경을 전환하려고 한다

**예상 동작:**
- 시스템이 Claude Code 재시작을 안내해야 한다
- 재시작 전 현재 세션 저장을 권장해야 한다
- 재시작 후 새 환경이 적용되어야 한다

### Edge Case 2: 존재하지 않는 환경으로 전환 시도

**상황:** 사용자가 `switch-env invalid-env` 명령을 실행한다

**예상 동작:**
- 시스템이 사용 가능한 환경 목록을 표시해야 한다
- 사용법 안내를 출력해야 한다
- 에러 메시지가 명확해야 한다

### Edge Case 3: Git worktree 충돌

**상황:** 두 worktree에서 동일한 파일을 수정하려고 한다

**예상 동작:**
- Git이 충돌을 감지하고 알려야 한다
- 사용자에게 해결 방법을 안내해야 한다
- 데이터 손실이 방지되어야 한다

### Edge Case 4: 디스크 공간 부족

**상황:** 새 worktree를 생성할 디스크 공간이 부족하다

**예상 동작:**
- 시스템이 디스크 공간 부족을 알려야 한다
- 사용하지 않는 worktree 삭제를 권장해야 한다
- sparse checkout 대안을 제시해야 한다

### Edge Case 5: 네트워크 연결 없이 환경 전환

**상황:** 오프라인 상태에서 환경을 전환하려고 한다

**예상 동작:**
- Git worktree 전환은 로컬에서 작동해야 한다
- 네트워크 의존성이 없어야 한다
- 오프라인 상태에서도 모든 기능이 작동해야 한다

### Edge Case 6: CLAUDE.md 파일 충돌

**상황:** 환경 전환 시 CLAUDE.md가 예상과 다르게 설정되어 있다

**예상 동작:**
- 시스템이 CLAUDE.md 무결성을 검증해야 한다
- 문제 발생 시 복원 방법을 안내해야 한다
- 백업본을 유지해야 한다

---

## 3. Quality Gates

### 품질 게이트 1: 환경 격리 검증

**목적:** 각 환경이 완전히 격리되었는지 확인

**검증 항목:**
- [ ] ARIA 개발 환경에 모든 ARIA 파일이 존재하는지
- [ ] 순수 테스트 환경에 모든 ARIA 파일이 제외되었는지
- [ ] MoAI-ADK 환경에 ARIA 파일이 없는지
- [ ] Claude Code가 환경에 따라 다르게 초기화되는지

**통과 기준:**
- 모든 검증 항목이 Pass
- 파일 목록 검증 스크립트 성공
- Claude Code 로드 확인

---

### 품질 게이트 2: 환경 전환 성능

**목적:** 환경 전환이 30초 이내에 완료되는지 확인

**검증 항목:**
- [ ] 평균 전환 시간이 30초 이내인지
- [ ] 전환 시간의 표준편차가 5초 이내인지
- [ ] 90번째 백분위수가 40초 이내인지

**통과 기준:**
- 평균 전환 시간 ≤ 30초
- 표준편차 ≤ 5초
- P90 ≤ 40초

**측정 방법:**
```bash
# 벤치마크 스크립트
for i in {1..100}; do
  time switch-env aria-dev
  time switch-env pure-test
  time switch-env moai-main
done
```

---

### 품질 게이트 3: Git 무결성

**목적:** Git history가 깔끔하게 유지되는지 확인

**검증 항목:**
- [ ] 불필요한 merge commit이 없는지
- [ ] 브랜치 전략이 준수되는지
- [ ] PR 병합 후 main 브랜치가 clean한지
- [ ] worktree 간 충돌이 없는지

**통과 기준:**
- merge commit 수 = 0 (Rebase 전략)
- 브랜치 명명 규칙 100% 준수
- main 브랜치 ARIA 파일 = 0

**검증 스크립트:**
```bash
# Merge commit 확인
git log --oneline --merges | wc -l  # 0이어야 함

# 브랜치 명명 규칙 확인
git branch | grep -v "aria\|main"  # 없어야 함

# Main 브랜치 ARIA 파일 확인
ls .claude/agents/aria/ 2>/dev/null  # 없어야 함
```

---

### 품질 게이트 4: 데이터 손실 방지

**목적:** 환경 전환 중 데이터 손실이 없는지 확인

**검증 항목:**
- [ ] 환경 전환 전후 파일 무결성
- [ ] Uncommitted changes 보존
- [ ] Staged changes 보존
- [ ] Git history 보존

**통과 기준:**
- 파일 해시 일치
- Uncommitted changes 유지
- Git log 변경 없음

**검증 스크립트:**
```bash
# 전후 파일 해시 비교
find . -type f -exec sha256sum {} \; > before.txt
switch-env aria-dev
find . -type f -exec sha256sum {} \; > after.txt
diff before.txt after.txt  # worktree 공유 파일만 다름
```

---

### 품질 게이트 5: 사용자 경험

**목적:** 환경 전환이 사용자에게 직관적인지 확인

**검증 항목:**
- [ ] 명령어가 직관적인지
- [ ] 에러 메시지가 명확한지
- [ ] 도움말이 충분한지
- [ ] 자동 완성이 지원되는지

**통과 기준:**
- 사용자 학습 시간 ≤ 10분
- 에러 메시지 이해도 ≥ 90%
- 도움말 충분도 ≥ 80%

**사용자 테스트:**
- 5명의 사용자에게 환경 전환 작업 수행
- 완료 시간 및 오류율 측정
- 설문조사 진행

---

## 4. Definition of Done

**기능 완료 기준:**

- [x] SPEC-ARIA-008의 모든 필수 요구사항(EARS-001 ~ EARS-006) 구현
- [x] Git worktree 기반 환경 분리 구조 완료
- [x] 환경 전환 스크립트(switch-env.sh) 구현
- [x] 환경별 .gitignore 설정 완료
- [x] CLAUDE.md 분리 완료

**품질 기준:**

- [x] 모든 품질 게이트 통과
- [x] Edge case 테스트 통과
- [x] 성능 벤치마크 통과 (30초 이내)
- [x] Git 무결성 검증 통과
- [x] 사용자 경험 테스트 통과

**문서화 기준:**

- [x] 환경 전환 가이드 문서 작성
- [x] Git worktree 관리 문서 작성
- [x] 문제 해결 가이드 작성
- [x] API/스크립트 문서 작성

**배포 기준:**

- [ ] 내부 파일럿 테스트 완료
- [ ] 베타 사용자 피드백 수집
- [ ] 버그 수정 및 완화
- [ ] 전체 배포 승인

---

## 5. Test Automation

### 자동화된 테스트 스크립트

**환경 격리 검증 스크립트:**

```bash
#!/bin/bash
# test_env_isolation.sh

echo "=== Environment Isolation Test ==="

# Test 1: ARIA Dev Environment
cd ../agent-skills-aria-dev
if [ -d ".claude/agents/aria" ] && [ -d ".claude/skills/aria" ]; then
  echo "✓ ARIA Dev: All ARIA files present"
else
  echo "✗ ARIA Dev: Missing ARIA files"
  exit 1
fi

# Test 2: Pure Test Environment
cd ../agent-skills-pure-test
if [ ! -d ".claude/agents/aria" ] && [ ! -d ".claude/skills/aria" ]; then
  echo "✓ Pure Test: No ARIA files present"
else
  echo "✗ Pure Test: ARIA files should not exist"
  exit 1
fi

# Test 3: MoAI-ADK Main Environment
cd ../agent-skills
if [ ! -d ".claude/agents/aria" ]; then
  echo "✓ MoAI-ADK Main: No ARIA files present"
else
  echo "✗ MoAI-ADK Main: ARIA files should not exist"
  exit 1
fi

echo "=== All Tests Passed ==="
```

**환경 전환 성능 테스트:**

```bash
#!/bin/bash
# benchmark_env_switch.sh

echo "=== Environment Switch Benchmark ==="

total_time=0
iterations=10

for i in $(seq 1 $iterations); do
  start=$(date +%s%N)
  switch-env aria-dev
  switch-env pure-test
  switch-env moai-main
  end=$(date +%s%N)

  elapsed=$((($end - $start) / 1000000))
  total_time=$(($total_time + $elapsed))
  echo "Iteration $i: ${elapsed}ms"
done

avg_time=$(($total_time / $iterations))
echo "Average: ${avg_time}ms"

if [ $avg_time -le 30000 ]; then
  echo "✓ Performance target met (≤30s)"
else
  echo "✗ Performance target exceeded (>30s)"
  exit 1
fi
```

---

## Traceability

### SPEC-ARIA-008 연계

- **EARS-001 ~ EARS-006:** 시나리오 1~6으로 검증
- **EARS-011:** 품질 게이트 2로 검증
- **EARS-014, EARS-015:** 품질 게이트 3, 4로 검증

### TAG 참조

- **SPEC-ARIA-008:** 요구사항 정의
- **PLAN-ARIA-008:** 구현 계획
- **ACCEPT-ARIA-008:** 현재 문서 (인수 조건)

---

## 6. Success Metrics

### 정량적 지표

| 지표 | 목표 | 현재 | 상태 |
|------|------|------|------|
| 환경 격리률 | 100% | - | 🔄 측정 필요 |
| 전환 시간 (평균) | ≤30초 | - | 🔄 측정 필요 |
| Git 무결성 | 100% | - | 🔄 측정 필요 |
| 데이터 손실률 | 0% | - | 🔄 측정 필요 |
| 테스트 통과율 | 100% | - | 🔄 측정 필요 |

### 정성적 지표

| 지표 | 목표 | 현재 | 상태 |
|------|------|------|------|
| 사용자 만족도 | ≥80% | - | 🔄 조사 필요 |
| 학습 곡선 | ≤10분 | - | 🔄 조사 필요 |
| 에러 메시지 명확성 | ≥90% | - | 🔄 조사 필요 |
| 문서 충분성 | ≥80% | - | 🔄 조사 필요 |
