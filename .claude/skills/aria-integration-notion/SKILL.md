---
name: aria-integration-notion
description: >
  Notion MCP 서버 연동을 위한 ARIA 스킬. 규제 요구사항 관리를 위한 6개 데이터베이스 스키마 자동 생성,
  CRUD 작업, 감사 추적 기능을 제공합니다. 의료기기 규제 준수 문서 관리에 사용합니다.
license: Apache-2.0
compatibility: Designed for Claude Code
allowed-tools: Read Write Edit Bash
user-invocable: true
metadata:
  version: "2.1.0"
  category: "domain"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "notion, mcp, regulatory, database, crud, audit, traceability, capa, risk, aria"
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
    - "regulatory database"
    - "crud"
    - "audit trail"
    - "database creation"
    - "규제"
    - "데이터베이스"
    - "감사"
  agents:
    - "expert-backend"
    - "manager-spec"
    - "manager-quality"
  phases:
    - "plan"
    - "run"
    - "sync"
  languages:
    - "typescript"
    - "python"
---

# ARIA Notion Integration

ARIA 규제 관리 시스템을 위한 Notion MCP 연동 스킬입니다. 6개 데이터베이스 자동 생성, CRUD 작업, 감사 추적 기능을 제공합니다.

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

### 초기화 명령어

```bash
# Notion 데이터베이스 초기화
/aria init notion
```

이 명령어는 6개 데이터베이스를 자동으로 생성합니다:
- Regulatory Requirements (규제 요구사항)
- Document Registry (문서 등록부)
- CAPA Tracker (시정예방조치)
- Risk Register (위험 등록부)
- Submission Tracker (제출 추적)
- Knowledge Base (지식 기반)

## 핵심 기능

### 1. 데이터베이스 자동 생성

Phase 3 스키마를 기반으로 6개 데이터베이스를 자동 생성합니다. 각 데이터베이스는 규제 준수 요구사항에 맞게 구성됩니다.

### 2. CRUD 작업

생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 작업을 지원합니다. 모든 작업은 감사 로그에 기록됩니다.

### 3. 감사 추적

모든 데이터 변경은 자동으로 감사 로그에 기록됩니다:
- 변경 시간 (Timestamp)
- 변경자 (User)
- 작업 유형 (Action)
- 영향 받은 엔티티 (Entity)
- 변경 전후 값 (Changes)
- 변경 사유 (Reason)

## 상세 가이드

데이터베이스 스키마, CRUD 작업, 고급 기능의 상세 내용은 모듈 문서를 참조하세요:

**기본 모듈**:
- [데이터베이스 생성 가이드](modules/database-creation.md)
- [CRUD 작업 레퍼런스](modules/crud-operations.md)
- [감사 추적 시스템](modules/audit-trail.md)
- [MCP 도구 레퍼런스](modules/mcp-tools.md)

**고급 기능 모듈 (Milestone 2)**:
- [추적성 매트릭스](modules/traceability.md) - 요구사항, 문서, 증거 간 추적성 관리
- [CAPA Tracker](modules/capa-tracker.md) - 시정예방조치 자동 등록 및 관리
- [Risk Register](modules/risk-register.md) - 위험 자동 등록 및 Risk Index 계산
- [Document Registry](modules/document-registry.md) - 문서 자동 등록 및 버전 관리
- [Quality Validation](modules/quality-validation.md) - 데이터 무결성 검증

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
- `mcp__notion__create-database`: 데이터베이스 생성

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

## 고급 기능

### 4. 추적성 매트릭스

요구사항, 문서, 증거 간의 종단 추적성을 관리합니다:
- Requirements ↔ Documents ↔ Evidence 관계
- 자동 관계 설정
- 고아 페이지 탐지

### 5. CAPA 자동 관리

시정 및 예방 조치를 자동으로 관리합니다:
- CAPA 자동 등록 (CAPA-ID 생성)
- Risk Register 연동
- 마감일 알림 (Google Calendar 연동)

### 6. 위험 관리

ISO 14971 위험 관리를 지원합니다:
- 위험 자동 등록 (Risk ID 생성)
- Risk Index 자동 계산 (Severity × Probability)
- 수용성 평가 (Acceptable, Not Acceptable, ALARP)
- 허용 불가능 위험 경고

### 7. 문서 관리

품질 시스템 문서를 자동으로 관리합니다:
- 문서 자동 등록 (Document ID 생성)
- 버전 히스토리 관리 (Major.Minor)
- 검토일 알림 (SOP: 2년, WI: 1년, FORM: 3년)

### 8. 품질 검증

데이터 무결성을 보장합니다:
- 관계 무결성 검증
- 고아 페이지 탐지 및 경고
- 감사 추적 완전성 검사

버전 기록:
- v2.1.0 (2026-02-09): Milestone 2 - 고급 기능 모듈 추가
- v2.0.0 (2026-02-09): 모듈화 구조로 개편
- v1.0.0 (2026-02-09): 초기 릴리스
