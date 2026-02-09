# MCP Tools Reference

Notion MCP 서버에서 제공하는 도구의 완전한 레퍼런스입니다.

## 개요

이 문서는 Notion MCP(Model Context Protocol) 서버에서 제공하는 모든 도구의 사용법을 설명합니다. 이 도구들을 사용하여 Notion 데이터베이스와 상호작용할 수 있습니다.

## 사전 요구사항

### MCP 서버 로드

```javascript
// Notion MCP 도구 로드
ToolSearch("notion mcp")
```

### 환경 변수 설정

```bash
export NOTION_API_KEY="your_notion_integration_token"
export NOTION_DATABASE_ID="your_parent_database_id"
```

## 사용 가능한 도구

### mcp__notion__create-page

새 페이지를 데이터베이스에 생성합니다.

**매개변수**:

```yaml
parent (required): object
  database_id: string
    데이터베이스 ID

properties (required): object
  데이터베이스 스키마에 정의된 속성들
```

**예시**:

```javascript
const page = await mcp__notion__create-page({
  parent: {
    database_id: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
  },
  properties: {
    "CAPA ID": {
      title: [{
        text: {
          content: "CAPA-2026-001"
        }
      }]
    },
    "Problem Statement": {
      rich_text: [{
        type: "text",
        text: {
          content: "Design validation not performed..."
        }
      }]
    },
    "Status": {
      status: {
        name: "Open"
      }
    },
    "Severity": {
      select: {
        name: "Major"
      }
    }
  }
});
```

### mcp__notion__retrieve-page

단일 페이지를 검색합니다.

**매개변수**:

```yaml
page_id (required): string
  페이지 ID
```

**예시**:

```javascript
const page = await mcp__notion__retrieve-page({
  page_id: "page-id-here"
});

console.log(page.properties);
```

### mcp__notion__update-page

기존 페이지의 속성을 수정합니다.

**매개변수**:

```yaml
page_id (required): string
  페이지 ID

properties (required): object
  수정할 속성들
```

**예시**:

```javascript
const updated = await mcp__notion__update-page({
  page_id: "page-id-here",
  properties: {
    "Status": {
      status: {
        name: "In Progress"
      }
    },
    "Assigned To": {
      people: [{
        id: "user-id-here"
      }]
    }
  }
});
```

### mcp__notion__archive-page

페이지를 아카이브(Soft Delete)합니다.

**매개변수**:

```yaml
page_id (required): string
  페이지 ID

archive (required): boolean
  true로 설정하여 아카이브
```

**예시**:

```javascript
await mcp__notion__archive-page({
  page_id: "page-id-here",
  archive: true
});
```

### mcp__notion__query-database

데이터베이스를 쿼리합니다.

**매개변수**:

```yaml
database_id (required): string
  데이터베이스 ID

filter (optional): object
  필터 조건

sorts (optional): array
  정렬 조건

start_cursor (optional): string
  페이지네이션 커서
```

**예시**:

```javascript
const results = await mcp__notion__query-database({
  database_id: "database-id-here",
  filter: {
    property: "Status",
    status: {
      equals: "Open"
    }
  },
  sorts: [
    {
      property: "Created Date",
      direction: "descending"
    }
  ]
});
```

### mcp__notion__create-database

새 데이터베이스를 생성합니다.

**매개변수**:

```yaml
parent (required): object
  page_id: string
    상위 페이지 ID

title (required): string
  데이터베이스 제목

properties (required): object
  속성 정의들
```

**예시**:

```javascript
const database = await mcp__notion__create-database({
  parent: {
    page_id: "parent-page-id"
  },
  title: "Custom Database",
  properties: {
    "Name": { title: {} },
    "Status": {
      status: {
        options: [
          { name: "Todo", color: "gray" },
          { name: "In Progress", color: "blue" },
          { name: "Done", color: "green" }
        ]
      }
    },
    "Priority": {
      select: {
        options: [
          { name: "High", color: "red" },
          { name: "Medium", color: "yellow" },
          { name: "Low", color: "gray" }
        ]
      }
    }
  }
});
```

### mcp__notion__append-blocks

페이지에 블록을 추가합니다.

**매개변수**:

```yaml
page_id (required): string
  페이지 ID

blocks (required): array
  추가할 블록들
```

**예시**:

```javascript
await mcp__notion__append-blocks({
  page_id: "page-id-here",
  blocks: [
    {
      object: "block",
      type: "heading_1",
      heading_1: {
        rich_text: [{
          type: "text",
          text: {
            content: "CAPA Investigation Report"
          }
        }]
      }
    },
    {
      object: "block",
      type: "paragraph",
      paragraph: {
        rich_text: [{
          type: "text",
          text: {
            content: "Root cause analysis completed..."
          }
        }]
      }
    }
  ]
});
```

## 속성 타입 레퍼런스

### title

제목 속성 (각 페이지마다 하나)

```javascript
{
  "Document ID": {
    title: [{
      text: {
        content: "DOC-001"
      }
    }]
  }
}
```

### rich_text

여러 줄 텍스트

```javascript
{
  "Description": {
    rich_text: [{
      type: "text",
      text: {
        content: "Line 1\nLine 2\nLine 3"
      }
    }]
  }
}
```

### number

숫자 값

```javascript
{
  "Version": {
    number: 1.0
  }
}
```

### select

단일 선택 (Select)

```javascript
{
  "Category": {
    select: {
      name: "FDA"
    }
  }
}
```

### multi_select

다중 선택

```javascript
{
  "Tags": {
    multi_select: [
      { name: "FDA" },
      { name: "QSR" },
      { name: "Design Control" }
    ]
  }
}
```

### status

상태 (Status)

```javascript
{
  "Status": {
    status: {
      name: "In Progress"
    }
  }
}
```

### date

날짜

```javascript
{
  "Due Date": {
    date: {
      start: "2026-03-31"
    }
  }
}
```

날짜와 시간:

```javascript
{
  "Created Date": {
    date: {
      start: "2026-02-09T10:30:00Z"
    }
  }
}
```

날짜 범위:

```javascript
{
  "Review Period": {
    date: {
      start: "2026-03-01",
      end: "2026-03-31"
    }
  }
}
```

### people

사용자 참조

```javascript
{
  "Owner": {
    people: [{
      id: "user-id-here"
    }]
  }
}
```

### files

파일 첨부

```javascript
{
  "Attachment": {
    files: [
      {
        name: "document.pdf",
        external: {
          url: "https://example.com/document.pdf"
        }
      }
    ]
  }
}
```

### url

URL 링크

```javascript
{
  "Source": {
    url: "https://www.fda.gov/regulations"
  }
}
```

### email

이메일 주소

```javascript
{
  "Contact Email": {
    email: "user@example.com"
  }
}
```

### phone

전화번호

```javascript
{
  "Contact Phone": {
    phone: "+1-234-567-8900"
  }
}
```

### relation

관계 (다른 페이지와 연결)

```javascript
{
  "Related Documents": {
    relation: [
      { id: "page-id-1" },
      { id: "page-id-2" }
    ]
  }
}
```

### formula

계산식 (자동 계산)

```javascript
{
  "RPN Number": {
    formula: {
      number: 6 // 계산된 값
    }
  }
}
```

### checkbox

체크박스

```javascript
{
  "Verified": {
    checkbox: true
  }
}
```

## 필터 쿼리 레퍼런스

### 텍스트 필터

```javascript
{
  filter: {
    property: "Title",
    title: {
      contains: "keyword"
    }
  }
}
```

### 숫자 필터

```javascript
// 같음
{
  filter: {
    property: "RPN Number",
    number: {
      equals: 6
    }
  }
}

// 크거나 같음
{
  filter: {
    property: "RPN Number",
    number: {
      greater_than_or_equal_to: 6
    }
  }
}

// 작거나 같음
{
  filter: {
    property: "RPN Number",
    number: {
      less_than_or_equal_to: 6
    }
  }
}
```

### 선택 필터

```javascript
{
  filter: {
    property: "Category",
    select: {
      equals: "FDA"
    }
  }
}
```

### 상태 필터

```javascript
{
  filter: {
    property: "Status",
    status: {
      equals: "In Progress"
    }
  }
}
```

### 날짜 필터

```javascript
// 특정 날짜
{
  filter: {
    property: "Due Date",
    date: {
      equals: "2026-03-31"
    }
  }
}

// 이전 또는 같음
{
  filter: {
    property: "Due Date",
    date: {
      on_or_before: "2026-03-31"
    }
  }
}

// 이후 또는 같음
{
  filter: {
    property: "Created Date",
    date: {
      on_or_after: "2026-02-01"
    }
  }
}

// 기간 내
{
  filter: {
    property: "Review Date",
    date: {
      after: "2026-03-01",
      before: "2026-03-31"
    }
  }
}
```

### 복합 필터 (AND)

```javascript
{
  filter: {
    and: [
      {
        property: "Status",
        status: {
          equals: "Open"
        }
      },
      {
        property: "Priority",
        select: {
          equals: "High"
        }
      },
      {
        property: "Due Date",
        date: {
          on_or_before: "2026-03-31"
        }
      }
    ]
  }
}
```

### 복합 필터 (OR)

```javascript
{
  filter: {
    or: [
      {
        property: "Status",
        status: {
          equals: "Open"
        }
      },
      {
        property: "Status",
        status: {
          equals: "In Progress"
        }
      }
    ]
  }
}
```

## 정렬 레퍼런스

```javascript
{
  sorts: [
    {
      property: "Due Date",
      direction: "ascending"  // or "descending"
    },
    {
      property: "Priority",
      direction: "descending"
    }
  ]
}
```

## 오류 처리

### 일반적인 오류

| 오류 코드 | 설명 | 해결 방법 |
|-----------|------|-----------|
| object_not_found | 데이터베이스/페이지를 찾을 수 없음 | ID 확인 |
| unauthorized | API 토큰이 유효하지 않음 | NOTION_API_KEY 확인 |
| validation_error | 속성 값이 유효하지 않음 | 속성 타입과 옵션 확인 |
| rate_limited | API 속도 제한 초과 | 잠시 후 다시 시도 |

### 예외 처리 패턴

```javascript
async function safeQuery(databaseId, filter) {
  try {
    const results = await mcp__notion__query-database({
      database_id: databaseId,
      filter
    });
    return { success: true, data: results };
  } catch (error) {
    if (error.code === "object_not_found") {
      console.error("Database not found:", databaseId);
    } else if (error.code === "unauthorized") {
      console.error("Invalid API token");
    } else {
      console.error("Unknown error:", error);
    }
    return { success: false, error };
  }
}
```

## 성능 최적화

### 페이지네이션

대용량 데이터를 효율적으로 조회합니다.

```javascript
async function queryAllPages(databaseId) {
  let hasMore = true;
  let startCursor = undefined;
  const allPages = [];

  while (hasMore) {
    const response = await mcp__notion__query-database({
      database_id: databaseId,
      start_cursor: startCursor
    });

    allPages.push(...response.results);
    hasMore = response.has_more;
    startCursor = response.next_cursor;
  }

  return allPages;
}
```

### 일괄 처리

```javascript
// 여러 페이지 생성
const pages = await Promise.all([
  mcp__notion__create-page({ /* ... */ }),
  mcp__notion__create-page({ /* ... */ }),
  mcp__notion__create-page({ /* ... */ })
]);
```

## /aria init 명령어 구현

### 초기화 흐름

```typescript
async function initializeNotion() {
  // 1. MCP 도구 로드
  await ToolSearch("notion mcp");

  // 2. 상위 페이지 확인
  const parentPageId = process.env.NOTION_DATABASE_ID;
  if (!parentPageId) {
    throw new Error("NOTION_DATABASE_ID environment variable not set");
  }

  // 3. 6개 데이터베이스 생성
  const databases = [
    createRegulatoryRequirementsDB,
    createDocumentRegistryDB,
    createCAPATrackerDB,
    createRiskRegisterDB,
    createSubmissionTrackerDB,
    createKnowledgeBaseDB
  ];

  const results = [];

  for (const createDB of databases) {
    try {
      const db = await createDB(parentPageId);
      results.push({ success: true, name: db.title, id: db.id });
      console.log(`✓ Created: ${db.title}`);
    } catch (error) {
      results.push({ success: false, name: createDB.name, error });
      console.error(`✗ Failed: ${createDB.name} - ${error.message}`);
    }
  }

  // 4. 데이터베이스 ID 저장
  await saveDatabaseIds(results);

  // 5. 관계 설정
  await setupDatabaseRelations(results);

  return results;
}
```

## 다음 단계

MCP 도구 학습 후:
- [데이터베이스 생성 가이드](database-creation.md)로 스키마 이해
- [CRUD 작업](crud-operations.md)으로 데이터 조작 방법 학습
- [감사 추적 시스템](audit-trail.md)으로 변경 추적 방법 학습
