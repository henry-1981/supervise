# ARIA - AI Regulatory Intelligence Assistant

> Medical Device RA/QA (Regulatory Affairs / Quality Assurance) specialist powered by AI. Designed for non-developer business professionals.

## Project Overview

ARIA is a specialized AI assistant for medical device regulatory affairs and quality assurance professionals. Unlike generic AI tools, ARIA understands:

- **FDA Regulations**: 510(k), PMA, De Novo submissions, 21 CFR Part 820
- **EU MDR**: CE marking, Technical Documentation, Clinical Evaluation
- **International Standards**: ISO 13485, IEC 62304, ISO 14971, IEC 60601
- **MFDS Regulations**: Korean medical device classification and approval pathways

ARIA follows a **Brief-Execute-Deliver** workflow optimized for regulatory work:

1. **Brief**: Database-driven regulatory strategy analysis with user approval checkpoint
2. **Execute**: Document preparation with domain expert agents
3. **Deliver**: Quality-validated output ready for submission

## Target Users

ARIA is designed for **RA/QA practitioners**, not developers:

- **Regulatory Affairs Managers**: Strategy development, submission preparation
- **QA Engineers**: Quality systems, audits, CAPA management
- **Design Engineers**: Design controls, risk management, documentation
- **Clinical Specialists**: Clinical evaluation, post-market surveillance

## Key Features

### VALID Quality Framework

Every ARIA output passes through the VALID quality gates:

- **V**erified: Content verified against original regulations/standards
- **A**ccurate: Data, figures, and references are current and correct
- **L**inked: Full traceability between requirements, documents, and evidence
- **I**nspectable: Audit trail maintained for regulatory inspections
- **D**eliverable: Output meets submission format requirements

### Specialized Domain Agents

ARIA provides 16 specialized agents across 3 tiers:

**Core Layer (4 agents)**: Orchestration, document management, quality assurance, project tracking

**Business Layer (4 agents)**: Technical writing, data analysis, document review, regulatory research

**Domain Layer (8 agents)**: Regulatory strategy, standards interpretation, risk management, design controls, CAPA, clinical evaluation, submissions, audit management

### Natural Language Interface

No coding required. Simply describe your regulatory task in natural language:

```
/aria "Prepare a 510(k) submission for our new blood pressure monitor"
```

ARIA will:
1. Ask clarifying questions (device classification? predicate device? target market?)
2. Query regulatory databases and standards
3. Present regulatory strategy brief for approval
4. Generate submission documents with proper citations
5. Validate against VALID quality framework
6. Deliver submission-ready package

## Architecture

ARIA is built on MoAI-ADK principles, adapted for regulatory workflows:

| Aspect | MoAI-ADK (Development) | ARIA (RA/QA) |
|--------|----------------------|---------------|
| **Target Users** | Developers | RA/QA practitioners |
| **Workflow** | Plan-Run-Sync | Brief-Execute-Deliver |
| **Quality Framework** | TRUST 5 (code quality) | VALID (regulatory compliance) |
| **Token Budget** | Balanced (15%-75%-10%) | Brief-heavy (60%-30%-10%) |
| **Output** | Code, tests, APIs | Regulatory documents, submissions |

### Read-Think-Write-Verify Pattern

ARIA implements the universal knowledge worker pattern:

- **Read**: Regulation/standard documents, precedents, guidelines
- **Think**: Regulatory interpretation, strategy development, analysis
- **Write**: Regulatory documents, reports, submission packages
- **Verify**: Compliance review, quality gates, audit readiness

- **Automate Documentation**: Reduce regulatory document creation time by 60% through AI-assisted writing
- **Ensure Compliance**: Maintain VALID quality standards across all regulatory submissions
- **Streamline Workflows**: Orchestrate complex multi-step regulatory processes with minimal manual intervention
- **Enable Collaboration**: Coordinate cross-functional regulatory teams through intelligent task management
- **Ensure Quality**: Implement TRUST 5 quality gates for all deliverables

### Standalone Installation

- Regulatory Affairs professionals
- Quality Assurance specialists
- Compliance officers
- Regulatory operations teams
- Pharmaceutical and medical device companies

```bash
git clone https://github.com/henry-1981/supervise.git \
  ~/.claude/plugins/local/aria
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

> Note: Add to existing `plugins` object if other plugins are present.

- Notion workspace 및 API 키
- Google Workspace 계정
- Node.js (MCP 서버 실행)
- Claude Code with MCP support

### MCP 서버 설정

`.mcp.json` 파일에 MCP 서버를 추가합니다:

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

> Note: The marketplace plugin uses the legacy Cowork Supervisor name. ARIA v2.0+ rebrands to the specialized RA/QA focus.

### 초기화 명령어

3. **Execute the task**:
```
/aria "Help with 510(k) submission preparation"
```

ARIA will guide you through:
1. **Brief Phase**: Device classification, predicate device search, regulatory pathway analysis
2. **Approval Checkpoint**: Review and approve regulatory strategy
3. **Execute Phase**: Document preparation with domain experts
4. **Deliver Phase**: VALID-validated submission package

## Workflow Examples

### 510(k) Submission Preparation

5. **Deliver results**:
```
/aria "Prepare 510(k) submission for Class II medical device"
```

ARIA executes:
- **expert-researcher**: Predicate device database search
- **expert-regulatory**: Classification and pathway analysis
- **expert-submission**: Package structure and requirements
- **expert-writer**: Document section drafts
- **expert-reviewer**: Compliance verification
- **manager-quality**: VALID quality gates

### CAPA Management

```
/aria "Open CAPA for nonconforming product complaint"
```

ARIA executes:
- **expert-capa**: CAPA form creation
- **expert-analyst**: Complaint trend analysis
- **expert-risk**: Risk impact assessment
- **Root Cause Analysis**: 5 Whys, Fishbone diagrams
- **Action Planning**: Corrective/preventive measures
- **manager-project**: Timeline and assignee tracking

### Design Control Documentation

## 워크플로우

### Brief-Execute-Deliver 방법론

**Brief Phase:**
1. 사용자 요청 분석 및 규제 도메인 식별
2. 핵심 요구사항 및 제약조건 추출
3. 적용 가능한 규정 식별 (FDA, MDR, MFDS, ISO 13485)
4. 전달물 및 수락 기준 정의

**Execute Phase:**
1. 적절한 도메인 전문가 에이전트에 위임
2. MCP 통합 조정 (Notion, Google, Context7)
3. 작업 완료 및 품질 게이트 모니터링

**Deliver Phase:**
1. 추적 가능성을 포함한 전달물 컴파일
2. Notion DB 감사 추적 업데이트
3. 컴플라이언스 문서 생성

### VALID 품질 프레임워크

모든 전달물은 VALID 프레임워크를 충족해야 합니다:

- **Verified:** 규정 출처에서 요구사항 검증
- **Accurate:** 규정 해석 정확성 보장
- **Linked:** 구체적 규정 조항과 연결
- **Inspectable:** 감사 준비 형식 제공
- **Deliverable:** 제출 준비 전달물 생성

## 사용 예시

### 예시 1: 510(k) 제출 준비

```bash
# Brief Phase
/aria search "510(k) submission requirements for software medical device"

# Execute Phase
# aria-submission 에이전트가 자동으로 위임됨
# Notion Submission Tracker DB 업데이트
# Google Calendar에 데드라인 추가

# Deliver Phase
/aria status submission
/aria audit search --entity submission
```
/aria "Create Design History File for new software medical device"
```

ARIA executes:
- **expert-design-control**: DHF structure and requirements
- **expert-risk**: Hazard identification and analysis
- **expert-standards**: IEC 62304 compliance verification
- **Traceability Matrix**: Auto-generated requirements traceability
- **manager-docs**: Document version and approval workflow

## MCP Integrations

ARIA integrates with external services for comprehensive workflow support:

### Notion MCP - Central Knowledge Hub

- Regulatory document storage and version control
- CAPA tracker database
- Risk register management
- Submission tracking dashboard
- Knowledge base accumulation

### Google Workspace MCP - Collaboration

- Regulatory correspondence (Gmail)
- Collaborative document editing (Google Docs)
- Requirements matrices and data analysis (Google Sheets)
- Deadline and audit scheduling (Google Calendar)

### Context7 MCP - Regulatory Research

- Real-time regulatory document lookup
- Latest standards and guidance access
- Citation verification and referencing

### Sequential Thinking MCP - Complex Analysis

- Regulatory pathway decision support
- Substantial equivalence logic development
- Multi-market strategy analysis
- Risk-benefit assessment

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
supervise/
├── docs/
│   ├── CONTEXT.md              # Project context and background
│   └── specs/
│       └── ARCHITECTURE-REDESIGN.md  # Complete architecture specification
├── .claude-plugin/
│   ├── plugin.json             # Plugin manifest
│   └── capabilities.yaml       # Capability declaration
├── agents/
│   ├── core/                   # Core orchestration agents (4)
│   ├── business/               # Business workflow agents (4)
│   └── raqa/                   # RA/QA domain agents (8)
├── skills/
│   ├── aria-core/              # Core orchestration skills
│   ├── aria-domain-raqa/       # RA/QA domain knowledge
│   ├── aria-knowledge-fda/     # FDA regulations
│   ├── aria-knowledge-eumdr/   # EU MDR knowledge
│   ├── aria-knowledge-standards/  # International standards
│   └── aria-quality-valid/     # VALID framework implementation
├── commands/
│   └── aria.md                 # /aria command interface
├── templates/                  # Regulatory document templates
│   ├── 510k/
│   ├── design-control/
│   ├── risk-management/
│   ├── capa/
│   └── clinical/
├── CHANGELOG.md
├── CLAUDE.md                   # ARIA execution directives
└── README.md
```

## Documentation

- **[CONTEXT.md](docs/CONTEXT.md)**: Project background, MoAI-ADK benchmarking, design decisions, domain selection rationale
- **[ARCHITECTURE-REDESIGN.md](docs/specs/ARCHITECTURE-REDESIGN.md)**: Complete system architecture, agent catalog, workflow design, implementation roadmap
- **[CHANGELOG.md](CHANGELOG.md)**: Version history and changes

1. Fork 하세요
2. 기능 브랜치를 만드세요 (`git checkout -b feature/AmazingFeature`)
3. 커밋하세요 (`git commit -m 'Add some AmazingFeature'`)
4. 푸시하세요 (`git push origin feature/AmazingFeature`)
5. Pull Request를 여세요

ARIA is under active architecture redesign. Contributions will be welcomed after Phase 1 implementation.

For now, please:
1. Review the architecture documentation
2. Provide feedback on the RA/QA domain requirements
3. Share use cases and regulatory scenarios

## Roadmap

### Phase 1: Core Framework (Completed ✅)
- ✅ Plugin skeleton and basic orchestration
- ✅ `/aria` command implementation
- ✅ Brief-Execute-Deliver workflow structure
- ✅ Core orchestrator agent with intent classification
- ✅ aria-core skill with VALID framework
- ✅ Plugin manifest (plugin.json, capabilities.yaml)
- ✅ Configuration system (aria.yaml)
- ✅ CLAUDE.md execution directives

### Phase 2: Business Agents (In Progress 🚧)
- Generic business workflow agents
- VALID quality framework implementation
- Document management workflows
- Template system integration

### Phase 2: Business Agents
- Generic business workflow agents
- VALID quality framework
- Document management

### Phase 3: RA/QA Specialization
- 8 domain-specific agents
- Regulatory knowledge bases
- Core workflows (510(k), CAPA, Design Control)

### Phase 4: MCP Integrations
- Notion database integration
- Google Workspace connectivity
- Context7 and Sequential Thinking

### Phase 5: Advanced Features
- Agent memory and learning
- Advanced analytics
- Multi-product project management

For regulatory content contributions:
- Cite specific standards (e.g., ISO 13485:2016 Section 4.2.3)
- Include regulatory source references
- Ensure VALID framework compliance

## 연락처

Apache-2.0 License - see [LICENSE](LICENSE) file for details

## Support

For issues, questions, or contributions:
- GitHub Issues: https://github.com/henry-1981/ARIA-Phase2/issues
- Documentation: https://aria-phase2.readthedocs.io/
- Community: https://discord.gg/aria-community

---

- Built for [Claude Code](https://claude.ai/claude-code)
- Inspired by [MoAI-ADK](https://github.com/henry-1981/Agent-RA) principles
- Part of the [Team Attention](https://github.com/team-attention) plugin ecosystem

---

**ARIA v2.0.0** - Specialized for Medical Device RA/QA professionals
