# Ritual: Landscape

**Spells:** prior-art → bpap
**Type:** Sequential
**Plan mode:** Compatible

**Use when:** You need to evaluate existing solutions AND codify best practices for a domain. Prior-art surveys the landscape; bpap distills it into actionable guidance.

---

## Phase 1: prior-art

Run `prior-art` with the user's topic as the argument.

**Full spell execution** — run the entire prior-art process without modification.

---

## Bridge: prior-art → bpap

**Extract** from prior-art output:
- **RECOMMENDATION** — the verdict (adopt/adapt/build) and rationale
- **COMPARISON** — the evaluation criteria and how candidates scored
- **EXISTING SOLUTIONS** — the top 3 candidates with their strengths and concerns

**Reframe** as input for bpap:
- Topic becomes: "best practices and antipatterns for <original topic>, informed by the landscape of existing solutions"
- Context: Carry forward the recommendation verdict, the top solution names, and the key trade-offs identified in the comparison. These become grounding evidence for bpap's research phase — the best practices should reflect what the winning solutions do well, and the antipatterns should reflect the failure modes found in weaker candidates.

**Gate check:**
- If prior-art found strong candidates with clear recommendation → proceed normally, bpap will codify practices informed by the landscape
- If prior-art found no viable solutions (verdict: build custom) → reframe bpap topic as "best practices for building custom <topic>" with the gap analysis from prior-art as context
- If prior-art found the topic is too vague to survey → stop and report to user; the topic needs narrowing before bpap can produce useful output

**User checkpoint:** Present the bridge content and ask:
1. Proceed with bpap using this framing
2. Modify the framing (adjust what bpap should focus on)
3. Skip to synthesis (prior-art output is sufficient)
4. Redirect to a different spell

---

## Phase 2: bpap

Run `bpap` with the reframed topic from the bridge.

**Full spell execution** — run the entire bpap process without modification.

---

## Synthesis

Produce a synthesis that cross-references the two outputs:

**Convergent findings:** Where prior-art's evaluation criteria and bpap's best practices point to the same conclusions (e.g., if prior-art flagged "poor error handling" as a concern in weaker candidates, and bpap independently identified error handling as a best practice — that convergence is a strong signal).

**Divergent findings:** Where the landscape survey and the best practices tension each other (e.g., if the recommended solution violates one of bpap's own antipatterns — that tension needs resolution).

**Emergent insights:** Patterns visible only in combination — the prior-art survey may reveal that the best practices are consistently violated across the ecosystem, or that the antipatterns are so common they're treated as normal.
