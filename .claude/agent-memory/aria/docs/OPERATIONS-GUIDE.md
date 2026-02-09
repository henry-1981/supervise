# ARIA Memory System Operations Guide

## Quick Start

### Installation

The Memory System is automatically installed with ARIA. No additional setup required.

### Memory Location

```
.claude/agent-memory/aria/
├── regulatory-decisions-enhanced.json
├── company-preferences-enhanced.json
├── task-patterns-enhanced.json
└── learning-metrics-enhanced.json
```

### Basic Usage

#### Store a Regulatory Decision

```bash
cd /Users/hb/Project/Agent-Skills
python .claude/agent-memory/aria/operations/memory-manager.py store-decision \
  --question "Is SaMD subject to FDA 510(k) for minor bug fixes?" \
  --answer "Bug fixes that do not affect device safety or effectiveness are typically not subject to 510(k) submission requirements." \
  --regulation "21 CFR 807.81(a)" \
  --domain "FDA" \
  --confidence 0.95
```

#### Retrieve Relevant Decisions

```bash
python .claude/agent-memory/aria/operations/memory-manager.py retrieve-decisions \
  --query "Software updates for medical devices" \
  --threshold 0.7 \
  --domain "FDA"
```

#### Learn Company Preference

```bash
python .claude/agent-memory/aria/operations/memory-manager.py learn-preference \
  --company-id "acme-corp" \
  --category "formatting" \
  --key "date_format" \
  --value "DD/MM/YYYY"
```

#### Record Suggestion Feedback

```bash
python .claude/agent-memory/aria/operations/memory-manager.py record-feedback \
  --company-id "acme-corp" \
  --suggestion-type "template_selection" \
  --feedback "accepted"
```

#### Validate Memory Files

```bash
python .claude/agent-memory/aria/operations/memory-manager.py validate --all
```

## Memory Operations

### Regulatory Decision Memory

#### Store Decision

**Command**: `store-decision`

**Required Arguments**:
- `--question`: Regulatory question asked
- `--answer`: Decision provided
- `--regulation`: Source regulation citation

**Optional Arguments**:
- `--section`: Specific section/article
- `--rationale`: Decision rationale
- `--domain`: Regulatory domain (FDA, EU MDR, MFDS)
- `--company-specific`: Flag for company-specific interpretation
- `--confidence`: Confidence score (0-1, default: 0.8)

**Example**:
```bash
python .claude/agent-memory/aria/operations/memory-manager.py store-decision \
  --question "What is the timeline for FDA 510(k) submission?" \
  --answer "FDA typically provides substantive review within 90 calendar days for traditional 510(k) submissions." \
  --regulation "21 CFR 807.100" \
  --section "807.100" \
  --rationale "FDA statutory requirements for 510(k) review timelines" \
  --domain "FDA" \
  --confidence 0.9
```

#### Retrieve Decisions

**Command**: `retrieve-decisions`

**Required Arguments**:
- `--query`: Search query

**Optional Arguments**:
- `--threshold`: Relevance threshold (0-1, default: 0.7)
- `--domain`: Filter by regulatory domain

**Example**:
```bash
python .claude/agent-memory/aria/operations/memory-manager.py retrieve-decisions \
  --query "510k timeline submission requirements" \
  --threshold 0.6 \
  --domain "FDA"
```

#### Flag Obsolete Decisions

When regulations change, flag affected decisions:

```python
from aria.memory import MemoryManager

manager = MemoryManager()
flagged = manager.flag_obsolete_decisions(
    regulation="21 CFR 807.81(a)",
    change_date="2026-06-01T00:00:00Z"
)
print(f"Flagged {len(flagged)} decisions as obsolete")
```

### Company Preference Learning

#### Learn Preference

**Command**: `learn-preference`

**Required Arguments**:
- `--category`: Preference category
- `--key`: Preference key
- `--value`: Preference value

**Optional Arguments**:
- `--company-id`: Company identifier (default: "default")

**Categories**:
- `formatting`: Document structure, dates, numbers
- `terminology`: Term mappings
- `templates`: Template preferences
- `regulatory_framework`: Framework settings
- `workflow`: Process settings

**Examples**:

```bash
# Formatting preference
python .claude/agent-memory/aria/operations/memory-manager.py learn-preference \
  --company-id "acme-corp" \
  --category "formatting" \
  --key "citation_style" \
  --value "regulatory-standard"

# Template preference
python .claude/agent-memory/aria/operations/memory-manager.py learn-preference \
  --category "templates" \
  --key "510k" \
  --value "special-510k"

# Terminology preference
python .claude/agent-memory/aria/operations/memory-manager.py learn-preference \
  --category "terminology" \
  --key "device" \
  --value "medical apparatus"
```

#### Record Feedback

**Command**: `record-feedback`

**Required Arguments**:
- `--suggestion-type`: Type of suggestion
- `--feedback`: Feedback (accepted, rejected, modified)

**Optional Arguments**:
- `--company-id`: Company identifier
- `--reason`: Reason for rejection

**Examples**:

```bash
# Accepted suggestion
python .claude/agent-memory/aria/operations/memory-manager.py record-feedback \
  --company-id "acme-corp" \
  --suggestion-type "template_selection" \
  --feedback "accepted"

# Rejected suggestion with reason
python .claude/agent-memory/aria/operations/memory-manager.py record-feedback \
  --suggestion-type "terminology_change" \
  --feedback "rejected" \
  --reason "Company-specific term required"

# Modified suggestion
python .claude/agent-memory/aria/operations/memory-manager.py record-feedback \
  --feedback "modified" \
  --suggestion-type "date_format"
```

### Task Pattern Recognition

#### Detect Pattern

```python
from aria.memory import PatternDetector

detector = PatternDetector()

# Analyze session log
patterns = detector.analyze_session_log(session_log_data)

# Suggest automation
suggestion = detector.suggest_automation(task_sequence)
if suggestion:
    print(f"Pattern detected: {suggestion['pattern_name']}")
    print(f"Automatable: {suggestion['automatable']}")
    print(f"Estimated savings: {suggestion['estimated_duration_hours']} hours")
```

#### Merge Patterns

**Command**: `merge` (via pattern-detector.py)

**Required Arguments**:
- `--pattern-ids`: Comma-separated pattern IDs

**Example**:
```bash
python .claude/agent-memory/aria/operations/pattern-detector.py merge \
  --pattern-ids "PAT-2026-001,PAT-2026-002"
```

#### Get Pattern Statistics

```bash
python .claude/agent-memory/aria/operations/pattern-detector.py stats
```

## Notion Backup Operations

### Sync All Memory Files

```bash
python .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

### Sync Specific File Types

```bash
# Sync only decisions
python .claude/agent-memory/aria/operations/notion-backup.py sync-all \
  --types decisions

# Sync decisions and preferences
python .claude/agent-memory/aria/operations/notion-backup.py sync-all \
  --types decisions preferences
```

### Sync Individual Components

```bash
# Sync regulatory decisions
python .claude/agent-memory/aria/operations/notion-backup.py sync-decisions

# Sync company preferences
python .claude/agent-memory/aria/operations/notion-backup.py sync-preferences

# Sync task patterns
python .claude/agent-memory/aria/operations/notion-backup.py sync-patterns

# Sync learning metrics
python .claude/agent-memory/aria/operations/notion-backup.py sync-metrics
```

### Check Sync Status

```bash
python .claude/agent-memory/aria/operations/notion-backup.py status
```

### Restore from Backup

```bash
python .claude/agent-memory/aria/operations/notion-backup.py restore-backup \
  --output-dir /path/to/restore
```

## Validation and Maintenance

### Validate Memory Files

```bash
# Validate all memory files
python .claude/agent-memory/aria/operations/memory-manager.py validate --all
```

**Output**:
```
Validation Results:
Decisions: VALID
Preferences: VALID
Patterns: VALID
Metrics: VALID
```

### Check Memory Integrity

```python
from aria.memory import MemoryManager

manager = MemoryManager()
integrity = manager.check_integrity()
print(f"Memory Integrity: {integrity.score}%")
print(f"Issues: {integrity.issues}")
```

### Resolve Merge Conflicts

When Git merge conflicts occur in memory files:

```bash
# Use union merge for arrays
git merge-file --union \
  .claude/agent-memory/aria/regulatory-decisions-enhanced.json
```

### Archive Old Data

Archive decisions older than 365 days:

```python
from aria.memory import MemoryManager
from datetime import datetime, timedelta

manager = MemoryManager()
cutoff_date = datetime.now() - timedelta(days=365)

# Archive old decisions
archived = manager.archive_old_decisions(cutoff_date)
print(f"Archived {len(archived)} decisions")
```

## Performance Monitoring

### Check Learning Metrics

```python
import json

with open('.claude/agent-memory/aria/learning-metrics-enhanced.json', 'r') as f:
    metrics = json.load(f)

print("Adoption Metrics:")
print(f"  Total Interactions: {metrics['adoption']['total_interactions']}")
print(f"  Feature Usage: {metrics['adoption']['feature_usage']}")

print("\nEffectiveness Metrics:")
print(f"  Pattern Accuracy: {metrics['effectiveness']['pattern_accuracy']}")
print(f"  Decision Relevance: {metrics['effectiveness']['decision_relevance']}")

print("\nQuality Metrics:")
print(f"  Memory Integrity: {metrics['quality']['memory_integrity']}%")
print(f"  Backup Success Rate: {metrics['quality']['backup_success_rate']}%")
```

### Monitor Performance

```python
from aria.memory import MemoryManager

manager = MemoryManager()
perf = manager.get_performance_metrics()

print("Performance Metrics:")
print(f"  Avg Decision Retrieval: {perf['avg_decision_retrieval_time_ms']}ms")
print(f"  Avg Pattern Detection: {perf['avg_pattern_detection_time_ms']}ms")
print(f"  Notion Sync Success: {perf['notion_sync_success_rate']}%")
print(f"  Cache Hit Rate: {perf['cache_hit_rate']:.2%}")
```

## Troubleshooting

### Common Issues

#### Issue: Merge Conflicts

**Symptom**: Git merge conflicts in memory files

**Solution**:
```bash
# Use union merge strategy
git config merge.union.name "Union Merge"
git config merge.union.driver "union %O %A %B"

# Re-merge
git merge --abort
git merge feature-branch
```

#### Issue: Notion Sync Failures

**Symptom**: Sync operations fail with API errors

**Solution**:
```bash
# Check environment variable
echo $NOTION_ARIA_MEMORY_DB

# Verify Notion MCP is running
# (Check Claude Code MCP server status)

# Retry with exponential backoff
python .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

#### Issue: Memory Corruption

**Symptom**: JSON parsing errors or missing data

**Solution**:
```bash
# Validate memory files
python .claude/agent-memory/aria/operations/memory-manager.py validate --all

# Restore from Notion backup
python .claude/agent-memory/aria/operations/notion-backup.py restore-backup
```

#### Issue: Slow Performance

**Symptom**: Memory operations take > 1 second

**Solution**:
```python
# Enable caching
from aria.memory import MemoryManager

manager = MemoryManager()
manager.enable_cache(max_size=100)

# Clear cache if needed
manager.clear_cache()
```

### Debug Mode

Enable debug logging:

```python
import logging
logging.getLogger('aria.memory').setLevel(logging.DEBUG)

# Now operations will print detailed logs
manager = MemoryManager()
decisions = manager.retrieve_decisions("query")
```

### Health Check

Run comprehensive health check:

```python
from aria.memory import MemoryManager, PatternDetector, NotionBackup

manager = MemoryManager()
detector = PatternDetector()
backup = NotionMemoryBackup()

# Validate memory
validation = manager.validate_all()
print(f"Validation: {validation}")

# Check patterns
stats = detector.get_pattern_statistics()
print(f"Pattern Stats: {stats}")

# Check sync status
status = backup.get_sync_status()
print(f"Sync Status: {status}")
```

## Best Practices

### 1. Regular Backups

Sync to Notion after each session:

```bash
python .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

### 2. Version Control

Commit memory changes regularly:

```bash
git add .claude/agent-memory/aria/
git commit -m "Update memory with new decisions and preferences"
```

### 3. Validation

Validate memory files before committing:

```bash
python .claude/agent-memory/aria/operations/memory-manager.py validate --all
```

### 4. Conflict Prevention

Pull latest changes before starting work:

```bash
git pull origin main
```

### 5. Regular Maintenance

Archive old data quarterly:

```python
from aria.memory import MemoryManager
from datetime import datetime, timedelta

manager = MemoryManager()
cutoff = datetime.now() - timedelta(days=90)
manager.archive_old_decisions(cutoff)
```

## API Reference

### MemoryManager Class

**Methods**:
- `store_decision(decision_data: Dict) -> str`
- `retrieve_decisions(query: str, threshold: float, domain: str) -> List[Dict]`
- `flag_obsolete_decisions(regulation: str, change_date: str) -> List[str]`
- `learn_preference(company_id: str, category: str, key: str, value: Any) -> bool`
- `record_suggestion_feedback(company_id: str, suggestion_type: str, feedback: str, reason: str) -> bool`
- `validate_all() -> Dict[str, Any]`

### PatternDetector Class

**Methods**:
- `analyze_session_log(session_log: List[Dict]) -> List[Dict]`
- `suggest_automation(task_sequence: List[Dict]) -> Optional[Dict]`
- `merge_patterns(pattern_ids: List[str]) -> Optional[Dict]`
- `get_pattern_statistics() -> Dict[str, Any]`

### NotionMemoryBackup Class

**Methods**:
- `sync_all(file_types: Optional[List[str]]) -> Dict[str, Any]`
- `sync_decisions() -> Dict[str, Any]`
- `sync_preferences() -> Dict[str, Any]`
- `sync_patterns() -> Dict[str, Any]`
- `sync_metrics() -> Dict[str, Any]`
- `restore_backup(output_dir: Optional[Path]) -> bool`
- `get_sync_status() -> Dict[str, Any]`

## Support

For issues or questions:
1. Check this operations guide
2. Review troubleshooting section
3. Check SPEC-ARIA-005 documentation
4. Contact ARIA development team

---

**Version**: 2.0.0
**Last Updated**: 2026-02-09
**Status**: Active
