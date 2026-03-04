# Ritual: Investigate

**Spells:** cause-map → diagnose
**Type:** Sequential
**Plan mode:** Compatible

**Use when:** A problem has unknown or multiple causes and you need both breadth (map ALL causes) AND depth (trace the top one to its root). Cause-map surveys the landscape; diagnose traces the most likely chain.

---

## Phase 1: cause-map

Run `cause-map` with the user's problem as the argument.

**Full spell execution** — run the entire cause-map process without modification.

---

## Bridge: cause-map → diagnose

**Extract** from cause-map output:
- **PRIORITY RANKING** — the top 3-5 causes by Impact x Likelihood score
- **CROSS-CUTTING CAUSES** — systemic issues that appear across multiple categories
- **FISHBONE DIAGRAM** — the full cause landscape for reference
- **INVESTIGATION PLAN** — the specific investigation steps for top causes

**Reframe** as input for diagnose:
- Topic becomes: "<#1 ranked cause from the priority ranking> — in the context of <original problem>"
- Context: Carry forward the priority ranking (so diagnose knows what to trace), the cross-cutting causes (so diagnose watches for systemic issues during tracing), and the investigation plan steps (so diagnose can use them as starting evidence). The cause-map's breadth informs diagnose's depth — diagnose should trace the top cause but watch for connections to the cross-cutting issues.

**Gate check:**
- If cause-map found a clear #1 priority cause → proceed normally, diagnose will trace it to root
- If cause-map found multiple causes with similar scores (top 3 within 20% of each other) → present all three to user and ask which to trace first; diagnose will trace the selected one
- If cause-map found a dominant cross-cutting cause → reframe diagnose to trace the cross-cutting cause rather than the top individual cause, since systemic issues are higher-leverage
- If cause-map found no plausible causes → stop and report to user; the problem statement may need reframing

**User checkpoint:** Present the bridge content and ask:
1. Proceed with diagnose on the #1 cause
2. Choose a different cause to trace (show top 3)
3. Skip to synthesis (cause-map output is sufficient)
4. Redirect to a different spell

---

## Phase 2: diagnose

Run `diagnose` with the reframed topic from the bridge.

**Full spell execution** — run the entire diagnose process without modification.

---

## Synthesis

Produce a synthesis that cross-references the two outputs:

**Convergent findings:** Where cause-map's priority ranking and diagnose's root cause analysis agree (e.g., if the cause-map ranked "state management" highest and diagnose traced to a stale state root cause — strong confirmation).

**Divergent findings:** Where the breadth survey and the depth trace tension each other (e.g., if diagnose found the root cause in a category that cause-map ranked low — either the ranking was wrong or the root cause has an unexpected pathway).

**Emergent insights:** Patterns visible only in combination — the cause-map may reveal that the diagnosed root cause connects to other causes through the cross-cutting analysis, suggesting the fix may address multiple issues simultaneously. Or diagnose may find that the root cause is upstream of several other causes on the fishbone, making it higher-leverage than the priority ranking suggested.
