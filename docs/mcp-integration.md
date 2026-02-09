# MCP Integration Guide

MoAI ARIA Phase 2를 위한 MCP(Model Context Protocol) 서버 통합 가이드입니다.

## 개요

ARIA 시스템은 여러 MCP 서버를 사용하여 각 에이전트의 기능을 확장합니다. 이 문서는 어떤 에이전트가 어떤 MCP 서버를 사용하는지, 그리고 도구를 로드하는 방법을 설명합니다.

## 구성된 MCP 서버

### 1. Context7 MCP

**용도**: 최신 라이브러리 문서 및 코드 예제 조회

**사용 에이전트**:
- `expert-researcher`: 문서 연구
- `expert-writer`: 기술 작성 시 참조

**주요 도구**:
- `mcp__context7__resolve-library-id`: 라이브러리 식별자 찾기
- `mcp__context7__query-docs`: 문서 쿼리

**로드 패턴**:
```javascript
ToolSearch("context7 library")
// 사용 가능해짐: mcp__context7__resolve-library-id, mcp__context7__query-docs
```

### 2. Sequential Thinking MCP

**용도**: 복잡한 문제에 대한 단계별 분석

**사용 에이전트**:
- `expert-analyst`: 복잡한 분석 작업
- `expert-architect`: 아키텍처 의사결정
- `expert-researcher`: 단계별 연구 수행

**주요 도구**:
- `mcp__sequential-thinking__sequentialthinking`: 단계별 추론

**로드 패턴**:
```javascript
ToolSearch("sequential thinking")
// 사용 가능해짐: mcp__sequential-thinking__sequentialthinking
```

### 3. Notion MCP

**용도**: Notion 문서 통합 및 지식 관리

**사용 에이전트**:
- `manager-docs`: 문서 생성 및 동기화
- `knowledge` 명령: Notion 지식베이스 관리

**주요 도구**:
- `mcp__claude_ai_Notion__notion-search`: Notion 검색
- `mcp__claude_ai_Notion__notion-fetch`: Notion 페이지 가져오기
- `mcp__claude_ai_Notion__notion-create-pages`: 페이지 생성
- `mcp__claude_ai_Notion__notion-update-page`: 페이지 업데이트
- `mcp__claude_ai_Notion__notion-move-pages`: 페이지 이동
- `mcp__claude_ai_Notion__notion-duplicate-page`: 페이지 복제
- `mcp__claude_ai_Notion__notion-create-database`: 데이터베이스 생성
- `mcp__claude_ai_Notion__notion-update-data-source`: 데이터 소스 업데이트
- `mcp__claude_ai_Notion__notion-create-comment`: 댓글 생성
- `mcp__claude_ai_Notion__notion-get-comments`: 댓글 가져오기
- `mcp__claude_ai_Notion__notion-get-teams`: 팀 정보 가져오기
- `mcp__claude_ai_Notion__notion-get-users`: 사용자 정보 가져오기

**로드 패턴**:
```javascript
ToolSearch("notion")
// 사용 가능해짐: 모든 mcp__claude_ai_Notion__* 도구들
```

## 도구 로드 프로세스

MCP 도구는 지연 로딩(deferred loading) 방식으로 동작합니다.

### 필수 단계

1. **ToolSearch로 도구 찾기**
   ```javascript
   ToolSearch({ query: "context7", maxResults: 5 })
   ```

2. **도구 직접 호출**
   ```javascript
   mcp__context7__resolve-library-id({ libraryName: "react" })
   ```

### 로드 후 사용 가능한 도구

| MCP 서버 | 접두사 | 도구 수 |
|---------|--------|--------|
| Context7 | `mcp__context7__` | 2개 |
| Sequential Thinking | `mcp__sequential-thinking__` | 1개 |
| Notion | `mcp__claude_ai_Notion__` | 12개 |

## 에이전트-MCP 매핑

| 에이전트 | Context7 | Sequential Thinking | Notion |
|---------|----------|-------------------|--------|
| expert-researcher | ✅ | ✅ | ❌ |
| expert-writer | ✅ | ❌ | ❌ |
| expert-analyst | ❌ | ✅ | ❌ |
| expert-architect | ❌ | ✅ | ❌ |
| manager-docs | ❌ | ❌ | ✅ |
| knowledge 명령 | ❌ | ❌ | ✅ |

## 폴백 메커니즘

### MCP 서버 연결 실패 시

1. **자동 재시도**: 최대 3회 재시도
2. **그레이스풀 디그레이션**: MCP 기능 없이 기본 기능만 수행
3. **사용자 알림**: 실패 사항을 로깅하고 사용자에게 알림

### 도구 로드 실패 시

1. **대안 수단**: 웹 검색(WebSearch)으로 대체
2. **로컬 캐시**: 이전에 로드한 정보 활용
3. **에러 보고**: 실패한 도구와 이유를 보고

## 환경 변수 설정

일부 MCP 서버는 추가 인증이 필요할 수 있습니다.

### Notion MCP 인증

```bash
# Notion API Key 필요
export NOTION_API_KEY="your_notion_integration_token"
export NOTION_DATABASE_ID="your_database_id"
```

### Context7 MCP

현재 공개 버전으로 별도 인증 불필요.

### Sequential Thinking MCP

현재 공개 버전으로 별도 인증 불필요.

## 사용 예제

### 예제 1: 문서 검색 (Context7)

```javascript
// 1. 도구 로드
ToolSearch({ query: "context7", maxResults: 5 })

// 2. 라이브러리 검색
const result = await mcp__context7__resolve-library-id({
  libraryName: "react",
  version: "18"
})

// 3. 문서 가져오기
const docs = await mcp__context7__query-docs({
  libraryId: result.id,
  query: "hooks"
})
```

### 예제 2: 복잡한 분석 (Sequential Thinking)

```javascript
// 1. 도구 로드
ToolSearch({ query: "sequential thinking", maxResults: 5 })

// 2. 단계별 분석
const analysis = await mcp__sequential-thinking__sequentialthinking({
  prompt: "아키텍처 비교 분석",
  context: "현재 시스템 상태"
})
```

### 예제 3: Notion 문서 생성

```javascript
// 1. 도구 로드
ToolSearch({ query: "notion", maxResults: 5 })

// 2. 페이지 생성
const page = await mcp__claude_ai_Notion__notion-create-pages({
  parentId: "parent_page_id",
  title: "새 문서",
  content: "문서 내용"
})
```

## 모범 사례

1. **도구 로드 먼저**: MCP 도구를 사용하기 전에 항상 ToolSearch로 먼저 로드
2. **에러 핸들링**: 모든 MCP 호출은 try-catch로 감싸기
3. **폴백 준비**: MCP가 실패할 경우를 대비한 대안 준비
4. **인증 확인**: 인증이 필요한 서버는 환경 변수 설정 확인
5. **토큰 최적화**: 불필요한 MCP 호출은 피하고 결과 캐싱 활용

## 문제 해결

### 문제: MCP 도구를 찾을 수 없음

**원인**: ToolSearch를 호출하지 않음

**해결**:
```javascript
// 잘못된 방법
mcp__context7__resolve-library-id({ ... })  // 에러!

// 올바른 방법
ToolSearch({ query: "context7" })
mcp__context7__resolve-library-id({ ... })  // 성공
```

### 문제: Notion MCP 인증 실패

**원인**: API 키 미설정

**해결**:
```bash
export NOTION_API_KEY="your_key"
```

### 문제: MCP 서버 연결 시간 초과

**원인**: 네트워크 문제 또는 서버 다운

**해결**: `.mcp.json`에서 연결 시간 증가
```json
{
  "staggeredStartup": {
    "connectionTimeout": 30000
  }
}
```

## 추가 참고자료

- [MCP 공식 문서](https://modelcontextprotocol.io/)
- [Claude Code MCP 통합 가이드](https://github.com/anthropics/claude-code)
- [MoAI MCP 규칙](../.claude/rules/moai/core/mcp-integration.md)

---

버전: 1.0.0
최종 업데이트: 2026-02-09
유지 관리: MoAI 팀
