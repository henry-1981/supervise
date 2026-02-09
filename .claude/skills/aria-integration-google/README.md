# ARIA Google Workspace Integration

Google Workspace MCP 서버 연동을 위한 ARIA 스킬입니다. Gmail, Docs, Sheets, Calendar 통합과 OAuth 2.0 인증 흐름을 제공합니다.

## 기능

### OAuth 2.0 인증
- Google Cloud 프로젝트 설정 자동화
- OAuth 2.0 동의 화면 구성
- 인증 코드 획득 및 토큰 교환
- 액세스 토큰 자동 갱신
- 토큰 만료 모니터링

### Gmail 통합
- 규제 관련 이메일 검색
- CAPA 통지, 제출 완료 알림 발송
- 이메일 템플릿 (제출 완료, CAPA 할당)
- 라벨 자동 분류 규칙

### Google Docs 통합
- 규제 요구사항 문서 생성
- CAPA 보고서 생성
- 위험 평가 문서 생성
- 감사 보고서 생성
- Markdown 형식 지원

### Google Sheets 통합
- 위험 등록부 생성 및 관리
- CAPA 추적표 생성 및 관리
- 제출 추적표 생성 및 관리
- RPN (Risk Priority Number) 자동 계산
- 데이터 유효성 검사 규칙

### Google Calendar 통합
- 규제 검토 일정 생성
- 감사 일정 생성
- 반복 일정 설정 (분기별, 주간)
- 제출 마감 리마인더
- 색상 코딩 (FDA, Audit, CAPA, Compliance)

## 사용법

### 1. 인증 설정

```bash
/aria auth google setup
```

### 2. 인증 상태 확인

```bash
/aria auth google status
```

### 3. 토큰 갱신

```bash
/aria auth google refresh
```

### 4. MCP 도구 사용

```javascript
// Google Workspace MCP 도구 로드
ToolSearch("google workspace mcp")

// 이메일 검색
const emails = await mcp__google-workspace__gmail_search({
  query: 'subject:"regulatory"',
  maxResults: 10
});

// 문서 생성
const doc = await mcp__google-workspace__docs_create({
  title: 'CAPA Report',
  content: '# CAPA Report\n...'
});
```

## 구조

```
aria-integration-google/
├── SKILL.md                 # 메인 스킬 파일 (Progressive Disclosure)
├── modules/                 # 상세 모듈 (Level 3 - On-Demand)
│   ├── oauth-flow.md        # OAuth 2.0 상세 구현
│   ├── gmail-integration.md # Gmail API 통합
│   ├── docs-integration.md  # Google Docs 문서 생성
│   ├── sheets-integration.md# Google Sheets 데이터 관리
│   └── calendar-integration.md # Google Calendar 일정 관리
├── tests/                   # TDD 테스트 파일
│   └── oauth-flow.test.ts   # OAuth 흐름 테스트
├── templates/               # 문서 템플릿
│   ├── regulatory-requirement.md
│   ├── capa-report.md
│   ├── risk-assessment.md
│   └── audit-report.md
└── README.md               # 이 파일
```

## Progressive Disclosure

### Level 1: 메타데이터 (~100 토큰)
- 항상 로드됨
- 스킬 이름, 설명, 버전
- 트리거 키워드

### Level 2: 핵심 기능 (~5000 토큰)
- 트리거 시 로드
- OAuth 2.0 개요
- MCP 도구 인터페이스
- 기본 사용 예시

### Level 3: 상세 모듈 (On-Demand)
- 필요시 로드
- 전체 코드 예제
- 상세 구현 가이드
- 테스트 케이스

## 의존성

### 필수 MCP 서버
- `@modelcontextprotocol/server-google-workspace`

### 선택적 MCP 서버
- `@modelcontextprotocol/server-notion` (Notion 연동)

### 환경 변수
```bash
GOOGLE_CLIENT_ID="your_client_id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="your_client_secret"
GOOGLE_REDIRECT_URI="http://localhost:3000/callback"
GOOGLE_REFRESH_TOKEN="your_refresh_token"
```

## 보안

1. **HTTPS 전용:** 모든 API 호출은 HTTPS 사용
2. **토큰 저장:** 리프레시 토큰은 안전한 곳에 저장
3. **최소 권한:** 필요한 API 범위만 요청
4. **감사 로그:** 모든 API 호출 기록
5. **액세스 제어:** 서비스 계정 사용 및 권한 제한

## 테스트

```bash
# Jest 설치
npm install --save-dev jest @types/jest ts-jest

# 테스트 실행
npm test

# 커버리지 확인
npm test -- --coverage
```

## 라이선스

Apache-2.0

## 버전

- v2.0.0 (2026-02-09): Phase 4 - 모듈화, /aria auth google 명령 추가
- v1.0.0 (2026-02-09): 초기 릴리스

## 기여

ARIA Core Team
