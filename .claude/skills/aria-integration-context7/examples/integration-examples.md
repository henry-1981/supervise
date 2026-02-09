# Context7 Integration Examples

Working code examples for Context7 integration with ARIA workflow, including regulatory search patterns, caching implementation, and query optimization.

## Basic Context7 Query Examples

### FDA 21 CFR 820 Query

```javascript
// Resolve FDA library ID
const fdaLibraryId = await mcp__context7__resolve-library-id({
  query: "fda 21 cfr 820"
});

// Get design controls requirements
const designControls = await mcp__context7__get-library-docs({
  libraryId: fdaLibraryId,
  query: "design controls 820.30",
  tokens: 5000
});

console.log('Design Controls Results:', designControls.results);
```

### ISO 13485 Query

```javascript
// Resolve ISO library ID
const isoLibraryId = await mcp__context7__resolve-library-id({
  query: "iso 13485"
});

// Get QMS requirements
const qmsRequirements = await mcp__context7__get-library-docs({
  libraryId: isoLibraryId,
  query: "quality management system clause 4",
  tokens: 5000
});

console.log('QMS Requirements:', qmsRequirements.results);
```

### EU MDR Query

```javascript
// Resolve EU MDR library ID
const mdrLibraryId = await mcp__context7__resolve-library-id({
  query: "eu mdr 2017/745"
});

// Get technical documentation requirements
const techDocs = await mcp__context7__get-library-docs({
  libraryId: mdrLibraryId,
  query: "technical documentation annex i chapter ii",
  tokens: 5000
});

console.log('Technical Documentation:', techDocs.results);
```

## Regulatory Search Pattern Examples

### Design Controls Comparison

```javascript
async function compareDesignControls() {
  const comparisons = [
    {
      source: "FDA 21 CFR 820.30",
      query: "design controls",
      library: await resolveLibraryId("fda 21 cfr 820")
    },
    {
      source: "ISO 13485 Clause 7.3",
      query: "design and development",
      library: await resolveLibraryId("iso 13485")
    },
    {
      source: "EU MDR Annex I",
      query: "technical documentation",
      library: await resolveLibraryId("eu mdr 2017/745")
    }
  ];

  const results = await Promise.all(
    comparisons.map(async (comp) => {
      const docs = await mcp__context7__get-library-docs({
        libraryId: comp.library,
        query: comp.query,
        tokens: 5000
      });

      return {
        source: comp.source,
        requirements: docs.results,
        timestamp: new Date().toISOString()
      };
    })
  );

  return results;
}
```

### Risk Management Search

```javascript
async function searchRiskManagement() {
  const riskQueries = [
    {
      regulation: "FDA 21 CFR 820",
      sections: ["820.30", "820.100"],
      query: "risk analysis"
    },
    {
      regulation: "ISO 13485",
      sections: ["7.1", "8.2.3"],
      query: "risk management"
    },
    {
      regulation: "EU MDR",
      sections: ["Annex I", "Annex IX"],
      query: "risk management"
    }
  ];

  const results = [];

  for (const rq of riskQueries) {
    const libraryId = await resolveLibraryId(rq.regulation);
    const docs = await mcp__context7__get-library-docs({
      libraryId: libraryId,
      query: rq.query,
      tokens: 5000
    });

    results.push({
      regulation: rq.regulation,
      sections: rq.sections,
      results: docs.results
    });
  }

  return results;
}
```

## Caching Implementation Examples

### Cache Management Class

```javascript
class Context7Cache {
  constructor(ttl = 2592000) { // 30 days default
    this.cache = new Map();
    this.ttl = ttl;
  }

  generateKey(libraryId, query, language = 'en') {
    const crypto = require('crypto');
    const queryHash = crypto
      .createHash('sha256')
      .update(query.toLowerCase().trim())
      .digest('hex')
      .substring(0, 16);

    return `ctx7:${libraryId}:${queryHash}:${language}`;
  }

  get(key) {
    const entry = this.cache.get(key);

    if (!entry) {
      return null;
    }

    const now = Math.floor(Date.now() / 1000);
    const age = now - entry.timestamp;

    if (age >= this.ttl) {
      this.cache.delete(key);
      return null;
    }

    entry.accessCount++;
    entry.lastAccessed = now;

    return entry.value;
  }

  set(key, value) {
    const now = Math.floor(Date.now() / 1000);

    this.cache.set(key, {
      value: value,
      timestamp: now,
      accessCount: 0,
      lastAccessed: now
    });
  }

  invalidate(pattern) {
    const keysToDelete = [];

    this.cache.forEach((entry, key) => {
      if (key.includes(pattern)) {
        keysToDelete.push(key);
      }
    });

    keysToDelete.forEach(key => this.cache.delete(key));

    return keysToDelete.length;
  }

  getStats() {
    let totalAccess = 0;
    let oldestEntry = Date.now() / 1000;

    this.cache.forEach((entry) => {
      totalAccess += entry.accessCount;
      if (entry.timestamp < oldestEntry) {
        oldestEntry = entry.timestamp;
      }
    });

    return {
      size: this.cache.size,
      totalAccess: totalAccess,
      averageAccess: totalAccess / this.cache.size,
      oldestEntryAge: Math.floor(Date.now() / 1000) - oldestEntry
    };
  }
}

// Usage
const cache = new Context7Cache();

async function cachedQuery(libraryId, query) {
  const cacheKey = cache.generateKey(libraryId, query);

  // Check cache first
  const cached = cache.get(cacheKey);
  if (cached) {
    console.log('Cache hit for:', query);
    return cached;
  }

  // Query Context7 if not in cache
  console.log('Cache miss for:', query);
  const results = await mcp__context7__get-library-docs({
    libraryId: libraryId,
    query: query,
    tokens: 5000
  });

  // Store in cache
  cache.set(cacheKey, results);

  return results;
}
```

## Batch Query Processing Examples

### Batch Processor Class

```javascript
class Context7BatchProcessor {
  constructor(maxBatchSize = 10) {
    this.maxBatchSize = maxBatchSize;
    this.processingQueue = [];
  }

  async processBatch(queries) {
    const batches = this.createBatches(queries);
    const allResults = [];

    for (const batch of batches) {
      console.log(`Processing batch with ${batch.length} queries`);

      const batchResults = await this.executeBatch(batch);
      allResults.push(...batchResults);

      // Small delay between batches to respect rate limits
      if (batches.indexOf(batch) < batches.length - 1) {
        await this.delay(500);
      }
    }

    return allResults;
  }

  createBatches(queries) {
    const batches = [];
    const currentBatch = [];

    for (const query of queries) {
      currentBatch.push(query);

      if (currentBatch.length === this.maxBatchSize) {
        batches.push([...currentBatch]);
        currentBatch.length = 0;
      }
    }

    if (currentBatch.length > 0) {
      batches.push(currentBatch);
    }

    return batches;
  }

  async executeBatch(batch) {
    const results = [];

    for (const query of batch) {
      try {
        const result = await mcp__context7__get-library-docs({
          libraryId: query.libraryId,
          query: query.topic,
          tokens: 3000
        });

        results.push({
          query: query,
          success: true,
          data: result
        });

        // Small delay between queries
        await this.delay(100);
      } catch (error) {
        results.push({
          query: query,
          success: false,
          error: error.message
        });
      }
    }

    return results;
  }

  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

// Usage
const processor = new Context7BatchProcessor(10);

const queries = [
  { libraryId: "fda-21-cfr-part-820", topic: "design controls" },
  { libraryId: "fda-21-cfr-part-820", topic: "design validation" },
  { libraryId: "iso-13485", topic: "quality management system" },
  // ... more queries
];

const results = await processor.processBatch(queries);
```

## ARIA Workflow Integration Examples

### Brief Phase Integration

```javascript
async function briefPhaseRegulatoryCheck(deviceInfo) {
  // Identify applicable regulations based on device classification
  const applicableRegs = identifyApplicableRegulations(deviceInfo);

  // Batch query applicable regulations
  const queries = applicableRegs.map(reg => ({
    libraryId: reg.libraryId,
    topic: reg.generalRequirements
  }));

  const processor = new Context7BatchProcessor();
  const results = await processor.processBatch(queries);

  // Generate regulatory landscape
  return generateRegulatoryLandscape(results);
}

function identifyApplicableRegulations(deviceInfo) {
  const regs = [];

  if (deviceInfo.markets.includes('US')) {
    regs.push({
      libraryId: "fda-21-cfr-part-820",
      generalRequirements: "quality system requirements"
    });
  }

  if (deviceInfo.markets.includes('EU')) {
    regs.push({
      libraryId: "eu-mdr-2017-745",
      generalRequirements: "general safety and performance requirements"
    });
  }

  if (deviceInfo.requiresQMS) {
    regs.push({
      libraryId: "iso-13485",
      generalRequirements: "quality management system"
    });
  }

  return regs;
}
```

### Execute Phase Integration

```javascript
async function executePhaseDocumentDrafting(requirements) {
  const documents = [];

  for (const requirement of requirements) {
    // Use cached results for efficiency
    const cached = await cachedQuery(
      requirement.regulationLibrary,
      requirement.searchQuery
    );

    if (cached && cached.results.length > 0) {
      const document = await draftDocument(requirement, cached);
      documents.push(document);
    }
  }

  return documents;
}
```

### Deliver Phase Integration

```javascript
async function deliverPhaseValidation(deliverables) {
  const validationResults = [];

  for (const deliverable of deliverables) {
    // Verify citations are current
    const citations = extractCitations(deliverable);

    for (const citation of citations) {
      const current = await cachedQuery(
        citation.libraryId,
        citation.query
      );

      const isValid = validateCitation(citation, current);

      validationResults.push({
        citation: citation,
        valid: isValid,
        timestamp: new Date().toISOString()
      });
    }
  }

  return {
    deliverable: deliverable,
    citations: validationResults,
    overallValid: validationResults.every(v => v.valid)
  };
}
```

## Knowledge Base Update Examples

### Weekly Update Process

```javascript
async function weeklyKnowledgeBaseUpdate() {
  console.log('Starting weekly knowledge base update');

  // Step 1: Detect changes
  const changes = await detectRegulatoryChanges();
  console.log(`Detected ${changes.length} regulatory changes`);

  // Step 2: Batch query changed sections
  if (changes.length > 0) {
    const queries = changes.map(change => ({
      libraryId: change.libraryId,
      topic: change.section
    }));

    const processor = new Context7BatchProcessor(10);
    const results = await processor.processBatch(queries);

    // Step 3: Update knowledge base
    await updateKnowledgeBase(results);

    // Step 4: Invalidate affected cache entries
    const cache = new Context7Cache();
    changes.forEach(change => {
      cache.invalidate(change.libraryId);
    });
  }

  console.log('Weekly update completed');
}

async function detectRegulatoryChanges() {
  // Check publication schedules
  const changes = [];

  // FDA quarterly updates
  if (isFDAPublicationWeek()) {
    changes.push(...await detectFDAChanges());
  }

  // ISO annual updates
  if (isISOUpdateWeek()) {
    changes.push(...await detectISOChanges());
  }

  // EU MDR ad-hoc updates
  changes.push(...await detectMDRChanges());

  return changes;
}
```

## Advanced Optimization Examples

### Query Result Deduplication

```javascript
function deduplicateResults(results) {
  const seen = new Set();
  const unique = [];

  for (const result of results) {
    const signature = JSON.stringify({
      citation: result.citation,
      section: result.section,
      contentHash: hashContent(result.content)
    });

    if (!seen.has(signature)) {
      seen.add(signature);
      unique.push(result);
    }
  }

  return unique;
}

function hashContent(content) {
  const crypto = require('crypto');
  return crypto
    .createHash('sha256')
    .update(content.toLowerCase().replace(/\s+/g, ' '))
    .digest('hex')
    .substring(0, 16);
}
```

### Result Ranking

```javascript
function rankResults(results, query) {
  return results
    .map(result => ({
      ...result,
      score: calculateRelevanceScore(result, query)
    }))
    .sort((a, b) => b.score - a.score)
    .map((result, index) => ({
      ...result,
      rank: index + 1
    }));
}

function calculateRelevanceScore(result, query) {
  let score = 0;

  // Topic match (40%)
  score += topicMatchScore(result, query) * 40;

  // Recency (20%)
  score += recencyScore(result.date) * 20;

  // Authority (20%)
  score += authorityScore(result.source) * 20;

  // Completeness (10%)
  score += completenessScore(result) * 10;

  // User history (10%)
  score += historyScore(result) * 10;

  return score;
}
```

## Error Handling Examples

### Context7 Fallback

```javascript
async function resilientQuery(libraryId, query, cache) {
  try {
    // Try Context7 first
    const results = await mcp__context7__get-library-docs({
      libraryId: libraryId,
      query: query,
      tokens: 5000
    });

    // Cache successful results
    const cacheKey = cache.generateKey(libraryId, query);
    cache.set(cacheKey, results);

    return results;
  } catch (error) {
    console.error('Context7 query failed:', error.message);

    // Fallback to cache if available
    const cacheKey = cache.generateKey(libraryId, query);
    const cached = cache.get(cacheKey);

    if (cached) {
      console.log('Using cached results as fallback');
      return cached;
    }

    // No cache available, provide manual guidance
    return {
      error: 'Context7 unavailable and no cached results',
      guidance: `Manual research required for: ${query}`,
      alternativeSources: suggestAlternativeSources(libraryId, query)
    };
  }
}

function suggestAlternativeSources(libraryId, query) {
  const sources = {
    'fda-21-cfr-part-820': [
      'https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H',
      'https://www.fda.gov/medical-devices/quality-systems-qsr'
    ],
    'iso-13485': [
      'https://www.iso.org/standard/59752.html',
      'https://www.iso.org/committee/5393609.html'
    ],
    'eu-mdr-2017-745': [
      'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R0745',
      'https://health.ec.europa.eu/medical-devices-sector/new-regulations_en'
    ]
  };

  return sources[libraryId] || [];
}
```

---

Last Updated: 2026-02-09
Maintained by: ARIA Development Team
