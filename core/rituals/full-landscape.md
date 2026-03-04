# Ritual: Full Landscape

**Spells:** prior-art + deep-dive → bpap
**Type:** Triple (parallel-then-sequential)
**Plan mode:** Compatible

**Use when:** You need the complete picture before codifying practices: what exists externally (prior-art), what exists internally (deep-dive), then distill it all into actionable guidance (bpap). The most comprehensive ritual for entering a new domain or making a major technical decision.

---

## Phase 1: Parallel Execution

Run both spells independently:

**Spell A: prior-art** — Run with the user's topic framed as the capability/need to survey.
**Spell B: deep-dive** — Run with the user's topic framed as the internal codebase area to explore.

**Full spell execution for both** — run each spell's entire process without modification.

**Execution note:** Run spell A first, then spell B. Both receive the original topic but framed for their respective purpose.

---

## Bridge: (prior-art + deep-dive) → bpap

**Extract** from prior-art output:
- **RECOMMENDATION** — the verdict (adopt/adapt/build) and rationale
- **COMPARISON** — evaluation criteria and how candidates scored
- **EXISTING SOLUTIONS** — top candidates with strengths and concerns

**Extract** from deep-dive output:
- **DESIGN DECISIONS** — patterns and conventions the codebase already follows
- **ARCHITECTURE** — module/component relationships
- **DATA FLOW** — how data moves through the current system

**Reframe** as input for bpap:
- Topic becomes: "best practices and antipatterns for <original topic>, informed by the external landscape and internal architecture"
- Context: Carry forward both perspectives — the external landscape (what solutions exist, their trade-offs, the recommended approach) AND the internal architecture (what patterns the codebase follows, what constraints exist, how data flows). Best practices should reflect what works in both the external ecosystem and the internal context. Antipatterns should include both external failure modes (from prior-art's concerns) and internal anti-patterns (from deep-dive's design decisions that may be problematic).

**Gate check:**
- If both prior-art and deep-dive produced clear outputs → proceed normally with the combined context
- If prior-art found no viable solutions AND deep-dive found a well-structured existing implementation → reframe bpap to codify the existing approach's practices
- If deep-dive found the codebase has no relevant architecture (greenfield) → reframe bpap to focus on the external landscape's practices, noting this is for new development
- If either spell produced unclear or insufficient output → present what was gathered, ask user whether to proceed or narrow scope

**User checkpoint:** Present the bridge content and ask:
1. Proceed with bpap using the combined framing
2. Modify the framing (adjust focus or scope)
3. Skip to synthesis (prior-art + deep-dive outputs are sufficient)
4. Redirect to a different spell

---

## Phase 2: bpap

Run `bpap` with the reframed topic from the bridge.

**Full spell execution** — run the entire bpap process without modification.

---

## Synthesis

Produce a synthesis that cross-references all three outputs:

**Convergent findings** (same conclusion from three angles = very strong signal):
Look for practices that are validated by all three perspectives — recommended by external solutions, already followed in the codebase, and codified as a best practice. These are the highest-confidence recommendations.

**Divergent findings** (tensions requiring resolution):
- External vs. internal: prior-art recommends one approach, but deep-dive shows the codebase follows another
- Best practice vs. reality: bpap codifies a best practice that neither external solutions nor the internal codebase actually follows
- External vs. codified: prior-art found strong solutions, but bpap's antipatterns apply to those solutions

**Emergent insights** (visible only in combination):
- Which best practices the codebase already follows (strengths to maintain)
- Which antipatterns the codebase currently exhibits (priorities for improvement)
- How the recommended external solution aligns with or conflicts with the codified practices
- The gap between ideal practices and ecosystem reality — if most solutions violate a best practice, that's either a sign the practice is impractical or that the ecosystem has a systemic problem

**Combined verdict:**
One integrated recommendation covering what to adopt externally, what to maintain internally, and what practices to follow going forward.

**Unified next steps:**
Ordered by impact, combining adoption steps, architectural changes, and practice improvements.
