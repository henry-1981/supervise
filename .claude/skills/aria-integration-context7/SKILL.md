---
name: aria-integration-context7
description: >
  Context7 MCP optimization for ARIA regulatory research. Provides optimized
  search patterns for FDA 21 CFR 820, ISO 13485, EU MDR 2017/745, automated
  knowledge base updates with weekly scheduling, 30-day search result caching,
  and Context7 query optimization for regulatory information retrieval.

license: Apache-2.0
compatibility: Designed for Claude Code with ARIA Phase 3+ agents
allowed-tools: Read Grep Glob Bash mcp__context7__resolve-library-id mcp__context7__get-library-docs
user-invocable: true
metadata:
  version: "1.0.0"
  category: "integration"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "context7, regulatory, search, optimization, caching, knowledge-base"
  author: "ARIA Development Team"
  context7-libraries: "fda-cfr, iso-standards, eu-mdr"
  related-skills: "aria-domain-raqa, aria-knowledge-fda, aria-knowledge-eumdr, aria-knowledge-standards"
  aliases: "aria-context7, regulatory-search"
  argument-hint: "Search query for regulatory information"
  context: "Optimizes Context7 MCP queries for RA/QA regulatory research"
  agent: "expert-regulatory, expert-standards, expert-researcher"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords: ["regulatory", "FDA", "21 CFR", "ISO 13485", "EU MDR", "Context7", "search", "knowledge base", "regulation lookup"]
  agents: ["expert-regulatory", "expert-standards", "expert-researcher", "expert-submission"]
  phases: ["execute"]
  languages: ["en"]
---

# aria-integration-context7

Context7 MCP optimization for ARIA regulatory research with automated knowledge management.

## Quick Reference (30 seconds)

### What This Skill Does

Optimizes Context7 MCP queries for regulatory information retrieval. Provides pre-configured search patterns for FDA 21 CFR 820 (QSR), ISO 13485 (QMS), and EU MDR 2017/745. Implements automated knowledge base updates with weekly scheduling, 30-day search result caching, and query optimization for faster regulatory research.

### When to Use

- Searching FDA 21 CFR 820 regulations for medical device QSR
- Looking up ISO 13485 requirements for quality management systems
- Researching EU MDR 2017/745 requirements for CE marking
- Building regulatory knowledge base with automated updates
- Optimizing repeated regulatory queries with caching
- Integrating Context7 with ARIA RA/QA workflow

### Core Capabilities

**Regulatory Search Patterns**: Pre-configured Context7 query templates for FDA, ISO, and EU MDR regulations. Optimized for regulatory terminology and citation formats.

**Knowledge Base Auto-Update**: Weekly automated knowledge base synchronization with latest regulatory updates. Configurable schedule with change detection.

**Search Result Caching**: 30-day TTL cache for Context7 query results. Reduces redundant API calls while maintaining data freshness.

**Query Optimization**: Batching, deduplication, and result ranking for efficient regulatory research. Integrates with ARIA VALID quality framework.

### Quick Commands

For FDA 21 CFR 820 searches, use mcp__context7__resolve-library-id with query "fda 21 cfr 820" to get library ID, then mcp__context7__get-library-docs with resolved ID and topic like "qsr requirements" or "design controls".

For ISO 13485 searches, use mcp__context7__resolve-library-id with query "iso 13485" to get library ID, then mcp__context7__get-library-docs with resolved ID and topic like "qms clauses" or "management responsibility".

For EU MDR searches, use mcp__context7__resolve-library-id with query "eu mdr 2017/745" to get library ID, then mcp__context7__get-library-docs with resolved ID and topic like "technical documentation" or "clinical evaluation".

---

## Implementation Guide (5 minutes)

### Regulatory Search Patterns

**FDA 21 CFR 820 QSR Patterns**:

Context7 library resolution for FDA 21 CFR 820 requires specific query formatting. Use "fda 21 cfr 820" or "fda qsr" as the base query. The resolved library ID typically maps to FDA electronic Code of Federal Regulations.

Search topics for FDA 21 CFR 820 include "quality system", "design controls", "corrective and preventive action", "record keeping", "servicing", "statistical techniques". Each major subpart (820.20 through 820.250) can be queried individually.

**ISO 13485 QMS Patterns**:

Context7 library resolution for ISO 13485 uses "iso 13485" or "iso 13485:2016" as the base query. The resolved library ID maps to ISO quality management system standards.

Search topics for ISO 13485 include "quality management system", "management responsibility", "resource management", "product realization", "measurement analysis", "improvement". Each clause (4 through 8) can be queried individually with specific requirements.

**EU MDR 2017/745 Patterns**:

Context7 library resolution for EU MDR uses "eu mdr 2017/745" or "medical device regulation" as the base query. The resolved library ID typically maps to EU MDR official documentation.

Search topics for EU MDR include "technical documentation", "clinical evaluation", "post-market surveillance", "vigilance", "market surveillance", "classification", "conformity assessment". Each chapter (I through X) can be queried with specific article references.

### Knowledge Base Auto-Update

**Weekly Schedule Configuration**:

Knowledge base auto-update runs on a weekly schedule, typically synchronized with regulatory publication cycles. FDA updates are published quarterly, ISO updates annually, and EU MDR updates as needed.

The auto-update mechanism uses three phases. Phase 1 performs change detection by comparing last update timestamps with regulatory publication schedules. Phase 2 executes incremental updates for changed regulations only. Phase 3 validates updated content and logs changes.

**Update Triggers**:

Automatic triggers include scheduled weekly execution, manual trigger via /aria knowledge refresh command, and detection of regulatory publication announcements. Each trigger logs the update reason and timestamp.

**Knowledge Base Storage**:

Knowledge base content is stored in Notion via Notion MCP for ARIA integration. Regulatory documents are organized by regulation type, chapter or clause hierarchy, and last update date. Each entry includes citation, section text, and source timestamp.

### Search Result Caching

**Cache Key Generation**:

Cache keys are generated from query parameters including library ID, search topic, and language. Hash function ensures consistent key generation for identical queries. Cache keys follow format: ctx7:{library_id}:{topic_hash}:{language}.

**30-Day TTL Enforcement**:

Cache entries store creation timestamp in Unix epoch format. TTL validation occurs on cache read, comparing current time with creation timestamp. Entries older than 30 days are automatically invalidated and removed. Cache cleanup runs during weekly knowledge base updates.

**Cache Invalidation**:

Manual cache invalidation occurs via /aria knowledge clear-cache command. Automatic invalidation occurs for entries exceeding TTL. Version-based invalidation occurs when regulatory updates are detected, ensuring stale data is removed.

### Context7 Query Optimization

**Batch Query Generation**:

Related queries are batched to reduce Context7 API calls. Batch queries group related topics by regulation and chapter hierarchy. Maximum batch size is 10 queries per batch to respect rate limits. Batch results are decomposed and cached individually.

**Result Deduplication**:

Duplicate results are identified by comparing citation, section number, and content hash. Deduplication occurs across batch results and cached entries. Unique results maintain original source attribution.

**Result Ranking**:

Search results are ranked by relevance score calculated from topic match quality, citation recency, and source authority. FDA regulations rank by subpart hierarchy. ISO standards rank by clause hierarchy. EU MDR ranks by chapter and article number.

---

## Advanced Implementation (10+ minutes)

### Integration with ARIA Workflow

**Brief Phase Integration**:

During Brief phase, use optimized Context7 queries to identify applicable regulations based on device classification and target markets. Regulatory search patterns provide preliminary requirements landscape.

**Execute Phase Integration**:

During Execute phase, leverage cached results for repeated regulatory lookups. Query optimization reduces research time for document drafting and requirements verification.

**Deliver Phase Integration**:

During Deliver phase, include source citations from Context7 results. Cached results provide traceability for VALID framework verification.

### VALID Quality Framework Integration

**Verified Dimension**:

Context7 source validation ensures content matches original regulation text. Cache metadata includes retrieval timestamp for audit trail.

**Accurate Dimension**:

Regulatory update validation ensures knowledge base reflects current requirements. Version tracking identifies last update date for each regulation.

**Linked Dimension**:

Traceability between citations and Context7 sources enables requirement-to-evidence linking. Cache keys maintain query-to-result mapping.

**Inspectable Dimension**:

Knowledge base change logs provide audit trail for regulatory updates. Cache invalidation events are logged with reasoning.

**Deliverable Dimension**:

Formatted regulatory citations meet submission package requirements. Context7 results export to standard formats for documentation.

### Error Handling and Recovery

**Context7 Unavailability**:

When Context7 MCP is unavailable, the system falls back to cached results if available. If no cached results exist, the system provides manual research guidance and logs the Context7 failure for investigation.

**Cache Corruption**:

Cache validation runs on startup to detect corrupted entries. Corrupted entries are automatically removed and regenerated. Cache rebuild process queries Context7 for missing entries.

**Regulatory Update Conflicts**:

When regulatory updates conflict with cached content, the system prioritizes newer content with version tracking. Conflict resolution logs both versions with timestamps and provides manual review flag for significant changes.

---

## Works Well With

**ARIA Knowledge Skills**:

- aria-knowledge-fda: FDA regulations content with Context7 optimization
- aria-knowledge-eumdr: EU MDR content with Context7 optimization
- aria-knowledge-standards: ISO standards content with Context7 optimization

**ARIA Domain Agents**:

- expert-regulatory: Regulatory strategy with optimized research
- expert-standards: Standards interpretation with automated updates
- expert-researcher: Regulatory information research with caching

**ARIA Integration**:

- aria-domain-raqa: RA/QA domain knowledge with optimized lookup
- Notion MCP: Knowledge base storage and synchronization
- ARIA VALID: Quality framework compliance verification

---

## Module Reference

For detailed implementation patterns, see the modules directory:

**regulatory-search-patterns.md**: Complete Context7 query templates for FDA 21 CFR 820, ISO 13485, EU MDR 2017/745, and citation formats.

**knowledge-base-management.md**: Weekly auto-update configuration, change detection, incremental update mechanisms, and Notion integration.

**caching-strategy.md**: Cache key generation, 30-day TTL enforcement, invalidation rules, and cleanup processes.

**query-optimization.md**: Batch query generation, result deduplication, relevance ranking, and performance optimization.

**examples/integration-examples.md**: Working code examples for Context7 integration with ARIA workflow.

---

## Troubleshooting

**Context7 Queries Return No Results**:

Verify library ID resolution with mcp__context7__resolve-library-id using correct query format. Check that Context7 MCP server is running in .mcp.json. Confirm search topic matches available content in the library.

**Cache Not Working**:

Check that cache directory exists with write permissions. Verify system time is correct for TTL validation. Review cache logs for validation errors. Manually clear cache with /aria knowledge clear-cache if needed.

**Knowledge Base Not Updating**:

Confirm weekly schedule is configured correctly. Check Notion MCP connection and permissions. Review update logs for error messages. Manually trigger update with /aria knowledge refresh if needed.

**Search Results Outdated**:

Check last update timestamp in knowledge base. Run manual knowledge refresh if updates are available. Verify regulatory publication sources for recent changes. Clear cache to force fresh queries if needed.

---

## Status

Production Ready (v1.0.0)
Last Updated: 2026-02-09
Maintained by: ARIA Development Team
Phase: ARIA Phase 4 - Universal Business Agents
