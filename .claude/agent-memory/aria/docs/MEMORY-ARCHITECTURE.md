# ARIA Agent Memory System Architecture

## Overview

The ARIA Agent Memory System implements SPEC-ARIA-005 requirements for persistent cross-session learning, enabling regulatory intelligence assistants to remember decisions, preferences, and patterns across sessions.

## Design Principles

### 1. Separation of Concerns

Each memory component has a specific purpose:
- **Regulatory Decisions**: Store regulatory interpretations with citations
- **Company Preferences**: Learn formatting and terminology preferences
- **Task Patterns**: Identify repetitive workflow sequences
- **Learning Metrics**: Track system effectiveness and quality

### 2. Progressive Enhancement

- **Phase 1** (Current): Basic storage and retrieval
- **Phase 2**: Vector similarity search for decisions
- **Phase 3**: Machine learning for pattern prediction
- **Phase 4**: Cross-team learning (anonymized)

### 3. Data Integrity

- Schema validation for all memory files
- Atomic writes to prevent corruption
- Git-friendly merge strategies for VCS
- Notion backup for cloud persistence

## Memory Schema

### Regulatory Decision Memory

**File**: `regulatory-decisions-enhanced.json`

**Purpose**: Store regulatory decisions with complete context for reuse.

**Key Features**:
- Decision indexing by regulation, domain, and applicability
- Company-specific flag for segregation
- Confidence scoring for decision quality
- Validity tracking for regulation changes
- Usage statistics for relevance ranking

**Schema Structure**:
```json
{
  "version": "2.0.0",
  "last_updated": "ISO-8601 timestamp",
  "metadata": {
    "total_decisions": "integer",
    "active_decisions": "integer",
    "regulatory_domains": ["FDA", "EU MDR", "MFDS"],
    "company_specific_count": "integer"
  },
  "decisions": [
    {
      "decision_id": "DEC-YYYY-NNN",
      "question": "string",
      "answer": "string",
      "regulation": "string",
      "section": "string",
      "rationale": "string",
      "applicability": ["string"],
      "regulatory_domain": "FDA|EU MDR|MFDS",
      "company_specific": "boolean",
      "confidence_score": "0.0-1.0",
      "valid_until": "ISO-8601|null",
      "created_at": "ISO-8601",
      "last_reviewed": "ISO-8601",
      "created_by": "string",
      "usage_count": "integer",
      "last_used_at": "ISO-8601|null",
      "tags": ["string"],
      "related_decisions": ["decision_id"],
      "evidence_citations": ["string"],
      "is_valid": "boolean"
    }
  ],
  "index": {
    "by_regulation": {},
    "by_domain": {},
    "by_applicability": {}
  }
}
```

**Use Cases (UR-001 to UR-007)**:
- UR-001: Persistent memory across sessions
- UR-002: Store rationale, regulations, applicability
- UR-003: Organize by regulatory domain
- UR-004: Prompt to store during drafting
- UR-005: Retrieve relevant past decisions
- UR-006: Flag obsolete decisions
- UR-007: Tag company-specific interpretations

### Company Preference Learning

**File**: `company-preferences-enhanced.json`

**Purpose**: Learn and apply company-specific preferences for documents and workflows.

**Key Features**:
- Multi-company support with segregation
- Preference categories for different aspects
- Suggestion history with feedback tracking
- Conflict detection and resolution
- Global standards for regulatory domains

**Schema Structure**:
```json
{
  "version": "2.0.0",
  "last_updated": "ISO-8601 timestamp",
  "metadata": {
    "total_companies": "integer",
    "active_companies": "integer",
    "preference_categories": ["string"]
  },
  "companies": {
    "company_id": {
      "company_id": "string",
      "company_name": "string",
      "preferences": {
        "formatting": {
          "document_template": "string",
          "date_format": "string",
          "number_format": "string",
          "language": "string",
          "terminology_style": "string",
          "citation_style": "string",
          "heading_style": "string"
        },
        "terminology": {
          "device": "string",
          "manufacturer": "string",
          "intended_use": "string",
          "indications_for_use": "string",
          "contraindications": "string",
          "adverse_events": "string",
          "risk_analysis": "string",
          "clinical_evaluation": "string"
        },
        "templates": {
          "510k": "string",
          "technical_file": "string",
          "cer": "string",
          "psur": "string",
          "capa": "string",
          "internal_audit": "string"
        },
        "regulatory_framework": {
          "primary": "FDA|EU MDR|MFDS",
          "secondary": ["string"],
          "notified_body": "string|null",
          "iec_standards": ["string"],
          "quality_standard": "string"
        },
        "workflow": {
          "default_reviewer": "string|null",
          "approval_required": "boolean",
          "version_control": "git|svn|other",
          "document_lifecycle": "string",
          "signature_requirements": "string"
        }
      },
      "suggestion_history": {
        "accepted": [{"timestamp": "...", ...}],
        "rejected": [{"timestamp": "...", "reason": "..."}],
        "modified": [{"timestamp": "...", ...}]
      },
      "created_at": "ISO-8601",
      "updated_at": "ISO-8601",
      "preference_conflicts": [{"conflict_id": "...", ...}],
      "user_overrides": {}
    }
  },
  "global_standards": {
    "citation_format": "string",
    "date_format_standards": {
      "FDA": "MM/DD/YYYY",
      "EU MDR": "DD/MM/YYYY",
      "MFDS": "YYYY-MM-DD"
    },
    "number_format_standards": {
      "FDA": "1,234.56",
      "EU MDR": "1.234,56",
      "MFDS": "1,234.56"
    }
  }
}
```

**Use Cases (UR-008 to UR-014)**:
- UR-008: Learn company-specific preferences
- UR-009: Maintain preferred templates
- UR-010: Track approved vs rejected suggestions
- UR-011: Record rejection reasons
- UR-012: Learn from user modifications
- UR-013: Detect preference conflicts
- UR-014: Flag user vs company standard conflicts

### Repetitive Task Pattern Recognition

**File**: `task-patterns-enhanced.json`

**Purpose**: Identify and automate repetitive RA/QA workflow sequences.

**Key Features**:
- Pattern detection from task sequences
- Confidence scoring based on occurrences
- Pattern library for common workflows
- Automation threshold configuration
- Pattern merging for generalization

**Schema Structure**:
```json
{
  "version": "2.0.0",
  "last_updated": "ISO-8601 timestamp",
  "metadata": {
    "total_patterns": "integer",
    "high_confidence_patterns": "integer",
    "automatable_patterns": "integer",
    "pattern_tags": ["string"]
  },
  "patterns": [
    {
      "id": "PAT-YYYY-NNN",
      "name": "string",
      "description": "string",
      "occurrence_count": "integer >= 3",
      "confidence": "0.0-1.0",
      "steps": [
        {
          "order": "integer",
          "action": "string",
          "description": "string",
          "agent": "string"
        }
      ],
      "estimated_duration_hours": "number",
      "automatable": "boolean",
      "created_at": "ISO-8601",
      "updated_at": "ISO-8601",
      "last_suggested_at": "ISO-8601|null",
      "suggestion_count": "integer",
      "tags": ["string"],
      "merged_from": ["pattern_id"],
      "is_valid": "boolean"
    }
  ],
  "pattern_library": {
    "common_sequences": [
      {
        "id": "PAT-XXX",
        "name": "string",
        "description": "string",
        "occurrence_threshold": "integer",
        "steps": [...],
        "estimated_duration_hours": "number",
        "automatable": "boolean"
      }
    ]
  },
  "learning_state": {
    "detection_enabled": "boolean",
    "automation_threshold": "integer",
    "confidence_threshold": "0.0-1.0",
    "pattern_variations_allowed": "0.0-1.0"
  }
}
```

**Use Cases (UR-015 to UR-021)**:
- UR-015: Identify repetitive task patterns
- UR-016: Maintain common task sequences
- UR-017: Suggest automation for patterns
- UR-018: Suggest templates after 3+ repetitions
- UR-019: Offer to execute learned patterns
- UR-020: Detect significant pattern variations
- UR-021: Merge overlapping patterns

### Learning Metrics Tracking

**File**: `learning-metrics-enhanced.json`

**Purpose**: Monitor system learning effectiveness and quality indicators.

**Key Features**:
- Adoption metrics for feature usage
- Effectiveness metrics for accuracy
- Learning metrics for knowledge accumulation
- Quality metrics for integrity
- Performance metrics for optimization
- Regulatory coverage tracking

**Schema Structure**:
```json
{
  "version": "2.0.0",
  "last_updated": "ISO-8601 timestamp",
  "metadata": {
    "first_tracked": "ISO-8601",
    "tracking_period_days": "integer",
    "data_retention_days": "integer",
    "system_version": "string"
  },
  "adoption": {
    "total_interactions": "integer",
    "unique_sessions": "integer",
    "feature_usage": {
      "regulatory_decisions": {
        "access_count": "integer",
        "contribution_count": "integer",
        "last_accessed": "ISO-8601|null"
      },
      "company_preferences": {...},
      "task_patterns": {
        "suggestions_shown": "integer",
        "suggestions_accepted": "integer",
        "last_suggested": "ISO-8601|null"
      }
    },
    "session_metrics": {
      "avg_session_duration_minutes": "number",
      "most_used_features": ["string"],
      "feature_adoption_rate": "0.0-1.0"
    }
  },
  "effectiveness": {
    "pattern_accuracy": {
      "correct": "integer",
      "incorrect": "integer",
      "ignored": "integer"
    },
    "decision_relevance": {
      "relevant": "integer",
      "not_relevant": "integer",
      "neutral": "integer"
    },
    "preference_application": {
      "applied": "integer",
      "overridden": "integer",
      "conflicts": "integer"
    },
    "automation_savings": {
      "hours_saved": "number",
      "tasks_automated": "integer",
      "patterns_recognized": "integer"
    }
  },
  "learning": {
    "new_patterns_learned": "integer",
    "preferences_extracted": "integer",
    "decisions_stored": "integer",
    "confidence_updates": "integer",
    "regulation_changes_processed": "integer",
    "knowledge_base_updates": "integer"
  },
  "quality": {
    "memory_integrity": "0-100",
    "schema_validations": {
      "passed": "integer",
      "failed": "integer"
    },
    "merge_conflicts_resolved": "integer",
    "data_consistency_score": "0-100",
    "backup_success_rate": "0-100"
  },
  "performance": {
    "avg_decision_retrieval_time_ms": "integer",
    "avg_pattern_detection_time_ms": "integer",
    "avg_preference_application_time_ms": "integer",
    "notion_sync_success_rate": "0-100",
    "cache_hit_rate": "0.0-1.0"
  },
  "regulatory_coverage": {
    "domains_active": ["FDA", "EU MDR", "MFDS"],
    "decisions_by_domain": {
      "FDA": "integer",
      "EU MDR": "integer",
      "MFDS": "integer"
    },
    "regulation_change_monitoring": {
      "last_check": "ISO-8601|null",
      "changes_detected": "integer",
      "decisions_flagged": "integer"
    }
  },
  "user_feedback": {
    "total_suggestions": "integer",
    "accepted_suggestions": "integer",
    "rejected_suggestions": "integer",
    "modified_suggestions": "integer",
    "average_satisfaction_score": "number|null"
  }
}
```

## Memory Operations

### Storage Operations

1. **Store Regulatory Decision**
   - Generate unique decision ID
   - Validate required fields
   - Update search indexes
   - Track usage statistics

2. **Learn Company Preference**
   - Extract from user modifications
   - Validate preference category
   - Record suggestion feedback
   - Detect conflicts

3. **Detect Task Pattern**
   - Analyze task sequences
   - Compare with existing patterns
   - Calculate confidence score
   - Suggest automation

### Retrieval Operations

1. **Retrieve Regulatory Decisions**
   - Keyword search in questions/answers
   - Filter by regulatory domain
   - Sort by relevance score
   - Update usage statistics

2. **Apply Company Preferences**
   - Load company preferences
   - Apply to document generation
   - Track application success
   - Record overrides

3. **Suggest Pattern Automation**
   - Recognize task sequences
   - Match to known patterns
   - Calculate automation benefit
   - Present suggestion

### Maintenance Operations

1. **Validate Memory Integrity**
   - Schema validation
   - Cross-reference validation
   - Consistency checks
   - Error reporting

2. **Flag Obsolete Decisions**
   - Monitor regulation changes
   - Flag affected decisions
   - Update validity flags
   - Notify users

3. **Merge Patterns**
   - Detect overlapping patterns
   - Validate merge compatibility
   - Create generalized template
   - Archive original patterns

## Integration Points

### Notion MCP Integration

**Purpose**: Cloud backup and knowledge base integration.

**Operations**:
- Sync memory files to Notion database
- Query decisions from knowledge base
- Cross-reference with regulatory documents
- Backup and restore functionality

**Database Schema**:
```
ARIA Memory Database
├── Regulatory Decisions (pages)
│   ├── Decision ID (title)
│   ├── Question (rich text)
│   ├── Answer (rich text)
│   ├── Regulation (rich text)
│   ├── Regulatory Domain (select)
│   ├── Company Specific (checkbox)
│   ├── Confidence Score (number)
│   ├── Valid Until (date)
│   ├── Created At (date)
│   ├── Is Valid (checkbox)
│   └── Tags (multi-select)
├── Company Preferences (pages)
├── Task Patterns (pages)
└── Learning Metrics (pages)
```

### Git Integration

**Purpose**: VCS-based team synchronization.

**Configuration**:
```bash
# .gitattributes
*.json merge=union
*.json-language merge=union

# Union merge strategy
git config merge.union.name "Union Merge"
git config merge.union.driver "union %O %A %B"
```

**Workflow**:
1. Pull latest changes before session
2. Commit new decisions/preferences after learning
3. Resolve conflicts with union merge
4. Push to share with team

### Agent Integration

**Memory Access from Agents**:

```python
# In agent code
from aria.memory import MemoryManager

memory = MemoryManager()

# Store decision
decision_id = memory.store_decision({
    'question': 'Is SaMD subject to FDA 510(k)?',
    'answer': 'Bug fixes not affecting safety...',
    'regulation': '21 CFR 807.81(a)',
    'regulatory_domain': 'FDA'
})

# Retrieve decisions
decisions = memory.retrieve_decisions(
    query='Software updates for medical devices',
    threshold=0.7
)

# Learn preference
memory.learn_preference(
    company_id='acme-corp',
    category='formatting',
    key='date_format',
    value='DD/MM/YYYY'
)
```

## Performance Considerations

### Caching Strategy

- **LRU Cache**: Recent decision retrievals (max 100 entries)
- **Index Cache**: In-memory indexes for fast lookup
- **Pattern Cache**: Detected patterns during session

### Sync Strategy

- **Incremental Sync**: Only changed records
- **Batch Operations**: Batch Notion API calls
- **Conflict Resolution**: Last-write-wins with audit trail

### Scalability

- **Memory Size**: Support up to 10,000 decisions per company
- **Query Performance**: < 100ms for decision retrieval
- **Sync Performance**: < 30 seconds for full sync

## Security and Privacy

### Data Protection

- **Company Segregation**: Tag company-specific data
- **Access Control**: Notion permissions by team
- **Audit Trail**: All modifications tracked

### Sensitive Information

- **No Secrets**: Never store credentials
- **Obfuscation**: Personal identifiers obfuscated
- **Retention**: 365-day retention with archive

## Future Enhancements

### Phase 6+ Roadmap

1. **Vector Search**: Semantic similarity for decisions
2. **Machine Learning**: Pattern prediction
3. **Cross-Team Learning**: Anonymized pattern sharing
4. **Regulatory API**: Real-time monitoring

## Troubleshooting

### Common Issues

**Issue**: Merge conflicts in memory files
**Solution**: Use `git merge-file --union` for arrays

**Issue**: Notion sync failures
**Solution**: Check API limits, implement backoff

**Issue**: Memory corruption
**Solution**: Restore from Notion backup

---

**Version**: 2.0.0
**Last Updated**: 2026-02-09
**Status**: Active
