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
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "false"
  tags: "google, workspace, gmail, docs, sheets, calendar, oauth, aria"
  author: "MoAI-ARIA"
  context7-libraries: "google-api-nodejs-client"
  argument-hint: "Google Workspace 서비스 통합"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
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
    - "구글"
    - "이메일"
    - "문서"
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

### MCP 서버 설정

.mcp.json에 Google Workspace MCP 서버를 추가합니다:

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-workspace"],
      "env": {
        "GOOGLE_CLIENT_ID": "PLACEHOLDER_CLIENT_ID.apps.googleusercontent.com",
        "GOOGLE_CLIENT_SECRET": "PLACEHOLDER_CLIENT_SECRET",
        "GOOGLE_REDIRECT_URI": "http://localhost:3000/callback",
        "GOOGLE_REFRESH_TOKEN": "PLACEHOLDER_REFRESH_TOKEN"
      }
    }
  }
}
```

### OAuth 2.0 인증 흐름

#### 1단계: Google Cloud 프로젝트 설정

Google Cloud Console에서 프로젝트를 생성하고 API 및 서비스 사용자 인증 정보로 이동합니다.

OAuth 2.0 클라이언트 ID를 생성합니다:
- 애플리케이션 유형: 데스크톱 앱
- 승인된 리디렉션 URI: http://localhost:3000/callback

#### 2단계: API 사용 설정

사용 설정해야 할 API:
- Gmail API
- Google Docs API
- Google Sheets API
- Google Calendar API

#### 3단계: OAuth 동의 화면 구성

앱 정보:
- 앱 이름: ARIA Regulatory Manager
- 사용자 지원 이메일: (관리자 이메일)
- 개발자 연락처 정보: (관리자 이메일)

범위 (Scopes):
- https://www.googleapis.com/auth/gmail.readonly
- https://www.googleapis.com/auth/gmail.send
- https://www.googleapis.com/auth/documents
- https://www.googleapis.com/auth/spreadsheets
- https://www.googleapis.com/auth/calendar

#### 4단계: 토큰 획득

인증 코드 획득 및 액세스 토큰 교환 표준 OAuth 2.0 흐름을 따릅니다.

### 환경 변수 설정

bashrc 또는 zshrc에 환경 변수를 추가합니다 (실제 값으로 교체 필요):

```bash
export GOOGLE_CLIENT_ID="your_actual_client_id.apps.googleusercontent.com"
export GOOGLE_CLIENT_SECRET="your_actual_client_secret"
export GOOGLE_REDIRECT_URI="http://localhost:3000/callback"
export GOOGLE_REFRESH_TOKEN="your_actual_refresh_token"
```

## Gmail 통합

### 이메일 검색

규제 관련 이메일 검색 및 라벨별 필터링을 지원합니다.

### 이메일 전송

CAPA 통지, 제출 완료 알림 등의 이메일을 발송할 수 있습니다.

### 이메일 템플릿

제출 완료 알림 템플릿 예시:
- 제목: [ARIA] 제출 완료: 제출ID
- 본문: 제출 ID, 유형, 대상 시장, 제출일, 문서 링크 포함

## Google Docs 통합

### 문서 생성

규제 요구사항 문서, CAPA 보고서, 위험 평가, 감사 보고서 등을 생성합니다.

### 문서 템플릿

| 템플릿 이름 | 용도 | 필수 섹션 |
|-------------|------|-----------|
| regulatory-requirement | 규제 요구사항 | ID, 설명, 카테고리, 준수 방법 |
| capa-report | CAPA 보고서 | 문제 설명, 근본 원인, 시정 조치 |
| risk-assessment | 위험 평가 | 위험 식별, 심각성, 완화 전략 |
| audit-report | 감사 보고서 | 감사 범위, 발견 사항, 권장사항 |

## Google Sheets 통합

### 스프레드시트 생성

위험 등록부, CAPA 추적표 등을 생성합니다.

### 데이터 쓰기 및 읽기

위험 등록부에 데이터를 추가하고 RPN 점수를 계산합니다.

### 캘린더 통합

### 일정 생성

규제 검토 일정, 감사 일정 등을 생성합니다.

### 일정 조회

지정된 기간의 규제 관련 일정을 조회합니다.

### 반복 일정 설정

분기별 내부 감사와 같은 정기 일정을 설정합니다.

## MCP 도구 사용

### ToolSearch로 도구 로드

Google Workspace MCP 도구를 검색하고 로드합니다.

### 사용 가능한 도구

| 도구 | 기능 | 사용 사례 |
|------|------|-----------|
| Gmail 검색 | 이메일 검색 | 규제 관련 이메일 찾기 |
| Gmail 전송 | 이메일 발송 | CAPA 통지, 제출 알림 |
| Docs 생성 | 문서 생성 | 규제 문서 작성 |
| Docs 추가 | 내용 추가 | 문서 업데이트 |
| Sheets 추가 | 데이터 추가 | 위험 등록부 업데이트 |
| Sheets 조회 | 데이터 조회 | 위험 분석 |
| Calendar 생성 | 일정 생성 | 검토 일정, 감사 일정 |
| Calendar 조회 | 일정 조회 | 일정 확인 |

## 보안 고려사항

### 데이터 보호

1. 모든 전송은 HTTPS 사용
2. 리프레시 토큰은 안전한 곳에 저장
3. 필요한 API 범위만 요청 (최소 권한)
4. 모든 API 호출 기록 (감사 로그)

### 액세스 제어

서비스 계정을 사용하고 권한을 제한합니다.

## 모범 사례

1. Gmail 라벨로 규제 이메일 자동 분류
2. Google Docs 버전 기록으로 변경 추적
3. Sheets 데이터 유효성 검사 규칙 사용
4. Calendar 알림으로 중요 일정 미리 알림
5. 개발 중에는 테스트 폴더/라벨 사용

## MoAI 통합

- manager-spec: 요구사항 정의
- expert-backend: API 구현
- expert-frontend: UI 통합
- manager-quality: 보안 검증

버전 기록:
- v1.0.0 (2026-02-09): 초기 릴리스
