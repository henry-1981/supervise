# Google Sheets Integration Module

## Overview

Google Sheets API integration for regulatory data management in ARIA Phase 4.

## MCP Tool Interfaces

### 1. Create Spreadsheet

```typescript
interface SheetsCreateParams {
  title: string;
  sheets?: Array<{
    title: string;
    rowCount: number;
    columnCount: number;
  }>;
}

interface SheetsResponse {
  spreadsheetId: string;
  title: string;
}
```

**Tool**: `mcp__google-workspace__sheets_create`

### 2. Append Rows

```typescript
interface SheetsAppendParams {
  spreadsheetId: string;
  sheetName: string;
  rows: Array<Record<string, string | number | boolean>>;
}
```

**Tool**: `mcp__google-workspace__sheets_append`

### 3. Query Data

```typescript
interface SheetsQueryParams {
  spreadsheetId: string;
  sheetName: string;
  range?: string;
  filter?: Record<string, unknown>;
}
```

**Tool**: `mcp__google-workspace__sheets_query`

## Regulatory Spreadsheet Templates

### 1. Risk Register

**Template ID**: `risk-register`

```typescript
interface RiskRegisterData {
  riskId: string;
  riskDescription: string;
  riskCategory: 'Clinical' | 'Technical' | 'Regulatory';
  hazard: string;
  harm: string;
  causes: string;
  initialSeverity: number; // 1-3
  initialProbability: number; // 1-3
  initialRPN: number;
  mitigationStrategy: string;
  residualSeverity: number; // 1-3
  residualProbability: number; // 1-3
  residualRPN: number;
  acceptability: 'Acceptable' | 'Not Acceptable';
  mitigationOwner: string;
  targetDate: Date;
  status: 'Open' | 'Mitigated' | 'Closed';
}

async function createRiskRegister(): Promise<string> {
  const spreadsheet = await mcp__google-workspace__sheets_create({
    title: `Risk Register - ${new Date().toISOString()}`,
    sheets: [{
      title: 'Risks',
      rowCount: 1000,
      columnCount: 15
    }]
  });

  // Add header row
  await mcp__google-workspace__sheets_append({
    spreadsheetId: spreadsheet.spreadsheetId,
    sheetName: 'Risks',
    rows: [{
      risk_id: 'Risk ID',
      risk_description: 'Risk Description',
      risk_category: 'Category',
      hazard: 'Hazard',
      harm: 'Harm',
      causes: 'Causes',
      initial_severity: 'Initial Severity',
      initial_probability: 'Initial Probability',
      initial_rpn: 'Initial RPN',
      mitigation_strategy: 'Mitigation Strategy',
      residual_severity: 'Residual Severity',
      residual_probability: 'Residual Probability',
      residual_rpn: 'Residual RPN',
      acceptability: 'Acceptability',
      mitigation_owner: 'Owner',
      target_date: 'Target Date',
      status: 'Status'
    }]
  });

  return spreadsheet.spreadsheetId;
}

async function addRisk(
  spreadsheetId: string,
  risk: RiskRegisterData
): Promise<void> {
  await mcp__google-workspace__sheets_append({
    spreadsheetId,
    sheetName: 'Risks',
    rows: [{
      risk_id: risk.riskId,
      risk_description: risk.riskDescription,
      risk_category: risk.riskCategory,
      hazard: risk.hazard,
      harm: risk.harm,
      causes: risk.causes,
      initial_severity: risk.initialSeverity,
      initial_probability: risk.initialProbability,
      initial_rpn: risk.initialRPN,
      mitigation_strategy: risk.mitigationStrategy,
      residual_severity: risk.residualSeverity,
      residual_probability: risk.residualProbability,
      residual_rpn: risk.residualRPN,
      acceptability: risk.acceptability,
      mitigation_owner: risk.mitigationOwner,
      target_date: risk.targetDate.toISOString(),
      status: risk.status
    }]
  });
}
```

### 2. CAPA Tracker

**Template ID**: `capa-tracker`

```typescript
interface CAPATrackerData {
  capaId: string;
  source: string;
  sourceDate: Date;
  problemStatement: string;
  rootCause: string;
  correctionAction: string;
  preventionAction: string;
  responsiblePerson: string;
  targetDate: Date;
  actualCompletionDate?: Date;
  effectivenessCheck: string;
  effectivenessResult: 'Effective' | 'Not Effective' | 'Pending';
  status: 'Open' | 'In Progress' | 'Closed';
}

async function createCAPATracker(): Promise<string> {
  const spreadsheet = await mcp__google-workspace__sheets_create({
    title: `CAPA Tracker - ${new Date().toISOString()}`,
    sheets: [{
      title: 'CAPA',
      rowCount: 1000,
      columnCount: 12
    }]
  });

  await mcp__google-workspace__sheets_append({
    spreadsheetId: spreadsheet.spreadsheetId,
    sheetName: 'CAPA',
    rows: [{
      capa_id: 'CAPA ID',
      source: 'Source',
      source_date: 'Source Date',
      problem_statement: 'Problem Statement',
      root_cause: 'Root Cause',
      correction_action: 'Correction Action',
      prevention_action: 'Prevention Action',
      responsible_person: 'Responsible Person',
      target_date: 'Target Date',
      actual_completion_date: 'Actual Completion',
      effectiveness_check: 'Effectiveness Check',
      effectiveness_result: 'Effectiveness Result',
      status: 'Status'
    }]
  });

  return spreadsheet.spreadsheetId;
}
```

### 3. Submission Tracker

**Template ID**: `submission-tracker`

```typescript
interface SubmissionTrackerData {
  submissionId: string;
  submissionType: '510(k)' | 'PMA' | 'CE' | 'MFDS';
  targetMarket: string;
  productCode: string;
  submissionDate: Date;
  expectedApprovalDate?: Date;
  actualApprovalDate?: Date;
  status: 'Preparing' | 'Submitted' | 'Under Review' | 'Approved' | 'Rejected';
  reviewer: string;
  submissionNumber: string;
  documentLinks: string;
  notes: string;
}

async function createSubmissionTracker(): Promise<string> {
  const spreadsheet = await mcp__google-workspace__sheets_create({
    title: `Submission Tracker - ${new Date().toISOString()}`,
    sheets: [{
      title: 'Submissions',
      rowCount: 1000,
      columnCount: 12
    }]
  });

  await mcp__google-workspace__sheets_append({
    spreadsheetId: spreadsheet.spreadsheetId,
    sheetName: 'Submissions',
    rows: [{
      submission_id: 'Submission ID',
      submission_type: 'Type',
      target_market: 'Target Market',
      product_code: 'Product Code',
      submission_date: 'Submission Date',
      expected_approval_date: 'Expected Approval',
      actual_approval_date: 'Actual Approval',
      status: 'Status',
      reviewer: 'Reviewer',
      submission_number: 'Submission Number',
      document_links: 'Document Links',
      notes: 'Notes'
    }]
  });

  return spreadsheet.spreadsheetId;
}
```

## Data Validation Rules

### Risk Register Validation

```typescript
interface ValidationRule {
  column: string;
  type: 'list' | 'number' | 'date';
  condition?: string;
  values?: string[];
}

const riskRegisterValidations: ValidationRule[] = [
  {
    column: 'risk_category',
    type: 'list',
    values: ['Clinical', 'Technical', 'Regulatory']
  },
  {
    column: 'initial_severity',
    type: 'number',
    condition: '>=1 && <=3'
  },
  {
    column: 'initial_probability',
    type: 'number',
    condition: '>=1 && <=3'
  },
  {
    column: 'acceptability',
    type: 'list',
    values: ['Acceptable', 'Not Acceptable']
  },
  {
    column: 'status',
    type: 'list',
    values: ['Open', 'Mitigated', 'Closed']
  }
];
```

## Formulas and Calculations

### RPN Calculation

```typescript
// For Risk Register
const rpnFormula = '=ARRAYFORMULA(IF(ROW(A:A)=1, "Initial RPN", IF(A2:A<>"", G2*H2, "")))';
const residualRPNFormula = '=ARRAYFORMULA(IF(ROW(A:A)=1, "Residual RPN", IF(A2:A<>"", L2*M2, "")))';

// Risk Level Classification
const riskLevelFormula = '=ARRAYFORMULA(IF(ROW(A:A)=1, "Risk Level", IF(I2:I<>"", IF(I2:I>=6, "HIGH", IF(I2:I>=3, "MEDIUM", "LOW")), "")))';
```

### Days Until Target Date

```typescript
const daysUntilFormula = '=ARRAYFORMULA(IF(ROW(A:A)=1, "Days Until Target", IF(J2:J<>"", DAYS(J2:A, TODAY()), "")))';

// Conditional formatting (to be applied via API)
const overdueRule = {
  condition: 'LESS_THAN',
  value: '0',
  format: { red: true, bold: true }
};
```

## Data Analysis

### Risk Summary Dashboard

```typescript
interface RiskSummary {
  totalRisks: number;
  openRisks: number;
  mitigatedRisks: number;
  closedRisks: number;
  highRisks: number;
  mediumRisks: number;
  lowRisks: number;
  averageRPN: number;
}

async function getRiskSummary(
  spreadsheetId: string
): Promise<RiskSummary> {
  const risks = await mcp__google-workspace__sheets_query({
    spreadsheetId,
    sheetName: 'Risks'
  });

  const summary: RiskSummary = {
    totalRisks: risks.length,
    openRisks: risks.filter(r => r.status === 'Open').length,
    mitigatedRisks: risks.filter(r => r.status === 'Mitigated').length,
    closedRisks: risks.filter(r => r.status === 'Closed').length,
    highRisks: risks.filter(r => r.initial_rpn >= 6).length,
    mediumRisks: risks.filter(r => r.initial_rpn >= 3 && r.initial_rpn < 6).length,
    lowRisks: risks.filter(r => r.initial_rpn < 3).length,
    averageRPN: risks.reduce((sum, r) => sum + r.initial_rpn, 0) / risks.length
  };

  return summary;
}
```

### CAPA Aging Report

```typescript
interface CAPAAging {
  overdue: number;
  dueThisWeek: number;
  dueThisMonth: number;
  onTrack: number;
}

async function getCAPAAging(
  spreadsheetId: string
): Promise<CAPAAging> {
  const capas = await mcp__google-workspace__sheets_query({
    spreadsheetId,
    sheetName: 'CAPA'
  });

  const today = new Date();
  const weekFromNow = new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000);
  const monthFromNow = new Date(today.getTime() + 30 * 24 * 60 * 60 * 1000);

  const aging: CAPAAging = {
    overdue: capas.filter(c => new Date(c.target_date) < today && c.status !== 'Closed').length,
    dueThisWeek: capas.filter(c => {
      const target = new Date(c.target_date);
      return target >= today && target <= weekFromNow && c.status !== 'Closed';
    }).length,
    dueThisMonth: capas.filter(c => {
      const target = new Date(c.target_date);
      return target > weekFromNow && target <= monthFromNow && c.status !== 'Closed';
    }).length,
    onTrack: capas.filter(c => {
      const target = new Date(c.target_date);
      return target > monthFromNow && c.status !== 'Closed';
    }).length
  };

  return aging;
}
```

## Integration with Notion

### Sync Risk Register to Notion

```typescript
async function syncRiskRegisterToNotion(
  spreadsheetId: string,
  notionDatabaseId: string
): Promise<void> {
  // 1. Read from Sheets
  const risks = await mcp__google-workspace__sheets_query({
    spreadsheetId,
    sheetName: 'Risks'
  });

  // 2. For each risk, update/create Notion page
  for (const risk of risks) {
    await mcp__notion__create-page({
      databaseId: notionDatabaseId,
      properties: {
        'Risk ID': { title: [{ text: { content: risk.risk_id } }] },
        'Risk Description': { rich_text: [{ text: { content: risk.risk_description } }] },
        'Risk Category': { select: { name: risk.risk_category } },
        'Severity': { select: { name: risk.initial_severity.toString() } },
        'Probability': { select: { name: risk.initial_probability.toString() } },
        'RPN Number': { number: risk.initial_rpn },
        'Status': { status: { name: risk.status === 'Closed' ? 'Done' : 'In Progress' } }
      }
    });
  }
}
```

## Error Handling

| Error | Description | Resolution |
|-------|-------------|------------|
| `invalid_spreadsheet_id` | Spreadsheet not found | Verify spreadsheet ID |
| `invalid_sheet_name` | Sheet doesn't exist | Check sheet name spelling |
| `invalid_data_type` | Data type mismatch | Verify data types |
| `row_limit_exceeded` | Sheet row limit exceeded | Create new sheet |
| `unauthorized` | Invalid access token | Refresh OAuth token |

## Testing

### Test Cases

1. **Spreadsheet Creation**: Verify each template
2. **Data Append**: Test row insertion
3. **Data Query**: Test filtering and retrieval
4. **Formulas**: Verify RPN calculations
5. **Validation**: Test data validation rules
6. **Sync Tests**: Test Notion integration
