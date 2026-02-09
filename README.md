# ARIA (AI Regulatory Intelligence Assistant)

> AI-powered Regulatory Affairs and Quality Assurance assistant for Medical Device professionals

## Overview

ARIA is a Claude Code plugin specialized for Medical Device RA/QA (Regulatory Affairs / Quality Assurance) workflows. It enables non-developer business professionals to perform complex regulatory tasks through natural language interactions.

### What ARIA Does

ARIA acts as your intelligent regulatory assistant, helping you with:

- **Document Drafting**: Create regulatory submissions, technical files, and compliance documents
- **Analysis**: Analyze regulatory requirements, standards, and pathways
- **Review**: Review documents for compliance and accuracy
- **Research**: Search and retrieve regulatory information with source citations

### How ARIA Works

```
Your Natural Language Request
         |
         v
  [Intent Analysis]
         |  What do you need?
         |  Document drafting, analysis, review, or search?
         v
  [Brief Phase - 60%]
         |  Regulatory strategy analysis
         |  Requirements identification
         |  Resource estimation
         v
  [Approval Checkpoint]
         |  Review and approve strategy
         v
  [Execute Phase - 30%]
         |  Document preparation
         |  Content generation
         |  Quality validation
         v
  [Deliver Phase - 10%]
         |  VALID quality gates
         |  Format and package
         v
  Quality-Validated Output
```

## Installation

### Standalone Installation

1. **Clone the plugin**:

```bash
git clone https://github.com/henry-1981/supervise.git \
  ~/.claude/plugins/local/aria
cd ~/.claude/plugins/local/aria
git checkout feature/SPEC-ARIA-001
```

2. **Register in `~/.claude/plugins/installed_plugins.json`**:

```json
{
  "plugins": {
    "aria@local": [{
      "scope": "user",
      "installPath": "~/.claude/plugins/local/aria",
      "version": "2.0.0",
      "installedAt": "2026-02-09T00:00:00Z",
      "lastUpdated": "2026-02-09T00:00:00Z"
    }]
  }
}
```

3. **Enable in `~/.claude/settings.json`**:

```json
{
  "enabledPlugins": {
    "aria@local": true
  }
}
```

4. **Restart Claude Code**

## Quick Start

```
/aria "510(k) submission preparation for my device"
```

ARIA will:
1. Ask clarifying questions (device type, classification, predicate device)
2. Analyze regulatory pathway (Brief phase)
3. Present strategy for your approval
4. Prepare submission documents (Execute phase)
5. Deliver quality-validated output (Deliver phase)

## Usage Examples

### Document Drafting

```
/aria "Create a 510(k) submission for Class II medical device"
```

```
/aria "Prepare ISO 13485 internal audit checklist"
```

```
/aria "Draft a technical file for EU MDR compliance"
```

### Analysis

```
/aria "Analyze regulatory requirements for combination product"
```

```
/aria "Compare FDA and EU MDR classification pathways"
```

```
/aria "Assess post-market surveillance requirements"
```

### Review

```
/aria "Review this IFU for compliance with FDA labeling requirements"
```

```
/aria "Check if our design control process meets 21 CFR 820.30"
```

### Search

```
/aria "Find latest FDA guidance on software as a medical device"
```

```
/aria "Search for ISO 14971 risk management examples"
```

## Key Features

### Brief-Execute-Deliver Workflow

ARIA uses a three-phase workflow optimized for regulatory tasks:

**Brief Phase (60% token budget)**
- Intent analysis and classification
- Regulatory strategy development
- Requirements identification
- Resource estimation
- User approval checkpoint

**Execute Phase (30% token budget)**
- Document preparation
- Content generation
- Quality validation
- Compliance verification

**Deliver Phase (10% token budget)**
- VALID quality gates
- Format validation
- Final packaging
- Distribution (local files, Phase 4: Notion integration)

### VALID Quality Framework

All ARIA outputs pass through the VALID quality framework:

- **V**erified: Content matches source regulation text with citations
- **A**ccurate: Data, figures, and references are current and correct
- **L**inked: Traceability between requirements, documents, and evidence
- **I**nspectable: Audit trail maintained with decision rationale
- **D**eliverable: Output meets submission format requirements

### Natural Language Interface

- **Korean Language**: All user-facing responses in Korean
- **Plain Language Errors**: No technical jargon, clear next-step guidance
- **Approval Checkpoints**: User approval before major decisions
- **Max 4 Options**: Clear, focused questions

### Regulatory Citations

ARIA always cites sources for regulatory claims:

- Format: Standard name, section number, version/date
- Example: "FDA 21 CFR Part 820.30(i) - Design Controls"
- Context7 MCP integration for up-to-date documentation

## Project Structure

```
aria/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest v2.0.0
│   └── capabilities.yaml        # Capability declaration
├── .claude/
│   ├── agents/
│   │   └── aria/
│   │       └── orchestrator.md  # Main orchestrator agent
│   ├── commands/
│   │   └── aria.md              # /aria command
│   └── skills/
│       └── aria-core/
│           ├── SKILL.md         # Core orchestration skill
│           └── modules/
│               ├── workflow.md  # Brief-Execute-Deliver workflow
│               └── quality.md   # VALID framework
├── .moai/
│   ├── specs/
│   │   └── SPEC-ARIA-001/
│   │       └── spec.md          # Complete specification
│   └── config/
│       └── sections/
│           ├── user.yaml
│           ├── language.yaml
│           └── quality.yaml
├── aria.yaml                    # ARIA configuration
├── .mcp.json                    # MCP server configuration
├── CLAUDE.md                    # ARIA execution directives
├── README.md                    # This file
└── CHANGELOG.md                 # Version history
```

## Configuration

### aria.yaml

ARIA behavior is configured via `aria.yaml`:

```yaml
# Language Settings
language:
  conversation_language: ko              # User-facing language
  agent_prompt_language: en              # Internal communication
  documentation_language: ko             # Regulatory documents

# Workflow Settings
workflow:
  phases:
    brief:
      token_budget: 60                   # 60% for analysis
      require_approval: true             # User approval checkpoint
      max_questions: 5                   # Maximum clarifying questions

    execute:
      token_budget: 30                   # 30% for execution
      max_parallel_agents: 3             # Parallel agent limit

    deliver:
      token_budget: 10                   # 10% for delivery
      enforce_valid: true                # VALID quality gates

# Quality Framework
quality:
  valid:
    verified:
      require_citations: true            # Source citations required
      citation_format: "{standard} {section} ({version})"
    accurate:
      reference_check_days: 365          # Currency validation
    linked:
      traceability: true                 # Requirement linking
    inspectable:
      decision_rationale: true           # Audit trail
    deliverable:
      templates: true                    # Format templates
```

### MCP Integration

ARIA integrates with MCP servers for enhanced capabilities:

**Context7 MCP** (Phase 1)
- Up-to-date regulatory documentation lookup
- Current FDA guidance documents
- Latest ISO standard versions
- Regulation citation verification

**Sequential Thinking MCP** (Phase 1)
- Complex regulatory pathway analysis
- Substantial equivalence logic
- Multi-market strategy development

**Notion MCP** (Phase 4 - Planned)
- Knowledge base integration
- Document management
- CAPA tracking
- Risk register

## Supported Regulatory Domains

### FDA (United States)
- 510(k) Premarket Notification
- PMA (Premarket Approval)
- IDE (Investigational Device Exemption)
- 21 CFR Part 820 (QSR)
- Labeling requirements

### EU MDR (European Union)
- Technical File preparation
- Clinical Evaluation Reports
- Post-Market Surveillance
- UDI requirements
- Notified Body submissions

### ISO Standards
- ISO 13485 (QMS)
- ISO 14971 (Risk Management)
- IEC 62304 (Software Lifecycle)
- IEC 62366 (Usability Engineering)

## Development

### Phase 1 (Current - v2.0.0)
- Plugin structure and basic orchestration
- /aria command with natural language interface
- Brief-Execute-Deliver workflow skeleton
- VALID quality framework foundation
- MCP integration (Context7, Sequential Thinking)

### Phase 2 (Planned)
- Business agents (writer, analyst, reviewer, researcher)
- Document templates and formatting
- PDF/Word export
- FAQ and progress indicators

### Phase 3 (Planned)
- RA/QA domain agents (regulatory, standards, risk, design control, CAPA, clinical, submission, audit)
- Regulatory knowledge bases
- Advanced document automation

### Phase 4 (Planned)
- Notion MCP integration
- Google Workspace MCP integration
- Knowledge base synchronization
- CAPA tracker integration

### Phase 5 (Planned)
- Agent memory and learning
- Advanced analytics
- Workflow optimization
- Multi-language support expansion

## Quality Assurance

ARIA follows the VALID quality framework:

- All regulatory claims cite sources (standard, section, version)
- Error messages use plain Korean with next-step guidance
- User approval checkpoints before major decisions
- Questions present maximum 4 options
- Document traceability maintained
- Audit trail captured for all decisions

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/SPEC-XXX-001`)
3. Create SPEC document using MoAI SPEC workflow
4. Implement following ARIA architecture
5. Submit Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for [Claude Code](https://claude.ai/claude-code)
- Part of the [Cowork](https://github.com/henry-1981/supervise) plugin ecosystem
- Architectural patterns inspired by [MoAI-ADK](https://github.com/henry-1981/Agent-RA)
- Regulatory domain expertise from medical device RA/QA professionals

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

### v2.0.0 (2026-02-09)
- ARIA Phase 1: Core Framework Implementation
- Plugin structure with orchestrator agent
- /aria command with natural language interface
- Brief-Execute-Deliver workflow
- VALID quality framework foundation
- MCP integration (Context7, Sequential Thinking)

### v1.0.0 (2026-02-05)
- Cowork Supervisor (original plugin)

## Support

For issues, questions, or contributions:

- GitHub Issues: [henry-1981/supervise](https://github.com/henry-1981/supervise/issues)
- Documentation: See CLAUDE.md and .moai/specs/SPEC-ARIA-001/spec.md

---

**ARIA** - Your AI Regulatory Intelligence Assistant for Medical Device RA/QA excellence.
