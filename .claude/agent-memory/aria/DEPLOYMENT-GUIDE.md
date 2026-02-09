# ARIA Agent Memory System - Deployment Guide

## Quick Reference

### Location
```
/Users/hb/Project/Agent-Skills/.claude/agent-memory/aria/
```

### Memory Files
- `regulatory-decisions-enhanced.json` - Regulatory decisions (v2.0.0)
- `company-preferences-enhanced.json` - Company preferences (v2.0.0)
- `task-patterns-enhanced.json` - Task patterns (v2.0.0)
- `learning-metrics-enhanced.json` - Learning metrics (v2.0.0)

### Operations Scripts
- `operations/memory-manager.py` - Core memory operations
- `operations/notion-backup.py` - Notion MCP integration
- `operations/pattern-detector.py` - Pattern recognition

### Documentation
- `README.md` - System overview and quick start
- `docs/MEMORY-ARCHITECTURE.md` - Technical architecture
- `docs/OPERATIONS-GUIDE.md` - User operations guide
- `docs/NOTION-INTEGRATION.md` - Notion integration guide
- `IMPLEMENTATION-SUMMARY.md` - Implementation details

## Verification

### Validate Memory Files

```bash
python3 .claude/agent-memory/aria/operations/memory-manager.py validate --all
```

**Expected Output**:
```
Validation Results:
Decisions: VALID
Preferences: VALID
Patterns: VALID
Metrics: VALID
```

### Check File Structure

```bash
ls -la .claude/agent-memory/aria/
```

**Expected Files**:
- 4 enhanced JSON files (v2.0.0)
- 4 original JSON files (v1.0.0 - preserved)
- 4 schema files (validation)
- 3 operations scripts (Python)
- 5 documentation files (Markdown)

## Basic Operations

### Store a Regulatory Decision

```bash
python3 .claude/agent-memory/aria/operations/memory-manager.py store-decision \
  --question "Is SaMD subject to FDA 510(k) for minor bug fixes?" \
  --answer "Bug fixes that do not affect device safety or effectiveness are typically not subject to 510(k) submission requirements." \
  --regulation "21 CFR 807.81(a)" \
  --domain "FDA" \
  --confidence 0.95
```

### Retrieve Decisions

```bash
python3 .claude/agent-memory/aria/operations/memory-manager.py retrieve-decisions \
  --query "Software updates medical devices" \
  --threshold 0.7
```

### Learn Company Preference

```bash
python3 .claude/agent-memory/aria/operations/memory-manager.py learn-preference \
  --company-id "default" \
  --category "formatting" \
  --key "date_format" \
  --value "DD/MM/YYYY"
```

### Sync to Notion

```bash
python3 .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

## Requirements Coverage

### Regulatory Decision Memory (UR-001 to UR-007)
- UR-001: Persistent memory across sessions (Complete)
- UR-002: Store rationale, regulations, applicability (Complete)
- UR-003: Organize by regulatory domain (Complete)
- UR-004: Prompt to store during drafting (Complete)
- UR-005: Retrieve relevant past decisions (Complete)
- UR-006: Flag obsolete decisions (Complete)
- UR-007: Tag company-specific interpretations (Complete)

### Company Preference Learning (UR-008 to UR-014)
- UR-008: Learn company-specific preferences (Complete)
- UR-009: Maintain preferred templates (Complete)
- UR-010: Track approved vs rejected suggestions (Complete)
- UR-011: Record rejection reasons (Complete)
- UR-012: Learn from user modifications (Complete)
- UR-013: Detect preference conflicts (Complete)
- UR-014: Flag user vs company standard conflicts (Complete)

### Repetitive Task Pattern Recognition (UR-015 to UR-021)
- UR-015: Identify repetitive task patterns (Complete)
- UR-016: Maintain common task sequences (Complete)
- UR-017: Suggest automation for patterns (Complete)
- UR-018: Suggest templates after 3+ repetitions (Complete)
- UR-019: Offer to execute learned patterns (Complete)
- UR-020: Detect significant pattern variations (Complete)
- UR-021: Merge overlapping patterns (Complete)

## Integration Points

### Agent Integration

Agents can access memory via:

```python
from aria.memory import MemoryManager

manager = MemoryManager()
decision_id = manager.store_decision({...})
decisions = manager.retrieve_decisions("query")
manager.learn_preference("company-id", "category", "key", "value")
```

### Notion MCP Integration

Configure Notion database ID:

```bash
export NOTION_ARIA_MEMORY_DB="your-database-id"
python3 .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

### Git Integration

Configure union merge for memory files:

```bash
git config merge.union.name "Union Merge"
git config merge.union.driver "union %O %A %B"
```

## File Structure

```
.claude/agent-memory/aria/
├── regulatory-decisions-enhanced.json      # v2.0.0 - Complete schema
├── company-preferences-enhanced.json       # v2.0.0 - Multi-company support
├── task-patterns-enhanced.json             # v2.0.0 - Pattern library
├── learning-metrics-enhanced.json          # v2.0.0 - Comprehensive metrics
├── regulatory-decisions.json               # v1.0.0 - Original (preserved)
├── company-preferences.json                # v1.0.0 - Original (preserved)
├── task-patterns.json                      # v1.0.0 - Original (preserved)
├── learning-metrics.json                   # v1.0.0 - Original (preserved)
├── schemas/
│   ├── regulatory-decisions-schema.json    # JSON Schema validation
│   ├── company-preferences-schema.json     # JSON Schema validation
│   ├── task-patterns-schema.json           # JSON Schema validation
│   └── learning-metrics-schema.json        # JSON Schema validation
├── operations/
│   ├── memory-manager.py                   # Core memory operations (500+ lines)
│   ├── notion-backup.py                    # Notion integration (400+ lines)
│   └── pattern-detector.py                 # Pattern recognition (400+ lines)
├── docs/
│   ├── MEMORY-ARCHITECTURE.md              # Technical architecture (600+ lines)
│   ├── OPERATIONS-GUIDE.md                 # User operations (500+ lines)
│   └── NOTION-INTEGRATION.md               # Notion integration (400+ lines)
├── README.md                               # System overview (400+ lines)
└── IMPLEMENTATION-SUMMARY.md               # Implementation details (400+ lines)
```

## Key Features

### Regulatory Decision Memory
- Decision indexing by regulation, domain, applicability
- Company-specific flag for segregation
- Confidence scoring for quality
- Validity tracking for regulation changes
- Usage statistics for relevance ranking

### Company Preference Learning
- Multi-company support with segregation
- 5 preference categories (formatting, terminology, templates, regulatory_framework, workflow)
- Suggestion history with feedback tracking
- Conflict detection and resolution
- Global standards for regulatory domains

### Repetitive Task Pattern Recognition
- Pattern detection from task sequences
- Confidence scoring based on occurrences
- Pattern library with common workflows
- Automation threshold configuration (default: 3 occurrences)
- Pattern merging for generalization

### Learning Metrics Tracking
- Adoption metrics (feature usage, sessions)
- Effectiveness metrics (accuracy, relevance)
- Learning metrics (patterns, preferences, decisions)
- Quality metrics (integrity, consistency)
- Performance metrics (retrieval time, sync rate)
- Regulatory coverage (domains, decisions)

## Quality Assurance

### Schema Validation
All memory files validated against JSON schemas:

```bash
python3 .claude/agent-memory/aria/operations/memory-manager.py validate --all
```

### Memory Integrity
Integrity scoring (0-100) for:
- Data consistency
- Cross-reference validation
- Merge conflict detection

### Performance Monitoring
Metrics for:
- Decision retrieval time
- Pattern detection time
- Notion sync success rate
- Cache hit rate

## Security and Privacy

### Data Protection
- Company-specific data segregation
- No secrets stored in memory
- Audit trail for all modifications
- 365-day data retention policy

### Access Control
- Notion permissions by team
- Git access control for VCS
- Read-only access for user scope patterns

### Backup Strategy
Three-layer backup:
1. Local: Git version control
2. Cloud: Notion database
3. Archive: Quarterly exports

## Next Steps

### Immediate Actions
1. Review documentation in `docs/` directory
2. Validate memory files using operations script
3. Configure Notion database ID (if using Notion backup)
4. Test basic operations (store/retrieve decisions)

### Configuration
1. Set Notion database ID environment variable
2. Configure Git merge strategy for memory files
3. Set up automated sync via hooks
4. Configure retention policies

### Training
1. Review OPERATIONS-GUIDE.md for usage instructions
2. Test pattern detection with sample sequences
3. Practice storing and retrieving decisions
4. Configure company-specific preferences

## Troubleshooting

### Common Issues

**Issue**: Merge conflicts in memory files
**Solution**: Use `git merge-file --union` for arrays

**Issue**: Notion sync failures
**Solution**: Check `NOTION_ARIA_MEMORY_DB` environment variable

**Issue**: Schema validation errors
**Solution**: Compare with schema files in `schemas/` directory

### Debug Mode

Enable debug logging:
```python
import logging
logging.getLogger('aria.memory').setLevel(logging.DEBUG)
```

## Support

### Documentation
- README.md: Quick start guide
- MEMORY-ARCHITECTURE.md: System architecture
- OPERATIONS-GUIDE.md: User operations
- NOTION-INTEGRATION.md: Notion integration

### Verification
All memory files validated successfully:
- Decisions: VALID
- Preferences: VALID
- Patterns: VALID
- Metrics: VALID

## Status

**Implementation**: Complete
**Validation**: Passed
**Documentation**: Complete
**Ready for Production**: Yes

---

**Version**: 2.0.0
**Date**: 2026-02-09
**Status**: Complete and Validated
