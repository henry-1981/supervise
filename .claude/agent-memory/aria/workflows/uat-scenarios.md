# ARIA Workflows - User Acceptance Test Scenarios

Document Version: 1.0
Created: 2026-02-09
Status: Ready for Testing

## Overview

This document contains User Acceptance Test (UAT) scenarios for ARIA workflow implementations (Milestone 4: Complete Workflows).

### Test Environment

- **Claude Code Version**: v2.1.32+
- **ARIA Plugin Version**: 1.0.0
- **Test Data**: Synthetic device and audit data
- **Test Users**: RA/QA professionals, Clinical evaluation specialists, Quality auditors

---

## Clinical Evaluation Workflow (MEDDEV 2.7.1 rev 4)

### UAT-CE-001: Complete CER Workflow Execution

**Priority**: P0 (Critical)
**Type**: End-to-End
**Estimated Time**: 45 minutes

**Preconditions**:
- ARIA plugin installed and enabled
- Test device: "CardioStent X2" (Class IIb coronary stent)
- PubMed and Google Scholar access available

**Test Steps**:

1. **Initiate Clinical Evaluation Workflow**
   - Command: `/aria clinical-evaluation start`
   - Expected: Workflow ID generated (WF-CE-2025-001)
   - Expected: Stage 1 (Scope Definition) starts

2. **Stage 1: Scope Definition**
   - Provide device identification:
     - Device name: "CardioStent X2"
     - Model: "CS-X2-40"
     - Manufacturer: "MedTech Corp"
     - Intended use: "Treatment of coronary artery disease"
     - Device class: "IIb"
   - Define clinical objectives:
     - Safety: "No stent thrombosis within 12 months"
     - Performance: "Target vessel revascularization < 10%"
   - Expected: Stage 1 completes, progress = 25%

3. **Stage 2: Literature Search**
   - Configure search strategy:
     - Databases: PubMed, Google Scholar, Cochrane
     - Keywords: "coronary stent", "drug-eluting stent", "XIENCE"
     - Publication date range: "2015-01 to 2025-01"
   - Execute literature search
   - Expected: 50+ studies identified
   - Expected: Literature summary generated
   - Expected: Gap analysis performed
   - Expected: Stage 2 completes, progress = 50%

4. **Stage 3: Data Analysis**
   - Identify predicate device: "XIENCE Sierra"
   - Perform equivalence assessment:
     - Technical similarity: High
     - Clinical similarity: High
   - Analyze clinical data from 10 included studies
   - Perform benefit-risk analysis:
     - Clinical benefits: "Reduced restenosis"
     - Risks: "Stent thrombosis"
     - Overall assessment: "Favorable"
   - Expected: Stage 3 completes, progress = 75%

5. **Stage 4: CER Generation**
   - Generate Clinical Evaluation Report
   - Expected: CER document generated with all required sections
   - Expected: PMCF requirements identified (if applicable)
   - Expected: Stage 4 completes, progress = 100%

**Acceptance Criteria**:
- [ ] All 4 stages completed successfully
- [ ] CER document generated per MEDDEV 2.7.1 rev 4 Annex XV
- [ ] Progress indicators accurate at each stage
- [ ] Context preserved across all stages
- [ ] Workflow state persisted and recoverable

**Test Data**:
```
Device: CardioStent X2
Model: CS-X2-40
Class: IIb
Predicate: XIENCE Sierra
Search Results: 52 studies
Included Studies: 10 studies
PMCF Required: No
```

---

### UAT-CE-002: Workflow Interruption and Resumption

**Priority**: P1 (High)
**Type**: Resilience
**Estimated Time**: 20 minutes

**Preconditions**:
- Clinical evaluation workflow in progress
- At Stage 2 (Literature Search)

**Test Steps**:

1. **Interrupt Workflow**
   - Simulate session interruption (close Claude Code)
   - Wait 5 minutes

2. **Resume Workflow**
   - Command: `/aria clinical-evaluation resume WF-CE-2025-001`
   - Expected: Workflow resumes at Stage 2
   - Expected: All collected data preserved
   - Expected: Progress indicator correct (50%)

3. **Complete Workflow**
   - Continue from Stage 2 through Stage 4
   - Expected: Workflow completes successfully

**Acceptance Criteria**:
- [ ] Workflow state persisted across interruption
- [ ] All collected data preserved
- [ ] Resume functionality works correctly
- [ ] No data loss or corruption

---

### UAT-CE-003: PMCF Requirement Flagging

**Priority**: P1 (High)
**Type**: Functional
**Estimated Time**: 30 minutes

**Preconditions**:
- Test device: "NeuroLink Brain Interface" (Class III novel device)

**Test Steps**:

1. **Execute Clinical Evaluation Workflow**
   - Stages 1-3 complete normally

2. **Stage 3: Data Analysis**
   - Literature search identifies insufficient clinical data
   - Gap analysis reveals:
     - No predicate device identified
     - Limited clinical data (< 3 studies)
     - Novel technology with unknown safety profile

3. **Verify PMCF Flagging**
   - Expected: System flags PMCF requirements
   - Expected: Flag severity: "Critical"
   - Expected: PMCF activities suggested

4. **Generate CER**
   - Expected: CER includes PMCF section
   - Expected: PMCF plan template provided

**Acceptance Criteria**:
- [ ] PMCF requirements correctly identified
- [ ] Flag created with appropriate severity
- [ ] CER includes PMCF section
- [ ] PMCF plan template available

---

## Internal Audit Workflow (ISO 13485)

### UAT-IA-001: Complete Audit Workflow Execution

**Priority**: P0 (Critical)
**Type**: End-to-End
**Estimated Time**: 60 minutes

**Preconditions**:
- ARIA plugin installed and enabled
- Test audit: Internal audit of "R&D Department"
- Previous audit findings available

**Test Steps**:

1. **Initiate Internal Audit Workflow**
   - Command: `/aria internal-audit start`
   - Expected: Workflow ID generated (WF-IA-2025-001)
   - Expected: Stage 1 (Audit Planning) starts

2. **Stage 1: Audit Planning**
   - Define audit scope:
     - Department: "R&D Department"
     - ISO 13485 clauses: 7.1 (Planning), 7.3 (Design and Development), 8.3 (Design Transfer)
     - Duration: 2 days
   - Previous findings:
     - Repeat finding: "Design validation incomplete" (3 times)
     - Major finding: "Design reviews not documented"
   - Expected: Audit agenda generated
   - Expected: High-risk areas prioritized
   - Expected: Checklists prepared
   - Expected: Stage 1 completes, progress = 25%

3. **Stage 2: Audit Execution**
   - Execute audit per agenda
   - Document findings:
     - Critical: None
     - Major: "Design verification not performed for CS-X2-40"
     - Minor: "Design history file incomplete"
     - Observation: "Could improve design review meeting structure"
   - Expected: All findings documented with evidence
   - Expected: Repeat finding detection active
   - Expected: Stage 2 completes, progress = 50%

4. **Stage 3: CAPA Planning**
   - Root cause analysis for major finding:
     - Method: 5 Whys
     - Root cause: "Insufficient design verification resources"
   - Develop corrective actions:
     - Immediate: "Assign additional verification engineer"
     - Deadline: 2025-03-01
   - Develop preventive actions:
     - Systemic: "Update design verification procedure"
     - Document updates: "SOP-7.3-005 Design Verification"
   - Expected: CAPA plan created
   - Expected: Root cause documented
   - Expected: Stage 3 completes, progress = 75%

5. **Stage 4: Verification**
   - Monitor CAPA implementation
   - Verify effectiveness:
     - Method: "Review verification records for next 3 designs"
     - Success criteria: "100% verification completion"
   - Perform trend analysis:
     - Design findings: "Decreasing trend"
     - CAPA effectiveness: "98% on-time completion"
   - Expected: Effectiveness report generated
   - Expected: Continuous improvement recommendations provided
   - Expected: Stage 4 completes, progress = 100%

**Acceptance Criteria**:
- [ ] All 4 stages completed successfully
- [ ] Audit agenda prioritizes high-risk areas
- [ ] Repeat findings detected and flagged
- [ ] Root cause analysis performed using 5 Whys
- [ ] CAPA plan includes corrective and preventive actions
- [ ] Effectiveness verification defined
- [ ] Trend analysis performed

**Test Data**:
```
Department: R&D Department
Clauses: 7.1, 7.3, 8.3
Duration: 2 days
Critical findings: 0
Major findings: 1
Minor findings: 1
Observations: 1
Repeat findings detected: Yes (Design validation)
CAPA effectiveness: 98%
```

---

### UAT-IA-002: Repeat Finding Detection

**Priority**: P1 (High)
**Type**: Functional
**Estimated Time**: 30 minutes

**Preconditions**:
- Three previous internal audits with documented findings
- Finding history available

**Test Steps**:

1. **Stage 1: Audit Planning**
   - System analyzes previous findings
   - Identifies repeat findings:
     - "Design validation incomplete" (3 occurrences)
     - "Training records missing" (2 occurrences)

2. **Verify Repeat Finding Flags**
   - Expected: Repeat findings flagged in agenda
   - Expected: Priority increased to "HIGH"
   - Expected: Justification includes repeat count

3. **Stage 2: Audit Execution**
   - Focus on repeat finding areas
   - Document if issue persists

4. **Verify Systemic Issue Flagging**
   - Expected: If repeat finding continues, flag as "systemic"
   - Expected: Recommend process review

**Acceptance Criteria**:
- [ ] Repeat findings detected from historical data
- [ ] Repeat findings prioritized in agenda
- [ ] Systemic issues flagged when appropriate
- [ ] Recommendations for process improvement provided

---

### UAT-IA-003: Back-Navigation Support

**Priority**: P2 (Medium)
**Type**: Functional
**Estimated Time**: 20 minutes

**Preconditions**:
- Internal audit workflow at Stage 3 (CAPA Planning)

**Test Steps**:

1. **Request Back-Navigation**
   - Command: `/aria internal-audit back-to audit-planning`
   - Expected: Confirmation prompt
   - Expected: Explanation of impact

2. **Confirm Navigation**
   - Confirm navigation to Stage 1
   - Expected: Workflow returns to Stage 1
   - Expected: Stage 2 and 3 data preserved
   - Expected: Progress updated (25%)

3. **Update Previous Stage**
   - Modify audit scope
   - Expected: Data preserved
   - Expected: Can continue forward from updated stage

**Acceptance Criteria**:
- [ ] Back-navigation supported between stages
- [ ] Data preservation during navigation
- [ ] Progress recalculated correctly
- [ ] History tracks navigation events

---

## Post-Market Surveillance Workflow (EU MDR Article 83-85)

### UAT-PMS-001: Complete PMS Workflow Execution

**Priority**: P0 (Critical)
**Type**: End-to-End
**Estimated Time**: 60 minutes

**Preconditions**:
- ARIA plugin installed and enabled
- Test device: "CardioStent X2" with 12 months of PMS data
- Synthetic PMS data available

**Test Steps**:

1. **Initiate PMS Workflow**
   - Command: `/aria pms start`
   - Expected: Workflow ID generated (WF-PMS-2025-001)
   - Expected: Stage 1 (Data Collection) starts

2. **Stage 1: Data Collection**
   - Configure PMS data sources:
     - Complaint handling system
     - Adverse event reporting
     - Field service reports
     - Literature monitoring
   - Collect data for period: "2024-01 to 2024-12"
   - Expected: 500+ PMS records collected
   - Expected: Data validated and aggregated
   - Expected: Stage 1 completes, progress = 25%

3. **Stage 2: Trend Analysis**
   - Perform statistical analysis:
     - Complaint rate: 15.2 per 1000 devices
     - Baseline: 12.5 per 1000 devices
     - Change: +21.6% (statistically significant, p < 0.05)
   - Analyze lot variation:
     - Lot CS-X2-40-Lot123: 28 complaints (expected range: 12-18)
     - Outside expected range: Yes
   - Analyze geographical clustering:
     - Region: "Germany" - 3.2x higher complaint rate
   - Expected: Significant trends flagged
   - Expected: Lot cluster identified
   - Expected: Geographical cluster detected
   - Expected: Stage 2 completes, progress = 50%

4. **Stage 3: Reporting**
   - Compile PSUR data:
     - Period: "2024-01 to 2024-12"
     - Units sold: 10,000
     - Units in use: 8,500
     - Serious incidents: 12
     - Non-serious incidents: 138
   - Generate PSUR per Annex XIII
   - Expected: PSUR document generated
   - Expected: All required sections included
   - Expected: Trend analysis summary included
   - Expected: Stage 3 completes, progress = 75%

5. **Stage 4: FSCA Trigger** (Not triggered - no safety issues)
   - Verify no safety issues detected
   - Expected: Workflow completes without FSCA
   - Expected: Progress = 100%

**Acceptance Criteria**:
- [ ] All 4 stages completed successfully
- [ ] PMS data collected from multiple sources
- [ ] Statistical trend analysis performed
- [ ] Significant trends correctly flagged
- [ ] Lot clustering detected
- [ ] Geographical clustering detected
- [ ] PSUR generated per Annex XIII
- [ ] Timeline compliance verified

**Test Data**:
```
Device: CardioStent X2
PMS Period: 2024-01 to 2024-12
Units sold: 10,000
Units in use: 8,500
Total PMS records: 512
Serious incidents: 12
Non-serious incidents: 138
Complaint rate: 15.2/1000 (baseline: 12.5/1000)
Lot cluster: CS-X2-40-Lot123
Geographical cluster: Germany
PSUR generated: Yes
FSCA required: No
```

---

### UAT-PMS-002: FSCA Trigger Workflow

**Priority**: P0 (Critical)
**Type**: Functional
**Estimated Time**: 40 minutes

**Preconditions**:
- PMS workflow at Stage 2 (Trend Analysis)
- Serious adverse event detected

**Test Steps**:

1. **Stage 2: Trend Analysis**
   - Detect safety issue:
     - 3 patient deaths reported
     - Device: "CardioStent X2"
     - Lot: "CS-X2-40-Lot456"
     - Timeframe: "Last 30 days"
   - Expected: Safety issue flagged immediately
   - Expected: Flag severity: "Critical"

2. **Trigger FSCA Assessment**
   - Expected: Stage 4 (FSCA Trigger) activates
   - Expected: Timeline alert: "Within 24 hours"

3. **FSCA Assessment**
   - Risk assessment:
     - Hazard: "Stent thrombosis"
     - Harm: "Death, myocardial infarction"
     - Probability: "High"
     - Severity: "Serious"
     - Risk level: "Unacceptable"
   - Regulatory assessment:
     - Reportable to Competent Authority: Yes
     - Deadline: "Within 10 days"
     - Reportable to Notified Body: Yes
     - Deadline: "Per NB agreement (5 days)"
   - FSCA decision:
     - FSCA required: Yes
     - FSCA type: "Field Safety Notice"
     - Scope: "International"
     - Affected lots: "CS-X2-40-Lot456 and related lots"

4. **FSCA Plan Generation**
   - Generate FSCA plan:
     - Immediate actions: "Halt distribution of affected lots"
     - Communications plan: "Field Safety Notice distribution"
     - Regulatory notifications: "Competent Authority, NB, other NBs"
   - Expected: FSCA plan generated
   - Expected: Timeline compliance tracking enabled
   - Expected: Stage 4 completes, progress = 100%

**Acceptance Criteria**:
- [ ] Safety issue detected and flagged immediately
- [ ] FSCA assessment triggered automatically
- [ ] Risk assessment performed
- [ ] Regulatory reporting requirements identified
- [ ] FSCA decision documented
- [ ] FSCA plan generated
- [ ] Timeline compliance tracking enabled
- [ ] Regulatory notification deadlines tracked

---

### UAT-PMS-003: Timeline Compliance Tracking

**Priority**: P1 (High)
**Type**: Functional
**Estimated Time**: 30 minutes

**Preconditions**:
- Serious incident reported
- FSCA workflow triggered

**Test Steps**:

1. **Report Serious Incident**
   - Incident: Patient death during procedure
   - Device involvement: Confirmed
   - Reportable: Yes

2. **Verify Timeline Tracking**
   - Expected: Timeline dashboard displayed
   - Expected: Deadlines tracked:
     - Competent Authority: "10 days from incident awareness"
     - Notified Body: "5 days from incident awareness"
     - Other NBs: "As required"
   - Expected: Countdown timer active

3. **Simulate Timeline Progression**
   - Day 3: Initial investigation complete
   - Day 5: Report to Notified Body submitted
   - Day 9: Report to Competent Authority submitted
   - Expected: Timeline updates as actions complete
   - Expected: Compliance status: "On track"

4. **Test Overdue Scenario**
   - Simulate delay beyond deadline
   - Expected: Warning alert
   - Expected: Consequence displayed
   - Expected: Escalation recommended

**Acceptance Criteria**:
- [ ] Timeline requirements correctly identified per EU MDR
- [ ] Deadline countdown functional
- [ ] Compliance status updates correctly
- [ ] Overdue warnings generated
- [ ] Escalation recommendations provided

---

## Cross-Workflow Scenarios

### UAT-CW-001: Multi-Workflow Execution

**Priority**: P2 (Medium)
**Type**: Integration
**Estimated Time**: 90 minutes

**Preconditions**:
- Multiple workflows to execute

**Test Steps**:

1. **Execute Clinical Evaluation Workflow**
   - Device: "CardioStent X2"
   - Expected: CER generated

2. **Execute Internal Audit Workflow**
   - Scope: "Clinical evaluation process"
   - Expected: Audit findings documented

3. **Execute PMS Workflow**
   - Device: "CardioStent X2"
   - Expected: PSUR generated

4. **Verify Data Sharing**
   - Expected: Device identification consistent across workflows
   - Expected: Regulatory requirements shared
   - Expected: Findings from audit inform PMS data collection

**Acceptance Criteria**:
- [ ] Multiple workflows can execute independently
- [ ] Data consistency maintained across workflows
- [ ] Context preserved within each workflow
- [ ] No interference between concurrent workflows

---

### UAT-CW-002: Workflow State Persistence

**Priority**: P1 (High)
**Type**: Resilience
**Estimated Time**: 60 minutes

**Preconditions**:
- Multiple workflows in various states

**Test Steps**:

1. **Create Workflows**
   - Start Clinical Evaluation: Complete Stage 1
   - Start Internal Audit: Complete Stages 1-2
   - Start PMS: Complete Stage 1

2. **Verify State Persistence**
   - Close Claude Code
   - Wait 10 minutes
   - Reopen Claude Code

3. **List Active Workflows**
   - Command: `/aria workflow list`
   - Expected: All 3 workflows listed
   - Expected: Correct stages displayed
   - Expected: Progress indicators accurate

4. **Resume Each Workflow**
   - Resume Clinical Evaluation: Expected at Stage 2
   - Resume Internal Audit: Expected at Stage 3
   - Resume PMS: Expected at Stage 2
   - Expected: All data preserved

**Acceptance Criteria**:
- [ ] Workflow states persist across sessions
- [ ] Multiple workflows managed simultaneously
- [ ] Resume functionality works for all workflows
- [ ] No data corruption or loss

---

## Performance Scenarios

### UAT-PERF-001: Large Dataset Processing

**Priority**: P2 (Medium)
**Type**: Performance
**Estimated Time**: 45 minutes

**Preconditions**:
- Large PMS dataset (10,000+ records)

**Test Steps**:

1. **Load Large Dataset**
   - PMS records: 10,000
   - Time period: 3 years
   - Device models: 15

2. **Execute Trend Analysis**
   - Expected: Analysis completes within 5 minutes
   - Expected: All trends identified
   - Expected: Statistical tests performed correctly

3. **Verify Results**
   - Expected: Accurate trend detection
   - Expected: No performance degradation
   - Expected: Memory usage acceptable

**Acceptance Criteria**:
- [ ] Large datasets processed within acceptable time
- [ ] No performance degradation
- [ ] Accurate results maintained

---

## Test Summary Matrix

| Test ID | Scenario | Priority | Type | Status | Notes |
|---------|----------|----------|------|--------|-------|
| UAT-CE-001 | Complete CER Workflow | P0 | End-to-End | Ready | |
| UAT-CE-002 | Workflow Interruption | P1 | Resilience | Ready | |
| UAT-CE-003 | PMCF Flagging | P1 | Functional | Ready | |
| UAT-IA-001 | Complete Audit Workflow | P0 | End-to-End | Ready | |
| UAT-IA-002 | Repeat Finding Detection | P1 | Functional | Ready | |
| UAT-IA-003 | Back-Navigation | P2 | Functional | Ready | |
| UAT-PMS-001 | Complete PMS Workflow | P0 | End-to-End | Ready | |
| UAT-PMS-002 | FSCA Trigger | P0 | Functional | Ready | |
| UAT-PMS-003 | Timeline Compliance | P1 | Functional | Ready | |
| UAT-CW-001 | Multi-Workflow Execution | P2 | Integration | Ready | |
| UAT-CW-002 | State Persistence | P1 | Resilience | Ready | |
| UAT-PERF-001 | Large Dataset | P2 | Performance | Ready | |

---

## Test Execution Checklist

### Pre-Test Setup
- [ ] ARIA plugin installed
- [ ] Claude Code v2.1.32+ active
- [ ] Test data prepared
- [ ] Test environment configured
- [ ] Test users available

### Test Execution
- [ ] Execute P0 tests first
- [ ] Execute P1 tests second
- [ ] Execute P2 tests last
- [ ] Document all deviations
- [ ] Capture screenshots
- [ ] Record performance metrics

### Post-Test
- [ ] Collect test results
- [ ] Document defects
- [ ] Generate test report
- [ ] Review acceptance criteria
- [ ] Sign-off on successful tests
