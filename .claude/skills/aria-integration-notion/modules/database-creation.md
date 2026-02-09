# Database Creation Guide

Phase 3 스키마를 기반으로 6개 Notion 데이터베이스를 자동 생성하는 방법입니다.

## 개요

ARIA Phase 3은 6개 데이터베이스 스키마를 정의합니다. 이 가이드는 각 데이터베이스를 Notion MCP를 통해 자동 생성하는 방법을 설명합니다.

## 사전 요구사항

1. **Notion Integration Token**
   - [Notion My Integrations](https://www.notion.so/my-integrations)에서 생성
   - 워크스페이스에 대한 액세스 권한 필요

2. **Parent Page ID**
   - 데이터베이스를 생성할 상위 페이지 ID
   - Notion 페이지 URL에서 추출 가능

3. **MCP 서버 설정**
   - `.mcp.json`에 Notion MCP 서버가 구성되어 있어야 함

## 데이터베이스 스키마

### 1. Regulatory Requirements (규제 요구사항)

**목적**: 규제 요구사항 추적 및 준수 관리

**속성 정의**:

| 속성명 | 타입 | 옵션/설명 | 필수 여부 |
|--------|------|-----------|----------|
| Requirement ID | Title | 자동 생성 (REQ-001) | ✓ |
| Category | Select | FDA, ISO 13485, EU MDR, MFDS | ✓ |
| Subcategory | Select | 21 CFR 820, Part 11, MDR Article... | |
| Description | Text | 요구사항 상세 설명 | ✓ |
| Status | Status | Draft, Review, Approved, Implemented | ✓ |
| Priority | Select | High, Medium, Low | ✓ |
| Due Date | Date | 준수 마감일 | |
| Owner | People | 담당자 | |
| Evidence Link | URL | 증거 문서 링크 | |
| Related Documents | Relation | Document Registry와 연결 | |
| Created Date | Date | 자동 생성 | ✓ |
| Last Modified | Date | 자동 업데이트 | ✓ |

**데이터베이스 생성 코드**:

```javascript
await mcp__notion__create-database({
  parent: { page_id: PARENT_PAGE_ID },
  title: "Regulatory Requirements",
  properties: {
    "Requirement ID": { title: {} },
    "Category": {
      select: {
        options: [
          { name: "FDA", color: "blue" },
          { name: "ISO 13485", color: "green" },
          { name: "EU MDR", color: "purple" },
          { name: "MFDS", color: "orange" }
        ]
      }
    },
    "Description": { rich_text: {} },
    "Status": {
      status: {
        options: [
          { name: "Draft", color: "gray" },
          { name: "Review", color: "yellow" },
          { name: "Approved", color: "green" },
          { name: "Implemented", color: "blue" }
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
    },
    "Due Date": { date: {} },
    "Owner": { people: {} },
    "Evidence Link": { url: {} },
    "Related Documents": { relation: {} },
    "Created Date": { date: {} },
    "Last Modified": { date: {} }
  }
});
```

### 2. Document Registry (문서 등록부)

**목적**: 품질 시스템 문서 관리 및 버전 추적

**속성 정의**:

| 속성명 | 타입 | 옵션/설명 | 필수 여부 |
|--------|------|-----------|----------|
| Document ID | Title | 자동 생성 (DOC-001) | ✓ |
| Document Type | Select | SOP, WI, FORM, RECORD, TEMPLATE | ✓ |
| Version | Number | 문서 버전 (1.0, 1.1...) | ✓ |
| Title | Text | 문서 제목 | ✓ |
| Status | Status | Draft, Under Review, Approved, Obsolete | ✓ |
| Effective Date | Date | 발효일 | |
| Review Date | Date | 검토 예정일 | |
| Approved By | People | 승인자 | |
| File Attachment | Files | 문서 파일 | |
| Related Requirements | Relation | Regulatory Requirements와 연결 | |
| Created Date | Date | 자동 생성 | ✓ |
| Last Modified | Date | 자동 업데이트 | ✓ |

**데이터베이스 생성 코드**:

```javascript
await mcp__notion__create-database({
  parent: { page_id: PARENT_PAGE_ID },
  title: "Document Registry",
  properties: {
    "Document ID": { title: {} },
    "Document Type": {
      select: {
        options: [
          { name: "SOP", color: "blue" },
          { name: "WI", color: "green" },
          { name: "FORM", color: "yellow" },
          { name: "RECORD", color: "gray" },
          { name: "TEMPLATE", color: "purple" }
        ]
      }
    },
    "Version": { number: { format: "number" } },
    "Title": { rich_text: {} },
    "Status": {
      status: {
        options: [
          { name: "Draft", color: "gray" },
          { name: "Under Review", color: "yellow" },
          { name: "Approved", color: "green" },
          { name: "Obsolete", color: "red" }
        ]
      }
    },
    "Effective Date": { date: {} },
    "Review Date": { date: {} },
    "Approved By": { people: {} },
    "File Attachment": { files: {} },
    "Related Requirements": { relation: {} },
    "Created Date": { date: {} },
    "Last Modified": { date: {} }
  }
});
```

### 3. CAPA Tracker (시정예방조치)

**목적**: 비적합 및 시정예방조치 관리

**속성 정의**:

| 속성명 | 타입 | 옵션/설명 | 필수 여부 |
|--------|------|-----------|----------|
| CAPA ID | Title | 자동 생성 (CAPA-2026-001) | ✓ |
| Source | Select | Internal Audit, Customer Complaint, Nonconformance... | ✓ |
| Problem Statement | Text | 문제 설명 | ✓ |
| Root Cause | Text | 근본 원인 분석 (5 Why, Fishbone) | |
| Correction Action | Text | 시정 조치 (즉시 조치) | |
| Prevention Action | Text | 예방 조치 (재발 방지) | |
| Severity | Select | Critical, Major, Minor | ✓ |
| Status | Status | Open, In Progress, Closed, Verified | ✓ |
| Opened Date | Date | 개설일 | ✓ |
| Target Date | Date | 목표 완료일 | ✓ |
| Completed Date | Date | 실제 완료일 | |
| Assigned To | People | 담당자 | |
| Related Risk | Relation | Risk Register와 연결 | |
| Related Documents | Relation | Document Registry와 연결 | |
| Verification | Text | 효과 검증 결과 | |
| Created Date | Date | 자동 생성 | ✓ |

**데이터베이스 생성 코드**:

```javascript
await mcp__notion__create-database({
  parent: { page_id: PARENT_PAGE_ID },
  title: "CAPA Tracker",
  properties: {
    "CAPA ID": { title: {} },
    "Source": {
      select: {
        options: [
          { name: "Internal Audit", color: "blue" },
          { name: "Customer Complaint", color: "red" },
          { name: "Nonconformance", color: "orange" },
          { name: "FDA Observation", color: "purple" },
          { name: "Supplier Issue", color: "green" }
        ]
      }
    },
    "Problem Statement": { rich_text: {} },
    "Root Cause": { rich_text: {} },
    "Correction Action": { rich_text: {} },
    "Prevention Action": { rich_text: {} },
    "Severity": {
      select: {
        options: [
          { name: "Critical", color: "red" },
          { name: "Major", color: "orange" },
          { name: "Minor", color: "yellow" }
        ]
      }
    },
    "Status": {
      status: {
        options: [
          { name: "Open", color: "red" },
          { name: "In Progress", color: "yellow" },
          { name: "Closed", color: "green" },
          { name: "Verified", color: "blue" }
        ]
      }
    },
    "Opened Date": { date: {} },
    "Target Date": { date: {} },
    "Completed Date": { date: {} },
    "Assigned To": { people: {} },
    "Related Risk": { relation: {} },
    "Related Documents": { relation: {} },
    "Verification": { rich_text: {} },
    "Created Date": { date: {} }
  }
});
```

### 4. Risk Register (위험 등록부)

**목적**: ISO 14971 위험 관리 및 추적

**속성 정의**:

| 속성명 | 타입 | 옵션/설명 | 필수 여부 |
|--------|------|-----------|----------|
| Risk ID | Title | 자동 생성 (RISK-001) | ✓ |
| Risk Description | Text | 위험 설명 | ✓ |
| Risk Category | Select | Clinical, Technical, Regulatory, Manufacturing | ✓ |
| Hazard | Text | 위해 요소 | |
| Harm | Text | 손상 유형 | |
| Severity | Select | High (3), Medium (2), Low (1) | ✓ |
| Probability | Select | High (3), Medium (2), Low (1) | ✓ |
| RPN Number | Formula | Severity × Probability | ✓ |
| Mitigation Strategy | Text | 완화 전략 | |
| Residual Severity | Select | High (3), Medium (2), Low (1) | |
| Residual Probability | Select | High (3), Medium (2), Low (1) | |
| Residual RPN | Formula | Residual Severity × Residual Probability | |
| Acceptability | Select | Acceptable, Not Acceptable, ALARP | ✓ |
| Status | Status | Open, Mitigating, Closed | ✓ |
| Related CAPA | Relation | CAPA Tracker와 연결 | |
| Created Date | Date | 자동 생성 | ✓ |
| Review Date | Date | 재검토 일정 | |

**데이터베이스 생성 코드**:

```javascript
await mcp__notion__create-database({
  parent: { page_id: PARENT_PAGE_ID },
  title: "Risk Register",
  properties: {
    "Risk ID": { title: {} },
    "Risk Description": { rich_text: {} },
    "Risk Category": {
      select: {
        options: [
          { name: "Clinical", color: "red" },
          { name: "Technical", color: "blue" },
          { name: "Regulatory", color: "purple" },
          { name: "Manufacturing", color: "green" }
        ]
      }
    },
    "Hazard": { rich_text: {} },
    "Harm": { rich_text: {} },
    "Severity": {
      select: {
        options: [
          { name: "High (3)", color: "red" },
          { name: "Medium (2)", color: "yellow" },
          { name: "Low (1)", color: "green" }
        ]
      }
    },
    "Probability": {
      select: {
        options: [
          { name: "High (3)", color: "red" },
          { name: "Medium (2)", color: "yellow" },
          { name: "Low (1)", color: "green" }
        ]
      }
    },
    "RPN Number": { number: { format: "number" } },
    "Mitigation Strategy": { rich_text: {} },
    "Residual Severity": {
      select: {
        options: [
          { name: "High (3)", color: "red" },
          { name: "Medium (2)", color: "yellow" },
          { name: "Low (1)", color: "green" }
        ]
      }
    },
    "Residual Probability": {
      select: {
        options: [
          { name: "High (3)", color: "red" },
          { name: "Medium (2)", color: "yellow" },
          { name: "Low (1)", color: "green" }
        ]
      }
    },
    "Residual RPN": { number: { format: "number" } },
    "Acceptability": {
      select: {
        options: [
          { name: "Acceptable", color: "green" },
          { name: "Not Acceptable", color: "red" },
          { name: "ALARP", color: "yellow" }
        ]
      }
    },
    "Status": {
      status: {
        options: [
          { name: "Open", color: "red" },
          { name: "Mitigating", color: "yellow" },
          { name: "Closed", color: "green" }
        ]
      }
    },
    "Related CAPA": { relation: {} },
    "Created Date": { date: {} },
    "Review Date": { date: {} }
  }
});
```

### 5. Submission Tracker (제출 추적)

**목적**: 시판 전/후 제출물 추적

**속성 정의**:

| 속성명 | 타입 | 옵션/설명 | 필수 여부 |
|--------|------|-----------|----------|
| Submission ID | Title | 자동 생성 (SUB-2026-001) | ✓ |
| Submission Type | Select | 510(k), PMA, De Novo, CE Mark, MFDS | ✓ |
| Target Market | Select | USA, EU, Korea, Japan, China | ✓ |
| Product Name | Text | 제품명 | ✓ |
| Submission Date | Date | 제출일 | |
| Approval Date | Date | 승인일 | |
| Status | Status | Preparing, Submitted, Under Review, Approved, Rejected | ✓ |
| Reviewer | Select | FDA, NB, MFDS, PMDA | |
| Assigned To | People | 담당자 | |
| Related Documents | Relation | Document Registry와 연결 | |
| Feedback | Text | 검토 피드백 | |
| Created Date | Date | 자동 생성 | ✓ |

**데이터베이스 생성 코드**:

```javascript
await mcp__notion__create-database({
  parent: { page_id: PARENT_PAGE_ID },
  title: "Submission Tracker",
  properties: {
    "Submission ID": { title: {} },
    "Submission Type": {
      select: {
        options: [
          { name: "510(k)", color: "blue" },
          { name: "PMA", color: "purple" },
          { name: "De Novo", color: "green" },
          { name: "CE Mark", color: "orange" },
          { name: "MFDS", color: "red" }
        ]
      }
    },
    "Target Market": {
      select: {
        options: [
          { name: "USA", color: "blue" },
          { name: "EU", color: "purple" },
          { name: "Korea", color: "red" },
          { name: "Japan", color: "green" },
          { name: "China", color: "orange" }
        ]
      }
    },
    "Product Name": { rich_text: {} },
    "Submission Date": { date: {} },
    "Approval Date": { date: {} },
    "Status": {
      status: {
        options: [
          { name: "Preparing", color: "gray" },
          { name: "Submitted", color: "yellow" },
          { name: "Under Review", color: "blue" },
          { name: "Approved", color: "green" },
          { name: "Rejected", color: "red" }
        ]
      }
    },
    "Reviewer": {
      select: {
        options: [
          { name: "FDA", color: "blue" },
          { name: "NB", color: "purple" },
          { name: "MFDS", color: "red" },
          { name: "PMDA", color: "green" }
        ]
      }
    },
    "Assigned To": { people: {} },
    "Related Documents": { relation: {} },
    "Feedback": { rich_text: {} },
    "Created Date": { date: {} }
  }
});
```

### 6. Knowledge Base (지식 기반)

**목적**: 규정 지식 자동 업데이트 및 검색

**속성 정의**:

| 속성명 | 타입 | 옵션/설명 | 필수 여부 |
|--------|------|-----------|----------|
| Article ID | Title | 자동 생성 (KB-001) | ✓ |
| Category | Select | Regulation, Guideline, Best Practice, News | ✓ |
| Tags | Multi-select | FDA, ISO, MDR, QSR, IEC 62304... | |
| Title | Text | 문서 제목 | ✓ |
| Content | Text | 문서 내용 | ✓ |
| Source | URL | 출처 URL | |
| Last Updated | Date | 최종 업데이트 | ✓ |
| TTL | Number | 캐시 만료 시간 (초) | ✓ |
| Related Requirements | Relation | Regulatory Requirements와 연결 | |
| Created Date | Date | 자동 생성 | ✓ |

**데이터베이스 생성 코드**:

```javascript
await mcp__notion__create-database({
  parent: { page_id: PARENT_PAGE_ID },
  title: "Knowledge Base",
  properties: {
    "Article ID": { title: {} },
    "Category": {
      select: {
        options: [
          { name: "Regulation", color: "blue" },
          { name: "Guideline", color: "green" },
          { name: "Best Practice", color: "yellow" },
          { name: "News", color: "orange" }
        ]
      }
    },
    "Tags": {
      multi_select: {
        options: [
          { name: "FDA", color: "blue" },
          { name: "ISO", color: "green" },
          { name: "MDR", color: "purple" },
          { name: "QSR", color: "red" },
          { name: "IEC 62304", color: "orange" },
          { name: "21 CFR 820", color: "gray" },
          { name: "ISO 14971", color: "pink" }
        ]
      }
    },
    "Title": { rich_text: {} },
    "Content": { rich_text: {} },
    "Source": { url: {} },
    "Last Updated": { date: {} },
    "TTL": { number: { format: "number" } },
    "Related Requirements": { relation: {} },
    "Created Date": { date: {} }
  }
});
```

## 자동 생성 스크립트

`/aria init notion` 명령어는 다음 순서로 데이터베이스를 생성합니다:

```typescript
async function initializeNotionDatabases(parentPageId: string) {
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
      results.push({ success: true, db });
      console.log(`✓ Created: ${db.title}`);
    } catch (error) {
      results.push({ success: false, error });
      console.error(`✗ Failed: ${error.message}`);
    }
  }

  return results;
}
```

## 데이터베이스 관계 설정

데이터베이스 간 Relation 속성을 설정하여 데이터 일관성을 유지합니다:

| 데이터베이스 | 관계 | 대상 데이터베이스 |
|------------|------|------------------|
| Regulatory Requirements | Related Documents | Document Registry |
| Document Registry | Related Requirements | Regulatory Requirements |
| CAPA Tracker | Related Risk | Risk Register |
| CAPA Tracker | Related Documents | Document Registry |
| Risk Register | Related CAPA | CAPA Tracker |
| Submission Tracker | Related Documents | Document Registry |
| Knowledge Base | Related Requirements | Regulatory Requirements |

## 검증 체크리스트

데이터베이스 생성 후 다음을 확인합니다:

- [ ] 모든 6개 데이터베이스가 생성되었는가?
- [ ] 각 데이터베이스의 필수 속성이 올바른가?
- [ ] Select 옵션의 색상이 일관되게 설정되었는가?
- [ ] Relation 속성이 올바르게 연결되었는가?
- [ ] 데이터베이스 제목이 올바른가?
- [ ] 자동 생성 속성(생성일, ID)이 작동하는가?

## 문제 해결

### 생성 실패

**문제**: 데이터베이스 생성이 실패함

**해결**:
1. Notion Integration Token 유효성 확인
2. Parent Page ID가 올바른지 확인
3. MCP 서버가 실행 중인지 확인

### 속성 오류

**문제**: 속성 타입이 올바르지 않음

**해결**:
1. Notion API 문서에서 속성 타입 확인
2. Select 옵션 이름에 오타가 없는지 확인
3. Relation 속성의 대상 데이터베이스가 먼저 생성되었는지 확인

### 관계 설정 실패

**문제**: Relation 속성이 작동하지 않음

**해결**:
1. 대상 데이터베이스가 이미 생성되었는지 확인
2. 데이터베이스 ID가 올바른지 확인
3. 데이터베이스가 삭제되지 않았는지 확인

## 다음 단계

데이터베이스 생성 후:
- [CRUD 작업](crud-operations.md)로 데이터 조작 방법 학습
- [감사 추적 시스템](audit-trail.md)으로 변경 추적 방법 학습
- [MCP 도구 레퍼런스](mcp-tools.md)로 사용 가능한 도구 확인
