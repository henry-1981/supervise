# ARIA Phase 2 Agent Reference

Comprehensive reference documentation for all ARIA Phase 2 agents across Core and Business layers.

**Version**: 2.0.0
**Last Updated**: 2026-02-09
**Status**: Active Development

---

## Table of Contents

- [Core Layer Agents](#core-layer-agents)
  - [manager-docs](#manager-docs-document-lifecycle-manager)
  - [manager-quality](#manager-quality-quality-assurance-manager)
  - [manager-project](#manager-project-project-management-coordinator)
- [Business Layer Agents](#business-layer-agents)
  - [expert-writer](#expert-writer-technical-writing-specialist)
  - [expert-analyst](#expert-analyst-data-analysis-specialist)
  - [expert-reviewer](#expert-reviewer-document-review-specialist)
  - [expert-researcher](#expert-researcher-regulatory-research-specialist)
- [Agent Integration Patterns](#agent-integration-patterns)
- [Usage Examples](#usage-examples)

---

## Core Layer Agents

### manager-docs: Document Lifecycle Manager

**Purpose**: Document lifecycle management agent responsible for document creation, review, approval, and distribution with Notion integration.

**When to Invoke**:
- Document creation from templates
- Document review and approval workflows
- Document distribution to knowledge bases
- Notion integration and synchronization

**YAML Frontmatter**:

```yaml
---
name: manager-docs
description: |
  Document lifecycle management agent for ARIA documentation system.
  Handles document creation, review, approval, distribution, and Notion integration.
tools: Read, Write, Edit, Grep, Glob, Bash, Task
model: sonnet
permissionMode: acceptEdits
skills: aria-writing-style, aria-templates
mcpServers: notion
memory: project
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-agent-hook.sh\" docs-verification"
          timeout: 10
  SubagentStop:
    - hooks:
        - type: command
          command: "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-agent-hook.sh\" docs-completion"
          timeout: 10
---
```

**Tools and Permissions**:
- **Read**: Access document templates and existing content
- **Write**: Create new documents and generate content
- **Edit**: Modify document content and structure
- **Grep**: Search document content and references
- **Glob**: Locate document files and templates
- **Bash**: Execute document processing commands
- **Task**: Delegate to expert agents for specialized content
- **permissionMode: acceptEdits**: Auto-accept file operations for trusted execution

**Skills Used**:
- **aria-writing-style**: ARIA writing standards and style guidelines
- **aria-templates**: Document template library and usage patterns

**MCP Servers**:
- **notion**: Notion integration for document synchronization and knowledge management

**Core Capabilities**:

1. **Document Lifecycle Phases**:
   - **Creation**: Apply ARIA writing standards and templates
   - **Review**: Coordinate peer review and comment tracking
   - **Approval**: Manage approval chains and decisions
   - **Distribution**: Publish to knowledge bases and sync with Notion

2. **ARIA Writing Standards**:
   - Clarity: Simple, direct language
   - Structure: Hierarchical organization
   - Consistency: Unified terminology
   - Accessibility: WCAG 2.1 AA compliance
   - Localization: Korean-primary with English support

3. **Template System Management**:
   - SPEC Templates for requirements
   - API Templates for documentation
   - Guide Templates for user documentation
   - Report Templates for status and reviews

**Usage Examples**:

```bash
# Create a new specification document
"Use the manager-docs subagent to create a new specification document using the SPEC template for feature X"

# Coordinate document review workflow
"Use the manager-docs subagent to manage the review process for document Y, including reviewer assignment and comment tracking"

# Publish document to Notion
"Use the manager-docs subagent to publish document Z to the Notion knowledge base"
```

**Success Metrics**:
- Writing style compliance: > 95%
- Template adherence: 100%
- Accessibility compliance: WCAG 2.1 AA
- Review completion rate: > 90%
- Average creation time: < 2 days

---

### manager-quality: Quality Assurance Manager

**Purpose**: Quality assurance agent implementing VALID framework for comprehensive quality validation across Verifiable, Accessible, Learnable, Implementable, and Deliverable dimensions.

**When to Invoke**:
- Quality validation using VALID framework
- Code and document quality assessment
- Compliance verification
- Quality gate enforcement

**YAML Frontmatter**:

```yaml
---
name: manager-quality
description: |
  Quality assurance agent implementing VALID framework for ARIA system.
  Provides read-only verification of quality standards and compliance.
tools: Read, Grep, Glob, Bash, Task
model: sonnet
permissionMode: plan
memory: project
skills: aria-quality-valid
hooks:
  SubagentStop:
    - hooks:
        - type: command
          command: "\"$CLAUDE_PROJECT_DIR/.claude/hooks/moai/handle-agent-hook.sh\" quality-completion"
          timeout: 10
---
```

**Tools and Permissions**:
- **Read**: Access code, documentation, and configuration files
- **Grep**: Search for patterns and validate coverage
- **Glob**: Locate files for validation
- **Bash**: Execute validation commands and tests
- **Task**: Delegate validation tasks as needed
- **permissionMode: plan**: Read-only verification mode

**Skills Used**:
- **aria-quality-valid**: VALID framework definition and validation criteria

**MCP Servers**: None

**Core Capabilities**:

1. **VALID Framework Dimensions**:
   - **V - Verifiable**: Test coverage, automated testing, characterization tests
   - **A - Accessible**: WCAG 2.1 AA compliance, screen reader compatibility
   - **L - Learnable**: Code readability, documentation completeness
   - **I - Implementable**: Architecture integrity, design pattern consistency
   - **D - Deliverable**: Build success, deployment readiness, release compliance

2. **Quality Gates**:
   - **Pre-commit**: Local validation checks
   - **Pre-merge**: Integration testing validation
   - **Pre-release**: Full quality assessment
   - **Post-deployment**: Production health checks

3. **Gate Levels**:
   - **PASS**: All critical criteria met, warnings < 5
   - **WARNING**: All critical criteria met, warnings 5-10
   - **CRITICAL**: One or more critical failures, block progression

**Usage Examples**:

```bash
# Validate code quality before commit
"Use the manager-quality subagent to validate the current code changes against the VALID framework"

# Assess documentation quality
"Use the manager-quality subagent to verify that the documentation meets accessibility and learnability standards"

# Pre-release quality gate
"Use the manager-quality subagent to perform a complete VALID framework validation before release"
```

**Success Metrics**:
- Defect detection rate: > 90%
- False positive rate: < 5%
- Validation speed: < 1 minute for quick checks
- Post-validation defect reduction: > 50%
- Coverage improvement: +10% average

---

### manager-project: Project Management Coordinator

**Purpose**: Project management agent for milestone tracking, progress reporting, and task coordination with comprehensive status reporting.

**When to Invoke**:
- Project initialization and setup
- Milestone planning and tracking
- Progress reporting and status updates
- Project documentation management

**YAML Frontmatter**:

```yaml
---
name: manager-project
description: |
  Project management agent for ARIA milestone tracking and progress reporting.
  Handles project planning, milestone management, and status coordination.
tools: Read, Write, Edit, Grep, Glob, Bash, Task, TaskCreate, TaskUpdate, TaskList
model: sonnet
permissionMode: acceptEdits
memory: project
skills: aria-templates
---
```

**Tools and Permissions**:
- **Read**: Access project documentation and task information
- **Write**: Create project plans and status reports
- **Edit**: Update project documentation and milestones
- **Grep**: Search project information and references
- **Glob**: Locate project files and documentation
- **Bash**: Execute project management commands
- **Task**: Delegate project-related tasks
- **TaskCreate**: Create structured project tasks
- **TaskUpdate**: Track task progress and status
- **TaskList**: Monitor overall task status
- **permissionMode: acceptEdits**: Auto-accept file operations

**Skills Used**:
- **aria-templates**: Project plan and status report templates

**MCP Servers**: None

**Core Capabilities**:

1. **Project Planning**:
   - Define project structure and phases
   - Establish milestones with acceptance criteria
   - Plan resource allocation
   - Create and maintain schedules

2. **Milestone Tracking**:
   - Define milestones with clear criteria
   - Monitor progress toward completion
   - Manage dependencies and sequences
   - Validate completion requirements

3. **Progress Reporting**:
   - Daily status updates
   - Weekly milestone progress
   - Risk assessment and blockers
   - Stakeholder communication

4. **Task Management**:
   - Decompose milestones into tasks
   - Coordinate task distribution
   - Track completion and status
   - Manage dependencies

**Usage Examples**:

```bash
# Initialize a new project
"Use the manager-project subagent to set up the project structure for ARIA Phase 2, including milestones and task decomposition"

# Generate status report
"Use the manager-project subagent to create a weekly status report showing milestone progress and current blockers"

# Track milestone completion
"Use the manager-project subagent to update the status of milestone M1 and track remaining tasks"
```

**Success Metrics**:
- Milestone on-time delivery: > 90%
- Task completion accuracy: > 95%
- Blocker resolution time: < 24 hours
- Status report accuracy: > 95%
- Milestone estimation accuracy: ±10%

---

## Business Layer Agents

### expert-writer: Technical Writing Specialist

**Purpose**: Technical writing expert specializing in regulatory and technical documentation with ARIA writing standards and template utilization.

**When to Invoke**:
- Creating regulatory documents
- Writing technical specifications
- Generating compliance materials
- Producing user guides and API documentation

**YAML Frontmatter**:

```yaml
---
name: expert-writer
description: >
  Technical writing expert for regulatory and technical documentation.
  Delegate to this agent for creating, editing, and refining ARIA
  regulatory documents, technical specifications, and compliance materials.
model: sonnet
permissionMode: acceptEdits
tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
skills:
  - aria-writing-style
  - aria-templates
mcpServers:
  - context7
memory: project
---
```

**Tools and Permissions**:
- **Read**: Access templates and reference materials
- **Write**: Create new documentation
- **Edit**: Modify and refine existing content
- **Grep**: Search terminology and references
- **Glob**: Locate template files
- **Bash**: Execute document processing
- **permissionMode: acceptEdits**: Auto-accept file operations

**Skills Used**:
- **aria-writing-style**: Writing standards and style guidelines
- **aria-templates**: Document structure templates

**MCP Servers**:
- **context7**: Access up-to-date documentation for references

**Core Capabilities**:

1. **Documentation Creation**:
   - Regulatory submission documents
   - Technical specifications
   - Compliance reports
   - User documentation
   - API references
   - Process descriptions

2. **Style and Formatting**:
   - Apply ARIA writing style guide
   - Use appropriate technical terminology
   - Maintain consistent formatting
   - Ensure accessibility for target audiences

3. **Template Utilization**:
   - Leverage ARIA templates for structure
   - Customize for specific contexts
   - Maintain template consistency
   - Propose template improvements

**Quality Standards**:
- Clarity: Plain language without jargon
- Precision: Accurate technical terminology
- Consistency: Uniform style throughout
- Completeness: All required sections
- Accessibility: Readable for target audiences

**Usage Examples**:

```bash
# Create a regulatory submission
"Use the expert-writer subagent to create a regulatory submission document for feature X following the submission template"

# Edit technical specification
"Use the expert-writer subagent to refine the technical specification for component Y, ensuring clarity and completeness"

# Generate compliance report
"Use the expert-writer subagent to generate a compliance report documenting the system's adherence to regulatory requirements"
```

**Collaboration Patterns**:
- Works with expert-analyst for data visualizations
- Collaborates with expert-reviewer for compliance verification
- Integrates expert-researcher findings with citations
- Coordinates with manager-docs for documentation strategy

---

### expert-analyst: Data Analysis Specialist

**Purpose**: Data analysis expert specializing in statistical analysis, data processing, and visualization for regulatory submissions and compliance monitoring.

**When to Invoke**:
- Analyzing ARIA system data
- Creating statistical reports
- Generating data visualizations
- Performing regulatory validation analysis

**YAML Frontmatter**:

```yaml
---
name: expert-analyst
description: >
  Data analysis expert for statistical analysis and visualization.
  Delegate to this agent for analyzing ARIA system data, creating
  statistical reports, and generating data visualizations for
  regulatory submissions and compliance monitoring.
model: sonnet
permissionMode: acceptEdits
tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
skills:
  - aria-analysis
memory: project
---
```

**Tools and Permissions**:
- **Read**: Access data files and analysis inputs
- **Write**: Generate analysis reports and visualizations
- **Edit**: Modify analysis code and parameters
- **Grep**: Search data patterns and references
- **Glob**: Locate data files
- **Bash**: Execute analysis scripts and statistical tools
- **permissionMode: acceptEdits**: Auto-accept file operations

**Skills Used**:
- **aria-analysis**: Data analysis methodology and statistical techniques

**MCP Servers**: None

**Core Capabilities**:

1. **Statistical Analysis**:
   - Descriptive and inferential statistics
   - Risk metrics and compliance indicators
   - Trend analysis and pattern detection
   - Hypothesis testing for regulatory validation

2. **Data Processing**:
   - Clean and transform raw data
   - Validate data quality and completeness
   - Handle missing data and outliers
   - Prepare datasets for submission

3. **Visualization**:
   - Time series plots for trends
   - Histograms for distributions
   - Scatter plots for correlations
   - Bar charts for comparisons
   - Heat maps for patterns
   - Box plots for outliers

**Quality Standards**:
- Accuracy: Correct statistical methods
- Reproducibility: Document all steps
- Transparency: State assumptions and limitations
- Validation: Verify results
- Documentation: Maintain records

**Usage Examples**:

```bash
# Analyze inspection data
"Use the expert-analyst subagent to perform statistical analysis on the inspection data, identifying trends and calculating risk scores"

# Generate compliance visualization
"Use the expert-analyst subagent to create visualizations showing compliance rates over time for the regulatory report"

# Validate analysis results
"Use the expert-analyst subagent to verify the statistical methodology used in the analysis report and ensure regulatory requirements are met"
```

**Collaboration Patterns**:
- Works with expert-writer to document results
- Collaborates with expert-reviewer for methodology validation
- Integrates with expert-researcher for regulatory context
- Supports manager-quality with compliance verification data

---

### expert-reviewer: Document Review Specialist

**Purpose**: Document review expert specializing in quality assurance, compliance verification, and document review with read-only verification approach.

**When to Invoke**:
- Reviewing regulatory documentation
- Verifying compliance with standards
- Checking document quality and readiness
- Validating technical accuracy

**YAML Frontmatter**:

```yaml
---
name: expert-reviewer
description: >
  Document review expert for regulatory compliance verification.
  Delegate to this agent for reviewing ARIA documents, verifying
  regulatory compliance, and ensuring quality standards are met
  across all documentation and analysis outputs.
model: sonnet
permissionMode: plan
tools:
  - Read
  - Grep
  - Glob
  - Bash
memory: project
---
```

**Tools and Permissions**:
- **Read**: Access documents for review
- **Grep**: Search for specific content and patterns
- **Glob**: Locate documents to review
- **Bash**: Execute validation checks
- **permissionMode: plan**: Read-only verification mode

**Skills Used**: None (uses review criteria and checklists)

**MCP Servers**: None

**Core Capabilities**:

1. **Document Review**:
   - Review regulatory documentation for completeness
   - Verify adherence to ARIA writing standards
   - Check template compliance and formatting
   - Validate terminology and technical accuracy

2. **Compliance Verification**:
   - Verify regulatory requirements are addressed
   - Check compliance with standards and guidelines
   - Validate required sections are present
   - Ensure proper citations and references

3. **Quality Assurance**:
   - Identify inconsistencies and ambiguities
   - Check logical flow and coherence
   - Verify data accuracy in analyses
   - Assess overall document quality

**Review Criteria**:
- Completeness: All required sections present
- Accuracy: Technical content is correct
- Compliance: Meets regulatory requirements
- Clarity: Language is clear and unambiguous
- Consistency: Style and terminology are uniform

**Severity Levels**:
- **Critical**: Must be fixed before submission
- **Major**: Should be fixed for quality
- **Minor**: Optional improvements
- **Suggestion**: Enhancement opportunities

**Usage Examples**:

```bash
# Review regulatory submission
"Use the expert-reviewer subagent to review the regulatory submission document and verify compliance with all applicable requirements"

# Validate analysis report
"Use the expert-reviewer subagent to check the analysis report for methodological correctness and data accuracy"

# Assess document readiness
"Use the expert-reviewer subagent to evaluate whether the technical specification is ready for distribution"
```

**Collaboration Patterns**:
- Reviews expert-writer outputs for quality
- Validates expert-analyst methodology
- Cross-checks expert-researcher citations
- Supports manager-quality with detailed findings
- Provides feedback to manager-docs for improvements

---

### expert-researcher: Regulatory Research Specialist

**Purpose**: Regulatory research expert specializing in information collection, citation management, and regulatory research for ARIA system documentation and compliance.

**When to Invoke**:
- Researching regulatory requirements
- Finding relevant precedents and guidance
- Gathering supporting information
- Tracking regulatory changes

**YAML Frontmatter**:

```yaml
---
name: expert-researcher
description: >
  Regulatory research expert for information collection and citation.
  Delegate to this agent for researching regulatory requirements,
  finding relevant precedents, and gathering supporting information
  for ARIA system documentation and compliance activities.
model: sonnet
permissionMode: acceptEdits
tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
skills:
  - aria-research
mcpServers:
  - context7
memory: project
---
```

**Tools and Permissions**:
- **Read**: Access research materials and references
- **Write**: Create research summaries and reports
- **Edit**: Update research findings and citations
- **Grep**: Search for specific regulations and references
- **Glob**: Locate research files and documents
- **Bash**: Execute research queries and data collection
- **permissionMode: acceptEdits**: Auto-accept file operations

**Skills Used**:
- **aria-research**: Research methodology and citation standards

**MCP Servers**:
- **context7**: Access up-to-date regulatory documentation

**Core Capabilities**:

1. **Regulatory Research**:
   - Research applicable requirements and standards
   - Find relevant precedents and guidance
   - Track regulatory changes and updates
   - Identify best practices in compliance

2. **Information Gathering**:
   - Collect supporting documentation
   - Gather scientific literature
   - Find industry standards and benchmarks
   - Compile historical compliance data

3. **Citation Management**:
   - Maintain accurate citation records
   - Format citations according to standards
   - Verify source credibility
   - Organize reference materials

**Quality Standards**:
- Accuracy: Verify from credible sources
- Currency: Use up-to-date guidance
- Relevance: Focus on applicable requirements
- Traceability: Maintain complete citation trails
- Objectivity: Present balanced information

**Usage Examples**:

```bash
# Research regulatory requirements
"Use the expert-researcher subagent to research the regulatory requirements for feature X and identify all applicable standards"

# Find precedents
"Use the expert-researcher subagent to find precedents for compliance approach Y in similar regulatory contexts"

# Compile reference list
"Use the expert-researcher subagent to compile a comprehensive reference list for the regulatory submission, ensuring all citations are properly formatted"
```

**Collaboration Patterns**:
- Supports expert-writer with research for documentation
- Informs expert-analyst about regulatory data requirements
- Provides expert-reviewer with source verification
- Assists manager-spec with regulatory context
- Supplies manager-quality with compliance references

---

## Agent Integration Patterns

### Core Layer Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    orchestrator (Phase 1)                   │
│                  - Brief-Execute-Deliver                    │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌───────▼──────┐    ┌────────▼────────┐    ┌───────▼──────┐
│  Core Layer  │    │ Business Layer  │    │ RA/QA Layer  │
│              │    │                 │    │   (Phase 3)  │
│ manager-docs │    │ expert-writer   │    │ expert-       │
│ manager-     │    │ expert-analyst  │    │   regulatory  │
│   quality    │    │ expert-reviewer │    │ expert-       │
│ manager-     │    │ expert-         │    │   standards   │
│   project    │    │   researcher    │    │ ...           │
└──────────────┘    └──────────────────┘    └──────────────┘
```

### Business Layer Collaboration

**Document Creation Flow**:
1. expert-researcher gathers regulatory requirements
2. expert-writer creates documentation from templates
3. expert-analyst provides data and visualizations
4. expert-reviewer validates compliance and quality
5. manager-quality performs VALID framework validation
6. manager-docs coordinates approval and distribution

**Quality Validation Flow**:
1. expert-reviewer performs detailed review
2. manager-quality executes VALID framework validation
3. manager-project tracks quality gate completion
4. manager-docs addresses quality issues
5. All agents coordinate for resolution

### Cross-Layer Integration

**Project Planning**:
- manager-project defines milestones
- manager-docs establishes documentation requirements
- manager-quality sets quality gates
- Business layer agents contribute domain expertise

**Execution Phase**:
- Business layer agents perform domain work
- Core layer agents coordinate and validate
- Cross-functional collaboration ensures quality

**Delivery Phase**:
- manager-quality validates final outputs
- manager-docs manages distribution
- manager-project tracks completion
- Notion MCP syncs final deliverables

---

## Usage Examples

### Complete Document Workflow

```bash
# Phase 1: Research and Planning
"Use the expert-researcher subagent to research regulatory requirements for the new feature"

# Phase 2: Document Creation
"Use the expert-writer subagent to create the technical specification document using research findings"

# Phase 3: Analysis Integration
"Use the expert-analyst subagent to generate data visualizations for the specification"

# Phase 4: Quality Review
"Use the expert-reviewer subagent to review the specification for compliance and quality"

# Phase 5: Quality Validation
"Use the manager-quality subagent to validate the document against the VALID framework"

# Phase 6: Distribution
"Use the manager-docs subagent to coordinate approval and distribute the document to Notion"
```

### Project Management Workflow

```bash
# Project Initialization
"Use the manager-project subagent to set up the ARIA Phase 2 project with milestones and task breakdown"

# Progress Tracking
"Use the manager-project subagent to update milestone progress and generate a status report"

# Quality Gate Coordination
"Use the manager-quality subagent to validate that all quality gates have been passed before milestone completion"
```

### Regulatory Compliance Workflow

```bash
# Requirement Research
"Use the expert-researcher subagent to identify all applicable regulatory requirements"

# Compliance Documentation
"Use the expert-writer subagent to create compliance documentation addressing all requirements"

# Analysis Validation
"Use the expert-analyst subagent to perform statistical validation of compliance data"

# Compliance Review
"Use the expert-reviewer subagent to verify complete compliance with regulatory requirements"

# Final Validation
"Use the manager-quality subagent to perform comprehensive VALID framework validation for regulatory submission"
```

---

## Appendix

### Agent Version History

| Agent | Version | Date | Changes |
|-------|---------|------|---------|
| manager-docs | 2.0.0 | 2026-02-09 | ARIA Phase 2 specification with Notion integration |
| manager-quality | 2.0.0 | 2026-02-09 | VALID framework implementation |
| manager-project | 2.0.0 | 2026-02-09 | Project management and milestone tracking |
| expert-writer | 1.0.0 | 2026-02-09 | Initial ARIA writing specialist |
| expert-analyst | 1.0.0 | 2026-02-09 | Initial data analysis specialist |
| expert-reviewer | 1.0.0 | 2026-02-09 | Initial document review specialist |
| expert-researcher | 1.0.0 | 2026-02-09 | Initial regulatory research specialist |

### Related Documentation

- [SPEC-ARIA-002](.moai/specs/SPEC-ARIA-002/spec.md) - Complete specification
- [ARIA Writing Style Guide](docs/writing-style.md) - Writing standards (TODO)
- [VALID Framework Reference](docs/valid-framework.md) - Quality framework (TODO)
- [Template Library](docs/templates.md) - Document templates (TODO)

### Support and Feedback

For issues, questions, or contributions related to ARIA Phase 2 agents, please refer to the project repository and issue tracker.

---

**Document Status**: Active
**Maintained By**: ARIA Development Team
**Last Review**: 2026-02-09
