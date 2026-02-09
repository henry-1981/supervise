# CRUD Operations Reference

Notion MCP를 사용한 6개 데이터베이스의 CRUD 작업 레퍼런스입니다.

## 개요

이 가이드는 Notion MCP 도구를 사용하여 데이터를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)하는 방법을 설명합니다. 모든 작업은 자동으로 감사 로그에 기록됩니다.

## 사전 요구사항

1. **MCP 도구 로드**
   ```javascript
   ToolSearch("notion mcp")
   ```

2. **데이터베이스 ID**
   - `.moai/config/sections/knowledge.yaml`에 데이터베이스 ID가 구성되어 있어야 함

3. **감사 추적 활성화**
   - 모든 CRUD 작업은 자동으로 Audit Log 데이터베이스에 기록됨

## Create (생성)

### Regulatory Requirements 생성

```javascript
const page = await mcp__notion__create-page({
  parent: {
    database_id: REGULATORY_REQUIREMENTS_DATABASE_ID
  },
  properties: {
    "Requirement ID": {
      title: [
        {
          text: {
            content: "REQ-2026-001"
          }
        }
      ]
    },
    "Category": {
      select: {
        name: "FDA"
      }
    },
    "Subcategory": {
      select: {
        name: "21 CFR 820"
      }
    },
    "Description": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "Design validation procedures shall be documented..."
          }
        }
      ]
    },
    "Status": {
      status: {
        name: "Draft"
      }
    },
    "Priority": {
      select: {
        name: "High"
      }
    },
    "Due Date": {
      date: {
        start: "2026-03-31"
      }
    },
    "Owner": {
      people: [
        {
          id: "USER_ID_HERE"
        }
      ]
    },
    "Evidence Link": {
      url: "https://notion.so/page-id"
    },
    "Created Date": {
      date: {
        start: new Date().toISOString()
      }
    },
    "Last Modified": {
      date: {
        start: new Date().toISOString()
      }
    }
  }
});

// 감사 로그 자동 기록됨
```

### CAPA 생성

```javascript
const capa = await mcp__notion__create-page({
  parent: {
    database_id: CAPA_TRACKER_DATABASE_ID
  },
  properties: {
    "CAPA ID": {
      title: [
        {
          text: {
            content: `CAPA-${new Date().getFullYear()}-${String(counter).padStart(3, '0')}`
          }
        }
      ]
    },
    "Source": {
      select: {
        name: "Internal Audit"
      }
    },
    "Problem Statement": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "Design validation not performed for software module..."
          }
        }
      ]
    },
    "Root Cause": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "1. No validation procedure defined\n2. Team not trained on validation requirements\n3. No validation template available"
          }
        }
      ]
    },
    "Correction Action": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "1. Create validation procedure SOP-001\n2. Conduct training for all engineers\n3. Develop validation template"
          }
        }
      ]
    },
    "Prevention Action": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "1. Implement design control checklist\n2. Add validation milestone to project templates\n3. Quarterly audit of validation records"
          }
        }
      ]
    },
    "Severity": {
      select: {
        name: "Major"
      }
    },
    "Status": {
      status: {
        name: "Open"
      }
    },
    "Opened Date": {
      date: {
        start: new Date().toISOString()
      }
    },
    "Target Date": {
      date: {
        start: getTargetDate(30) // 30일 후
      }
    },
    "Assigned To": {
      people: [
        {
          id: "USER_ID_HERE"
        }
      ]
    }
  }
});
```

### Risk Register 생성

```javascript
const risk = await mcp__notion__create-page({
  parent: {
    database_id: RISK_REGISTER_DATABASE_ID
  },
  properties: {
    "Risk ID": {
      title: [
        {
          text: {
            content: "RISK-001"
          }
        }
      ]
    },
    "Risk Description": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "Software failure could result in incorrect patient diagnosis"
          }
        }
      ]
    },
    "Risk Category": {
      select: {
        name: "Clinical"
      }
    },
    "Hazard": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "Software algorithm error"
          }
        }
      ]
    },
    "Harm": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "Incorrect diagnosis leading to delayed treatment"
          }
        }
      ]
    },
    "Severity": {
      select: {
        name: "High (3)"
      }
    },
    "Probability": {
      select: {
        name: "Medium (2)"
      }
    },
    "RPN Number": {
      number: 6 // 3 × 2 = 6
    },
    "Mitigation Strategy": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "1. Algorithm validation with clinical data\n2. Independent code review\n3. Clinical evaluation with diverse population"
          }
        }
      ]
    },
    "Residual Severity": {
      select: {
        name: "Low (1)"
      }
    },
    "Residual Probability": {
      select: {
        name: "Low (1)"
      }
    },
    "Residual RPN": {
      number: 1 // 1 × 1 = 1
    },
    "Acceptability": {
      select: {
        name: "Acceptable"
      }
    },
    "Status": {
      status: {
        name: "Open"
      }
    },
    "Created Date": {
      date: {
        start: new Date().toISOString()
      }
    },
    "Review Date": {
      date: {
        start: getReviewDate(90) // 90일 후
      }
    }
  }
});
```

## Read (조회)

### 단일 페이지 조회

```javascript
const page = await mcp__notion__retrieve-page({
  page_id: "PAGE_ID_HERE"
});

console.log("Page:", page);
```

### 데이터베이스 쿼리

```javascript
// 모든 승인된 요구사항 조회
const approvedRequirements = await mcp__notion__query-database({
  database_id: REGULATORY_REQUIREMENTS_DATABASE_ID,
  filter: {
    property: "Status",
    status: {
      equals: "Approved"
    }
  }
});

// 높은 우선순위의 열린 CAPA 조회
const highPriorityCAPA = await mcp__notion__query-database({
  database_id: CAPA_TRACKER_DATABASE_ID,
  filter: {
    and: [
      {
        property: "Status",
        status: {
          equals: "Open"
        }
      },
      {
        property: "Severity",
        select: {
          equals: "Critical"
        }
      }
    ]
  }
});

// 특정 기간 내 생성된 위험 조회
const recentRisks = await mcp__notion__query-database({
  database_id: RISK_REGISTER_DATABASE_ID,
  filter: {
    property: "Created Date",
    date: {
      on_or_after: "2026-02-01"
    }
  }
});

// FDA 관련 지식 기반 검색
const fdaKnowledge = await mcp__notion__query-database({
  database_id: KNOWLEDGE_BASE_DATABASE_ID,
  filter: {
    property: "Tags",
    multi_select: {
      contains: "FDA"
    }
  }
});
```

### 복잡한 쿼리

```javascript
// 마감일 임박 높은 우선순위 요구사항
const urgentRequirements = await mcp__notion__query-database({
  database_id: REGULATORY_REQUIREMENTS_DATABASE_ID,
  filter: {
    and: [
      {
        property: "Status",
        status: {
          equals: "Approved"
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
  },
  sorts: [
    {
      property: "Due Date",
      direction: "ascending"
    }
  ]
});

// 특정 담당자의 진행 중 CAPA
const myCAPAs = await mcp__notion__query-database({
  database_id: CAPA_TRACKER_DATABASE_ID,
  filter: {
    and: [
      {
        property: "Assigned To",
        people: {
          contains: "USER_ID_HERE"
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
});

// RPN 6 이상 위험 (높은 위험)
const highRisks = await mcp__notion__query-database({
  database_id: RISK_REGISTER_DATABASE_ID,
  filter: {
    property: "RPN Number",
    number: {
      greater_than_or_equal_to: 6
    }
  },
  sorts: [
    {
      property: "RPN Number",
      direction: "descending"
    }
  ]
});
```

## Update (수정)

### 상태 업데이트

```javascript
// CAPA 상태 변경
await mcp__notion__update-page({
  page_id: "CAPA_PAGE_ID",
  properties: {
    "Status": {
      status: {
        name: "In Progress"
      }
    },
    "Last Modified": {
      date: {
        start: new Date().toISOString()
      }
    }
  }
});

// 감사 로그 자동 기록:
// - Action: UPDATE
// - Entity: CAPA Tracker / CAPA-2026-001
// - Changes: Status: "Open" → "In Progress"
// - Timestamp: 2026-02-09T10:30:00Z
// - User: user@example.com
```

### 완료 날짜 설정

```javascript
await mcp__notion__update-page({
  page_id: "CAPA_PAGE_ID",
  properties: {
    "Status": {
      status: {
        name: "Closed"
      }
    },
    "Completed Date": {
      date: {
        start: new Date().toISOString()
      }
    },
    "Verification": {
      rich_text: [
        {
          type: "text",
          text: {
            content: "CAPA effectiveness verified through:\n1. 3-month monitoring - no recurrence\n2. Process audit passed\n3. Training completion confirmed"
          }
        }
      ]
    }
  }
});
```

### 관계 설정

```javascript
// CAPA와 위험 연결
await mcp__notion__update-page({
  page_id: "CAPA_PAGE_ID",
  properties: {
    "Related Risk": {
      relation: [
        {
          id: "RISK_PAGE_ID"
        }
      ]
    }
  }
});

// 요구사항과 문서 연결
await mcp__notion__update-page({
  page_id: "REQ_PAGE_ID",
  properties: {
    "Related Documents": {
      relation: [
        {
          id: "DOC_PAGE_ID_1"
        },
        {
          id: "DOC_PAGE_ID_2"
        }
      ]
    }
  }
});
```

### 일괄 수정

```javascript
// 여러 페이지 수정
async function updateStatusBatch(pageIds, newStatus) {
  for (const pageId of pageIds) {
    await mcp__notion__update-page({
      page_id,
      properties: {
        "Status": {
          status: {
            name: newStatus
          }
        }
      }
    });
  }
}
```

## Delete (삭제)

### 페이지 아카이브 (Soft Delete)

```javascript
await mcp__notion__archive-page({
  page_id: "PAGE_ID_HERE",
  archive: true
});

// 감사 로그 자동 기록:
// - Action: ARCHIVE (Soft Delete)
// - Entity: [Database Name] / [Page Title]
// - Changes: Page archived (not permanently deleted)
// - Timestamp: 2026-02-09T10:30:00Z
// - User: user@example.com
```

### 영구 삭제 (Hard Delete)

Notion API는 영구 삭제를 지원하지 않습니다. 아카이브만 가능합니다.

## 트랜잭션 처리

### 여러 관련 페이지 생성

```javascript
async function createCAPAWithRelatedItems(capaData, riskIds, docIds) {
  // 1. CAPA 생성
  const capa = await mcp__notion__create-page({
    parent: { database_id: CAPA_TRACKER_DATABASE_ID },
    properties: capaData
  });

  // 2. 관계 설정
  await mcp__notion__update-page({
    page_id: capa.id,
    properties: {
      "Related Risk": {
        relation: riskIds.map(id => ({ id }))
      },
      "Related Documents": {
        relation: docIds.map(id => ({ id }))
      }
    }
  });

  return capa;
}
```

### 원자적 업데이트

```javascript
// 실패 시 롤백을 위한 원자적 업데이트
async function atomicUpdate(pageId, updates) {
  try {
    const result = await mcp__notion__update-page({
      page_id: pageId,
      properties: updates
    });
    return { success: true, result };
  } catch (error) {
    // 롤백 로직 필요 시 이전 상태 복원
    return { success: false, error };
  }
}
```

## 오류 처리

### 일반적인 오류

```javascript
try {
  const page = await mcp__notion__create-page({
    parent: { database_id: DATABASE_ID },
    properties: { /* ... */ }
  });
} catch (error) {
  if (error.code === "object_not_found") {
    console.error("Database not found:", DATABASE_ID);
  } else if (error.code === "validation_error") {
    console.error("Invalid properties:", error.message);
  } else if (error.code === "unauthorized") {
    console.error("Invalid API token");
  } else {
    console.error("Unknown error:", error);
  }
}
```

### 속성 유효성 검사

```javascript
function validateProperties(properties, schema) {
  for (const [key, value] of Object.entries(properties)) {
    const schemaType = schema[key];

    if (!schemaType) {
      throw new Error(`Unknown property: ${key}`);
    }

    if (schemaType.required && !value) {
      throw new Error(`Required property missing: ${key}`);
    }

    // Select 옵션 유효성 검사
    if (schemaType.type === "select" && value) {
      const validOptions = schemaType.options.map(o => o.name);
      if (!validOptions.includes(value.select.name)) {
        throw new Error(`Invalid select option for ${key}`);
      }
    }
  }
}
```

## 성능 최적화

### 일괄 처리

```javascript
// 한 번에 여러 페이지 생성
async function batchCreate(items) {
  const results = await Promise.allSettled(
    items.map(item =>
      mcp__notion__create-page({
        parent: { database_id: item.databaseId },
        properties: item.properties
      })
    )
  );

  const successful = results.filter(r => r.status === "fulfilled");
  const failed = results.filter(r => r.status === "rejected");

  console.log(`Created: ${successful.length}, Failed: ${failed.length}`);

  return { successful, failed };
}
```

### 페이지네이션

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

## 다음 단계

CRUD 작업 학습 후:
- [감사 추적 시스템](audit-trail.md)으로 변경 추적 방법 학습
- [MCP 도구 레퍼런스](mcp-tools.md)로 모든 도구 확인
- [데이터베이스 생성 가이드](database-creation.md)로 스키마 이해
