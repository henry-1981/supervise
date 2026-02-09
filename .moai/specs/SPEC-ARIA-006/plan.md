# SPEC-ARIA-006: Execution Plan

## Metadata

| Field | Value |
|-------|-------|
| SPEC ID | SPEC-ARIA-006 |
| Title | Document Consistency Corrections |
| Created | 2026-02-09 |

## 1. Execution Strategy

### Approach

Team-based parallel execution with file ownership boundaries to prevent conflicts.

### Phase Decomposition

| Phase | Agent | Files | Corrections |
|-------|-------|-------|-------------|
| Phase 1: SPEC-002 Corrections | Agent A | SPEC-002 (spec/acceptance/plan) | CR-001, CR-005, CR-008, CR-010 |
| Phase 2: SPEC-003/004 Corrections | Agent B | SPEC-003, SPEC-004 (spec/acceptance/plan) | CR-003, CR-004 |
| Phase 3: SPEC-001/005 Corrections | Agent C | SPEC-001, SPEC-005 (spec) | CR-005, CR-009, CR-011, CR-012 |
| Phase 4: Architecture Corrections | Agent D | ARCHITECTURE-REDESIGN.md, CONTEXT.md | CR-002, CR-007, CR-013 |
| Phase 5: CLAUDE.md Corrections | Agent D | CLAUDE.md | CR-006 |

### Execution Mode

- Phase 1~3: Parallel (no file overlap)
- Phase 4~5: Sequential after Phase 1~3 (may reference corrected SPEC content)

## 2. Detailed Task Breakdown

### Phase 1: SPEC-002 Corrections (Agent A)

**Task 1.1:** Fix TRUST 5 → VALID references [CR-001]
- spec.md lines 95, 493
- acceptance.md lines 19, 566, 611
- plan.md lines 35, 371

**Task 1.2:** Fix date 2025 → 2026 [CR-005]
- spec.md lines 6, 512
- acceptance.md line 5
- plan.md lines 5, 216

**Task 1.3:** Fix Phase 2.3 reference [CR-008]
- spec.md line 44: "Phase 2.3" → "Phase 3, SPEC-ARIA-003"

**Task 1.4:** Fix technology stack [CR-010]
- spec.md lines 61-62: Python/TypeScript → Claude Code CLI / Markdown+YAML

### Phase 2: SPEC-003/004 Chinese Character Corrections (Agent B)

**Task 2.1:** Fix Chinese characters in SPEC-003 [CR-003]
- spec.md line 248: 追踪 → 추적
- spec.md line 257: 清单 → 체크리스트
- acceptance.md line 236: 追踪 → 추적

**Task 2.2:** Fix Chinese characters in SPEC-004 [CR-003]
- spec.md lines 125, 135, 194, 286: 填充 → 입력
- acceptance.md lines 30, 94, 149: 填充 → 입력
- plan.md lines 56, 111: 填充 → 입력

**Task 2.3:** Fix agent count [CR-004]
- spec.md line 41: "20개 에이전트" → "16개 에이전트 (Core 4 + Business 4 + Domain 8)"

### Phase 3: SPEC-001/005 Corrections (Agent C)

**Task 3.1:** Fix dates in SPEC-005 [CR-005]
- spec.md lines 8, 400, 408, 409: 2025 → 2026

**Task 3.2:** Fix token budget in SPEC-001 [CR-009]
- spec.md line 858: Clarify total 200K budget allocation

**Task 3.3:** Fix model assignment in SPEC-001 [CR-011]
- spec.md line 526: haiku → sonnet

**Task 3.4:** Fix plugin name in SPEC-001 [CR-012]
- spec.md plugin.json block: "aria" → "aria-core"

### Phase 4: Architecture Corrections (Agent D)

**Task 4.1:** Fix directory structure [CR-002]
- ARCHITECTURE-REDESIGN.md Section 7.1 (lines 1631-1764)
- Prefix all agents/, skills/, commands/ with .claude/

**Task 4.2:** Add Audit Log DB [CR-007]
- ARCHITECTURE-REDESIGN.md Section 4.2 (after line ~1012)

**Task 4.3:** Fix Notion MCP package name [CR-013]
- ARCHITECTURE-REDESIGN.md line 896: → claude_ai_Notion reference

### Phase 5: CLAUDE.md Corrections (Agent D)

**Task 5.1:** Add missing commands [CR-006]
- CLAUDE.md Section 2: Add /aria template, /aria knowledge

## 3. Quality Verification

After all corrections:
1. Cross-reference all agent counts → must be 16 everywhere
2. Search all files for "2025" → must be 0 occurrences (except MoAI-ADK version references if any)
3. Search all files for Chinese characters (填充, 追踪, 清单, 效, 点检) → must be 0
4. Search all files for "TRUST 5" in ARIA context → must be 0 (only in MoAI-ADK reference context)
5. Verify all directory paths use .claude/ prefix
6. Verify plugin name is aria-core consistently
7. Verify Notion MCP references claude_ai_Notion

## 4. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Line numbers shifted from previous edits | Medium | Low | Use content-based search, not hardcoded line numbers |
| Additional Chinese characters not yet found | Low | Low | Full CJK character scan post-correction |
| TRUST 5 reference in valid MoAI-ADK context removed | Low | Medium | Only fix ARIA-context TRUST 5, preserve MoAI-ADK references |

## 5. Completion Criteria

- [ ] All 13 corrections (CR-001 ~ CR-013) applied
- [ ] Zero Chinese characters in Korean text
- [ ] Zero incorrect date references
- [ ] Quality verification checklist passes
- [ ] Git commit with conventional format

## 6. Version History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0.0 | 2026-02-09 | Initial plan | MoAI Orchestrator |
