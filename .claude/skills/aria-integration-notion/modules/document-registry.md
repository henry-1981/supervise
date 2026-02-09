# Document Registry

품질 시스템 문서 관리를 위한 Notion 연동 모듈입니다. 문서 자동 등록, 버전 히스토리 관리, 검토일 알림 기능을 제공합니다.

## 개요

Document Registry는 ISO 13485 품질 시스템 요구사항에 따라 문서를 관리합니다. SOP (표준 운영 절차), WI (작업 지침), FORM (양식), RECORD (기록), TEMPLATE (템플릿) 문서를 추적합니다.

## 문서 유형

| 문서 유형 | 설명 | 예시 |
|----------|------|------|
| SOP | Standard Operating Procedure (표준 운영 절차) | Design Control Procedure, CAPA Procedure |
| WI | Work Instruction (작업 지침) | Device Testing Instructions, Calibration Steps |
| FORM | Form (양식) | CAPA Report Form, Risk Assessment Form |
| RECORD | Record (기록) | Meeting Minutes, Training Records, Test Results |
| TEMPLATE | Template (템플릿) | SOP Template, Report Template |

## 문서 관리 프로세스

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 문서 작성 (Draft)                                         │
│    - 새 문서 초안 작성                                        │
│    - Document ID 자동 할당                                    │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. 검토 (Under Review)                                       │
│    - 관계자 검토                                              │
│    - 피드백 수집                                              │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. 승인 (Approved)                                          │
│    - 승인자 승인                                              │
│    - Effective Date 설정                                      │
│    - Version 1.0 발행                                         │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. 배포 & 이행 (Implementation)                              │
│    - 교육, 실무 적용                                           │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. 정기 검토 (Periodic Review)                               │
│    - Review Date 도달 시 검토                                  │
│    - 개정 필요 시 수정                                        │
│    - Version 업데이트                                         │
└─────────────────────────────────────────────────────────────┘
```

## Notion 자동 등록

### 문서 생성 시 자동 등록

```typescript
/**
 * 문서 생성 시 Notion DB에 자동 등록
 */
async function createDocumentNotionEntry(documentData: DocumentData) {
    // Document ID 자동 생성
    const documentId = generateDocumentId(documentData.documentType);

    // Notion 페이지 생성
    const documentPage = await mcp__notion__create-page({
        parent: { database_id: DOCUMENT_REGISTRY_DB_ID },
        properties: {
            "Document ID": { title: [{ text: { content: documentId } }] },
            "Document Type": { select: { name: documentData.documentType } },
            "Version": { number: 1.0 },
            "Title": { rich_text: [{ text: { content: documentData.title } }] },
            "Status": { status: { name: "Draft" } },
            "Created Date": { date: { start: new Date().toISOString() } },
            "Last Modified": { date: { start: new Date().toISOString() } }
        }
    });

    // 감사 추적 기록
    await logAuditTrail({
        action: "Create",
        entity: "Document",
        entityId: documentId,
        decision: `문서 생성: ${documentData.title}`,
        rationale: `문서 유형: ${documentData.documentType}`
    });

    return documentPage;
}
```

### Document ID 생성 규칙

```
{문서유형}-{NNN}
예시: SOP-001, WI-015, FORM-042
```

```typescript
/**
 * Document ID 자동 생성
 */
async function generateDocumentId(documentType: string): Promise<string> {
    const query = await mcp__notion__query-database({
        database_id: DOCUMENT_REGISTRY_DB_ID,
        filter: {
            property: "Document Type",
            select: { equals: documentType }
        }
    });

    const nextSequence = query.results.length + 1;
    return `${documentType}-${nextSequence.toString().padStart(3, '0')}`;
}
```

## 버전 히스토리 관리

### 버전 규칙

```
Major.Minor 형식
- Major: 주요 개정 (0 → 1 → 2)
- Minor: 경미 수정 (1.0 → 1.1 → 1.2)
```

### 버전 업데이트 로직

```typescript
/**
 * 문서 수정 시 버전 업데이트
 */
async function updateDocumentVersion(
    documentPageId: string,
    updateType: "major" | "minor",
    changeDescription: string
) {
    // 현재 문서 정보 조회
    const document = await mcp__notion__query-database({
        database_id: DOCUMENT_REGISTRY_DB_ID,
        filter: {
            property: "Document ID",
            title: { equals: documentPageId }
        }
    });

    const currentVersion = document.results[0].properties.Version.number;
    const newVersion = calculateNewVersion(currentVersion, updateType);

    // 버전 업데이트
    await mcp__notion__update-page({
        page_id: documentPageId,
        properties: {
            "Version": { number: newVersion },
            "Last Modified": { date: { start: new Date().toISOString() } }
        }
    });

    // 변경 이력 기록 (Notion 페이지 블록에 추가)
    await appendChangeHistory(documentPageId, {
        version: newVersion,
        changeDate: new Date().toISOString(),
        changeType: updateType,
        description: changeDescription
    });

    // 감사 추적 기록
    await logAuditTrail({
        action: "Update",
        entity: "Document",
        entityId: documentPageId,
        decision: `버전 업데이트: ${currentVersion} → ${newVersion}`,
        rationale: changeDescription
    });

    return newVersion;
}

/**
 * 새 버전 계산
 */
function calculateNewVersion(
    currentVersion: number,
    updateType: "major" | "minor"
): number {
    const [major, minor] = currentVersion.toString().split('.').map(Number);

    if (updateType === "major") {
        return parseFloat(`${major + 1}.0`);
    } else {
        return parseFloat(`${major}.${minor + 1}`);
    }
}

/**
 * 변경 이력 추가
 */
async function appendChangeHistory(
    documentPageId: string,
    changeRecord: ChangeRecord
) {
    await mcp__notion__append-blocks({
        block_id: documentPageId,
        children: [
            {
                object: "block",
                type: "callout",
                callout: {
                    rich_text: [{
                        type: "text",
                        text: {
                            content: `Version ${changeRecord.version} (${changeRecord.changeDate})\n${changeRecord.description}`
                        }
                    }],
                    color: "gray"
                }
            }
        ]
    });
}
```

### 버전 히스토리 조회

```typescript
/**
 * 문서 버전 히스토리 조회
 */
async function getDocumentVersionHistory(documentPageId: string) {
    const document = await mcp__notion__retrieve-page({ page_id: documentPageId });

    // 변경 이력 블록 추출
    const changeHistoryBlocks = document.blocks.filter(block =>
        block.type === "callout"
    );

    return {
        currentVersion: document.properties.Version.number,
        history: changeHistoryBlocks.map(block => ({
            version: block.callout.rich_text[0].text.content.match(/Version (\d+\.\d+)/)[1],
            date: block.callout.rich_text[0].text.content.match(/\(([^)]+)\)/)[1],
            description: block.callout.rich_text[0].text.content.split('\n')[1]
        }))
    };
}
```

## 검토일 알림

### 검토일 설정

```typescript
/**
 * 문서 승인 시 검토일 자동 설정
 */
async function setupDocumentReviewReminder(documentPageId: string) {
    // 문서 승인 시 Effective Date 설정
    const today = new Date();
    const reviewDate = calculateReviewDate(today);

    // Review Date 업데이트
    await mcp__notion__update-page({
        page_id: documentPageId,
        properties: {
            "Status": { status: { name: "Approved" } },
            "Effective Date": { date: { start: today.toISOString() } },
            "Review Date": { date: { start: reviewDate } }
        }
    });

    // Google Calendar 이벤트 생성
    const calendarEvent = await createGoogleCalendarEvent({
        title: `문서 검토 알림: ${documentPageId}`,
        start: reviewDate,
        reminders: [
            { method: "email", minutes: 10080 }, // 1주 전
            { method: "popup", minutes: 0 }
        ],
        description: `문서 정기 검토가 예정되어 있습니다.`
    });

    return calendarEvent;
}
```

### 검토일 계산

```typescript
/**
 * 다음 검토일 계산
 * - SOP: 2년마다
 * - WI: 1년마다
 * - FORM: 3년마다
 * - RECORD: 5년마다 (보존 기간)
 * - TEMPLATE: 2년마다
 */
function calculateReviewDate(effectiveDate: Date, documentType: string): string {
    const reviewDate = new Date(effectiveDate);

    const reviewIntervals = {
        "SOP": 2,
        "WI": 1,
        "FORM": 3,
        "RECORD": 5,
        "TEMPLATE": 2
    };

    const years = reviewIntervals[documentType] || 2;
    reviewDate.setFullYear(reviewDate.getFullYear() + years);

    return reviewDate.toISOString();
}
```

### 검토일 모니터링

```typescript
/**
 * 검토일 임박 문서 모니터링
 */
async function monitorDocumentReviewDates() {
    const today = new Date();
    const warningDays = 30;

    // 30일 이내 검토 예정 문서 조회
    const upcomingReviews = await mcp__notion__query-database({
        database_id: DOCUMENT_REGISTRY_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { equals: "Approved" } },
                {
                    property: "Review Date",
                    date: {
                        on_or_before: new Date(today.getTime() + warningDays * 24 * 60 * 60 * 1000).toISOString()
                    }
                }
            ]
        }
    });

    // 검토 경과 문서 조회
    const overdueReviews = upcomingReviews.results.filter(doc => {
        const reviewDate = new Date(doc.properties.Review Date.date.start);
        return reviewDate < today;
    });

    return {
        upcoming: upcomingReviews.results.filter(d => !overdueReviews.includes(d)),
        overdue: overdueReviews
    };
}
```

## 문서 상태 관리

### 상태 전이

```
Draft → Under Review → Approved → Obsolete
         ↓                ↓
      Rejected        Revised (다시 Draft)
```

### 상태 변경 로직

```typescript
/**
 * 문서 상태 변경
 */
async function updateDocumentStatus(
    documentPageId: string,
    newStatus: "Draft" | "Under Review" | "Approved" | "Obsolete",
    reason: string
) {
    // 상태 변경
    await mcp__notion__update-page({
        page_id: documentPageId,
        properties: {
            "Status": { status: { name: newStatus } },
            "Last Modified": { date: { start: new Date().toISOString() } }
        }
    });

    // 승인 시 Effective Date 및 Review Date 설정
    if (newStatus === "Approved") {
        await setupDocumentReviewReminder(documentPageId);
    }

    // 감사 추적 기록
    await logAuditTrail({
        action: "Update",
        entity: "Document",
        entityId: documentPageId,
        decision: `상태 변경: ${newStatus}`,
        rationale: reason
    });
}
```

## 사용 예시

### 예시 1: 새 SOP 문서 생성

```typescript
const document = await createDocumentNotionEntry({
    documentType: "SOP",
    title: "Design Control Procedure",
    content: "This procedure defines the design control process...",
    author: "John Doe",
    reviewer: "Jane Smith",
    approver: "Quality Manager"
});

// Document ID: SOP-001 자동 생성
```

### 예시 2: 문서 검토 및 승인

```typescript
// 검토 상태로 변경
await updateDocumentStatus("SOP-001", "Under Review", "검토 요청");

// 승인 (Effective Date 및 Review Date 자동 설정)
await updateDocumentStatus("SOP-001", "Approved", "승인 완료");
// Effective Date: 오늘, Review Date: 2년 후
```

### 예시 3: 문서 수정 및 버전 업데이트

```typescript
// 주요 개정 (1.0 → 2.0)
await updateDocumentVersion("SOP-001", "major", "ISO 13485:2016 요구사항 반영");

// 경미 수정 (2.0 → 2.1)
await updateDocumentVersion("SOP-001", "minor", "오타 수정");
```

### 예시 4: 검토일 모니터링

```typescript
const reviewStatus = await monitorDocumentReviewDates();

console.log(`검토 예정 문서: ${reviewStatus.upcoming.length}개`);
console.log(`검토 경과 문서: ${reviewStatus.overdue.length}개`);

reviewStatus.overdue.forEach(doc => {
    console.log(`- ${doc.properties.Document ID.title[0].text.content}: ${doc.properties.Title.rich_text[0].text.content}`);
});
```

## 검증 체크리스트

Document Registry 구현 후 다음을 확인합니다:

- [ ] 문서 생성 시 Notion DB에 자동 등록되는가?
- [ ] Document ID가 자동 생성되는가?
- [ ] 버전 히스토리가 관리되는가?
- [ ] 버전 업데이트가 올바르게 작동하는가?
- [ ] 검토일 알림이 설정되는가?
- [ ] 검토일 모니터링이 경고를 표시하는가?
- [ ] 문서 상태 변경이 감사 로그에 기록되는가?
- [ ] Regulatory Requirements와 연동되는가?

## 문제 해결

### Document ID 중복

**문제**: Document ID가 중복 생성됨

**해결**:
1. 문서 유형별 시퀀스 확인
2. 동시 생성 제어 로직 추가
3. ID 생성 잠금 메커니즘 구현

### 버전 업데이트 오류

**문제**: 버전이 올바르게 업데이트되지 않음

**해결**:
1. 버전 계산 로직 검증
2. Minor/Major 구분 확인
3. 현재 버전 조회 정확성 확인

### 검토일 경고 미작동

**문제**: 검토일 경고가 작동하지 않음

**해결**:
1. Review Date 필드 확인
2. 모니터링 스케줄 확인
3. Google Calendar 연동 확인

## 다음 단계

- [CAPA Tracker](capa-tracker.md)로 시정예방조치 관리 방법 학습
- [Risk Register](risk-register.md)로 위험 관리 방법 학습
- [Quality Validation](quality-validation.md)으로 데이터 무결성 검증 방법 학습
