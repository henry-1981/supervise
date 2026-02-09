---
name: aria-search
description: >
  ARIA unified search command - Search across Notion databases, Context7 MCP regulatory
  documents, and Google Workspace (Gmail, Docs, Drive) simultaneously. Results are
  ranked by relevance scoring algorithm (keyword_match*0.4 + semantic_similarity*0.3 + recency*0.2 + source_authority*0.1)
  and support category filtering with source attribution.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "2.1.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, search, notion, context7, google, unified, relevance-scoring"
  argument-hint: "\"search query\" [--filter category] [--date range] [--sort relevance|date|source]"
---

# ARIA Unified Search Command

## Purpose

Search across all ARIA data sources (Notion DB, Context7, Google Workspace) simultaneously and provide ranked results with relevance scoring and source attribution.

## Usage

```
/aria search "510(k) submission requirements"
/aria search "ISO 13485 clause 8.5.2" --filter standards
/aria search "CAPA overdue" --date "2024-01-01:2024-12-31"
/aria search "FDA 510(k) request" --filter emails
```

## Search Sources

### 1. Notion Database Search

Searches across 6 Notion databases:

- **Regulatory Requirements:** Regulatory requirements, standard clauses
- **Document Registry:** SOPs, WIs, Reports, documents
- **CAPA Tracker:** CAPA records, action plans
- **Risk Register:** Risk analyses, control measures
- **Submission Tracker:** Submission records, status
- **Knowledge Base:** Knowledge items, regulatory interpretations

**Search Fields:** Full-text search across Title, Text, Rich Text fields

### 2. Context7 MCP Search

Search for up-to-date regulatory documents via Context7:

**Libraries:**
- FDA 21 CFR 820 (Quality System Regulation)
- ISO 13485 (Medical devices - Quality management systems)
- EU MDR 2017/745 (Medical Device Regulation)
- IEC 62366 (Usability engineering)
- ISO 14971 (Risk management)

**Search Process:**
1. Use `mcp__context7__resolve-library-id` to confirm library ID
2. Use `mcp__context7__get-library-docs` to search related documents
3. Auto-save search results to Knowledge Base (caching)

### 3. Google Workspace Search

Search for regulatory-related information in Google services:

- **Gmail:** Regulatory correspondence from FDA, NB (Nominated Body), MFDS
- **Google Docs:** Collaborative documents, review materials
- **Google Drive:** Regulatory submission packages, evidence documents

## Search Process

### Step 1: Query Analysis

Analyze user search query to extract keywords and intent:

```
Input: "510(k) submission requirements for software medical device"
Keyword Extraction: ["510(k)", "submission", "requirements", "software", "medical device"]
Intent Classification: Regulatory requirements search
Data Source Priority: Notion > Context7 > Google
```

### Step 2: Parallel Search Execution

Execute simultaneous searches across all three data sources:

```
[Parallel]
1. Notion DB search (mcp__notion__query)
2. Context7 search (mcp__context7__get-library-docs)
3. Google search (mcp__google__search)
```

### Step 3: Result Integration and Scoring

Assign relevance scores to search results and sort using the SPEC-ARIA-004 defined algorithm:

```python
# SPEC-ARIA-004 S5.2 Relevance Scoring Algorithm
relevance_score = (
    keyword_match * 0.4 +        # Keyword match rate (exact/substring matches)
    semantic_similarity * 0.3 +   # Semantic similarity (contextual understanding)
    recency * 0.2 +               # Recency (recent documents prioritized, decay over time)
    source_authority * 0.1        # Source authority (official docs > internal > user-generated)
)

# Source Authority Weights:
# - Official Regulations (FDA, ISO, EU MDR): 1.0
# - Context7 MCP (verified regulatory docs): 0.95
# - Notion DB (company documents): 0.8
# - Google Workspace (emails, docs): 0.7
# - User-generated content: 0.5
```

### Step 4: Filtering and Sorting

Apply user-specified filters and sort results:

**Category Filters:**
- `requirements`: Regulatory requirements only
- `documents`: Document registry only
- `capa`: CAPA tracker only
- `risk`: Risk register only
- `submissions`: Submission tracker only
- `standards`: Standards/regulations only
- `emails`: Emails only
- `all`: All categories (default)

**Date Range Filters:**
```
--date "2024-01-01:2024-12-31"  # Specific date range
--date "last-30-days"             # Last 30 days
--date "last-12-months"            # Last 12 months
```

### Step 5: Display Results

Display results sorted by relevance:

```markdown
## Search Results: "510(k) submission requirements"

Total 23 results found (Notion: 12, Context7: 8, Google: 3)

### Top Results (90%+ relevance)

1. **[REQ-042] 21 CFR 807 Subpart E - 510(k) Requirements** (Notion)
   - Relevance: 95%
   - Source: Regulatory Requirements DB
   - Summary: 510(k) submission requirements, Predicate Device, Substantial Equivalence
   - Link: [Notion page](https://notion.so/req-042)

2. **[KB-156] 510(k) Software as Medical Device Guidance** (Context7)
   - Relevance: 92%
   - Source: FDA Guidance Document
   - Summary: SaMD 510(k) submission guidelines, testing requirements
   - Link: [Context7 document](...)

### Results by Category

**Requirements (8 items)**
- REQ-042: 21 CFR 807 Subpart E (95%)
- REQ-089: IEC 62304 Software Lifecycle (78%)
...

**Documents (5 items)**
- DOC-SOP-015: 510(k) Submission Process SOP (85%)
...

**Standards (6 items)**
- FDA Guidance: SaMD 510(k) (92%)
- ISO 13485 Clause 7.3 (72%)
...

**Emails (1 item)**
- FDA 510(k) Request Letter (68%)
```

## Advanced Features

### Auto Knowledge Base Update

Automatically save Context7 search results to Knowledge Base:

```yaml
Condition: Relevance score >= 80% AND not in Knowledge Base
Actions:
  1. Create new item in Knowledge Base DB
  2. Save source, summary, tags
  3. Notify user of "New knowledge item added"
```

### Related Document Recommendations

Recommend Notion pages related to search results:

```
Related Documents:
- CAPA-2024-003: 510(k) Submission Gap Analysis
- RISK-012: Software Validation Risk
- DOC-REP-028: Previous 510(k) Submission Report
```

### Search History Logging

Log all search queries to Audit Log DB:

```yaml
Fields:
  - Timestamp: Search time
  - Query: Search term
  - Results Count: Number of results
  - Top Result: Top result ID
  - User: User who performed search
```

## Filter Options Detail

### Category Filter

```
--filter requirements    # Regulatory requirements
--filter documents       # Document registry
--filter capa            # CAPA tracker
--filter risk            # Risk register
--filter submissions     # Submission tracker
--filter standards       # Standards/regulations (Context7)
--filter emails          # Emails (Gmail)
--filter all             # All categories (default)
```

### Source Filter

```
--source notion          # Notion DB only
--source context7        # Context7 only
--source google          # Google Workspace only
--source all             # All sources (default)
```

### Sort Options

```
--sort relevance         # By relevance (default)
--sort date              # Most recent first
--sort source            # Grouped by source
```

## Error Handling

### No Search Results

```
Search Results: No results found for "xyz abc"

Suggestions:
1. Generalize search terms (e.g., "software validation")
2. Try Context7 regulatory search
3. Consider adding new item to Knowledge Base
```

### API Rate Limiting

```
Notice: Throttling search rate (Notion API rate limit)
Estimated wait time: 30 seconds
```

### Authentication Expired

```
Error: Google OAuth authentication expired.
Resolution: Run /aria init google to re-authenticate
```

## Usage Examples

### Example 1: Regulatory Search

```
/aria search "21 CFR 820.30 design controls"
→ Searches Notion Regulatory Requirements, Context7 FDA docs
→ Returns Design Control requirements, related document recommendations
```

### Example 2: CAPA Search

```
/aria search "CAPA overdue" --filter capa
→ Searches CAPA Tracker DB for overdue items
→ Displays related Risk Register items
```

### Example 3: Email Search

```
/aria search "FDA 510(k) request" --filter emails --date "last-30-days"
→ Searches Gmail for FDA 510(k) related emails from last 30 days
→ Suggests connecting to related Notion pages
```

### Example 4: Comprehensive Search

```
/aria search "ISO 14971 risk management"
→ Searches Notion Risk Register, Context7 ISO 14971, Google Docs
→ Displays comprehensive risk management standards, related CAPAs, documents
```

## Completion Marker

Add `<aria:search:complete results=N>` marker when search completes. (N: result count)

## Notes

- Search displays up to 100 results ranked by relevance score
- Context7 search results are automatically cached in Knowledge Base (TTL: 30 days)
- Google Workspace search requires separate OAuth authentication
- Search history is saved to Audit Log DB for audit trail support

---

**Version:** 2.1.0 (Phase 4 - SPEC-ARIA-004 Milestone 5)
**Last Updated:** 2026-02-09
**Language:** English
**Core Principle:** Unified search across all ARIA data sources with MCP integration
**Spec Compliance:** SPEC-ARIA-004 ER-012, ER-013, UR-009
