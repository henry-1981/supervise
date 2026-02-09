# ARIA Commands Reference

Complete guide to ARIA (AI Regulatory Intelligence Assistant) commands for business workflow automation.

## Overview

ARIA commands implement the Brief-Execute-Deliver workflow for regulatory intelligence and technical documentation tasks. These commands orchestrate ARIA agents and skills to accomplish complex business workflows.

**Core Commands:**
- **/aria brief**: Task understanding and scope definition
- **/aria execute**: Workflow execution and agent coordination
- **/aria deliver**: Final deliverable generation and distribution
- **/aria template**: Template management and selection
- **/aria knowledge**: Knowledge base management

---

## /aria brief

### Purpose

Task understanding and scope definition phase of the ARIA workflow. Clarifies user intent, defines project scope, and creates execution plans.

### When to Use

- Starting new regulatory intelligence tasks
- Defining scope for document creation
- Planning complex multi-agent workflows
- Clarifying ambiguous requirements

### Parameters

**Required:**

- `task`: Task description or requirements

**Optional:**

- `--scope`: Specific scope boundaries
- `--priority`: Task priority (low, medium, high, critical)
- `--deadline`: Target completion date
- `--agents`: Specific agents to include
- `--template`: Initial template selection

### Usage Examples

Basic task briefing:

```
/aria brief "Create a regulatory submission document for FDA 510(k) submission"
```

Scoped task with priority:

```
/aria brief "Analyze competitor regulatory filings" --scope="medical device software" --priority="high"
```

Complex workflow planning:

```
/aria brief "Prepare comprehensive regulatory strategy report for US and EU markets" --deadline="2025-03-31" --agents="expert-researcher,expert-analyst,expert-writer"
```

### Workflow

1. **Intent Clarification**

   - Asks targeted questions to understand needs
   - Identifies ambiguous requirements
   - Confirms scope and deliverables

2. **Capability Discovery**

   - Identifies relevant agents
   - Maps requirements to skills
   - Determines resource needs

3. **Planning**

   - Creates execution plan
   - Estimates effort and timeline
   - Identifies dependencies

4. **Approval**

   - Presents plan for user approval
   - Allows plan modification
   - Secures resource commitment

### Output

- Project brief document
- Execution plan with milestones
- Agent assignments and responsibilities
- Resource requirements
- Risk assessment

### Related Agents

- **orchestrator**: Command coordinator
- **supervisor-planner**: Plan creation
- **intent-clarifier**: Requirements clarification
- **capability-discoverer**: Agent/skill discovery

### Related Skills

- aria-templates: Initial template selection
- aria-research: Requirement investigation
- aria-quality-valid: Plan quality validation

### Best Practices

- Provide clear, specific task descriptions
- Answer clarification questions thoroughly
- Review execution plan carefully
- Set realistic deadlines
- Consider agent availability

---

## /aria execute

### Purpose

Execute the ARIA workflow by coordinating agents and skills to accomplish the defined task. Manages the research, draft, review, and refine phases.

### When to Use

- Executing approved execution plans
- Running multi-agent workflows
- Coordinating complex document creation
- Managing iterative refinement processes

### Parameters

**Required:**

- `task_id`: Task identifier from brief phase
- OR `plan`: Direct execution plan input

**Optional:**

- `--phase`: Specific phase to execute (research, draft, review, refine)
- `--parallel`: Enable parallel execution
- `--continue`: Resume interrupted execution
- `--verbose`: Detailed progress reporting

### Usage Examples

Execute from brief:

```
/aria execute TASK-001
```

Execute specific phase:

```
/aria execute TASK-001 --phase="draft"
```

Continue interrupted execution:

```
/aria execute TASK-001 --continue
```

Direct plan execution:

```
/aria execute --plan="research FDA requirements, draft submission document, review for VALID compliance"
```

### Workflow Phases

**Research Phase (30%)**

- Information gathering using aria-research
- Source verification and citation
- Data collection for analysis
- Context7 MCP integration for official documents

**Draft Phase (40%)**

- Content creation using aria-writing-style
- Template-based document generation using aria-templates
- Expert-writer coordination
- Iterative content development

**Review Phase (20%)**

- Quality validation using aria-quality-valid
- Expert-reviewer assessment
- Regulatory compliance check
- Improvement recommendation implementation

**Refine Phase (10%)**

- Final content refinement
- Format standardization
- Deliverable preparation
- Pre-delivery validation

### Agent Coordination

**Parallel Execution:**

```
Research Team (Parallel):
├── expert-researcher: Regulatory research
├── expert-analyst: Data analysis
└── capability-discoverer: Capability mapping

Draft Team (Sequential):
├── expert-writer: Content creation
└── manager-docs: Document management

Review Team (Parallel):
├── expert-reviewer: Content review
└── manager-quality: Quality validation
```

### Progress Tracking

- Milestone completion tracking
- Agent status reporting
- Issue identification and resolution
- Timeline adherence monitoring

### Output

- Intermediate deliverables per phase
- Progress reports
- Quality assessment reports
- Issue logs and resolutions
- Refined deliverable

### Related Agents

- **orchestrator**: Command coordinator
- **orchestra**: Agent coordination
- **aggregator**: Result aggregation

### Related Skills

- aria-research: Research methodology
- aria-writing-style: Content creation
- aria-templates: Document templates
- aria-quality-valid: Quality validation
- aria-analysis: Data analysis

### Error Handling

- Agent failure recovery
- Rollback to last stable state
- Alternative agent selection
- Partial result preservation
- User notification and guidance

### Best Practices

- Monitor progress closely
- Address issues promptly
- Validate each phase output
- Maintain communication with agents
- Document deviations and decisions

---

## /aria deliver

### Purpose

Generate final deliverables and manage distribution to target channels. Ensures quality gate compliance and format requirements.

### When to Use

- Completing ARIA workflow
- Generating final deliverables
- Preparing regulatory submissions
- Distributing documents to stakeholders

### Parameters

**Required:**

- `task_id`: Task identifier
- OR `deliverable`: Path to deliverable

**Optional:**

- `--format`: Output format (markdown, pdf, docx, html)
- `--channel`: Distribution channel (email, notion, filesystem)
- `--validate`: Quality validation level (basic, standard, comprehensive)
- `--notify`: Recipient notification
- `--archive`: Archive location

### Usage Examples

Standard delivery:

```
/aria deliver TASK-001
```

Format conversion:

```
/aria deliver TASK-001 --format="pdf"
```

Multi-channel distribution:

```
/aria deliver TASK-001 --channel="notion,email" --notify="team@company.com"
```

Comprehensive validation:

```
/aria deliver TASK-001 --validate="comprehensive" --format="docx" --channel="filesystem"
```

### Delivery Process

1. **Final Validation**

   - VALID framework compliance check
   - Quality gate validation
   - Format requirement verification
   - Regulatory submission readiness assessment

2. **Format Conversion**

   - Generate requested output formats
   - Apply template styling
   - Embed metadata and versioning
   - Create accessibility compliant versions

3. **Quality Assurance**

   - Automated quality checks
   - Manual review integration
   - Compliance verification
   - Acceptance testing

4. **Distribution**

   - Channel-specific formatting
   - Metadata attachment
   - Recipient notification
   - Delivery confirmation

5. **Archival**

   - Version controlled storage
   - Audit trail creation
   - Backup generation
   - Indexing for retrieval

### Output Formats

**Document Formats:**

- Markdown (.md): Source format, version control friendly
- PDF (.pdf): Final submission format
- Word (.docx): Editable document format
- HTML (.html): Web presentation format

**Metadata:**

- JSON (.json): Structured metadata
- YAML (.yaml): Configuration data
- XML (.xml): Regulatory submission format

### Distribution Channels

**Filesystem:**

- Local directory storage
- Network share deployment
- Cloud storage synchronization
- Backup system integration

**Notion:**

- Workspace page creation
- Database entry
- Team notification
- Version tracking

**Email:**

- Attachment delivery
- Recipient notification
- Read receipt tracking
- Distribution list management

### Quality Validation

**Validation Levels:**

**Basic:**
- Automated checks only
- Format validation
- Required field verification
- Estimated processing time: < 1 minute

**Standard:**
- Basic + VALID framework validation
- Content quality scoring
- Regulatory compliance check
- Estimated processing time: 5-10 minutes

**Comprehensive:**
- Standard + manual review integration
- Multi-dimensional quality assessment
- Full regulatory submission readiness
- Estimated processing time: 30-60 minutes

### Delivery Checklist

- [ ] VALID framework validation passed
- [ ] Format requirements met
- [ ] Quality threshold achieved (80%+)
- [ ] Regulatory compliance verified
- [ ] Stakeholder approvals obtained
- [ ] Distribution channels configured
- [ ] Archival process completed
- [ ] Audit trail documented

### Related Agents

- **manager-docs**: Document finalization
- **manager-quality**: Quality gate validation
- **aggregator**: Result compilation

### Related Skills

- aria-quality-valid: Final quality validation
- aria-templates: Format compliance
- aria-writing-style: Final style check

### Delivery Report

Each delivery generates a report including:

- Deliverable summary
- Quality validation results
- Distribution confirmation
- Recipient notifications
- Archival location
- Version information
- Audit trail

### Best Practices

- Validate thoroughly before delivery
- Use appropriate format for recipient
- Confirm distribution channels
- Maintain delivery records
- Archive for future reference
- Notify stakeholders appropriately

---

## /aria template

### Purpose

Template management command for browsing, selecting, previewing, and managing document templates in the ARIA template library.

### When to Use

- Selecting templates for new documents
- Browsing available template options
- Previewing template structure
- Creating custom templates
- Managing template versions

### Parameters

**Required:**

- `action`: Action to perform (list, show, preview, create, update)

**Optional:**

- `--category`: Template category filter
- `--type`: Document type filter
- `--id`: Specific template identifier
- `--search`: Keyword search
- `--output`: Output format

### Usage Examples

List all templates:

```
/aria template list
```

List by category:

```
/aria template list --category="regulatory"
```

Show template details:

```
/aria template show --id="FDA-510k-Submission"
```

Preview template:

```
/aria template preview --id="Technical-Specification"
```

Search templates:

```
/aria template list --search="validation"
```

### Template Categories

**Regulatory Documents:**

- FDA 510(k) Submission
- EU MDR Technical Documentation
- ISO 13485 Quality Manual
- Validation Protocols
- Risk Assessment Reports
- CAPA Reports

**Technical Documents:**

- Technical Specifications
- Design Documents
- User Manuals
- Installation Guides
- Maintenance Procedures
- Test Protocols

**Project Management:**

- Project Plans
- Status Reports
- Meeting Minutes
- Requirements Documents
- Change Requests
- Review Records

### Template Information

Each template includes:

**Metadata:**
- Template ID and name
- Version information
- Last update date
- Category and tags
- Author/owner

**Structure:**
- Section outline
- Placeholder fields
- Formatting rules
- Required vs optional sections

**Usage:**
- Intended use cases
- Regulatory references
- Compliance notes
- Examples and samples

### Template Selection Process

1. **Browse Available Templates**

   - List templates by category
   - Search by keywords
   - Filter by document type

2. **Review Template Details**

   - Show template structure
   - Preview content sections
   - Check compliance notes

3. **Select Template**

   - Choose appropriate template
   - Confirm selection
   - Load into workspace

4. **Customize (Optional)**

   - Modify placeholder fields
   - Add custom sections
   - Save as custom variant

### Template Management

**Creating Custom Templates:**

```
/aria template create --base="Technical-Specification" --name="Company-Spec-Template"
```

**Updating Templates:**

```
/aria template update --id="Custom-Template" --version="2.0"
```

**Version Management:**

- Automatic version tracking
- Change history logging
- Rollback capability
- Version comparison

### Related Agents

- **manager-docs**: Template management
- **expert-writer**: Template usage

### Related Skills

- aria-templates: Template library

### Best Practices

- Choose the most specific template for your need
- Review template structure before selection
- Customize appropriately without breaking compliance
- Maintain version control for custom templates
- Document template customizations

---

## /aria knowledge

### Purpose

Knowledge base management command for accessing, searching, and managing regulatory intelligence information stored in Notion and other knowledge repositories.

### When to Use

- Researching regulatory requirements
- Accessing historical information
- Searching knowledge base
- Updating knowledge repositories
- Synchronizing with external sources

### Parameters

**Required:**

- `action`: Action to perform (search, get, add, update, sync)

**Optional:**

- `--query`: Search query
- `--category`: Knowledge category
- `--source`: Knowledge source (notion, local)
- `--tags`: Tag filters
- `--limit`: Result limit

### Usage Examples

Search knowledge base:

```
/aria knowledge search --query="FDA software validation"
```

Get specific entry:

```
/aria knowledge get --id="KB-FDA-001"
```

Browse by category:

```
/aria knowledge search --category="regulatory-guidance"
```

Sync with Notion:

```
/aria knowledge sync --source="notion"
```

Add knowledge entry:

```
/aria knowledge add --title="New FDA Guidance" --content="..." --category="regulatory"
```

### Knowledge Categories

**Regulatory Information:**

- FDA guidances and regulations
- EU MDR requirements
- ISO standards
- International regulations
- Regional requirements

**Technical Knowledge:**

- Best practices
- Lessons learned
- Case studies
- Validation approaches
- Risk assessment methods

**Project Information:**

- Project documentation
- Submission history
- Compliance records
- Audit findings
- CAPA records

**Market Intelligence:**

- Competitor submissions
- Market trends
- Regulatory changes
- Industry developments
- Technology updates

### Knowledge Sources

**Notion Integration:**

- Central knowledge hub
- Document registry
- CAPA tracker
- Risk register
- Compliance database

**Local Storage:**

- Cached frequently accessed information
- Offline access capability
- Fast retrieval
- Version control

**External Sources:**

- Regulatory body websites
- Standards organizations
- Industry databases
- Scientific literature

### Search Features

**Full-Text Search:**

- Search across all content
- Keyword matching
- Phrase search
- Boolean operators

**Filtered Search:**

- Category filtering
- Tag filtering
- Date range filtering
- Source filtering

**Semantic Search:**

- Concept-based matching
- Related content discovery
- Contextual relevance
- Intelligent ranking

### Knowledge Management

**Adding Knowledge:**

- Automatic citation capture
- Metadata extraction
- Tag suggestion
- Category assignment
- Quality validation

**Updating Knowledge:**

- Version tracking
- Change history
- Approval workflow
- Update notifications
- Audit trail

**Synchronization:**

- Bidirectional Notion sync
- Conflict resolution
- Incremental updates
- Background sync
- Status reporting

### Related Agents

- **expert-researcher**: Knowledge usage
- **manager-docs**: Knowledge documentation

### Related Skills

- aria-research: Research methodology
- Context7 MCP: External knowledge access

### Knowledge Quality

**Quality Criteria:**

- Source authority verification
- Information currency check
- Accuracy validation
- Completeness assessment
- Relevance scoring

**Maintenance:**

- Regular review cycles
- Update notifications
- Obsolescence tracking
- Archive management

### Best Practices

- Use specific search terms for better results
- Verify knowledge currency before use
- Contribute validated knowledge back to repository
- Maintain proper citations and references
- Regular knowledge base reviews

---

## Command Integration

### Brief-Execute-Deliver Workflow

Commands integrate into the complete ARIA workflow:

```
/aria brief (60% - Planning)
    ↓
/aria execute (30% - Execution)
    ↓
/aria deliver (10% - Delivery)
```

### Supporting Commands

**/aria template:**

- Used during brief for template selection
- Supports execute phase with templates
- Ensures deliver format compliance

**/aria knowledge:**

- Supports brief with research
- Informs execute with context
- Enriches deliver with references

### Command Orchestration

**Sequential Execution:**

```
1. /aria brief "Create regulatory submission"
   → Generates plan and task ID

2. /aria execute TASK-001
   → Executes research, draft, review phases

3. /aria deliver TASK-001
   → Generates final deliverable
```

**Parallel Execution:**

```
/aria execute can coordinate multiple agents:
- expert-researcher (research phase)
- expert-writer (draft phase)
- expert-reviewer (review phase)
- manager-quality (validation)
```

---

## Quick Reference

| Command | Purpose | Phase | Key Feature |
|---------|---------|-------|-------------|
| /aria brief | Task understanding | Brief (60%) | Planning and scoping |
| /aria execute | Workflow execution | Execute (30%) | Agent coordination |
| /aria deliver | Deliverable generation | Deliver (10%) | Quality validation |
| /aria template | Template management | Support | Template library access |
| /aria knowledge | Knowledge management | Support | Information retrieval |

---

## Best Practices

### Command Usage

**Start with /aria brief:**

- Always begin new tasks with brief
- Provide clear, specific descriptions
- Answer clarification questions
- Review execution plan carefully

**Monitor /aria execute:**

- Track progress through phases
- Address issues promptly
- Validate intermediate outputs
- Maintain communication

**Validate with /aria deliver:**

- Use appropriate validation level
- Confirm format requirements
- Verify distribution channels
- Maintain delivery records

**Use supporting commands:**

- Leverage /aria template for consistency
- Access /aria knowledge for information
- Synchronize regularly

### Error Handling

**Common Issues:**

- Unclear task descriptions: Use /aria brief clarification
- Agent failures: Check /aria execute status
- Validation failures: Review /aria deliver requirements
- Template issues: Browse /aria template options

**Recovery Strategies:**

- Use --continue flag for interrupted execution
- Re-plan with /aria brief if scope changes
- Roll back to previous phase if needed
- Contact support for persistent issues

---

## Version Information

**Current Version:** 1.0.0
**Last Updated:** 2025-02-09
**Status:** Active Development

---

## Support

For issues or questions:

- ARIA Project Repository
- SPEC-ARIA-002 Documentation
- Command Examples and Use Cases
- Agent and Skill Documentation
