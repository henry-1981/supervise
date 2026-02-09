# ARIA Hook System

Hook implementations for ARIA (Advanced Regulatory & Intelligence Assistant) SPEC-ARIA-005 Milestone 7.

## Overview

ARIA hooks provide regulatory compliance validation and audit trail functionality for medical device RA/QA documentation workflows.

## Hook Scripts

### 1. Quality Check Hook (PreToolUse)
**Script**: `quality-check-pre-tool.sh`

**Event**: PreToolUse
**Matcher**: Write, Edit
**Timeout**: 100ms

**Features**:
- Validates regulatory citation format (e.g., "21 CFR 820.30", "EU MDR Annex I", "IEC 62304")
- Checks document structure compliance with template requirements
- Verifies VALID framework compliance (Verified, Accurate, Linked, Inspectable, Deliverable)
- Prevents document completion if quality checks fail (exit code 2)

**Exit Codes**:
- 0: Pass - operation allowed
- 0 (with warning): Pass with warning message
- 2: Block - operation prevented

### 2. Audit Trail Hook (PostToolUse)
**Script**: `audit-trail-post-tool.sh`

**Event**: PostToolUse
**Matcher**: Write, Edit
**Timeout**: 2s

**Features**:
- Logs all Write/Edit operations with timestamp, user, and change summary
- Maintains audit trail integrity per 21 CFR Part 11
- Implements audit trail export with chain of custody documentation
- Creates resumption entries after system restart
- JSON-based chain of custody tracking

**Log Files**:
- `.claude/audit/audit-trail.log` - Human-readable audit log
- `.claude/audit/chain-of-custody.json` - Machine-readable chain of custody
- `.claude/audit/resumption-{session_id}.json` - Crash recovery entries

### 3. Template Verification Hook (SessionStart)
**Script**: `template-verification-session-start.sh`

**Event**: SessionStart
**Timeout**: 10s

**Features**:
- Validates template currency against regulatory requirements
- Alerts users to outdated templates before document generation
- Offers automated template updates when available
- Caches last known good status for offline operation

**Tracked Templates**:
- 510k-submission
- technical-file
- risk-analysis
- design-history
- clinical-evaluation

**Regulatory Requirements**:
- 21 CFR 820 (QSR)
- EU MDR 2017/745
- IEC 62304 (Software Life Cycle)
- ISO 13485 (Quality Management)

## Configuration

Hooks are registered in `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/aria/template-verification-session-start.sh\"",
            "timeout": 10,
            "type": "command"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "hooks": [
          {
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/aria/quality-check-pre-tool.sh\"",
            "timeout": 1,
            "type": "command"
          }
        ],
        "matcher": "Write|Edit"
      }
    ],
    "PostToolUse": [
      {
        "hooks": [
          {
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/aria/audit-trail-post-tool.sh\"",
            "timeout": 2,
            "type": "command"
          }
        ],
        "matcher": "Write|Edit"
      }
    ]
  }
}
```

## Performance

- Quality Check: <100ms average
- Audit Trail: <50ms average
- Template Verification: <500ms average (cached), <5s initial

## Error Handling

All hooks implement:
- Graceful degradation on missing dependencies (jq, date options)
- Retry logic for transient failures
- Comprehensive logging to `.claude/logs/` directory
- Non-blocking warnings vs. hard blocks

## Compliance

### 21 CFR Part 11

Audit trail hooks maintain:
- Timestamp (UTC)
- User identity
- Operation type
- File path
- Change summary
- Session ID for traceability

### VALID Framework

All validated documents demonstrate:
- **V**erified: Quality checks passed
- **A**ccurate: Regulatory citations validated
- **L**inked: Traceability to requirements
- **I**nspectable: Complete audit trail
- **D**eliverable: Template compliant

## Troubleshooting

### Hook Not Executing

1. Check script permissions: `chmod +x .claude/hooks/aria/*.sh`
2. Verify path in settings.json uses `$CLAUDE_PROJECT_DIR`
3. Check logs: `.claude/logs/aria-*.log`

### Quality Check Too Strict

Edit `quality-check-pre-tool.sh` to adjust:
- Citation patterns
- VALID framework keywords
- Required sections

### Audit Trail Growing

Implement log rotation in `audit-trail-post-tool.sh`:
```bash
# Archive logs older than 90 days
find .claude/audit -name "audit-trail.log" -mtime +90 -exec gzip {} \;
```

## Development

### Adding New Hooks

1. Create script in `.claude/hooks/aria/`
2. Make executable: `chmod +x`
3. Add to settings.json
4. Document in this README

### Hook Testing

Test hooks manually:
```bash
echo '{"toolName":"Write","session":{"cwd":"."}}' | ./quality-check-pre-tool.sh
echo '{"toolName":"Write","session":{"id":"test"}}' | ./audit-trail-post-tool.sh
echo '{"sessionId":"test","projectDir":"."}' | ./template-verification-session-start.sh
```

## Version

Current: 1.0.0
Updated: 2025-02-09
SPEC: SPEC-ARIA-005 Milestone 7
