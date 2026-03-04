# Ritual: Doc-Structure

**Spells:** doc-audit → doc-restructure
**Type:** Sequential
**Plan mode:** Compatible (doc-audit is read-only, doc-restructure outputs to conversation)

**Use when:** You need to audit documentation for gaps and structural issues, then reorganize it. Doc-audit analyzes by purpose (Diataxis quadrants), depth (progressive disclosure), and content quality (ROT). Doc-restructure applies the findings.

---

## Phase 1: doc-audit

Run `doc-audit` with the user's path as the argument.

**Full spell execution** — run the entire doc-audit process without modification.

---

## Bridge: doc-audit → doc-restructure

**Extract** from doc-audit output:
- **QUADRANT COVERAGE** — which quadrants are populated and which are missing
- **DEPTH LAYERING** — depth level assessment, navigation status, entry point
- **GAPS** — identified documentation gaps and missing quadrants
- **MIXED-CONCERN DOCS** — documents that need splitting
- **RECOMMENDATIONS** — prioritized improvements

**Reframe** as input for doc-restructure:
- Path stays the same as the user's original path
- Context: Carry forward the quadrant classifications (so doc-restructure knows which files serve which purpose), the mixed-concern docs (so doc-restructure knows what to split), the depth layering assessment (so doc-restructure can apply progressive disclosure), and the prioritized recommendations (so doc-restructure addresses the most critical issues first).

**Gate check:**
- If doc-audit found no documentation exists → stop and report to user; creating docs from scratch should use `doc-generate` first
- If doc-audit found documentation is already well-structured (no mixed concerns, good quadrant coverage, proper depth layering) → ask if restructure is still needed
- If doc-audit found documentation but it's severely lacking (3+ empty quadrants, no entry point) → proceed but note that `doc-generate` may be needed for missing content

**User checkpoint:** Present the bridge content and ask:
1. Proceed with doc-restructure using the audit findings
2. Modify the approach (focus on specific issues)
3. Skip to synthesis (audit report is sufficient)
4. Redirect to a different spell (e.g., doc-generate for missing content)

---

## Phase 2: doc-restructure

Run `doc-restructure` with the same path from the bridge.

**Full spell execution** — run the entire doc-restructure process without modification.

---

## Synthesis

Produce a synthesis that cross-references the two outputs:

**Convergent findings:** Where audit findings directly drove restructuring decisions — issues identified in the audit that were resolved by restructuring (e.g., mixed-concern docs that were split, missing entry point that was created).

**Divergent findings:** Where restructuring revealed issues the audit didn't catch — structural problems that only became visible when reorganizing content (e.g., content that seemed fine in place but didn't fit any quadrant cleanly when separated).

**Emergent insights:** Patterns visible only in combination — the combined view may reveal documentation debt patterns (e.g., all how-to content was buried inside tutorials, suggesting the team writes tutorials when they mean to write guides), or gaps that restructuring can't fix (content that needs to be written, not just moved).
