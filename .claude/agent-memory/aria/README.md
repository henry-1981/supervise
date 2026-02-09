# ARIA Agent Memory System

## Overview

The ARIA Agent Memory System implements SPEC-ARIA-005 requirements for persistent cross-session learning, enabling regulatory intelligence assistants to remember decisions, preferences, and patterns across sessions.

## Architecture

### Memory Storage Structure

```
.claude/agent-memory/aria/
├── regulatory-decisions-enhanced.json    # Regulatory decision memory
├── company-preferences-enhanced.json      # Company preference learning
├── task-patterns-enhanced.json            # Repetitive task patterns
├── learning-metrics-enhanced.json         # System learning tracking
├── schemas/                               # JSON Schema definitions
│   ├── regulatory-decisions-schema.json
│   ├── company-preferences-schema.json
│   ├── task-patterns-schema.json
│   └── learning-metrics-schema.json
├── operations/                            # Memory operation utilities
│   ├── memory-manager.py
│   ├── notion-backup.py
│   └── pattern-detector.py
└── docs/                                  # Documentation
    ├── MEMORY-ARCHITECTURE.md
    ├── OPERATIONS-GUIDE.md
    └── NOTION-INTEGRATION.md
```

### Memory Scopes

- **Project Scope** (`.claude/agent-memory/aria/`): Shared via VCS, team-accessible
- **Notion Backup**: Persistent cloud backup with knowledge base integration
- **Session Cache**: Runtime caching for performance optimization

## Memory Components

### 1. Regulatory Decision Memory

**Purpose**: Store regulatory decisions with rationale, source regulations, and applicability context.

**Schema Version**: 2.0.0

**Key Fields**:
- `decision_id`: Unique identifier (DEC-YYYY-NNN)
- `question`: Regulatory question asked
- `answer`: Decision provided with rationale
- `regulation`: Source regulation citation
- `applicability`: Applicable domains/tags
- `company_specific`: Whether interpretation is company-specific
- `confidence_score`: Decision confidence (0-1)
- `valid_until`: Expiration date for time-sensitive decisions

**Index Structure**:
```json
{
  "by_regulation": {"21 CFR 807.81(a)": ["DEC-2026-001"]},
  "by_domain": {"FDA": ["DEC-2026-001"]},
  "by_applicability": {"SaMD": ["DEC-2026-001"]}
}
```

**Use Cases**:
- UR-001: Persistent memory across sessions
- UR-004: Prompt to store decisions during drafting
- UR-005: Retrieve relevant past decisions
- UR-006: Flag obsolete decisions when regulations change
- UR-007: Segregate company-specific interpretations

### 2. Company Preference Learning

**Purpose**: Learn and remember company-specific preferences for formatting, terminology, and templates.

**Schema Version**: 2.0.0

**Preference Categories**:
- `formatting`: Document structure, dates, numbers, citations
- `terminology`: Company-specific term mappings
- `templates`: Preferred templates per document type
- `regulatory_framework`: Primary/secondary frameworks, standards
- `workflow`: Approval processes, version control

**Suggestion History**:
```json
{
  "accepted": [{"timestamp": "...", "suggestion": "..."}],
  "rejected": [{"timestamp": "...", "reason": "..."}],
  "modified": [{"timestamp": "...", "original": "...", "modification": "..."}]
}
```

**Use Cases**:
- UR-008: Learn company-specific preferences
- UR-009: Maintain preferred templates
- UR-010: Track approved vs rejected suggestions
- UR-011: Record rejection reasons
- UR-012: Learn from user modifications
- UR-013: Detect and resolve preference conflicts
- UR-014: Flag user vs company standard conflicts

### 3. Repetitive Task Pattern Recognition

**Purpose**: Identify and remember repetitive task patterns for automation suggestions.

**Schema Version**: 2.0.0

**Pattern Structure**:
```json
{
  "id": "PAT-001",
  "name": "Quarterly Audit Preparation",
  "occurrence_count": 3,
  "confidence": 0.85,
  "steps": [
    {"order": 1, "action": "schedule_audit", "agent": "orchestrator"},
    {"order": 2, "action": "generate_agenda", "agent": "expert-audit"}
  ],
  "automatable": true
}
```

**Learning State**:
- `detection_enabled`: Enable/disable pattern detection
- `automation_threshold`: Minimum occurrences (default: 3)
- `confidence_threshold`: Minimum confidence score (default: 0.7)
- `pattern_variations_allowed`: Allowed variation tolerance (default: 0.2)

**Use Cases**:
- UR-015: Identify repetitive task patterns
- UR-016: Maintain common task sequences
- UR-017: Suggest automation for patterns
- UR-018: Suggest templates after 3+ repetitions
- UR-019: Offer to execute learned patterns
- UR-020: Detect significant pattern variations
- UR-021: Merge overlapping patterns

### 4. Learning Metrics Tracking

**Purpose**: Monitor system learning effectiveness and quality.

**Schema Version**: 2.0.0

**Metric Categories**:
- `adoption`: Feature usage and interaction metrics
- `effectiveness`: Accuracy, relevance, and application rates
- `learning`: New patterns, preferences, and decisions
- `quality`: Memory integrity and consistency scores
- `performance`: Retrieval and synchronization times
- `regulatory_coverage`: Domain coverage and monitoring

**Quality Indicators**:
```json
{
  "memory_integrity": 100,
  "data_consistency_score": 100,
  "backup_success_rate": 100,
  "schema_validations": {"passed": 0, "failed": 0}
}
```

## Operations Guide

### Memory Operations

#### Storing a Regulatory Decision

```python
# Via /aria command or agent interaction
decision = {
    "question": "Is SaMD subject to FDA 510(k) for bug fixes?",
    "answer": "Bug fixes not affecting safety...",
    "regulation": "21 CFR 807.81(a)",
    "regulatory_domain": "FDA"
}
memory_manager.store_decision(decision)
```

#### Retrieving Relevant Decisions

```python
# Query by question similarity
decisions = memory_manager.retrieve_decisions(
    query="Software updates for medical devices",
    threshold=0.7
)
```

#### Learning Company Preferences

```python
# Extract from user interactions
preference = {
    "category": "formatting",
    "key": "date_format",
    "value": "DD/MM/YYYY",
    "source": "user_modification"
}
memory_manager.learn_preference(preference)
```

#### Detecting Task Patterns

```python
# Analyze task sequences
pattern = pattern_detector.analyze_sequence([
    {"action": "schedule_audit", "agent": "orchestrator"},
    {"action": "generate_agenda", "agent": "expert-audit"}
])
```

### Notion Integration

#### Backup Configuration

```python
# Configure Notion backup
notion_backup = NotionMemoryBackup(
    database_id="...",  # ARIA Memory Database
    api_key="...",
    sync_interval_seconds=300
)
```

#### Sync Operation

```python
# Sync memory to Notion
notion_backup.sync_all([
    "regulatory-decisions-enhanced.json",
    "company-preferences-enhanced.json",
    "task-patterns-enhanced.json",
    "learning-metrics-enhanced.json"
])
```

## VCS Integration

### Git Configuration

```bash
# .gitattributes for memory files
*.json merge=union
*.json-language merge=union

# Prevent merge conflicts with union merge strategy
git config merge.union.name "Union Merge"
git config merge.union.driver "union %O %A %B"
```

### Team Synchronization

1. **Pull Before Session**: Always pull latest memory changes
2. **Commit After Learning**: Commit new decisions/preferences
3. **Resolve Conflicts**: Use union merge for memory arrays
4. **Review Periodically**: Weekly review of accumulated memory

## Quality Assurance

### Schema Validation

```bash
# Validate JSON schemas
ajv validate \
  -s schemas/regulatory-decisions-schema.json \
  -d regulatory-decisions-enhanced.json
```

### Integrity Checks

```python
# Memory integrity check
integrity = memory_manager.check_integrity()
assert integrity.score >= 95, "Memory integrity below threshold"
```

### Consistency Validation

```python
# Validate cross-references
assert memory_manager.validate_references()
assert memory_manager.check_conflicts()
```

## Performance Optimization

### Caching Strategy

- **LRU Cache**: Cache recent decision retrievals (max 100 entries)
- **Index Cache**: Maintain in-memory indexes for fast lookup
- **Pattern Cache**: Cache detected patterns during session

### Sync Strategy

- **Incremental Sync**: Sync only changed records
- **Batch Operations**: Batch Notion API calls for efficiency
- **Conflict Resolution**: Last-write-wins with audit trail

## Security and Privacy

### Data Protection

- **Company Segregation**: Company-specific decisions tagged and isolated
- **Access Control**: Notion permissions restrict access by team
- **Audit Trail**: All memory modifications tracked with timestamp and user

### Sensitive Information

- **No Secrets**: Never store credentials or API keys in memory
- **Obfuscation**: Personal identifiers obfuscated in metrics
- **Retention**: 365-day data retention with manual archive

## Monitoring and Alerts

### Health Metrics

```python
# Monitor memory system health
health = {
    "memory_integrity": learning_metrics["quality"]["memory_integrity"],
    "backup_success": learning_metrics["quality"]["backup_success_rate"],
    "sync_status": notion_backup.last_sync_status
}
```

### Alert Conditions

- Memory integrity < 95%
- Backup failure > 3 consecutive attempts
- Schema validation failure
- Merge conflict requiring resolution

## Future Enhancements

### Phase 6+ Roadmap

- **Vector Search**: Semantic similarity search for decisions
- **Machine Learning**: Pattern prediction and proactive suggestions
- **Cross-Team Learning**: Share anonymized patterns across companies
- **Regulatory API**: Real-time regulation change monitoring

## Troubleshooting

### Common Issues

**Issue**: Merge conflicts in memory files
**Solution**: Use `git merge-file --union` for array merging

**Issue**: Notion sync failures
**Solution**: Check API rate limits, implement exponential backoff

**Issue**: Memory corruption
**Solution**: Restore from Notion backup, validate schemas

### Debug Mode

```python
# Enable debug logging
import logging
logging.getLogger("aria.memory").setLevel(logging.DEBUG)
```

## References

- SPEC-ARIA-005: Phase 5 Requirements
- MoAI-ADK Memory System: Persistent memory architecture
- Notion MCP: Knowledge base integration
- VALID Framework: Quality validation requirements

---

**Version**: 2.0.0
**Last Updated**: 2026-02-09
**Status**: Active
