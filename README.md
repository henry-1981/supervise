# ARIA Phase 2

> AI-powered Regulatory Affairs Intelligence system for regulatory documentation and compliance workflows

## Project Overview

ARIA (Active Risk Inspection and Assessment) Phase 2 is an intelligent system designed to streamline regulatory affairs workflows through AI-powered automation. It transforms how regulatory professionals create, manage, and deliver regulatory documentation by combining specialized AI agents, validated workflows, and quality assurance frameworks.

### Core Objectives

- **Automate Documentation**: Reduce regulatory document creation time by 60% through AI-assisted writing
- **Ensure Compliance**: Maintain VALID quality standards across all regulatory submissions
- **Streamline Workflows**: Orchestrate complex multi-step regulatory processes with minimal manual intervention
- **Enable Collaboration**: Coordinate cross-functional regulatory teams through intelligent task management
- **Ensure Quality**: Implement TRUST 5 quality gates for all deliverables

### Target Audience

- Regulatory Affairs professionals
- Quality Assurance specialists
- Compliance officers
- Regulatory operations teams
- Pharmaceutical and medical device companies

## Architecture

ARIA Phase 2 implements a two-layer architecture with Core orchestration and Business domain expertise.

### System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         ARIA Phase 2                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    Core Layer (3 Agents)                   │ │
│  │                                                              │ │
│  │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │ │
│  │  │  Supervisor  │───▶│   Planner    │───▶│ Orchestrator │ │ │
│  │  │              │    │              │    │              │ │ │
│  │  │ Intent       │    │ Execution    │    │ Multi-Agent  │ │ │
│  │  │ Clarification│    │ Planning     │    │ Coordination │ │ │
│  │  └──────────────┘    └──────────────┘    └──────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                     │
│                           ▼                                     │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                Business Layer (4 Agents)                   │ │
│  │                                                              │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │ │
│  │  │  Researcher  │  │    Analyst   │  │    Writer    │     │ │
│  │  │              │  │              │  │              │     │ │
│  │  │ Regulatory   │  │ Statistical  │  │ Technical    │     │ │
│  │  │ Intelligence │  │ Analysis     │  │ Documentation│     │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘     │ │
│  │                                                              │ │
│  │  ┌──────────────┐                                          │ │
│  │  │   Reviewer   │                                          │ │
│  │  │              │                                          │ │
│  │  │ Quality      │                                          │ │
│  │  │ Validation   │                                          │ │
│  │  └──────────────┘                                          │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                   Knowledge Base (5 Skills)                │ │
│  │   Research │ Analysis │ Writing │ Templates │ Quality       │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **User Request** → Supervisor clarifies intent
2. **Intent Analysis** → Planner creates execution strategy
3. **Task Assignment** → Orchestrator coordinates business agents
4. **Domain Processing** → Specialized agents execute tasks
5. **Quality Validation** → Reviewer ensures compliance
6. **Result Delivery** → Aggregated output with sources

## Agents

ARIA Phase 2 implements 7 specialized agents organized into Core and Business layers.

### Core Layer Agents

#### 1. Supervisor Agent

**Purpose**: Main orchestrator for multi-agent coordination

**Responsibilities**:
- Clarify user intent through targeted questioning
- Route tasks to appropriate business agents
- Coordinate multi-agent workflows
- Aggregate results from multiple agents
- Handle error recovery and fallback strategies

**Model**: Claude Sonnet (balanced speed and intelligence)

**Tools**: Task, AskUserQuestion, Read, Glob, Grep

**Key Features**:
- Never implements directly (delegation-only)
- User interaction handled only at this layer
- Parallel execution when possible (max 10 concurrent)
- Responds in user's conversation language

#### 2. Planner Agent

**Purpose**: Execution planning and task decomposition

**Responsibilities**:
- Analyze clarified intent
- Create execution plans with phases
- Identify task dependencies
- Assign tasks to appropriate agents
- Present plans for user approval

**Model**: Claude Haiku (fast planning)

**Tools**: Read, Grep, Glob

**Key Features**:
- Generates sequential and parallel execution strategies
- Identifies fallback options for each task
- Estimates resource requirements
- Creates milestone checkpoints

#### 3. Orchestrator Agent

**Purpose**: Multi-agent execution coordination

**Responsibilities**:
- Execute approved plans
- Coordinate agent timing and dependencies
- Handle inter-agent communication
- Monitor execution progress
- Implement error recovery

**Model**: Claude Sonnet

**Tools**: Task, Read, Write, Edit, Bash

**Key Features**:
- Manages agent lifecycle
- Implements retry logic
- Tracks execution state
- Provides progress updates

### Business Layer Agents

#### 4. Expert Researcher

**Purpose**: Regulatory research and intelligence gathering

**Responsibilities**:
- Research regulatory requirements
- Find relevant precedents and guidance
- Track regulatory changes
- Gather supporting documentation
- Maintain citation records

**Model**: Claude Sonnet

**Skills**: aria-research

**MCP Integration**: Context7 for up-to-date regulatory documentation

**Key Outputs**:
- Regulatory requirement summaries
- Annotated reference lists
- Compliance gap analyses
- Best practice compilations

#### 5. Expert Analyst

**Purpose**: Statistical analysis and data visualization

**Responsibilities**:
- Perform statistical analyses
- Calculate risk metrics
- Analyze trends and patterns
- Create data visualizations
- Validate analysis results

**Model**: Claude Sonnet

**Skills**: aria-analysis

**Key Outputs**:
- Statistical reports
- Trend analysis charts
- Risk scoring models
- Compliance dashboards

#### 6. Expert Writer

**Purpose**: Technical documentation authoring

**Responsibilities**:
- Write regulatory submissions
- Create technical documentation
- Format according to standards
- Maintain consistency
- Integrate feedback

**Model**: Claude Sonnet

**Skills**: aria-writing-style, aria-templates

**Key Outputs**:
- Regulatory submissions
- Technical reports
- User documentation
- SOPs and work instructions

#### 7. Expert Reviewer

**Purpose**: Quality validation and compliance verification

**Responsibilities**:
- Validate document quality
- Check regulatory compliance
- Verify citation accuracy
- Assess completeness
- Ensure consistency

**Model**: Claude Sonnet

**Skills**: aria-quality-valid

**Key Outputs**:
- Quality assessment reports
- Compliance checklists
- Validation summaries
- Improvement recommendations

## Skills

ARIA Phase 2 includes 5 specialized skills providing domain knowledge and validated methodologies.

### 1. aria-research

**Purpose**: Research methodology and citation standards

**Modules**:
- `quick-reference.md` - Fast access to research protocols
- `web-research.md` - Online research techniques
- `INDEX.md` - Module navigation

**Key Features**:
- Source evaluation criteria (CRAAP test)
- Citation standards for regulatory documents
- Evidence hierarchy (Level 1-5)
- Research documentation templates

**Usage**: Automatically loaded by expert-researcher for all research tasks

### 2. aria-analysis

**Purpose**: Statistical analysis and data visualization

**Modules**:
- `quick-reference.md` - Statistical method selection
- `requirement-analysis.md` - Regulatory data requirements
- `feasibility-study.md` - Analysis planning
- `INDEX.md` - Module navigation

**Key Features**:
- Statistical test selection guide
- Effect size interpretation
- Confidence interval standards
- Visualization best practices

**Usage**: Automatically loaded by expert-analyst for data analysis tasks

### 3. aria-writing-style

**Purpose**: Technical writing standards and style guidelines

**Modules**:
- `quick-reference.md` - Style essentials
- Regulatory writing conventions
- Document structure templates

**Key Features**:
- Regulatory document structures
- Writing style guidelines
- Formatting standards
- Consistency rules

**Usage**: Automatically loaded by expert-writer for documentation tasks

### 4. aria-templates

**Purpose**: Document templates and standardized formats

**Modules**:
- `quick-reference.md` - Template selection guide
- `brief-templates.md` - Brief document templates
- `INDEX.md` - Template navigation

**Key Features**:
- Regulatory submission templates
- Brief document templates
- Report structures
- Checklist templates

**Usage**: Automatically loaded by expert-writer and supervisor for document creation

### 5. aria-quality-valid

**Purpose**: Quality validation and compliance verification

**Modules**:
- `quick-reference.md` - Validation criteria
- VALID framework reference
- Compliance checklists

**Key Features**:
- VALID quality dimensions
- Compliance verification checklists
- Quality assessment templates
- Validation reporting

**Usage**: Automatically loaded by expert-reviewer for quality validation

## Commands

ARIA Phase 2 provides 5 slash commands for complete workflow management.

### 1. /aria brief

**Purpose**: Initialize task with structured brief

**Usage**:
```
/aria brief "Implement authentication system"
/aria brief "Refactor payment module" --scope=narrow
/aria brief SPEC-001
```

**Output**: Structured brief document containing:
- Task overview and objectives
- Success criteria
- Constraints and dependencies
- Risk assessment
- Next steps

**Location**: `.moai/briefs/{task_id}.md`

**When to Use**:
- Starting new tasks
- Beginning refactoring efforts
- Analyzing SPEC documents
- Clarifying requirements

### 2. /aria execute

**Purpose**: Execute briefed tasks with quality validation

**Usage**:
```
/aria execute TASK-001
/aria execute TASK-002 --mode=parallel
/aria execute TASK-003 --continue
```

**Execution Modes**:
- `sequential` - Step-by-step with validation
- `parallel` - Independent steps concurrently
- `hybrid` - Auto-select optimal mode

**Features**:
- Progress tracking with visual indicators
- Loop prevention and recovery
- Quality gates (tests, LSP, coverage)
- Checkpoint/resume capability

**When to Use**:
- After brief completion
- Implementing features
- Running automated workflows

### 3. /aria deliver

**Purpose**: Generate final deliverable package

**Usage**:
```
/aria deliver TASK-001
/aria deliver TASK-002 --format=pdf
/aria deliver TASK-003 --include=tests,docs,reports
```

**Output Formats**:
- `markdown` (default) - Version control friendly
- `pdf` - Professional presentation
- `html` - Web-ready format
- `all` - Generate all formats

**Deliverable Package**:
- Implementation artifacts (code, tests, configs)
- Documentation (API, user guides, technical specs)
- Reports (execution, quality, coverage, LSP)
- Artifacts (changelog, migration guide, rollout plan)

**When to Use**:
- After successful execution
- Creating handoff artifacts
- Preparing regulatory submissions

### 4. /aria template

**Purpose**: Generate documents from templates

**Usage**:
```
/aria template regulatory-submission --data=submission_data.json
/aria template technical-report --type=validation
```

**Template Categories**:
- Regulatory submissions
- Technical reports
- Brief documents
- Quality reports

**When to Use**:
- Creating standardized documents
- Ensuring consistent formatting
- Rapid document generation

### 5. /aria knowledge

**Purpose**: Query ARIA knowledge base

**Usage**:
```
/aria knowledge "regulatory requirements for medical devices"
/aria knowledge "statistical methods for compliance data"
```

**Knowledge Areas**:
- Regulatory requirements
- Statistical methods
- Writing standards
- Quality criteria
- Best practices

**When to Use**:
- Quick reference questions
- Methodology queries
- Standard lookups

## MCP Integration

ARIA Phase 2 integrates with Model Context Protocol servers for enhanced capabilities.

### 1. Context7 MCP

**Purpose**: Up-to-date library and documentation lookup

**Usage**:
```python
# Resolve library identifier
library_id = mcp__context7__resolve_library_id(
    query="FDA regulatory guidance",
    libraryName="regulatory-docs"
)

# Get documentation
docs = mcp__context7__get-library-docs(
    libraryId=library_id,
    symbols=["Q8(R2)", "Q9", "Q10"]
)
```

**Benefits**:
- Always-current regulatory guidance
- Official documentation sources
- Quick reference access
- Version-aware lookups

**Used By**: expert-researcher for regulatory research

### 2. Sequential Thinking MCP

**Purpose**: Complex problem decomposition and analysis

**Usage**:
```python
# Break down complex regulatory analysis
mcp__sequential-thinking__sequentialthinking(
    thought="Analyzing requirement applicability...",
    nextThoughtNeeded=True,
    thoughtNumber=1,
    totalThoughts=5
)
```

**Benefits**:
- Step-by-step reasoning
- Complex decision tracking
- Revision and refinement
- Transparent analysis process

**Used By**: supervisor for complex planning, analyst for methodology design

### 3. Notion MCP

**Purpose**: Integration with Notion for documentation management

**Usage**:
```python
# Query Notion database
notion_pages = mcp__notion__queryDatabase(
    databaseId="regulatory_tracker",
    filter={"property": "Status", "equals": "In Progress"}
)

# Create documentation page
page = mcp__notion__createPage(
    parent_id="documentation_space",
    properties={"title": "New Regulatory Submission"}
)
```

**Benefits**:
- Centralized documentation storage
- Team collaboration
- Version tracking
- Search and retrieval

**Used By**: All agents for documentation persistence

## Quick Start

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/henry-1981/ARIA-Phase2.git ~/.claude/plugins/local/aria-phase2
```

2. **Register plugin** in `~/.claude/plugins/installed_plugins.json`:
```json
{
  "plugins": {
    "aria-phase2@local": [{
      "scope": "user",
      "installPath": "~/.claude/plugins/local/aria-phase2",
      "version": "2.0.0",
      "installedAt": "2026-02-09T00:00:00Z",
      "lastUpdated": "2026-02-09T00:00:00Z"
    }]
  }
}
```

3. **Enable in settings** (`~/.claude/settings.json`):
```json
{
  "enabledPlugins": {
    "aria-phase2@local": true
  }
}
```

4. **Restart Claude Code**

### First Task

1. **Create a brief**:
```
/aria brief "Create regulatory submission for new medical device"
```

2. **Review and approve** the brief

3. **Execute the task**:
```
/aria execute TASK-001
```

4. **Review progress** and provide feedback as needed

5. **Deliver results**:
```
/aria deliver TASK-001
```

### Basic Workflow Example

```bash
# User request: Prepare 510(k) submission for new software medical device

/aria brief "Prepare 510(k) submission for new software medical device"
# → System asks clarifying questions
# → Creates structured brief

/aria execute TASK-001
# → Researcher gathers FDA requirements
# → Analyst analyzes predicate device data
# → Writer drafts submission sections
# → Reviewer validates quality and compliance
# → Coordinator aggregates results

/aria deliver TASK-001 --format=all
# → Generates complete submission package
# → Includes all supporting documentation
# → Creates quality validation report
```

## VALID Framework

ARIA Phase 2 implements the VALID quality framework for regulatory documentation.

### 5 Quality Dimensions

#### 1. Verifiable

**Definition**: All claims and data must be traceable to credible sources

**Requirements**:
- Complete citation trails
- Source verification
- Audit trail maintenance
- Evidence backing for assertions

**Validation**:
- Citation completeness check
- Source credibility assessment
- Traceability verification
- Evidence adequacy review

#### 2. Accurate

**Definition**: Content must be factually correct and error-free

**Requirements**:
- Factual correctness
- Calculation accuracy
- Regulatory currency
- Technical precision

**Validation**:
- Fact-checking processes
- Statistical verification
- Regulation update checks
- Peer review

#### 3. Logical

**Definition**: Content must follow clear, rational structure

**Requirements**:
- Coherent argument flow
- Consistent terminology
- Clear cause-effect relationships
- Rational conclusions

**Validation**:
- Structure analysis
- Terminology consistency checks
- Logic flow verification
- Conclusion validation

#### 4. Integrity

**Definition**: Content must be complete and unbiased

**Requirements**:
- No omitted material information
- Balanced presentation
- Conflict of interest disclosure
- Limitations documentation

**Validation**:
- Completeness assessment
- Bias detection
- Disclosure verification
- Limitations review

#### 5. Documented

**Definition**: Content must follow documentation standards

**Requirements**:
- Standard format compliance
- Proper organization
- Clear language
- Appropriate technical level

**Validation**:
- Format compliance check
- Structure verification
- Language clarity assessment
- Technical level review

### Quality Scoring

Each dimension scored 1-5:
- 5: Exceeds requirements
- 4: Meets all requirements
- 3: Meets most requirements
- 2: Meets some requirements
- 1: Fails to meet requirements

**Overall VALID Score**: Average of 5 dimensions (target: 4.0+)

## Workflow

ARIA Phase 2 implements a Brief-Execute-Deliver workflow with 60%-30%-10% time allocation.

### Workflow Phases

```
┌──────────────────────────────────────────────────────────────┐
│                     Brief (60%)                               │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐              │
│  │ Understand │→ │  Define    │→ │  Document  │              │
│  │ Intent     │  │ Scope      │  │ Brief      │              │
│  └────────────┘  └────────────┘  └────────────┘              │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    Execute (30%)                             │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐              │
│  │  Plan      │→ │ Implement  │→ │ Validate   │              │
│  │ Execution  │  │ Solution   │  │ Quality    │              │
│  └────────────┘  └────────────┘  └────────────┘              │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    Deliver (10%)                             │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐              │
│  │ Package    │→ │ Format     │→ │ Present    │              │
│  │ Artifacts  │  │ Output     │  │ Results    │              │
│  └────────────┘  └────────────┘  └────────────┘              │
└──────────────────────────────────────────────────────────────┘
```

### Phase 1: Brief (60%)

**Goal**: Thoroughly understand and document requirements

**Activities**:
- Intent clarification through questioning
- Scope definition with boundaries
- Success criteria identification
- Risk assessment and mitigation
- Resource requirement planning

**Outputs**:
- Structured brief document
- Clarified intent specification
- Execution prerequisites
- Quality gate definitions

**Quality Gates**:
- [ ] Intent clearly understood
- [ ] Scope well-defined
- [ ] Success criteria measurable
- [ ] Risks identified
- [ ] Dependencies documented

### Phase 2: Execute (30%)

**Goal**: Implement solution with quality validation

**Activities**:
- Detailed execution planning
- Agent task assignment
- Parallel execution coordination
- Progress monitoring
- Quality gate validation

**Outputs**:
- Completed implementation
- Test results
- Validation reports
- Execution logs

**Quality Gates**:
- [ ] All tests passing
- [ ] LSP clean (0 errors)
- [ ] Coverage >= 85%
- [ ] VALID score >= 4.0
- [ ] Documentation complete

### Phase 3: Deliver (10%)

**Goal**: Package and present results

**Activities**:
- Artifact collection
- Format generation
- Quality report creation
- Final presentation

**Outputs**:
- Deliverable package
- Quality reports
- Documentation
- Handoff notes

**Quality Gates**:
- [ ] All artifacts included
- [ ] Formats validated
- [ ] Documentation complete
- [ ] Quality reports generated

### Time Allocation Rationale

**Brief (60%)**: Thorough planning prevents rework and ensures alignment

**Execute (30%)**: Efficient execution with clear requirements and validated workflows

**Deliver (10%)**: Streamlined packaging with automated generation

## Next Steps

### Phase 2.2: Enhanced Integration

**Planned Features**:
- Enhanced Notion MCP integration with bi-directional sync
- Regulatory database connectors (FDA, EMA, PMDA)
- Advanced template library with 50+ regulatory templates
- Multi-language support (English, Korean, Japanese)

**Timeline**: Q2 2026

### Phase 2.3: Advanced Analytics

**Planned Features**:
- Predictive compliance analytics
- Automated regulatory change detection
- Risk assessment dashboards
- Collaboration workflow optimization

**Timeline**: Q3 2026

### Phase 3.0: Enterprise Scale

**Planned Features**:
- Multi-tenant architecture
- Advanced security and audit trails
- API for custom integrations
- Enterprise support and SLAs

**Timeline**: Q4 2026

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Apache-2.0 License - see [LICENSE](LICENSE) file for details

## Support

For issues, questions, or contributions:
- GitHub Issues: https://github.com/henry-1981/ARIA-Phase2/issues
- Documentation: https://aria-phase2.readthedocs.io/
- Community: https://discord.gg/aria-community

## Acknowledgments

- Built for [Claude Code](https://claude.ai/claude-code)
- Part of the [MoAI-ADK](https://github.com/henry-1981/moai-adk) ecosystem
- Inspired by regulatory affairs best practices
- Enhanced by community feedback and contributions

---

**Version**: 2.0.0
**Last Updated**: 2026-02-09
**Status**: Production Ready (Phase 2.1)
