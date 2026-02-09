# Traceability Matrix

요구사항, 문서, 증거 간의 추적성을 관리하는 Traceability Matrix 모듈입니다. Notion 데이터베이스 간의 Relation을 활용하여 종단 추적성(End-to-End Traceability)을 보장합니다.

## 개요

Traceability Matrix는 다음 관계를 관리합니다:
- Requirements ↔ Documents: 요구사항과 문서 간의 매핑
- Documents ↔ Evidence: 문서와 증거 간의 연결
- CAPA ↔ Risk: 시정예방조치와 위험 관리 간의 연결
- Requirements ↔ CAPA: 규제 요구사항과 CAPA 간의 추적성

## 추적성 모델

### 1. 요구사항-문서 추적성

**목적**: 규제 요구사항이 문서에 올바르게 반영되었는지 확인

**추적 관계**:
```
Regulatory Requirements
    ↓ (Related Documents)
Document Registry
    ↓ (Evidence Link)
증거 문서 (테스트 결과, 검증 기록)
```

**Notion Relation 설정**:
- Regulatory Requirements → Document Registry (Related Documents)
- Document Registry → Regulatory Requirements (Related Requirements)

**자동 Relation 설정**:

```typescript
/**
 * 문서 생성 시 관련 요구사항과 자동으로 Relation 설정
 */
async function linkDocumentToRequirements(
    documentPageId: string,
    requirementIds: string[]
) {
    for (const reqId of requirementIds) {
        await mcp__notion__update-page({
            page_id: documentPageId,
            properties: {
                "Related Requirements": {
                    relation: [{ id: reqId }]
                }
            }
        });
    }
}
```

### 2. 문서-증거 추적성

**목적**: 문서에 대한 증거(테스트 결과, 검증 기록) 연결

**추적 관계**:
```
Document Registry
    ↓ (Evidence Link)
증거 문서 (SOP, WI, RECORD, TEMPLATE)
    ↓ (Audit Log)
변경 이력 및 승인 기록
```

**Evidence Link 필드**:
- URL 타입 속성
- 테스트 결과, 검증 기록 등 증거 문서 링크
- Notion 페이지 또는 외부 파일 링크 지원

### 3. CAPA-Risk 추적성

**목적**: 시정예방조치와 위험 관리 간의 연결

**추적 관계**:
```
Risk Register
    ↓ (Related CAPA)
CAPA Tracker
    ↓ (Related Documents)
문화된 문서 및 증거
```

**양방향 Relation**:
- Risk Register → CAPA Tracker (Related CAPA)
- CAPA Tracker → Risk Register (Related Risk)

**자동 연결 로직**:

```typescript
/**
 * CAPA 생성 시 관련 위험 자동 연결
 */
async function linkCAPAToRisk(
    capaPageId: string,
    riskPageId: string
) {
    // CAPA → Risk 연결
    await mcp__notion__update-page({
        page_id: capaPageId,
        properties: {
            "Related Risk": {
                relation: [{ id: riskPageId }]
            }
        }
    });

    // Risk → CAPA 연결 (양방향)
    await mcp__notion__update-page({
        page_id: riskPageId,
        properties: {
            "Related CAPA": {
                relation: [{ id: capaPageId }]
            }
        }
    });
}
```

### 4. 요구사항-CAPA 추적성

**목적**: 규제 요구사항 불준비에 대한 CAPA 추적

**간접 관계**:
```
Regulatory Requirements
    ↓ (Related Documents)
Document Registry
    ↓ (Related CAPA)
CAPA Tracker
```

## 고아 페이지 탐지

### 정의

고아 페이지(Orphaned Page)는 다음과 같은 페이지를 의미합니다:
1. 관계가 없는 요구사항 (문서와 연결되지 않음)
2. 관계가 없는 문서 (요구사항과 연결되지 않음)
3. CAPA와 연결되지 않은 위험
4. 위험과 연결되지 않은 CAPA

### 탐지 로직

```typescript
/**
 * 고아 페이지 탐지
 */
async function detectOrphanedPages() {
    const orphanedPages = {
        orphanedRequirements: [] as string[],
        orphanedDocuments: [] as string[],
        orphanedRisks: [] as string[],
        orphanedCAPAs: [] as string[]
    };

    // 고아 요구사항 탐지 (문서와 연결되지 않음)
    const requirements = await mcp__notion__query-database({
        database_id: REGULATORY_REQUIREMENTS_DB_ID,
        filter: {
            property: "Related Documents",
            relation: { is_empty: true }
        }
    });

    orphanedPages.orphanedRequirements = requirements.results.map(r => r.id);

    // 고아 문서 탐지 (요구사항과 연결되지 않음)
    const documents = await mcp__notion__query-database({
        database_id: DOCUMENT_REGISTRY_DB_ID,
        filter: {
            property: "Related Requirements",
            relation: { is_empty: true }
        }
    });

    orphanedPages.orphanedDocuments = documents.results.map(d => d.id);

    // 고아 위험 탐지 (CAPA와 연결되지 않음)
    const risks = await mcp__notion__query-database({
        database_id: RISK_REGISTER_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { equals: "Open" } },
                { property: "Related CAPA", relation: { is_empty: true } }
            ]
        }
    });

    orphanedPages.orphanedRisks = risks.results.map(r => r.id);

    // 고아 CAPA 탐지 (위험과 연결되지 않음)
    const capas = await mcp__notion__query-database({
        database_id: CAPA_TRACKER_DB_ID,
        filter: {
            and: [
                { property: "Status", status: { equals: "Open" } },
                { property: "Related Risk", relation: { is_empty: true } }
            ]
        }
    });

    orphanedPages.orphanedCAPAs = capas.results.map(c => c.id);

    return orphanedPages;
}
```

### 경고 시스템

```typescript
/**
 * 고아 페이지 경고 생성
 */
async function warnOrphanedPages(orphanedPages: OrphanedPages) {
    const warnings = [];

    if (orphanedPages.orphanedRequirements.length > 0) {
        warnings.push({
            level: "warning",
            message: `${orphanedPages.orphanedRequirements.length}개의 요구사항이 문서와 연결되지 않았습니다.`,
            action: "요구사항에 관련 문서를 연결하십시오."
        });
    }

    if (orphanedPages.orphanedDocuments.length > 0) {
        warnings.push({
            level: "info",
            message: `${orphanedPages.orphanedDocuments.length}개의 문서가 요구사항과 연결되지 않았습니다.`,
            action: "문서가 요구사항 없이 생성된 경우 검토가 필요합니다."
        });
    }

    if (orphanedPages.orphanedRisks.length > 0) {
        warnings.push({
            level: "critical",
            message: `${orphanedPages.orphanedRisks.length}개의 위험이 CAPA와 연결되지 않았습니다.`,
            action: "위험에 대한 CAPA를 생성하십시오."
        });
    }

    if (orphanedPages.orphanedCAPAs.length > 0) {
        warnings.push({
            level: "warning",
            message: `${orphanedPages.orphanedCAPAs.length}개의 CAPA가 위험과 연결되지 않았습니다.`,
            action: "CAPA가 위험 없이 생성된 경우 검토가 필요합니다."
        });
    }

    return warnings;
}
```

## 추적성 뷰

### Notion 뷰 구성

**Requirements Matrix View**:
- 그룹: Category
- 필터: Status ≠ Implemented
- 속성: Requirement ID, Category, Status, Related Documents, Due Date

**Document Traceability View**:
- 그룹: Document Type
- 필터: Status ≠ Obsolete
- 속성: Document ID, Document Type, Status, Related Requirements, Review Date

**CAPA-Risk Matrix View**:
- 그룹: Status
- 필터: Status ≠ Closed
- 속성: CAPA ID, Severity, Status, Related Risk, Target Date

## 사용 예시

### 예시 1: 새 문서 생성 시 요구사항 연결

```typescript
// 문서 생성
const document = await mcp__notion__create-page({
    parent: { database_id: DOCUMENT_REGISTRY_DB_ID },
    properties: {
        "Document ID": { title: [{ text: { content: "DOC-001" } }] },
        "Document Type": { select: { name: "SOP" } },
        "Version": { number: 1.0 },
        "Title": { rich_text: [{ text: { content: "Design Control Procedure" } }] },
        "Status": { status: { name: "Approved" } }
    }
});

// 관련 요구사항 연결
await linkDocumentToRequirements(
    document.id,
    ["REQ-001", "REQ-002"] // 21 CFR 820.30 요구사항
);
```

### 예시 2: CAPA 생성 시 위험 연결

```typescript
// CAPA 생성
const capa = await mcp__notion__create-page({
    parent: { database_id: CAPA_TRACKER_DB_ID },
    properties: {
        "CAPA ID": { title: [{ text: { content: "CAPA-2026-001" } }] },
        "Source": { select: { name: "Internal Audit" } },
        "Problem Statement": { rich_text: [{ text: { content: "Design validation failure" } }] },
        "Status": { status: { name: "Open" } }
    }
});

// 관련 위험 연결
await linkCAPAToRisk(capa.id, "RISK-015");
```

### 예시 3: 고아 페이지 검사

```typescript
// 고아 페이지 탐지
const orphanedPages = await detectOrphanedPages();

// 경고 생성
const warnings = await warnOrphanedPages(orphanedPages);

// 경고 표시
warnings.forEach(warning => {
    console.log(`[${warning.level.toUpperCase()}] ${warning.message}`);
    console.log(`Action: ${warning.action}`);
});
```

## 검증 체크리스트

Traceability Matrix 구현 후 다음을 확인합니다:

- [ ] 모든 요구사항이 하나 이상의 문서와 연결되었는가?
- [ ] 모든 문서가 요구사항과 연결되었는가? (요구사항 없는 문서 검토)
- [ ] 모든 위험이 CAPA와 연결되었는가? (Open 위험만)
- [ ] 모든 CAPA가 위험과 연결되었는가? (Open CAPA만)
- [ ] 고아 페이지 경고가 정상 작동하는가?
- [ ] 추적성 뷰가 올바르게 구성되었는가?
- [ ] Relation이 양방향으로 설정되었는가?

## 문제 해결

### 관계 설정 실패

**문제**: Relation이 작동하지 않음

**해결**:
1. 대상 데이터베이스가 이미 생성되었는지 확인
2. Relation 속성 이름이 올바른지 확인
3. 페이지 ID가 유효한지 확인

### 고아 페이지 과다

**문제**: 너무 많은 고아 페이지가 탐지됨

**해결**:
1. 데이터 마이그레이션 필요
2. 대량 Relation 설정 스크립트 실행
3. 데이터 정리 프로세스 수립

### 추적성 깨짐

**문제**: 추적성 링크가 끊어짐

**해결**:
1. Audit Log로 변경 이력 확인
2. Relation 속성 무결성 검증
3. 자동 복구 스크립트 실행

## 다음 단계

- [CAPA Tracker](capa-tracker.md)로 시정예방조치 관리 방법 학습
- [Risk Register](risk-register.md)로 위험 관리 방법 학습
- [Quality Validation](quality-validation.md)으로 데이터 무결성 검증 방법 학습
