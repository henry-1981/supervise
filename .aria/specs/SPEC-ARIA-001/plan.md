# SPEC-ARIA-001: Implementation Plan

## TAG BLOCK

```yaml
SPEC_ID: SPEC-ARIA-001
TITLE: ARIA Phase 1 - Core Framework Implementation
VERSION: 1.0.0
STATUS: Planned
PRIORITY: High
DOMAIN: aria-core
PHASE: 1
CREATED: 2026-02-09
AUTHOR: ARIA Architect
ASSIGNED: orchestrator
```

---

## Implementation Strategy

### Approach Overview

Phase 1 implements the **Core Framework Scaffold** for ARIA. This is the foundation upon which all subsequent phases will build.

**Key Design Decisions:**

1. **Minimal Viable Plugin**: Focus on plugin structure recognition and basic command execution
2. **Orchestrator-First**: Implement only the orchestrator agent; defer business/domain agents to Phase 2/3
3. **MCP Integration**: Configure Context7 and Sequential Thinking MCP but defer complex usage to later phases
4. **Configuration-Driven**: Use `aria.yaml` for all tunable parameters to enable easy iteration

**Development Methodology:**

- **DDD (Domain-Driven Development)**: ANALYZE-PRESERVE-IMPROVE cycle
- **Test Coverage Target**: 85% for new code
- **Quality Framework**: VALID (Verified, Accurate, Linked, Inspectable, Deliverable)

---

## Milestones

### Milestone 1: Plugin Structure (Priority: Primary)

**Objective**: Establish basic plugin structure recognized by Claude Code

**Tasks**:
1. Create `.claude-plugin/` directory with `plugin.json` manifest
2. Create `.claude/agents/aria/` directory structure
3. Create `.claude/commands/` directory structure
4. Create `.claude/skills/aria-core/` directory structure
5. Create `aria.yaml` configuration file
6. Create `.mcp.json` with MCP server configurations

**Success Criteria**:
- [ ] Plugin directory structure matches Claude Code specification
- [ ] `plugin.json` contains all required fields
- [ ] `.mcp.json` includes Context7 and Sequential Thinking MCP
- [ ] Directories are properly nested with correct naming

**Estimated Complexity**: Low

**Dependencies**: None

---

### Milestone 2: Orchestrator Agent (Priority: Primary)

**Objective**: Implement the central orchestrator agent with intent classification

**Tasks**:
1. Create `.claude/agents/aria/orchestrator.md` with YAML frontmatter
2. Define agent core responsibilities (intent analysis, workflow routing, agent delegation, user interaction, error handling)
3. Implement intent classification logic (document drafting, analysis, review, search)
4. Define user interaction protocol (Korean responses, English internal communication)
5. Define error handling protocol (plain language, next-step guidance)
6. Create agent skill references (aria-core, moai-foundation-core)

**Success Criteria**:
- [ ] Agent definition follows Claude Code agent format
- [ ] Intent classification logic is documented
- [ ] User interaction protocol specifies Korean responses
- [ ] Error handling specifies plain language messages
- [ ] Agent references correct skills

**Estimated Complexity**: Medium

**Dependencies**: Milestone 1

---

### Milestone 3: /aria Command (Priority: Primary)

**Objective**: Implement the main /aria command interface

**Tasks**:
1. Create `.claude/commands/aria.md` with YAML frontmatter
2. Define command parameters (query: optional string)
3. Document command usage and examples
4. Define command behavior flow (intent analysis → scope definition → brief → execute → deliver)
5. Implement help command behavior (display introduction, use cases, reference)
6. Create command behavior flow diagram

**Success Criteria**:
- [ ] Command definition follows Claude Code command format
- [ ] Command parameters are properly documented
- [ ] Usage examples cover main scenarios
- [ ] Behavior flow is clearly documented
- [ ] Help command provides useful information

**Estimated Complexity**: Medium

**Dependencies**: Milestone 1, Milestone 2

---

### Milestone 4: Configuration System (Priority: Primary)

**Objective**: Implement aria.yaml configuration file

**Tasks**:
1. Create `aria.yaml` with complete structure
2. Define language settings (conversation_language, agent_prompt_language, documentation_language)
3. Define workflow settings (brief/execute/deliver token budgets, approval requirements)
4. Define quality framework settings (VALID framework configuration)
5. Define agent settings (orchestrator model and timeout)
6. Define integration settings (MCP server configurations)
7. Define error handling settings (max_retries, retry_delay, plain_language)
8. Define development settings (debug mode, log level, feature flags)

**Success Criteria**:
- [ ] Configuration file is syntactically correct YAML
- [ ] All settings have default values
- [ ] Settings are properly documented with comments
- [ ] Configuration loading priority is documented
- [ ] Feature flags control Phase 1 scope

**Estimated Complexity**: Low

**Dependencies**: Milestone 1

---

### Milestone 5: Workflow Skeleton (Priority: Primary)

**Objective**: Implement Brief-Execute-Deliver workflow structure

**Tasks**:
1. Create aria-core skill with SKILL.md
2. Implement Brief phase skeleton (intent analysis, scope definition, regulatory mapping, strategy development, approval checkpoint)
3. Implement Execute phase skeleton (task decomposition, agent dispatch, document preparation, quality gates)
4. Implement Deliver phase skeleton (quality review, format conversion, packaging, distribution)
5. Create phase transition diagrams
6. Document token budget allocation (60%-30%-10%)
7. Define approval checkpoint behavior

**Success Criteria**:
- [ ] Workflow phases are clearly defined
- [ ] Token budget allocation is documented
- [ ] Approval checkpoint is specified
- [ ] Phase transitions are documented
- [ ] Skeleton is extensible for future phases

**Estimated Complexity**: Medium

**Dependencies**: Milestone 2, Milestone 4

---

### Milestone 6: Error Handling (Priority: Primary)

**Objective**: Implement plain language error handling with regulatory defect detection

**Tasks**:
1. Define error classification (connection errors, missing information, regulatory ambiguity, token limit, agent failure)
2. Define regulatory defect categories (missing cybersecurity, incomplete risk analysis, insufficient validation, inadequate traceability)
3. Create error message template (problem, cause, next steps)
4. Create regulatory alert template (defect description, regulatory impact, remediation options)
5. Document error recovery strategies
6. Implement retry logic (max 3 retries for system errors)
7. Create example error messages in Korean
8. Create example regulatory defect alerts in Korean
9. Document next-step guidance patterns

**Success Criteria**:
- [ ] All error types are classified
- [ ] Regulatory defect categories are defined
- [ ] Error messages use plain Korean language
- [ ] Regulatory alerts provide clear remediation options
- [ ] Recovery strategies are documented
- [ ] Retry logic is specified
- [ ] Error messages provide next-step guidance
- [ ] Regulatory alerts cite applicable regulations

**Examples - Regulatory Defect Alerts**:

*Example 1: Missing Cybersecurity*
```
[규제 결함 감지] 제품에 사이버보안 로직이 구현되지 않은 것으로 보입니다.

영향 분석:
- FDA 21 CFR 820.30(g): Design Input 불충분
- EU MDR Annex I Chapter II: 사이버 보안 요구사항 미충족

다음 단계:
  1. 전문가 상담 (cybersecurity expert)
  2. 보완 계획 수립 (remediation planning)
  3. 재검토 예약 (schedule re-review)
```

*Example 2: Incomplete Risk Analysis*
```
[규제 결함 감지] 위험 분석이 불완전한 것으로 보입니다.

영향 분석:
- ISO 14971 Clause 7: Risk Analysis 요구사항
- FDA 21 CFR 820.30(d): Design Verification 불충분

다음 단계:
  1. risk expert 상담
  2. 추가 FMEA 수행
  3. 위험 등록부 업데이트
```

*Example 3: Insufficient Traceability*
```
[규제 결함 감지] 추적성 연결이 누락된 것으로 보입니다.

영향 분석:
- 21 CFR 820.30(d): Design Output과 Input 간 추적성
- ISO 13485 Clause 7.3.7: 추적성 문서화

다음 단계:
  1. Traceability Matrix 검토
  2. 누락된 연결 식별
  3. 추적성 보완 작업
```

**Estimated Complexity**: Low

**Dependencies**: Milestone 2, Milestone 4

---

### Milestone 7: MCP Integration (Priority: Secondary)

**Objective**: Configure and document MCP server integration

**Tasks**:
1. Create `.mcp.json` with Context7 and Sequential Thinking MCP
2. Document Context7 MCP usage pattern (regulatory documentation lookup)
3. Document Sequential Thinking MCP usage pattern (complex analysis)
4. Create usage examples for Brief phase
5. Document MCP timeout configurations
6. Specify MCP error handling

**Success Criteria**:
- [ ] `.mcp.json` includes both MCP servers
- [ ] Usage patterns are documented
- [ ] Examples show Brief phase integration
- [ ] Timeout configurations are specified
- [ ] Error handling is documented

**Estimated Complexity**: Medium

**Dependencies**: Milestone 1, Milestone 5

---

### Milestone 8: Documentation (Priority: Primary)

**Objective**: Create comprehensive documentation

**Tasks**:
1. Update README.md with ARIA overview and Phase 1 capabilities
2. Update CLAUDE.md with execution directives
3. Update CHANGELOG.md with Phase 1 changes
4. Create inline documentation in all code/config files
5. Document installation instructions
6. Document usage examples
7. Create troubleshooting guide

**Success Criteria**:
- [ ] README.md describes ARIA and Phase 1 scope
- [ ] CLAUDE.md contains execution directives
- [ ] CHANGELOG.md records Phase 1 changes
- [ ] All files have inline documentation
- [ ] Installation instructions are clear
- [ ] Usage examples are practical

**Estimated Complexity**: Low

**Dependencies**: Milestone 1-7

---

### Milestone 9: Testing (Priority: Primary)

**Objective**: Validate Phase 1 implementation

**Tasks**:
1. Test plugin recognition by Claude Code
2. Test `/aria help` command
3. Test intent classification with sample queries
4. Test user interaction with AskUserQuestion
5. Test error messages (plain language, next-step guidance)
6. Test MCP server connectivity
7. Test configuration loading
8. Validate all Korean language output
9. Validate citation format for regulatory claims
10. Validate max 4 options in questions

**Success Criteria**:
- [ ] Plugin loads without errors
- [ ] `/aria help` displays correct information
- [ ] Intent classification works for all categories
- [ ] User interaction respects max 4 options
- [ ] Error messages use plain Korean
- [ ] MCP servers are accessible
- [ ] Configuration loads correctly
- [ ] All output is Korean (user-facing)
- [ ] Citations follow standard format
- [ ] Questions respect option limit

**Estimated Complexity**: Medium

**Dependencies**: Milestone 1-8

---

### Milestone 10: Validation (Priority: Primary)

**Objective**: VALID quality framework validation

**Tasks**:
1. **V**erified: Verify all regulatory claims cite sources
2. **A**ccurate: Validate configuration values and error recovery
3. **L**inked: Verify requirement-to-specification traceability
4. **I**nspectable: Validate audit trail capability
5. **D**eliverable: Verify plugin structure compliance

**Success Criteria**:
- [ ] All regulatory claims have citations
- [ ] Configuration values are validated
- [ ] Traceability matrix is complete
- [ ] Audit trail is documented
- [ ] Plugin structure complies with specification

**Estimated Complexity**: Low

**Dependencies**: Milestone 9

---

## Technical Approach

### Architecture Pattern

**Agent-Based Orchestration**:

Phase 1 implements a **single-agent orchestrator** pattern. Future phases will expand to multi-agent delegation.

```
Phase 1:
  User → /aria → Orchestrator → (handles all tasks)

Phase 2:
  User → /aria → Orchestrator → {manager-docs, manager-quality, manager-project}

Phase 3:
  User → /aria → Orchestrator → {business agents} → {RA/QA domain agents}
```

**Brief-Execute-Deliver Workflow**:

```
Brief (60%): Regulatory strategy analysis
  ↓ Approval Checkpoint
Execute (30%): Document preparation
  ↓
Deliver (10%): Quality-validated output
```

### Technology Stack

**Core Technologies**:
- **Platform**: Claude Code Plugin System
- **Language**: YAML (configs), Markdown (docs/agents/commands/skills)
- **MCP**: Context7, Sequential Thinking
- **Configuration**: aria.yaml (YAML)
- **Documentation**: Markdown

**Why This Stack**:
- **Claude Code Native**: No build tools, no dependencies
- **YAML/Markdown**: Human-readable, version-control friendly
- **MCP**: Standard protocol for external service integration

### File Organization

**Directory Structure**:

```
supervise/
├── .claude-plugin/
│   ├── plugin.json                 # Plugin manifest
│   └── capabilities.yaml           # Capability declaration
├── .claude/
│   ├── agents/
│   │   └── aria/
│   │       └── orchestrator.md     # Orchestrator agent
│   ├── commands/
│   │   └── aria.md                 # /aria command
│   └── skills/
│       └── aria-core/
│           ├── SKILL.md            # Core skill
│           └── modules/
│               ├── workflow.md     # Brief-Execute-Deliver
│               └── quality.md      # VALID framework
├── .mcp.json                       # MCP configuration
├── aria.yaml                       # ARIA configuration
├── CLAUDE.md                       # Execution directives
├── README.md                       # User documentation
└── CHANGELOG.md                    # Version history
```

**Rationale**:
- `.claude-plugin/`: Claude Code plugin standard
- `.claude/`: Claude Code agents, commands, skills
- Separate aria-core skill: Progressive disclosure
- Configuration files in root: Discoverability

### Implementation Phases

**Phase 1A: Structure (Milestone 1)**
- Create directory structure
- Create plugin.json manifest
- Create aria.yaml configuration
- Create .mcp.json

**Phase 1B: Agents and Commands (Milestone 2-3)**
- Implement orchestrator agent
- Implement /aria command
- Document intent classification
- Document user interaction protocol

**Phase 1C: Workflow and Error Handling (Milestone 4-6)**
- Implement workflow skeleton
- Implement error handling
- Document Brief-Execute-Deliver
- Document error messages

**Phase 1D: Integration and Documentation (Milestone 7-10)**
- Configure MCP servers
- Create documentation
- Test implementation
- Validate with VALID framework

---

## Risk Management

### Technical Risks

**Risk 1: Claude Code Plugin API Changes**

- **Probability**: Medium
- **Impact**: High (breaks compatibility)
- **Mitigation**:
  - Follow official documentation closely
  - Use stable API features only
  - Version pin in plugin.json
  - Monitor Claude Code release notes

**Risk 2: MCP Server Unavailability**

- **Probability**: Low
- **Impact**: Medium (reduced functionality)
- **Mitigation**:
  - Implement retry logic (max 3)
  - Graceful degradation (continue without MCP)
  - Cached responses where possible
  - Clear error messages with guidance

**Risk 3: Token Budget Exceeded**

- **Probability**: Medium
- **Impact**: Medium (incomplete responses)
- **Mitigation**:
  - Progressive disclosure in skills
  - Aggressive /clear strategy
  - Phase token budget monitoring
  - User continuation prompts

### Domain Risks

**Risk 4: Regulatory Information Outdated**

- **Probability**: Low
- **Impact**: High (incorrect guidance)
- **Mitigation**:
  - Context7 MCP for current docs
  - Date validation on citations
  - User verification for critical decisions
  - Clear "best effort" communication

**Risk 5: User Misinterpretation**

- **Probability**: Medium
- **Impact**: Medium (incorrect usage)
- **Mitigation**:
  - Plain language in all communications
  - Clear examples in documentation
  - Approval checkpoints for key decisions
  - Interactive clarification questions

### User Experience Risks

**Risk 6: Language Confusion (Ko/En)**

- **Probability**: Low
- **Impact**: Medium (user confusion)
- **Mitigation**:
  - Strict separation: user=Ko, agent=En
  - Configuration validation
  - Test all user-facing output
  - Document language policy

**Risk 7: Too Many Questions**

- **Probability**: Medium
- **Impact**: Low (user frustration)
- **Mitigation**:
  - Max 5 questions in Brief
  - Max 4 options per question
  - Smart question ordering (broad → specific)
  - Allow user to skip optional questions

---

## Quality Assurance

### Testing Strategy

**Unit Testing** (Not applicable in Phase 1 - no executable code)

**Integration Testing**:
- Plugin recognition test
- Command execution test
- MCP connectivity test
- Configuration loading test

**User Acceptance Testing**:
- Korean language validation
- Plain language error message validation
- AskUserQuestion interaction validation
- Regulatory citation format validation

**Quality Gate Validation**:
- VALID framework verification
- Plugin structure compliance
- Documentation completeness

### VALID Framework Verification

**V**erified:
- All regulatory claims cite sources (when applicable in Brief phase)
- Context7 MCP provides current documentation

**A**ccurate:
- Configuration values validated
- Error recovery mechanisms tested

**L**inked:
- Requirement-to-specification traceability matrix maintained
- Brief-Execute-Deliver phase linkage documented

**I**nspectable:
- Decision rationale documentation capability
- Audit trail documentation

**D**eliverable:
- Plugin structure compliance validated
- Output format validation

---

## Success Metrics

### Functional Metrics

- Plugin recognition: 100% (Claude Code loads plugin)
- Command execution: 100% (/aria help works)
- Intent classification: ≥80% (correct classification)
- MCP connectivity: 100% (both servers accessible)
- Configuration loading: 100% (aria.yaml loads correctly)

### Quality Metrics

- Korean language coverage: 100% (all user-facing output)
- Plain language error messages: 100% (no technical jargon)
- Citation format compliance: 100% (standard, section, version)
- Question option limit: 100% (max 4 options)

### User Experience Metrics

- Help command clarity: Subjective assessment
- Error message clarity: Subjective assessment
- Documentation completeness: All sections present

---

## Next Steps

### Immediate Actions

1. **Create directory structure**: Execute Milestone 1 tasks
2. **Implement orchestrator agent**: Execute Milestone 2 tasks
3. **Implement /aria command**: Execute Milestone 3 tasks
4. **Create configuration files**: Execute Milestone 4 tasks

### Validation Actions

1. **Test plugin recognition**: Verify Claude Code loads plugin
2. **Test command execution**: Verify `/aria help` works
3. **Test user interaction**: Verify AskUserQuestion works
4. **Test error handling**: Verify plain language errors

### Documentation Actions

1. **Update README.md**: Describe ARIA and Phase 1
2. **Update CLAUDE.md**: Add execution directives
3. **Update CHANGELOG.md**: Record Phase 1 changes
4. **Create examples**: Provide usage examples

---

## Reference

### Related Documents

- [spec.md](./spec.md): Complete specification with EARS requirements
- [acceptance.md](./acceptance.md): Detailed acceptance criteria with Gherkin scenarios

### External References

- [Claude Code Plugin Documentation](https://claude.ai/claude-code/docs)
- [Context7 MCP Documentation](https://context7.io)
- [Sequential Thinking MCP Documentation](https://modelcontextprotocol.io)

### ARIA Architecture

- [ARCHITECTURE-REDESIGN.md](../../docs/specs/ARCHITECTURE-REDESIGN.md): Complete system architecture
- [CONTEXT.md](../../docs/CONTEXT.md): Project background and design decisions
