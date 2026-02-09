# ARIA Phase 4 - MCP 통합 시스템

> AI Regulatory Intelligence Assistant (ARIA) Phase 4 - MCP (Model Context Protocol) 통합 시스템. 의료기기 규제 담당자(RA)와 품질 보증(QA) 전문가를 위한 AI 기반 규제 준수 관리 시스템입니다.

## 개요

ARIA는 Claude Code Plugin 아키텍처를 기반으로 구축된 의료기기 RA/QA 전문가 시스템입니다. Phase 4에서는 MCP 서버 통합을 통해 Notion, Google Workspace, Context7 서비스와 연동하여 규제 정보를 중앙 관리합니다.

ARIA는 다음과 같은 작업을 수행합니다:

1. **규제 요구사항 분석**: FDA, MDR, MFDS 규정 자동 검색 및 해석
2. **중앙 데이터 관리**: Notion DB를 통한 규제 문서, CAPA, 위험 관리 통합
3. **협업 도구 연동**: Google Workspace를 통한 팀 협업 및 문서 관리
4. **감사 추적**: 모든 규제 활동에 대한 완전한 감사 추적 제공
5. **지식 베이스**: 최신 규정 정보 자동 업데이트 및 검색

## 주요 기능

### 1. Notion MCP 통합
- 6개 데이터베이스 자동 생성 (Regulatory Requirements, Document Registry, CAPA Tracker, Risk Register, Submission Tracker, Knowledge Base)
- CRUD 작업 지원 (생성, 조회, 수정, 삭제)
- 관계(Relation) 설정으로 데이터 연결
- 감사 추적(Audit Trail) 자동 기록
- 뷰(View) 생성 및 사용자 정의

### 2. Google Workspace MCP 통합
- Gmail: 규제 서신 검색 및 요약
- Google Docs: 협업 문서 생성 및 편집
- Google Sheets: 데이터 분석 및 시각화
- Google Calendar: 데드라인 관리 및 알림
- Google Drive: 파일 저장 및 버전 관리

### 3. Context7 MCP 통합
- 최신 규정 검색 (FDA 21 CFR 820, ISO 13485, EU MDR)
- 자동 지식 베이스 업데이트
- 규정 변경 알림

### 4. 통합 검색
- 모든 데이터 소스를 통합 검색 (Notion, Google, Context7)
- 관련성 점수 기반 정렬
- 필터링 및 정렬 기능

### 5. 상태 대시보드
- CAPA 추적 (Open items, Due dates, Overdue items)
- 위험 등록부 (Unacceptable risks, Review dates)
- 제출 추적 (Upcoming deadlines, Status)
- 문서 등록부 (Pending approvals, Review dates)
- Google Calendar (Upcoming regulatory events)

## 설치

### 사전 요구사항

- Notion workspace 및 API 키
- Google Workspace 계정
- Node.js (MCP 서버 실행)
- Claude Code with MCP support

### MCP 서버 설정

`.mcp.json` 파일에 MCP 서버를 추가합니다:

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
    },
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@anthropic/google-workspace-mcp"],
      "env": {
        "GOOGLE_CREDENTIALS": "${GOOGLE_CREDENTIALS}",
        "GOOGLE_TOKEN_PATH": "${GOOGLE_TOKEN_PATH}"
      }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

### 환경 변수 설정

```bash
export NOTION_API_KEY="your_notion_integration_token"
export NOTION_DATABASE_ID="your_parent_database_id"
export GOOGLE_CREDENTIALS="path_to_credentials.json"
export GOOGLE_TOKEN_PATH="path_to_token.json"
```

## 빠른 시작

### ARIA 초기화

```bash
/aria init notion   # Notion DB 생성 및 설정
/aria init google   # Google Workspace OAuth 설정
/aria init all      # 모든 통합 초기화
```

### 검색 및 조회

```bash
# 통합 검색
/aria search "510(k) submission requirements"

# 지식 베이스 조회
/aria knowledge "MDR classification rules"

# 상태 대시보드
/aria status
```

## 사용법

### 초기화 명령어

```bash
/aria init notion   # Notion 데이터베이스 생성
/aria init google   # Google Workspace OAuth 설정
/aria init all      # 모든 통합 초기화
```

### 검색 명령어

```bash
/aria search "510(k) submission requirements"
/aria search email "FDA 510(k) request"
/aria search docs "DHF Review"
```

### 지식 베이스 조회

```bash
/aria knowledge "MDR classification rules"
/aria knowledge "ISO 13485 Clause 8.5.2"
```

### 상태 대시보드

```bash
/aria status         # 전체 프로젝트 상태
/aria status capa    # CAPA 상태만 조회
/aria status risk    # 위험 상태만 조회
```

### 감사 추적

```bash
/aria audit search --agent expert-regulatory --date "2026-01-01:2026-02-09"
/aria audit export --format csv
```

## 아키텍처

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

### 에이전트 구조

**Coordinator:**
- `aria-orchestrator`: 워크플로우 조정 및 MCP 통합 관리

**Domain Experts (8개):**
1. `aria-regulatory`: FDA, MDR, MFDS 규정
2. `aria-clinical`: 임상 평가 요구사항
3. `aria-quality`: QMS, CAPA, 감사 준비
4. `aria-risk`: ISO 14971 위험 관리
5. `aria-postmarket`: 시판 후 조사, PMCF, 불만
6. `aria-document`: 기술 문서, 라벨링
7. `aria-submission`: 510(k), CE, PMA 제출
8. `aria-labeling`: IFU, 라벨, UDI

### Skills (3개)

1. `aria-integration-notion`: Notion MCP 통합
2. `aria-integration-google`: Google Workspace MCP 통합
3. `aria-integration-context7`: Context7 MCP 통합

### Commands (5개)

1. `/aria init`: 초기화 (notion, google, all)
2. `/aria search`: 통합 검색
3. `/aria knowledge`: 지식 베이스 조회
4. `/aria status`: 상태 대시보드
5. `/aria audit`: 감사 추적

## 워크플로우

### Brief-Execute-Deliver 방법론

**Brief Phase:**
1. 사용자 요청 분석 및 규제 도메인 식별
2. 핵심 요구사항 및 제약조건 추출
3. 적용 가능한 규정 식별 (FDA, MDR, MFDS, ISO 13485)
4. 전달물 및 수락 기준 정의

**Execute Phase:**
1. 적절한 도메인 전문가 에이전트에 위임
2. MCP 통합 조정 (Notion, Google, Context7)
3. 작업 완료 및 품질 게이트 모니터링

**Deliver Phase:**
1. 추적 가능성을 포함한 전달물 컴파일
2. Notion DB 감사 추적 업데이트
3. 컴플라이언스 문서 생성

### VALID 품질 프레임워크

모든 전달물은 VALID 프레임워크를 충족해야 합니다:

- **Verified:** 규정 출처에서 요구사항 검증
- **Accurate:** 규정 해석 정확성 보장
- **Linked:** 구체적 규정 조항과 연결
- **Inspectable:** 감사 준비 형식 제공
- **Deliverable:** 제출 준비 전달물 생성

## 사용 예시

### 예시 1: 510(k) 제출 준비

```bash
# Brief Phase
/aria search "510(k) submission requirements for software medical device"

# Execute Phase
# aria-submission 에이전트가 자동으로 위임됨
# Notion Submission Tracker DB 업데이트
# Google Calendar에 데드라인 추가

# Deliver Phase
/aria status submission
/aria audit search --entity submission
```

### 예시 2: CAPA 생성

```bash
# Brief Phase
# 비준수 문제 식별

# Execute Phase
/aria init notion  # CAPA Tracker DB 확인
# aria-quality 에이전트가 CAPA 생성
# Google Calendar에 Due Date 추가
# Google Docs에 CAPA 문서 생성

# Deliver Phase
/aria status capa
/aria audit search --entity capa
```

### 예시 3: 규정 검색

```bash
# Brief Phase
/aria knowledge "ISO 14971 risk management requirements"

# Execute Phase
# Context7 MCP에서 ISO 14971 검색
# Notion Knowledge Base에 저장

# Deliver Phase
/aria search "risk management"
```

## 문서 구조

```
ARIA Phase 4/
├── .claude/
│   ├── agents/aria/           # ARIA 에이전트 (9개)
│   │   ├── aria-orchestrator.md
│   │   ├── aria-regulatory.md
│   │   ├── aria-clinical.md
│   │   ├── aria-quality.md
│   │   ├── aria-risk.md
│   │   ├── aria-postmarket.md
│   │   ├── aria-document.md
│   │   ├── aria-submission.md
│   │   └── aria-labeling.md
│   ├── commands/aria/         # ARIA 명령어 (5개)
│   │   ├── init.md
│   │   ├── search.md
│   │   ├── knowledge.md
│   │   ├── status.md
│   │   └── audit.md
│   └── skills/aria-*/         # ARIA 스킬 (3개)
│       ├── aria-integration-notion/SKILL.md
│       ├── aria-integration-google/SKILL.md
│       └── aria-integration-context7/SKILL.md
├── .moai/specs/SPEC-ARIA-004/ # SPEC 문서
└── .mcp.json                   # MCP 서버 설정
```

## 품질 보증

### 감사 추적

모든 데이터 변경은 자동으로 감사 로그에 기록됩니다:

- **Timestamp**: 변경 시간 (ISO 8601)
- **User**: 변경자
- **Action**: 생성, 수정, 아카이브
- **Entity**: 영향 받은 데이터베이스/페이지
- **Changes**: 변경 전후 값 비교
- **Reason**: 변경 사유

### 추적성 매트릭스

요구사항 → 문서 → 증거 연결을 유지합니다:

- Regulatory Requirements → Document Registry
- CAPA Tracker → Risk Register
- Submission Tracker → Document Registry
- Knowledge Base → Regulatory Requirements

## 문제 해결

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

### Google OAuth 인증 만료

```
오류: Google OAuth 토큰이 만료되었습니다.
해결 방법:
1. /aria auth google 실행
2. 브라우저에서 재인증 수행
3. 새로운 토큰 저장
```

## 기여

ARIA 프로젝트에 기여하고 싶으시다면:

1. Fork 하세요
2. 기능 브랜치를 만드세요 (`git checkout -b feature/AmazingFeature`)
3. 커밋하세요 (`git commit -m 'Add some AmazingFeature'`)
4. 푸시하세요 (`git push origin feature/AmazingFeature`)
5. Pull Request를 여세요

## 라이선스

Apache-2.0 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.

## 연락처

- 프로젝트 홈페이지: https://github.com/moai-ai/aria
- 이슈 추적: https://github.com/moai-ai/aria/issues
- 문서: https://aria.moai.ai

---

**버전:** 1.0.0
**최종 업데이트:** 2026-02-09
**상태:** Production Ready
**SPEC:** SPEC-ARIA-004
