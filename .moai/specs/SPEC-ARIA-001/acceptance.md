# SPEC-ARIA-001: Acceptance Criteria

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

## Overview

This document defines detailed acceptance criteria for SPEC-ARIA-001 using **Gherkin (Given-When-Then)** format for scenario-based testing.

### Test Organization

- **Functional Requirements**: Plugin functionality, command execution, agent behavior
- **Quality Requirements**: VALID framework compliance, language requirements
- **Integration Requirements**: MCP integration, configuration loading
- **User Experience Requirements**: Error handling, user interaction

---

## Functional Requirements Acceptance

### FR1: Plugin Recognition by Claude Code

**Story**: As a Claude Code user, I want ARIA plugin to be recognized so that I can use `/aria` command.

**Acceptance Criteria**:

#### Scenario 1.1: Plugin loads without errors
```gherkin
Given Claude Code is running
And ARIA plugin is installed in ~/.claude/plugins/local/aria
And plugin.json contains valid manifest
When I start Claude Code
Then plugin should be recognized
And no error messages should be displayed
And /aria command should be available
```

#### Scenario 1.2: Plugin directory structure is valid
```gherkin
Given ARIA plugin is installed
When I examine .claude-plugin/ directory
Then plugin.json should exist
And capabilities.yaml should exist
And .claude/agents/aria/ directory should exist
And .claude/commands/ directory should exist
And .claude/skills/aria-core/ directory should exist
```

**Definition of Done**:
- [ ] Plugin loads in Claude Code without errors
- [ ] `/aria` command is listed in available commands
- [ ] Directory structure matches specification
- [ ] plugin.json contains all required fields

---

### FR2: /aria help Command

**Story**: As a new ARIA user, I want to see help information so that I understand how to use ARIA.

**Acceptance Criteria**:

#### Scenario 2.1: Help command displays usage information
```gherkin
Given ARIA plugin is loaded
When I enter "/aria help"
Then ARIA introduction should be displayed
And common use cases should be listed
And command reference should be shown
And all text should be in Korean
```

#### Scenario 2.2: Help command content is complete
```gherkin
Given I execute "/aria help"
When help information is displayed
Then it should include:
  - ARIA description and purpose
  - Target users (RA/QA practitioners)
  - At least 3 usage examples
  - Reference to /aria command syntax
```

**Definition of Done**:
- [ ] `/aria help` executes without errors
- [ ] Help content is in Korean
- [ ] Help content includes description, use cases, examples
- [ ] Help content is clear and actionable

---

### FR3: Intent Classification

**Story**: As ARIA orchestrator, I want to classify user intent so that I can route requests appropriately.

**Acceptance Criteria**:

#### Scenario 3.1: Classify document drafting intent
```gherkin
Given ARIA orchestrator is active
When user enters "510(k) 제출 준비 도와주세요"
Then intent should be classified as "document drafting"
And confidence score should be calculated
And classification should use keyword matching
```

#### Scenario 3.2: Classify analysis intent
```gherkin
Given ARIA orchestrator is active
When user enters "ISO 13485 준수 상태 분석"
Then intent should be classified as "analysis"
And classification should be logged
```

#### Scenario 3.3: Classify review intent
```gherkin
Given ARIA orchestrator is active
When user enters "디자인 히스토리 파일 검토"
Then intent should be classified as "review"
```

#### Scenario 3.4: Classify search intent
```gherkin
Given ARIA orchestrator is active
When user enters "FDA 가이던스 검색"
Then intent should be classified as "search"
```

#### Scenario 3.5: Complex query uses Sequential Thinking MCP
```gherkin
Given ARIA orchestrator is active
When user enters "Class II 기기를 US와 EU 시장에 동시 진출하는 전략"
Then Sequential Thinking MCP should be invoked
And analysis should be step-by-step
And strategy should be synthesized
```

**Definition of Done**:
- [ ] Intent classification works for all 4 categories
- [ ] Sequential Thinking MCP is used for complex queries
- [ ] Classification accuracy ≥80% on test queries
- [ ] Confidence scores are calculated

---

### FR4: User Interaction with AskUserQuestion

**Story**: As ARIA orchestrator, I want to clarify user scope so that I can provide accurate regulatory guidance.

**Acceptance Criteria**:

#### Scenario 4.1: Ask device classification
```gherkin
Given user wants to prepare 510(k) submission
And intent is classified as "document drafting"
When scope definition phase starts
Then user should be asked: "장비의 등급(Class)을 선택해주세요"
And exactly 4 options should be presented:
  - Class I
  - Class II
  - Class III
  - 잘 모르겠습니다
```

#### Scenario 4.2: Ask predicate device knowledge
```gherkin
Given user selected device classification
When predicate device information is needed
Then user should be asked: "Predicate device를 알고 계신가요?"
And exactly 4 options should be presented:
  - 예, 지정합니다
  - 아니요, 검색이 필요합니다
  - 확실하지 않습니다
  - 해당 사항 없음
```

#### Scenario 4.3: Questions are in Korean
```gherkin
Given any AskUserQuestion interaction
When question is presented
Then question text should be in Korean
And all options should be in Korean
And no English should be visible to user
```

#### Scenario 4.4: Maximum 5 questions in Brief phase
```gherkin
Given user is in Brief phase
When scope definition questions are asked
Then maximum 5 questions should be asked
And questions should be ordered from broad to specific
And user should be able to skip optional questions
```

**Definition of Done**:
- [ ] AskUserQuestion presents exactly 4 options
- [ ] All questions are in Korean
- [ ] Maximum 5 questions in Brief phase
- [ ] Questions are ordered logically

---

### FR5: Error Messages in Plain Korean

**Story**: As a non-developer user, I want to understand what went wrong so that I can fix the problem.

**Acceptance Criteria**:

#### Scenario 5.1: Connection error message
```gherkin
Given MCP server is unreachable
When connection error occurs
Then error message should be:
  "서버 연결이 원활하지 않습니다. 30초 후 다시 시도합니다.
   문제가 지속되면 네트워크 연결을 확인해 주세요."
And message should not contain technical terms like "ECONNREFUSED"
And message should suggest next steps
```

#### Scenario 5.2: Missing information error message
```gherkin
Given user query lacks required information
When error occurs
Then error message should ask follow-up question
And message should present 4 options for clarification
And message should be helpful and encouraging
```

#### Scenario 5.3: Regulatory ambiguity error message
```gherkin
Given regulatory requirements are unclear
When ambiguity is detected
Then error message should be:
  "규제 요구사항이 명확하지 않습니다. 전문가 검토가 권장됩니다.
   아래 옵션 중 하나를 선택해주세요:"
And options should be presented
And user should not be left without guidance
```

#### Scenario 5.4: Token limit error message
```gherkin
Given context window is approaching limit
When token limit warning is triggered
Then error message should be:
  "작업이 복잡하여 단계별로 진행하겠습니다. 계속하시겠습니까?"
And user should be able to choose continuation strategy
```

**Definition of Done**:
- [ ] All error messages use plain Korean
- [ ] No technical jargon in user-facing errors
- [ ] All error messages provide next-step guidance
- [ ] Error messages are helpful and actionable

---

### FR6: MCP Integration Configuration

**Story**: As ARIA orchestrator, I want to use MCP servers so that I can access current regulatory information.

**Acceptance Criteria**:

#### Scenario 6.1: Context7 MCP is configured
```gherkin
Given .mcp.json exists
When I examine configuration
Then Context7 MCP should be included
And command should be "npx"
And args should include "-y" and "@context7/mcp"
And description should mention "regulatory documentation"
```

#### Scenario 6.2: Sequential Thinking MCP is configured
```gherkin
Given .mcp.json exists
When I examine configuration
Then Sequential Thinking MCP should be included
And command should be "npx"
And args should include "-y" and "@modelcontextprotocol/server-sequential-thinking"
And description should mention "complex analysis"
```

#### Scenario 6.3: MCP servers are accessible
```gherkin
Given ARIA plugin is loaded
When I test MCP connectivity
Then Context7 MCP should respond
And Sequential Thinking MCP should respond
And timeout should be within configured limits
```

**Definition of Done**:
- [ ] .mcp.json includes both MCP servers
- [ ] MCP servers are accessible
- [ ] Timeout configurations are appropriate
- [ ] MCP usage patterns are documented

---

## Quality Requirements Acceptance

### QR1: All User-Facing Output is Korean

**Story**: As a Korean-speaking user, I want all responses in Korean so that I can use ARIA comfortably.

**Acceptance Criteria**:

#### Scenario 1.1: Command responses are in Korean
```gherkin
Given I execute any /aria command
When response is displayed
Then all user-facing text should be in Korean
And no English should be visible except:
  - Proper nouns (FDA, ISO, etc.)
  - Regulatory citations
  - Technical terms without Korean equivalent
```

#### Scenario 1.2: Error messages are in Korean
```gherkin
Given an error occurs
When error message is displayed
Then error message should be in Korean
And explanation should be in Korean
And next-step guidance should be in Korean
```

#### Scenario 1.3: AskUserQuestion options are in Korean
```gherkin
Given user is asked a question
When options are presented
Then question should be in Korean
And all options should be in Korean
```

**Definition of Done**:
- [ ] 100% of user-facing output is Korean
- [ ] Only proper nouns and citations use English
- [ ] No internal agent communication leaks to user

---

### QR2: Error Messages Use Plain Language

**Story**: As a non-developer user, I want error messages I can understand without technical knowledge.

**Acceptance Criteria**:

#### Scenario 2.1: No technical jargon in errors
```gherkin
Given any error occurs
When error message is generated
Then message should not contain:
  - Exception types (ECONNREFUSED, ValueError, etc.)
  - Stack traces
  - HTTP status codes
  - Technical protocol details
And message should use plain language equivalents
```

#### Scenario 2.2: Error context is provided
```gherkin
Given an error occurs
When error message is displayed
Then it should include:
  - What happened (in plain language)
  - Why it happened (simplified explanation)
  - What to do next (actionable steps)
And message should be encouraging, not blaming
```

#### Scenario 2.3: Error recovery options are provided
```gherkin
Given an error occurs
When error message is displayed
Then at least 2 recovery options should be suggested
And options should be specific and actionable
And user should be able to choose next action
```

**Definition of Done**:
- [ ] Zero technical jargon in error messages
- [ ] All errors provide context and recovery options
- [ ] Error messages are tested with non-developer users

---

### QR3: Regulatory Claims Cite Sources

**Story**: As a RA/QA professional, I want to verify regulatory claims so that I can trust ARIA's guidance.

**Acceptance Criteria**:

#### Scenario 3.1: FDA regulations are cited correctly
```gherkin
Given ARIA mentions FDA requirement
When regulatory claim is made
Then citation should follow format: "FDA 21 CFR Part 820.30(i)"
And citation should include:
  - Standard name (FDA)
  - Section number (21 CFR Part 820.30)
  - Subsection if applicable (i)
And date/version should be included if applicable
```

#### Scenario 3.2: ISO standards are cited correctly
```gherkin
Given ARIA mentions ISO standard
When regulatory claim is made
Then citation should follow format: "ISO 13485:2016 Clause 4.2.1"
And citation should include:
  - Standard name (ISO)
  - Standard number (13485)
  - Version year (2016)
  - Specific clause (4.2.1)
```

#### Scenario 3.3: EU MDR is cited correctly
```gherkin
Given ARIA mentions EU MDR requirement
When regulatory claim is made
Then citation should follow format: "EU MDR 2017/745 Article 10(1)"
And citation should include:
  - Regulation name (EU MDR)
  - Regulation number (2017/745)
  - Article number (10)
  - Paragraph if applicable (1)
```

#### Scenario 3.4: No unsupported claims
```gherkin
Given ARIA provides regulatory guidance
When claim is made
Then source citation must be provided
Or uncertainty must be explicitly stated:
  "출처를 확인할 수 없습니다. 전문가 검토가 권장됩니다."
```

**Definition of Done**:
- [ ] 100% of regulatory claims cite sources
- [ ] Citation format is consistent
- [ ] Uncertainty is explicitly stated when source is unknown

---

### QR4: Questions Present Maximum 4 Options

**Story**: As a user, I want clear, focused questions so that I can make decisions easily.

**Acceptance Criteria**:

#### Scenario 4.1: Device classification question has 4 options
```gherkin
Given user is asked about device classification
When AskUserQuestion is invoked
Then exactly 4 options should be presented
And options should be mutually exclusive
And options should cover common cases
And "other/unknown" option should be included
```

#### Scenario 4.2: Predicate device question has 4 options
```gherkin
Given user is asked about predicate device
When AskUserQuestion is invoked
Then exactly 4 options should be presented
And options should be clear and distinct
```

#### Scenario 4.3: Complex questions are split
```gherkin
Given a decision requires more than 4 options
When question is designed
Then it should be split into multiple questions
And each question should have ≤4 options
And questions should be ordered logically
```

**Definition of Done**:
- [ ] All AskUserQuestion calls have ≤4 options
- [ ] Options are mutually exclusive
- [ ] Complex decisions are split into multiple questions

---

## Integration Requirements Acceptance

### IR1: Context7 MCP Accessibility

**Story**: As ARIA orchestrator, I want to access Context7 MCP so that I can retrieve current regulatory documentation.

**Acceptance Criteria**:

#### Scenario 1.1: Context7 MCP responds to queries
```gherkin
Given Context7 MCP is configured
When I query "FDA 510(k) guidance 2024"
Then Context7 MCP should return results
And results should include document references
And response time should be <30 seconds
```

#### Scenario 1.2: Context7 MCP handles errors gracefully
```gherkin
Given Context7 MCP is configured
When query fails
Then error should be handled gracefully
And user should be informed with plain language
And retry should be attempted automatically (max 3)
```

**Definition of Done**:
- [ ] Context7 MCP is accessible
- [ ] Query response time is acceptable
- [ ] Error handling is implemented

---

### IR2: Sequential Thinking MCP Accessibility

**Story**: As ARIA orchestrator, I want to use Sequential Thinking MCP so that I can analyze complex regulatory pathways.

**Acceptance Criteria**:

#### Scenario 2.1: Sequential Thinking MCP analyzes complex queries
```gherkin
Given Sequential Thinking MCP is configured
When I submit complex regulatory strategy query
Then Sequential Thinking MCP should:
  - Break down problem into steps
  - Analyze each step systematically
  - Synthesize final recommendation
And response should be structured and clear
```

#### Scenario 2.2: Sequential Thinking MCP timeout is appropriate
```gherkin
Given Sequential Thinking MCP is configured
When analysis is performed
Then timeout should be 60 seconds
And analysis should complete within timeout
Or user should be informed if timeout occurs
```

**Definition of Done**:
- [ ] Sequential Thinking MCP is accessible
- [ ] Analysis results are structured
- [ ] Timeout is configured appropriately

---

### IR3: Plugin Loads Without Errors

**Story**: As a Claude Code user, I want ARIA plugin to load smoothly so that I can start using it immediately.

**Acceptance Criteria**:

#### Scenario 3.1: Plugin loads successfully
```gherkin
Given Claude Code is starting
When ARIA plugin is installed
Then plugin should load without errors
And /aria command should be available
And no error messages should be displayed
```

#### Scenario 3.2: Plugin dependencies are satisfied
```gherkin
Given ARIA plugin is loading
When dependencies are checked
Then plugin.json should be valid
And aria.yaml should be valid
And .mcp.json should be valid
And all required files should exist
```

**Definition of Done**:
- [ ] Plugin loads without errors
- [ ] All dependencies are satisfied
- [ ] /aria command is available

---

## User Experience Requirements Acceptance

### UR1: Help Command Clarity

**Story**: As a new user, I want clear help information so that I can understand ARIA's capabilities.

**Acceptance Criteria**:

#### Scenario 1.1: Help command is comprehensive
```gherkin
Given I execute "/aria help"
When help is displayed
Then it should include:
  - ARIA description (3-5 sentences)
  - Target users (who should use ARIA)
  - At least 3 usage examples
  - Brief-Execute-Deliver workflow explanation
  - Reference to additional resources
```

#### Scenario 1.2: Help command is easy to understand
```gherkin
Given help command output
When I read help content
Then language should be plain Korean
And technical terms should be explained
And examples should be practical
And structure should be clear with headings
```

**Definition of Done**:
- [ ] Help content is comprehensive
- [ ] Help content is easy to understand
- [ ] Help content is tested with new users

---

### UR2: Error Message Clarity

**Story**: As a user, I want clear error messages so that I know what to do next.

**Acceptance Criteria**:

#### Scenario 2.1: Error message structure is consistent
```gherkin
Given an error occurs
When error message is displayed
Then it should follow this structure:
  1. ## 문제 발생 (heading)
  2. [Plain language problem description]
  3. ### 원인 (cause heading)
  4. [Plain language cause explanation]
  5. ### 다음 단계 (next steps heading)
  6. [Numbered recovery options]
```

#### Scenario 2.2: Error message tone is helpful
```gherkin
Given an error occurs
When error message is displayed
Then tone should be:
  - Helpful, not blaming
  - Encouraging, not frustrating
  - Clear, not vague
And message should offer assistance: "/aria help"
```

**Definition of Done**:
- [ ] Error message structure is consistent
- [ ] Error message tone is helpful
- [ ] Error messages are tested with users

---

## VALID Framework Validation

### V: Verified Acceptance Criteria

**Story**: As a RA/QA professional, I want verified regulatory claims so that I can trust ARIA's guidance.

#### Scenario V.1: All regulatory claims are verified
```gherkin
Given ARIA provides regulatory guidance
When regulatory claim is made
Then source citation must be provided
And citation format must be consistent
And source must be authoritative
```

#### Scenario V.2: Context7 MCP provides current documentation
```gherkin
Given regulatory research is needed
When Context7 MCP is queried
Then current documentation should be retrieved
And document date should be verified
And outdated documents should be flagged
```

**Definition of Done**:
- [ ] 100% of regulatory claims have citations
- [ ] Citations are from authoritative sources
- [ ] Document currency is verified

---

### A: Accurate Acceptance Criteria

**Story**: As a RA/QA professional, I want accurate information so that I can make correct decisions.

#### Scenario A.1: Configuration values are validated
```gherkin
Given aria.yaml is loaded
When configuration is validated
Then all values should be within acceptable ranges
And token budgets should sum to 100%
And timeout values should be positive integers
```

#### Scenario A.2: Error recovery works correctly
```gherkin
Given transient error occurs
When error recovery is triggered
Then retry should be attempted (max 3)
And retry delay should be 30 seconds
And user should be informed of retry attempts
```

**Definition of Done**:
- [ ] Configuration validation is implemented
- [ ] Error recovery mechanisms are tested

---

### L: Linked Acceptance Criteria

**Story**: As a quality assessor, I want traceability so that I can verify requirements coverage.

#### Scenario L.1: Requirement-to-specification traceability
```gherkin
Given SPEC-ARIA-001 requirements
When traceability matrix is reviewed
Then each requirement should map to specification
And each specification should have test scenario
And all mappings should be documented
```

#### Scenario L.2: Brief-Execute-Deliver phase linkage
```gherkin
Given workflow phases are defined
When phase transitions are reviewed
Then Brief output should link to Execute input
And Execute output should link to Deliver input
And transitions should be documented
```

**Definition of Done**:
- [ ] Traceability matrix is complete
- [ ] Phase linkages are documented
- [ ] All requirements are covered

---

### I: Inspectable Acceptance Criteria

**Story**: As a regulatory auditor, I want audit trail so that I can verify decision rationale.

#### Scenario I.1: Decision rationale is documented
```gherkin
Given regulatory decision is made
When decision rationale is reviewed
Then reasoning should be documented
And sources should be cited
And alternatives considered should be listed
```

#### Scenario I.2: Audit trail capability exists
```gherkin
Given audit trail is enabled in configuration
When decision history is reviewed
Then all decisions should be logged
And timestamps should be recorded
And user approvals should be tracked
```

**Definition of Done**:
- [ ] Decision rationale documentation is implemented
- [ ] Audit trail capability is documented
- [ ] Configuration enables audit trail

---

### D: Deliverable Acceptance Criteria

**Story**: As a submitter, I want properly formatted output so that I can submit to regulatory authorities.

#### Scenario D.1: Plugin structure complies with specification
```gherkin
Given ARIA plugin is installed
When plugin structure is reviewed
Then it should match Claude Code specification
And plugin.json should have all required fields
And directory structure should be correct
```

#### Scenario D.2: Output format validation
```gherkin
Given Brief phase is complete
When output is generated
Then format should be Markdown
And structure should be consistent
And metadata should be attached
```

**Definition of Done**:
- [ ] Plugin structure is validated
- [ ] Output format is consistent
- [ ] Format templates are documented

---

## Test Execution Plan

### Test Environment

- **Claude Code Version**: Latest stable
- **Operating System**: macOS, Windows, Linux
- **MCP Servers**: Context7, Sequential Thinking
- **Test User**: Korean-speaking RA/QA practitioner

### Test Execution Order

1. **Unit Tests**: Configuration validation, file structure verification
2. **Integration Tests**: MCP connectivity, plugin loading
3. **User Acceptance Tests**: Command execution, error handling, language validation
4. **Quality Gate Tests**: VALID framework validation

### Test Data

- **Sample Queries**: 510(k) submission, ISO 13485 audit, CAPA management
- **Error Scenarios**: Connection failure, missing information, token limit
- **User Profiles**: Regulatory manager, QA engineer, design engineer

---

## Success Metrics

### Functional Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Plugin recognition | 100% | Claude Code loads plugin |
| Command execution | 100% | /aria help works |
| Intent classification | ≥80% | Correct classification rate |
| MCP connectivity | 100% | Both servers accessible |
| Configuration loading | 100% | aria.yaml loads correctly |

### Quality Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Korean language coverage | 100% | All user-facing output |
| Plain language errors | 100% | No technical jargon |
| Citation format compliance | 100% | Standard, section, version |
| Question option limit | 100% | Max 4 options |

### User Experience Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Help command clarity | Subjective | User assessment |
| Error message clarity | Subjective | User assessment |
| Documentation completeness | 100% | All sections present |

---

## Reference

### Related Documents

- [spec.md](./spec.md): Complete specification with EARS requirements
- [plan.md](./plan.md): Implementation plan with milestones

### Test Templates

Gherkin scenario templates are provided above for each acceptance criterion. These scenarios can be directly used for manual testing or automated test case generation.

### VALID Framework

VALID framework (Verified, Accurate, Linked, Inspectable, Deliverable) validation sections are provided above with specific scenarios for each dimension.
