# SPEC-ARIA-004: Implementation Plan

## 개요 (Overview)

본 문서는 ARIA Phase 4 - MCP 통합 시스템의 구현 계획을 정의합니다.

**목표:** Notion, Google Workspace, Context7 MCP 서비스를 ARIA에 통합하여 중앙 데이터 관리, 협업, 규제 검색 기능을 구현합니다.

**의존성:**
- Phase 1 (Core Framework): 완료 필요
- Phase 2 (Business Workflow): 완료 필요
- Phase 3 (RA/QA Specialization): 완료 필요

---

## 마일스톤 (Milestones)

### Milestone 1: Notion MCP 기본 통합 (Priority High)

**목표:** Notion DB 자동 생성 및 기본 CRUD 작업 구현

**작업:**
1. Notion MCP 서버 설정
   - `.mcp.json`에 notion 서버 추가
   - Notion API Key 설정 환경변수 구성
   - 인증 테스트

2. Notion DB 자동 생성 스킬 개발
   - `.claude/skills/aria-integration-notion/` 생성
   - 6개 DB 스키마 자동 생성 기능
   - 필드 속성 설정
   - Relation 설정

3. 기본 CRUD 작업 구현
   - Create: DB 페이지 생성
   - Read: DB 조회 및 검색
   - Update: 페이지 수정
   - Delete: 페이지 삭제 (감사 추적 포함)

4. 감사 추적 기능
   - Audit Log DB 생성
   - 모든 작업 로그 기록
   - 감사 추적 검색 기능

**성공 기준:**
- Notion DB 6개가 자동으로 생성됨
- 기본 CRUD 작업이 정상 작동함
- 감사 추적이 모든 작업을 기록함

**의존성:** 없음 (최우선 순위)

---

### Milestone 2: Notion DB 고급 기능 (Priority High)

**목표:** Traceability Matrix, 자동 입력, 관계 설정 구현

**작업:**
1. Traceability Matrix 구현
   - Requirements ↔ Documents ↔ Evidence 관계
   - 자동 관계 설정
   - 고아 페이지 탐지

2. CAPA Tracker Notion 연동
   - CAPA 생성 시 자동 DB 등록
   - Risk Register와 Relation 설정
   - Due Date 알림 설정

3. Risk Register Notion 연동
   - 위험 식별 시 자동 DB 등록
   - Risk Index 자동 계산 (Severity × Probability)
   - Acceptability 평가

4. Document Registry Notion 연동
   - 문서 생성 시 자동 DB 등록
   - Version History 관리
   - Review Date 알림

**성공 기준:**
- Traceability Matrix가 정상 작동함
- CAPA, Risk, Document Tracker가 자동으로 Notion에 동기화됨
- 고아 페이지 탐지 및 경고가 작동함

**의존성:** Milestone 1 완료

---

### Milestone 3: Google Workspace MCP 통합 (Priority Medium)

**목표:** Gmail, Docs, Sheets, Calendar 통합 구현

**작업:**
1. Google Workspace MCP 설정
   - `.mcp.json`에 google-workspace 서버 추가
   - OAuth 2.0 인증 플로우 구현
   - Token 관리 (access_token, refresh_token)

2. Gmail 통합
   - 규제 서신 검색 기능
   - 이메일 내용 요약
   - Notion DB와 연결

3. Google Docs 통합
   - 문서 자동 생성 기능
   - 템플릿 적용 (DHF, CAPA, Risk Report)
   - 팀원 공유 설정
   - Notion DB에 링크 기록

4. Google Sheets 통합
   - 데이터 분석 시트 생성
   - Notion DB 데이터 추출 및 입력
   - 차트/그래프 자동 생성

5. Google Calendar 통합
   - 데드라인 자동 등록
   - 알림 설정 (1주 전, 1일 전, 당일)
   - Notion 페이지 링크 포함

**성공 기준:**
- OAuth 인증이 정상 작동함
- Gmail 검색이 정상 작동함
- Docs, Sheets, Calendar 자동 생성이 작동함
- 모든 Google 서비스가 Notion과 연동됨

**의존성:** Milestone 1 완료

---

### Milestone 4: Context7 MCP 최적화 (Priority Medium)

**목표:** 규제 문서 검색 최적화 및 Knowledge Base 자동 업데이트

**작업:**
1. Context7 MCP 최적화 스킬 개발
   - `.claude/skills/aria-integration-context7/` 생성
   - 규정별 라이브러리 ID 매핑
   - 검색 쿼리 최적화

2. Knowledge Base 자동 업데이트
   - 주간 Context7 검색
   - 변경사항 탐지
   - Knowledge Base 업데이트
   - 사용자 알림

3. 검색 결과 캐싱
   - Notion Knowledge Base에 저장
   - TTL 30일 설정
   - 캐시 히트율 최적화

**성공 기준:**
- Context7 검색이 최적화됨
- Knowledge Base가 주간 자동 업데이트됨
- 검색 결과 캐싱이 작동함

**의존성:** Milestone 1 완료

---

### Milestone 5: `/aria` 명령어 구현 (Priority High)

**목표:** `/aria search`, `/aria knowledge`, `/aria status` 명령어 구현

**작업:**
1. `/aria search` 통합 검색
   - 모든 데이터 소스 검색 (Notion, Context7, Google)
   - 결과 통합 및 관련성 정렬
   - 필터링 옵션

2. `/aria knowledge` 지식 베이스 조회
   - Notion Knowledge Base 검색
   - Context7 fallback 검색
   - 자동 Knowledge Base 확장

3. `/aria status` 프로젝트 상태 대시보드
   - CAPA Tracker 현황
   - Risk Register 현황
   - Submission Tracker 현황
   - Document Registry 현황
   - Google Calendar 이벤트
   - 경고 시스템

**성공 기준:**
- `/aria search`가 모든 소스를 검색함
- `/aria knowledge`가 지식 베이스를 조회함
- `/aria status`가 대시보드를 표시함
- 경고 시스템이 작동함

**의존성:** Milestone 1, 2, 3, 4 완료

---

## 기술 접근 (Technical Approach)

### 아키텍처

```
┌─────────────────────────────────────────┐
│         ARIA Orchestrator              │
│    (Brief-Execute-Deliver Workflow)    │
└──────────────┬──────────────────────────┘
               │
     ┌─────────┴──────────┬──────────────┐
     │                   │              │
┌────▼────┐        ┌─────▼─────┐   ┌───▼────┐
│  Notion  │        │  Google   │   │Context7│
│   MCP   │        │ Workspace │   │  MCP   │
└────┬────┘        │    MCP    │   └───┬────┘
     │             └─────┬─────┘       │
     │                   │             │
┌────▼───────────────────▼─────────────▼────┐
│          Notion Workspace               │
│  ┌──────────────────────────────────┐   │
│  │ 6 DBs + Audit Log + Knowledge   │   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

### 기술 스택

**MCP 서버:**
- Notion: `claude_ai_Notion` (built-in MCP)
- Google Workspace: `@anthropic/google-workspace-mcp`
- Context7: `@upstash/context7-mcp@latest`
- Sequential Thinking: `@modelcontextprotocol/server-sequential-thinking`

**Notion API:**
- Notion API v2.2.3+
- Integration Token (Internal Integration Token)

**Google API:**
- Gmail API
- Google Docs API
- Google Sheets API
- Google Calendar API
- Google Drive API
- OAuth 2.0

**개발 언어:**
- TypeScript (Notion MCP client)
- Python (Google Workspace MCP wrapper)

### 통합 패턴

**Notion MCP 통합:**
1. ARIA 스킬에서 MCP tool 호출
2. Notion API 요청 전송
3. 응답을 ARIA 데이터 모델로 변환
4. Notion DB에 저장

**Google Workspace MCP 통합:**
1. OAuth 2.0 인증 플로우
2. API 호출 및 데이터 추출
3. Notion DB에 링크 저장
4. 협업 기능 제공

**Context7 MCP 통합:**
1. 라이브러리 ID 확인 (resolve-library-id)
2. 규정 검색 (get-library-docs)
3. Knowledge Base에 저장
4. 캐싱 및 TTL 관리

---

## 위험 및 완화 (Risks and Mitigation)

| 위험 | 확률 | 영향 | 완화 전략 |
|------|------|------|-----------|
| Notion API 속도 제한 | Medium | High | Exponential backoff, 배치 처리 |
| Google OAuth 복잡성 | Medium | Medium | 명확한 사용자 가이드, 재인증 자동화 |
| Context7 검색 결과 부정확 | Low | Medium | 출처 검증, 사용자 피드백 |
| MCP 서버 호환성 | Low | High | 버전 고정, 테스트 커버리지 |
| 데이터 동기화 오류 | Medium | Medium | 재시도 메커니즘, 감사 추적 |

---

## 성공 기준 (Success Criteria)

### 기능적 요구사항

- [FR1] Notion DB 6개가 자동으로 생성됨
- [FR2] 모든 Notion DB에서 CRUD 작업이 가능함
- [FR3] 감사 추적이 모든 작업을 기록함
- [FR4] Gmail 검색이 정상 작동함
- [FR5] Google Docs, Sheets, Calendar 자동 생성이 작동함
- [FR6] Context7 검색이 최적화됨
- [FR7] `/aria search`가 모든 소스를 검색함
- [FR8] `/aria knowledge`가 지식 베이스를 조회함
- [FR9] `/aria status`가 대시보드를 표시함

### 비기능적 요구사항

- [NFR1] API 속도 제한 준수 (Rate Limiting)
- [FR2] 응답 시간: 일반 쿼리 30초 이내
- [NFR3] 오류 발생 시 평이한 언어 안내
- [NFR4] 데이터 무결성 보장
- [NFR5] OAuth 인증 안정성

---

## 참고 자료 (References)

### 내부 참고 자료

- [ARCHITECTURE-REDESIGN.md](../docs/specs/ARCHITECTURE-REDESIGN.md): 전체 아키텍처
- [SPEC-ARIA-001](../.moai/specs/SPEC-ARIA-001/spec.md): Phase 1 Core Framework
- [SPEC-ARIA-002](../.moai/specs/SPEC-ARIA-002/spec.md): Phase 2 Business Workflow
- [SPEC-ARIA-003](../.moai/specs/SPEC-ARIA-003/spec.md): Phase 3 RA/QA Specialization

### 외부 참고 자료

- [Notion API Documentation](https://developers.notion.com/reference)
- [Google Workspace APIs](https://developers.google.com/workspace)
- [Context7 MCP](https://context7.io)
- [Model Context Protocol](https://modelcontextprotocol.io)
