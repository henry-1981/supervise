# Quality Validation

데이터 무결성을 검증하고 관계 무결성을 보장하는 품질 검증 모듈입니다. 관계 필드 검증, 고아 페이지 탐지, 감사 추적 완전성 검사 기능을 제공합니다.

## 개요

Quality Validation은 Notion 데이터베이스의 품질을 보장합니다. VALID 프레임워크의 Linked(연결됨), Inspectable(검증 가능함) 차원을 지원합니다.

## 검증 영역

### 1. 관계 무결성 (Referential Integrity)

**목적**: Relation 필드가 올바른 대상을 참조하는지 확인

**검증 항목**:
- Regulatory Requirements ↔ Document Registry
- CAPA Tracker ↔ Risk Register
- CAPA Tracker ↔ Document Registry
- Risk Register ↔ CAPA Tracker
- Submission Tracker ↔ Document Registry
- Knowledge Base ↔ Regulatory Requirements

### 2. 고아 페이지 탐지 (Orphaned Page Detection)

**목적**: 관계가 없는 페이지를 식별하고 경고

**검증 항목**:
- 관계가 없는 요구사항
- 관계가 없는 문서
- CAPA와 연결되지 않은 위험
- 위험과 연결되지 않은 CAPA

### 3. 감사 추적 완전성 (Audit Trail Completeness)

**목적**: 모든 변경이 감사 로그에 기록되었는지 확인

**검증 항목**:
- 모든 페이지 생성이 로그에 기록됨
- 모든 상태 변경이 로그에 기록됨
- 모든 Relation 변경이 로그에 기록됨
- 감사 로그 무결성 (수정 불가)

## 관계 무결성 검증

### Relation 필드 검증

```typescript
/**
 * 관계 무결성 검증
 */
async function validateReferentialIntegrity(): Promise<ValidationResult> {
    const violations: IntegrityViolation[] = [];

    // 1. Regulatory Requirements → Document Registry
    violations.push(...await validateRelation(
        "Regulatory Requirements",
        "Related Documents",
        "Document Registry"
    ));

    // 2. CAPA Tracker → Risk Register
    violations.push(...await validateRelation(
        "CAPA Tracker",
        "Related Risk",
        "Risk Register"
    ));

    // 3. CAPA Tracker → Document Registry
    violations.push(...await validateRelation(
        "CAPA Tracker",
        "Related Documents",
        "Document Registry"
    ));

    // 4. Risk Register → CAPA Tracker
    violations.push(...await validateRelation(
        "Risk Register",
        "Related CAPA",
        "CAPA Tracker"
    ));

    // 5. Submission Tracker → Document Registry
    violations.push(...await validateRelation(
        "Submission Tracker",
        "Related Documents",
        "Document Registry"
    ));

    // 6. Knowledge Base → Regulatory Requirements
    violations.push(...await validateRelation(
        "Knowledge Base",
        "Related Requirements",
        "Regulatory Requirements"
    ));

    return {
        valid: violations.length === 0,
        violations
    };
}

/**
 * 단일 Relation 검증
 */
async function validateRelation(
    sourceDB: string,
    relationProperty: string,
    targetDB: string
): Promise<IntegrityViolation[]> {
    const violations: IntegrityViolation[] = [];

    // 소스 데이터베이스 조회
    const sourcePages = await mcp__notion__query-database({
        database_id: getDatabaseId(sourceDB)
    });

    // 각 페이지의 Relation 검증
    for (const page of sourcePages.results) {
        const relations = page.properties[relationProperty]?.relation || [];

        for (const relation of relations) {
            try {
                // 대상 페이지가 존재하는지 확인
                await mcp__notion__retrieve-page({ page_id: relation.id });
            } catch (error) {
                violations.push({
                    type: "broken_relation",
                    source: page.id,
                    target: relation.id,
                    relation: relationProperty,
                    message: `${sourceDB}의 ${page.properties.title}가 존재하지 않는 ${targetDB}를 참조합니다.`
                });
            }
        }
    }

    return violations;
}
```

### 양방향 관계 검증

```typescript
/**
 * 양방향 관계 검증 (A → B, B → A)
 */
async function validateBidirectionalRelation(
    sourceDB: string,
    sourceRelation: string,
    targetDB: string,
    targetRelation: string
): Promise<BidirectionalViolation[]> {
    const violations: BidirectionalViolation[] = [];

    // 소스 → 타겟 관계 조회
    const sourcePages = await mcp__notion__query-database({
        database_id: getDatabaseId(sourceDB)
    });

    for (const sourcePage of sourcePages.results) {
        const relations = sourcePage.properties[sourceRelation]?.relation || [];

        for (const relation of relations) {
            // 타겟 페이지 조회
            const targetPage = await mcp__notion__retrieve-page({ page_id: relation.id });
            const targetRelations = targetPage.properties[targetRelation]?.relation || [];

            // 역방향 관계 확인
            const hasBackReference = targetRelations.some(r => r.id === sourcePage.id);

            if (!hasBackReference) {
                violations.push({
                    type: "missing_back_reference",
                    sourcePage: sourcePage.id,
                    targetPage: relation.id,
                    message: `${sourceDB} → ${targetDB} 관계가 있지만, 역방향 관계가 없습니다.`
                });
            }
        }
    }

    return violations;
}
```

## 고아 페이지 탐지

### 종합 고아 페이지 탐지

```typescript
/**
 * 모든 데이터베이스의 고아 페이지 탐지
 */
async function detectAllOrphanedPages(): Promise<OrphanedPagesReport> {
    return {
        orphanedRequirements: await detectOrphanedRequirements(),
        orphanedDocuments: await detectOrphanedDocuments(),
        orphanedRisks: await detectOrphanedRisks(),
        orphanedCAPAs: await detectOrphanedCAPAs(),
        orphanedSubmissions: await detectOrphanedSubmissions()
    };
}

/**
 * 고아 요구사항 탐지 (문서와 연결되지 않음)
 */
async function detectOrphanedRequirements(): Promise<OrphanedPage[]> {
    const orphanedPages: OrphanedPage[] = [];

    const requirements = await mcp__notion__query-database({
        database_id: REGULATORY_REQUIREMENTS_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { does_not_equal: "Implemented" } },
                { property: "Related Documents", relation: { is_empty: true } }
            ]
        }
    });

    for (const req of requirements.results) {
        orphanedPages.push({
            pageId: req.id,
            title: req.properties.Requirement ID?.title[0]?.text?.content,
            type: "Requirement",
            reason: "문서와 연결되지 않음",
            severity: "warning"
        });
    }

    return orphanedPages;
}

/**
 * 고아 문서 탐지 (요구사항과 연결되지 않음)
 */
async function detectOrphanedDocuments(): Promise<OrphanedPage[]> {
    const orphanedPages: OrphanedPage[] = [];

    const documents = await mcp__notion__query-database({
        database_id: DOCUMENT_REGISTRY_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { equals: "Approved" } },
                { property: "Related Requirements", relation: { is_empty: true } }
            ]
        }
    });

    for (const doc of documents.results) {
        orphanedPages.push({
            pageId: doc.id,
            title: doc.properties.Document ID?.title[0]?.text?.content,
            type: "Document",
            reason: "요구사항과 연결되지 않음",
            severity: "info"
        });
    }

    return orphanedPages;
}

/**
 * 고아 위험 탐지 (CAPA와 연결되지 않음, Open만)
 */
async function detectOrphanedRisks(): Promise<OrphanedPage[]> {
    const orphanedPages: OrphanedPage[] = [];

    const risks = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { equals: "Open" } },
                {
                    property: "Acceptability",
                    select: { equals: "Not Acceptable" }
                },
                { property: "Related CAPA", relation: { is_empty: true } }
            ]
        }
    });

    for (const risk of risks.results) {
        orphanedPages.push({
            pageId: risk.id,
            title: risk.properties.Risk ID?.title[0]?.text?.content,
            type: "Risk",
            reason: "허용 불가능 위험인데 CAPA와 연결되지 않음",
            severity: "critical"
        });
    }

    return orphanedPages;
}

/**
 * 고아 CAPA 탐지 (위험과 연결되지 않음)
 */
async function detectOrphanedCAPAs(): Promise<OrphanedPage[]> {
    const orphanedPages: OrphanedPage[] = [];

    const capas = await mcp__notion__query-database({
        database_id: CAPA_TRACKER_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { does_not_equal: "Closed" } },
                {
                    or: [
                        { property: "Source", select: { equals: "Internal Audit" } },
                        { property: "Source", select: { equals: "Nonconformance" } }
                    ]
                },
                { property: "Related Risk", relation: { is_empty: true } }
            ]
        }
    });

    for (const capa of capas.results) {
        orphanedPages.push({
            pageId: capa.id,
            title: capa.properties.CAPA ID?.title[0]?.text?.content,
            type: "CAPA",
            reason: "위험과 연결되지 않음",
            severity: "warning"
        });
    }

    return orphanedPages;
}

/**
 * 고아 제출물 탐지 (문서와 연결되지 않음)
 */
async function detectOrphanedSubmissions(): Promise<OrphanedPage[]> {
    const orphanedPages: OrphanedPage[] = [];

    const submissions = await mcp__notion__query-database({
        database_id: SUBMISSION_TRACKER_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { does_not_equal: "Approved" } },
                { property: "Related Documents", relation: { is_empty: true } }
            ]
        }
    });

    for (const sub of submissions.results) {
        orphanedPages.push({
            pageId: sub.id,
            title: sub.properties.Submission ID?.title[0]?.text?.content,
            type: "Submission",
            reason: "문서와 연결되지 않음",
            severity: "warning"
        });
    }

    return orphanedPages;
}
```

### 고아 페이지 경고 생성

```typescript
/**
 * 고아 페이지 경고 생성
 */
async function generateOrphanedPageWarnings(report: OrphanedPagesReport): Promise<Warning[]> {
    const warnings: Warning[] = [];

    // Critical 위험 경고
    if (report.orphanedRisks.length > 0) {
        warnings.push({
            level: "critical",
            title: "허용 불가능 위험이 CAPA와 연결되지 않음",
            message: `${report.orphanedRisks.length}개의 위험이 CAPA 없이 열려 있습니다.`,
            action: "즉시 CAPA를 생성하십시오.",
            items: report.orphanedRisks
        });
    }

    // Warning 경고
    const warningCount = report.orphanedRequirements.length +
                        report.orphanedCAPAs.length +
                        report.orphanedSubmissions.length;

    if (warningCount > 0) {
        warnings.push({
            level: "warning",
            title: "연결되지 않은 항목 존재",
            message: `${warningCount}개의 항목이 적절한 연결이 없습니다.`,
            action: "관계를 검토하고 연결을 설정하십시오.",
            items: [
                ...report.orphanedRequirements,
                ...report.orphanedCAPAs,
                ...report.orphanedSubmissions
            ]
        });
    }

    // Info 알림
    if (report.orphanedDocuments.length > 0) {
        warnings.push({
            level: "info",
            title: "요구사항 없는 승인 문서",
            message: `${report.orphanedDocuments.length}개의 문서가 요구사항과 연결되지 않았습니다.`,
            action: "문서가 요구사항 없이 생성된 경우 검토가 필요합니다.",
            items: report.orphanedDocuments
        });
    }

    return warnings;
}
```

## 감사 추적 완전성 검증

### 감사 로그 무결성 검증

```typescript
/**
 * 감사 추적 완전성 검증
 */
async function validateAuditTrailCompleteness(): Promise<AuditTrailValidationResult> {
    const issues: AuditTrailIssue[] = [];

    // 1. 모든 페이지 생성이 로그에 기록되었는지 확인
    issues.push(...await validateAllPageCreationsLogged());

    // 2. 모든 상태 변경이 로그에 기록되었는지 확인
    issues.push(...await validateAllStatusChangesLogged());

    // 3. 모든 Relation 변경이 로그에 기록되었는지 확인
    issues.push(...await validateAllRelationChangesLogged());

    // 4. 감사 로그 수정 불가 확인
    issues.push(...await validateAuditLogImmutability());

    return {
        complete: issues.length === 0,
        issues
    };
}

/**
 * 페이지 생성 로그 검증
 */
async function validateAllPageCreationsLogged(): Promise<AuditTrailIssue[]> {
    const issues: AuditTrailIssue[] = [];

    // 모든 데이터베이스의 페이지 조회
    const databases = [
        REGULATORY_REQUIREMENTS_DB_ID,
        DOCUMENT_REGISTRY_DB_ID,
        CAPA_TRACKER_DB_ID,
        RISK_REGISTER_DB_ID,
        SUBMISSION_TRACKER_DB_ID
    ];

    for (const dbId of databases) {
        const pages = await mcp__notion__query-database({
            database_id: dbId
        });

        for (const page of pages.results) {
            const createdTime = page.created_time;
            const pageId = page.id;

            // 감사 로그에서 해당 생성 이벤트 검색
            const logExists = await auditLogEntryExists({
                action: "Create",
                entityId: pageId,
                timestamp: createdTime
            });

            if (!logExists) {
                issues.push({
                    type: "missing_creation_log",
                    pageId,
                    message: `페이지 생성 로그가 누락되었습니다.`,
                    severity: "high"
                });
            }
        }
    }

    return issues;
}

/**
 * 상태 변경 로그 검증
 */
async function validateAllStatusChangesLogged(): Promise<AuditTrailIssue[]> {
    const issues: AuditTrailIssue[] = [];

    // Audit Log의 상태 변경 이벤트와 Notion 페이지의 상태 비교
    const auditLogs = await mcp__notion__query-database({
        database_id: AUDIT_LOG_DB_ID,
        filter: {
            property: "Action",
            select: { equals: "Update" }
        }
    });

    for (const log of auditLogs.results) {
        const entityId = log.properties.Entity ID?.title[0]?.text?.content;
        const statusChange = log.properties.Decision?.rich_text[0]?.text?.content;

        if (statusChange?.includes("상태 변경")) {
            // Notion 페이지의 Last Modified와 감사 로그의 Timestamp 비교
            const page = await mcp__notion__retrieve-page({ page_id: entityId });
            const lastModified = new Date(page.last_edited_time);
            const logTimestamp = new Date(log.created_time);

            // 감사 로그가 페이지 수정 후 1분 이내에 기록되었는지 확인
            const timeDiff = Math.abs(lastModified.getTime() - logTimestamp.getTime());
            if (timeDiff > 60000) { // 1분
                issues.push({
                    type: "late_status_log",
                    pageId: entityId,
                    message: `상태 변경 로그가 지연 기록되었습니다.`,
                    severity: "medium"
                });
            }
        }
    }

    return issues;
}

/**
 * 감사 로그 무결성 검증 (수정 불가)
 */
async function validateAuditLogImmutability(): Promise<AuditTrailIssue[]> {
    const issues: AuditTrailIssue[] = [];

    const auditLogs = await mcp__notion__query-database({
        database_id: AUDIT_LOG_DB_ID
    });

    for (const log of auditLogs.results) {
        const createdTime = new Date(log.created_time);
        const lastEditedTime = new Date(log.last_edited_time);

        // 생성 시간과 마지막 수정 시간이 다르면 수정됨
        if (createdTime.getTime() !== lastEditedTime.getTime()) {
            issues.push({
                type: "modified_audit_log",
                pageId: log.id,
                message: `감사 로그가 수정되었습니다 (무결성 위반)`,
                severity: "critical"
            });
        }
    }

    return issues;
}

/**
 * 감사 로그 항목 존재 확인
 */
async function auditLogEntryExists(criteria: AuditLogCriteria): Promise<boolean> {
    const logs = await mcp__notion__query-database({
        database_id: AUDIT_LOG_DB_ID,
        filter: {
            and: [
                { property: "Action", select: { equals: criteria.action } },
                { property: "Entity ID", title: { equals: criteria.entityId } }
            ]
        }
    });

    return logs.results.length > 0;
}
```

## 자동 복구

### 관계 자동 복구

```typescript
/**
 * 끊어진 관계 자동 복구
 */
async function autoRepairRelations(violations: IntegrityViolation[]): Promise<RepairResult> {
    const repaired = [];
    const failed = [];

    for (const violation of violations) {
        try {
            // 끊어진 관계 제거
            await mcp__notion__update-page({
                page_id: violation.source,
                properties: {
                    [violation.relation]: { relation: [] }
                }
            });

            repaired.push(violation);
        } catch (error) {
            failed.push({ violation, error });
        }
    }

    return {
        repairedCount: repaired.length,
        failedCount: failed.length,
        repaired,
        failed
    };
}
```

## 사용 예시

### 예시 1: 전체 품질 검증

```typescript
// 1. 관계 무결성 검증
const integrityResult = await validateReferentialIntegrity();
if (!integrityResult.valid) {
    console.log("관계 무결성 위반 발견:");
    integrityResult.violations.forEach(v => console.log(`- ${v.message}`));
}

// 2. 고아 페이지 탐지
const orphanedReport = await detectAllOrphanedPages();
const warnings = await generateOrphanedPageWarnings(orphanedReport);
warnings.forEach(w => console.log(`[${w.level.toUpperCase()}] ${w.title}: ${w.message}`));

// 3. 감사 추적 완전성 검증
const auditResult = await validateAuditTrailCompleteness();
if (!auditResult.complete) {
    console.log("감사 추적 문제 발견:");
    auditResult.issues.forEach(i => console.log(`- ${i.message}`));
}
```

### 예시 2: 자동 복구

```typescript
// 관계 무결성 위반 자동 복구
const repairResult = await autoRepairRelations(integrityResult.violations);

console.log(`${repairResult.repairedCount}개 복구 완료`);
console.log(`${repairResult.failedCount}개 복구 실패`);
```

### 예시 3: 주기적 품질 검증

```typescript
// 주기적 품질 검증 스케줄 (예: 매일)
setInterval(async () => {
    const report = await detectAllOrphanedPages();
    const warnings = await generateOrphanedPageWarnings(report);

    // Critical 경고만 즉시 알림
    warnings.filter(w => w.level === "critical").forEach(warning => {
        await sendSystemAlert({
            level: "critical",
            message: warning.message,
            action: "review_orphans"
        });
    });
}, 24 * 60 * 60 * 1000); // 24시간
```

## 검증 체크리스트

Quality Validation 구현 후 다음을 확인합니다:

- [ ] 관계 무결성 검증이 작동하는가?
- [ ] 고아 페이지 탐지가 정확한가?
- [ ] 감사 추적 완전성 검증이 작동하는가?
- [ ] 감사 로그 무결성이 보장되는가?
- [ ] 경고 시스템이 작동하는가?
- [ ] 자동 복구 기능이 작동하는가?
- [ ] 주기적 검증이 가능한가?

## 문제 해결

### 검증 성능 저하

**문제**: 대용량 데이터베이스 검증이 느림

**해결**:
1. 배치 처리로 페이지 단위 조회
2. 병렬 검증 실행
3. 캐싱으로 중복 조회 방지

### 거짓 양성 (False Positive)

**문제**: 실제로는 문제가 없는데 위반으로 탐지됨

**해결**:
1. 검증 로직 검토
2. 예외 처리 규칙 추가
3. 탐지 기준 조정

### 자동 복구 실패

**문제**: 자동 복구가 실패함

**해결**:
1. 실패 원인 로깅
2. 사용자에게 수동 복구 안내
3. 복구 전 백업 생성

## 다음 단계

- [Traceability Matrix](traceability.md)로 추적성 관리 방법 학습
- [CAPA Tracker](capa-tracker.md)로 시정예방조치 관리 방법 학습
- [Risk Register](risk-register.md)로 위험 관리 방법 학습
