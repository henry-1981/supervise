# Knowledge Base Management

Weekly auto-update configuration, change detection, incremental update mechanisms, and Notion integration for ARIA regulatory knowledge base.

## Overview

The knowledge base auto-update system ensures regulatory information remains current by synchronizing with Context7 MCP on a weekly schedule. The system uses change detection to perform incremental updates, minimizing API calls while maintaining data freshness.

## Weekly Schedule Configuration

### Default Schedule

**Frequency**: Weekly (every 7 days)
**Default Day**: Sunday
**Default Time**: 02:00 UTC (low-traffic period)

### Schedule Configuration

```yaml
knowledge_base:
  auto_update:
    enabled: true
    schedule:
      frequency: "weekly"
      day: "sunday"
      time: "02:00"
      timezone: "UTC"
    triggers:
      - scheduled
      - manual
      - regulatory_announcement
```

### Regulatory Publication Cycles

**FDA Updates**:
- Frequency: Quarterly (January, April, July, October)
- Source: Federal Register
- Topics: New guidances, draft rules, final rules

**ISO Updates**:
- Frequency: Annually (typically January)
- Source: ISO.org announcements
- Topics: Standard revisions, new standards

**EU MDR Updates**:
- Frequency: As needed (no fixed schedule)
- Source: Official Journal of the European Union
- Topics: Implementing acts, delegated acts, guidelines

### Schedule Override Conditions

The auto-update schedule is overridden when:
1. Regulatory publication announcements detected
2. Manual update triggered via /aria knowledge refresh
3. Critical regulatory changes identified
4. System initialization (first run)

## Change Detection Mechanism

### Last Update Tracking

**Data Structure**:
```javascript
{
  regulationType: "FDA 21 CFR 820",
  lastUpdateTimestamp: "2026-02-09T02:00:00Z",
  lastUpdateHash: "abc123...",
  sectionsUpdated: [
    "820.30",
    "820.40"
  ],
  versionTracked: {
    major: 21,
    minor: 0,
    patch: 0
  }
}
```

### Change Detection Process

**Phase 1: Metadata Comparison**

1. Retrieve last update timestamps for each regulation
2. Compare against regulatory publication schedules
3. Identify regulations requiring updates
4. Generate update priority list

**Phase 2: Content Hash Comparison**

1. Calculate hash of existing content sections
2. Query Context7 for current version
3. Compare hashes to detect changed sections
4. Flag sections with hash mismatches

**Phase 3: Version Tracking**

1. Track regulation version numbers
2. Monitor for version increments
3. Flag significant version changes
4. Trigger full-content updates for major version changes

### Change Detection Algorithms

**Hash Calculation**:
```javascript
function calculateContentHash(content) {
  const crypto = require('crypto');
  return crypto
    .createHash('sha256')
    .update(JSON.stringify(content))
    .digest('hex');
}
```

**Version Comparison**:
```javascript
function compareVersions(current, latest) {
  if (current.major !== latest.major) {
    return 'major';
  }
  if (current.minor !== latest.minor) {
    return 'minor';
  }
  if (current.patch !== latest.patch) {
    return 'patch';
  }
  return 'current';
}
```

## Incremental Update Process

### Update Trigger Logic

**Automatic Trigger**:
- Scheduled weekly execution
- Regulatory publication detected via RSS/API monitoring
- Version change detected

**Manual Trigger**:
- User initiates via /aria knowledge refresh
- Admin initiates via system interface
- Test/initiation requests

### Update Execution Flow

**Step 1: Change Detection**
- Query last update timestamps
- Compare against regulatory schedules
- Generate list of changed regulations
- Prioritize by change significance

**Step 2: Selective Content Retrieval**
- Query Context7 for changed sections only
- Retrieve full content for major version changes
- Retrieve differential content for minor changes
- Cache retrieved results

**Step 3: Content Validation**
- Verify content completeness
- Check for structural integrity
- Validate citation formats
- Confirm source attribution

**Step 4: Knowledge Base Update**
- Update Notion database with new content
- Update metadata (timestamps, hashes, versions)
- Log changes to audit trail
- Invalidate relevant cache entries

**Step 5: Notification**
- Generate update summary
- Send notification if significant changes
- Update dashboard metrics
- Log completion

### Update Optimization Strategies

**Batch Processing**:
- Group multiple section updates into single transactions
- Limit batch size to 100 sections per transaction
- Use parallel processing for independent regulations

**Differential Updates**:
- For minor changes, update only affected sections
- For major changes, perform full regulation update
- Maintain change history for rollback capability

**Rate Limiting**:
- Respect Context7 API rate limits
- Implement exponential backoff for retries
- Queue updates when rate limit reached

## Notion MCP Integration

### Database Schema

**Regulatory Content Database**:
```
Properties:
- Title (Title): Regulation citation (e.g., "21 CFR 820.30")
- Category (Select): FDA / ISO / EU MDR
- Section (Text): Section identifier (e.g., "820.30")
- Content (Text): Full regulation text
- Last Updated (Date): Update timestamp
- Source (URL): Context7 or official source URL
- Version (Text): Regulation version
- Hash (Text): Content hash for change detection
- Tags (Multi-select): QSR, QMS, Design Controls, etc.
```

**Update Log Database**:
```
Properties:
- Update ID (Title): Unique update identifier
- Timestamp (Date): When update occurred
- Regulation Type (Select): FDA / ISO / EU MDR
- Sections Updated (Multi-select): List of sections
- Change Type (Select): Major / Minor / Patch
- Trigger (Select): Scheduled / Manual / Announcement
- Status (Select): Success / Failed / Partial
- Summary (Text): Update description
```

### Notion API Operations

**Create/Update Page**:
```javascript
async function updateRegulatoryPage(regulationData) {
  const notion = await getNotionClient();

  const pageProperties = {
    parent: { database_id: REGULATORY_CONTENT_DB },
    properties: {
      "Title": {
        title: [{ text: { content: regulationData.citation } }]
      },
      "Category": { select: { name: regulationData.category } },
      "Section": { rich_text: [{ text: { content: regulationData.section } }] },
      "Content": { rich_text: [{ text: { content: regulationData.content } }] },
      "Last Updated": { date: { start: new Date().toISOString() } },
      "Source": { url: regulationData.sourceUrl },
      "Version": { rich_text: [{ text: { content: regulationData.version } }] },
      "Hash": { rich_text: [{ text: { content: regulationData.hash } }] }
    }
  };

  return await notion.pages.create(pageProperties);
}
```

**Query Existing Page**:
```javascript
async function findExistingPage(citation) {
  const notion = await getNotionClient();

  const response = await notion.databases.query({
    database_id: REGULATORY_CONTENT_DB,
    filter: {
      property: "Title",
      title: { equals: citation }
    }
  });

  return response.results.length > 0 ? response.results[0] : null;
}
```

**Update Existing Page**:
```javascript
async function updateExistingPage(pageId, regulationData) {
  const notion = await getNotionClient();

  return await notion.pages.update({
    page_id: pageId,
    properties: {
      "Content": { rich_text: [{ text: { content: regulationData.content } }] },
      "Last Updated": { date: { start: new Date().toISOString() } },
      "Version": { rich_text: [{ text: { content: regulationData.version } }] },
      "Hash": { rich_text: [{ text: { content: regulationData.hash } }] }
    }
  });
}
```

### Update Logging

**Log Update Event**:
```javascript
async function logUpdateEvent(updateData) {
  const notion = await getNotionClient();

  const logProperties = {
    parent: { database_id: UPDATE_LOG_DB },
    properties: {
      "Update ID": {
        title: [{ text: { content: `UPDATE-${Date.now()}` } }]
      },
      "Timestamp": { date: { start: new Date().toISOString() } },
      "Regulation Type": { select: { name: updateData.regulationType } },
      "Sections Updated": {
        multi_select: updateData.sections.map(s => ({ name: s }))
      },
      "Change Type": { select: { name: updateData.changeType } },
      "Trigger": { select: { name: updateData.trigger } },
      "Status": { select: { name: updateData.status } },
      "Summary": { rich_text: [{ text: { content: updateData.summary } }] }
    }
  };

  return await notion.pages.create(logProperties);
}
```

## Error Handling and Recovery

### Context7 Unavailability

**Detection**: Context7 MCP server not responding or returning errors

**Recovery Strategy**:
1. Log error to update log database
2. Use cached content if available
3. Schedule retry with exponential backoff
4. Send notification if unavailable for > 24 hours

**Retry Schedule**:
- First retry: 5 minutes
- Second retry: 15 minutes
- Third retry: 1 hour
- Fourth retry: 4 hours
- Fifth retry: 24 hours

### Notion API Errors

**Detection**: Notion API rate limits, connection errors, validation errors

**Recovery Strategy**:
1. Implement exponential backoff
2. Queue failed updates
3. Process queue when Notion is available
4. Log all failures for manual review

### Content Validation Failures

**Detection**: Empty content, malformed citations, missing required fields

**Recovery Strategy**:
1. Log validation failure
2. Flag content for manual review
3. Use previous version if available
4. Send notification for critical failures

## Monitoring and Alerts

### Update Success Metrics

**Metrics Tracked**:
- Update execution time
- Number of sections updated per regulation
- API call count
- Cache hit rate
- Error rate

**Success Criteria**:
- Update completes within 30 minutes
- Zero critical failures
- > 95% sections updated successfully
- Cache hit rate > 80%

### Alert Conditions

**Warning Alerts**:
- Update takes > 30 minutes
- Cache hit rate < 80%
- > 5% sections fail validation

**Critical Alerts**:
- Context7 unavailable for > 1 hour
- Notion API unavailable for > 4 hours
- Major regulation version change detected
- > 10% critical sections fail update

### Dashboard Integration

Update status displayed on ARIA dashboard showing:
- Last successful update timestamp
- Next scheduled update time
- Regulations requiring updates
- Update success rate
- Recent update log entries

---

Last Updated: 2026-02-09
Maintained by: ARIA Development Team
