# Risk Register

ISO 14971 위험 관리를 위한 Notion 연동 모듈입니다. 위험 자동 등록, Risk Index 자동 계산, 수용성 평가, 경고 기능을 제공합니다.

## 개요

Risk Register는 의료기기 위험 관리 프로세스를 지원합니다. ISO 14971:2019 요구사항에 따라 위험 식별, 평가, 완화, 잔여 위험 평가를 관리합니다.

## 위험 관리 프로세스

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 위험 식별 (Risk Identification)                           │
│    - 위해 요소(Hazard), 위해 상황(Hazardous Situation)       │
│    - 손상(Harm) 식별                                          │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. 위험 평가 (Risk Estimation)                               │
│    - 심각도(Severity), 발생 확률(Probability) 평가            │
│    - Risk Index = Severity × Probability                     │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. 위험 평가 (Risk Evaluation)                               │
│    - 수용성(Acceptability) 평가                               │
│    - Acceptable, Not Acceptable, ALARP                      │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. 위험 완화 (Risk Mitigation)                               │
│    - 완화 조치 구현                                          │
│    - 잔여 위험 평가                                          │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. 위험 검토 (Risk Review)                                   │
│    - 정기 검토, 변경 시 검토                                  │
└─────────────────────────────────────────────────────────────┘
```

## Notion 자동 등록

### 위험 생성 시 자동 등록

```typescript
/**
 * 위험 생성 시 Notion DB에 자동 등록
 */
async function createRiskNotionEntry(riskData: RiskData) {
    // Risk ID 자동 생성
    const riskId = generateRiskId();

    // Risk Index 계산
    const riskIndex = calculateRiskIndex(riskData.severity, riskData.probability);
    const acceptability = evaluateRiskAcceptability(riskIndex);

    // Notion 페이지 생성
    const riskPage = await mcp__notion__create-page({
        parent: { database_id: RISK_REGISTER_DB_ID },
        properties: {
            "Risk ID": { title: [{ text: { content: riskId } }] },
            "Risk Description": { rich_text: [{ text: { content: riskData.description } }] },
            "Risk Category": { select: { name: riskData.category } },
            "Hazard": { rich_text: [{ text: { content: riskData.hazard } }] },
            "Harm": { rich_text: [{ text: { content: riskData.harm } }] },
            "Severity": { select: { name: mapSeverityToSelect(riskData.severity) } },
            "Probability": { select: { name: mapProbabilityToSelect(riskData.probability) } },
            "RPN Number": { number: riskIndex },
            "Acceptability": { select: { name: acceptability } },
            "Status": { status: { name: "Open" } },
            "Created Date": { date: { start: new Date().toISOString() } },
            "Review Date": { date: { start: calculateReviewDate() } }
        }
    });

    // 감사 추적 기록
    await logAuditTrail({
        action: "Create",
        entity: "Risk",
        entityId: riskId,
        decision: `위험 등록: ${riskData.description}`,
        rationale: `Risk Index: ${riskIndex}, Acceptability: ${acceptability}`
    });

    // 허용 불가능 위험 경고
    if (acceptability === "Not Acceptable") {
        await sendUnacceptableRiskAlert(riskId, riskIndex);
    }

    return riskPage;
}
```

### Risk ID 생성 규칙

```
RISK-{NNN}
예시: RISK-001, RISK-002
```

```typescript
/**
 * Risk ID 자동 생성
 */
async function generateRiskId(): Promise<string> {
    const query = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID
    });

    const nextSequence = query.results.length + 1;
    return `RISK-${nextSequence.toString().padStart(3, '0')}`;
}
```

## Risk Index 자동 계산

### 점수 체계

**Severity (심각도)**:
- High (3): 사망, 심각한 상해
- Medium (2): 건강 위협, 의료 개입 필요
- Low (1): 경미한 상해, 불편함

**Probability (발생 확률)**:
- High (3): 자주 발생 (>10%)
- Medium (2): 때때로 발생 (1-10%)
- Low (1): 드물게 발생 (<1%)

### Risk Index 계산

```typescript
/**
 * Risk Index 계산
 */
function calculateRiskIndex(severity: 1 | 2 | 3, probability: 1 | 2 | 3): number {
    return severity * probability;
}

/**
 * Severity 매핑
 */
function mapSeverityToSelect(severity: 1 | 2 | 3): string {
    const mapping = {
        1: "Low (1)",
        2: "Medium (2)",
        3: "High (3)"
    };
    return mapping[severity];
}

/**
 * Probability 매핑
 */
function mapProbabilityToSelect(probability: 1 | 2 | 3): string {
    const mapping = {
        1: "Low (1)",
        2: "Medium (2)",
        3: "High (3)"
    };
    return mapping[probability];
}
```

## 수용성 평가

### 평가 기준

| Risk Index | Acceptability | 조치 |
|------------|---------------|------|
| 1 (1×1) | Acceptable | 모니터링만 |
| 2 (1×2, 2×1) | Acceptable | 정기 검토 |
| 3 (1×3, 3×1) | ALARP | 합리적으로 실현 가능한 최저 수준으로 완화 |
| 4 (2×2) | ALARP | 완화 조치 고려 |
| 6 (2×3, 3×2) | Not Acceptable | 즉시 완화 조치 필요 |
| 9 (3×3) | Not Acceptable | 즉시 완화 조치 필요, 사용 중단 고려 |

```typescript
/**
 * 위험 수용성 평가
 */
function evaluateRiskAcceptability(riskIndex: number): "Acceptable" | "ALARP" | "Not Acceptable" {
    if (riskIndex <= 2) {
        return "Acceptable";
    } else if (riskIndex <= 4) {
        return "ALARP";
    } else {
        return "Not Acceptable";
    }
}
```

### 자동 평가 로직

```typescript
/**
 * 위험 등록 시 자동 수용성 평가
 */
async function autoEvaluateRiskAcceptability(riskPageId: string) {
    const risk = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID,
        filter: {
            property: "Risk ID",
            title: { equals: riskPageId }
        }
    });

    const riskData = risk.results[0];
    const severity = extractSeverityValue(riskData.properties.Severity.select.name);
    const probability = extractProbabilityValue(riskData.properties.Probability.select.name);
    const riskIndex = calculateRiskIndex(severity, probability);
    const acceptability = evaluateRiskAcceptability(riskIndex);

    // 수용성 업데이트
    await mcp__notion__update-page({
        page_id: riskPageId,
        properties: {
            "RPN Number": { number: riskIndex },
            "Acceptability": { select: { name: acceptability } }
        }
    });

    return { riskIndex, acceptability };
}

/**
 * Severity 값 추출
 */
function extractSeverityValue(selectName: string): 1 | 2 | 3 {
    const match = selectName.match(/\((\d)\)/);
    return parseInt(match[1]) as 1 | 2 | 3;
}

/**
 * Probability 값 추출
 */
function extractProbabilityValue(selectName: string): 1 | 2 | 3 {
    const match = selectName.match(/\((\d)\)/);
    return parseInt(match[1]) as 1 | 2 | 3;
}
```

## 허용 불가능 위험 경고

### 경고 발생 조건

- Risk Index ≥ 6 (Severity 2×Probability 3 또는 Severity 3×Probability 2)
- Risk Index = 9 (Severity 3×Probability 3)

### 경고 로직

```typescript
/**
 * 허용 불가능 위험 경고
 */
async function sendUnacceptableRiskAlert(riskId: string, riskIndex: number) {
    const risk = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID,
        filter: {
            property: "Risk ID",
            title: { equals: riskId }
        }
    });

    const riskData = risk.results[0];
    const description = riskData.properties.Risk Description.rich_text[0].text.content;

    // 경고 수준 결정
    const alertLevel = riskIndex >= 9 ? "Critical" : "High";

    // 경고 메시지 생성
    const alertMessage = `
[${alertLevel} ALERT] 허용 불가능 위험 감지

위험 ID: ${riskId}
위험 설명: ${description}
Risk Index: ${riskIndex}
조치: 즉시 완화 조치가 필요합니다. CAPA를 생성하십시오.
`;

    // 시스템 경고 전송
    await sendSystemAlert({
        level: alertLevel,
        message: alertMessage,
        action: "createCAPA",
        actionParams: { riskId }
    });

    // 감사 추적 기록
    await logAuditTrail({
        action: "Alert",
        entity: "Risk",
        entityId: riskId,
        decision: `허용 불가능 위험 경고 (Risk Index: ${riskIndex})`,
        rationale: "ISO 14971: 즉시 완화 조치 필요"
    });
}
```

### 경고 대시보드

```typescript
/**
 * 허용 불가능 위험 대시보드
 */
async function getUnacceptableRisksDashboard() {
    const unacceptableRisks = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID,
        filter: {
            and: [
                { property: "Acceptability", select: { equals: "Not Acceptable" } },
                { property: "Status", status: { does_not_equal: "Closed" } }
            ]
        },
        sorts: [
            {
                property: "RPN Number",
                direction: "descending"
            }
        ]
    });

    return {
        total: unacceptableRisks.results.length,
        critical: unacceptableRisks.results.filter(r => r.properties.RPN Number.number >= 9).length,
        high: unacceptableRisks.results.filter(r => r.properties.RPN Number.number === 6).length,
        risks: unacceptableRisks.results.map(risk => ({
            id: risk.properties.Risk ID.title[0].text.content,
            description: risk.properties.Risk Description.rich_text[0].text.content,
            riskIndex: risk.properties.RPN Number.number,
            category: risk.properties.Risk Category.select.name,
            status: risk.properties.Status.status.name
        }))
    };
}
```

## 위험 완화

### 완화 전략 설정

```typescript
/**
 * 위험 완화 전략 설정
 */
async function setMitigationStrategy(
    riskPageId: string,
    mitigationStrategy: string,
    residualSeverity: 1 | 2 | 3,
    residualProbability: 1 | 2 | 3
) {
    // 잔여 위험 계산
    const residualRiskIndex = calculateRiskIndex(residualSeverity, residualProbability);
    const residualAcceptability = evaluateRiskAcceptability(residualRiskIndex);

    // 완화 전략 및 잔여 위험 업데이트
    await mcp__notion__update-page({
        page_id: riskPageId,
        properties: {
            "Mitigation Strategy": { rich_text: [{ text: { content: mitigationStrategy } }] },
            "Residual Severity": { select: { name: mapSeverityToSelect(residualSeverity) } },
            "Residual Probability": { select: { name: mapProbabilityToSelect(residualProbability) } },
            "Residual RPN": { number: residualRiskIndex },
            "Status": { status: { name: "Mitigating" } }
        }
    });

    // 감사 추적 기록
    await logAuditTrail({
        action: "Update",
        entity: "Risk",
        entityId: riskPageId,
        decision: `완화 전략 설정 (잔여 위험: ${residualRiskIndex})`,
        rationale: mitigationStrategy
    });

    // 잔여 위험이 허용 불가능한 경우 경고
    if (residualAcceptability === "Not Acceptable") {
        await sendUnacceptableRiskAlert(riskPageId, residualRiskIndex);
    }
}
```

## 위험 검토

### 정기 검토 알림

```typescript
/**
 * 위험 정기 검토 알림 설정
 */
async function setupRiskReviewReminder(riskPageId: string) {
    const risk = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID,
        filter: {
            property: "Risk ID",
            title: { equals: riskPageId }
        }
    });

    const reviewDate = new Date(risk.results[0].properties.Review Date.date.start);

    // Google Calendar 이벤트 생성
    const calendarEvent = await createGoogleCalendarEvent({
        title: `위험 검토 알림: ${riskPageId}`,
        start: reviewDate,
        reminders: [
            { method: "email", minutes: 10080 }, // 1주 전
            { method: "popup", minutes: 0 }
        ],
        description: `위험 검토가 예정되어 있습니다.`
    });

    return calendarEvent;
}
```

### 검토일 계산

```typescript
/**
 * 다음 검토일 계산 (일반적으로 1년 후)
 */
function calculateReviewDate(): string {
    const reviewDate = new Date();
    reviewDate.setFullYear(reviewDate.getFullYear() + 1);
    return reviewDate.toISOString();
}
```

## 사용 예시

### 예시 1: 임상 위험 등록

```typescript
const risk = await createRiskNotionEntry({
    description: "Device malfunction during patient monitoring causing delayed treatment",
    category: "Clinical",
    hazard: "Electrical short circuit",
    harm: "Delayed treatment, patient deterioration",
    severity: 3, // High
    probability: 2, // Medium
    mitigationStrategy: "",
    residualSeverity: null,
    residualProbability: null
});

// Risk Index = 6 (Not Acceptable)
// 자동으로 CAPA 생성 제안
```

### 예시 2: 기술 위험 완화

```typescript
// 위험 완화 전략 설정
await setMitigationStrategy(
    "RISK-015",
    "Implement redundant power supply and alarm system",
    2, // 잔여 심각도: Medium
    1  // 잔여 확률: Low
);

// 잔여 위험 = 2 × 1 = 2 (Acceptable)
// 위험 상태가 Mitigating으로 변경됨
```

### 예시 3: 허용 불가능 위험 대시보드

```typescript
const dashboard = await getUnacceptableRisksDashboard();

console.log(`허용 불가능 위험: ${dashboard.total}개`);
console.log(`Critical (Risk Index ≥ 9): ${dashboard.critical}개`);
console.log(`High (Risk Index = 6): ${dashboard.high}개`);

dashboard.risks.forEach(risk => {
    console.log(`- ${risk.id}: ${risk.description} (Risk Index: ${risk.riskIndex})`);
});
```

## 검증 체크리스트

Risk Register 구현 후 다음을 확인합니다:

- [ ] 위험 생성 시 Notion DB에 자동 등록되는가?
- [ ] Risk ID가 자동 생성되는가?
- [ ] Risk Index가 자동 계산되는가?
- [ ] 수용성이 자동 평가되는가?
- [ ] 허용 불가능 위험 경고가 작동하는가?
- [ ] 완화 전략 설정이 가능한가?
- [ ] 잔여 위험이 계산되는가?
- [ ] 정기 검토 알림이 설정되는가?
- [ ] CAPA Tracker와 연동되는가?

## 문제 해결

### Risk Index 계산 오류

**문제**: Risk Index가 올바르게 계산되지 않음

**해결**:
1. Severity, Probability Select 옵션 확인
2. 값 추출 로직 확인
3. 계산 공식 검증

### 수용성 평가 오류

**문제**: 수용성 평가가 올바르지 않음

**해결**:
1. Risk Index 범위 확인
2. 평가 기준 테이블 검증
3. 평가 로직 수정

### 경고 미작동

**문제**: 허용 불가능 위험 경고가 작동하지 않음

**해결**:
1. 알림 시스템 설정 확인
2. 경고 발생 조건 검증
3. 시스템 경고 전송 로직 확인

## 다음 단계

- [CAPA Tracker](capa-tracker.md)로 시정예방조치 관리 방법 학습
- [Document Registry](document-registry.md)로 문서 관리 방법 학습
- [Quality Validation](quality-validation.md)으로 데이터 무결성 검증 방법 학습
