# ARIA Team Workflow: Audit Response Preparation

## Purpose

Prepare FDA/ISO audit responses through parallel team-based development with CAPA planning and implementation coordination.

## Prerequisites

- Audit findings received (FDA 483, ISO 13485 nonconformity)
- Finding details documented
- workflow.team.enabled: true
- CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
- Triggered by: /aria audit respond OR auto-detected complexity (3+ findings)

## Team Composition

### Audit Researcher (team-researcher, haiku)
- **Role**: Research audit findings and regulatory requirements
- **File Ownership**: `.aria/audit/research/**`, `.aria/audit/findings/**`
- **Tools**: Read, Grep, Glob, WebSearch, WebFetch
- **Permission Mode**: plan (read-only)

### CAPA Analyst (team-analyst, sonnet)
- **Role**: Plan CAPA and categorize findings
- **File Ownership**: `.aria/audit/capa-planning/**`, `.aria/audit/root-cause/**`
- **Tools**: Read, Grep, Glob, Write, Edit
- **Permission Mode**: plan

### CAPA Expert (team-expert, sonnet)
- **Role**: Execute root cause analysis and implement CAPA
- **File Ownership**: `.aria/audit/capa-documents/**`, `.aria/audit/effectiveness-checks/**`
- **Tools**: Read, Grep, Glob, Write, Edit
- **Permission Mode**: acceptEdits

## Phase 0: Task Decomposition

1. Analyze audit findings:
   - Parse all observations/nonconformities
   - Identify regulatory citations
   - Determine severity levels

2. Create team:
   ```typescript
   TeamCreate({
     team_name: "aria-audit-response-{audit_id}",
     description: "Audit Response for {audit_type} on {date}",
     teammates: [
       { name: "audit-researcher", model: "haiku", ... },
       { name: "capa-analyst", model: "sonnet", ... },
       { name: "capa-expert", model: "sonnet", ... }
     ],
     sharedTaskBoard: true
   })
   ```

3. Create shared task list:
   ```typescript
   TaskCreate({ subject: "Analyze audit observation details", assignee: "audit-researcher" })
   TaskCreate({ subject: "Categorize findings by severity", assignee: "capa-analyst", blockedBy: ["audit-researcher"] })
   TaskCreate({ subject: "Conduct root cause analysis", assignee: "capa-expert", blockedBy: ["capa-analyst"] })
   TaskCreate({ subject: "Implement and document CAPA", assignee: "capa-expert", blockedBy: ["capa-expert"] })
   ```

## Phase 1: Spawn Team

Spawn all teammates in parallel:

```typescript
Task(
  subagent_type: "team-researcher",
  team_name: "aria-audit-response-{audit_id}",
  name: "audit-researcher",
  prompt: "You are the Audit Researcher for audit response preparation.
    Audit: {audit_type} on {date}
    Findings: {finding_count} observations
    Your responsibilities: Analyze observations, research regulations, identify requirements.
    File ownership: .aria/audit/research/**, .aria/audit/findings/**
    Coordinate with capa-analyst for categorization.
    Mark tasks complete via TaskUpdate."
)

Task(
  subagent_type: "team-analyst",
  team_name: "aria-audit-response-{audit_id}",
  name: "capa-analyst",
  prompt: "You are the CAPA Planning Analyst for audit response.
    Audit: {audit_type} on {date}
    Your responsibilities: Categorize findings, plan CAPA, design corrective/preventive actions.
    File ownership: .aria/audit/capa-planning/**, .aria/audit/root-cause/**
    Wait for research from audit-researcher.
    Mark tasks complete via TaskUpdate."
)

Task(
  subagent_type: "team-expert",
  team_name: "aria-audit-response-{audit_id}",
  name: "capa-expert",
  prompt: "You are the CAPA Implementation Expert for audit response.
    Audit: {audit_type} on {date}
    Your responsibilities: Execute root cause analysis, implement CAPA, verify effectiveness.
    File ownership: .aria/audit/capa-documents/**, .aria/audit/effectiveness-checks/**
    Wait for CAPA plan from capa-analyst.
    Mark tasks complete via TaskUpdate."
)
```

## Phase 2: Parallel Execution

### Investigation Phase (audit-researcher + capa-analyst)

**Audit Researcher Tasks**:

1. **Observation Analysis**
   - Parse observation text
   - Extract regulatory citation
   - Identify scope and severity
   - Document in `.aria/audit/findings/`

2. **Regulatory Research**
   - Research full CFR/ISO requirement
   - Identify related requirements
   - Review applicable guidance
   - Store in `.aria/audit/research/`

3. **Coordination**
   - SendMessage to capa-analyst: "Finding {id} researched. Severity assessment: {severity}"
   - Update TaskList status

**CAPA Analyst Tasks** (in parallel):

1. **Finding Categorization**
   - Categorize by severity (Critical/Major/Minor)
   - Assign CAPA priority level
   - Document in `.aria/audit/categorization/`

2. **CAPA Planning**
   - Plan root cause approach
   - Design corrective actions
   - Design preventive actions
   - Store in `.aria/audit/capa-planning/`

### Root Cause Phase (capa-expert)

**Sequential Execution** (waits for categorization):

1. **Root Cause Analysis**
   - Execute 5-Whys or Fishbone analysis
   - Collect data and evidence
   - Identify true root cause(s)
   - Document in `.aria/audit/root-cause/`

2. **Coordination**
   - SendMessage to capa-analyst: "Root cause identified for finding {id}: {root_cause}"
   - Update TaskList status

### CAPA Planning Phase (capa-analyst + capa-expert)

**CAPA Analyst Tasks**:

1. **Action Design**
   - Design corrective actions based on root cause
   - Design preventive measures
   - Establish timeline and resources
   - Update CAPA plan in `.aria/audit/capa-planning/`

2. **Validation Routing**
   - Route CAPA plan for validation
   - Incorporate feedback
   - Finalize CAPA plan

### Implementation Phase (capa-expert)

**Sequential Execution**:

1. **CAPA Documentation**
   - Document immediate corrections
   - Document corrective actions
   - Document preventive measures
   - Store in `.aria/audit/capa-documents/`

2. **Effectiveness Verification**
   - Define effectiveness metrics
   - Collect verification data
   - Analyze results
   - Document conclusion in `.aria/audit/effectiveness-checks/`

## Phase 3: Coordination Patterns

### Finding Categorization

**Trigger**: Finding received

**Action**:
```typescript
SendMessage({
  type: "message",
  recipient: "capa-analyst",
  content: "FINDING RECEIVED: Observation {id} requires categorization. Citation: {citation}. Text: {observation_text}.",
  summary: "New finding requires categorization"
})
```

**Severity-Based CAPA Assignment**:
- **Critical**: Immediate CAPA expert assignment
- **Major**: Planned CAPA expert assignment
- **Minor**: Standard CAPA analyst planning

### CAPA Validation

**Trigger**: CAPA plan drafted

**Action**:
```typescript
SendMessage({
  type: "message",
  recipient: "quality-reviewer",
  content: "CAPA VALIDATION REQUEST: CAPA plan for finding {id} ready for validation. Root cause: {root_cause}. Actions: {actions}.",
  summary: "CAPA plan requires validation"
})
```

**Validation Chain**:
1. CAPA analyst self-review
2. Quality reviewer validation
3. Management approval (for Critical findings)

### Deadline Alert

**Trigger**: CAPA deadline at risk

**Action**:
```typescript
SendMessage({
  type: "broadcast",
  content: "DEADLINE ALERT: CAPA for finding {id} at risk. Current deadline: {deadline}. Days remaining: {days}. Suggest escalation to management.",
  summary: "CAPA deadline at risk"
})
```

**Threshold**: 3 days before deadline

### Cross-Functional Escalation

**Trigger**: Finding requires cross-functional input

**Action**:
```typescript
const escalationMap = {
  "R&D": "engineering-lead",
  "Manufacturing": "operations-lead",
  "Quality": "quality-manager",
  "Regulatory": "regulatory-affairs"
}

SendMessage({
  type: "message",
  recipient: escalationMap[department],
  content: "CROSS-FUNCTIONAL INPUT REQUESTED: Finding {id} requires {department} expertise. Context: {context}.",
  summary: "Cross-functional input needed for finding {id}"
})
```

## Phase 4: Quality Validation

After all CAPA complete:

1. **Root Cause Validation**
   - Verify root cause evidence-based
   - Confirm 5-Whys depth reached
   - Validate root cause linkage to finding

2. **CAPA Completeness Check**
   - Correction documented
   - Corrective action defined
   - Preventive action defined
   - Effectiveness check planned

3. **Timeline Validation**
   - Response timeline meets requirements (15 business days for FDA 483)
   - CAPA implementation timeline realistic
   - Effectiveness verification scheduled

4. **Documentation Completeness**
   - All CAPA elements documented
   - Traceability maintained
   - Audit trail complete

## Phase 5: Team Shutdown

After validation complete:

```typescript
// Notify team of completion
SendMessage({
  type: "broadcast",
  content: "AUDIT RESPONSE COMPLETE: All findings addressed with CAPA. CAPA documents: .aria/audit/capa-documents/",
  summary: "Audit response complete"
})

// Shutdown team
TeamDelete()
```

## Escalation Paths

| Condition | Escalate To | Action |
|-----------|-------------|--------|
| Critical finding | crisis-management | Activate immediate response protocol |
| Quality system issue | quality-management | Request management review |
| Complex finding (engineering) | engineering-lead | Request technical input |
| Regulatory uncertainty | regulatory-affairs | Request regulatory guidance |
| Supply chain issue | supplier-quality | Request supplier intervention |
| CAPA deadline at risk | management | Request extension or resources |

## Quality Gates

- [ ] Root cause identified and verified
- [ ] Correction documented
- [ ] Corrective action defined
- [ ] Preventive action defined
- [ ] Effectiveness check planned
- [ ] Timeline established
- [ ] Documentation complete

## Completion Markers

- All findings addressed
- CAPA approved
- Effectiveness verified
- Documentation signed off

## Root Cause Methods

- **Primary**: 5-Whys (required depth: 5)
- **Secondary**: Fishbone, Fault Tree Analysis, Is/Is Not Analysis

## Fallback Strategy

If team mode fails:
1. Graceful fallback to aria-orchestrator
2. Continue from last completed task
3. Sequential execution via expert-audit, expert-capa

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**SPEC**: SPEC-ARIA-005 (SR-008 to SR-014)
