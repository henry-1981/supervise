---
spec_id: SPEC-ARIA-008
version: 1.0.0
created: 2025-02-09
updated: 2025-02-09
author: ARIA Development Team
status: Planned
related-specs: SPEC-ARIA-008
tags: implementation-plan, git-worktree, environment-separation
---

# PLAN-ARIA-008: ARIA 개발/테스트 환경 분리 구현 계획

## 1. Milestones

### Primary Goal (필수 구현)

**Milestone 1: Git Worktree 기반 환경 분리 기본 구조**
- Git worktree 생성 및 브랜치 전략 수립
- 환경별 파일 포함/제외 규칙 정의
- 기본 환경 전환 스크립트 구현

### Secondary Goal (중요 구현)

**Milestone 2: 환경 전환 자동화**
- 환경 전환 스크립트 개선
- Claude Code 세션 자동 재시작 후크
- 환경 상태 표시 기능

### Optional Goal (선택적 구현)

**Milestone 3: 고급 기능**
- 환경 전환 GUI 도구
- 자동화된 테스트 파이프라인
- 성능 모니터링

---

## 2. Technical Approach

### 2.1 아키텍처 결정

**선택된 접근법: Git Worktree 기반 환경 분리**

**근거:**
1. **완전한 격리:** 각 worktree는 독립된 working directory를 가짐
2. **동시 개발 지원:** 여러 worktree를 동시에 사용 가능
3. **빠른 전환:** 디렉토리 이동만으로 환경 전환 가능
4. **Git history 깔끔 유지:** 브랜치 전략으로 명확한 관리

### 2.2 기술 스택

**핵심 기술:**
- Git 2.19+ (worktree support)
- Bash 스크립팅 (환경 전환 자동화)
- Claude Code Hooks (세션 자동화)

**의존성:**
- Git worktree 명령어
- .claude/ 디렉토리 구조 자동 로딩
- MoAI-ADK 스크립트 인프라

### 2.3 구현 순서

#### Phase 1: 기반 구조 (Priority: High)

1. **브랜치 전략 수립**
   - 메인 브랜치: main (MoAI-ADK)
   - ARIA 개발 브랜치: aria/feature-*, aria/fix-*
   - 순수 테스트 브랜치: aria/test-*

2. **Git Worktree 생성**
   ```bash
   # ARIA 개발용 worktree
   git worktree add ../agent-skills-aria-dev -b aria/feature-env-setup

   # 순수 테스트용 worktree
   git worktree add ../agent-skills-pure-test -b aria/test-pure-env
   ```

3. **환경별 .gitignore 설정**
   - 순수 테스트 환경: ARIA 파일 제외
   - ARIA 개발 환경: 모든 파일 포함

4. **CLAUDE.md 분리**
   - 메인: MoAI-ADK 실행 지시어
   - ARIA 개발: ARIA 실행 지시어
   - 순수 테스트: MoAI-ADK 실행 지시어 (ARIA 제외)

#### Phase 2: 자동화 (Priority: Medium)

1. **환경 전환 스크립트**
   - `.moai/scripts/switch-env.sh` 생성
   - 인자: aria-dev, pure-test, moai-main
   - 기능: cd + Claude Code 재시작 안내

2. **Claude Code Hooks 통합**
   - SessionStart 훅: 현재 환경 감지
   - 상태 표시: 현재 worktree 이름 표시

3. **환경 상태 관리**
   - `.moai/state/current-env.json` 파일
   - 현재 환경, worktree 경로, 브랜치 이름 저장

#### Phase 3: 고급 기능 (Priority: Low)

1. **GUI 도구 (선택적)**
   - 환경 전환 메뉴
   - 시각적 상태 표시

2. **자동화된 테스트 파이프라인**
   - 순수 환경에서 ARIA 영향 테스트
   - ARIA 환경에서 기능 테스트

3. **성능 모니터링**
   - 전환 시간 측정
   - 디스크 사용량 모니터링

---

## 3. Architecture Design

### 3.1 디렉토리 구조

```
~/Projects/
├── agent-skills/                    # 메인 저장소 (main 브랜치)
│   ├── .git/                        # Git 저장소
│   ├── .claude/                     # MoAI-ADK 설정
│   ├── .moai/
│   │   └── scripts/
│   │       └── switch-env.sh        # 환경 전환 스크립트
│   └── CLAUDE.md                    # MoAI-ADK 실행 지시어
│
├── agent-skills-aria-dev/           # Git Worktree 1 (aria/* 브랜치)
│   ├── .git                         # Worktree 링크
│   ├── .claude/
│   │   ├── agents/                  # MoAI-ADK + ARIA 에이전트
│   │   │   ├── aria/                # ARIA 에이전트 (개발 중)
│   │   │   └── moai/                # MoAI-ADK 에이전트
│   │   ├── skills/
│   │   │   ├── aria/                # ARIA 스킬 (개발 중)
│   │   │   └── moai/                # MoAI-ADK 스킬
│   │   ├── commands/
│   │   │   ├── aria.md              # ARIA 명령어
│   │   │   └── moai.md              # MoAI-ADK 명령어
│   │   └── rules/
│   │       └── moai/                # MoAI-ADK 규칙
│   ├── .moai/
│   │   ├── config/
│   │   │   └── aria.yaml            # ARIA 설정
│   │   └── state/
│   │       └── current-env.json     # 환경 상태
│   └── CLAUDE.md                    # ARIA 실행 지시어
│
└── agent-skills-pure-test/          # Git Worktree 2 (aria/test-* 브랜치)
    ├── .git                         # Worktree 링크
    ├── .claude/
    │   ├── agents/                  # MoAI-ADK 에이전트만
    │   │   └── moai/                # ARIA 없음
    │   ├── skills/                  # MoAI-ADK 스킬만
    │   │   └── moai/                # ARIA 없음
    │   └── rules/
    │       └── moai/                # MoAI-ADK 규칙
    ├── .moai/
    │   └── state/
    │       └── current-env.json     # 환경 상태
    └── CLAUDE.md                    # MoAI-ADK 실행 지시어 (ARIA 제외)
```

### 3.2 환경별 파일 포함 규칙

| 환경 | ARIA 에이전트 | ARIA 스킬 | ARIA 명령어 | ARIA 설정 | CLAUDE.md |
|------|--------------|-----------|-----------|----------|-----------|
| **MoAI-ADK (main)** | ❌ | ❌ | ❌ | ❌ | MoAI-ADK |
| **ARIA 개발 (aria/*)** | ✅ | ✅ | ✅ | ✅ | ARIA |
| **순수 테스트 (aria/test-*)** | ❌ | ❌ | ❌ | ❌ | MoAI-ADK |

### 3.3 Git 브랜치 전략

```
main (MoAI-ADK)
│
├── aria/feature-env-setup        # M1: 기반 구조
├── aria/feature-new-skill        # M1: ARIA 스킬 개발
├── aria/fix-cli-bug              # M1: 버그 수정
├── aria/test-pure-env            # M2: 순수 환경 테스트
└── aria/automation               # M3: 자동화
```

**병합 규칙:**
1. aria/* 브랜치 → main: PR 생성 후 review
2. main 브랜치는 항상 clean (ARIA 없음)
3. aria/* 브랜치 간 직접 병합 지양

---

## 4. Risk Analysis

### 4.1 리스크 식별

| 리스크 | 확률 | 영향 | 점수 | 완화 전략 |
|--------|------|------|------|----------|
| **디스크 공간 부족** | 중간 | 높음 | 6 | worktree 정기 정리, sparse checkout 활용 |
| **환경 전환 복잡성** | 낮음 | 중간 | 3 | 스크립트 자동화, 문서화 |
| **Git history 복잡화** | 낮음 | 중간 | 3 | 명확한 브랜치 전략, PR template |
| **Claude Code 캐시 문제** | 중간 | 중간 | 4 | 세션 재시작 후크, 캐시 클리어 |
| **파일 동기화 문제** | 낮음 | 높음 | 4 | Git worktree 자동 동기화 |

### 4.2 완화 전략 상세

**R1: 디스크 공간 부족**
- **완화:** 사용하지 않는 worktree 정기 제거 (`git worktree prune`)
- **모니터링:** 디스크 사용량 알림
- **대안:** sparse checkout으로 필요한 파일만 checkout

**R2: 환경 전환 복잡성**
- **완화:** `switch-env.sh` 스크립트로 일관된 인터페이스 제공
- **문서화:** README.md에 환경 전환 가이드 추가
- **도구:** 환경 상태 표시 기능

**R3: Git history 복잡화**
- **완화:** 명확한 브랜치 명명 규칙 (aria/*)
- **PR template:** 병합 시 체크리스트 제공
- **정책:** main 브랜치 직접 커밋 금지

**R4: Claude Code 캐시 문제**
- **완화:** 환경 전환 시 Claude Code 재시작 안내
- **후크:** SessionStart 훅으로 캐시 클리어
- **검증:** 환경 변수 확인

**R5: 파일 동기화 문제**
- **완화:** Git worktree의 자동 동기화 활용
- **검증:** worktree 상태 확인 스크립트
- **백업:** 중요 작업 전 commit

---

## 5. Implementation Tasks

### Phase 1: 기반 구조 (Priority: High)

**Task 1.1:** 브랜치 전략 문서화
- [ ] 브랜치 명명 규칙 정의
- [ ] 병합 정책 수립
- [ ] PR template 작성

**Task 1.2:** Git Worktree 생성
- [ ] ARIA 개발용 worktree 생성
- [ ] 순수 테스트용 worktree 생성
- [ ] worktree 관리 문서 작성

**Task 1.3:** 환경별 .gitignore 설정
- [ ] 순수 테스트 환경용 .gitignore 작성
- [ ] ARIA 파일 제외 규칙 정의
- [ ] 검증 스크립트 작성

**Task 1.4:** CLAUDE.md 분리
- [ ] MoAI-ADK용 CLAUDE.md 작성 (main)
- [ ] ARIA용 CLAUDE.md 작성 (aria/*)
- [ ] 분리 규칙 문서화

### Phase 2: 자동화 (Priority: Medium)

**Task 2.1:** 환경 전환 스크립트
- [ ] switch-env.sh 기본 구현
- [ ] 인자 처리 (aria-dev, pure-test, moai-main)
- [ ] 에러 처리 및 사용법 출력

**Task 2.2:** Claude Code Hooks 통합
- [ ] SessionStart 훅 구현
- [ ] 환경 감지 로직
- [ ] 상태 표시 기능

**Task 2.3:** 환경 상태 관리
- [ ] current-env.json 구조 정의
- [ ] 상태 저장/로드 함수
- [ ] 상태 검증 스크립트

### Phase 3: 고급 기능 (Priority: Low)

**Task 3.1:** GUI 도구 (선택적)
- [ ] 환경 전환 메뉴 구현
- [ ] 시각적 상태 표시
- [ ] 단축키 지원

**Task 3.2:** 자동화된 테스트 파이프라인
- [ ] 순수 환경 테스트 스크립트
- [ ] ARIA 환경 테스트 스크립트
- [ ] CI/CD 통합

**Task 3.3:** 성능 모니터링
- [ ] 전환 시간 측정
- [ ] 디스크 사용량 모니터링
- [ ] 성능 보고서 생성

---

## 6. Success Metrics

### 정량적 지표

- **환경 전환 시간:** 30초 이내 (목표)
- **디스크 사용량:** 각 worktree 500MB 이내
- **Git 병합 충돌:** 월 2회 이하
- **환경 전환 실패율:** 1% 이하

### 정성적 지표

- **사용자 만족도:** 환경 전환 용이성 만족
- **개발 생산성:** ARIA 개발 시 MoAI-ADK 영향 없음
- **테스트 신뢰성:** 순수 환경에서 일관된 테스트 결과
- **Git history 깔끔함:** 명확한 브랜치 관리

---

## 7. Rollout Plan

### Phase 1: 파일럿 (1주차)

1. 기본 worktree 생성
2. 핵심 스크립트 구현
3. 내부 테스트

### Phase 2: 베타 (2주차)

1. 자동화 기능 추가
2. 문서화 완료
3. 소규모 사용자 테스트

### Phase 3: 안정화 (3주차 이후)

1. 피드백 반영
2. 고급 기능 개발
3. 전체 배포

---

## Traceability

### SPEC-ARIA-008 연계

- **EARS-001, EARS-007:** Git worktree 구조로 완전한 격리 보장
- **EARS-002:** 브랜치 전략으로 Git history 깔끔 유지
- **EARS-003:** 환경 전환 스크립트로 쉬운 전환 지원
- **EARS-011:** 디스크 I/O 최적화로 30초 이내 전환 목표

### TAG 참조

- **SPEC-ARIA-008:** 요구사항 정의
- **PLAN-ARIA-008:** 현재 문서 (구현 계획)
- **ACCEPT-ARIA-008:** 인수 조건 (acceptance.md)
