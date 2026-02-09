# ARIA - AI Regulatory Intelligence Assistant

> Specialized AI assistant system for medical device Regulatory Affairs (RA) and Quality Assurance (QA) professionals

## Overview

ARIA (AI Regulatory Intelligence Assistant) is a specialized Claude Code plugin designed for medical device regulatory professionals. ARIA automates regulatory compliance workflows, standardizes documentation processes, and provides intelligent guidance through complex regulatory landscapes including FDA 21 CFR Part 820, EU MDR, ISO 13485, and MFDS requirements.

## Key Capabilities

ARIA provides comprehensive regulatory workflow support through eight domain-specialized expert agents:

1. **Regulatory Strategy**: FDA 510(k), PMA, De Novo pathway analysis, EU MDR CE Marking, MFDS market authorization
2. **Standards Compliance**: ISO 13485 QMS, ISO 14971 risk management, IEC 62304 software lifecycle, IEC 62366-1 usability
3. **Risk Management**: FMEA analysis, risk-benefit assessment, ALARP principle application with Notion Risk Register integration
4. **Design Control**: DHF/DMR/DHR management, design input/output verification, design validation protocols
5. **CAPA Management**: End-to-end CAPA lifecycle from issue identification to effectiveness validation
6. **Clinical Evaluation**: Clinical investigation planning, CER preparation, post-market clinical follow-up (PMCF)
7. **Submission Preparation**: FDA 510(k) eCopy, PMA modules, EU MDR Technical File, MFDS submission templates
8. **Audit Support**: Internal audit protocols, external audit (NB, FDA) preparation, finding response

## ARIA Architecture

### Multi-Agent Orchestration

ARIA uses intelligent task orchestration similar to the Cowork Supervisor pattern:

1. **Clarifies** your regulatory request through targeted questions
2. **Discovers** relevant regulatory requirements and standards
3. **Plans** the regulatory strategy or documentation approach
4. **Orchestrates** multiple expert agents in parallel/sequential execution
5. **Aggregates** results into compliant regulatory documentation

### Expert Agents

Eight domain-specialized agents with progressive disclosure knowledge delivery:

- **expert-regulatory**: Regulatory strategy and pathway analysis (Opus model)
- **expert-standards**: ISO/IEC standards compliance (Opus model)
- **expert-risk**: ISO 14971 risk management (Opus model)
- **expert-design-control**: Design control and DHF management (Sonnet model)
- **expert-capa**: CAPA lifecycle management (Sonnet model)
- **expert-clinical**: Clinical evaluation support (Opus model)
- **expert-submission**: Regulatory submission preparation (Sonnet model)
- **expert-audit**: Audit preparation and support (Sonnet model)

## Installation

### Standalone Installation (Recommended)

1. **Clone the plugin**:

```bash
git clone https://github.com/henry-1981/aria.git \
  ~/.claude/plugins/local/aria
```

2. **Register in `~/.claude/plugins/installed_plugins.json`**:

```json
{
  "plugins": {
    "aria@local": [{
      "scope": "user",
      "installPath": "~/.claude/plugins/local/aria",
      "version": "3.0.0",
      "installedAt": "2026-02-09T00:00:00Z",
      "lastUpdated": "2026-02-09T00:00:00Z"
    }]
  }
}
```

> Note: If the file already has other plugins, add the `aria@local` entry to the existing `plugins` object.

3. **Enable in `~/.claude/settings.json`**:

```json
{
  "enabledPlugins": {
    "aria@local": true
  }
}
```

> Note: Add to the existing `enabledPlugins` object if other plugins are already enabled.

4. **Configure MCP servers in `~/.mcp.json`** (optional, for enhanced capabilities):

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp"]
    }
  }
}
```

5. **Restart Claude Code**

## Quick Start

```
"Prepare 510(k) submission for glucose monitor"
```

ARIA will:
1. Ask clarifying questions (predicate device? intended use? technology?)
2. Discover relevant regulatory requirements (FDA 510(k), eCopy format)
3. Present a submission plan for your approval
4. Execute expert agents to prepare submission documentation
5. Aggregate results into submission-ready technical file

## How It Works

```
Your Regulatory Request
         |
         v
  [Intent Clarifier]
         |  Asks: What regulatory pathway?
         |  Asks: Which markets? Which device type?
         v
  [Capability Discoverer]
         |  Scans: Which agents are relevant?
         |  Maps: Which regulations apply?
         v
  [Supervisor Planner]
         |  Creates: Regulatory strategy plan
         |  You: Approve or modify approach
         v
  [Orchestra]
         |  Executes: Expert agents in parallel/sequence
         |  Handles: Regulatory conflicts and fallbacks
         v
  [Aggregator]
         |  Combines: Regulatory documentation
         |  Validates: Compliance with standards
         v
  Submission-Ready Output with Citations
```

## Usage Examples

### Regulatory Strategy

```
"Analyze regulatory pathway for new AI diagnostic software in US and EU markets"
```

ARIA will:
- expert-regulatory: Analyze FDA 510(k) vs De Novo pathway
- expert-standards: Check IEC 62304 software lifecycle requirements
- expert-risk: Assess ISO 14971 risk management needs
- expert-clinical: Evaluate clinical evidence requirements

### Risk Management

```
"Perform FMEA analysis for new surgical instrument with ISO 14971 compliance"
```

ARIA will:
- expert-risk: Conduct FMEA analysis with risk scoring
- expert-design-control: Link risks to design controls
- expert-standards: Validate against ISO 14971 requirements
- Create Notion Risk Register entries with traceability

### Submission Preparation

```
"Prepare FDA 510(k) submission for orthopedic implant with predicate device analysis"
```

ARIA will:
- expert-submission: Generate eCopy format sections 1-20
- expert-regulatory: Analyze substantial equivalence criteria
- expert-clinical: Prepare clinical performance summary
- expert-design-control: Compile design verification/validation data

### CAPA Management

```
"Manage CAPA for non-conforming product with root cause analysis and effectiveness check"
```

ARIA will:
- expert-capa: Guide through CAPA lifecycle
- expert-risk: Assess risk from nonconformity
- expert-audit: Ensure documentation for audit trail
- Update Notion CAPA Tracker with progress

### Audit Preparation

```
"Prepare for upcoming FDA QSR inspection with mock audit and document readiness check"
```

ARIA will:
- expert-audit: Conduct mock audit simulation
- expert-standards: Check ISO 13485 compliance gaps
- expert-design-control: Verify DHF/DMR/DHR completeness
- Generate inspection readiness report

## Regulatory Domains

ARIA covers all major medical device regulatory domains:

| Domain | Capabilities |
|--------|-------------|
| FDA Regulations | 510(k), PMA, De Novo, 21 CFR Part 820 QSR, HUD exemptions |
| EU MDR | CE Marking, Technical Files, Clinical Evaluation, Vigilance |
| International Standards | ISO 13485, ISO 14971, IEC 62304, IEC 62366, IEC 60601 |
| MFDS (Korea) | Market authorization, MFDS requirements, local standards |
| Risk Management | FMEA, FTA, Risk-Benefit Analysis, ALARP principle |
| Design Control | Design inputs/outputs, V&V, DHF/DMR/DHR traceability |
| CAPA | Root cause analysis, corrective actions, effectiveness verification |
| Clinical | Clinical investigations, CER, PMCF, literature reviews |
| Submissions | eCopy format, technical documentation, readiness reviews |
| Audits | Internal audits, external audits (NB, FDA), mock inspections |

## Project Structure

```
aria/
├── .claude-plugin/
│   ├── plugin.json        # Plugin manifest
│   └── capabilities.yaml  # Capability declaration
├── .claude/
│   ├── agents/
│   │   ├── aria/          # ARIA expert agents (8)
│   │   │   ├── expert-regulatory.md
│   │   │   ├── expert-standards.md
│   │   │   ├── expert-risk.md
│   │   │   ├── expert-design-control.md
│   │   │   ├── expert-capa.md
│   │   │   ├── expert-clinical.md
│   │   │   ├── expert-submission.md
│   │   │   └── expert-audit.md
│   │   └── moai/          # Framework agents
│   ├── skills/
│   │   ├── aria-/         # ARIA domain skills (9)
│   │   │   ├── aria-domain-raqa/
│   │   │   ├── aria-knowledge-fda/
│   │   │   ├── aria-knowledge-eumdr/
│   │   │   ├── aria-knowledge-standards/
│   │   │   ├── aria-knowledge-mfds/
│   │   │   ├── aria-risk-management/
│   │   │   ├── aria-design-control/
│   │   │   ├── aria-capa-process/
│   │   │   └── aria-submission-templates/
│   │   └── moai/          # Framework skills
│   ├── commands/
│   │   └── supervise.md   # Supervision command
│   ├── rules/             # MoAI-ADK rules
│   └── templates/         # Agent templates
├── .moai/
│   ├── config/            # MoAI configuration
│   ├── specs/             # Specification documents
│   └── project/           # Project documentation
│       ├── product.md     # Product overview
│       ├── structure.md   # Codebase structure
│       └── tech.md        # Technical stack
├── agents/                # Custom agents
│   ├── supervisor.md
│   ├── intent-clarifier.md
│   ├── capability-discoverer.md
│   ├── supervisor-planner.md
│   ├── orchestra.md
│   └── aggregator.md
├── skills/                # Custom skills
│   └── cowork-supervisor/
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## Configuration

### Basic Setup

No configuration required for basic functionality. ARIA automatically:
- Detects regulatory keywords in your requests
- Activates relevant expert agents
- Applies appropriate regulatory standards

### Enhanced Configuration

For advanced capabilities, configure the following:

**MCP Servers** (in `~/.mcp.json`):

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp"]
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/client"]
    }
  }
}
```

**Notion Integration** (optional):

Create Notion databases for:
- CAPA Tracker: Issue management and lifecycle
- Risk Register: FMEA analysis and risk scoring
- Document Registry: DHF/DMR/DHR traceability

Configure integration tokens in ARIA settings for automatic updates.

**Language Preferences** (in `.moai/config/sections/language.yaml`):

```yaml
language:
  conversation_language: "ko"  # Korean responses
  documentation: "ko"            # Korean docs
  code_comments: "ko"            # Korean comments
```

## Quality Framework

ARIA implements two quality frameworks:

### VALID Framework (Regulatory Content)

- **Verified**: All regulatory claims cite standard, section, version
- **Accurate**: Information validated against authoritative sources
- **Linked**: Traceability across requirements, risks, tests, documents
- **Inspectable**: Complete audit trail for decisions
- **Deliverable**: Outputs meet submission readiness criteria

### TRUST 5 Framework (Code Quality)

- **Tested**: 85%+ coverage with characterization tests
- **Readable**: Clear naming and English comments
- **Unified**: Consistent formatting with ruff/black
- **Secured**: OWASP compliance and input validation
- **Trackable**: Conventional commits with issue references

## Progress Tracking

ARIA development follows MoAI SPEC-First DDD methodology:

- **Phase 1**: Core Framework (Completed)
- **Phase 2**: Business Workflow (Future)
- **Phase 3**: RA/QA Specialization (Completed - 8 expert agents, 9 domain skills)
- **Phase 4**: Advanced Features (Planned)

See `.moai/specs/SPEC-ARIA-003/` for detailed specifications and implementation status.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

For regulatory content contributions:
- Cite specific standards (e.g., ISO 13485:2016 Section 4.2.3)
- Include regulatory source references
- Ensure VALID framework compliance

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for [Claude Code](https://claude.ai/claude-code)
- Powered by [MoAI-ADK](https://github.com/henry-1981) patterns
- Inspired by medical device RA/QA best practices
- Regulatory content based on FDA, EU MDR, ISO standards
