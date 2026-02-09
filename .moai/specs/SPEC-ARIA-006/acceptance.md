# SPEC-ARIA-006: Acceptance Criteria

## Metadata

| Field | Value |
|-------|-------|
| SPEC ID | SPEC-ARIA-006 |
| Title | Document Consistency Corrections |
| Created | 2026-02-09 |

## 1. Critical Priority

### AC-001: VALID Framework (CR-001)

- [ ] SPEC-002 spec.md REQ-001 references VALID, not TRUST 5
- [ ] SPEC-002 spec.md line 493 references VALID
- [ ] SPEC-002 acceptance.md: 0 occurrences of "TRUST 5" in ARIA quality context
- [ ] SPEC-002 plan.md: 0 occurrences of "TRUST 5" in ARIA quality context
- [ ] spec.md line 56 MoAI-ADK reference preserved (TRUST 5 is correct there)

### AC-002: Directory Structure (CR-002)

- [ ] ARCHITECTURE Section 7.1: all paths prefixed with `.claude/`
- [ ] agents/ → .claude/agents/
- [ ] skills/ → .claude/skills/
- [ ] commands/ → .claude/commands/

## 2. High Priority

### AC-003: Chinese Characters (CR-003)

- [ ] Zero occurrences of 填充 in SPEC-003, SPEC-004
- [ ] Zero occurrences of 追踪 in SPEC-003
- [ ] Zero occurrences of 清单 in SPEC-003
- [ ] All 12 replacements verified (9 in SPEC-004, 3 in SPEC-003)

### AC-004: Agent Count (CR-004)

- [ ] SPEC-004 spec.md: "16개 에이전트" (not "20개")

### AC-005: Date Corrections (CR-005)

- [ ] Zero occurrences of "2025-02-09" in SPEC-002 (all 3 files)
- [ ] Zero occurrences of "2025" as date in SPEC-005 spec.md
- [ ] All dates show 2026

## 3. Medium Priority

### AC-006: CLAUDE.md Commands (CR-006)

- [ ] /aria template listed in Section 2
- [ ] /aria knowledge listed in Section 2

### AC-007: Audit Log DB (CR-007)

- [ ] ARCHITECTURE Section 4.2 has 7 databases
- [ ] Audit Log DB definition with required fields

### AC-008: Phase Reference (CR-008)

- [ ] SPEC-002 spec.md: "Phase 3" or "SPEC-ARIA-003" (not "Phase 2.3")

### AC-009: Token Budget (CR-009)

- [ ] SPEC-001 [C9]: Total 200K explicitly stated
- [ ] Brief 120K, Execute 60K, Deliver 20K explicitly stated

### AC-010: Technology Stack (CR-010)

- [ ] SPEC-002: No Python 3.13+ reference in environment
- [ ] SPEC-002: No TypeScript 5.9+ reference in environment
- [ ] Accurate technology description present

## 4. Low Priority

### AC-011: Model Assignment (CR-011)

- [ ] SPEC-001: manager-project model = sonnet

### AC-012: Plugin Name (CR-012)

- [ ] SPEC-001 plugin.json: name = "aria-core"

### AC-013: Notion MCP (CR-013)

- [ ] ARCHITECTURE: Notion MCP references claude_ai_Notion
- [ ] SPEC-004: Notion MCP references claude_ai_Notion

## 5. Global Verification

### Post-Correction Checks

- [ ] `grep -r "2025" .moai/specs/` returns 0 date-related matches
- [ ] `grep -r "填充\|追踪\|清单\|点检\|效" .moai/specs/` returns 0 matches
- [ ] `grep -r "TRUST 5" .moai/specs/SPEC-ARIA-002/` returns only MoAI-ADK context matches
- [ ] `grep -r "20개 에이전트" .moai/specs/` returns 0 matches
- [ ] Plugin name "aria-core" consistent across all documents
- [ ] All directory paths use .claude/ prefix in ARCHITECTURE

## 6. Version History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0.0 | 2026-02-09 | Initial acceptance criteria | MoAI Orchestrator |
