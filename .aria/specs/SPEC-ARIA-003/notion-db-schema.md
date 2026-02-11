# Notion DB Schema Definition

ARIA Phase 3 RA/QA Specialization을 위한 Notion Database 스키마 정의입니다.

## Overview

3개의 Notion Database를 생성하여 RA/QA 워크플로우를 지원합니다:

1. **Risk Register** - 위험 관리 추적
2. **CAPA Tracker** - 수정/예방 조치 추적
3. **Document Registry** - 문서 관리 및 추적성

---

## 1. Risk Register Database

### Purpose

ISO 14971 위험 관리 프로세스를 지원하는 위험 등록부입니다.

### Fields

#### Basic Information (기본 정보)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| Risk ID | Auto-increment | 고유 위험 식별자 | RISK-001, RISK-002 |
| Hazard | Title | 위험 요소 | Electrical shock |
| Harm | Title | 위해 결과 | Patient injury, Death |
| Causes | Text | 원인 설명 | Power supply failure |

#### Initial Risk Assessment (초기 위험 평가)

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Initial Severity | Select | Negligible, Minor, Moderate, Major, Catastrophic | 심각성 |
| Initial Probability | Select | Remote, Low, Medium, High, Frequent | 발생 확률 |
| Initial Risk Index | Formula | Severity × Probability | 위험 지수 |

#### Risk Control (위험 경감)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| Control Measures | Text | 경감 조치 | Backup battery |
| Responsible Person | Person | 책임자 | John Doe |
| Target Date | Date | 목표일 | 2026-03-01 |

#### Residual Risk Assessment (잔여 위험 평가)

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Residual Severity | Select | Negligible, Minor, Moderate, Major, Catastrophic | 잔여 심각성 |
| Residual Probability | Select | Remote, Low, Medium, High, Frequent | 잔여 확률 |
| Residual Risk Index | Formula | Residual Severity × Residual Probability | 잔여 위험 지수 |
| Risk Acceptability | Select | Acceptable, ALARP, Unacceptable | 위험 수용성 |

#### Tracking (추적)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| Risk Evaluation Date | Date | 평가 일자 | 2026-02-09 |
| Review Date | Date | 재검토 일자 | 2026-08-09 |
| Related CAPA ID | Relation | CAPA Tracker와 연동 | CAPA-001 |
| Related Document ID | Relation | Document Registry와 연동 | DOC-001 |

### Risk Index Formula

```
Risk Index = Severity × Probability

Severity Values:
- Negligible = 1
- Minor = 2
- Moderate = 3
- Major = 4
- Catastrophic = 5

Probability Values:
- Remote = 1
- Low = 2
- Medium = 3
- High = 4
- Frequent = 5

Risk Acceptability:
- 1-4: Acceptable
- 5-9: ALARP (As Low As Reasonably Practicable)
- 10-25: Unacceptable
```

---

## 2. CAPA Tracker Database

### Purpose

ISO 13485 Section 8.5.2, 8.5.3, 8.5.4, 10.2 CAPA 프로세스를 추적합니다.

### Fields

#### Basic Information (기본 정보)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| CAPA ID | Auto-increment | 고유 CAPA 식별자 | CAPA-001, CAPA-002 |
| Issue Date | Date | 발생 일자 | 2026-02-09 |
| Problem Description | Text | 문제 설명 | Sensor drift detected |
| Nonconformance Type | Select | Product, Process, Documentation, Supplier | 불일치 유형 |
| Severity | Select | Critical, Major, Minor | 심각도 |

#### Root Cause Analysis (근본 원인 분석)

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Root Cause | Text | 근본 원인 | Calibration SOP missing |
| Root Cause Method | Select | 5 Whys, Fishbone, FMEA | 분석 방법 |

#### Actions (조치)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| Corrective Action | Text | 수정 조치 | Create calibration SOP |
| Preventive Action | Text | 예방 조치 | Training program |
| Responsible Person | Person | 책임자 | Jane Smith |
| Target Date | Date | 목표일 | 2026-03-15 |
| Completion Date | Date | 완료일 | 2026-03-10 |

#### Verification (검증)

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Effectiveness Check | Select | Pending, In Progress, Complete, Failed | 효성 검증 |
| Status | Select | Open, In Progress, Closed | 상태 |

#### Relations (연동)

| Field Name | Type | Description |
|------------|------|-------------|
| Related Risk ID | Relation | Risk Register와 연동 |
| Related Document ID | Relation | Document Registry와 연동 |

---

## 3. Document Registry Database

### Purpose

설계 통제, 품질 관리, 규제 준비 문서를 추적합니다.

### Fields

#### Basic Information (기본 정보)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| Document ID | Auto-increment | 고유 문서 식별자 | DOC-001, DOC-002 |
| Document Name | Title | 문서 이름 | DHF-001: Infusion Pump |
| Document Type | Select | DHF, DMR, DHR, Specification, SOP, Report | 문서 유형 |
| Version | Number | 버전 번호 | 1.0, 1.1, 2.0 |

#### Status (상태)

| Field Name | Type | Options | Description |
|------------|------|---------|-------------|
| Status | Select | Draft, Review, Approved, Released, Superseded | 상태 |
| Effective Date | Date | 발효일 | 2026-02-09 |
| Review Date | Date | 재검토 일자 | 2027-02-09 |

#### Ownership (소유권)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| Owner | Person | 문서 소유자 | John Doe |
| Approver | Person | 승인자 | Jane Smith |

#### Relations (연동)

| Field Name | Type | Description |
|------------|------|-------------|
| Related Design Input | Relation | 설계 입력 요구사항 |
| Related Design Output | Relation | 설계 출력 명세서 |
| Related CAPA ID | Relation | CAPA Tracker와 연동 |
| Related Risk ID | Relation | Risk Register와 연동 |

#### Control (통제)

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| Confidentiality | Select | Public, Internal, Confidential | 기밀성 |
| Retention Period | Number | 보관 기간 (년) | 10 |

---

## Database Relations

### Risk Register Relations

```
Risk Register
    ↓ (Related CAPA ID)
CAPA Tracker
    ↓ (Related Document ID)
Document Registry
```

### Document Registry Relations

```
Document Registry
    ↓ (Related Design Input)
Document Registry (Design Input)
    ↓ (Related Design Output)
Document Registry (Design Output)
    ↓ (Related Verification)
Document Registry (Test Result)
    ↓ (Related Validation)
Document Registry (Validation Report)
```

### CAPA Tracker Relations

```
CAPA Tracker
    ↓ (Related Risk ID)
Risk Register
    ↓ (Related Document ID)
Document Registry (SOP, Report)
```

---

## MCP Integration

### API Operations

#### Page Creation

```javascript
// Risk Register Page Creation
const riskPage = await notion.pages.create({
  parent: { database_id: RISK_REGISTER_DB_ID },
  properties: {
    "Risk ID": { title: [{ text: { content: "RISK-001" } }] },
    "Hazard": { select: { name: "Electrical shock" } },
    "Initial Severity": { select: { name: "Major" } },
    "Initial Probability": { select: { name: "Low" } },
    // ... other properties
  }
});
```

#### Relation Creation

```javascript
// CAPA-Risk Relation
const capaPage = await notion.pages.create({
  parent: { database_id: CAPA_TRACKER_DB_ID },
  properties: {
    "Related Risk ID": { relation: [{ id: RISK_PAGE_ID }] },
    // ... other properties
  }
});
```

#### Automated Calculations

```javascript
// Risk Index Calculation
const severityMap = { "Negligible": 1, "Minor": 2, "Moderate": 3, "Major": 4, "Catastrophic": 5 };
const probabilityMap = { "Remote": 1, "Low": 2, "Medium": 3, "High": 4, "Frequent": 5 };

const riskIndex = severityMap[severity] * probabilityMap[probability];
```

### Automation Triggers

1. **Risk Creation**
   - New risk → Assign Risk ID
   - Calculate Initial Risk Index
   - Set Target Date (30 days)

2. **CAPA Creation**
   - New CAPA → Assign CAPA ID
   - Set Target Date (30-90 days)
   - Create Relations

3. **Document Creation**
   - New document → Assign Document ID
   - Set Review Date (annual)
   - Create Relations

4. **Due Date Alerts**
   - Target Date approaching → Send notification
   - Overdue → Escalate

---

## Implementation Steps

### Step 1: Database Creation

1. Create Risk Register database in Notion
2. Create CAPA Tracker database in Notion
3. Create Document Registry database in Notion
4. Configure all properties
5. Set up Relations

### Step 2: MCP Connection

1. Install Notion MCP server
2. Configure authentication
3. Test database connection
4. Verify API access

### Step 3: Automation Setup

1. Create page creation templates
2. Implement automated calculations
3. Set up relation linking
4. Configure due date alerts

### Step 4: Integration Testing

1. Test Risk Register → CAPA Tracker link
2. Test CAPA Tracker → Document Registry link
3. Test automated calculations
4. Verify data integrity

---

## Database Properties Summary

### Risk Register (14 fields)

| # | Field | Type | Required |
|---|-------|------|----------|
| 1 | Risk ID | Auto | Yes |
| 2 | Hazard | Title | Yes |
| 3 | Harm | Title | Yes |
| 4 | Causes | Text | Yes |
| 5 | Initial Severity | Select | Yes |
| 6 | Initial Probability | Select | Yes |
| 7 | Initial Risk Index | Formula | Auto |
| 8 | Control Measures | Text | Yes |
| 9 | Responsible Person | Person | Yes |
| 10 | Target Date | Date | Yes |
| 11 | Residual Severity | Select | Yes |
| 12 | Residual Probability | Select | Yes |
| 13 | Residual Risk Index | Formula | Auto |
| 14 | Risk Acceptability | Select | Auto |

### CAPA Tracker (12 fields)

| # | Field | Type | Required |
|---|-------|------|----------|
| 1 | CAPA ID | Auto | Yes |
| 2 | Issue Date | Date | Yes |
| 3 | Problem Description | Text | Yes |
| 4 | Nonconformance Type | Select | Yes |
| 5 | Severity | Select | Yes |
| 6 | Root Cause | Text | Yes |
| 7 | Root Cause Method | Select | Yes |
| 8 | Corrective Action | Text | Yes |
| 9 | Preventive Action | Text | Yes |
| 10 | Responsible Person | Person | Yes |
| 11 | Target Date | Date | Yes |
| 12 | Completion Date | Date | No |
| 13 | Effectiveness Check | Select | Yes |
| 14 | Status | Select | Yes |
| 15 | Related Risk ID | Relation | No |
| 16 | Related Document ID | Relation | No |

### Document Registry (11 fields)

| # | Field | Type | Required |
|---|-------|------|----------|
| 1 | Document ID | Auto | Yes |
| 2 | Document Name | Title | Yes |
| 3 | Document Type | Select | Yes |
| 4 | Version | Number | Yes |
| 5 | Status | Select | Yes |
| 6 | Effective Date | Date | Yes |
| 7 | Review Date | Date | Yes |
| 8 | Owner | Person | Yes |
| 9 | Approver | Person | No |
| 10 | Related Design Input | Relation | No |
| 11 | Related Design Output | Relation | No |
| 12 | Related CAPA ID | Relation | No |
| 13 | Related Risk ID | Relation | No |
| 14 | Confidentiality | Select | Yes |
| 15 | Retention Period | Number | Yes |

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Related**: SPEC-ARIA-003
