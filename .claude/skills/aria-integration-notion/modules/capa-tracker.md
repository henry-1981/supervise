# CAPA Tracker

시정 및 예방 조치(Corrective and Preventive Action) 관리를 위한 Notion 연동 모듈입니다. CAPA 자동 등록, Risk Register 연동, 마감일 알림 기능을 제공합니다.

## 개요

CAPA Tracker는 ISO 13485 요구사항에 따라 비적합, 불만, 감사 결과, 규제 관찰 사항으로부터 발생한 시정 및 예방 조치를 관리합니다.

## CAPA 프로세스 흐름

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 문제 식별 (Identification)                                │
│    - 내부 감사, 고객 불만, 비적합, FDA 관찰 사항              │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. 근본 원인 분석 (Root Cause Analysis)                       │
│    - 5 Why, Fishbone, FMEA                                   │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. 조치 계획 (Action Plan)                                   │
│    - 시정 조치 (Correction): 즉시 조치                        │
│    - 예방 조치 (Prevention): 재발 방지                        │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. 구현 (Implementation)                                     │
│    - 조치 실행, 담당자 할당, 마감일 설정                      │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. 효과 검증 (Verification)                                  │
│    - 조치 효과 확인, 재발 방지 확인                           │
└─────────────────────────────────────────────────────────────┘
```

## Notion 자동 등록

### CAPA 생성 시 자동 등록

```typescript
/**
 * CAPA 생성 시 Notion DB에 자동 등록
 */
async function createCAPANotionEntry(capaData: CAPAData) {
    // CAPA ID 자동 생성
    const capaId = generateCAPAId();

    // Notion 페이지 생성
    const capaPage = await mcp__notion__create-page({
        parent: { database_id: CAPA_TRACKER_DB_ID },
        properties: {
            "CAPA ID": { title: [{ text: { content: capaId } }] },
            "Source": { select: { name: capaData.source } },
            "Problem Statement": { rich_text: [{ text: { content: capaData.problemStatement } }] },
            "Root Cause": { rich_text: [{ text: { content: capaData.rootCause } }] },
            "Correction Action": { rich_text: [{ text: { content: capaData.correction } }] },
            "Prevention Action": { rich_text: [{ text: { content: capaData.prevention } }] },
            "Severity": { select: { name: capaData.severity } },
            "Status": { status: { name: "Open" } },
            "Opened Date": { date: { start: new Date().toISOString() } },
            "Target Date": { date: { start: capaData.targetDate } },
            "Assigned To": { people: [{ id: capaData.assigneeId }] }
        }
    });

    // 감사 추적 기록
    await logAuditTrail({
        action: "Create",
        entity: "CAPA",
        entityId: capaId,
        decision: `CAPA 생성: ${capaData.problemStatement}`,
        rationale: capaData.source
    });

    return capaPage;
}
```

### CAPA ID 생성 규칙

```
CAPA-{YYYY}-{NNN}
예시: CAPA-2026-001, CAPA-2026-002
```

```typescript
/**
 * CAPA ID 자동 생성
 */
function generateCAPAId(): string {
    const year = new Date().getFullYear();
    const sequence = getNextSequenceNumber(year);
    return `CAPA-${year}-${sequence.toString().padStart(3, '0')}`;
}

/**
 * 연도별 시퀀스 번호 조회
 */
async function getNextSequenceNumber(year: number): Promise<number> {
    const query = await mcp__notion__query-database({
        database_id: CAPA_TRACKER_DB_ID,
        filter: {
            property: "CAPA ID",
            title: {
                contains: `CAPA-${year}`
            }
        }
    });

    return query.results.length + 1;
}
```

## Risk Register 연동

### CAPA-Risk 연결

```typescript
/**
 * CAPA 생성 시 관련 위험 자동 연결
 */
async function linkCAPAToRisk(capaPageId: string, riskId: string) {
    // CAPA → Risk 연결
    await mcp__notion__update-page({
        page_id: capaPageId,
        properties: {
            "Related Risk": {
                relation: [{ id: riskId }]
            }
        }
    });

    // Risk → CAPA 양방향 연결
    await mcp__notion__update-page({
        page_id: riskId,
        properties: {
            "Related CAPA": {
                relation: [{ id: capaPageId }]
            }
        }
    });
}
```

### 위험 기반 CAPA 생성

```typescript
/**
 * 위험 등록 시 CAPA 자동 생성 제안
 */
async function suggestCAPAForRisk(riskPageId: string) {
    const risk = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID,
        filter: {
            property: "Risk ID",
            title: { equals: riskPageId }
        }
    });

    const riskData = risk.results[0];
    const acceptability = riskData.properties.Acceptability.select.name;

    if (acceptability === "Not Acceptable") {
        return {
            shouldCreate: true,
            reason: "위험이 허용 불가능 수준입니다. CAPA가 필요합니다.",
            suggestedSource: "Risk Assessment",
            suggestedSeverity: riskData.properties.RPNNumber.number > 6 ? "Critical" : "Major"
        };
    }

    return { shouldCreate: false };
}
```

## 마감일 알림

### 알림 설정

```typescript
/**
 * CAPA 마감일 알림 설정
 */
async function setupCAPADueDateReminder(capaPageId: string) {
    const capa = await mcp__notion__query-database({
        database_id: CAPA_TRACKER_DB_ID,
        filter: {
            property: "CAPA ID",
            title: { equals: capaPageId }
        }
    });

    const targetDate = capa.results[0].properties.TargetDate.date.start;

    // Google Calendar 이벤트 생성 (Google Workspace MCP 연동)
    const calendarEvent = await createGoogleCalendarEvent({
        title: `CAPA 마감일 알림: ${capaPageId}`,
        start: targetDate,
        reminders: [
            { method: "email", minutes: 10080 }, // 1주 전
            { method: "email", minutes: 1440 },  // 1일 전
            { method: "popup", minutes: 0 }      // 당일
        ],
        description: `CAPA 문제: ${capa.results[0].properties.ProblemStatement.rich_text[0].text.content}`
    });

    // CAPA 페이지에 캘린더 이벤트 링크 추가
    await mcp__notion__update-page({
        page_id: capaPageId,
        properties: {
            "Calendar Event": {
                url: calendarEvent.htmlLink
            }
        }
    });
}
```

### 마감일 모니터링

```typescript
/**
 * 마감일 임박 CAPA 모니터링
 */
async function monitorCAPADueDates() {
    const today = new Date();
    const warningDays = 7;

    // 7일 이내 마감 CAPA 조회
    const upcomingCAPAs = await mcp__notion__query-database({
        database_id: CAPA_TRACKER_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { does_not_equal: "Closed" } },
                {
                    property: "Target Date",
                    date: {
                        on_or_before: new Date(today.getTime() + warningDays * 24 * 60 * 60 * 1000).toISOString()
                    }
                }
            ]
        }
    });

    // 경과 CAPA 조회
    const overdueCAPAs = upcomingCAPAs.results.filter(capa => {
        const targetDate = new Date(capa.properties.Target Date.date.start);
        return targetDate < today;
    });

    return {
        upcoming: upcomingCAPAs.results.filter(c => !overdueCAPAs.includes(c)),
        overdue: overdueCAPAs
    };
}
```

## CAPA 상태 관리

### 상태 전이

```
Open → In Progress → Closed → Verified
  ↓                      ↓
Cancelled               Reopened
```

### 상태 변경 로직

```typescript
/**
 * CAPA 상태 변경
 */
async function updateCAPAStatus(
    capaPageId: string,
    newStatus: "Open" | "In Progress" | "Closed" | "Verified" | "Cancelled" | "Reopened",
    reason: string
) {
    // 상태 변경
    await mcp__notion__update-page({
        page_id: capaPageId,
        properties: {
            "Status": { status: { name: newStatus } },
            "Last Modified": { date: { start: new Date().toISOString() } }
        }
    });

    // 완료일 자동 설정
    if (newStatus === "Closed" || newStatus === "Verified") {
        await mcp__notion__update-page({
            page_id: capaPageId,
            properties: {
                "Completed Date": { date: { start: new Date().toISOString() } }
            }
        });
    }

    // 감사 추적 기록
    await logAuditTrail({
        action: "Update",
        entity: "CAPA",
        entityId: capaPageId,
        decision: `상태 변경: ${newStatus}`,
        rationale: reason
    });
}
```

## 효과 검증

### 검증 체크리스트

```typescript
/**
 * CAPA 효과 검증 체크리스트
 */
interface CAPAVerificationChecklist {
    /** 시정 조치가 완료되었는가? */
    correctionCompleted: boolean;

    /** 예방 조치가 구현되었는가? */
    preventionImplemented: boolean;

    /** 재발 방지 확인되었는가? */
    recurrencePrevented: boolean;

    /** 근본 원인이 해결되었는가? */
    rootCauseEliminated: boolean;

    /** 문서화가 완료되었는가? */
    documentationComplete: boolean;

    /** 관련자가 훈련되었는가? */
    personnelTrained: boolean;
}

/**
 * CAPA 효과 검증
 */
async function verifyCAPAEffectiveness(
    capaPageId: string,
    checklist: CAPAVerificationChecklist
): Promise<{ verified: boolean; findings: string[] }> {
    const findings: string[] = [];

    if (!checklist.correctionCompleted) {
        findings.push("시정 조치가 완료되지 않았습니다.");
    }

    if (!checklist.preventionImplemented) {
        findings.push("예방 조치가 구현되지 않았습니다.");
    }

    if (!checklist.recurrencePrevented) {
        findings.push("재발 방지가 확인되지 않았습니다.");
    }

    if (!checklist.rootCauseEliminated) {
        findings.push("근본 원인이 해결되지 않았습니다.");
    }

    const verified = findings.length === 0;

    if (verified) {
        // 상태를 Verified로 변경
        await updateCAPAStatus(capaPageId, "Verified", "모든 검증 항목 통과");
    }

    return { verified, findings };
}
```

## 사용 예시

### 예시 1: 내부 감사 발견사항 CAPA 생성

```typescript
const capa = await createCAPANotionEntry({
    source: "Internal Audit",
    problemStatement: "Design validation procedure not followed for Device X",
    rootCause: "Insufficient training on design control requirements",
    correction: "Retrain design team on 21 CFR 820.30",
    prevention: "Update SOP-DC-001 with detailed validation checklist",
    severity: "Major",
    targetDate: "2026-03-15",
    assigneeId: "user-id-123"
});

// 관련 위험 연결 (위험 ID: RISK-015)
await linkCAPAToRisk(capa.id, "RISK-015");

// 마감일 알림 설정
await setupCAPADueDateReminder(capa.id);
```

### 예시 2: FDA 관찰사항 CAPA 생성

```typescript
const capa = await createCAPANotionEntry({
    source: "FDA Observation",
    problemStatement: "FDA 483 Observation: Lack of CAPA procedure documentation",
    rootCause: "CAPA procedure not updated per ISO 13485:2016",
    correction: "Revise CAPA procedure within 30 days",
    prevention: "Implement procedure review cycle annually",
    severity: "Critical",
    targetDate: "2026-03-01",
    assigneeId: "user-id-456"
});

// Critical CAPA: 즉시 경고
await sendCriticalCAPAAlert(capa.id);
```

### 예시 3: CAPA 효과 검증

```typescript
const verification = await verifyCAPAEffectiveness("CAPA-2026-001", {
    correctionCompleted: true,
    preventionImplemented: true,
    recurrencePrevented: true,
    rootCauseEliminated: true,
    documentationComplete: false,
    personnelTrained: false
});

if (!verification.verified) {
    console.log("CAPA 검증 실패:");
    verification.findings.forEach(finding => console.log(`- ${finding}`));
}
```

## 검증 체크리스트

CAPA Tracker 구현 후 다음을 확인합니다:

- [ ] CAPA 생성 시 Notion DB에 자동 등록되는가?
- [ ] CAPA ID가 자동 생성되는가?
- [ ] Risk Register와 연동되는가?
- [ ] 마감일 알림이 설정되는가?
- [ ] 상태 변경이 감사 로그에 기록되는가?
- [ ] 효과 검증 체크리스트가 작동하는가?
- [ ] 마감일 모니터링이 경고를 표시하는가?

## 문제 해결

### CAPA-Risk 연결 실패

**문제**: CAPA와 위험 간 연결이 실패함

**해결**:
1. Risk Register에 해당 위험이 존재하는지 확인
2. Relation 속성이 올바르게 설정되었는지 확인
3. 양방향 연결이 필요한지 확인

### 마감일 알림 미작동

**문제**: Google Calendar 알림이 작동하지 않음

**해결**:
1. Google Workspace MCP가 설정되었는지 확인
2. OAuth 인증이 유효한지 확인
3. 캘린더 권한이 있는지 확인

### 효과 검증 실패

**문제**: CAPA가 검증에 통과하지 못함

**해결**:
1. 검증 체크리스트 항목 검토
2. CAPA 문서화 상태 확인
3. 관련자 훈련 상태 확인

## 다음 단계

- [Risk Register](risk-register.md)로 위험 관리 방법 학습
- [Document Registry](document-registry.md)로 문서 관리 방법 학습
- [Quality Validation](quality-validation.md)으로 데이터 무결성 검증 방법 학습
