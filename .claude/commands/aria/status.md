---
name: aria-status
description: >
  ARIA project status dashboard command - Display current status of CAPA Tracker (Open, Overdue, Due < 7 days),
  Risk Register (Unacceptable risks, Review overdue), Submission Tracker (Upcoming, Deadlines),
  Document Registry (Pending, Review overdue), and Google Calendar events (Audits, Deadlines).
  Detects and alerts on risky situations with 3-level warning system (Critical/Warning/Info).
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "2.1.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, status, dashboard, overview, warning-system"
  argument-hint: "[--summary] [--detailed] [--alert-only]"
---

# ARIA Project Status Dashboard Command

## Purpose

Display comprehensive status of all ARIA databases and Google Calendar, detecting risky situations and providing alerts with 3-level warning system (per SPEC-ARIA-004 ER-016, ER-017, S7.2).

## Usage

```
/aria status              # Full dashboard
/aria status --summary    # Summary view
/aria status --detailed   # Detailed view
/aria status --alert-only # Alert items only
```

## Dashboard Components

### 1. CAPA Tracker Status

```markdown
## CAPA Tracker

### Summary
- Total CAPA: 15 items
- Open: 5 items (Attention)
- In Progress: 7 items
- Verified: 2 items
- Closed: 1 item

### Alert Items

**CRITICAL: Overdue (2 items)**
- CAPA-2024-003: Design Validation Failure
  - Due: 2024-01-15 (15 days overdue)
  - Owner: John Doe
  - Action: Immediate review required, schedule adjustment

**CRITICAL: Overdue (1 item)**
- CAPA-2024-008: Supplier Qualification Gap
  - Due: 2024-01-20 (10 days overdue)
  - Owner: Jane Smith
  - Action: Supplier re-qualification in progress

**WARNING: Due within 7 days (3 items)**
- CAPA-2024-012: Risk Assessment Update
  - Due: 2024-02-05 (3 days remaining)
- CAPA-2024-013: Document Revision
  - Due: 2024-02-07 (5 days remaining)
- CAPA-2024-014: Training Completion
  - Due: 2024-02-08 (6 days remaining)

### Notion Page: [CAPA Tracker Dashboard](https://notion.so/capa-dashboard)
```

### 2. Risk Register Status

```markdown
## Risk Register

### Summary
- Total Risks: 42 items
- Acceptable: 35 items
- Unacceptable: 1 item (Risk)
- Review Overdue: 4 items (Attention)

### Alert Items

**CRITICAL: Unacceptable Risk (1 item)**
- RISK-015: Software Failure - Patient Safety Impact
  - Severity: S5 (Critical)
  - Probability: P3 (Moderate)
  - Risk Level: 15 (High)
  - Current Controls: Insufficient
  - Action: Additional controls required immediately, CAPA creation recommended

**WARNING: Review Overdue (4 items)**
- RISK-008: Electrical Safety
  - Due: 2024-01-10 (20 days overdue)
- RISK-012: Software Compatibility
  - Due: 2024-01-15 (15 days overdue)
- RISK-022: Sterile Packaging
  - Due: 2024-01-18 (12 days overdue)
- RISK-028: Labeling Requirements
  - Due: 2024-01-20 (10 days overdue)

### Notion Page: [Risk Register Dashboard](https://notion.so/risk-dashboard)
```

### 3. Submission Tracker Status

```markdown
## Submission Tracker

### Summary
- Submissions in Progress: 3 items
- Planned Submissions: 2 items
- Completed Submissions: 8 items (2024)

### Upcoming Submissions

**CRITICAL: Deadline < 7 days (1 item)**
- SUB-510K-045: [Device Name] 510(k) Submission
  - Target: 2024-02-10 (5 days remaining)
  - Status: Preparation (80% complete)
  - Remaining: Final Review, Pre-submission Meeting
  - Owner: Jane Smith
  - Action: Confirm schedule, complete remaining items

**WARNING: Deadline 7-30 days (2 items)**
- SUB-CE-012: CE Mark Technical Documentation
  - Target: 2024-03-15 (35 days remaining)
  - Status: Early Preparation
- SUB-PMA-003: PMA Submission
  - Target: 2024-04-20 (71 days remaining)
  - Status: Planning

### Notion Page: [Submission Tracker Dashboard](https://notion.so/submission-dashboard)
```

### 4. Document Registry Status

```markdown
## Document Registry

### Summary
- Total Documents: 285 items
- Pending Approval: 8 items (Attention)
- Review Overdue: 3 items (Risk)
- Scheduled Reviews: 12 items (within 30 days)

### Alert Items

**CRITICAL: Review Overdue (3 items)**
- DOC-SOP-015: 510(k) Submission Process SOP
  - Review Due: 2024-01-10 (20 days overdue)
  - Status: Approved (re-review required)
- DOC-WI-028: Software Validation WI
  - Review Due: 2024-01-15 (15 days overdue)
  - Status: Under Review
- DOC-REP-034: Risk Assessment Report
  - Review Due: 2024-01-20 (10 days overdue)
  - Status: Draft

**WARNING: Pending Approval (8 items)**
- DOC-SOP-045: MDR Classification Procedure
  - Submitted: 2024-01-25
  - Pending: 5 days
- DOC-TMP-011: Validation Protocol Template
  - Submitted: 2024-01-28
  - Pending: 2 days
... (total 8 items)

### Notion Page: [Document Registry Dashboard](https://notion.so/document-dashboard)
```

### 5. Google Calendar Events

```markdown
## Google Calendar - Regulatory Events

### Upcoming Events

**CRITICAL: This Week (2 items)**
- 2024-02-05: FDA Pre-submission Meeting
  - Time: 14:00-15:00
  - Preparation: Presentation, Q&A preparation
- 2024-02-08: NB Audit - Design Control
  - Time: 09:00-17:00
  - Preparation: Design dossier, Evidence documents

**WARNING: Next Week (3 items)**
- 2024-02-12: Management Review Meeting
  - Time: 10:00-12:00
- 2024-02-14: CAPA Review Committee
  - Time: 15:00-16:00
- 2024-02-15: Risk Assessment Workshop
  - Time: 13:00-17:00

**INFO: Scheduled Events (8 items)**
- 2024-02-20: ISO 13485 Internal Audit
- 2024-02-25: 510(k) Submission Target Date
- 2024-03-10: Notified Body Surveillance Audit
...

### Google Calendar: [Regulatory Calendar](https://calendar.google.com/aria)
```

## Alert System (SPEC-ARIA-004 S7.2)

### Alert Levels

| Level | Icon | Condition | Example |
|-------|------|-----------|---------|
| Critical | Red | CAPA overdue, Unacceptable risk, Deadline < 7 days | Immediate action required |
| Warning | Yellow | Review overdue, Pending approval, Deadline 7-30 days | Attention needed |
| Info | Blue | Scheduled events, Status changes | For reference |

**Per SPEC-ARIA-004 S7.2:**
- **Critical (빨강):** CAPA overdue, Unacceptable risk
- **Warning (노랑):** Deadline < 7 days, Review overdue
- **Info (파랑):** Upcoming events, Status changes

### Alert Display

```markdown
**CRITICAL: [Category]**
  - Item title
  - Details
  - Due date
  - Suggested action
  - Notion page link
```

## Options Detail

### --summary (Summary View)

```markdown
## ARIA Status Summary

### Alert Summary
**Critical: 6 items**
  - CAPA Overdue: 2 items
  - Unacceptable Risk: 1 item
  - Submission Deadline < 7 days: 1 item
  - Document Review Overdue: 3 items

**Warning: 12 items**
  - CAPA Due within 7 days: 3 items
  - Risk Review Overdue: 4 items
  - Pending Approval: 8 items

### Key Metrics
- CAPA Open: 5/15 (33%)
- Risk Unacceptable: 1/42 (2.4%)
- Submission Progress: 80% (1 item deadline imminent)
- Document Pending Approval: 8/285 (2.8%)

### Immediate Action Required
1. CAPA-2024-003: Design Validation Failure (15 days overdue)
2. RISK-015: Software Failure - Patient Safety Impact
3. SUB-510K-045: 510(k) Submission (5 days remaining)

For details, run /aria status --detailed
```

### --detailed (Detailed View)

Display detailed information for all items (default).

### --alert-only (Alert Items Only)

Display only Critical and Warning items:

```markdown
## Alert-Only View

### CRITICAL (6 items)
... (all Critical items in detail)

### WARNING (12 items)
... (all Warning items in detail)
```

## Dashboard Updates

### Real-time Updates

```yaml
Condition: Notion DB changes
Actions:
  1. Detect changes via Notion API webhook or polling
  2. Auto-refresh dashboard
  3. Notify user of changes (Critical items)

Frequency: Auto-refresh every 5 minutes
```

### Push Notifications

```yaml
Condition: New Critical item occurs
Actions:
  1. Send push notification to user
  2. Email notification (optional)
  3. Include Notion page link

Example:
  "New CAPA Overdue item detected:
   CAPA-2024-015, Due: 2024-01-30
   Details: [Notion page]"
```

## Statistics and Trends

### Monthly Report

```markdown
## ARIA Monthly Status Report (2024-01)

### CAPA Performance
- New CAPA: 5 items
- Completed CAPA: 3 items
- Average Completion Time: 18 days (Target: 14 days)
- Overdue Rate: 13% (Target: < 5%)

### Risk Management
- New Risks: 8 items
- Mitigated Risks: 6 items
- Unacceptable Risk: 1 item (ongoing monitoring)

### Submission Progress
- Submissions Completed: 2 items
- In Progress: 3 items
- Average Preparation Time: 85 days

### Document Management
- New Documents: 12 items
- Approved: 10 items
- Average Approval Time: 5 days
```

## Error Handling

### Notion API Connection Failed

```
Error: Cannot connect to Notion database.

Resolution:
1. Check internet connection
2. Verify Notion API key is valid
3. Run /aria init notion to reset
```

### Google Calendar Connection Failed

```
Error: Cannot connect to Google Calendar.

Resolution:
1. Verify OAuth authentication is valid
2. Run /aria init google to re-authenticate
```

## Completion Marker

Add `<aria:status:complete alerts=N>` marker when status check completes. (N: alert count)

## Notes

- Dashboard is based on real-time data from Notion DB and Google Calendar
- All items link directly to Notion pages
- Alert thresholds are configurable in settings
- Monthly reports are auto-generated at midnight

---

**Version:** 2.1.0 (Phase 4 - SPEC-ARIA-004 Milestone 5)
**Last Updated:** 2026-02-09
**Language:** English
**Core Principle:** Comprehensive status visibility with proactive risk detection and 3-level warning system
**Spec Compliance:** SPEC-ARIA-004 ER-016, ER-017, S7.1, S7.2
