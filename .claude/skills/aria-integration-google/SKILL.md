---
name: aria-integration-google
description: >
  Google Workspace MCP 서버 연동을 위한 ARIA 스킬. Gmail, Docs, Sheets, Calendar 통합과
  OAuth 2.0 인증 흐름을 제공합니다. 규제 준수 문서 협업 및 일정 관리에 사용합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Grep Glob Bash
user-invocable: true
metadata:
  version: "2.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "google, workspace, gmail, docs, sheets, calendar, oauth, aria"
  author: "MoAI-ARIA"
  context7-libraries: "google-api-nodejs-client"
  argument-hint: "Google Workspace 서비스 통합"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "google"
    - "workspace"
    - "gmail"
    - "docs"
    - "sheets"
    - "calendar"
    - "oauth"
    - "authentication"
    - "token"
    - "refresh token"
    - "구글"
    - "이메일"
    - "문서"
    - "달력"
  agents:
    - "expert-backend"
    - "expert-frontend"
  phases:
    - "plan"
    - "run"
  languages:
    - "typescript"
    - "javascript"
---

# ARIA Google Workspace Integration

ARIA 규제 관리 시스템을 위한 Google Workspace MCP 연동 스킬입니다.

## 빠른 시작

### 1. OAuth 인증 설정

```bash
/aria auth google setup
```

이 명령어는 다음을 수행합니다:
- Google Cloud 프로젝트 설정 안내
- OAuth 2.0 동의 화면 구성
- 인증 코드 획득 및 토큰 교환
- MCP 서버 설정 및 환경 변수 저장

### 2. 인증 상태 확인

```bash
/aria auth google status
```

현재 인증 상태, 토큰 만료 시간, API 액세스 권한을 확인합니다.

### 3. MCP 서버 설정

`.mcp.json`에 Google Workspace MCP 서버가 자동 추가됩니다:

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-workspace"],
      "env": {
        "GOOGLE_CLIENT_ID": "your_client_id.apps.googleusercontent.com",
        "GOOGLE_CLIENT_SECRET": "your_client_secret",
        "GOOGLE_REFRESH_TOKEN": "your_refresh_token"
      }
    }
  }
}
```

## 모듈 구조

이 스킬은 Progressive Disclosure 시스템을 사용하여 5개 모듈로 구성됩니다:

### Level 1: 메타데이터 (~100 토큰)
- 스킬 이름, 설명, 버전
- 트리거 키워드 및 에이전트 할당

### Level 2: 핵심 기능 (~5000 토큰)
- OAuth 2.0 인증 흐름 개요
- MCP 도구 인터페이스
- 기본 사용 예시

### Level 3: 상세 모듈 (On-Demand)
- `modules/oauth-flow.md` - OAuth 2.0 상세 구현 (전체 코드 포함)
- `modules/gmail-integration.md` - Gmail API 통합 (이메일 템플릿)
- `modules/docs-integration.md` - Google Docs 문서 생성 (4가지 템플릿)
- `modules/sheets-integration.md` - Google Sheets 데이터 관리 (RPN 계산)
- `modules/calendar-integration.md` - Google Calendar 일정 관리 (반복 일정)

## OAuth 2.0 인증 흐름 (개요)

상세 구현은 `modules/oauth-flow.md`를 참조하세요.

### 1단계: Google Cloud 프로젝트 설정

Google Cloud Console에서 프로젝트를 생성하고 API를 사용 설정합니다.

**필수 API:**
- Gmail API
- Google Docs API
- Google Sheets API
- Google Calendar API

### 2단계: OAuth 2.0 클라이언트 생성

**애플리케이션 유형:** 데스크톱 앱
**승인된 리디렉션 URI:** `http://localhost:3000/callback`

### 3단계: OAuth 동의 화면 구성

**필수 범위 (Scopes):**
```
https://www.googleapis.com/auth/gmail.readonly
https://www.googleapis.com/auth/gmail.send
https://www.googleapis.com/auth/documents
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/calendar
```

### 4단계: 토큰 획득 및 저장

```bash
# 환경 변수 설정 (bashrc 또는 zshrc)
export GOOGLE_CLIENT_ID="your_client_id.apps.googleusercontent.com"
export GOOGLE_CLIENT_SECRET="your_client_secret"
export GOOGLE_REFRESH_TOKEN="your_refresh_token"
```

## Gmail 통합

### MCP 도구

```typescript
// 이메일 검색
const emails = await mcp__google-workspace__gmail_search({
  query: 'subject:"regulatory" from:fda.gov',
  maxResults: 10
});

// 이메일 전송
await mcp__google-workspace__gmail_send({
  to: ['regulatory@company.com'],
  subject: '[ARIA] 510(k) Submission Complete',
  body: 'Submission details...'
});
```

### 규제 이메일 사용 사례

**제출 완료 알림:**
- 제목: `[ARIA] 제출 완료: {submissionId}`
- 본문: 제출 ID, 유형, 대상 시장, 제출일, 문서 링크

**CAPA 할당 알림:**
- 제목: `[ARIA] CAPA 할당: {capaId}`
- 본문: 문제 설명, 근본 원인, 마감일

**규제 기관 검색:**
- FDA: `from:fda.gov subject:"regulatory"`
- EU MDR: `from:*.notifiedbody.eu subject:"MDR"`
- MFDS: `from:mfds.go.kr subject:"medical device"`

상세 내용은 `modules/gmail-integration.md`를 참조하세요.

## Google Docs 통합

### MCP 도구

```typescript
const doc = await mcp__google-workspace__docs_create({
  title: 'CAPA Report: CAPA-001',
  content: '# CAPA Report\n...'
});

await mcp__google-workspace__docs_append({
  documentId: doc.documentId,
  content: '## Additional Notes'
});
```

### 문서 템플릿

| 템플릿 | 용도 | 필수 섹션 |
|--------|------|-----------|
| `regulatory-requirement` | 규제 요구사항 | ID, 설명, 카테고리, 준수 방법 |
| `capa-report` | CAPA 보고서 | 문제 설명, 근본 원인, 시정 조치 |
| `risk-assessment` | 위험 평가 | 위험 식별, 심각성, 완화 전략 |
| `audit-report` | 감사 보고서 | 감사 범위, 발견 사항, 권장사항 |

상세 템플릿은 `modules/docs-integration.md`를 참조하세요.

## Google Sheets 통합

### MCP 도구

```typescript
const sheet = await mcp__google-workspace__sheets_create({
  title: 'Risk Register - 2026',
  sheets: [{
    title: 'Risks',
    rowCount: 1000,
    columnCount: 15
  }]
});

await mcp__google-workspace__sheets_append({
  spreadsheetId: sheet.spreadsheetId,
  sheetName: 'Risks',
  rows: [{ risk_id: 'RISK-001', description: '...' }]
});
```

### 스프레드시트 템플릿

| 템플릿 | 용도 | 주요 필드 |
|--------|------|-----------|
| `risk-register` | 위험 등록부 | 위험 ID, 설명, 심각성, 확률, RPN, 완화 전략 |
| `capa-tracker` | CAPA 추적표 | CAPA ID, 문제 설명, 근본 원인, 담당자, 마감일 |
| `submission-tracker` | 제출 추적 | 제출 ID, 유형, 대상 시장, 제출일, 상태 |

### 데이터 분석

**RPN 계산:** `Severity × Probability`
**위험 수준 분류:** High (RPN ≥ 6), Medium (RPN 3-5), Low (RPN 1-2)
**CAPA 노화 보고:** 초과예정, 이번 주 예정, 이번 달 예정, 정상 진행

상세 내용은 `modules/sheets-integration.md`를 참조하세요.

## Google Calendar 통합

### MCP 도구

```typescript
const event = await mcp__google-workspace__calendar_create({
  title: '[FDA] 510(k) Review Meeting',
  description: 'Submission ID: SUB-001',
  start: new Date('2026-02-15T10:00:00'),
  end: new Date('2026-02-15T11:00:00'),
  attendees: ['regulatory@company.com']
});

const events = await mcp__google-workspace__calendar_query({
  timeMin: new Date('2026-02-01'),
  timeMax: new Date('2026-02-28'),
  q: 'regulatory audit compliance'
});
```

### 일정 템플릿

| 이벤트 유형 | 빈도 | 지속 시간 | 참석자 |
|-------------|------|-----------|--------|
| 분기별 내부 감사 | 3개월 | 2시간 | 품질 팀, 규제 팀 |
| 주간 CAPA 검토 | 주간 | 1시간 | 품질 관리자, 생산 팀 |
| 제출 마감 리마인더 | 30일 전 | 1시간 | 규제 팀 |
| 연간 교육 | 연간 | 4시간 | 전체 직원 |

### 색상 코딩

| 카테고리 | 색상 | 설명 |
|----------|------|------|
| FDA | 파랑 (1) | FDA 관련 이벤트 |
| Audit | 초록 (2) | 감사 이벤트 |
| CAPA | 보라 (3) | CAPA 관련 이벤트 |
| Compliance | 빨강 (4) | 규정 준수 작업 |
| Submission | 노랑 (5) | 제출 마감일 |

상세 내용은 `modules/calendar-integration.md`를 참조하세요.

## MCP 도구 로드

### ToolSearch로 도구 검색

```javascript
// Google Workspace MCP 도구 검색 및 로드
ToolSearch("google workspace mcp")
// 이제 mcp__google-workspace__* 도구 사용 가능
```

### 사용 가능한 도구

| 도구 | 기능 | 사용 사례 |
|------|------|-----------|
| `mcp__google-workspace__gmail_search` | 이메일 검색 | 규제 관련 이메일 찾기 |
| `mcp__google-workspace__gmail_send` | 이메일 발송 | CAPA 통지, 제출 알림 |
| `mcp__google-workspace__docs_create` | 문서 생성 | 규제 문서 작성 |
| `mcp__google-workspace__docs_append` | 내용 추가 | 문서 업데이트 |
| `mcp__google-workspace__sheets_create` | 스프레드시트 생성 | 위험 등록부 생성 |
| `mcp__google-workspace__sheets_append` | 데이터 추가 | 위험 데이터 추가 |
| `mcp__google-workspace__sheets_query` | 데이터 조회 | 위험 분석 |
| `mcp__google-workspace__calendar_create` | 일정 생성 | 검토 일정, 감사 일정 |
| `mcp__google-workspace__calendar_query` | 일정 조회 | 일정 확인 |

## Notion 연동

### 동기화 워크플로우

**Sheets → Notion:**
1. Google Sheets에서 데이터 읽기
2. Notion 데이터베이스에 페이지 생성

**Calendar → Notion:**
1. Google Calendar에서 이벤트 조회
2. Notion 데이터베이스에 일정 생성

## 보안 고려사항

### 데이터 보호

1. **HTTPS 전용:** 모든 API 호출은 HTTPS 사용
2. **토큰 저장:** 리프레시 토큰은 안전한 곳에 저장 (시스템 키체인)
3. **최소 권한:** 필요한 API 범위만 요청
4. **감사 로그:** 모든 API 호출 기록
5. **액세스 제어:** 서비스 계정 사용 및 권한 제한

### 환경 변수 관리

**.gitignore에 추가:**
```
.env
.mcp.json.local
```

**시스템별 저장 위치:**
- Linux/macOS: `~/.bashrc` 또는 `~/.zshrc`
- Windows: 시스템 환경 변수

### 토큰 갱신

액세스 토큰은 1시간마다 만료됩니다. 리프레시 토큰을 사용하여 자동 갱신:

```bash
/aria auth google refresh
```

## 모범 사례

1. **Gmail 라벨링:** 규제 이메일 자동 분류
2. **Docs 버전 관리:** 변경 추적 및 협업
3. **Sheets 데이터 유효성:** 데이터 유효성 검사 규칙 사용
4. **Calendar 알림:** 중요 일정 미리 알림 설정
5. **개발 환경:** 테스트 폴더/라벨 사용

## 테스트

### 테스트 케이스

1. **인증 흐름:** OAuth 2.0 전체 흐름 테스트
2. **Gmail 통합:** 이메일 검색, 전송 테스트
3. **Docs 생성:** 각 템플릿별 문서 생성 테스트
4. **Sheets CRUD:** 생성, 조회, 수정, 삭제 테스트
5. **Calendar 일정:** 생성, 조회, 반복 일정 테스트
6. **Notion 연동:** 데이터 동기화 테스트
7. **오류 처리:** 모든 오류 시나리오 테스트

### 테스트 데이터

```typescript
const testData = {
  risk: {
    riskId: 'TEST-RISK-001',
    description: 'Test risk for validation',
    severity: 2,
    probability: 2,
    mitigation: 'Test mitigation strategy'
  },
  capa: {
    capaId: 'TEST-CAPA-001',
    problem: 'Test problem statement',
    rootCause: 'Test root cause',
    targetDate: new Date('2026-03-01')
  }
};
```

## MoAI 통합

### 에이전트 위임

- `manager-spec`: 요구사항 정의
- `expert-backend`: MCP 서버 구현
- `expert-frontend`: 사용자 인터페이스
- `manager-quality`: 보안 검증

### 워크플로우 통합

**Brief Phase:**
- 인증 상태 확인
- 필요한 API 액세스 권한 확인

**Execute Phase:**
- Google Workspace API 호출
- 문서 생성 및 데이터 입력
- 일정 예약

**Deliver Phase:**
- 생성된 문서 링크 제공
- 데이터 요약 보고서 생성
- 다음 단계 권장 사항 제공

## 문제 해결

### 일반적인 문제

**인증 실패:**
```
Error: invalid_client
해결: Google Cloud 자격 증명 확인
```

**토큰 만료:**
```
Error: unauthorized
해결: /aria auth google refresh 실행
```

**API 할당량 초과:**
```
Error: quota_exceeded
해결: 속도 제한 구현, 재시도 로직 추가
```

**MCP 서버 로드 실패:**
```
Error: MCP server not loaded
해결: Claude Code 재시작
```

## 버전 기록

- v2.0.0 (2026-02-09): Phase 4 - 모듈화, /aria auth google 명령 추가
- v1.0.0 (2026-02-09): 초기 릴리스

## 추가 리소스

- [Google API Node.js Client](https://github.com/googleapis/google-api-nodejs-client)
- [Gmail API Documentation](https://developers.google.com/gmail/api)
- [Google Docs API](https://developers.google.com/docs/api)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [Google Calendar API](https://developers.google.com/calendar/api)
