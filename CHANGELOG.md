# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-02-09

### Added
- Output Styles feature with three built-in styles (MoAI, R2D2, Yoda)
- Multi-format output conversion scripts (Markdown, HTML, PDF, Word)
- WCAG 2.1 AA accessibility validation for HTML outputs
- Output configuration system (`.moai/config/sections/output.yaml`)
- Enhanced agent coordination with output style selection
- Improved documentation with language-aware responses

### Features
- Three output personality styles for different use cases:
  - MoAI: Strategic orchestrator with bilingual support (Korean/English)
  - R2D2: Technical, concise communication style
  - Yoda: Wisdom-focused, thoughtful responses
- Format conversion pipeline with company branding support
- Accessibility compliance for regulatory submissions
- Flexible output configuration via YAML

### Changed
- Enhanced supervisor agent to support output style selection
- Improved aggregator agent with style-aware response formatting
- Updated documentation for new output features

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
