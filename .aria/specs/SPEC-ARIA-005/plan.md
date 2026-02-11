# SPEC-ARIA-005: Implementation Plan

## TAG BLOCK

```
SPEC-ID: SPEC-ARIA-005
Related: SPEC-ARIA-001, SPEC-ARIA-002, SPEC-ARIA-003, SPEC-ARIA-004
Phase: Phase 5 (Advanced Features)
Complexity: High (8 major feature areas)
Estimated Duration: 4-6 weeks
Risk Level: Medium (experimental Agent Teams feature)
```

## Implementation Milestones

### Milestone 1: Agent Memory System (Priority: High)

**Objective**: Implement persistent memory for regulatory decisions, company preferences, and task patterns.

**Success Criteria**:
- Regulatory decisions stored and retrieved across sessions
- Company preferences learned and applied consistently
- Repetitive task patterns detected and automated

**Technical Approach**:

1. **Memory Storage Architecture**
   - Create `.claude/agent-memory/aria/` directory structure
   - Implement JSON schemas for each memory type
   - Add VCS integration with `.gitattributes` for merge conflict resolution

2. **Regulatory Decision Memory**
   - Implement decision storage API with metadata tagging
   - Create decision retrieval with relevance scoring
   - Add decision validity tracking (expiration flags)

3. **Company Preference Learning**
   - Implement preference extraction from user interactions
   - Create preference application engine for document generation
   - Add conflict detection and resolution workflow

4. **Task Pattern Recognition**
   - Implement task sequence tracking (3+ repetitions)
   - Create pattern suggestion algorithm
   - Add workflow template generation

**File Structure**:
```
.claude/agent-memory/aria/
├── regulatory-decisions.json     # Stored decisions with citations
├── company-preferences.json      # Formatting, terminology, templates
├── task-patterns.json            # Recognized repetitive sequences
└── learning-metrics.json         # Adoption and effectiveness tracking
```

**Risks and Mitigation**:
- **Risk**: Memory conflicts in team environments
  - **Mitigation**: Implement merge conflict resolution with `.gitattributes` and user-specific memory scopes
- **Risk**: Memory accumulation size
  - **Mitigation**: Implement memory pruning with importance scoring and retention policies

**Dependencies**:
- None (foundational feature)

---

### Milestone 2: Agent Teams Mode (Priority: Medium)

**Objective**: Implement parallel execution for 510(k) and audit workflows using Claude Code Agent Teams.

**Success Criteria**:
- 510(k) preparation team successfully creates submission in parallel
- Audit response team coordinates CAPA planning across team members
- Team coordination achieves measurable time savings vs sequential execution

**Technical Approach**:

1. **Team Configuration**
   - Create team definition JSON files for each workflow type
   - Implement TeamCreate API integration with proper teammate configuration
   - Add shared task board for task ownership and progress tracking

2. **510(k) Preparation Team**
   - Configure researcher agent (haiku) for FDA 510(k) research
   - Configure analyst agent (sonnet) for predicate device comparison
   - Configure writer agent (sonnet) for submission section drafting
   - Implement task decomposition with file ownership boundaries

3. **Audit Response Team**
   - Configure researcher agent for audit finding analysis
   - Configure analyst agent for CAPA planning
   - Configure capa-expert agent for root cause analysis
   - Implement escalation paths for cross-functional findings

4. **Team Coordination**
   - Implement task board sharing via TaskCreate/TaskUpdate
   - Add completion marker detection for team phase transitions
   - Create team shutdown workflow after task completion

**Team Configuration Example**:
```json
{
  "team_name": "510k-prep-team",
  "teammates": [
    {
      "name": "researcher",
      "model": "haiku",
      "tools": ["Read", "Grep", "Glob", "WebSearch", "WebFetch"],
      "prompt": "Research FDA 510(k) requirements and predicate devices"
    },
    {
      "name": "analyst",
      "model": "sonnet",
      "tools": ["Read", "Write", "Edit", "Grep"],
      "prompt": "Analyze device specifications and predicate comparisons"
    },
    {
      "name": "writer",
      "model": "sonnet",
      "tools": ["Read", "Write", "Edit"],
      "prompt": "Draft 510(k) submission sections following eCopy templates"
    }
  ]
}
```

**Risks and Mitigation**:
- **Risk**: Agent Teams API instability (experimental feature)
  - **Mitigation**: Implement graceful fallback to sequential execution if TeamCreate fails
- **Risk**: Team coordination overhead outweighs benefits for simple tasks
  - **Mitigation**: Implement complexity threshold for team activation (only for tasks with 5+ sections)

**Dependencies**:
- Claude Code v2.1.32+ installed
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` environment variable set

---

### Milestone 3: Advanced Analytics Features (Priority: High)

**Objective**: Implement complaint trend analysis, regulatory change impact analysis, and cross-submission knowledge utilization.

**Success Criteria**:
- Complaint trends automatically detected and alerts generated
- Regulatory changes mapped to affected documents
- Successful submission content searchable and reusable

**Technical Approach**:

1. **Complaint Trend Analysis**
   - Implement statistical baseline calculation (mean ± 2σ)
   - Create trend detection algorithm with significance testing
   - Add correlation analysis with product changes and lot numbers
   - Generate actionable alert recommendations

2. **Regulatory Change Impact Analysis**
   - Implement WebSearch-based monitoring for FDA/EU/MFDS updates
   - Create regulation-to-document mapping in knowledge base
   - Add automatic flagging of affected documents in Notion
   - Implement decision validity checking against current regulations

3. **Cross-Submission Knowledge Utilization**
   - Implement knowledge base schema with outcome tagging
   - Create content search with relevance scoring
   - Add context validation when reusing previous content
   - Implement warning system for failed submission patterns

**Data Flow**:
```
Complaint Data → Statistical Analysis → Trend Detection → Alert Generation
     ↓
Regulatory Monitoring → WebSearch → Context7 MCP → Impact Analysis
     ↓
Knowledge Base → Content Search → Relevance Scoring → Suggestion
```

**Risks and Mitigation**:
- **Risk**: Insufficient historical data for trend analysis
  - **Mitigation**: Implement synthetic data generation for testing and gradual accuracy improvement
- **Risk**: False positive trend alerts
  - **Mitigation**: Implement confidence scoring and user feedback for alert tuning

**Dependencies**:
- Notion MCP (knowledge base storage)
- Context7 MCP (regulatory documentation)
- Google Workspace MCP (complaint data collection)

---

### Milestone 4: Complete Workflows (Priority: High)

**Objective**: Implement end-to-end workflows for clinical evaluation, internal audit, and post-market surveillance.

**Success Criteria**:
- Clinical evaluation workflow guides through all MEDDEV 2.7.1 rev 4 stages
- Internal audit workflow covers planning through CAPA tracking
- Post-market surveillance workflow implements EU MDR Article 83-85 requirements

**Technical Approach**:

1. **Clinical Evaluation Workflow**
   - Implement Stage 1: Scope definition with device identification
   - Implement Stage 2: Literature search with PubMed/Google Scholar integration
   - Implement Stage 3: Data analysis with equivalence assessment
   - Implement Stage 4: CER generation with MEDDEV 2.7.1 rev 4 compliance
   - Add PMCF requirement flagging for data gaps

2. **Internal Audit Workflow**
   - Implement audit planning with agenda generation based on risk areas
   - Implement audit execution with finding documentation
   - Implement CAPA planning with root cause analysis (5 Whys, Fishbone)
   - Add repeat finding detection and systemic issue flagging

3. **Post-Market Surveillance Workflow**
   - Implement PMS data collection from multiple sources (complaints, service, literature)
   - Implement trend reporting with statistical significance testing
   - Implement PSUR generation with automatic data compilation
   - Add FSCA (Field Safety Corrective Action) trigger workflow

**Workflow State Machine**:
```
Clinical Evaluation:
  [Scope] → [Literature Search] → [Data Analysis] → [CER Generation]
    ↓ (gaps detected)
  [PMCF Plan] → [PMCF Data Collection] → [CER Update]

Internal Audit:
  [Planning] → [Execution] → [Finding Documentation] → [CAPA Planning]
    ↓ (CAPA fails)
  [CAPA Revision] → [Verification]

Post-Market Surveillance:
  [PMS Data Collection] → [Trend Analysis] → [PSUR Generation]
    ↓ (safety issue)
  [FSCA Trigger] → [FSCA Execution] → [Regulatory Notification]
```

**Risks and Mitigation**:
- **Risk**: Workflow complexity causing user confusion
  - **Mitigation**: Implement step-by-step guidance with progress indicators and back-navigation
- **Risk**: Regulatory requirement changes invalidating workflows
  - **Mitigation**: Implement modular workflow design for easy updating

**Dependencies**:
- Clinical templates (Milestone 6)
- Audit templates (Milestone 6)
- EU MDR templates (Milestone 6)

---

### Milestone 5: Multi-Country Regulatory Strategy Comparison (Priority: Medium)

**Objective**: Implement requirement comparison matrix for FDA, EU MDR, MFDS, PMDA, ANVISA, Health Canada.

**Success Criteria**:
- Requirement matrix highlights differences across markets
- Conflict detection suggests harmonization strategies
- Timeline analysis suggests submission sequencing

**Technical Approach**:

1. **Regulatory Database**
   - Implement requirement database by device classification and market
   - Create requirement comparison engine with conflict detection
   - Add timeline tracking for submission and approval durations

2. **Comparison Matrix**
   - Generate side-by-side requirement comparison
   - Highlight missing requirements for specific markets
   - Suggest harmonization strategies for conflicting requirements

3. **Strategic Recommendations**
   - Analyze approval timelines for optimal submission sequencing
   - Identify "easy win" markets for early approval
   - Flag high-risk markets requiring additional resources

**Comparison Matrix Structure**:
```
| Requirement               | FDA (US) | EU MDR | MFDS (KR) | PMDA (JP) |
|---------------------------|----------|---------|-----------|-----------|
| Clinical Investigation    | Case-by-case | Required | Case-by-case | Required |
| Quality Management System | 21 CFR 820 | ISO 13485 | ISO 13485 | ISO 13485 |
| Post-Market Surveillance  | Required | Required | Required | Required |
```

**Risks and Mitigation**:
- **Risk**: Regulatory requirements frequently changing
  - **Mitigation**: Implement quarterly review cycle and Context7 MCP integration for current requirements
- **Risk**: Oversimplification of complex regulatory landscapes
  - **Mitigation**: Add disclaimer and links to official regulatory sources

**Dependencies**:
- Context7 MCP for up-to-date regulatory information
- WebSearch for regulatory update monitoring

---

### Milestone 6: Additional Templates (Priority: Medium)

**Objective**: Create comprehensive template library for clinical, QMS, audit, and EU MDR documentation.

**Success Criteria**:
- 12 new templates created covering all major regulatory document types
- Templates validated against regulatory requirements
- Template customization workflow supports company-specific adaptations

**Technical Approach**:

1. **Clinical Templates** (3 templates)
   - CER template per MEDDEV 2.7.1 rev 4
   - PMCF Plan template with post-market protocol
   - Clinical Investigation Plan template per ISO 14155

2. **QMS Templates** (3 templates)
   - Quality Manual template per ISO 13485
   - CAPA procedure template with root cause analysis framework
   - Management Review template with KPI tracking

3. **Audit Templates** (3 templates)
   - Internal Audit Checklist template per ISO 13485 clauses
   - Audit Report template with finding categorization
   - Supplier Audit template for supplier qualification

4. **EU MDR Templates** (3 templates)
   - Technical File template per Annex II and Annex III
   - PSUR template per Annex XIII
   - SSR template per Annex I

**Template Validation Process**:
1. Draft template based on regulatory requirements
2. Validate against official regulatory document structures
3. Test with sample content generation
4. Review with regulatory subject matter expert
5. Incorporate feedback and finalize

**Risks and Mitigation**:
- **Risk**: Template obsolescence due to regulation changes
  - **Mitigation**: Implement template versioning and automated currency checking (Milestone 7)
- **Risk**: Template over-customization reducing standardization benefits
  - **Mitigation**: Implement base template preservation with customization layer

**Dependencies**:
- Regulatory requirement documentation (via Context7 MCP)
- Template validation workflow (Milestone 7)

---

### Milestone 7: Hook System Integration (Priority: High)

**Objective**: Implement quality check, audit trail, and template verification hooks using MoAI-ADK hooks system.

**Success Criteria**:
- Quality check hooks validate regulatory citations before document completion
- Audit trail hooks log all changes with user attribution
- Template verification hooks check currency on session start

**Technical Approach**:

1. **Hook Configuration**
   - Add hook definitions to `.claude/settings.json`
   - Create hook wrapper scripts in `.claude/hooks/moai/`
   - Implement hook execution with proper error handling

2. **Quality Check Hooks** (PreToolUse)
   - Validate regulatory citation format (e.g., "21 CFR 820.30")
   - Check document structure compliance with template requirements
   - Verify VALID framework compliance (Verified, Accurate, Linked, Inspectable, Deliverable)
   - Prevent document completion if quality checks fail

3. **Audit Trail Hooks** (PostToolUse)
   - Log all Write/Edit operations with timestamp, user, and change summary
   - Maintain audit trail integrity per 21 CFR Part 11
   - Implement audit trail export with chain of custody documentation
   - Create resumption entries after system restart

4. **Template Verification Hooks** (SessionStart)
   - Validate template currency against regulatory requirements
   - Alert users to outdated templates before document generation
   - Offer automated template updates when available
   - Cache last known good status for offline operation

**Hook Configuration Example**:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-pre-tool.sh\"",
      "timeout": 5
    }],
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-post-tool.sh\"",
      "timeout": 10
    }],
    "SessionStart": [{
      "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-session-start.sh\"",
      "timeout": 5
    }]
  }
}
```

**Hook Action Mappings**:
- `aria-quality-check`: PreToolWrite validation of regulatory citations
- `aria-audit-trail`: PostToolWrite/Edit logging with attribution
- `aria-template-verify`: SessionStart template currency check

**Risks and Mitigation**:
- **Risk**: Hook execution performance impact
  - **Mitigation**: Implement timeout limits and asynchronous execution where possible
- **Risk**: Hook failures blocking workflow
  - **Mitigation**: Implement graceful degradation with user alerts and fallback modes

**Dependencies**:
- MoAI-ADK hooks system
- Context7 MCP for template currency validation

---

### Milestone 8: Output Styles and Format Conversion (Priority: Low)

**Objective**: Implement multi-format output generation with accessibility compliance and company branding.

**Success Criteria**:
- Reports generated in Markdown, HTML, PDF, and Word formats
- HTML output meets WCAG 2.1 AA accessibility standards
- PDF output includes document outline and navigation metadata

**Technical Approach**:

1. **Format Conversion Pipeline**
   - Implement Markdown → HTML conversion with semantic markup
   - Implement HTML → PDF conversion using wkhtmltopdf or Pandoc
   - Implement Markdown → Word conversion using Pandoc
   - Add company branding template application

2. **Accessibility Compliance**
   - Ensure HTML output uses semantic markup (headings, lists, tables)
   - Add ARIA labels and alt text for screen reader compatibility
   - Implement tagged PDF generation for PDF accessibility
   - Validate output against WCAG 2.1 AA success criteria

3. **Configuration and Customization**
   - Create output configuration file (`.moai/config/sections/output.yaml`)
   - Support company-specific branding templates (CSS, fonts, logos)
   - Implement output style selection via user preferences
   - Add fallback to Markdown if conversion fails

**Output Configuration**:
```yaml
output:
  default_format: markdown
  formats:
    markdown:
      extension: ".md"
      encoding: "utf-8"
    html:
      extension: ".html"
      css_theme: "regulatory-standard"
      accessibility: "wcag-2.1-aa"
    pdf:
      extension: ".pdf"
      page_size: "letter"
      margins: "0.75in"
      toc: true
      bookmarks: true
    word:
      extension: ".docx"
      template: "regulatory-template.dotx"
```

**Risks and Mitigation**:
- **Risk**: External tool dependencies (Pandoc, wkhtmltopdf)
  - **Mitigation**: Implement tool availability checking and fallback to Markdown
- **Risk**: Format conversion losing document structure or metadata
  - **Mitigation**: Implement validation checks and warning system for conversion losses

**Dependencies**:
- Pandoc (format conversion)
- wkhtmltopdf (PDF generation)
- Company branding assets (CSS, fonts, logos)

---

## Development Methodology

### Approach: DDD (Domain-Driven Development)

Per `.moai/config/sections/quality.yaml`:
- **development_mode**: ddd
- **characterization_tests**: true
- **behavior_snapshots**: true
- **max_transformation_size**: small

**ANALYZE Phase**:
- Read existing Phase 4 MCP integration code
- Identify hook system integration points
- Map agent memory data flow

**PRESERVE Phase**:
- Create characterization tests for existing MCP integrations
- Capture behavior snapshots for Notion knowledge base operations
- Document current session state management

**IMPROVE Phase**:
- Implement small, incremental transformations
- Add agent memory system first (foundational)
- Integrate Agent Teams mode second (experimental)
- Add analytics features third (data-dependent)
- Complete workflows and templates fourth (user-facing)
- Integrate hooks system fifth (quality enforcement)
- Add output styles last (polish)

### Success Criteria

**Completion Criteria**:
- All SPEC requirements implemented
- Characterization tests passing for Phase 4 integration points
- 85%+ code coverage for new Phase 5 features
- TRUST 5 quality gates passed
- VALID framework compliance verified

**Quality Metrics**:
- Agent Memory: 90%+ decision retrieval accuracy
- Agent Teams: 30%+ time savings vs sequential execution
- Analytics: 85%+ trend detection precision
- Workflows: End-to-end completion with <5% user intervention
- Templates: 100% regulatory requirement coverage
- Hooks: <100ms hook execution latency
- Output Styles: WCAG 2.1 AA compliance verified

---

## Risk Management

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Agent Teams API instability | Medium | High | Fallback to sequential execution |
| Memory merge conflicts | Medium | Medium | User-specific memory scopes |
| Insufficient trend data | High | Medium | Synthetic data for testing |
| Template obsolescence | Medium | High | Automated currency checking |
| Hook performance impact | Low | Medium | Timeout limits and async execution |

### Dependency Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Notion MCP downtime | Low | High | Retry with exponential backoff |
| Context7 MCP rate limits | Medium | Medium | Result caching for 24 hours |
| Google Workspace MCP changes | Low | Medium | Version-specific integration |

### User Adoption Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Workflow complexity | Medium | High | Step-by-step guidance |
| Agent Teams confusion | Medium | Medium | Progressive disclosure |
| Template overfitting | Low | Medium | Base template preservation |

---

## Timeline Estimate

**Total Duration**: 4-6 weeks

**Breakdown**:
- Week 1: Milestone 1 (Agent Memory) + Milestone 2 (Agent Teams)
- Week 2: Milestone 3 (Advanced Analytics)
- Week 3: Milestone 4 (Complete Workflows)
- Week 4: Milestone 5 (Multi-Country Comparison) + Milestone 6 (Templates)
- Week 5: Milestone 7 (Hook System)
- Week 6: Milestone 8 (Output Styles) + Testing + Documentation

**Parallel Execution Opportunities**:
- Milestone 5 and Milestone 6 can run in parallel
- Milestone 8 can start after Milestone 7 (testing in parallel)

**Critical Path**:
Milestone 1 → Milestone 2 → Milestone 3 → Milestone 4 → Milestone 7 → Testing

---

## Integration Points

### Phase 4 Dependencies
- **Notion MCP**: Knowledge base storage for agent memory and cross-submission knowledge
- **Context7 MCP**: Regulatory documentation for template validation and regulatory monitoring
- **Google Workspace MCP**: Complaint data collection for trend analysis
- **Sequential Thinking MCP**: Complex workflow decision points

### MoAI-ADK Integration
- **Hooks System**: Event-driven quality checks and audit trails
- **Agent Teams API**: Parallel execution for 510(k) and audit workflows
- **Agent Memory**: Project scope memory sharing via VCS

### External Integrations
- **Pandoc**: Format conversion (Markdown → HTML/PDF/Word)
- **wkhtmltopdf**: PDF generation with bookmarks and outlines
- **PubMed/Google Scholar**: Literature search for clinical evaluation

---

## Testing Strategy

### Unit Tests
- Agent memory CRUD operations
- Regulatory decision retrieval relevance scoring
- Template currency validation logic
- Hook execution with various scenarios

### Integration Tests
- Agent Teams coordination with shared task board
- MCP integration (Notion, Context7) for analytics
- Hook system integration with PreToolUse/PostToolUse
- Format conversion pipeline end-to-end

### Characterization Tests
- Existing Phase 4 MCP integration behavior
- Notion knowledge base operations
- Session state management across context boundaries

### User Acceptance Tests
- Complete 510(k) preparation workflow
- Complete audit response workflow
- Clinical evaluation workflow with literature search
- Multi-format report generation

---

## Definition of Done

- [ ] All 8 milestones completed
- [ ] All requirements in spec.md implemented
- [ ] All acceptance criteria in acceptance.md met
- [ ] Characterization tests passing for Phase 4 integration
- [ ] 85%+ code coverage for new features
- [ ] TRUST 5 quality gates passed
- [ ] VALID framework compliance verified
- [ ] Documentation updated (README, CHANGELOG)
- [ ] Multi-format output generation tested
- [ ] Agent Teams fallback to sequential execution verified
- [ ] Hook execution latency <100ms
- [ ] User acceptance testing completed
- [ ] Phase 5 handoff documentation created

---

**END OF SPEC-ARIA-005/plan.md**
