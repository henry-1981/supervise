---
spec_id: SPEC-ARIA-008
version: 3.0.0
created: 2025-02-09
updated: 2025-02-10
author: ARIA Development Team
status: In Progress
related-specs: SPEC-ARIA-008
tags: implementation-plan, git-worktree, environment-separation, architecture-inversion
---

# PLAN-ARIA-008: ARIA 개발/테스트 환경 분리 구현 계획

## HISTORY

| 버전 | 날짜 | 변경사항 | 작성자 |
|------|------|----------|--------|
| 1.0.0 | 2025-02-09 | 초기 계획 작성 | ARIA Development Team |
| 2.0.0 | 2025-02-10 | 팀 분석 기반 전면 개편: Phase 1 우선순위 재조정, Phase 1.5 신설, 스크립트 패턴 수정, Lessons Learned 추가 | ARIA Development Team |
| 3.0.0 | 2025-02-10 | 근본적 아키텍처 반전에 따른 전면 재작성. main=ARIA 유지, moai-dev worktree 생성으로 단순화. ~130개 ARIA 파일 제거 작업 제거. 3-환경에서 2-환경으로 축소. Rebase 불필요. 구현 복잡도 대폭 감소 | ARIA Development Team |

---

## 1. Milestones

### Primary Goal (필수 구현)

**Milestone 1: moai-dev worktree 생성 및 MoAI-ADK 전용 환경 구성**
- moai/develop 브랜치 기반 moai-dev worktree 생성
- clean 스크립트로 moai-dev에서 ARIA 파일 제거
- moai-dev용 MoAI Execution Directive CLAUDE.md 생성
- EARS-001, EARS-009, EARS-018, EARS-020 충족

**Milestone 2: clean 스크립트 수정 및 검증**
- clean-pure-env.sh를 clean-moai-dev.sh로 이름 변경 및 패턴 수정
- EARS-020의 완전한 패턴 목록 적용
- 멱등성 보장 (EARS-022)
- 잔여 ARIA 파일 자동 검증 단계 추가

### Secondary Goal (중요 구현)

**Milestone 3: 환경 정리 및 전환 스크립트**
- 기존 pure-test worktree 제거
- aria/test-pure-env 브랜치 제거
- switch-env.sh를 2-환경(main, moai-dev) 대응으로 수정
- source 기반 셸 함수로 전환 (A7 가정 해결)

### Optional Goal (선택적 구현)

**Milestone 4: 고급 자동화**
- SessionStart 환경 감지 훅 구현
- 상태 관리 (.moai/state/environment.json) 구현
- 환경 전환 상태 시각적 표시

---

## 2. Technical Approach

### 2.1 아키텍처 결정

**선택된 접근법: 2-환경 Git Worktree 기반 분리**

**근거:**
1. **프로젝트 자연 구조 준수:** Agent-Skills = ARIA 프로젝트이므로 main에 ARIA 유지
2. **단순화:** 3-환경에서 2-환경으로 축소, 구현 복잡도 대폭 감소
3. **안전성:** main에서 ~130개 파일 제거 불필요 (가장 위험한 작업 제거)
4. **병합 단순화:** Rebase 불필요, moai-dev -> main 단방향 병합
5. **완전한 격리:** moai-dev worktree에서 ARIA 간섭 없는 MoAI-ADK 개발 가능

### 2.2 기술 스택

**핵심 기술:**
- Git 2.19+ (worktree support)
- Bash 스크립팅 (환경 설정 자동화)
- Claude Code Hooks (세션 자동화, 선택적)

**의존성:**
- Git worktree 명령어
- .claude/ 디렉토리 구조 자동 로딩
- MoAI-ADK 스크립트 인프라

### 2.3 구현 순서 (v3.0.0)

#### Phase 1: moai-dev worktree 생성 (Priority: High)

**Task 1.1: moai-dev worktree 및 브랜치 생성**
- [ ] `git worktree add ../agent-skills-moai-dev -b moai/develop` 실행
- [ ] worktree 경로 대소문자 확인 (EARS-021)
- [ ] worktree 정상 생성 확인

**Task 1.2: moai-dev에서 ARIA 파일 정리**
- [ ] clean 스크립트 또는 수동으로 EARS-020 패턴의 모든 ARIA 파일 제거:
  - `.claude/agents/aria/` 디렉토리
  - `.claude/agents/aria-workflow-guide.md`
  - `.claude/skills/aria/` 디렉토리
  - `.claude/skills/aria-*/` 디렉토리들
  - `.claude/commands/aria/` 디렉토리
  - `.claude/commands/aria.md` (존재 시)
  - `.claude/hooks/aria/` 디렉토리
  - `.moai/config/aria.yaml`
- [ ] 제거 후 잔여 ARIA 파일 없음을 검증

**Task 1.3: moai-dev CLAUDE.md 생성**
- [ ] MoAI Execution Directive 내용의 CLAUDE.md 작성
- [ ] ARIA 관련 내용이 없음을 검증
- [ ] moai-dev worktree에 커밋

**Task 1.4: moai-dev 환경 검증**
- [ ] moai-dev worktree에서 ARIA 파일 0개 확인
- [ ] CLAUDE.md가 MoAI Execution Directive인지 확인
- [ ] MoAI-ADK 기능 정상 작동 확인

#### Phase 2: clean 스크립트 수정 (Priority: High)

**Task 2.1: clean-pure-env.sh -> clean-moai-dev.sh 이름 변경 및 패턴 수정**
- [ ] 스크립트 이름을 `clean-moai-dev.sh`로 변경 (목적 명확화)
- [ ] `aria-*` glob 패턴을 명시적 패턴 목록으로 변경
- [ ] `.claude/agents/aria-workflow-guide.md` 처리 추가
- [ ] `.claude/skills/aria/` 디렉토리 처리 추가 (dash 없는 패턴)
- [ ] `.claude/commands/aria/` 디렉토리 처리 추가
- [ ] 멱등성(idempotency) 보장: `rm -rf` 사용으로 존재하지 않는 경로에도 에러 없음
- [ ] 스크립트 실행 후 잔여 ARIA 파일 검증 단계 추가

**Task 2.2: CLAUDE.md 교체 로직 추가**
- [ ] clean-moai-dev.sh에 CLAUDE.md 교체 기능 포함
- [ ] MoAI Execution Directive 템플릿 참조
- [ ] ARIA CLAUDE.md 백업 (선택적)

#### Phase 3: 기존 환경 정리 및 전환 스크립트 (Priority: Medium)

**Task 3.1: pure-test worktree 제거**
- [ ] `git worktree remove ../agent-skills-pure-test` 실행 (또는 `--force`)
- [ ] worktree 정상 제거 확인

**Task 3.2: aria/test-pure-env 브랜치 제거**
- [ ] `git branch -D aria/test-pure-env` 실행
- [ ] 브랜치 제거 확인

**Task 3.3: aria/feature-env-setup 브랜치 정리 (선택적)**
- [ ] aria/feature-env-setup을 aria/develop 또는 main에 병합 후 제거
- [ ] 또는 더 이상 필요 없으면 직접 삭제

**Task 3.4: switch-env.sh 2-환경 대응 수정**
- [ ] 3-환경(aria-dev, pure-test, moai-main)에서 2-환경(main, moai-dev)으로 변경
- [ ] source 기반 셸 함수로 전환 (부모 셸 디렉토리 변경)
- [ ] 부모 셸의 디렉토리가 실제로 변경되는지 검증
- [ ] 사용법: `source .moai/scripts/switch-env.sh && switch-env moai-dev`

#### Phase 4: 고급 기능 (Priority: Low)

**Task 4.1: SessionStart 환경 감지 훅**
- [ ] 현재 worktree 경로 기반 환경 감지 로직 구현
- [ ] main worktree -> ARIA 환경 메시지
- [ ] moai-dev worktree -> MoAI-ADK 환경 메시지

**Task 4.2: 상태 관리**
- [ ] `.moai/state/environment.json` 구조 정의
- [ ] 환경 전환 시 자동 상태 저장
- [ ] 상태 조회 명령 구현

**Task 4.3: 환경 전환 상태 시각적 표시**
- [ ] 프롬프트 또는 StatusLine에 현재 환경 표시
- [ ] 환경별 색상 구분

---

## 3. Architecture Design

### 3.1 디렉토리 구조 (v3.0.0)

```
~/Project/
+-- Agent-Skills/                   # 메인 저장소 (main, ARIA + MoAI-ADK)
|   +-- .git/                       # Git 저장소
|   +-- .claude/
|   |   +-- agents/
|   |   |   +-- aria/               # ARIA 에이전트 (33개)
|   |   |   +-- aria-workflow-guide.md
|   |   |   +-- moai/               # MoAI-ADK 에이전트
|   |   +-- skills/
|   |   |   +-- aria/               # ARIA 스킬
|   |   |   +-- aria-*/             # ARIA 스킬 (접두사)
|   |   |   +-- moai-*/             # MoAI-ADK 스킬
|   |   +-- commands/
|   |   |   +-- aria/               # ARIA 명령어
|   |   |   +-- moai.md             # MoAI 명령어
|   |   +-- hooks/
|   |   |   +-- aria/               # ARIA 훅
|   |   |   +-- moai/               # MoAI 훅
|   |   +-- rules/moai/             # MoAI-ADK 규칙
|   +-- .moai/
|   |   +-- config/aria.yaml        # ARIA 설정
|   |   +-- specs/SPEC-ARIA-008/    # 현재 SPEC
|   +-- CLAUDE.md                   # ARIA Execution Directive
|
+-- agent-skills-moai-dev/          # Git Worktree (moai/develop 브랜치)
    +-- .git                        # Worktree 링크
    +-- .claude/
    |   +-- agents/moai/            # MoAI-ADK 에이전트만
    |   +-- skills/moai-*/          # MoAI-ADK 스킬만
    |   +-- hooks/moai/             # MoAI-ADK 훅만
    |   +-- rules/moai/             # MoAI-ADK 규칙
    +-- .moai/
    |   +-- config/                 # MoAI 설정만 (aria.yaml 없음)
    +-- CLAUDE.md                   # MoAI Execution Directive
```

### 3.2 Git 브랜치 전략 (v3.0.0)

```
main (ARIA + MoAI-ADK, 통합 환경, PRIMARY)
|
+-- aria/feature-*                  # ARIA 기능 개발 (short-lived -> main)
|
+-- moai/develop                    # MoAI-ADK 전용 (worktree로 연결)
```

**병합 규칙 (v3.0.0):**
1. `aria/feature-*` -> `main`: PR 또는 직접 병합
2. `moai/develop` -> `main`: PR 필수, MoAI-ADK 변경사항만 (ARIA 파일 무영향)
3. main에서 ARIA 관련 직접 커밋: 허용 (ARIA 프로젝트이므로)
4. moai-dev에서 ARIA 파일 추가: 금지 (clean 스크립트로 방지)

---

## 4. Risk Analysis

### 4.1 리스크 식별 (v3.0.0)

| 리스크 | 확률 | 영향 | 점수 | 상태 | 완화 전략 |
|--------|------|------|------|------|----------|
| **moai-dev clean 스크립트 ARIA 누락** | 중간 | 높음 | 6 | 미발현 | EARS-020 완전 패턴 + 검증 단계 |
| **moai-dev -> main 병합 시 ARIA 삭제 유입** | 낮음 | 높음 | 5 | 미발현 | PR 리뷰에서 ARIA 파일 변경 확인 |
| **moai-dev CLAUDE.md가 ARIA 버전으로 덮어쓰기** | 낮음 | 중간 | 3 | 미발현 | 병합 시 CLAUDE.md 충돌 해결 주의 |
| **switch-env.sh 서브셸 제한** | 확인됨 | 중간 | 5 | 발현 | source 기반 함수로 전환 |
| **디스크 공간 부족** | 낮음 | 중간 | 3 | 미발현 | worktree 1개만 필요 (v2.0.0의 2개에서 감소) |
| **경로 대소문자 불일치** | 확인됨 | 낮음 | 3 | 발현 | EARS-021로 표준화 |

**리스크 프로파일 비교 (v2.0.0 vs v3.0.0):**

| 항목 | v2.0.0 | v3.0.0 | 변화 |
|------|--------|--------|------|
| 전체 리스크 수 | 10개 | 6개 | 40% 감소 |
| Critical 리스크 | 4개 | 0개 | 완전 제거 |
| 최대 리스크 점수 | 10 | 6 | 40% 감소 |
| 발현된 리스크 | 5개 | 2개 | 60% 감소 |

**제거된 리스크 (v3.0.0):**
- main에 ARIA 파일 잔존 (점수 10): main에 ARIA가 있는 것이 정상
- CLAUDE.md 미분화 (점수 8): main의 ARIA CLAUDE.md가 정상
- Rebase 충돌 (점수 5): Rebase 불필요
- worktree 브랜치 동기화 지연 (점수 6): 2개 worktree 동기화 불필요

---

## 5. Implementation Tasks (통합 우선순위 목록)

| # | 우선순위 | Task | Phase | 위험도 | 상태 |
|---|----------|------|-------|--------|------|
| 1 | High | moai-dev worktree 및 moai/develop 브랜치 생성 | 1 | 낮음 | 미완료 |
| 2 | High | moai-dev에서 ARIA 파일 정리 (EARS-020 패턴) | 1 | 낮음 | 미완료 |
| 3 | High | moai-dev MoAI CLAUDE.md 생성 | 1 | 낮음 | 미완료 |
| 4 | High | clean-pure-env.sh -> clean-moai-dev.sh 이름 변경 및 패턴 수정 | 2 | 낮음 | 미완료 |
| 5 | Medium | pure-test worktree 제거 | 3 | 낮음 | 미완료 |
| 6 | Medium | aria/test-pure-env 브랜치 제거 | 3 | 낮음 | 미완료 |
| 7 | Medium | switch-env.sh 2-환경 대응 수정 (source 기반) | 3 | 낮음 | 미완료 |
| 8 | Low | SessionStart 환경 감지 훅 | 4 | 낮음 | 미완료 |
| 9 | Low | 상태 관리 (.moai/state/environment.json) | 4 | 낮음 | 미완료 |

---

## 6. Success Metrics

### 정량적 지표

- **moai-dev ARIA 파일 수:** 0개 (필수)
- **main ARIA 파일 수:** 현재 유지 (필수, 제거하면 안 됨)
- **CLAUDE.md 정확도:** 환경별 100% 일치 (main=ARIA, moai-dev=MoAI)
- **환경 전환 시간:** 30초 이내 (목표)
- **worktree 수:** 2개 (main + moai-dev)
- **Git 병합 충돌:** 월 1회 이하
- **clean 스크립트 패턴 커버리지:** 100% (EARS-020 완전 준수)

### 정성적 지표

- **사용자 만족도:** 환경 전환 용이성 만족
- **개발 생산성:** MoAI-ADK 개발 시 ARIA 영향 없음
- **아키텍처 자연스러움:** 프로젝트 구조와 환경 구조가 일치
- **유지보수 용이성:** 2-환경 관리가 3-환경 대비 단순

---

## 7. Rollout Plan (v3.0.0)

### Phase 1: moai-dev 환경 구성

1. moai-dev worktree 생성 (`git worktree add`)
2. ARIA 파일 정리 (EARS-020 패턴)
3. MoAI CLAUDE.md 생성
4. 환경 검증

### Phase 2: clean 스크립트 수정

1. clean-moai-dev.sh 생성 (패턴 수정)
2. 멱등성 검증
3. 잔여 파일 자동 검증 포함

### Phase 3: 기존 환경 정리

1. pure-test worktree 제거
2. aria/test-pure-env 브랜치 제거
3. switch-env.sh 2-환경 수정

### Phase 4: 고급 기능 (선택적)

1. SessionStart 훅
2. 상태 관리
3. 시각적 환경 표시

---

## 8. Lessons Learned

### v2.0.0에서의 교훈 (계승)

**1. Glob 패턴은 명시적으로 검증해야 한다**
- `aria-*` 패턴이 `aria/` 디렉토리를 매칭하지 못하는 문제가 발생
- 교훈: 스크립트의 패턴은 실제 파일 구조에 대해 반드시 테스트해야 함
- 권장: 패턴 기반 삭제 후 잔여 파일 검증 단계를 필수로 포함

**2. CLAUDE.md는 환경의 핵심 식별자이다**
- CLAUDE.md 내용이 Claude Code의 전체 동작을 결정함
- 교훈: 환경 분리 시 CLAUDE.md 분화가 가장 먼저 이루어져야 함
- 권장: CLAUDE.md 내용 검증을 모든 환경 전환 스크립트에 포함

**3. 서브셸의 `cd`는 부모 셸에 영향을 주지 않는다**
- switch-env.sh 스크립트의 `cd` 명령이 실제로 사용자의 셸 디렉토리를 변경하지 못함
- 교훈: 셸 스크립트 실행 방식(source vs 직접 실행)에 따른 동작 차이를 이해해야 함
- 권장: 디렉토리 변경이 필요한 스크립트는 셸 함수로 구현하고 `source`로 로드

### v3.0.0에서의 교훈 (신규)

**4. 프로젝트의 자연스러운 구조를 따라야 한다**
- Agent-Skills 저장소가 곧 ARIA 프로젝트인데, main에서 ARIA를 제거하려 한 것은 부자연스러운 접근이었음
- 교훈: "프로젝트가 무엇인가"에서 출발하여 환경 구조를 설계해야 함
- 영향: ~130개 파일 제거 작업이 완전히 제거되어 구현 복잡도가 극적으로 감소

**5. 가장 큰 리스크를 제거하는 것이 최선의 완화 전략이다**
- v2.0.0의 Critical 리스크 4개 중 3개가 "main에서 ARIA 제거"에서 파생됨
- 교훈: 리스크를 완화하기보다 리스크의 원인 자체를 제거하는 것이 더 효과적
- 영향: 전체 리스크 점수가 40% 감소, Critical 리스크 0개

**6. 환경 수를 최소화하면 관리 복잡도가 비례적으로 감소한다**
- 3-환경에서 2-환경으로 축소한 것만으로도 Task 수, 리스크 수, 검증 항목이 대폭 감소
- 교훈: "필요 최소한의 환경"을 유지하는 것이 장기 유지보수에 유리
- 영향: 구현 Task 11개에서 9개로 감소, 리스크 10개에서 6개로 감소

---

## Traceability

### SPEC-ARIA-008 연계

- **EARS-001:** 2-환경 worktree 구조로 main/moai-dev 분리
- **EARS-002:** 단방향 병합 흐름 (moai-dev -> main)으로 Git history 깔끔 유지
- **EARS-003:** 환경 전환 셸 함수(source 기반)로 2-환경 간 쉬운 전환 지원
- **EARS-009:** moai-dev worktree에서 ARIA 배제로 MoAI-ADK 개발 독립성 보장
- **EARS-011:** 디렉토리 이동만으로 30초 이내 전환 목표
- **EARS-018:** CLAUDE.md 환경별 분화 (main=ARIA, moai-dev=MoAI)
- **EARS-020:** 완전한 ARIA 파일 패턴 목록 (moai-dev 정리용)
- **EARS-021:** worktree 경로 대소문자 통일
- **EARS-022:** 멱등적 clean-moai-dev.sh
- **EARS-023:** main 브랜치 ARIA + MoAI-ADK 유지
- **EARS-024:** moai-dev -> main 단방향 병합
- **EARS-025:** ARIA 기능 개발은 main 직접 또는 aria/feature-* -> main

### TAG 참조

- **SPEC-ARIA-008:** 요구사항 정의
- **PLAN-ARIA-008:** 현재 문서 (구현 계획)
- **ACCEPT-ARIA-008:** 인수 조건 (acceptance.md)
