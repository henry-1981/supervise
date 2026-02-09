# ARIA MCP Integration Patterns

This document describes how ARIA agents and skills integrate with Model Context Protocol (MCP) servers for regulatory intelligence workflows.

## Overview

ARIA Phase 3 integrates with three MCP servers:

1. **Context7 MCP**: Up-to-date regulatory and standards documentation
2. **Notion MCP**: Central knowledge hub and document management
3. **Sequential Thinking MCP**: Complex regulatory analysis and decision-making

## MCP Tool Loading Protocol

All MCP tools are deferred and must be loaded before use:

```yaml
Step 1: Load MCP tools
Tool: ToolSearch
Parameters:
  query: "context7"
  max_results: 5

Step 2: Call loaded tool
Tool: mcp__context7__resolve-library-id
Parameters:
  query: "FDA 21 CFR 820"
```

---

## Context7 MCP Integration

### Purpose

Access up-to-date regulatory documentation and standards for accurate citations and research.

### FDA Regulation Lookup

**Use Case**: User asks about FDA QSR requirements for design control.

**Pattern**:
```yaml
Step 1: Resolve FDA library
Tool: mcp__context7__resolve-library-id
Parameters:
  query: "FDA 21 CFR 820 Quality System Regulation"

Expected Output:
  library_id: "fda-21-cfr-820"

Step 2: Get specific sections
Tool: mcp__context7__get-library-docs
Parameters:
  library_id: "fda-21-cfr-820"
  topics: ["design-control", "risk-analysis", "validation"]

Expected Output:
  - 21 CFR 820.30 Design controls
  - 21 CFR 820.30(g) Design validation
  - Related guidance documents
```

**Citation Format**: `[21 CFR 820.30]` for standard references in documents.

### ISO Standard Lookup

**Use Case**: User needs ISO 13485 requirements for quality management.

**Pattern**:
```yaml
Step 1: Resolve ISO library
Tool: mcp__context7__resolve-library-id
Parameters:
  query: "ISO 13485:2016 Medical devices QMS"

Expected Output:
  library_id: "iso-13485-2016"

Step 2: Get clauses
Tool: mcp__context7__get-library-docs
Parameters:
  library_id: "iso-13485-2016"
  topics: ["design-development", "risk-management", "document-control"]

Expected Output:
  - Clause 7.3 Design and development
  - Clause 8.5.2 Corrective action
  - Related standards (ISO 14971)
```

**Citation Format**: `[ISO 13485:2016, Clause 7.3]` for standard references.

### IEC Standard Lookup

**Use Case**: User asks about IEC 62304 software lifecycle requirements.

**Pattern**:
```yaml
Step 1: Resolve IEC library
Tool: mcp__context7__resolve-library-id
Parameters:
  query: "IEC 62304 Medical device software lifecycle"

Expected Output:
  library_id: "iec-62304"

Step 2: Get software class requirements
Tool: mcp__context7__get-library-docs
Parameters:
  library_id: "iec-62304"
  topics: ["software-class", "safety-classification", "testing"]

Expected Output:
  - Software Class A, B, C definitions
  - Testing requirements by class
  - Documentation requirements
```

**Citation Format**: `[IEC 62304, Clause 5.x]` for standard references.

### Version Verification

**Use Case**: Verify current version before citing in regulatory submission.

**Pattern**:
```yaml
Step 1: Get standard metadata
Tool: mcp__context7__get-library-docs
Parameters:
  library_id: "iso-14971"
  topics: ["version", "amendments"]

Step 2: Cross-reference with FDA recognition
Tool: mcp__context7__get-library-docs
Parameters:
  library_id: "fda-recognized-consensus-standards"
  topics: ["ISO 14971"]
```

### Error Handling

**No Results**: Standard not available in Context7
- Fallback: Web search for official standard body website
- Fallback: Refer to hard copy or internal document library

**Multiple Versions**: More than one version found
- Check user query for specific year (e.g., "ISO 13485:2016")
- Default to latest version if not specified
- Explicitly state version in citations

---

## Notion MCP Integration

### Purpose

Central knowledge hub for CAPA tracking, risk register, and document registry with full traceability.

### CAPA Creation

**Use Case**: User identifies nonconformity and needs to create CAPA record.

**Pattern**:
```yaml
Step 1: Create CAPA page
Tool: mcp__notion__create-page
Parameters:
  parent:
    database_id: "CAPA_TRACKER_DATABASE_ID"
  properties:
    "CAPA ID":
      title: [{ text: "CAPA-2026-001" }]
    "Problem Description":
      rich_text: [{ text: "Validation protocol missing acceptance criteria" }]
    "Source":
      select: { name: "Internal audit" }
    "Severity":
      select: { name: "Major" }
    "Status":
      select: { name: "Open" }]
    "Opened Date":
      date: { start: "2026-02-09" }
    "Assigned To":
      people: [{ id: "USER_ID" }]

Expected Output:
  page_id: "CAPA_PAGE_ID"

Step 2: Link to related risk (if applicable)
Tool: mcp__notion__update-page
Parameters:
  page_id: "CAPA_PAGE_ID"
  properties:
    "Related Risk ID":
      relation: [{ id: "RISK_PAGE_ID" }]
```

### Risk Registration

**Use Case**: User identifies new risk during design review and needs to register it.

**Pattern**:
```yaml
Step 1: Create risk entry
Tool: mcp__notion__create-page
Parameters:
  parent:
    database_id: "RISK_REGISTER_DATABASE_ID"
  properties:
    "Risk ID":
      title: [{ text: "RISK-2026-001" }]
    "Hazard Description":
      rich_text: [{ text: "Software failure could lead to incorrect diagnosis" }]
    "Harm":
      rich_text: [{ text: "Delayed or incorrect treatment" }]
    "Severity":
      select: { name: "Moderate" }]
    "Probability":
      select: { name: "Low" }]
    "Risk Priority Number":
      number: 6
    "Mitigation Status":
      select: { name: "Open" }]
    "Related Standard":
      multi_select: [{ name: "ISO 14971" }, { name: "IEC 62304" }]

Expected Output:
  page_id: "RISK_PAGE_ID"

Step 2: Link to design control (if applicable)
Tool: mcp__notion__update-page
Parameters:
  page_id: "RISK_PAGE_ID"
  properties:
    "Related Design Output":
      relation: [{ id: "DESIGN_OUTPUT_PAGE_ID" }]
```

### Document Registration

**Use Case**: User completes document and needs to register it in Document Registry.

**Pattern**:
```yaml
Step 1: Register document
Tool: mcp__notion__create-page
Parameters:
  parent:
    database_id: "DOCUMENT_REGISTRY_DATABASE_ID"
  properties:
    "Document ID":
      title: [{ text: "DHF-001-001" }]
    "Document Title":
      rich_text: [{ text: "Design Input - User Needs" }]
    "Document Type":
      select: { name: "Design Control" }]
    "Version":
      number: 1.0
    "Status":
      select: { name: "Approved" }]
    "Effective Date":
      date: { start: "2026-02-09" }
    "Related CAPA":
      relation: []  # Empty if no related CAPA
    "Related Risk":
      relation: [{ id: "RISK_PAGE_ID" }]  # If applicable

Expected Output:
  page_id: "DOC_PAGE_ID"
```

### Database Query

**Use Case**: User needs to review all open CAPAs for management review.

**Pattern**:
```yaml
Tool: mcp__notion__query-database
Parameters:
  database_id: "CAPA_TRACKER_DATABASE_ID"
  filter:
    property: "Status"
    select: { equals: "Open" }

Expected Output:
  - List of open CAPA pages with properties
  - CAPA ID, description, severity, due dates
```

### Relation Linking

**Use Case**: Link CAPA to Risk and Document for full traceability.

**Pattern**:
```yaml
Step 1: Link CAPA to Risk
Tool: mcp__notion__update-page
Parameters:
  page_id: "CAPA_PAGE_ID"
  properties:
    "Related Risk ID":
      relation: [{ id: "RISK_PAGE_ID" }]

Step 2: Link CAPA to resulting document
Tool: mcp__notion__update-page
Parameters:
  page_id: "CAPA_PAGE_ID"
  properties:
    "Related Documents":
      relation: [{ id: "DOC_PAGE_ID" }]

Step 3: Verify bidirectional links
Tool: mcp__notion__get-page
Parameters:
  page_id: "RISK_PAGE_ID"

Expected Output:
  Risk page shows "Related CAPA" relation back to CAPA_PAGE_ID
```

### Error Handling

**Database Not Found**: Invalid database ID
- Verify .moai/config/sections/knowledge.yaml for correct IDs
- Prompt user to confirm database exists in workspace

**Permission Error**: Insufficient Notion permissions
- Prompt user to check Notion integration settings
- Suggest manual entry as fallback

**Missing Property**: Database schema mismatch
- Check template in knowledge.yaml
- Prompt user for manual update to Notion database

---

## Sequential Thinking MCP Integration

### Purpose

Complex regulatory analysis requiring multi-step reasoning, assumption auditing, and bias detection.

### Regulatory Pathway Analysis

**Use Case**: User asks for optimal FDA submission pathway (510(k) vs PMA vs De Novo).

**Pattern**:
```yaml
Tool: mcp__sequential-thinking__sequentialthinking
Prompt: |
  Analyze optimal FDA submission pathway for [device description]:

  1. Assumption Audit
     - What device classification are we assuming?
     - What predicate device are we assuming exists?
     - What risks are we assuming are acceptable?

  2. First Principles
     - What is the statutory definition of this device type?
     - What is the FDA's primary safety concern for this category?
     - What evidence standard is required by law?

  3. Alternative Generation
     - 510(k): Predicate device exists, substantial equivalence
     - De Novo: New device, low-moderate risk, no predicate
     - PMA: High risk, no predicate, high safety concerns
     - Exempt: Class I, low risk, general controls sufficient

  4. Trade-off Analysis
     - Timeline: 510(k) (3-12 mo) vs De Novo (6-12 mo) vs PMA (12-36 mo)
     - Cost: 510(k) ($$) vs De Novo ($$$) vs PMA ($$$$)
     - Success Probability: 510(k) (high) vs De Novo (medium) vs PMA (variable)
     - Data Requirements: 510(k) (bench/comparison) vs PMA (clinical)

  5. Bias Check
     - Anchoring bias: Are we biased toward familiar pathway?
     - Availability bias: Overweighting recent case studies?
     - Confirmation bias: Ignoring evidence suggesting higher-risk pathway?

Expected Output:
  Structured reasoning with:
  - Recommended pathway with rationale
  - Identified assumptions and their validity
  - Trade-off comparison table
  - Flagged potential biases
  - Confidence level in recommendation
```

### Multi-Market Strategy

**Use Case**: User needs simultaneous US, EU, and Korea market entry strategy.

**Pattern**:
```yaml
Tool: mcp__sequential-thinking__sequentialthinking
Prompt: |
  Optimize regulatory strategy for simultaneous US, EU, Korea entry:

  1. Assumption Audit
     - Are we assuming identical device classification across markets?
     - Are we assuming simultaneous submission is feasible?
     - Are we assuming clinical data is transferrable?

  2. First Principles
     - US: 510(k)/PMA pathway, safety and effectiveness
     - EU: MDR classification, clinical evaluation, state-of-the-art
     - Korea: MFDS approval, KGMP requirement, local clinical data

  3. Alternative Generation
     - Sequential: US → EU → Korea (carryover data)
     - Parallel: Simultaneous submissions (highest cost, fastest time)
     - Staggered: US + EU → Korea (leverage data sharing)

  4. Dependency Analysis
     - Predicate device availability (US-specific)
     - Clinical study acceptability (EU MDR stricter than FDA)
     - Local testing requirements (Korea biocompatibility)

  5. Optimization
     - Minimize total time to market (critical mass)
     - Minimize total cost (resource allocation)
     - Maximize data reuse (study design)

Expected Output:
  Recommended sequence with:
  - Timeline projection by market
  - Cost comparison by strategy
  - Critical path dependencies
  - Data reuse opportunities
  - Risk mitigation for each market
```

### Risk-Benefit Analysis

**Use Case**: User needs to justify residual risk in regulatory submission.

**Pattern**:
```yaml
Tool: mcp__sequential-thinking__sequentialthinking
Prompt: |
  Evaluate risk-benefit balance for [identified residual risk]:

  1. Assumption Audit
     - Are we assuming benefit is clinically meaningful?
     - Are we assuming risk probability is accurate?
     - Are we assuming alternatives are less acceptable?

  2. First Principles (ISO 14971)
     - Residual risk must be acceptable
     - Benefit must outweigh risk
     - Risk must be minimized as far as possible
     - Both individual and societal benefit considered

  3. Benefit Quantification
     - Clinical benefit magnitude (health outcome improvement)
     - Availability of alternative treatments
     - Impact on quality of life
     - Societal benefit (cost reduction, access)

  4. Risk Characterization
     - Severity of harm (worst-case scenario)
     - Probability of occurrence (with current controls)
     - Detectability (monitoring capability)
     - Reversibility (ability to mitigate after occurrence)

  5. Alternative Analysis
     - What if risk elimination required design change?
     - What if probability reduction required costly controls?
     - What if alternative treatments have worse risk-benefit?

  6. Bias Check
     - Availability bias: Overweighting easily imagined harms?
     - Omission bias: Preferring inaction over action despite benefit?
     - Status quo bias: Underestimating risk of existing treatments?

Expected Output:
  Risk-benefit justification with:
  - Quantified benefit magnitude
  - Characterized residual risk
  - Comparison to available alternatives
  - ISO 14971 compliance rationale
  - Identified cognitive biases and mitigation
```

### Root Cause Analysis

**Use Case**: User needs to investigate root cause of nonconformity for CAPA.

**Pattern**:
```yaml
Tool: mcp__sequential-thinking__sequentialthinking
Prompt: |
  Conduct root cause analysis for [nonconformity description]:

  1. Problem Definition
     - What specifically happened?
     - What should have happened?
     - What is the gap (deviation)?

  2. 5 Whys Analysis
     - Why did the nonconformity occur?
     - Why did that cause happen?
     - (Continue 5 levels deep)

  3. Fishbone (Ishikawa) Exploration
     - Man: Training, competence, fatigue
     - Machine: Equipment capability, maintenance
     - Material: Input quality, specifications
     - Method: Process design, validation
     - Environment: Conditions, external factors
     - Measurement: Inspection, test methods

  4. System vs Root Cause
     - Is this a symptom or system issue?
     - Would fixing this prevent recurrence?
     - Is this within our control to change?

  5. Solution Alternative
     - Containment (immediate action)
     - Correction (fix current issue)
     - Corrective Action (prevent recurrence)
     - Preventive Action (prevent future occurrence)

Expected Output:
  Root cause analysis with:
  - Identified root cause (not symptom)
  - Contributing factors mapped
  - Recommended corrective actions
  - Preventive action recommendations
  - Verification methods for effectiveness
```

### Error Handling

**Timeout**: Analysis exceeds token limit
- Simplify prompt by reducing scope
- Break into multiple analyses
- Suggest manual reasoning as fallback

**Inconclusive**: No clear recommendation emerges
- Explicitly state uncertainty
- Present multiple options with trade-offs
- Request user input for decision criteria

**Contradictory Results**: Analysis produces conflicting conclusions
- Re-run with emphasis on conflict resolution
- Identify sources of contradiction
- Present both perspectives for user decision
```

## Integration Examples

### Example 1: Design Control with Full MCP Stack

User asks: "What design control requirements apply to our software-as-medical-device?"

```yaml
Step 1: Context7 - Get FDA design control requirements
Tool: mcp__context7__get-library-docs
library_id: "fda-21-cfr-820"
topics: ["design-control", "software-validation"]

Step 2: Context7 - Get IEC 62304 software classification
Tool: mcp__context7__get-library-docs
library_id: "iec-62304"
topics: ["software-class", "safety-classification"]

Step 3: Sequential Thinking - Determine software class
Tool: mcp__sequential-thinking__sequentialthinking
prompt: |
  Analyze device for IEC 62304 software class:
  1. What is the severity of harm if software fails?
  2. What is the probability of software failure?
  3. Can software failure be detected by user?
  4. Class determination (A/B/C) with rationale

Step 4: Notion - Create design output document
Tool: mcp__notion__create-page
parent: { database_id: "DOCUMENT_REGISTRY" }
properties:
  "Document Type": "Design Output"
  "Related Standard": ["21 CFR 820.30", "IEC 62304"]

Expected Result:
  Document cites [21 CFR 820.30(g)] and [IEC 62304, Clause 5.x]
  Registered in Document Registry with standard references
```

### Example 2: CAPA from Audit Finding

User asks: "Audit found we're missing design reviews. Create CAPA."

```yaml
Step 1: Context7 - Verify requirement
Tool: mcp__context7__get-library-docs
library_id: "iso-13485-2016"
topics: ["design-review", "clause-7.3.4"]

Step 2: Sequential Thinking - Root cause analysis
Tool: mcp__sequential-thinking__sequentialthinking
prompt: |
  Root cause analysis for missing design reviews:
  1. Why were reviews not documented?
  2. Why was the process not followed?
  3. Systemic issue vs one-time oversight?
  4. Corrective action to prevent recurrence

Step 3: Notion - Create CAPA
Tool: mcp__notion__create-page
parent: { database_id: "CAPA_TRACKER" }
properties:
  "Problem Description": "Design reviews not documented per ISO 13485:2016, Clause 7.3.4"
  "Source": "External audit"
  "Related Standard": ["ISO 13485:2016"]

Step 4: Notion - Link to process document (if exists)
Tool: mcp__notion__update-page
properties:
  "Related Documents": [{ relation: "DESIGN_PROCESS_DOC_ID" }]

Expected Result:
  CAPA cites [ISO 13485:2016, Clause 7.3.4]
  Root cause analysis documented
  Linked to design process for traceability
```

## Best Practices

### Context7 MCP
- Always resolve library ID before getting docs
- Verify version number before citing
- Use standard citation format: `[Standard] Section [Number]`
- Cross-reference multiple standards when applicable

### Notion MCP
- Always link related records (CAPA ↔ Risk ↔ Document)
- Use select options consistently (check templates)
- Verify page creation before linking relations
- Query existing records before creating duplicates

### Sequential Thinking MCP
- Use structured prompts with numbered steps
- Always include bias checking step
- Request confidence levels in conclusions
- Break complex analyses into smaller components

### Error Recovery
- When MCP tools fail, fallback to web search (Context7)
- When Notion fails, prompt for manual entry
- When analysis times out, simplify and retry

## Version History

- v1.0.0 (2026-02-09): Initial Phase 3 documentation
