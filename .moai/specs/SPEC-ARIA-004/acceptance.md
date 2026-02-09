# SPEC-ARIA-004: Acceptance Criteria

## 개요 (Overview)

본 문서는 ARIA Phase 4 - MCP 통합 시스템의 인수 기준(Acceptance Criteria)을 정의합니다.

**목표:** 모든 요구사항이 충족되었는지 검증하고, 품질 기준을 준수하는지 확인합니다.

---

## Given-When-Then 형식 인수 기준

### AC-1: Notion MCP 기본 통합

**Scenario 1.1: Notion DB 자동 생성**

**GIVEN** 사용자가 Notion workspace에 접근 권한을 가지고 있고
**AND** Notion API Key가 설정되어 있으며
**WHEN** `/aria init notion` 명령어를 실행하면
**THEN** Notion에 6개 데이터베이스가 자동으로 생성되어야 하고
**AND** 각 DB의 필드 속성이 올바르게 설정되어야 하며
**AND** DB 간 Relation이 올바르게 설정되어야 하고
**AND** 사용자에게 생성 완료 메시지가 표시되어야 한다.

**Scenario 1.2: Notion DB 페이지 생성**

**GIVEN** Notion DB가 생성되어 있고
**WHEN** 새로운 CAPA를 생성하면
**THEN** CAPA Tracker DB에 페이지가 자동으로 생성되어야 하고
**AND** CAPA ID, Description, Root Cause 필드가 자동으로填充되어야 하며
**AND** Due Date 알림이 설정되어야 한다.

**Scenario 1.3: Notion DB 조회**

**GIVEN** Notion DB에 데이터가 존재하고
**WHEN** `/aria search capa "overdue"`를 실행하면
**THEN** CAPA Tracker DB에서 관련 페이지를 검색해야 하고
**AND** 검색 결과가 관련성 순으로 정렬되어야 하며
**AND** 각 결과에 Notion 페이지 링크가 포함되어야 한다.

### AC-2: Notion DB 고급 기능

**Scenario 2.1: Traceability Matrix**

**GIVEN** Requirements와 Documents가 존재하고
**WHEN** 새로운 문서를 생성하면
**THEN** 관련 Requirements와 Relation이 자동으로 설정되어야 하고
**AND** Traceability Matrix가 업데이트되어야 하며
**AND** 고아 페이지(Orphaned page)가 없어야 한다.

**Scenario 2.2: Risk Index 자동 계산**

**GIVEN** Risk Register DB가 생성되어 있고
**WHEN** 새로운 위험을 등록하면
**THEN** Severity × Probability로 Risk Index가 자동 계산되어야 하고
**AND** Acceptability가 평가되어야 하며
**AND** Risk Index가 Unacceptable이면 경고가 표시되어야 한다.

**Scenario 2.3: Version History 관리**

**GIVEN** Document Registry DB가 생성되어 있고
**WHEN** 문서가 수정되면
**THEN** 이전 버전이 보존되어야 하고
**AND** Change Description이 기록되어야 하며
**AND** Version History를 조회할 수 있어야 한다.

### AC-3: Google Workspace MCP 통합

**Scenario 3.1: Gmail 검색**

**GIVEN** Google OAuth 인증이 완료되어 있고
**AND** Gmail에 규제 서신이 존재하며
**WHEN** `/aria search email "FDA 510(k) request"`를 실행하면
**THEN** Gmail API로 관련 이메일을 검색해야 하고
**AND** 이메일 목록이 표시되어야 하며
**AND** 각 이메일에 요약이 포함되어야 하고
**AND** Notion DB에 저장 옵션이 제공되어야 한다.

**Scenario 3.2: Google Docs 생성**

**GIVEN** Google OAuth 인증이 완료되어 있고
**WHEN** `/aria docs create "DHF Review - [Device]"`를 실행하면
**THEN** Google Docs 문서가 자동으로 생성되어야 하고
**AND** DHF 템플릿이 적용되어야 하며
**AND** 팀원과 공유되어야 하고
**AND** Notion Document Registry에 링크가 기록되어야 한다.

**Scenario 3.3: Google Sheets 생성**

**GIVEN** Google OAuth 인증이 완료되어 있고
**AND** Notion CAPA Tracker에 데이터가 존재하며
**WHEN** `/aria sheets create "CAPA Trend Analysis"`를 실행하면
**THEN** Google Sheets 스프레드시트가 생성되어야 하고
**AND** Notion CAPA 데이터가 추출되어填充되어야 하며
**AND** 차트/그래프가 자동으로 생성되어야 하고
**AND** Notion에 시트 링크가 기록되어야 한다.

**Scenario 3.4: Google Calendar 등록**

**GIVEN** Google OAuth 인증이 완료되어 있고
**WHEN** CAPA가 생성되고 Due Date가 설정되면
**THEN** Google Calendar 이벤트가 자동으로 생성되어야 하고
**AND** 알림이 설정되어야 하며 (1주 전, 1일 전, 당일)
**AND** 관련 Notion 페이지 링크가 포함되어야 한다.

**Scenario 3.5: OAuth 재인증**

**GIVEN** OAuth token이 만료되었고
**WHEN** Google API를 호출하면
**THEN** 자동으로 재인증 플로우가 시작되어야 하고
**AND** 사용자에게 재인증 안내가 표시되어야 하며
**AND** 재인증 완료 후 작업이 재개되어야 한다.

### AC-4: Context7 MCP 최적화

**Scenario 4.1: 규정 검색**

**GIVEN** Context7 MCP가 설정되어 있고
**WHEN** `/aria search regulation "FDA 21 CFR 820.30"`를 실행하면
**THEN** Context7에서 관련 규정을 검색해야 하고
**AND** 검색 결과가 Notion Knowledge Base에 저장되어야 하며
**AND** 출처 인용이 포함되어야 하고
**AND** 사용자에게 검색 결과가 표시되어야 한다.

**Scenario 4.2: Knowledge Base 자동 업데이트**

**GIVEN** Knowledge Base가 생성되어 있고
**WHEN** 주간 업데이트 스케줄이 실행되면
**THEN** Context7에서 최신 규정을 검색해야 하고
**AND** 변경사항이 탐지되어야 하며
**AND** Knowledge Base가 업데이트되어야 하고
**AND** 주요 변경사항에 대해 사용자 알림이 전송되어야 한다.

**Scenario 4.3: 검색 결과 캐싱**

**GIVEN** Knowledge Base에 검색 결과가 캐시되어 있고
**WHEN** 동일한 검색어로 검색하면
**THEN** 캐시된 결과가 반환되어야 하고
**AND** Context7 API 호출이 발생하지 않아야 하며
**AND** 응답 시간이 개선되어야 한다.

### AC-5: 감사 추적 (Audit Trail)

**Scenario 5.1: 감사 추적 기록**

**GIVEN** Audit Log DB가 생성되어 있고
**WHEN** 문서가 승인되면
**THEN** Audit Log에 기록되어야 하고
**AND** Timestamp, Agent, Action, Entity, Decision, Rationale, Outcome 필드가填充되어야 하며
**AND** 관련 문서와 Relation이 설정되어야 한다.

**Scenario 5.2: 감사 추적 검색**

**GIVEN** Audit Log에 데이터가 존재하고
**WHEN** `/aria audit search --agent expert-regulatory --date "2026-01-01:2026-02-09"`를 실행하면
**THEN** 해당 기간의 expert-regulatory 작업 로그가 표시되어야 하고
**AND** 필터링 옵션이 적용되어야 하며
**AND** Timeline view로 표시되어야 하고
**AND** CSV/PDF로 export할 수 있어야 한다.

**Scenario 5.3: 감사 추적 무결성**

**GIVEN** Audit Log가 생성되어 있고
**WHEN** 감사 추적을 검증하면
**THEN** 모든 결정/변경이 기록되어야 하고
**AND** Audit Log가 수정 불가능해야 하며 (Immutable)
**AND** 기록이 완전해야 한다 (Complete).

### AC-6: `/aria search` 통합 검색

**Scenario 6.1: 통합 검색 실행**

**GIVEN** 모든 데이터 소스가 설정되어 있고
**WHEN** `/aria search "510(k) submission requirements"`를 실행하면
**THEN** Notion DB, Context7, Google Workspace에서 병렬 검색이 실행되어야 하고
**AND** 결과가 통합되어야 하며
**AND** 관련성 점수로 정렬되어야 하고
**AND** 각 결과에 출처가 표시되어야 한다.

**Scenario 6.2: 검색 결과 필터링**

**GIVEN** 100개 이상의 검색 결과가 반환되고
**WHEN** 검색 결과가 표시되면
**THEN** 카테고리별 필터가 제공되어야 하고 (Requirements, Documents, Emails, Standards)
**AND** 날짜 범위 필터가 제공되어야 하며
**AND** 필터 적용 시 결과가 업데이트되어야 한다.

### AC-7: `/aria knowledge` 지식 베이스 조회

**Scenario 7.1: Knowledge Base 조회**

**GIVEN** Knowledge Base에 데이터가 존재하고
**WHEN** `/aria knowledge "MDR classification rules"`를 실행하면
**THEN** Knowledge Base에서 관련 항목을 검색해야 하고
**AND** 검색 결과가 표시되어야 하며
**AND** 관련 Requirements와 Relations가 표시되어야 하고
**AND** 출처 및 신뢰도가 표시되어야 한다.

**Scenario 7.2: Knowledge Base 자동 확장**

**GIVEN** Knowledge Base에 관련 항목이 없고
**WHEN** `/aria knowledge "new regulation topic"`를 실행하면
**THEN** Context7에서 검색이 실행되어야 하고
**AND** 검색 결과가 Knowledge Base에 저장되어야 하며
**AND** 사용자에게 새 항목 추가 알림이 전송되어야 한다.

### AC-8: `/aria status` 프로젝트 상태 대시보드

**Scenario 8.1: 대시보드 표시**

**GIVEN** 모든 Notion DB가 설정되어 있고
**WHEN** `/aria status`를 실행하면
**THEN** CAPA Tracker 현황이 표시되어야 하고 (Open items, Overdue, Due within 7 days)
**AND** Risk Register 현황이 표시되어야 하며 (Unacceptable risks, Review overdue)
**AND** Submission Tracker 현황이 표시되어야 하고 (Upcoming submissions, Deadlines)
**AND** Document Registry 현황이 표시되어야 하며 (Pending approvals, Review overdue)
**AND** Google Calendar 이벤트가 표시되어야 한다 (Upcoming audits, Regulatory deadlines).

**Scenario 8.2: 경고 시스템**

**GIVEN** 대시보드가 표시되어 있고
**WHEN** CAPA가 Overdue이고 Risk가 Unacceptable이면
**THEN** Critical 경고(빨강)가 표시되어야 하고
**AND** Notion 페이지 링크가 제공되어야 하며
**AND** 조치 제안이 표시되어야 한다.

**Scenario 8.3: 실시간 업데이트**

**GIVEN** 대시보드가 표시되어 있고
**WHEN** Notion DB에 변경이 발생하면
**THEN** 대시보드가 자동으로 갱신되어야 하고
**AND** Visual indicators가 업데이트되어야 하며 (색상, 아이콘)
**AND** 변경사항이 강조 표시되어야 한다.

---

## 품질 게이트 (Quality Gates)

### VALID 품질 프레임워크

**V**erified (검증됨):
- [ ] 모든 규제 주장에 출처 인용이 포함되어야 함
- [ ] Context7 MCP 검색 결과가 규정 원문과 대조 검증됨
- [ ] 최신 규정 버전이 사용됨

**A**ccurate (정확함):
- [ ] 모든 데이터 출처가 검증됨
- [ ] 수치/날짜 정확성이 확인됨
- [ ] 모순 데이터가 해결됨

**L**inked (연결됨):
- [ ] Requirements ↔ Documents ↔ Evidence 추적성 확보
- [ ] Notion DB 관계가 올바르게 설정됨
- [ ] 고아 페이지(Orphaned page)가 없음

**I**nspectable (검증 가능함):
- [ ] 모든 결정에 근거 문서화
- [ ] 감사 추적 완전성 확보
- [ ] 타임스탬프 기록

**D**eliverable (전달 가능함):
- [ ] Notion DB 스키마가 준수됨
- [ ] Google Workspace 형식 요구사항 충족
- [ ] API 응답 시간: 일반 쿼리 30초 이내

### 성능 기준

| 항목 | 기준 | 측정 방법 |
|------|------|----------|
| Notion DB 생성 시간 | 6개 DB < 60초 | Timer |
| API 응답 시간 | 일반 쿼리 < 30초 | Timer |
| 검색 응답 시간 | 통합 검색 < 45초 | Timer |
| 감사 추적 기록 | 모든 작업 로그 | Audit Log 조회 |
| OAuth 인증 | 재인증 플로우 < 30초 | Timer |

### 보안 기준

| 항목 | 기준 | 검증 방법 |
|------|------|----------|
| Notion API Key | 암호화된 저장 | Security audit |
| Google OAuth | OAuth 2.0 준수 | OAuth flow test |
| 데이터 전송 | HTTPS 암호화 | Network inspection |
| 감사 추적 | Immutable log | Audit log verification |
| 접근 제어 | Role-based access | Access control test |

---

## 테스트 시나리오 (Test Scenarios)

### 통합 테스트 (Integration Tests)

**IT-1: Notion MCP End-to-End**

```
1. `/aria init notion` 실행
2. Notion API Key 입력
3. 6개 DB 생성 확인
4. CAPA 생성 테스트
5. CAPA Tracker DB에 페이지 생성 확인
6. 감사 추적 기록 확인
```

**IT-2: Google Workspace MCP End-to-End**

```
1. `/aria auth google` 실행
2. OAuth 승인 완료
3. Gmail 검색 테스트
4. Google Docs 생성 테스트
5. Google Sheets 생성 테스트
6. Google Calendar 등록 테스트
7. Notion DB 연동 확인
```

**IT-3: Context7 MCP End-to-End**

```
1. `/aria search regulation "FDA 21 CFR 820.30"` 실행
2. Context7 검색 확인
3. Knowledge Base 저장 확인
4. 캐싱 동작 확인
5. 주간 업데이트 스케줄 확인
```

**IT-4: 통합 검색 End-to-End**

```
1. `/aria search "510(k) submission requirements"` 실행
2. Notion DB 검색 확인
3. Context7 검색 확인
4. Google Workspace 검색 확인
5. 결과 통합 및 정렬 확인
6. 필터링 기능 확인
```

### 성능 테스트 (Performance Tests)

**PT-1: Notion API 속도 제한**

```
1. 100개 페이지 생성 시도
2. Exponential backoff 동작 확인
3. 최대 3회 재시도 확인
4. 속도 제한 준수 확인
```

**PT-2: 대용량 검색**

```
1. Knowledge Base에 1000개 항목 저장
2. 통합 검색 실행
3. 응답 시간 < 45초 확인
4. 결과 관련성 확인
```

### 사용자 경험 테스트 (UX Tests)

**UX-1: 오류 메시지**

```
1. Notion API Key 없이 `/aria init notion` 실행
2. 평이한 언어 오류 메시지 확인
3. 다음 단계 안내 확인
```

**UX-2: OAuth 재인증**

```
1. OAuth token 만료 시뮬레이션
2. 재인증 플로우 안내 확인
3. 재인증 완료 후 작업 재개 확인
```

---

## Definition of Done

각 Milestone이 완료되기 위해 다음 조건이 모두 충족되어야 합니다:

### 공통 조건

- [ ] 모든 인수 기준(Acceptance Criteria) 충족
- [ ] 모든 품질 게이트(VALID) 통과
- [ ] 모든 성능 기준 충족
- [ ] 모든 보안 기준 충족
- [ ] 통합 테스트 통과
- [ ] 성능 테스트 통과
- [ ] 사용자 경험 테스트 통과

### Milestone별 조건

**Milestone 1: Notion MCP 기본 통합**
- [ ] Notion DB 6개 생성됨
- [ ] 기본 CRUD 작동
- [ ] 감사 추적 기록

**Milestone 2: Notion DB 고급 기능**
- [ ] Traceability Matrix 작동
- [ ] CAPA, Risk, Document Tracker 연동
- [ ] 고아 페이지 탐지

**Milestone 3: Google Workspace MCP 통합**
- [ ] Gmail 검색 작동
- [ ] Docs, Sheets, Calendar 생성 작동
- [ ] OAuth 인증 안정성

**Milestone 4: Context7 MCP 최적화**
- [ ] Context7 검색 최적화
- [ ] Knowledge Base 자동 업데이트
- [ ] 검색 결과 캐싱

**Milestone 5: `/aria` 명령어 구현**
- [ ] `/aria search` 작동
- [ ] `/aria knowledge` 작동
- [ ] `/aria status` 작동
- [ ] 경고 시스템 작동
