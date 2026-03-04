# Ritual: Survey

**Spells:** prior-art + deep-dive (parallel)
**Type:** Parallel-then-synthesize
**Plan mode:** Compatible

**Use when:** You need to understand both external solutions AND internal architecture before making a decision. Prior-art surveys what's available outside; deep-dive maps what exists inside. Together they give you the full picture for build-vs-buy, integration, or migration decisions.

---

## Phase 1: Parallel Execution

Run both spells independently:

**Spell A: prior-art** — Run with the user's topic framed as the capability/need to survey.
**Spell B: deep-dive** — Run with the user's topic framed as the internal codebase area to explore.

**Full spell execution for both** — run each spell's entire process without modification.

**Execution note:** Run spell A first, then spell B. Both receive the original topic but framed for their respective purpose — prior-art looks outward, deep-dive looks inward.

---

## Synthesis

After both spells complete, produce a synthesis that cross-references their outputs:

**Extract** from prior-art output:
- **EXISTING SOLUTIONS** — the candidate solutions with strengths and concerns
- **COMPARISON** — evaluation across criteria
- **RECOMMENDATION** — adopt/adapt/build verdict

**Extract** from deep-dive output:
- **ARCHITECTURE** — the current system's module/component relationships
- **KEY FILES** — important files and their roles
- **DESIGN DECISIONS** — existing patterns and conventions
- **DATA FLOW** — how data moves through the current system

**Cross-reference analysis:**

**Convergent findings** (same conclusion from different angles = strong signal):
Look for cases where external solutions and internal architecture point the same way. For example, if prior-art recommends adopting a library that follows the same patterns deep-dive found in the codebase — that's a natural fit. Or if prior-art's concerns about a solution align with architectural constraints deep-dive identified.

**Divergent findings** (tensions requiring resolution):
Look for cases where external and internal perspectives clash. For example, if prior-art recommends a solution that's architecturally incompatible with what deep-dive found — the integration cost may outweigh the solution's benefits. Or if deep-dive reveals the codebase already partially solves the need, but prior-art found a better external solution — the switching cost needs evaluation.

**Emergent insights** (visible only in combination):
- The gap between what external solutions provide and what the internal architecture needs — this gap IS the integration challenge
- Whether the codebase's existing patterns make adoption easier or harder for specific candidates
- Whether the architecture needs to change to accommodate any external solution (and if so, whether that change is worth it)

**Combined verdict:**
Merge prior-art's adopt/adapt/build recommendation with deep-dive's architectural constraints. The recommendation must account for integration feasibility, not just solution quality.

**Unified next steps:**
Concrete actions that account for both the external solution's integration requirements and the internal architecture's constraints.
