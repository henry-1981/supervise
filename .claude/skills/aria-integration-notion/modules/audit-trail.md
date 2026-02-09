# Audit Trail System

모든 Notion 데이터 변경을 추적하는 감사 추적 시스템입니다.

## 개요

ARIA VALID 프레임워크의 **Inspectable** 차원을 구현합니다. 모든 데이터 변경은 자동으로 Audit Log 데이터베이스에 기록되어, 규제 준수 요구사항(21 CFR Part 11, EU MDR Annex XV)을 충족합니다.

## 감사 로그 데이터베이스 스키마

| 속성명 | 타입 | 설명 | 필수 여부 |
|--------|------|------|----------|
| Audit ID | Title | 고유 감사 ID (AUDIT-2026-001) | ✓ |
| Timestamp | Date | 변경 시간 (ISO 8601) | ✓ |
| User | Text | 변경자 이메일 또는 ID | ✓ |
| Action | Select | CREATE, UPDATE, ARCHIVE, RELATION_ADD, RELATION_REMOVE | ✓ |
| Entity | Text | 영향 받은 데이터베이스/페이지 | ✓ |
| Changes | Text | 변경 전후 값 비교 (JSON) | ✓ |
| Reason | Text | 변경 사유 | |
| IP Address | Text | 변경자 IP (선택 사항) | |
| Session ID | Text | 세션 식별자 (선택 사항) | |
| Related Page | Relation | 관련 페이지 링크 | |

## 자동 감사 기록

### 감사 대상 작업

다음 작업은 자동으로 감사 로그에 기록됩니다:

1. **CREATE**: 페이지 생성
2. **UPDATE**: 속성 수정
3. **ARCHIVE**: 페이지 아카이브 (Soft Delete)
4. **RELATION_ADD**: 관계 추가
5. **RELATION_REMOVE**: 관계 제거

### 감사 로그 구조

```json
{
  "audit_id": "AUDIT-2026-001",
  "timestamp": "2026-02-09T10:30:00Z",
  "user": "user@example.com",
  "action": "UPDATE",
  "entity": "CAPA Tracker / CAPA-2026-001",
  "changes": {
    "Status": {
      "before": "Open",
      "after": "In Progress"
    },
    "Assigned To": {
      "before": null,
      "after": "John Doe"
    }
  },
  "reason": "CAPA assigned to QA team for investigation",
  "ip_address": "192.168.1.100",
  "session_id": "sess_abc123"
}
```

## 감사 로그 생성 함수

### createAuditLog

```javascript
async function createAuditLog(config) {
  const {
    action,
    entity,
    changes,
    reason = "",
    relatedPageId = null
  } = config;

  const auditEntry = {
    parent: {
      database_id: AUDIT_LOG_DATABASE_ID
    },
    properties: {
      "Audit ID": {
        title: [{
          text: {
            content: `AUDIT-${new Date().getFullYear()}-${String(getAuditCounter()).padStart(3, '0')}`
          }
        }]
      },
      "Timestamp": {
        date: {
          start: new Date().toISOString()
        }
      },
      "User": {
        rich_text: [{
          type: "text",
          text: {
            content: getUserEmail() // 현재 사용자 이메일
          }
        }]
      },
      "Action": {
        select: {
          name: action
        }
      },
      "Entity": {
        rich_text: [{
          type: "text",
          text: {
            content: entity
          }
        }]
      },
      "Changes": {
        rich_text: [{
          type: "text",
          text: {
            content: JSON.stringify(changes, null, 2)
          }
        }]
      },
      "Reason": {
        rich_text: [{
          type: "text",
          text: {
            content: reason
          }
        }]
      }
    }
  };

  if (relatedPageId) {
    auditEntry.properties["Related Page"] = {
      relation: [{ id: relatedPageId }]
    };
  }

  return await mcp__notion__create-page(auditEntry);
}
```

### 변경 감지

```javascript
function detectChanges(before, after) {
  const changes = {};

  for (const key in after) {
    if (JSON.stringify(before[key]) !== JSON.stringify(after[key])) {
      changes[key] = {
        before: before[key],
        after: after[key]
      };
    }
  }

  return changes;
}
```

## CRUD 작업과 감사 통합

### Create와 감사

```javascript
async function createPageWithAudit(databaseId, properties, reason) {
  // 1. 페이지 생성
  const page = await mcp__notion__create-page({
    parent: { database_id: databaseId },
    properties
  });

  // 2. 감사 로그 기록
  await createAuditLog({
    action: "CREATE",
    entity: `${getDatabaseName(databaseId)} / ${extractPageId(page)}`,
    changes: {
      "Created": {
        before: null,
        after: properties
      }
    },
    reason,
    relatedPageId: page.id
  });

  return page;
}
```

### Update와 감사

```javascript
async function updatePageWithAudit(pageId, updates, reason) {
  // 1. 현재 상태 조회
  const currentPage = await mcp__notion__retrieve-page({
    page_id: pageId
  });

  // 2. 변경 감지
  const changes = detectChanges(currentPage.properties, updates);

  if (Object.keys(changes).length === 0) {
    console.log("No changes detected");
    return currentPage;
  }

  // 3. 페이지 수정
  const updatedPage = await mcp__notion__update-page({
    page_id: pageId,
    properties: updates
  });

  // 4. 감사 로그 기록
  await createAuditLog({
    action: "UPDATE",
    entity: `${getDatabaseName(updatedPage.parent.database_id)} / ${extractPageTitle(currentPage)}`,
    changes,
    reason,
    relatedPageId: pageId
  });

  return updatedPage;
}
```

### Archive와 감사

```javascript
async function archivePageWithAudit(pageId, reason) {
  // 1. 현재 상태 조회
  const currentPage = await mcp__notion__retrieve-page({
    page_id: pageId
  });

  // 2. 페이지 아카이브
  await mcp__notion__archive-page({
    page_id: pageId,
    archive: true
  });

  // 3. 감사 로그 기록
  await createAuditLog({
    action: "ARCHIVE",
    entity: `${getDatabaseName(currentPage.parent.database_id)} / ${extractPageTitle(currentPage)}`,
    changes: {
      "Archived": {
        before: "Active",
        after: "Archived"
      }
    },
    reason,
    relatedPageId: pageId
  });
}
```

## 감사 로그 조회

### 최근 변경 내역

```javascript
async function getRecentAuditLogs(limit = 50) {
  const logs = await mcp__notion__query-database({
    database_id: AUDIT_LOG_DATABASE_ID,
    sorts: [
      {
        property: "Timestamp",
        direction: "descending"
      }
    ]
  });

  return logs.results.slice(0, limit);
}
```

### 특정 사용자 변경 내역

```javascript
async function getUserAuditHistory(userEmail) {
  const logs = await mcp__notion__query-database({
    database_id: AUDIT_LOG_DATABASE_ID,
    filter: {
      property: "User",
      rich_text: {
        contains: userEmail
      }
    },
    sorts: [
      {
        property: "Timestamp",
        direction: "descending"
      }
    ]
  });

  return logs.results;
}
```

### 특정 페이지 변경 내역

```javascript
async function getPageAuditHistory(pageId) {
  const logs = await mcp__notion__query-database({
    database_id: AUDIT_LOG_DATABASE_ID,
    filter: {
      property: "Related Page",
      relation: {
        contains: pageId
      }
    },
    sorts: [
      {
        property: "Timestamp",
        direction: "descending"
      }
    ]
  });

  return logs.results;
}
```

### 특정 기간 변경 내역

```javascript
async function getAuditLogsByDateRange(startDate, endDate) {
  const logs = await mcp__notion__query-database({
    database_id: AUDIT_LOG_DATABASE_ID,
    filter: {
      property: "Timestamp",
      date: {
        on_or_after: startDate,
        on_or_before: endDate
      }
    },
    sorts: [
      {
        property: "Timestamp",
        direction: "descending"
      }
    ]
  });

  return logs.results;
}
```

## 규제 준수 매핑

### 21 CFR Part 11 준수

| 요구사항 | 구현 |
|---------|------|
| 11.10(a) - Audit Trail | ✓ 모든 변경 기록 |
| 11.10(b) - Secure Records | ✓ Notion 암호화 |
| 11.10(c) - Timestamp | ✓ ISO 8601 형식 |
| 11.10(d) - Operator ID | ✓ 사용자 이메일 |
| 11.10(e) - Reason | ✓ 변경 사유 |

### EU MDR Annex XV 준수

| 요구사항 | 구현 |
|---------|------|
| Traceability | ✓ Relation 속성으로 연결 |
| Change Control | ✓ 감사 로그 기록 |
| Decision History | ✓ 이유 필드 |
| Date Records | ✓ 타임스탬프 |

## 감사 로그 보고서

### 일일 변경 요약

```javascript
async function generateDailyAuditSummary(date = new Date()) {
  const startOfDay = new Date(date.setHours(0, 0, 0, 0));
  const endOfDay = new Date(date.setHours(23, 59, 59, 999));

  const logs = await getAuditLogsByDateRange(
    startOfDay.toISOString(),
    endOfDay.toISOString()
  );

  const summary = {
    date: date.toISOString().split('T')[0],
    total_changes: logs.length,
    by_action: {},
    by_user: {},
    by_database: {}
  };

  for (const log of logs) {
    const action = log.properties.Action.select.name;
    const user = log.properties.User.rich_text[0].text.content;
    const entity = log.properties.Entity.rich_text[0].text.content;

    summary.by_action[action] = (summary.by_action[action] || 0) + 1;
    summary.by_user[user] = (summary.by_user[user] || 0) + 1;

    const database = entity.split('/')[0];
    summary.by_database[database] = (summary.by_database[database] || 0) + 1;
  }

  return summary;
}
```

### CAPA 추적 보고서

```javascript
async function generateCAPAAuditReport(capaId) {
  // CAPA 페이지 찾기
  const capaPage = await findCAPAById(capaId);

  // CAPA 관련 모든 감사 로그
  const auditLogs = await getPageAuditHistory(capaPage.id);

  const report = {
    capa_id: capaId,
    created_date: capaPage.properties["Opened Date"].date.start,
    current_status: capaPage.properties.Status.status.name,
    audit_trail: auditLogs.map(log => ({
      timestamp: log.properties.Timestamp.date.start,
      user: log.properties.User.rich_text[0].text.content,
      action: log.properties.Action.select.name,
      changes: JSON.parse(log.properties.Changes.rich_text[0].text.content),
      reason: log.properties.Reason.rich_text[0].text.content
    }))
  };

  return report;
}
```

## /aria audit 명령어

### 사용법

```bash
# 최근 변경 내역 조회
/aria audit --limit 50

# 특정 사용자 변경 내역
/aria audit --user "user@example.com"

# 특정 기간 변경 내역
/aria audit --since "2026-02-01" --until "2026-02-09"

# 특정 페이지 변경 내역
/aria audit --page "CAPA-2026-001"

# 일일 요약 보고서
/aria audit --summary --date "2026-02-09"
```

### 구현

```typescript
async function handleAuditCommand(options) {
  if (options.page) {
    // 특정 페이지 감사 로그
    const page = await findPageById(options.page);
    const logs = await getPageAuditHistory(page.id);
    return formatAuditLogs(logs);
  }

  if (options.user) {
    // 사용자별 감사 로그
    const logs = await getUserAuditHistory(options.user);
    return formatAuditLogs(logs);
  }

  if (options.since && options.until) {
    // 기간별 감사 로그
    const logs = await getAuditLogsByDateRange(options.since, options.until);
    return formatAuditLogs(logs);
  }

  if (options.summary) {
    // 일일 요약
    const summary = await generateDailyAuditSummary(new Date(options.date));
    return formatAuditSummary(summary);
  }

  // 기본: 최근 변경 내역
  const logs = await getRecentAuditLogs(options.limit || 50);
  return formatAuditLogs(logs);
}
```

## 감사 로그 무결성

### 무결성 검사

```javascript
async function verifyAuditLogIntegrity() {
  const logs = await getRecentAuditLogs(1000);
  const issues = [];

  for (const log of logs) {
    // 1. 타임스탬프 검증
    const timestamp = new Date(log.properties.Timestamp.date.start);
    if (timestamp > new Date()) {
      issues.push({
        audit_id: extractAuditId(log),
        issue: "Future timestamp detected",
        timestamp: timestamp.toISOString()
      });
    }

    // 2. 관련 페이지 검증
    const relatedPageId = log.properties["Related Page"]?.relation[0]?.id;
    if (relatedPageId) {
      try {
        await mcp__notion__retrieve-page({ page_id: relatedPageId });
      } catch (error) {
        issues.push({
          audit_id: extractAuditId(log),
          issue: "Related page not found",
          page_id: relatedPageId
        });
      }
    }

    // 3. 사용자 이메일 검증
    const userEmail = log.properties.User.rich_text[0].text.content;
    if (!isValidEmail(userEmail)) {
      issues.push({
        audit_id: extractAuditId(log),
        issue: "Invalid user email",
        email: userEmail
      });
    }
  }

  return {
    total_logs: logs.length,
    issues_found: issues.length,
    issues
  };
}
```

### 감사 로그 내보내기

```javascript
async function exportAuditLogs(format = "json") {
  const logs = await getRecentAuditLogs(1000);

  if (format === "json") {
    return JSON.stringify(logs, null, 2);
  }

  if (format === "csv") {
    const headers = ["Audit ID", "Timestamp", "User", "Action", "Entity", "Changes", "Reason"];
    const rows = logs.map(log => [
      extractAuditId(log),
      log.properties.Timestamp.date.start,
      log.properties.User.rich_text[0].text.content,
      log.properties.Action.select.name,
      log.properties.Entity.rich_text[0].text.content,
      JSON.stringify(log.properties.Changes.rich_text[0].text.content),
      log.properties.Reason.rich_text[0].text.content
    ]);

    return [headers, ...rows]
      .map(row => row.map(cell => `"${cell}"`).join(","))
      .join("\n");
  }

  throw new Error(`Unsupported format: ${format}`);
}
```

## 보안 고려사항

### 감사 로그 보호

1. **읽기 전용 접근**: 감사 로그는 읽기 전용으로 유지
2. **암호화**: Notion의 기본 암호화 활용
3. **접근 제어**: Notion 권한으로 제한
4. **정기 백업**: 주기적으로 내보내기

### 개인정보 보호

```javascript
// 민감한 정보 마스킹
function maskSensitiveInfo(data) {
  const masked = { ...data };

  if (masked.ip_address) {
    masked.ip_address = masked.ip_address.replace(/\.\d+$/, ".***");
  }

  if (masked.user) {
    const [name, domain] = masked.user.split("@");
    masked.user = `${name[0]}***@${domain}`;
  }

  return masked;
}
```

## 문제 해결

### 감사 로그 누락

**문제**: CRUD 작업 후 감사 로그가 기록되지 않음

**해결**:
1. MCP 도구가 올바르게 로드되었는지 확인
2. 감사 로그 데이터베이스 ID가 올바른지 확인
3. 네트워크 연결 상태 확인
4. 감사 로그 생성 함수의 예외 처리 확인

### 변경 감지 실패

**문제**: 변경이 감지되지 않음

**해결**:
1. `detectChanges` 함수가 올바르게 작동하는지 확인
2. 속성 값 비교 로직 검증
3. 중첩된 객체 처리 확인

## 다음 단계

감사 추적 학습 후:
- [MCP 도구 레퍼런스](mcp-tools.md)로 모든 도구 확인
- [CRUD 작업](crud-operations.md)으로 데이터 조작 방법 복습
- [데이터베이스 생성 가이드](database-creation.md)로 스키마 이해
