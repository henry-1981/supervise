# ARIA Product Overview

## Product Identity

ARIA (AI Regulatory Intelligence Assistant) is a specialized AI assistant system designed for medical device Regulatory Affairs (RA) and Quality Assurance (QA) professionals. ARIA automates regulatory compliance workflows, standardizes documentation processes, and provides intelligent guidance through complex regulatory landscapes.

## Value Proposition

ARIA addresses critical pain points in medical device regulatory management:

- Regulatory Complexity: Navigates FDA 21 CFR Part 820, EU MDR, ISO 13485, and MFDS requirements
- Documentation Burden: Automates DHF (Design History File), DMR (Device Master Record), DHR (Device History Record) creation
- Risk Management: Implements ISO 14971 risk management processes with FMEA analysis
- Submission Readiness: Prepares 510(k), PMA, CE Marking technical documentation
- Quality Systems: Manages CAPA (Corrective and Preventive Action) lifecycle end-to-end

## Target Users

Primary Users: RA/QA professionals at medical device companies

- Regulatory Affairs Managers: Strategy development, submission preparation, market authorization
- Quality Assurance Engineers: CAPA management, audit preparation, compliance monitoring
- Clinical Evaluation Specialists: Clinical investigation planning, CER (Clinical Evaluation Report) preparation
- Design Control Engineers: Design V&V, risk management, technical documentation

User Profile: Non-developers, natural language interface preference, deep regulatory domain expertise

## Product Architecture

ARIA is built as a Claude Code Plugin with MoAI-ADK patterns:

Plugin Architecture: Standalone plugin for Claude Code with multi-agent orchestration

Agent Types: Three-tier specialization system

- Core Orchestrator Agents: supervisor, intent-clarifier, capability-discoverer, supervisor-planner, orchestra, aggregator
- Manager Agents: manager-docs, manager-quality, manager-project for workflow coordination
- Expert Agents: Eight domain-specialized agents for regulatory workflows

Skill System: Progressive disclosure architecture with 9 domain skills

Level 1: Metadata loaded at startup approximately 100 tokens per skill
Level 2: Full skill body when triggered approximately 5000 tokens
Level 3: Knowledge modules on-demand unlimited tokens

## Core Features

Feature 1: Regulatory Strategy Development

expert-regulatory agent with aria-domain-raqa skill provides multi-market regulatory pathway analysis. Supports FDA 510(k), PMA, De Novo classification determination, EU MDR CE Marking requirements, MFDS market authorization. Context7 integration for latest regulatory updates.

Feature 2: Standards Compliance Management

expert-standards agent with aria-knowledge-standards skill manages ISO 13485 QMS, ISO 14971 risk management, IEC 62304 software lifecycle, IEC 62366-1 usability engineering. Automated gap analysis against standard requirements with section-level precision.

Feature 3: Risk Management Automation

expert-risk agent with aria-risk-management skill implements FMEA (Failure Modes and Effects Analysis), risk-benefit analysis framework, ALARP (As Low As Reasonably Practicable) principle application, risk acceptability determination. Integration with Notion Risk Register for traceability.

Feature 4: Design Control System

expert-design-control agent with aria-design-control skill manages design input requirements, design output verification, design validation protocols, design transfer process, DHF/DMR/DHR traceability matrix.

Feature 5: CAPA Lifecycle Management

expert-capa agent with aria-capa-process skill handles issue identification and root cause analysis, CAPA initiation and planning, implementation verification, effectiveness validation, closure and documentation. Notion CAPA Tracker integration.

Feature 6: Clinical Evaluation Support

expert-clinical agent with aria-domain-raqa skill supports clinical investigation planning, CER (Clinical Evaluation Report) preparation, clinical literature review, post-market clinical follow-up (PMCF).

Feature 7: Submission Preparation

expert-submission agent with aria-submission-templates skill provides FDA 510(k) eCopy templates, PMA modules structure, EU MDR Technical File format, MFDS submission requirements. Automated section completion and validation.

Feature 8: Audit Readiness

expert-audit agent with aria-domain-raqa skill prepares internal audit protocols, external audit (NB, FDA) support, mock audit simulations, finding response preparation.

## Technical Integration

MCP Server Integration

Context7: Real-time regulatory standard updates and documentation lookup
Notion API: CAPA Tracker, Risk Register, Document Registry integration
Sequential Thinking: Complex regulatory strategy analysis and decision trees

Model Assignment Strategy

Opus: High-complexity regulatory analysis (expert-regulatory, expert-standards, expert-risk, expert-clinical)
Sonnet: Process and submission workflows (expert-design-control, expert-capa, expert-submission, expert-audit)

## Quality Framework

VALID Quality Framework: Five-pillar quality assurance system

Verified: All regulatory claims cite standard, section, version
Accurate: Information validated against authoritative regulatory sources
Linked: Traceability maintained across requirements, risks, tests, documents
Inspectable: Complete audit trail for all decisions and recommendations
Deliverable: Final outputs meet submission readiness criteria

## Market Position

Competitive Differentiation: Specialized for medical device RA/QA with domain-specific expert agents

Unlike generic AI assistants, ARIA provides regulated industry expertise with citation precision and workflow automation tailored to medical device development lifecycles.

## Roadmap

Phase 1: Core Framework (Completed)

Core orchestrator and manager agents, business workflow agents, Brief-Execute-Deliver workflow foundation, VALID quality framework definition

Phase 2: Business Workflow (Future)

Brief-Execute-Deliver full implementation, task decomposition and assignment, progress tracking and reporting

Phase 3: RA/QA Specialization (Current)

Eight domain expert agents, nine domain skills with progressive disclosure, Notion DB integration and traceability, Wave Parallelism execution model

Future Phases

Multi-language support (English, Korean, Japanese), advanced analytics and reporting, integration with external QMS systems, mobile interface for field audits
