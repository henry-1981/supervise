---
name: aria-init
description: >
  ARIA 초기화 명령어 - Notion 데이터베이스 자동 생성 및 MCP 서버 설정을 수행합니다.
  Notion 워크스페이스에 6개 데이터베이스(Regulatory Requirements, Document Registry,
  CAPA Tracker, Risk Register, Submission Tracker, Knowledge Base)를 생성하고
  필드 속성, 관계(Relation), 뷰(View)를 설정합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "1.0.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, init, notion, database, setup"
  argument-hint: "notion | google | all"
---

# ARIA 초기화 명령어

## 목적

ARIA 시스템 초기화를 수행하고 Notion 데이터베이스와 MCP 서버 설정을 구성합니다.

## 사용법

```
/aria init notion   # Notion DB 생성 및 설정
/aria init google   # Google Workspace OAuth 설정
/aria init all      # 모든 통합 초기화
```

## Notion 데이터베이스 초기화

### 단계 1: Notion API 인증 확인

사용자에게 Notion Integration Token을 요청합니다:

1. Notion workspace에서 [My Integrations](https://www.notion.so/my-integrations) 접속
2. 새로운 통합(Integration) 생성: "ARIA System"
3. Internal Integration Token 복사
4. 환경 변수로 설정: `export NOTION_API_KEY=your_token`
5. 또는 `.mcp.json`에 직접 설정

### 단계 2: 워크스페이스 접근 권한 부여

1. 생성된 Integration을 Notion 페이지에서 공유
2. ARIA가 Notion API를 통해 워크스페이스 접근 권한 확인

### 단계 3: 데이터베이스 스키마 생성

다음 6개 데이터베이스를 자동 생성합니다:

#### 1. Regulatory Requirements (규제 요구사항)

**필드:**
- ID (Title): 요구사항 고유 번호 (예: REQ-001)
- Standard (Select): FDA 21 CFR 820, ISO 13485, EU MDR
- Section (Text): 해당 조항/섹션
- Requirement (Text): 요구사항 내용
- Category (Multi-select): Design Control, Risk Management, CAPA
- Applicability (Select): Full, Partial, N/A
- Evidence (Files): 증거 파일 링크
- Status (Select): Active, Deprecated, Under Review
- Notes (Text): 추가 참고사항

**관계(Relations):**
- Document Registry (Many-to-many)
- CAPA Tracker (Many-to-many)

#### 2. Document Registry (문서 등록부)

**필드:**
- Doc ID (Title): 문서 고유 번호 (예: DOC-SOP-001)
- Title (Text): 문서 제목
- Type (Select): SOP, WI, Report, Form, Template
- Version (Number): 문서 버전
- Status (Select): Draft, Under Review, Approved, Withdrawn
- Owner (Person): 문서 담당자
- Review Date (Date): 다음 리뷰 일자
- Related Reqs (Relation): 관련 규제 요구사항
- Change History (Rich Text): 변경 이력

**관계(Relations):**
- CAPA Tracker (One-to-many)
- Risk Register (Many-to-many)

#### 3. CAPA Tracker

**필드:**
- CAPA ID (Title): CAPA 고유 번호 (예: CAPA-2024-001)
- Type (Select): Correction, Corrective Action, Preventive Action
- Source (Select): Audit, Complaint, Non-conformance
- Description (Text): 문제 설명
- Root Cause (Rich Text): 근본 원인 분석
- Action Plan (Rich Text): 조치 계획
- Status (Select): Open, In Progress, Verified, Closed
- Due Date (Date): 목표 완료일
- Assignee (Person): 담당자
- Effectiveness (Select): Effective, Partial, Ineffective

**관계(Relations):**
- Risk Register (Many-to-many)
- Document Registry (Many-to-many)

#### 4. Risk Register (위험 등록부)

**필드:**
- Risk ID (Title): 위험 고유 번호 (예: RISK-001)
- Hazard (Text): 위험 요소
- Hazardous Situation (Text): 위험 상황
- Harm (Text): 발생 가능한伤害
- Severity (Select): S1, S2, S3, S4, S5
- Probability (Select): P1, P2, P3, P4, P5
- Risk Level (Formula): Severity × Probability
- Acceptability (Select): Acceptable, Unacceptable
- Control Measures (Rich Text): 통제 조치
- Residual Risk (Formula): 잔여 위험도
- Verification (Text): 검증 방법

**관계(Relations):**
- CAPA Tracker (One-to-many)
- Document Registry (Many-to-many)

#### 5. Submission Tracker (제출 추적)

**필드:**
- Submission ID (Title): 제출 고유 번호 (예: SUB-510K-001)
- Type (Select): 510(k), CE, PMA, MDSAP
- Device Name (Text): 의료기기명
- Product Code (Text): FDA Product Code
- Predicate (Text): Predicate Device
- Status (Select): Planning, Preparation, Submitted, Review, Approved, Cleared
- Target Date (Date): 목표 제출일
- FDA Number (Text): FDA 제출 번호 (K번호)
- Documents (Files): 제출 패키지 링크
- Notes (Text): 추가 참고사항

**관계(Relations):**
- Document Registry (Many-to-many)

#### 6. Knowledge Base (지식 베이스)

**필드:**
- ID (Title): 지식 항목 ID (예: KB-001)
- Topic (Text): 주제
- Category (Select): Regulation, Standard, Guidance, Best Practice
- Content (Rich Text): 내용
- Source (Text): 출처 (예: FDA, ISO, NB)
- Applicable To (Multi-select): Design, Risk, CAPA, Submission
- Last Updated (Date): 마지막 업데이트 일자
- Confidence (Select): High, Medium, Low
- Tags (Multi-select): 검색용 태그

**관계(Relations):**
- Regulatory Requirements (Many-to-many)
- Document Registry (Many-to-many)

### 단계 4: 관계(Relation) 설정

데이터베이스 간 관계를 설정합니다:

- CAPA ↔ Risk: CAPA는 Risk 완화를 위한 조치
- Document ↔ Requirements: 문서는 요구사항 증명
- Document ↔ CAPA: CAPA 문서화
- Document ↔ Risk: 위험 분석 문서
- Document ↔ Submission: 제출 패키지 문서
- Knowledge ↔ Requirements: 규제 지식 베이스

### 단계 5: 뷰(View) 생성

각 데이터베이스에 유용한 뷰를 생성합니다:

- **Risk Matrix View:** Severity vs Probability 매트릭스
- **CAPA Status Dashboard:** Open/In Progress/Closed 요약
- **Submission Calendar:** 제출일 기간 시각화
- **Document Review Queue:** 리뷰 대기 문서
- **Requirements by Standard:** 규정별 요구사항 분류

## Google Workspace 초기화

### 단계 1: Google Cloud 프로젝트 설정

1. [Google Cloud Console](https://console.cloud.google.com) 접속
2. 새 프로젝트 생성: "ARIA Integration"
3. API 활성화: Gmail API, Google Docs API, Google Sheets API, Google Calendar API, Google Drive API

### 단계 2: OAuth 2.0 동의 화면 구성

1. OAuth 동의 화면 설정
2. 애플리케이션 정보 입력
3. 범위(Scopes) 추가:
   - `https://www.googleapis.com/auth/gmail.readonly`
   - `https://www.googleapis.com/auth/documents`
   - `https://www.googleapis.com/auth/spreadsheets`
   - `https://www.googleapis.com/auth/calendar`
   - `https://www.googleapis.com/auth/drive`

### 단계 3: OAuth 클라이언트 생성

1. 사용자 인증 정보 생성 → OAuth 클라이언트 ID
2. 애플리케이션 유형: Desktop app
3. 클라이언트 ID 및 시크릿 저장

### 단계 4: OAuth 인증 수행

```
/aria auth google
```

브라우저에서 Google 로그인 → ARIA에 액세스 권한 부여 → Token 저장

## MCP 서버 설정

### Notion MCP 구성 (.mcp.json)

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}",
        "NOTION_DATABASE_ID": "${NOTION_DATABASE_ID}"
      }
    }
  }
}
```

### Google Workspace MCP 구성

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gmail"],
      "env": {
        "GOOGLE_CREDENTIALS": "${GOOGLE_CREDENTIALS}",
        "GOOGLE_TOKEN_PATH": "${GOOGLE_TOKEN_PATH}"
      }
    }
  }
}
```

### Context7 MCP 구성

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

## 실행 순서

1. `/aria init notion` - Notion DB 생성
2. `/aria init google` - Google OAuth 설정
3. `/aria status` - 초기화 상태 확인

## 오류 처리

### Notion API 인증 실패

```
오류: Notion API 인증에 실패했습니다.
해결 방법:
1. Integration Token이 올바른지 확인하세요
2. Integration이 Notion 페이지와 공유되었는지 확인하세요
3. 토큰을 환경 변수로 설정한 후 다시 시도하세요
```

### 데이터베이스 이미 존재

```
안내: Notion 데이터베이스가 이미 존재합니다.
선택사항:
1. 기존 데이터베이스 사용 (스킵)
2. 스키마 업데이트 (기존 데이터 보존)
3. 데이터베이스 재생성 (기존 데이터 삭제)
```

## 완료 마커

초기화 완료 시 `<aria:init:complete>` 마커를 추가합니다.

## 참고

- Notion DB 스키마는 Phase 3에서 정의된 스펙을 따릅니다
- 각 데이터베이스는 Notion Page Template을 포함합니다
- 관계 설정은 데이터 무결성을 보장합니다
- 뷰는 사용자 맞춤화 가능합니다
