---
name: aria-integration-notion
description: >
  Notion MCP 서버 연동을 위한 ARIA 스킬. 규제 요구사항 관리를 위한 6개 데이터베이스 스키마 자동 생성,
  CRUD 작업, 감사 추적 기능을 제공합니다. 의료기기 규제 준수 문서 관리에 사용합니다.
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
  tags: "notion, mcp, regulatory, database, crud, audit, aria"
  author: "MoAI-ARIA"
  context7-libraries: "notion-sdk"
  argument-hint: "Notion 데이터베이스 작업 수행"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords:
    - "notion"
    - "mcp"
    - "regulatory"
    - "database"
    - "crud"
    - "audit"
    - "규제"
    - "데이터베이스"
    - "감사"
  agents:
    - "expert-backend"
    - "manager-spec"
  phases:
    - "plan"
    - "run"
  languages:
    - "typescript"
    - "python"
---

# ARIA Notion Integration

ARIA 규제 관리 시스템을 위한 Notion MCP 연동 스킬입니다.

## 빠른 시작

### MCP 서버 설정

`.mcp.json`에 Notion MCP 서버를 추가합니다:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "your_notion_integration_token",
        "NOTION_DATABASE_ID": "your_parent_database_id"
      }
    }
  }
}
```

### 환경 변수 설정

```bash
export NOTION_API_KEY="your_notion_integration_token"
export NOTION_DATABASE_ID="your_parent_database_id"
```

## 데이터베이스 스키마

### 1. Regulatory Requirements (규제 요구사항)

| 속성 | 타입 | 설명 |
|------|------|------|
| Requirement ID | Title | 고유 식별자 (REQ-001) |
| Category | Select | FDA, ISO 13485, EU MDR |
| Description | Text | 요구사항 상세 설명 |
| Status | Status | Draft, Review, Approved |
| Priority | Select | High, Medium, Low |
| Due Date | Date | 준수 마감일 |
| Owner | Person | 담당자 |
| Evidence Link | Url | 증거 문서 링크 |

### 2. Document Registry (문서 등록부)

| 속성 | 타입 | 설명 |
|------|------|------|
| Document ID | Title | 문서 고유 ID |
| Document Type | Select | SOP, WI, FORM, RECORD |
| Version | Number | 문서 버전 |
| Title | Text | 문서 제목 |
| Status | Status | Draft, Under Review, Approved, Obsolete |
| Effective Date | Date | 발효일 |
| Review Date | Date | 검토 예정일 |
| Approved By | Person | 승인자 |

### 3. CAPA Tracker (시정예방조치)

| 속성 | 타입 | 설명 |
|------|------|------|
| CAPA ID | Title | CAPA 고유 ID |
| Source | Select | Internal Audit, Customer Complaint, Nonconformance |
| Problem Statement | Text | 문제 설명 |
| Root Cause | Text | 근본 원인 분석 |
| Correction Action | Text | 시정 조치 |
| Prevention Action | Text | 예방 조치 |
| Status | Status | Open, In Progress, Closed |
| Due Date | Date | 완료 마감일 |

### 4. Risk Register (위험 등록부)

| 속성 | 타입 | 설명 |
|------|------|------|
| Risk ID | Title | 위험 고유 ID |
| Risk Description | Text | 위험 설명 |
| Risk Category | Select | Clinical, Technical, Regulatory |
| Severity | Select | High (3), Medium (2), Low (1) |
| Probability | Select | High (3), Medium (2), Low (1) |
| RPN Number | Number | 위험 우선순위 번호 (Severity × Probability) |
| Mitigation Strategy | Text | 완화 전략 |
| Residual Risk | Select | Acceptable, Not Acceptable |

### 5. Submission Tracker (제출 추적)

| 속성 | 타입 | 설명 |
|------|------|------|
| Submission ID | Title | 제출물 고유 ID |
| Submission Type | Select | 510(k), PMA, CE Mark |
| Target Market | Select | USA, EU, Korea, Japan |
| Submission Date | Date | 제출일 |
| Approval Date | Date | 승인일 |
| Status | Status | Preparing, Submitted, Under Review, Approved, Rejected |
| Reviewer | Select | FDA, NB, MFDS |

### 6. Knowledge Base (지식 기반)

| 속성 | 타입 | 설명 |
|------|------|------|
| Article ID | Title | 문서 고유 ID |
| Category | Select | Regulation, Guideline, Best Practice |
| Tags | Multi-select | FDA, ISO, MDR, QSR |
| Content | Text | 문서 내용 |
| Source | Url | 출처 URL |
| Last Updated | Date | 최종 업데이트 |
| TTL | Number | 캐시 만료 시간 (초) |

## CRUD 작업

### Create (생성)

```bash
# 새로운 규제 요구사항 생성
aria-tool-notion create \
  --database "Regulatory Requirements" \
  --properties '{"Requirement ID": "REQ-001", "Category": "FDA", "Status": "Draft"}'
```

### Read (조회)

```bash
# 모든 요구사항 조회
aria-tool-notion query \
  --database "Regulatory Requirements" \
  --filter '{"property": "Status", "equals": "Approved"}'

# 특정 ID로 조회
aria-tool-notion retrieve --page-id "page_id_here"
```

### Update (수정)

```bash
# 요구사항 상태 수정
aria-tool-notion update \
  --page-id "page_id_here" \
  --properties '{"Status": "Approved"}'
```

### Delete (삭제)

```bash
# 페이지 아카이브 (Soft Delete)
aria-tool-notion archive --page-id "page_id_here"
```

## 감사 추적

### 감사 로그 항목

모든 데이터 변경은 다음 정보를 자동으로 기록합니다:

- **Timestamp**: 변경 시간 (ISO 8601)
- **User**: 변경자
- **Action**: 생성, 수정, 아카이브
- **Entity**: 영향 받은 데이터베이스/페이지
- **Changes**: 변경 전후 값 비교
- **Reason**: 변경 사유

### 감사 로그 조회

```bash
# 최근 변경 내역 조회
aria-tool-notion audit-log \
  --database "Regulatory Requirements" \
  --limit 50 \
  --since "2026-02-01"
```

## MCP 도구 사용

### ToolSearch로 도구 로드

```javascript
// Notion MCP 도구 검색 및 로드
ToolSearch("notion mcp")
// mcp__notion__* 도구 사용 가능
```

### 사용 가능한 도구

- `mcp__notion__create-page`: 페이지 생성
- `mcp__notion__query-database`: 데이터베이스 쿼리
- `mcp__notion__update-page`: 페이지 수정
- `mcp__notion__archive-page`: 페이지 아카이브
- `mcp__notion__append-blocks`: 블록 추가

## 모범 사례

1. **데이터베이스 관계**: 관련 페이지 간 Relation 속성으로 연결
2. **템플릿 사용**: 반복 작업을 위해 템플릿 정의
3. **속성 유효성**: Select 옵션으로 데이터 일관성 유지
4. **감사 추적**: 모든 중요 변경에 감사 로그 기록
5. **액세스 제어**: Notion 통합 권한을 최소 권한으로 설정

## MoAI 통합

- `manager-spec`: 규제 요구사항 분석
- `expert-backend`: MCP 서버 구성
- `manager-quality`: 감사 추적 검증

버전 기록:
- v1.0.0 (2026-02-09): 초기 릴리스
