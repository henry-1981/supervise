# SPEC-ARIA-004: ARIA Phase 4 - MCP 통합 (MCP Integrations)

## TAG BLOCK

```yaml
SPEC_ID: SPEC-ARIA-004
TITLE: ARIA Phase 4 - MCP 통합 시스템
VERSION: 1.0.0
STATUS: Planned
PRIORITY: High
ASSIGNED: ARIA Core Team
EPIC: ARIA Architecture Redesign
PHASE: Phase 4 (MCP Integrations)
CREATED: 2026-02-09
LANGUAGE: ko
```

## 환경 (Environment)

### 프로젝트 맥락

ARIA (AI Regulatory Intelligence Assistant)는 의료기기 RA/QA (Regulatory Affairs / Quality Assurance) 전문가를 위한 AI 어시스턴트 시스템입니다.

**현재 상태:**
- Phase 1 (Core Framework): 완료 - 기반 아키텍처 및 오케스트레이터
- Phase 2 (Business Workflow): 완료 - 범용 비즈니스 에이전트 및 VALID 프레임워크
- Phase 3 (RA/QA Specialization): 완료 - 8개 도메인 전문가 에이전트 및 Notion DB 스키마 정의
- Phase 4 (MCP Integrations): 본 SPEC 대상 - MCP 서비스 통합 구현

**기술 스택:**
- Claude Code Plugin 아키텍처
- MCP (Model Context Protocol) 서버 통합
- Notion API (중앙 데이터 저장소)
- Google Workspace API (협업 도구)
- Context7 MCP (규제 문서 검색)
- Sequential Thinking MCP (복잡한 분석)

### 기존 시스템 구조

**Phase 1-3 완료 항목:**
- ARIA 코어/비즈니스/도메인 에이전트 (16개 에이전트: Core 4 + Business 4 + Domain 8)
- Brief-Execute-Deliver 워크플로우
- VALID 품질 프레임워크
- Notion DB 스키마 설계 (6개 데이터베이스)
- RA/QA 도메인 지식 스킬

**Phase 4 목표:**
- Notion MCP 통합 및 DB 자동 생성
- Google Workspace MCP 통합
- Context7 MCP 규제 문서 검색 최적화
- 감사 추적(Audit Trail) Notion 기반 구현
- `/aria search`, `/aria knowledge`, `/aria status` 명령어 구현

## 가정 (Assumptions)

### 사용자 가정

1. **Notion 사용 환경:**
   - 사용자는 Notion workspace에 접근 권한 보유
   - Notion API 키 발급 가능 (Integration Token)
   - Notion DB 기본 개념 이해 (Database, Relation, Rollup)

2. **Google Workspace 사용 환경:**
   - Google Workspace 계정 보유
   - Google OAuth 인증 가능
   - Gmail, Docs, Sheets, Calendar 사용 경험

3. **업무 요구사항:**
   - 규제 문서 중앙 관리 필요성
   - 팀 협업 및 문서 공유 요구
   - 감사 추적 및 컴플라이언스 증빙 필요

### 기술적 가정

1. **MCP 서버:**
   - Notion MCP 서버: `claude_ai_Notion` (built-in MCP)
   - Google Workspace MCP 서버: Google API 기반
   - Context7 MCP: Upstash Context7 서비스
   - Sequential Thinking MCP: Model Context Protocol 공식 서버

2. **Notion DB 스키마:**
   - Phase 3에서 정의된 6개 DB 스키마 활용
   - Regulatory Requirements, Document Registry, CAPA Tracker
   - Risk Register, Submission Tracker, Knowledge Base

3. **API 인증:**
   - Notion: Integration Token (Internal Integration Token)
   - Google: OAuth 2.0 flow
   - Context7: API Key

### 제약 사항

1. **비기능적 요구사항:**
   - API 호출 속도 제한 준수 (Rate Limiting)
   - 대용량 데이터 처리 시 배치 처리
   - 오류 발생 시 사용자에게 평이한 언어 안내

2. **품질 게이트:**
   - VALID 프레임워크 (Verified, Accurate, Linked, Inspectable, Deliverable)
   - 감사 추적 완전성 (Audit Trail Completeness)
   - 데이터 일관성 보장

## 요구사항 (Requirements)

### 1. Notion MCP 통합

#### 1.1 Event-Driven Requirements

**WHEN** ARIA가 초기화되면, **THE** 시스템은 **SHALL** Notion 데이터베이스 스키마를 자동 생성한다.

- **Given:** Notion workspace 접근 권한, Integration Token
- **When:** ARIA 초기화 또는 `/aria init notion` 실행
- **Then:**
  1. Phase 3에서 정의된 6개 DB 스키마 생성
  2. 필드 속성 설정 (Title, Text, Select, Relation, Formula 등)
  3. 관계(Relation) 설정 (CAPA ↔ Risk, Document ↔ Requirements)
  4. 뷰(View) 생성 (Risk Matrix, Status Dashboard 등)

**WHEN** 문서가 생성되면, **THE** 시스템은 **SHALL** Notion DB에 자동 등록한다.

- **Given:** 새로운 규제 문서 생성 (SOP, WI, Report 등)
- **When:** Document 생성 완료 이벤트
- **Then:**
  1. Document Registry DB에 페이지 생성
  2. 필드 자동 입력 (Doc ID, Title, Type, Version, Date)
  3. 관련 Requirements와 Relation 설정
  4. Notion 페이지 템플릿 적용

**WHEN** CAPA가 생성되면, **THE** 시스템은 **SHALL** CAPA Tracker DB에 기록한다.

- **Given:** Non-conformance 또는 Quality issue 식별
- **When:** CAPA 개시 이벤트
- **Then:**
  1. CAPA Tracker DB에 페이지 생성
  2. Root Cause, Action Plan 필드 입력
  3. 관련 Risk ID와 Relation 설정 (선택)
  4. Due Date 알림 설정

#### 1.2 State-Driven Requirements

**IF** Notion API 속도 제한에 도달하면, **THE** 시스템은 **SHALL** 자동으로 재시도한다.

- **Condition:** HTTP 429 Too Many Requests 수신
- **Action:** Exponential backoff로 재시도 (초기 1초, 최대 60초)
- **Max Retries:** 3회

**IF** Notion DB 페이지가 존재하지 않으면, **THE** 시스템은 **SHALL** 사용자에게 알리고 생성을 제안한다.

- **Condition:** Notion DB 조회 실패 (404 Not Found)
- **Action:** 사용자에게 DB 생성 제안, `/aria init notion` 안내

#### 1.3 Ubiquitous Requirements

시스템은 **항상** Notion DB 변경 이력을 **SHALL** 추적해야 한다.

- **Fields:** Created time, Last edited time, Created by, Last edited by
- **Purpose:** 감사 추적(Audit Trail) 지원

시스템은 **항상** Notion DB 무결성을 **SHALL** 보장해야 한다.

- **Validation:** Relation 필드 참조 무결성
- **Error Handling:** Orphaned page 탐지 및 경고

### 2. Google Workspace MCP 통합

#### 2.1 Event-Driven Requirements

**WHEN** 규제 서신이 도착하면, **THE** 시스템은 **SHALL** Gmail에서 검색한다.

- **Given:** FDA, NB, MFDS로부터 서신 수신
- **When:** `/aria search email "FDA 510(k) request"` 실행
- **Then:**
  1. Gmail API로 검색 수행 (query: subject, sender, date range)
  2. 관련 이메일 목록 추출
  3. 이메일 본문 요약
  4. 관련 Notion DB 페이지와 연결 제안

**WHEN** 협업 문서가 필요하면, **THE** 시스템은 **SHALL** Google Docs를 생성한다.

- **Given:** 팀 검토가 필요한 규제 문서
- **When:** `/aria docs create "DHF Review - [Device Name]"` 실행
- **Then:**
  1. Google Docs 문서 생성
  2. 템플릿 적용 (DHF, CAPA, Risk Report 등)
  3. 팀원 공유 설정
  4. Notion DB에 문서 링크 기록

**WHEN** 데이터 분석이 필요하면, **THE** 시스템은 **SHALL** Google Sheets를 생성한다.

- **Given:** CAPA 추세, 위험 매트릭스, 준수 체크리스트
- **When:** `/aria sheets create "CAPA Trend Analysis"` 실행
- **Then:**
  1. Google Sheets 스프레드시트 생성
  2. Notion DB 데이터 추출 및 입력
  3. 차트/그래프 자동 생성
  4. Notion DB에 시트 링크 기록

**WHEN** 데드라인이 설정되면, **THE** 시스템은 **SHALL** Google Calendar에 등록한다.

- **Given:** 규제 제출일, 감사일, 리뷰 마감일
- **When:** CAPA 생성, Submission planning, Audit scheduling
- **Then:**
  1. Google Calendar 이벤트 생성
  2. 알림 설정 (1주 전, 1일 전, 당일)
  3. 관련 Notion 페이지 링크 포함

#### 2.2 State-Driven Requirements

**IF** Google API 할당량이 초과되면, **THE** 시스템은 **SHALL** 사용량을 모니터링하고 경고한다.

- **Condition:** API quota 80% 도달
- **Action:** 사용자에게 경고, 할당량 리셋 시간 안내

**IF** Google OAuth 인증이 만료되면, **THE** 시스템은 **SHALL** 재인증을 요청한다.

- **Condition:** OAuth token 만료 (401 Unauthorized)
- **Action:** 재인증 플로우 안내

#### 2.3 Ubiquitous Requirements

시스템은 **항상** Google Workspace 변경 사항을 **SHALL** Notion에 동기화해야 한다.

- **Sync:** Docs 편집 → Notion DB 업데이트
- **Purpose:** 중앙 데이터 저장소 유지

시스템은 **항상** Google 데이터 백업을 **SHALL** 지원해야 한다.

- **Backup:** Drive에 제출 패키지 자동 백업
- **Version:** 문서 버전 관리

### 3. Context7 MCP 최적화

#### 3.1 Event-Driven Requirements

**WHEN** 규정 검색이 필요하면, **THE** 시스템은 **SHALL** Context7 MCP를 사용한다.

- **Given:** "FDA 21 CFR 820.30 최신 해석" 요청
- **When:** Brief phase 규제 분석
- **Then:**
  1. `mcp__context7__resolve-library-id`로 라이브러리 ID 확인
  2. `mcp__context7__get-library-docs`로 관련 문서 검색
  3. 검색 결과를 Notion Knowledge Base에 저장
  4. 출처 인용 (standard, section, version)

**WHEN** 표준 해석이 필요하면, **THE** 시스템은 **SHALL** Context7 문서를 참조한다.

- **Given:** "ISO 13485 Clause 8.5.2 적용 범위" 요청
- **When:** Standards interpretation 필요
- **Then:**
  1. Context7에서 ISO 13485 문서 검색
  2. 관련 조항 추출 및 해석
  3. 실무 적용 가이드 제공
  4. Notion Knowledge Base에 저장

#### 3.2 Ubiquitous Requirements

시스템은 **항상** Context7 검색 결과를 **SHALL** 캐시해야 한다.

- **Cache:** Notion Knowledge Base에 검색 결과 저장
- **TTL:** 30일 (규정 변경 주고려)

시스템은 **항상** 최신 규정을 **SHALL** 반영해야 한다.

- **Update:** 주간 자동 업데이트 확인
- **Notification:** 주요 규정 변경 시 사용자 알림

### 4. 감사 추적 (Audit Trail)

#### 4.1 Event-Driven Requirements

**WHEN** 결정이 내려지면, **THE** 시스템은 **SHALL** 감사 추적을 기록한다.

- **Given:** 규제 전략 결정, CAPA 승인, 문서 승인
- **When:** Decision event 발생
- **Then:**
  1. Notion Audit Log DB에 기록
  2. 필드: Timestamp, Agent, Decision, Rationale, Outcome
  3. 관련 문서/Requirements와 Relation 설정

**WHEN** 문서가 변경되면, **THE** 시스템은 **SHALL** 버전 히스토리를 유지한다.

- **Given:** Document edit, approval, withdrawal
- **When:** Document state change
- **Then:**
  1. Notion Page Version History 자동 기록
  2. Change Description 필드 입력
  3. Previous version과 비교 기능 제공

#### 4.2 Ubiquitous Requirements

시스템은 **항상** 감사 추적 무결성을 **SHALL** 보장해야 한다.

- **Immutable:** Audit Log는 수정 불가
- **Complete:** 모든 결정/변경 기록

시스템은 **항상** 감사 추적 검색을 **SHALL** 지원해야 한다.

- **Search:** Agent, Date range, Decision type, Outcome
- **Export:** CSV/PDF 보고서 생성

### 5. `/aria search` 통합 검색

#### 5.1 Event-Driven Requirements

**WHEN** `/aria search`가 실행되면, **THE** 시스템은 **SHALL** 모든 데이터 소스를 검색한다.

- **Given:** `/aria search "510(k) submission requirements"` 실행
- **When:** Search command 수신
- **Then:**
  1. Notion DB 검색 (Regulatory Requirements, Documents, Knowledge Base)
  2. Context7 MCP 검색 (최신 규정)
  3. Google Workspace 검색 (Gmail, Docs, Drive)
  4. 결과 통합 및 관련성 순 정렬

**WHEN** 검색 결과가 많으면, **THE** 시스템은 **SHALL** 필터링 옵션을 제공한다.

- **Given:** 100개 이상 검색 결과
- **When:** Search 결과 반환
- **Then:**
  1. 카테고리별 필터 (Requirements, Documents, Emails, Standards)
  2. 날짜 범위 필터
  3. 관련성 점수 기반 정렬

#### 5.2 Ubiquitous Requirements

시스템은 **항상** 검색 결과에 출처를 **SHALL** 표시해야 한다.

- **Sources:** Notion DB, Context7, Google Workspace
- **Confidence:** 검색 결과 신뢰도 표시

### 6. `/aria knowledge` 지식 베이스 조회

#### 6.1 Event-Driven Requirements

**WHEN** `/aria knowledge`가 실행되면, **THE** 시스템은 **SHALL** Notion Knowledge Base를 조회한다.

- **Given:** `/aria knowledge "MDR classification rules"` 실행
- **When:** Knowledge query 수신
- **Then:**
  1. Notion Knowledge Base DB 검색
  2. 관련 지식 항목 추출
  3. 관련 Requirements와 Relations 표시
  4. 출처 및 신뢰도 표시

**WHEN** 지식 항목이 없으면, **THE** 시스템은 **SHALL** Context7에서 검색하고 저장한다.

- **Given:** Knowledge Base에 관련 항목 없음
- **When:** Knowledge query 실패
- **Then:**
  1. Context7 MCP로 규정 검색
  2. 검색 결과를 Knowledge Base에 저장
  3. 사용자에게 새 항목 추가 확인

#### 6.2 Ubiquitous Requirements

시스템은 **항상** Knowledge Base를 **SHALL** 최신 상태로 유지해야 한다.

- **Update:** 주간 자동 업데이트
- **Validation:** 만료된 지식 항목 탐지

### 7. `/aria status` 프로젝트 상태 대시보드

#### 7.1 Event-Driven Requirements

**WHEN** `/aria status`가 실행되면, **THE** 시스템은 **SHALL** 프로젝트 현황을 표시한다.

- **Given:** `/aria status` 실행
- **When:** Status query 수신
- **Then:**
  1. CAPA Tracker: Open items, Due dates, Overdue items
  2. Risk Register: Unacceptable risks, Review dates
  3. Submission Tracker: Upcoming deadlines, Status
  4. Document Registry: Pending approvals, Review dates
  5. Google Calendar: Upcoming regulatory events

**WHEN** 위험 상황이 감지되면, **THE** 시스템은 **SHALL** 경고를 표시한다.

- **Given:** CAPA overdue, Unacceptable risk, Submission deadline < 7 days
- **When:** Status check
- **Then:**
  1. 경고 메시지 표시
  2. 관련 Notion 페이지 링크
  3. 조치 제안

#### 7.2 Ubiquitous Requirements

시스템은 **항상** 대시보드를 실시간으로 **SHALL** 업데이트해야 한다.

- **Refresh:** Notion DB 변경 시 자동 갱신
- **Display:** Visual indicators (색상, 아이콘)

## 스펙 (Specifications)

### S1: Notion MCP 통합 아키텍처

**S1.1 Notion DB 자동 생성**

```yaml
파일 위치: .claude/skills/aria-integration-notion/modules/database-creation.md

Notion DB 생성 프로세스:
1. Notion API 인증 (Integration Token)
2. Workspace DB 조회 (기존 DB 확인)
3. DB 스키마 생성 (Phase 3 정의 스키마)
4. 필드 속성 설정
5. Relation 설정 (DB 간 관계)
6. 뷰(View) 생성
7. 템플릿 페이지 생성
```

**S1.2 Notion MCP 구성**

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "claude_ai_Notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}",
        "NOTION_DATABASE_ID": "${NOTION_DATABASE_ID}"
      }
    }
  }
}
```

**S1.3 Notion DB 스키마 (6개)**

1. **Regulatory Requirements (규제 요구사항)**
   - 필드: ID, Standard, Section, Requirement, Category, Applicability, Evidence, Status, Notes
   - Relations: Document Registry, CAPA Tracker

2. **Document Registry (문서 등록부)**
   - 필드: Doc ID, Title, Type, Version, Status, Owner, Review Date, Related Reqs, Change History
   - Relations: CAPA Tracker, Risk Register

3. **CAPA Tracker**
   - 필드: CAPA ID, Type, Source, Description, Root Cause, Action Plan, Status, Due Date, Assignee, Effectiveness
   - Relations: Risk Register, Document Registry

4. **Risk Register (위험 등록부)**
   - 필드: Risk ID, Hazard, Hazardous Situation, Harm, Severity, Probability, Risk Level, Acceptability, Control Measures, Residual Risk, Verification
   - Relations: CAPA Tracker, Document Registry

5. **Submission Tracker (제출 추적)**
   - 필드: Submission ID, Type, Device Name, Product Code, Predicate, Status, Target Date, FDA Number, Documents, Notes
   - Relations: Document Registry

6. **Knowledge Base (지식 베이스)**
   - 필드: ID, Topic, Category, Content, Source, Applicable To, Last Updated, Confidence, Tags
   - Relations: Regulatory Requirements, Document Registry

### S2: Google Workspace MCP 통합

**S2.1 Google Workspace MCP 구성**

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@anthropic/google-workspace-mcp"],
      "env": {
        "GOOGLE_CREDENTIALS": "${GOOGLE_CREDENTIALS}",
        "GOOGLE_TOKEN_PATH": "${GOOGLE_TOKEN_PATH}"
      }
    }
  }
}
```

**S2.2 Google 서비스별 통합**

| 서비스 | 목적 | API 호출 | Notion 연동 |
|--------|------|----------|-------------|
| Gmail | 규제 서신 검색 | `users.messages.list` | 이메일 → Notion DB page |
| Google Docs | 협업 문서 편집 | `documents.create` | Docs 링크 → Notion DB |
| Google Sheets | 데이터 분석 | `spreadsheets.create` | 시트 데이터 → Notion DB |
| Google Calendar | 데드라인 관리 | `events.insert` | 이벤트 → Notion Dashboard |
| Google Drive | 파일 저장 | `files.create` | 파일 링크 → Notion DB |

**S2.3 OAuth 2.0 인증 플로우**

```
1. 사용자가 `/aria auth google` 실행
2. Google OAuth consent page 표시
3. 사용자 승인 (access_token, refresh_token 획득)
4. Token을 안전하게 저장 (encrypted storage)
5. API 호출 시 access_token 사용
6. Token 만료 시 refresh_token으로 갱신
```

### S3: Context7 MCP 최적화

**S3.1 Context7 MCP 구성**

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

**S3.2 규제 검색 패턴**

```yaml
# FDA 규정 검색
Library: "fda-21-cfr-820"
Topics: ["design-control", "risk-management", "capa"]

# ISO 표준 검색
Library: "iso-13485"
Topics: ["clause-8", "management-review", "internal-audit"]

# EU MDR 검색
Library: "eu-mdr-2017-745"
Topics: ["classification", "clinical-evaluation", "technical-documentation"]
```

**S3.3 Knowledge Base 자동 업데이트**

```
1. 주간 Context7 검색 (최신 규정 확인)
2. 변경사항 탐지 (version, date)
3. Knowledge Base 업데이트
4. 사용자 알림 (주요 변경사항)
```

### S4: 감사 추적 (Audit Trail)

**S4.1 Audit Log DB 스키마**

```yaml
Notion DB: Audit Log
필드:
  - Timestamp (Date): Created time
  - Agent (Text): orchestrator, expert-regulatory, etc.
  - Action (Select): Create, Update, Delete, Approve, Reject
  - Entity (Select): Document, CAPA, Risk, Submission, Requirement
  - Entity ID (Text): 관련 엔티티 ID
  - Decision (Text): 결정 내용
  - Rationale (Rich Text): 결정 근거
  - Outcome (Select): Approved, Rejected, Pending, Deferred
  - Related Docs (Relation): 관련 문서
```

**S4.2 감사 추적 검색**

```yaml
/aria audit search:
  Filters:
    - Agent: expert-regulatory
    - Date range: 2026-01-01 ~ 2026-02-09
    - Action: Approve, Reject
    - Entity: CAPA, Risk
  Output:
    - Audit Log entries
    - Related documents
    - Timeline view
    - Export (CSV/PDF)
```

### S5: `/aria search` 통합 검색

**S5.1 검색 엔진 아키텍처**

```yaml
통합 검색 프로세스:
1. 쿼리 분석 (키워드 추출, 의도 파악)
2. 검색 소스 결정 (Notion, Context7, Google)
3. 병렬 검색 실행
4. 결과 통합 및 관련성 점수 계산
5. 필터링 및 정렬
6. 결과 표시
```

**S5.2 관련성 점수 알고리즘**

```python
relevance_score = (
    keyword_match * 0.4 +
    semantic_similarity * 0.3 +
    recency * 0.2 +
    source_authority * 0.1
)
```

### S6: `/aria knowledge` 지식 베이스 조회

**S6.1 Knowledge Base 조회 프로세스**

```yaml
1. Notion Knowledge Base DB 검색
2. 관련 항목 추출 (제목, 내용, 태그)
3. Relations 표시 (연결된 Requirements, Documents)
4. 출처 및 신뢰도 표시
5. 관련 문서 링크
```

**S6.2 Knowledge Base 자동 확장**

```
1. 사용자 질문 분석
2. Knowledge Base 조회
3. 없으면 Context7 검색
4. 검색 결과를 Knowledge Base에 저장
5. 사용자에게 새 항목 알림
```

### S7: `/aria status` 프로젝트 상태 대시보드

**S7.1 대시보드 구성**

```yaml
CAPA Tracker:
  - Open items: 5
  - Overdue: 2 (경고)
  - Due within 7 days: 3

Risk Register:
  - Unacceptable risks: 1 (경고)
  - Review overdue: 4

Submission Tracker:
  - Upcoming submissions: 2
  - Deadline < 7 days: 1 (경고)

Document Registry:
  - Pending approvals: 8
  - Review overdue: 3

Google Calendar:
  - Upcoming audits: 1
  - Regulatory deadlines: 2
```

**S7.2 경고 시스템**

```yaml
경고 레벨:
  - Critical (빨강): CAPA overdue, Unacceptable risk
  - Warning (노랑): Deadline < 7 days, Review overdue
  - Info (파랑): Upcoming events, Status changes

경고 표시:
  - 색상coded 아이콘
  - Notion 페이지 링크
  - 조치 제안
```

## 추적성 (Traceability)

### 요구사항-구현 매트릭스

| REQ # | Requirement | Notion DB | Google | Context7 | Command |
|-------|-------------|-----------|--------|----------|---------|
| 1.1-1.3 | Notion MCP 통합 | All 6 DBs | - | - | `/aria init notion` |
| 2.1-2.3 | Google Workspace 통합 | Doc links | Gmail, Docs, Sheets, Calendar | - | `/aria docs`, `/aria sheets` |
| 3.1-3.2 | Context7 최적화 | Knowledge Base | - | All libraries | (automatic) |
| 4.1-4.2 | 감사 추적 | Audit Log | - | - | `/aria audit search` |
| 5.1-5.2 | 통합 검색 | All DBs | Gmail, Docs, Drive | All libraries | `/aria search` |
| 6.1-6.2 | 지식 베이스 | Knowledge Base | - | All libraries | `/aria knowledge` |
| 7.1-7.2 | 상태 대시보드 | All DBs | Calendar | - | `/aria status` |

### MCP 통합 의존성

```
Notion MCP (중앙 저장소)
    ├─ Document Registry ← Google Docs, Drive
    ├─ CAPA Tracker ← Google Calendar (Due dates)
    ├─ Risk Register ← Google Sheets (Analysis)
    ├─ Submission Tracker ← Google Calendar (Deadlines)
    └─ Knowledge Base ← Context7 MCP (Regulations)

Google Workspace MCP (협업)
    ├─ Gmail → Notion (Email search)
    ├─ Docs → Notion (Collaboration)
    ├─ Sheets → Notion (Data analysis)
    └─ Calendar → Notion (Deadlines)

Context7 MCP (규제 검색)
    └─ Knowledge Base ← Search results
```

## 변경 이력

| 버전 | 날짜 | 변경 사항 | 작성자 |
|------|------|-----------|--------|
| 1.0.0 | 2026-02-09 | 초기 SPEC 작성 | ARIA Core Team |

## 승인 기록

| 역할 | 이름 | 서명 | 날짜 |
|------|------|------|------|
| Spec Author | ARIA Core Team | | 2026-02-09 |
| Technical Reviewer | | | |
| Domain Expert | | | |
| Approval Authority | | | |
