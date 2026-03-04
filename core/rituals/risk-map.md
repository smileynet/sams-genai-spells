# Ritual: Risk Map

**Spells:** blind-spot + zoom-out → cause-map
**Type:** Triple (parallel-then-sequential)
**Plan mode:** Compatible

**Use when:** You need to stress-test a plan AND map all the risks found. Blind-spot and zoom-out surface hidden issues from different angles; cause-map organizes everything into a structured risk landscape with prioritized investigation.

---

## Phase 1: Parallel Execution

Run both spells independently with the same topic:

**Spell A: blind-spot** — Run with the user's topic as the argument.
**Spell B: zoom-out** — Run with the user's topic as the argument.

**Full spell execution for both** — run each spell's entire process without modification.

**Execution note:** Run spell A first, then spell B. Both receive the original topic directly.

---

## Bridge: (blind-spot + zoom-out) → cause-map

**Extract** from blind-spot output:
- **BLIND SPOTS** — the numbered findings with categories and evidence
- **PATTERN MAP** — convergence clusters across techniques

**Extract** from zoom-out output:
- **STRATEGIC FINDINGS** — the numbered findings with lenses and evidence
- **CONVERGENCE MAP** — cross-lens patterns
- **STRATEGIC RECOMMENDATION** — the verdict

**Reframe** as input for cause-map:
- Topic becomes: "all risks and failure modes for <original topic>, as identified by blind spot analysis and strategic challenge"
- Context: Carry forward the combined findings from both spells. These become the candidate causes for cause-map to organize. Blind-spot's hidden assumptions become causes in the "Human Factors" or "Process" categories. Zoom-out's strategic findings become causes across relevant categories. The convergence patterns from both analyses become candidates for cross-cutting causes.

**Gate check:**
- If both spells produced clear findings → proceed normally, cause-map will organize and prioritize them
- If the findings are mostly strategic (zoom-out dominant) with few blind spots → reframe cause-map to focus on strategic risk categorization rather than technical failure modes
- If the findings are mostly hidden gaps (blind-spot dominant) with weak strategic challenge → reframe cause-map to focus on assumption-based risk mapping
- If neither spell produced substantive findings → stop and report to user; the topic may be well-analyzed already, or it needs a more specific framing

**User checkpoint:** Present the bridge content and ask:
1. Proceed with cause-map using the combined findings
2. Modify the framing (focus on specific risk categories)
3. Skip to synthesis (blind-spot + zoom-out outputs are sufficient)
4. Redirect to a different spell

---

## Phase 2: cause-map

Run `cause-map` with the reframed topic from the bridge.

**Full spell execution** — run the entire cause-map process without modification.

---

## Synthesis

Produce a synthesis that cross-references all three outputs:

**Convergent findings** (same risk from three angles = critical signal):
Look for risks identified independently by blind-spot, zoom-out, AND confirmed by cause-map's categorization. A risk that shows up as a blind spot, a strategic weakness, and a high-priority cause is the single most important thing to address.

**Divergent findings** (tensions requiring resolution):
- Blind-spot found risks that cause-map ranked low — either the evidence doesn't support them or cause-map's categories missed them
- Zoom-out recommended "stay course" but cause-map's priority ranking shows critical unaddressed risks
- Cause-map found cross-cutting causes that neither blind-spot nor zoom-out identified independently

**Emergent insights** (visible only in combination):
- The complete risk landscape: blind-spot and zoom-out found the risks, cause-map organized and prioritized them — together they show both WHAT the risks are and HOW they relate to each other
- Whether the risks are predominantly strategic (framing/direction problems) or operational (execution/implementation problems)
- Whether the cross-cutting causes map to blind-spot's convergence clusters — if so, the systemic issues are even more deeply rooted than any single analysis showed

**Combined verdict:**
One integrated risk assessment incorporating zoom-out's strategic recommendation, blind-spot's coverage assessment, and cause-map's prioritized investigation plan.

**Unified next steps:**
Ordered by cause-map's priority ranking, enriched with blind-spot's specific probes and zoom-out's strategic actions. Each next step addresses a specific risk with a concrete action.
