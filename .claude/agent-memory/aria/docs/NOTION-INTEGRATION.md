# ARIA Notion Integration Guide

## Overview

The ARIA Agent Memory System integrates with Notion via the Notion MCP server for cloud backup, knowledge base connectivity, and team collaboration.

## Prerequisites

### 1. Notion MCP Server

Ensure Notion MCP server is configured in `.mcp.json`:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"]
    }
  }
}
```

### 2. Notion Database Setup

Create a Notion database with the following properties:

#### Regulatory Decisions Database

| Property | Type | Required |
|----------|------|----------|
| Decision ID | Title | Yes |
| Question | Text | Yes |
| Answer | Text | Yes |
| Regulation | Text | Yes |
| Section | Text | No |
| Regulatory Domain | Select | Yes |
| Company Specific | Checkbox | Yes |
| Confidence Score | Number | Yes |
| Valid Until | Date | No |
| Created At | Date | Yes |
| Is Valid | Checkbox | Yes |
| Tags | Multi-select | No |

#### Company Preferences Database

| Property | Type | Required |
|----------|------|----------|
| Company ID | Title | Yes |
| Company Name | Text | Yes |
| Type | Select | Yes |
| Category | Text | No |
| Key | Text | No |
| Value | Text | No |
| Last Updated | Date | Yes |

#### Task Patterns Database

| Property | Type | Required |
|----------|------|----------|
| Pattern ID | Title | Yes |
| Pattern Name | Text | Yes |
| Description | Text | No |
| Type | Select | Yes |
| Occurrence Count | Number | Yes |
| Confidence | Number | Yes |
| Automatable | Checkbox | Yes |
| Created At | Date | Yes |
| Tags | Multi-select | No |

### 3. Environment Configuration

Set the Notion database ID environment variable:

```bash
# In .claude/settings.local.json or shell profile
export NOTION_ARIA_MEMORY_DB="your-database-id-here"
```

## Integration Architecture

### Sync Flow

```
Local Memory Files
       ↓
   JSON Validation
       ↓
   Transform to Notion Format
       ↓
   MCP Tool Call (notion-create-pages)
       ↓
   Notion Database
       ↓
   Sync Status Update
```

### Backup Flow

```
Notion Database
       ↓
   Query Pages (notion-query)
       ↓
   Transform to Memory Format
       ↓
   Validate Schema
       ↓
   Write Local Files
       ↓
   Restore Complete
```

## Operations

### Initial Setup

1. **Create Notion Database**
   - Create a new database in your Notion workspace
   - Add properties as specified above
   - Copy database ID from URL

2. **Configure Environment**
   ```bash
   export NOTION_ARIA_MEMORY_DB="abcd1234-5678-90ef-ghij-klmnopqrstuv"
   ```

3. **Test Connection**
   ```bash
   python .claude/agent-memory/aria/operations/notion-backup.py status
   ```

### Sync Operations

#### Full Sync

Sync all memory components to Notion:

```bash
python .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

**Output**:
```
Sync Results:
Duration: 2.34 seconds
Total: 5
Synced: 5
Failed: 0

regulatory-decisions:
  Total: 1
  Synced: 1
  Failed: 0

company-preferences:
  Total: 1
  Synced: 1
  Failed: 0

task-patterns:
  Total: 0
  Synced: 0
  Failed: 0

learning-metrics:
  Total: 1
  Synced: 1
  Failed: 0
```

#### Selective Sync

Sync specific components:

```bash
# Sync only decisions
python .claude/agent-memory/aria/operations/notion-backup.py sync-decisions

# Sync decisions and preferences
python .claude/agent-memory/aria/operations/notion-backup.py sync-all \
  --types decisions preferences
```

#### Automated Sync

Configure automated sync via hooks:

```bash
# .claude/hooks/post-session-sync.sh
#!/bin/bash
cd /Users/hb/Project/Agent-Skills
python .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionEnd": [{
      "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/post-session-sync.sh\"",
      "timeout": 60
    }]
  }
}
```

### Restore Operations

#### Full Restore

Restore all memory from Notion:

```bash
python .claude/agent-memory/aria/operations/notion-backup.py restore-backup
```

#### Selective Restore

Restore specific components to directory:

```bash
python .claude/agent-memory/aria/operations/notion-backup.py restore-backup \
  --output-dir /path/to/restore
```

## Query Operations

### Query Decisions

Query Notion for specific decisions:

```python
from aria.memory import NotionMemoryBackup

backup = NotionMemoryBackup()

# Query by regulatory domain
decisions = backup.query_decisions(domain="FDA")

# Query by regulation
decisions = backup.query_decisions(regulation="21 CFR 807.81(a)")

# Query by tags
decisions = backup.query_decisions(tags=["SaMD", "510k-exemption"])
```

### Query Preferences

Query company preferences:

```python
# Query by company ID
preferences = backup.query_preferences(company_id="acme-corp")

# Query by category
preferences = backup.query_preferences(category="formatting")
```

### Query Patterns

Query task patterns:

```python
# Query high-confidence patterns
patterns = backup.query_patterns(min_confidence=0.7)

# Query automatable patterns
patterns = backup.query_patterns(automatable=True)
```

## Advanced Features

### Cross-Referencing

Link decisions to knowledge base documents:

```python
# Create decision with knowledge base links
decision = {
    "question": "Is SaMD subject to FDA 510(k)?",
    "answer": "Bug fixes not affecting safety...",
    "regulation": "21 CFR 807.81(a)",
    "knowledge_base_links": [
        "https://notion.so/page/samd-guidance",
        "https://notion.so/page/510k-requirements"
    ]
}
```

### Version History

Track decision versions in Notion:

```python
# Update existing decision
backup.update_decision(
    decision_id="DEC-2026-001",
    updates={"answer": "Updated guidance..."},
    create_version=True
)
```

### Team Collaboration

Share memory across team via Notion:

1. **Share Database**: Share Notion database with team members
2. **Set Permissions**: Configure read/write permissions
3. **Sync Regularly**: Each team member syncs before/after sessions
4. **Resolve Conflicts**: Use Notion's version history for conflict resolution

## Error Handling

### API Rate Limits

Notion API has rate limits. The backup system implements exponential backoff:

```python
# Automatic retry with backoff
retry_config = {
    "max_retries": 3,
    "initial_delay": 1.0,
    "backoff_factor": 2.0
}
```

### Connection Failures

Handle connection failures gracefully:

```python
try:
    backup = NotionMemoryBackup()
    results = backup.sync_all()
except ConnectionError as e:
    print(f"Notion connection failed: {e}")
    print("Retrying in 30 seconds...")
    time.sleep(30)
    results = backup.sync_all()
```

### Data Validation

Validate data before sync:

```python
# Validate against schema
validation = backup.validate_before_sync()
if not validation['valid']:
    print(f"Validation errors: {validation['errors']}")
    return False

# Proceed with sync
results = backup.sync_all()
```

## Performance Optimization

### Batch Operations

Batch multiple operations for efficiency:

```python
# Batch create decisions
decisions_to_create = [
    {"question": "...", "answer": "...", ...},
    {"question": "...", "answer": "...", ...},
    {"question": "...", "answer": "...", ...}
]

backup.batch_create_decisions(decisions_to_create)
```

### Incremental Sync

Sync only changed records:

```python
# Sync only decisions created since last sync
backup.sync_decisions_incremental(
    since="2026-02-01T00:00:00Z"
)
```

### Caching

Cache Notion queries for performance:

```python
# Enable caching
backup.enable_cache(ttl=300)  # 5 minutes

# Subsequent queries use cache
decisions = backup.query_decisions(domain="FDA")
```

## Security

### Access Control

Configure Notion permissions:

1. **Database-Level**: Set workspace permissions
2. **Page-Level**: Set individual page permissions
3. **Property-Level**: Use select properties for controlled vocabularies

### Data Protection

- **Sensitive Data**: Avoid storing confidential information
- **API Keys**: Use environment variables, never hardcode
- **Audit Trail**: Enable Notion page history for audit trail

### Encryption

Notion provides:
- Data in transit: TLS 1.2+
- Data at rest: AES-256 encryption
- Additional encryption available via enterprise plans

## Monitoring

### Sync Status

Monitor sync status:

```python
backup = NotionMemoryBackup()
status = backup.get_sync_status()

print(f"Last Sync: {status['last_sync']}")
print(f"Status: {status['last_sync_status']}")
print(f"Files Synced: {status['files_synced']}")
print(f"Errors: {status['sync_errors']}")
```

### Health Checks

Run health checks:

```python
health = backup.check_health()

print(f"Notion Connection: {health['notion_connected']}")
print(f"Database Access: {health['database_accessible']}")
print(f"API Rate Limit: {health['rate_limit_status']}")
print(f"Last Sync Age: {health['last_sync_age_hours']} hours")
```

### Alerts

Configure alerts for sync failures:

```python
# Alert on sync failure
if status['last_sync_status'] == 'failed':
    send_alert(f"Notion sync failed: {status['sync_errors']}")

# Alert on stale data
if health['last_sync_age_hours'] > 24:
    send_alert("Notion sync is stale (>24 hours)")
```

## Troubleshooting

### Common Issues

#### Issue: Database Not Found

**Symptom**: "Database not found" error

**Solution**:
```bash
# Verify database ID
echo $NOTION_ARIA_MEMORY_DB

# Check database permissions in Notion
# Ensure database is shared with integration
```

#### Issue: Rate Limit Exceeded

**Symptom**: "Rate limit exceeded" error

**Solution**:
```python
# Implement exponential backoff
backup = NotionMemoryBackup()
backup.set_retry_config(max_retries=5, backoff_factor=2.0)

# Reduce batch size
backup.sync_decisions(batch_size=10)
```

#### Issue: Property Mismatch

**Symptom**: "Property not found" error

**Solution**:
```bash
# Verify Notion database schema
python .claude/agent-memory/aria/operations/notion-backup.py validate-schema

# Update schema if needed
# Add missing properties to Notion database
```

### Debug Mode

Enable debug logging:

```python
import logging
logging.getLogger('aria.memory.notion').setLevel(logging.DEBUG)

backup = NotionMemoryBackup(debug=True)
results = backup.sync_all()
```

## Best Practices

### 1. Regular Sync

Sync after each session:

```bash
# Add to session end hook
python .claude/agent-memory/aria/operations/notion-backup.py sync-all
```

### 2. Schema Validation

Validate schema before operations:

```python
if backup.validate_schema():
    backup.sync_all()
else:
    print("Schema validation failed")
```

### 3. Error Handling

Implement comprehensive error handling:

```python
try:
    results = backup.sync_all()
    if results['summary']['failed'] > 0:
        handle_failed_sync(results)
except Exception as e:
    handle_sync_error(e)
```

### 4. Monitoring

Monitor sync health:

```python
# Daily health check
health = backup.check_health()
if health['last_sync_age_hours'] > 24:
    alert_team("Sync is stale")
```

### 5. Backup Strategy

Maintain multiple backup layers:

1. **Local**: Git version control
2. **Cloud**: Notion backup
3. **Archive**: Quarterly archives

## API Reference

### NotionMemoryBackup Class

**Constructor**:
```python
NotionMemoryBackup(
    memory_dir: Optional[Path] = None,
    notion_database_id: Optional[str] = None
)
```

**Methods**:
- `sync_all(file_types: Optional[List[str]]) -> Dict[str, Any]`
- `sync_decisions() -> Dict[str, Any]`
- `sync_preferences() -> Dict[str, Any]`
- `sync_patterns() -> Dict[str, Any]`
- `sync_metrics() -> Dict[str, Any]`
- `restore_backup(output_dir: Optional[Path]) -> bool`
- `get_sync_status() -> Dict[str, Any]`
- `query_decisions(**filters) -> List[Dict]`
- `query_preferences(**filters) -> List[Dict]`
- `query_patterns(**filters) -> List[Dict]`
- `validate_schema() -> bool`
- `check_health() -> Dict[str, Any]`

## Support

For Notion integration issues:
1. Check Notion MCP server status
2. Verify database permissions
3. Review this integration guide
4. Check Notion API documentation

---

**Version**: 2.0.0
**Last Updated**: 2026-02-09
**Status**: Active
