# ARIA Agent Teams Mode Implementation

SPEC-ARIA-005 Milestone 2: Agent Teams Mode implementation for medical device RA/QA workflows.

## Overview

ARIA (Audit Response & Submission Assistant) now supports Agent Teams mode for complex 510(k) preparation and audit response workflows. The system automatically selects between sequential and team-based execution based on complexity thresholds.

## Features

### 1. Dual-Mode Execution

- **Sequential Mode**: For simple workflows (single findings, few sections)
- **Team Mode**: For complex workflows (5+ sections, 3+ findings)
- **Automatic Fallback**: Gracefully falls back to sequential if team creation fails

### 2. 510(k) Preparation Team

**Teammates**:
- `fda-researcher` (haiku): FDA guidance and predicate research
- `predicate-analyst` (sonnet): Substantial equivalence analysis
- `submission-writer` (sonnet): eCopy template drafting

**Activation**: 5+ submission sections

**Workflow**: Research → Analysis → Drafting

### 3. Audit Response Team

**Teammates**:
- `audit-researcher` (haiku): Audit finding analysis
- `capa-analyst` (sonnet): CAPA planning
- `capa-expert` (sonnet): Root cause and implementation

**Activation**: 3+ audit findings

**Workflow**: Investigation → Root Cause → CAPA Planning → Implementation

## Configuration

### Environment Variables

Add to `.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Team Configuration Files

Located in `.aria/teams/`:

- `team-510k-preparation.json`: 510(k) workflow configuration
- `team-audit-response.json`: Audit response workflow configuration

## Usage

### 510(k) Preparation

```bash
# Simple submission (sequential mode)
/aria 510k --device "Blood Pressure Monitor"

# Complex submission (team mode activated)
/aria 510k --device "AI Diagnostic System" --team
```

### Audit Response

```bash
# Single finding (sequential mode)
/aria audit --finding "21 CFR 820.20 - No CAPA procedure"

# Multiple findings (team mode activated)
/aria audit --findings audit-483-2025.json --team
```

## File Structure

```
.aria/
├── teams/                              # Team configurations
│   ├── team-510k-preparation.json     # 510(k) team config
│   └── team-audit-response.json       # Audit team config
├── skills/                             # Coordination skills
│   ├── aria-team-coordination/        # Team management
│   └── aria-workflows/                # Workflow definitions
├── research/                           # FDA research outputs
├── analysis/                           # Analysis outputs
├── submissions/                        # 510(k) drafts
├── findings/                           # Audit finding analysis
├── capa/                               # CAPA documentation
└── checkpoints/                        # Progress tracking
```

## Agent Definitions

ARIA-specific team agents in `.claude/agents/aria/`:

- `team-fda-researcher.md`: FDA regulatory research specialist
- `team-predicate-analyst.md`: Substantial equivalence analyst
- `team-submission-writer.md`: 510(k) submission writer
- `team-audit-researcher.md`: Audit finding researcher
- `team-capa-analyst.md`: CAPA planning analyst
- `team-capa-expert.md`: CAPA implementation expert

## Quality Gates

### 510(k) Quality Gates

- sections_complete: All required sections present
- e_copy_format_compliant: eCopy template standards met
- references_cited: All references properly documented
- consistency_check: Cross-references validated

### Audit Quality Gates

- root_cause_identified: True root cause (not symptom)
- corrective_action_defined: Systemic change planned
- preventive_action_defined: Extension to similar issues
- effectiveness_check_planned: Verifiable metrics defined
- timeline_established: Realistic implementation schedule
- documentation_complete: Full audit trail

## Escalation Paths

### 510(k) Escalation

- Clinical expertise: clinical-reviewer
- Regulatory interpretation: regulatory-affairs
- Technical analysis: senior-analyst

### Audit Escalation

- Quality system: quality-management
- Engineering: engineering-lead
- Regulatory: regulatory-affairs
- Supplier: supplier-quality
- Critical: crisis-management

## Fallback Strategy

When team mode fails:

1. Shutdown any active teammates
2. Map to fallback agents:
   - fda-researcher → manager-spec
   - predicate-analyst → expert-backend
   - submission-writer → manager-docs
   - audit-researcher → manager-spec
   - capa-analyst → expert-debug
   - capa-expert → manager-quality
3. Resume from last completed checkpoint
4. Continue sequential execution

## Implementation Status

### Completed (Milestone 2)

- [x] Team configuration JSON files
- [x] 510(k) team agent definitions
- [x] Audit response team agent definitions
- [x] Team coordination skill
- [x] Integrated workflow skill
- [x] Fallback mechanism documentation

### Next Steps (Milestone 3+)

- [ ] Slash command integration
- [ ] Progress tracking dashboard
- [ ] Effectiveness verification templates
- [ ] CAPA effectiveness metrics
- [ ] Integration testing

## Version

Version: 1.0.0
Last Updated: 2025-02-09
SPEC: SPEC-ARIA-005
Milestone: 2 (Agent Teams Mode)
