# Caching Strategy

Cache key generation, 30-day TTL enforcement, invalidation rules, and cleanup processes for ARIA regulatory research optimization.

## Overview

The caching system stores Context7 query results for 30 days to reduce redundant API calls while maintaining regulatory information freshness. The system uses intelligent cache key generation, automatic TTL enforcement, and multiple invalidation strategies.

## Cache Key Generation

### Key Format

**Structure**: `ctx7:{library_id}:{topic_hash}:{language}`

**Components**:
- Prefix: `ctx7` (identifies Context7 cache)
- Library ID: Resolved Context7 library identifier
- Topic Hash: SHA-256 hash of search query/topic
- Language: Content language code (en, ko, ja, etc.)

### Hash Calculation

```javascript
const crypto = require('crypto');

function generateTopicHash(topic) {
  return crypto
    .createHash('sha256')
    .update(topic.toLowerCase().trim())
    .digest('hex')
    .substring(0, 16); // Use first 16 characters
}
```

**Examples**:
```javascript
// FDA QSR Design Controls
generateTopicHash("design controls 820.30")
// Output: "a1b2c3d4e5f6g7h8"

// ISO 13485 QMS
generateTopicHash("quality management system clause 4")
// Output: "i9j8k7l6m5n4o3p2"

// EU MDR Technical Documentation
generateTopicHash("technical documentation annex i")
// Output: "q1w2e3r4t5y6u7i8"
```

### Complete Cache Key Examples

```javascript
// FDA 21 CFR 820 Design Controls (English)
const key1 = `ctx7:fda-21-cfr-part-820:${generateTopicHash("design controls 820.30")}:en`;
// Result: "ctx7:fda-21-cfr-part-820:a1b2c3d4e5f6g7h8:en"

// ISO 13485 QMS (English)
const key2 = `ctx7:iso-13485:${generateTopicHash("quality management system")}:en`;
// Result: "ctx7:iso-13485:x9y8z7w6v5u4t3s2:en"

// EU MDR Technical Documentation (English)
const key3 = `ctx7:eu-mdr-2017-745:${generateTopicHash("technical documentation annex i")}:en`;
// Result: "ctx7:eu-mdr-2017-745:m1n2b3v4c5x6z7l8:en"
```

### Cache Entry Structure

```javascript
{
  key: "ctx7:fda-21-cfr-part-820:a1b2c3d4e5f6g7h8:en",
  value: {
    libraryId: "fda-21-cfr-part-820",
    query: "design controls 820.30",
    results: [...], // Context7 query results
    timestamp: "2026-02-09T10:30:00Z",
    ttl: 2592000, // 30 days in seconds
    version: "1.0.0",
    sourceUrl: "https://www.ecfr.gov/current/title-21/section-820.30"
  },
  metadata: {
    createdAt: 1707477000, // Unix timestamp
    accessCount: 0,
    lastAccessedAt: 1707477000
  }
}
```

## 30-Day TTL Enforcement

### TTL Configuration

**Standard TTL**: 30 days (2,592,000 seconds)
**Content Type Variations**:

| Content Type | TTL | Rationale |
|-------------|-----|-----------|
| Regulation Text | 30 days | Stable, infrequent changes |
| Interpretation | 14 days | May change with new guidance |
| Guidance Documents | 7 days | More frequent updates |
| News/Announcements | 1 day | Highly dynamic |

### TTL Validation

```javascript
function isCacheEntryValid(entry) {
  const now = Math.floor(Date.now() / 1000); // Current Unix timestamp
  const entryAge = now - entry.metadata.createdAt;

  return entryAge < entry.value.ttl;
}
```

### TTL Enforcement Process

**On Cache Read**:
1. Retrieve cache entry by key
2. Check if entry exists
3. Validate TTL hasn't expired
4. Update access count and last accessed timestamp
5. Return cached value or null if expired

**On Cache Write**:
1. Generate cache key from query parameters
2. Check if entry already exists
3. If exists, update with new content and reset timestamp
4. If new, create entry with current timestamp
5. Store entry in cache

### Automatic Expiration

**Cleanup Schedule**: Runs during weekly knowledge base updates

**Cleanup Process**:
```javascript
function cleanupExpiredEntries() {
  const now = Math.floor(Date.now() / 1000);
  let expiredCount = 0;

  cache.keys().forEach(key => {
    const entry = cache.get(key);
    const entryAge = now - entry.metadata.createdAt;

    if (entryAge >= entry.value.ttl) {
      cache.delete(key);
      expiredCount++;
    }
  });

  logCleanupResult(expiredCount);
  return expiredCount;
}
```

## Cache Invalidation Rules

### Invalidation Triggers

**Automatic Invalidation**:
1. TTL expiration (30 days elapsed)
2. Regulatory update detected (version change)
3. Content hash mismatch (content changed)
4. Cache size limit reached (LRU eviction)

**Manual Invalidation**:
1. User command: /aria knowledge clear-cache
2. Admin command via system interface
3. Test/initiation requests
4. Emergency regulatory updates

### Invalidation Strategies

**Time-Based Invalidation**:
```javascript
function invalidateByAge(maxAge = 2592000) { // 30 days default
  const now = Math.floor(Date.now() / 1000);

  cache.keys().forEach(key => {
    const entry = cache.get(key);
    const entryAge = now - entry.metadata.createdAt;

    if (entryAge >= maxAge) {
      cache.delete(key);
    }
  });
}
```

**Version-Based Invalidation**:
```javascript
function invalidateByVersion(regulationType, newVersion) {
  const pattern = `ctx7:${regulationType}:`;

  cache.keys().forEach(key => {
    if (key.startsWith(pattern)) {
      const entry = cache.get(key);
      const currentVersion = parseVersion(entry.value.version);
      const latestVersion = parseVersion(newVersion);

      if (compareVersions(latestVersion, currentVersion) > 0) {
        cache.delete(key);
        logInvalidation(key, 'version_change');
      }
    }
  });
}
```

**Pattern-Based Invalidation**:
```javascript
function invalidateByPattern(regulationType) {
  const pattern = `ctx7:${regulationType}:`;

  cache.keys().forEach(key => {
    if (key.startsWith(pattern)) {
      cache.delete(key);
      logInvalidation(key, 'pattern_match');
    }
  });
}
```

**Selective Invalidation**:
```javascript
function invalidateSpecificSections(regulationType, sections) {
  sections.forEach(section => {
    const hash = generateTopicHash(section);
    const key = `ctx7:${regulationType}:${hash}:en`;

    if (cache.has(key)) {
      cache.delete(key);
      logInvalidation(key, 'specific_section');
    }
  });
}
```

### Invalidation Logging

All invalidation events are logged:
```javascript
function logInvalidation(key, reason) {
  const logEntry = {
    timestamp: new Date().toISOString(),
    key: key,
    reason: reason,
    invalidatedBy: 'system' | 'user' | 'admin'
  };

  writeInvalidationLog(logEntry);
}
```

## Cache Storage

### In-Memory Storage (Default)

```javascript
const NodeCache = require('node-cache');
const cache = new NodeCache({
  stdTTL: 2592000, // 30 days in seconds
  checkperiod: 3600, // Check for expired entries every hour
  useClones: false   // Performance optimization
});
```

### Persistent Storage Option (Future)

For cache persistence across restarts:
```javascript
const cache = require('persistent-cache');

const cache = new cache({
  instance: 'context7-cache',
  dir: '.cache',
  ttl: 2592000 // 30 days
});
```

## Cache Performance Optimization

### LRU Eviction Policy

When cache reaches size limit:
1. Sort entries by last accessed timestamp
2. Remove least recently used entries
3. Maintain cache size below threshold
4. Log evicted entries for analysis

### Cache Warming

**Pre-load Common Queries**:
```javascript
async function warmCache() {
  const commonQueries = [
    { library: 'fda-21-cfr-part-820', topic: 'design controls' },
    { library: 'iso-13485', topic: 'quality management system' },
    { library: 'eu-mdr-2017-745', topic: 'technical documentation' }
  ];

  for (const query of commonQueries) {
    const key = generateCacheKey(query);

    if (!cache.has(key)) {
      const results = await queryContext7(query);
      cache.set(key, results);
    }
  }
}
```

### Cache Statistics

**Metrics Tracked**:
- Hit rate: (cache hits / total requests) * 100
- Miss rate: (cache misses / total requests) * 100
- Average entry age: Mean age of all cache entries
- Cache size: Number of entries in cache
- Eviction count: Number of entries evicted

**Performance Targets**:
- Hit rate: > 80%
- Average response time (cached): < 10ms
- Average response time (uncached): < 500ms (Context7 API)
- Memory usage: < 100MB

## Cache Integration with ARIA Workflow

### Brief Phase

During Brief phase, cache provides quick access to frequently accessed regulations for preliminary requirements analysis.

### Execute Phase

During Execute phase, cached results reduce research time for document drafting and requirements verification.

### Deliver Phase

During Deliver phase, cache metadata provides source attribution and retrieval timestamps for VALID framework verification.

## Monitoring and Maintenance

### Health Checks

**Daily Health Check**:
- Verify cache service is running
- Check cache size and memory usage
- Validate cache integrity (checksum verification)
- Monitor hit/miss rates

**Weekly Maintenance**:
- Clean up expired entries
- Analyze cache performance metrics
- Identify optimization opportunities
- Generate performance reports

### Alerts

**Performance Alerts**:
- Hit rate drops below 70%
- Average response time exceeds 50ms
- Cache size exceeds memory limit

**Operational Alerts**:
- Cache service unavailable
- Cache corruption detected
- Excessive eviction rate

---

Last Updated: 2026-02-09
Maintained by: ARIA Development Team
