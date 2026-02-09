# Query Optimization

Batch query generation, result deduplication, relevance ranking, and performance optimization for Context7 MCP queries.

## Overview

Query optimization reduces Context7 API calls and improves result quality through intelligent batching, deduplication, and relevance ranking. The system processes multiple related queries efficiently while maintaining accuracy for regulatory research.

## Batch Query Generation

### Batching Strategy

**Batch Formation Rules**:
1. Group queries by regulation type (FDA, ISO, EU MDR)
2. Group by chapter or clause hierarchy
3. Limit batch size to 10 queries maximum
4. Prioritize related topics in same batch

### Batch Query Structure

```javascript
{
  batchId: "batch-20260209-001",
  regulationType: "FDA 21 CFR 820",
  queries: [
    {
      id: "query-1",
      libraryId: "fda-21-cfr-part-820",
      topic: "design controls 820.30",
      priority: "high"
    },
    {
      id: "query-2",
      libraryId: "fda-21-cfr-part-820",
      topic: "design validation 820.30",
      priority: "high"
    },
    // ... up to 10 queries
  ],
  createdAt: "2026-02-09T10:30:00Z",
  status: "pending"
}
```

### Batch Processing Algorithm

```javascript
async function processBatch(batch) {
  const results = [];

  // Process queries sequentially to respect rate limits
  for (const query of batch.queries) {
    try {
      const result = await queryContext7(query);
      results.push({
        queryId: query.id,
        success: true,
        data: result
      });

      // Small delay between queries to respect rate limits
      await delay(100); // 100ms between queries
    } catch (error) {
      results.push({
        queryId: query.id,
        success: false,
        error: error.message
      });
    }
  }

  return {
    batchId: batch.batchId,
    results: results,
    completedAt: new Date().toISOString()
  };
}
```

### Smart Batching

**Related Topic Detection**:
```javascript
function detectRelatedQueries(queries) {
  const groups = new Map();

  queries.forEach(query => {
    const keywords = extractKeywords(query.topic);

    keywords.forEach(keyword => {
      if (!groups.has(keyword)) {
        groups.set(keyword, []);
      }
      groups.get(keyword).push(query);
    });
  });

  return groups;
}
```

**Batch Formation Example**:
```javascript
const queries = [
  "design controls 820.30",
  "design validation 820.30",
  "design verification 820.30",
  "document control 820.40",
  "document approval 820.40"
];

// Smart batching groups related queries
const batches = createSmartBatches(queries);
// Result: 2 batches
// Batch 1: design controls, design validation, design verification
// Batch 2: document control, document approval
```

## Result Deduplication

### Deduplication Strategy

**Deduplication Criteria**:
1. Exact match on citation
2. Exact match on section number
3. Content hash match (90%+ similarity)

### Deduplication Algorithm

```javascript
function deduplicateResults(results) {
  const unique = new Map();
  const duplicates = [];

  results.forEach(result => {
    const signature = generateResultSignature(result);

    if (unique.has(signature)) {
      duplicates.push({
        original: unique.get(signature),
        duplicate: result
      });
    } else {
      unique.set(signature, result);
    }
  });

  return {
    uniqueResults: Array.from(unique.values()),
    duplicates: duplicates,
    duplicateCount: duplicates.length
  };
}
```

### Signature Generation

```javascript
function generateResultSignature(result) {
  const signatureData = {
    citation: result.citation,
    section: result.section,
    contentHash: calculateHash(result.content)
  };

  return JSON.stringify(signatureData);
}
```

### Similarity Detection

```javascript
function calculateSimilarity(content1, content2) {
  const tokens1 = tokenize(content1);
  const tokens2 = tokenize(content2);

  const intersection = tokens1.filter(token => tokens2.includes(token));
  const union = [...new Set([...tokens1, ...tokens2])];

  return intersection.length / union.length; // Jaccard similarity
}
```

**Similarity Threshold**: 0.9 (90% similarity = duplicate)

## Result Ranking

### Relevance Scoring

**Scoring Factors**:
1. Topic match quality (0-40 points)
2. Citation recency (0-20 points)
3. Source authority (0-20 points)
4. Content completeness (0-10 points)
5. User interaction history (0-10 points)

### Scoring Algorithm

```javascript
function calculateRelevanceScore(result, query) {
  let score = 0;

  // Topic match quality (0-40 points)
  score += calculateTopicMatchScore(result, query) * 40;

  // Citation recency (0-20 points)
  score += calculateRecencyScore(result.publicationDate) * 20;

  // Source authority (0-20 points)
  score += calculateAuthorityScore(result.source) * 20;

  // Content completeness (0-10 points)
  score += calculateCompletenessScore(result) * 10;

  // User interaction history (0-10 points)
  score += calculateHistoryScore(result) * 10;

  return {
    result: result,
    score: score,
    timestamp: Date.now()
  };
}
```

### Topic Match Quality

```javascript
function calculateTopicMatchScore(result, query) {
  const queryKeywords = extractKeywords(query.topic);
  const resultKeywords = extractKeywords(result.content);

  const matchCount = queryKeywords.filter(kw =>
    resultKeywords.some(rk => rk.includes(kw))
  ).length;

  return matchCount / queryKeywords.length;
}
```

### Citation Recency

```javascript
function calculateRecencyScore(publicationDate) {
  const now = new Date();
  const pubDate = new Date(publicationDate);
  const ageInYears = (now - pubDate) / (1000 * 60 * 60 * 24 * 365);

  if (ageInYears < 1) return 1.0;
  if (ageInYears < 3) return 0.8;
  if (ageInYears < 5) return 0.6;
  if (ageInYears < 10) return 0.4;
  return 0.2;
}
```

### Source Authority

**Authority Ratings**:
- Official regulatory source: 1.0 (e.g., FDA.gov, ISO.org)
- Government database: 0.9 (e.g., eCFR, EUR-LEX)
- Reputable legal database: 0.8 (e.g., LexisNexis)
- Industry association: 0.7
- General reference: 0.5

```javascript
const authorityRatings = {
  'fda.gov': 1.0,
  'ecfr.gov': 1.0,
  'iso.org': 1.0,
  'eur-lex.europa.eu': 1.0,
  'lexisnexis.com': 0.8,
  // ... more sources
};

function calculateAuthorityScore(source) {
  const domain = extractDomain(source);
  return authorityRatings[domain] || 0.5;
}
```

### Ranking Results

```javascript
function rankResults(results, query) {
  const scoredResults = results.map(result =>
    calculateRelevanceScore(result, query)
  );

  scoredResults.sort((a, b) => b.score - a.score);

  return scoredResults.map((sr, index) => ({
    ...sr.result,
    rank: index + 1,
    relevanceScore: sr.score
  }));
}
```

## Performance Optimization

### Query Caching

**Cache Before Batch**:
```javascript
async function optimizedBatchProcess(queries) {
  const uncachedQueries = [];
  const cachedResults = [];

  // Check cache for each query
  for (const query of queries) {
    const cacheKey = generateCacheKey(query);

    if (cache.has(cacheKey)) {
      cachedResults.push(cache.get(cacheKey));
    } else {
      uncachedQueries.push(query);
    }
  }

  // Process only uncached queries in batch
  const batchResults = await processBatch({
    queries: uncachedQueries
  });

  // Cache new results
  batchResults.results.forEach(result => {
    if (result.success) {
      const cacheKey = generateCacheKey(result.query);
      cache.set(cacheKey, result.data);
    }
  });

  // Combine cached and new results
  return [...cachedResults, ...batchResults.results];
}
```

### Parallel Processing (where safe)

```javascript
async function parallelQueryProcess(queries) {
  const chunks = chunkArray(queries, 3); // Max 3 parallel queries

  const results = [];

  for (const chunk of chunks) {
    const chunkResults = await Promise.all(
      chunk.map(query => queryContext7(query))
    );

    results.push(...chunkResults);

    // Rate limit delay between chunks
    await delay(500);
  }

  return results;
}
```

### Result Compression

For large result sets, compress before caching:
```javascript
const zlib = require('zlib');

function compressResult(result) {
  const json = JSON.stringify(result);
  return zlib.gzipSync(json);
}

function decompressResult(compressed) {
  const json = zlib.gunzipSync(compressed).toString();
  return JSON.parse(json);
}
```

## Query Optimization Patterns

### Progressive Refinement

**Start Broad, Then Narrow**:
```javascript
// Step 1: Broad search
const broadResults = await queryContext7({
  library: "fda-21-cfr-part-820",
  topic: "design controls"
});

// Step 2: Refine with specific sections
const specificResults = await queryContext7({
  library: "fda-21-cfr-part-820",
  topic: "design validation 820.30"
});
```

### Hierarchical Queries

**Query by Hierarchy**:
```javascript
// Top-level query
const topLevel = await queryContext7({
  library: "iso-13485",
  topic: "quality management system"
});

// Next-level queries based on top-level results
const nextLevelQueries = topLevel.results.flatMap(result =>
  result.subsections.map(sub => ({
    library: "iso-13485",
    topic: `${result.section} ${sub}`
  }))
);
```

### Cross-Regulation Comparison

**Batch Multiple Regulations**:
```javascript
const comparisonBatch = {
  queries: [
    { library: "fda-21-cfr-part-820", topic: "design controls" },
    { library: "iso-13485", topic: "design and development" },
    { library: "eu-mdr-2017-745", topic: "technical documentation" }
  ]
};

const comparison = await processBatch(comparisonBatch);
```

## Monitoring and Analytics

### Query Performance Metrics

**Metrics Tracked**:
- Average query execution time
- Batch processing efficiency
- Cache hit/miss rates
- Deduplication rate
- Result relevance scores

**Performance Targets**:
- Cached query response: < 10ms
- Uncached query response: < 500ms
- Batch processing: < 5 seconds for 10 queries
- Deduplication rate: > 15% for related queries

### Query Analytics

**Track Query Patterns**:
```javascript
function logQuery(query, result) {
  const analytics = {
    timestamp: Date.now(),
    query: query,
    resultCount: result.results.length,
    executionTime: result.executionTime,
    cacheHit: result.fromCache,
    relevanceScore: result.averageRelevance
  };

  writeQueryLog(analytics);
}
```

**Analyze Query Trends**:
- Most frequently queried regulations
- Average query complexity
- Peak query times
- Cache effectiveness by regulation type

## Integration with ARIA Workflow

### Brief Phase Optimization

During Brief phase, use cached results for common regulatory lookups to quickly identify applicable requirements.

### Execute Phase Optimization

During Execute phase, use batch processing for comprehensive regulatory research across multiple requirements.

### Deliver Phase Optimization

During Deliver phase, use ranked results to provide most relevant citations for documentation.

---

Last Updated: 2026-02-09
Maintained by: ARIA Development Team
