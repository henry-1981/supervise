---
name: aria-audit
description: >
  ARIA audit trail search and export command - Search Notion Audit Log database
  for decision history, document changes, and approval records. Supports filtering
  by agent, date range, and action type. CSV/PDF report export available.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "2.0.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, audit, trail, log, compliance"
  argument-hint: "search [--agent name] [--date range] [--action type] [--export format]"
---

# ARIA Audit Trail Search and Export Command

## Purpose

Search Notion Audit Log database for all decision history, document changes, and approval records. Generate audit trail reports for regulatory compliance evidence.

## Usage

```
/aria audit search "CAPA approval" --agent expert-regulatory
/aria audit search --date "2024-01-01:2024-01-31" --action Approve
/aria audit search "document approval" --export csv
/aria audit search --agent orchestrator --export pdf
```

## Audit Log Database Structure

### Fields

- **Timestamp:** Date/time of action (Created time)
- **Agent:** Agent type (orchestrator, expert-regulatory, expert-risk, etc.)
- **Action:** Action type (Create, Update, Delete, Approve, Reject)
- **Entity:** Entity type (Document, CAPA, Risk, Submission, Requirement)
- **Entity ID:** Related entity ID (e.g., CAPA-2024-003)
- **Decision:** Decision content (Text)
- **Rationale:** Decision rationale (Rich Text)
- **Outcome:** Result (Approved, Rejected, Pending, Deferred)
- **Related Docs:** Related documents (Relation)

### Searchable Fields

Timestamp, Agent, Action, Entity, Entity ID, Decision, Outcome

## Search Process

### Step 1: Build Search Query

```
Input: "CAPA approval" --agent expert-regulatory --date "2024-01-01:2024-01-31"

Query Construction:
1. Text search: "CAPA" AND "approval" in Decision, Rationale fields
2. Filter: Agent = "expert-regulatory"
3. Filter: Timestamp >= "2024-01-01" AND <= "2024-01-31"
4. Sort: Timestamp descending (most recent first)
```

### Step 2: Display Search Results

```markdown
## Audit Trail Search Results: "CAPA approval"

Search Criteria:
- Agent: expert-regulatory
- Date: 2024-01-01 ~ 2024-01-31
- Action: Approve

### Found Items (12)

1. **2024-01-28 14:32** - expert-regulatory
   - Action: Approve
   - Entity: CAPA
   - Entity ID: CAPA-2024-008
   - Decision: Supplier qualification CAPA approved
   - Rationale: Supplier achieved ISO 13485 certification, requirements met
   - Outcome: Approved
   - Related Docs: DOC-REP-112 (Supplier Audit Report)
   - [View Notion page](https://notion.so/audit-log-xxx)

2. **2024-01-25 10:15** - expert-regulatory
   - Action: Approve
   - Entity: CAPA
   - Entity ID: CAPA-2024-007
   - Decision: Design validation CAPA approved
   - Rationale: All validation tests passed, usability study complete
   - Outcome: Approved
   - Related Docs: DOC-REP-108 (Validation Report)
   - [View Notion page](https://notion.so/audit-log-xxx)

...

### Summary
- Total search: 12 items
- Approved: 10 items
- Rejected: 1 item
- Pending: 1 item
```

## Filter Options

### Agent Filter

```
--agent orchestrator           # MoAI orchestrator
--agent expert-regulatory      # Regulatory expert
--agent expert-risk            # Risk management expert
--agent expert-capa            # CAPA expert
--agent expert-document        # Document management expert
--agent all                    # All agents (default)
```

### Date Filter

```
--date "2024-01-01:2024-01-31"  # Specific date range
--date "today"                   # Today
--date "last-7-days"             # Last 7 days
--date "last-30-days"            # Last 30 days
--date "this-month"              # This month
--date "last-month"              # Last month
```

### Action Filter

```
--action Create                 # Create
--action Update                 # Update
--action Delete                 # Delete
--action Approve                # Approve
--action Reject                 # Reject
--action all                    # All actions (default)
```

### Entity Filter

```
--entity Document              # Document
--entity CAPA                  # CAPA
--entity Risk                  # Risk
--entity Submission            # Submission
--entity Requirement           # Requirement
--entity all                   # All entities (default)
```

## Report Export

### CSV Export

```csv
Timestamp,Agent,Action,Entity,Entity ID,Decision,Outcome
2024-01-28 14:32,expert-regulatory,Approve,CAPA,CAPA-2024-008,"Supplier qualification CAPA approved",Approved
2024-01-25 10:15,expert-regulatory,Approve,CAPA,CAPA-2024-007,"Design validation CAPA approved",Approved
...
```

Usage:
```
/aria audit search "CAPA approval" --export csv
→ Saved to audit-trail-20240129.csv file
```

### PDF Export

Generate audit trail report in PDF format:

```
/aria audit search --date "2024-01-01:2024-01-31" --export pdf
→ Saved to audit-trail-report-202401.pdf file
```

PDF report structure:
```markdown
# ARIA Audit Trail Report

**Report Period:** 2024-01-01 ~ 2024-01-31
**Generated:** 2024-02-09
**Generated By:** ARIA System

## Summary
- Total items: 156
- By agent: orchestrator (45), expert-regulatory (32), ...
- By action: Create (42), Update (68), Approve (28), ...
- By entity: Document (58), CAPA (32), Risk (28), ...

## Timeline

### 2024-01-31 (5 items)
...

### 2024-01-30 (8 items)
...

## Detailed History
...
```

## Timeline View

Display audit trail history in chronological order:

```markdown
## Audit Trail Timeline: 2024-01-29

### 14:32 - expert-regulatory
📝 CAPA-2024-008 Approved
   - Decision: Supplier qualification CAPA approved
   - Rationale: ISO 13485 certification achieved
   - Result: Approved

### 14:15 - orchestrator
🔧 CAPA-2024-008 Created
   - Decision: CAPA initiated for supplier qualification gap
   - Rationale: NB audit finding
   - Result: Pending

### 13:45 - expert-risk
📊 RISK-022 Re-evaluated
   - Decision: Risk level down-graded (15 → 9)
   - Rationale: Additional controls implemented
   - Result: Approved

### 11:20 - expert-document
📄 DOC-SOP-045 Approved
   - Decision: MDR classification procedure approved
   - Rationale: NB comments incorporated
   - Result: Approved

[View Full Timeline]
```

## Audit Trail Integrity

### Immutability Guarantee

```yaml
Audit Log Immutability:
  - Created Audit Log items cannot be modified
  - Deletion prohibited (Read-only permission)
  - Change history tracked via Notion Page Version History

Tamper Prevention:
  - Timestamp is Notion Created time (auto-generated)
  - Agent is automatically recorded by system
  - User cannot directly modify
```

### Completeness Verification

```yaml
Audit Trail Completeness Check:
  1. All decisions must be recorded in Audit Log
  2. Verify connection via Related Docs Relation
  3. Verify Timestamp continuity (no gaps)
  4. Verify agent activity history match

On mismatch detection:
  - Warning: "Audit Log gap detected: 2024-01-15 14:00 ~ 16:00"
  - Action: Notify administrator, manual investigation required
```

## Regulatory Compliance Support

### ISO 13485 Requirements

```
ISO 13485 Clause 4.2.4: Quality management system documentation
- All decisions must be documented
- Change history must be maintained
- Audit trail must be traceable

ARIA Audit Log provides:
- Decision: Decision content documentation
- Rationale: Decision rationale recording
- Timestamp: Change time recording
- Related Docs: Related document links
```

### FDA 21 CFR 820 Requirements

```
21 CFR 820.40: Management responsibility
- All quality activities must be documented
- Management review records maintained

21 CFR 820.180: General records
- Record retention period: product life + 2 years
- Record searchability guaranteed

ARIA Audit Log provides:
- All agent activity recording
- Permanent storage via Notion DB
- Full-text search support
```

### EU MDR Requirements

```
EU MDR Annex IX: Quality management system
- Internal audit records maintained
- Management review records
- CAPA traceability

ARIA Audit Log provides:
- Internal audit tracking
- Management decision records
- CAPA lifecycle tracking
```

## Advanced Search

### Complex Condition Search

```
/aria audit search --agent expert-regulatory --action Approve --entity CAPA --date "last-30-days"

Result: All CAPA decisions approved by expert-regulatory in last 30 days
```

### Decision Rationale Search

```
/aria audit search "ISO 13485"

Result: All audit trails with "ISO 13485" in Decision or Rationale fields
```

### Result Filtering

```
/aria audit search --outcome Approved --date "this-month"

Result: All approved decisions this month
```

## Error Handling

### No Audit Log Found

```
Search Results: No Audit Log found matching criteria.

Suggestions:
1. Relax search criteria (expand date range)
2. Try different filters
3. View full Audit Log: /aria audit search --date "last-30-days"
```

### Permission Denied

```
Error: No permission to access Audit Log.

Resolution:
1. Grant Audit Log DB access permission to Notion Integration
2. Run /aria init notion to reset permissions
```

### Export Failed

```
Error: CSV/PDF export failed.

Resolution:
1. Too many search results (1000+ items). Reduce date range.
2. Check disk space
3. Check file permissions
```

## Usage Examples

### Example 1: CAPA Decision History

```
/aria audit search --entity CAPA --action Approve --date "last-30-days"

Result:
- 8 CAPA decisions approved in last 30 days
- Each CAPA's decision rationale, related documents
- CAPA-2024-008, CAPA-2024-007, ... detailed information
```

### Example 2: Document Change Tracking

```
/aria audit search --entity Document --action Update --date "2024-01-01:2024-01-31"

Result:
- 42 document change histories in January
- Changed documents: DOC-SOP-015, DOC-WI-028, ...
- Change time, responsible agent, change rationale
```

### Example 3: Agent Activity Report

```
/aria audit search --agent expert-regulatory --date "last-month" --export pdf

Result:
- expert-regulatory activity report (PDF)
- 32 total activities
- Activity type distribution
- Timeline view
```

### Example 4: Regulatory Compliance Evidence

```
/aria audit search "NB audit" --date "2024-01-01:2024-01-31" --export csv

Result:
- All NB audit related activities
- CSV file provided as regulatory compliance evidence
- CAPA, Risk, Document change tracking
```

## Completion Marker

Add `<aria:audit:complete results=N exported=Y>` marker when search completes. (N: result count, Y: export status)

## Notes

- Audit Log is an immutable permanent record
- All decisions must be recorded in Audit Log (audit trail completeness)
- CSV/PDF export supports regulatory compliance evidence
- Search results limited to 1000 items for export
- Audit Log retained for product life + 2 years (FDA 21 CFR 820.180)

---

**Version:** 2.0.0 (Phase 4 - Enhanced Export and Compliance Features)
**Last Updated:** 2026-02-09
**Language:** English
**Core Principle:** Complete audit trail for regulatory compliance evidence
