# ARIA MCP Tool Reference

Complete reference for all MCP tools used in ARIA regulatory intelligence workflows.

## Tool Loading Protocol

All MCP tools are deferred and must be loaded before use:

```yaml
Step 1: Search and load tools
Tool: ToolSearch
Parameters:
  query: "context7"  # or "sequential-thinking", "notion"
  max_results: 5

Result:
  - Tool is now loaded and available for direct call

Step 2: Call loaded tool directly
Tool: mcp__context7__resolve-library-id
Parameters:
  query: "FDA 21 CFR 820"
```

---

## Context7 MCP Tools

### mcp__context7__resolve-library-id

**Purpose**: Resolve a regulatory library identifier from a query string.

**Parameters**:
```yaml
query (required): string
  Examples:
    - "FDA 21 CFR 820"
    - "ISO 13485:2016"
    - "IEC 62304"
    - "ISO 14971"
```

**Returns**:
```yaml
library_id: string
  Example: "fda-21-cfr-820"

libraries: array of matching libraries
  - name: Display name
  - id: Library identifier
  - version: Version or year
```

**Example Usage**:
```yaml
Tool: mcp__context7__resolve-library-id
Parameters:
  query: "FDA 21 CFR 820 Quality System Regulation"

Expected Output:
  library_id: "fda-21-cfr-820"
  name: "21 CFR Part 820 - Quality System Regulation"
  version: "Current"
```

**Common Library IDs**:
| Regulation/Standard | Library ID |
|---------------------|------------|
| FDA 21 CFR 820 | fda-21-cfr-820 |
| FDA 21 CFR 820.30 (Design Control) | fda-21-cfr-820-30 |
| ISO 13485:2016 | iso-13485-2016 |
| ISO 14971:2019 | iso-14971-2019 |
| IEC 62304 | iec-62304 |
| IEC 60601-1 | iec-60601-1 |
| EU MDR | eu-mdr-2017-745 |

**Error Handling**:
- **No results**: Query too specific or standard not in Context7
  - Retry with simpler query
  - Verify standard name spelling
  - Use alternative source (web search)

- **Multiple results**: More than one standard matches
  - Check version year in query
  - Select most appropriate from list
  - Explicitly state selected version

---

### mcp__context7__get-library-docs

**Purpose**: Retrieve documentation content for a specific regulatory library.

**Parameters**:
```yaml
library_id (required): string
  From resolve-library-id result
  Example: "fda-21-cfr-820"

topics (optional): array of strings
  Filter documentation by topics
  Examples:
    - ["design-control"]
    - ["risk-management", "risk-analysis"]
    - ["validation", "verification"]

full_content (optional): boolean
  Return full documentation or summarized
  Default: false (summarized)
```

**Returns**:
```yaml
sections: array of documentation sections
  - title: Section title
  - content: Section text/requirements
  - citation: Standard citation
  - subsections: Nested sections if applicable

topics: array of topics covered
  matches requested topics or all topics

metadata: object
  - version: Standard version
  - effective_date: When standard became effective
  - amendments: List of amendments
```

**Example Usage**:
```yaml
Tool: mcp__context7__get-library-docs
Parameters:
  library_id: "fda-21-cfr-820"
  topics: ["design-control"]

Expected Output:
  sections:
    - title: "21 CFR 820.30 Design Controls"
      content: "Each manufacturer shall establish and maintain procedures..."
      citation: "[21 CFR 820.30]"
      subsections:
        - title: "820.30(a) Design and development planning"
        - title: "820.30(b) Design input"
        - title: "820.30(c) Design output"
        - title: "820.30(d) Design review"
        - title: "820.30(e) Design verification"
        - title: "820.30(f) Design validation"
        - title: "820.30(g) Design transfer"
        - title: "820.30(h) Design changes"
```

**Topic Examples by Standard**:

**FDA 21 CFR 820**:
```yaml
topics:
  - quality-system
  - design-control
  - risk-analysis
  - document-control
  - purchasing-controls
  - identification-traceability
  - production-process-controls
  - acceptance-activities
  - nonconforming-product
  - corrective-preventive-action
  - labeling-packaging
  - installation- servicing
  - records
  - servicing-statistics
```

**ISO 13485:2016**:
```yaml
topics:
  - quality-management-system
  - management-responsibility
  - resource-management
  - product-realization
  - design-development
  - purchasing
  - production-service-provision
  - control-of-monitoring-measuring
  - measurement-analysis-improvement
```

**ISO 14971:2019**:
```yaml
topics:
  - risk-analysis
  - risk-evaluation
  - risk-control
  - overall-residual-risk-acceptability
  - risk-management-review
  - production-post-production
```

**IEC 62304**:
```yaml
topics:
  - software-class
  - safety-classification
  - software-development-process
  - software-testing
  - software-maintenance
```

**Error Handling**:
- **Invalid library_id**: Library not found
  - Re-run resolve-library-id to get correct ID
  - Check for typos in library_id

- **No matching topics**: Requested topics not in standard
  - Use broader topics
  - Request full content without topic filter
  - Check standard table of contents for correct topic names

---

## Notion MCP Tools

### mcp__notion__create-page

**Purpose**: Create a new page in a Notion database.

**Parameters**:
```yaml
parent (required): object
  database_id: string
    From .moai/config/sections/knowledge.yaml
    Examples:
      - CAPA_TRACKER_DATABASE_ID
      - RISK_REGISTER_DATABASE_ID
      - DOCUMENT_REGISTRY_DATABASE_ID

properties (required): object
  Varies by database schema
  Common property types:
    - title: Page title (required)
    - rich_text: Multi-line text
    - select: Single select option
    - multi_select: Multiple select options
    - date: Date value
    - number: Numeric value
    - people: User reference
    - relation: Link to other pages
    - files: File attachment
```

**CAPA Tracker Properties**:
```yaml
properties:
  "CAPA ID":
    title:
      text: "CAPA-2026-001"

  "Problem Description":
    rich_text:
      text: "Detailed description of nonconformity..."

  "Source":
    select:
      name: "Internal audit"
      # Options: Internal audit, External audit, Customer complaint, FDA observation, etc.

  "Severity":
    select:
      name: "Major"
      # Options: Critical, Major, Minor

  "Status":
    select:
      name: "Open"
      # Options: Open, In Progress, Closed, Verified

  "Opened Date":
    date:
      start: "2026-02-09"

  "Target Date":
    date:
      start: "2026-03-09"

  "Assigned To":
    people:
      id: "USER_ID"

  "Related Risk ID":
    relation:
      - id: "RISK_PAGE_ID"

  "Related Documents":
    relation:
      - id: "DOC_PAGE_ID"
```

**Risk Register Properties**:
```yaml
properties:
  "Risk ID":
    title:
      text: "RISK-2026-001"

  "Hazard Description":
    rich_text:
      text: "Description of hazard scenario..."

  "Harm":
    rich_text:
      text: "Potential harm from hazard..."

  "Severity":
    select:
      name: "Moderate"
      # Options: Catastrophic, Critical, Moderate, Minor, Negligible

  "Probability":
    select:
      name: "Low"
      # Options: Frequent, Probable, Occasional, Remote, Improbable

  "Risk Priority Number":
    number: 6
      # Severity × Probability (1-25 scale)

  "Mitigation Status":
    select:
      name: "Open"
      # Options: Open, In Progress, Mitigated, Accepted, Eliminated

  "Related Standard":
    multi_select:
      - name: "ISO 14971"
      - name: "IEC 62304"

  "Related Design Output":
    relation:
      - id: "DESIGN_OUTPUT_PAGE_ID"
```

**Document Registry Properties**:
```yaml
properties:
  "Document ID":
    title:
      text: "DHF-001-001"

  "Document Title":
    rich_text:
      text: "Design Input - User Needs"

  "Document Type":
    select:
      name: "Design Control"
      # Options: Design Control, SOP, Work Instruction, Form, Record, etc.

  "Version":
    number: 1.0

  "Status":
    select:
      name: "Approved"
      # Options: Draft, Under Review, Approved, Superseded, Withdrawn

  "Effective Date":
    date:
      start: "2026-02-09"

  "Related CAPA":
    relation:
      - id: "CAPA_PAGE_ID"

  "Related Risk":
    relation:
      - id: "RISK_PAGE_ID"
```

**Example Usage**:
```yaml
Tool: mcp__notion__create-page
Parameters:
  parent:
    database_id: "CAPA_TRACKER_DATABASE_ID"
  properties:
    "CAPA ID":
      title: [{ text: "CAPA-2026-001" }]
    "Problem Description":
      rich_text: [{ text: "Design validation protocol missing acceptance criteria per 21 CFR 820.30(g)" }]
    "Source":
      select: { name: "Internal audit" }
    "Severity":
      select: { name: "Major" }]
    "Status":
      select: { name: "Open" }]
    "Opened Date":
      date: { start: "2026-02-09" }
    "Assigned To":
      people: [{ id: "USER_ID" }]

Expected Output:
  id: "PAGE_ID"
  url: "https://notion.so/page/PAGE_ID"
```

**Error Handling**:
- **Invalid database_id**: Database not found
  - Verify database ID in knowledge.yaml
  - Check database exists in workspace
  - Confirm integration permissions

- **Missing required property**: Property not in database schema
  - Check database template for required properties
  - Verify property names match exactly
  - Use Select options that exist in database

- **Invalid select option**: Option not in database
  - Check database for exact option names
  - Case-sensitive matching
  - Create option in database if needed

---

### mcp__notion__update-page

**Purpose**: Update an existing Notion page (typically for adding relations).

**Parameters**:
```yaml
page_id (required): string
  From create-page result or query-database

properties (required): object
  Subset of properties to update
  Common use: Add relations after page creation
```

**Example Usage**:
```yaml
Step 1: Create page first
Tool: mcp__notion__create-page
... (creates CAPA page, returns page_id)

Step 2: Update with relation
Tool: mcp__notion__update-page
Parameters:
  page_id: "CAPA_PAGE_ID"
  properties:
    "Related Risk ID":
      relation: [{ id: "RISK_PAGE_ID" }]

Expected Output:
  id: "CAPA_PAGE_ID"
  properties:
    "Related Risk ID":
      relation: [{ id: "RISK_PAGE_ID" }]
```

**Relation Linking Pattern**:
```yaml
# Bidirectional linking
Tool: mcp__notion__update-page
Parameters:
  page_id: "CAPA_PAGE_ID"
  properties:
    "Related Risk ID":
      relation: [{ id: "RISK_PAGE_ID" }]

# Then verify Risk page shows back-link
Tool: mcp__notion__get-page
Parameters:
  page_id: "RISK_PAGE_ID"

Expected Output:
  Risk page has "Related CAPA" property with CAPA_PAGE_ID relation
```

**Error Handling**:
- **Page not found**: Invalid page_id
  - Verify page_id from previous operation
  - Check page still exists in Notion

- **Property not in database**: Attempting to add non-existent property
  - Check database schema for correct property names
  - Don't create new properties via update

- **Relation not allowed**: Relation property doesn't exist
  - Verify database has relation property configured
  - Check relation is to correct database type

---

### mcp__notion__query-database

**Purpose**: Query Notion database to find pages matching filter criteria.

**Parameters**:
```yaml
database_id (required): string
  From .moai/config/sections/knowledge.yaml

filter (optional): object
  property: string
    Property name to filter on
  type: string
    Property type (text, number, select, date, etc.)
  condition: varies by type
    Text: { equals: "value", contains: "text" }
    Number: { equals: 1, greater_than: 5 }
    Select: { equals: "Open", does_not_equal: "Closed" }
    Date: { on_or_before: "2026-02-09" }

sorts (optional): array of sort objects
  property: string
    Property to sort on
  direction: string
    "ascending" or "descending"
```

**Example Queries**:

**Find all open CAPAs**:
```yaml
Tool: mcp__notion__query-database
Parameters:
  database_id: "CAPA_TRACKER_DATABASE_ID"
  filter:
    property: "Status"
    select: { equals: "Open" }
  sorts:
    - property: "Opened Date"
      direction: "descending"

Expected Output:
  results:
    - id: "PAGE_ID_1"
      properties:
        "CAPA ID": "CAPA-2026-001"
        "Status": "Open"
        "Severity": "Major"
    - id: "PAGE_ID_2"
      properties:
        "CAPA ID": "CAPA-2026-002"
        "Status": "Open"
        "Severity": "Critical"
```

**Find high-priority risks**:
```yaml
Tool: mcp__notion__query-database
Parameters:
  database_id: "RISK_REGISTER_DATABASE_ID"
  filter:
    property: "Risk Priority Number"
    number: { greater_than_or_equal_to: 15 }

Expected Output:
  results:
    - id: "RISK_PAGE_ID"
      properties:
        "Risk ID": "RISK-2026-001"
        "Risk Priority Number": 20
        "Mitigation Status": "Open"
```

**Find documents by type**:
```yaml
Tool: mcp__notion__query-database
Parameters:
  database_id: "DOCUMENT_REGISTRY_DATABASE_ID"
  filter:
    property: "Document Type"
    select: { equals: "Design Control" }

Expected Output:
  results:
    - id: "DOC_PAGE_ID"
      properties:
        "Document ID": "DHF-001-001"
        "Document Title": "Design Input"
        "Document Type": "Design Control"
```

**Error Handling**:
- **No results**: Query returns no matching pages
  - Verify filter criteria
  - Check database has matching data
  - Try broader filter

- **Invalid filter**: Property or filter type mismatch
  - Verify property name exists in database
  - Check property type matches filter type
  - Use correct filter syntax for property type

---

### mcp__notion__get-page

**Purpose**: Retrieve a single page's full content and properties.

**Parameters**:
```yaml
page_id (required): string
  From create-page, query-database, or known page ID
```

**Example Usage**:
```yaml
Tool: mcp__notion__get-page
Parameters:
  page_id: "RISK_PAGE_ID"

Expected Output:
  id: "RISK_PAGE_ID"
  properties:
    "Risk ID": "RISK-2026-001"
    "Hazard Description": "Software failure..."
    "Harm": "Incorrect diagnosis..."
    "Severity": "Moderate"
    "Probability": "Low"
    "Risk Priority Number": 6
    "Mitigation Status": "Open"
    "Related Standard": ["ISO 14971"]
    "Related CAPA":
      - id: "CAPA_PAGE_ID"
        properties:
          "CAPA ID": "CAPA-2026-001"
```

**Error Handling**:
- **Page not found**: Invalid page_id or page deleted
  - Verify page_id from previous operation
  - Check page exists in Notion workspace

---

## Sequential Thinking MCP Tools

### mcp__sequential-thinking__sequentialthinking

**Purpose**: Complex multi-step reasoning with assumption auditing and bias detection.

**Parameters**:
```yaml
prompt (required): string
  Structured reasoning prompt with numbered steps

  Recommended structure:
    1. Assumption Audit
    2. First Principles
    3. Alternative Generation
    4. Analysis/Trade-offs
    5. Bias Check
    6. Conclusion with confidence level
```

**Returns**:
```yaml
reasoning: string
  Step-by-step reasoning process

assumptions: array of identified assumptions
  - assumption: Statement
  - validity: Valid/Questionable/Invalid
  - rationale: Why assumption is questionable

alternatives: array of alternatives considered
  - option: Alternative description
  - pros: Advantages
  - cons: Disadvantages
  - score: Numeric score (if applicable)

biases: array of cognitive biases detected
  - bias_type: Name of bias (anchoring, availability, confirmation, etc.)
  - description: How bias may affect reasoning
  - mitigation: How to reduce bias impact

conclusion: string
  Final recommendation or determination

confidence: string
  Confidence level (High/Medium/Low)
  Rationale for confidence level
```

**Prompt Templates**:

**Regulatory Pathway Analysis**:
```yaml
prompt: |
  Analyze optimal regulatory pathway for [device description]:

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

  6. Conclusion
     - Recommended pathway with rationale
     - Confidence level (High/Medium/Low)
     - Critical assumptions that must hold true
     - What would change recommendation
```

**Risk-Benefit Analysis**:
```yaml
prompt: |
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

  7. Conclusion
     - Is residual risk acceptable per ISO 14971?
     - Benefit-risk justification
     - Confidence level
     - Documentation requirements for submission
```

**Root Cause Analysis**:
```yaml
prompt: |
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

  5. Solution Alternatives
     - Containment (immediate action)
     - Correction (fix current issue)
     - Corrective Action (prevent recurrence)
     - Preventive Action (prevent future occurrence)

  6. Bias Check
     - Fundamental attribution error: Blaming person vs process?
     - Confirmation bias: Seeking evidence that confirms initial theory?
     - Sunk cost fallacy: Defending previous decisions?

  7. Conclusion
     - Root cause statement (not symptom)
     - Contributing factors
     - Recommended corrective/preventive actions
     - Verification methods
     - Confidence level in root cause identification
```

**Multi-Market Strategy**:
```yaml
prompt: |
  Optimize regulatory strategy for simultaneous [US, EU, Korea] entry:

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

  6. Bias Check
     - Home country bias: Overweighting familiar market?
     - Status quo bias: Defaulting to sequential approach?
     - Optimism bias: Underestimating multi-market complexity?

  7. Conclusion
     - Recommended market entry sequence
     - Timeline projection by market
     - Cost comparison
     - Critical path dependencies
     - Confidence level
```

**Example Usage**:
```yaml
Tool: mcp__sequential-thinking__sequentialthinking
Parameters:
  prompt: |
    Analyze optimal FDA submission pathway for AI diagnostic software:

    1. Assumption Audit
       - Device Class: II (presumed)
       - Predicate: Similar AI software exists (presumed)
       - Risk: Algorithm bias risk acceptable (presumed)

    2. First Principles
       - Device safety: Software failure could misdiagnose
       - Effectiveness: Must show diagnostic accuracy
       - Predicates: FDA has cleared similar AI software

    3. Alternatives
       - 510(k): Cite Software as a Medical Device (SaMD) predicates
       - De Novo: New AI technology, no direct predicate
       - Breakthrough: If designated, expedited review possible

    4. Trade-offs
       - 510(k): Faster, lower cost, but requires good predicate match
       - De Novo: No predicate needed, but longer, higher cost
       - Breakthrough: Fastest, but requires qualifying criteria

    5. Bias Check
       - Anchoring: Defaulting to 510(k) without good predicate?
       - Availability: Overweighting recent De Novo approvals?

    6. Conclusion
       - Recommend pathway based on predicate availability analysis

Expected Output:
  reasoning: "Step-by-step analysis..."

  assumptions:
    - assumption: "Device is Class II"
      validity: "Valid"
      rationale: "FDA classifies diagnostic software as Class II"

    - assumption: "Suitable predicate exists"
      validity: "Questionable"
      rationale: "AI is rapidly evolving, exact predicates may not exist"

  alternatives:
    - option: "510(k)"
      pros: ["3-12 month timeline", "Lower cost", "Predictable pathway"]
      cons: ["Requires predicate", "Algorithm changes may require new 510(k)"]
      score: 7/10

    - option: "De Novo"
      pros: ["No predicate required", "Creates new predicate"]
      cons: ["6-12 month timeline", "Higher cost", "Uncertain outcome"]
      score: 5/10

  biases:
    - bias_type: "Availability bias"
      description: "Recent De Novo approvals may make pathway seem more common"
      mitigation: "Search FDA database for actual predicate options"

  conclusion: "Recommended pathway: 510(k) if suitable predicate found; otherwise De Novo"

  confidence: "Medium - depends on predicate search results"
```

**Error Handling**:
- **Timeout**: Analysis exceeds token limit or processing time
  - Simplify prompt by reducing scope
  - Break into multiple smaller analyses
  - Focus on most critical aspects first

- **Inconclusive**: No clear recommendation emerges
  - Explicitly state uncertainty in output
  - Present multiple options with trade-offs
  - Request user input for decision criteria

- **Contradictory Results**: Analysis produces conflicting conclusions
  - Re-run with emphasis on conflict resolution
  - Identify sources of contradiction
  - Present both perspectives for user decision

---

## MCP Configuration

### .mcp.json Configuration

Context7, Notion, and Sequential Thinking MCP servers must be configured in `.mcp.json`:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/client-mcp"]
    }
  }
}
```

### Knowledge Base Configuration

Notion database IDs must be configured in `.moai/config/sections/knowledge.yaml`:

```yaml
knowledge:
  notion:
    capa_tracker_database_id: "CAPA_TRACKER_DATABASE_ID"
    risk_register_database_id: "RISK_REGISTER_DATABASE_ID"
    document_registry_database_id: "DOCUMENT_REGISTRY_DATABASE_ID"

  context7:
    default_standards:
      - fda-21-cfr-820
      - iso-13485-2016
      - iso-14971-2019
      - iec-62304
      - iec-60601-1
```

---

## Tool Selection Guide

| Task | Tool | Key Parameters |
|------|------|----------------|
| Look up FDA regulation | `mcp__context7__resolve-library-id` + `mcp__context7__get-library-docs` | query: "FDA 21 CFR 820", topics: ["design-control"] |
| Look up ISO standard | `mcp__context7__resolve-library-id` + `mcp__context7__get-library-docs` | query: "ISO 13485:2016", topics: ["clause-7.3"] |
| Create CAPA record | `mcp__notion__create-page` | database_id: CAPA_TRACKER, properties: {...} |
| Register risk | `mcp__notion__create-page` | database_id: RISK_REGISTER, properties: {...} |
| Link CAPA to risk | `mcp__notion__update-page` | page_id: CAPA_ID, properties: { "Related Risk ID": relation } |
| Find open CAPAs | `mcp__notion__query-database` | database_id: CAPA_TRACKER, filter: { Status: "Open" } |
| Analyze regulatory pathway | `mcp__sequential-thinking__sequentialthinking` | prompt: structured pathway analysis |
| Root cause analysis | `mcp__sequential-thinking__sequentialthinking` | prompt: 5 whys + fishbone analysis |
| Risk-benefit analysis | `mcp__sequential-thinking__sequentialthinking` | prompt: ISO 14971 framework |

---

## Common Workflows

### Workflow 1: Regulatory Research + Documentation

```yaml
Step 1: Look up regulation
Tool: mcp__context7__get-library-docs
library_id: "fda-21-cfr-820"
topics: ["design-control"]

Step 2: Analyze requirements
Tool: mcp__sequential-thinking__sequentialthinking
prompt: "Map 21 CFR 820.30 requirements to our design process"

Step 3: Create document
Tool: mcp__notion__create-page
database_id: DOCUMENT_REGISTRY
properties: { "Document Type": "Design Control", "Related Standard": ["21 CFR 820.30"] }
```

### Workflow 2: CAPA from Nonconformity

```yaml
Step 1: Verify requirement
Tool: mcp__context7__get-library-docs
topics: ["nonconforming-product", "capa"]

Step 2: Root cause analysis
Tool: mcp__sequential-thinking__sequentialthinking
prompt: "Root cause analysis for nonconformity..."

Step 3: Create CAPA
Tool: mcp__notion__create-page
database_id: CAPA_TRACKER

Step 4: Link to risk (if applicable)
Tool: mcp__notion__update-page
properties: { "Related Risk ID": relation }
```

### Workflow 3: Risk-Benefit Justification

```yaml
Step 1: Get risk management standard
Tool: mcp__context7__get-library-docs
library_id: "iso-14971-2019"
topics: ["risk-evaluation", "risk-benefit"]

Step 2: Analyze risk-benefit
Tool: mcp__sequential-thinking__sequentialthinking
prompt: "ISO 14971 risk-benefit analysis for..."

Step 3: Register risk
Tool: mcp__notion__create-page
database_id: RISK_REGISTER

Step 4: Document justification
Tool: mcp__notion__create-page
database_id: DOCUMENT_REGISTRY
properties: { "Document Type": "Risk Analysis Report", "Related Risk": relation }
```

---

## Version History

- v1.0.0 (2026-02-09): Initial Phase 3 MCP tool reference
