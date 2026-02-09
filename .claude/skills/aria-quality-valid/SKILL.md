---
name: aria-quality-valid
description: >
  VALID quality framework for regulatory documentation. Implements
  5-dimension validation: Verified, Accurate, Linked, Inspectable, Deliverable.
  Used by manager-quality and expert-reviewer agents for quality gate validation.
license: Apache-2.0
compatibility: Designed for Claude Code with ARIA plugin
allowed-tools: Read Grep Glob Bash
user-invocable: false
metadata:
  version: "1.0.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-09"
  modularized: "true"
  tags: "aria, quality, validation, regulatory, compliance"
  author: "ARIA Team"
  related-skills: "aria-writing-style, moai-foundation-core"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 150
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords: ["quality", "valid", "verification", "validation", "compliance", "regulatory", "audit"]
  agents: ["manager-quality", "expert-reviewer"]
  phases: ["execute", "deliver"]
---

# VALID Quality Framework

## Quick Reference

The VALID framework ensures regulatory documentation meets submission standards through 5 quality dimensions:

| Dimension | Focus | Key Question |
|-----------|-------|--------------|
| **V**erified | Regulatory accuracy | Does content match source regulation text? |
| **A**ccurate | Data correctness | Are all data, figures, and references current and correct? |
| **L**inked | Traceability | Can requirements be traced to evidence? |
| **I**nspectable | Audit readiness | Is decision rationale documented? |
| **D**eliverable | Format compliance | Does output meet submission format requirements? |

## Quality Gates

Every document must pass VALID gates before delivery:

**Minimum Passing Score:** 80/100 (Grade B)

**Critical Failures (Automatic Rejection):**
- Verified dimension score below 70 (regulatory citation errors)
- Deliverable dimension score below 70 (format non-compliance)

## When to Apply

Apply VALID framework at these checkpoints:

1. **Post-Draft:** After expert-writer completes initial document
2. **Post-Review:** After expert-reviewer provides feedback
3. **Pre-Delivery:** Before final output to user

## Module References

For detailed information, see bundled modules:

- **modules/framework.md** - Complete dimension definitions and criteria
- **modules/verification.md** - Verification procedures and checklists
- **modules/scoring.md** - Quality scoring methodology and grade calculation
- **examples.md** - Real-world validation examples
- **reference.md** - External regulatory quality standards

## Usage Pattern

```
1. manager-quality receives document for validation
2. Apply each VALID dimension check (see modules/verification.md)
3. Calculate dimension scores (see modules/scoring.md)
4. Generate quality report with findings
5. If score >= 80: PASS, proceed to delivery
6. If score < 80: REJECT, return to expert-writer with feedback
```

## Integration with ARIA Workflow

**BRIEF Phase:** Not applicable (quality gates applied after content creation)

**EXECUTE Phase:**
- expert-writer drafts document
- expert-reviewer performs preliminary VALID check
- Iterative refinement until quality threshold met

**DELIVER Phase:**
- manager-quality performs final VALID gate validation
- Generate quality certificate for audit trail
- Distribute if passing, reject if failing
