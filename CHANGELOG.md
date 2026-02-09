# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2026-02-09

### Major Release: ARIA Phase 3 - RA/QA Specialization

Complete redesign and specialization for medical device Regulatory Affairs and Quality Assurance.

### Added: Expert Agents (8 total)

- **expert-regulatory**: FDA/MDR regulatory strategy specialist with Opus model
  - aria-domain-raqa skill for RA/QA domain workflow
  - aria-knowledge-fda skill for FDA regulations
  - aria-knowledge-eumdr skill for EU MDR regulations
  - Context7 MCP integration for latest regulatory updates

- **expert-standards**: ISO/IEC standards compliance specialist with Opus model
  - aria-knowledge-standards skill for ISO/IEC standards
  - ISO 13485 QMS, ISO 14971 risk management
  - IEC 62304 software lifecycle, IEC 62366 usability
  - Automated gap analysis with section-level precision

- **expert-risk**: ISO 14971 risk management specialist with Opus model
  - aria-risk-management skill for risk processes
  - FMEA analysis framework with scoring
  - Risk-benefit analysis and ALARP principle
  - Notion Risk Register integration

- **expert-design-control**: Design control specialist with Sonnet model
  - aria-design-control skill for design processes
  - Design input/output management
  - Design verification/validation protocols
  - DHF/DMR/DHR traceability matrix

- **expert-capa**: CAPA lifecycle specialist with Sonnet model
  - aria-capa-process skill for CAPA workflows
  - Root cause analysis guidance
  - Implementation verification and effectiveness validation
  - Notion CAPA Tracker integration

- **expert-clinical**: Clinical evaluation specialist with Opus model
  - aria-domain-raqa skill for clinical processes
  - Clinical investigation planning
  - CER (Clinical Evaluation Report) preparation
  - Post-market clinical follow-up (PMCF)

- **expert-submission**: Regulatory submission specialist with Sonnet model
  - aria-submission-templates skill for submission formats
  - FDA 510(k) eCopy templates
  - EU MDR Technical File structure
  - MFDS submission requirements

- **expert-audit**: Audit preparation specialist with Sonnet model
  - aria-domain-raqa skill for audit processes
  - Internal audit protocol generation
  - External audit (NB, FDA) support
  - Mock audit simulations

### Added: Domain Skills (9 total)

- **aria-domain-raqa**: RA/QA domain knowledge with 3 modules
  - regulatory-workflow.md: Regulatory process workflows
  - clinical-evaluation.md: Clinical assessment procedures
  - audit-preparation.md: Audit protocol generation

- **aria-knowledge-fda**: FDA regulations with 3 modules
  - 21-cfr-820.md: Quality System Regulation
  - 510k-process.md: 510(k) submission pathway
  - pma-process.md: PMA submission pathway

- **aria-knowledge-eumdr**: EU MDR regulations with 5 modules
  - classification.md: Device classification rules
  - clinical-evaluation.md: CER requirements
  - technical-documentation.md: Technical file structure
  - post-market-surveillance.md: PMS requirements
  - vigilance.md: Vigilance reporting

- **aria-knowledge-standards**: ISO/IEC standards with 5 modules
  - iso-13485.md: QMS standard requirements
  - iso-14971.md: Risk management standard
  - iec-62304.md: Software lifecycle standard
  - iec-62366.md: Usability engineering standard
  - iec-60601.md: Medical device electrical safety

- **aria-knowledge-mfds**: MFDS regulations with 1 module
  - mfds-regulations.md: Korean MFDS requirements

- **aria-risk-management**: Risk management with 3 modules
  - fMEA-analysis.md: Failure Modes and Effects Analysis
  - risk-benefit.md: Risk-benefit analysis framework
  - alarp-principle.md: As Low As Reasonably Practicable

- **aria-design-control**: Design control with 4 modules
  - design-inputs.md: Design input requirements
  - design-outputs.md: Design output verification
  - design-validation.md: Design validation protocols
  - design-transfer.md: Design transfer process

- **aria-capa-process**: CAPA management with 1 module
  - root-cause-analysis.md: RCA methods and CAPA verification

- **aria-submission-templates**: Submission templates with 1 module
  - submission-formats.md: FDA 510(k), PMA, EU MDR templates

### Added: Progressive Disclosure System

- Level 1 (Metadata): Approximately 100 tokens per skill, always loaded
- Level 2 (Body): Approximately 5000 tokens, loaded when triggered
- Level 3 (Modules): 22 knowledge modules loaded on-demand

### Added: Quality Frameworks

- **VALID Framework**: Verified, Accurate, Linked, Inspectable, Deliverable
- **TRUST 5 Framework**: Tested, Readable, Unified, Secured, Trackable

### Added: MCP Integration

- Context7: Real-time regulatory standard updates
- Notion API: CAPA Tracker, Risk Register, Document Registry
- Sequential Thinking: Complex regulatory strategy analysis

### Added: Notion Database Schemas

- CAPA Tracker: Issue lifecycle management
- Risk Register: ISO 14971 risk management
- Document Registry: DHF/DMR/DHR traceability

### Added: Project Documentation

- .moai/project/product.md: Product overview and value proposition
- .moai/project/structure.md: Codebase architecture
- .moai/project/tech.md: Technical stack details

### Changed

- Renamed plugin from "Cowork Supervisor" to "ARIA"
- Refactored README.md for medical device regulatory focus
- Updated CHANGELOG.md with comprehensive version history
- Enhanced project structure with ARIA-specific directories

### Performance Improvements

- Token optimization through progressive disclosure
- Strategic model assignment (Opus vs Sonnet)
- Parallel agent execution where applicable
- Caching for frequently accessed regulatory content

### Integration Testing

- E2E scenario tests for 510(k) submission workflow
- Risk management integration validation
- CE Marking technical file preparation
- CAPA lifecycle management testing

### Documentation

- Comprehensive README with regulatory use cases
- API documentation for agent-skill interactions
- Integration test report with validation results
- Technical stack documentation

## [1.0.0] - 2026-02-05

### Added
- Initial release of Cowork Supervisor plugin
- Intent Clarifier agent for understanding user requests
- Capability Discoverer agent for plugin detection
- Supervisor Planner agent for execution planning
- Orchestra agent for multi-plugin coordination
- Aggregator agent for result synthesis
- `/supervise` command for easy invocation
- Comprehensive README with installation and usage docs

### Features
- Multi-plugin orchestration with parallel/sequential execution
- Automatic plugin capability discovery
- User approval checkpoints for execution plans
- Error handling with fallback strategies
- Cross-domain result aggregation with conflict resolution
- Source attribution in final responses
