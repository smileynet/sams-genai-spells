---
description: Step back — are we solving the right problem? Challenge a plan or direction from five strategic lenses
---

## Summary

**Strategic problem validation.** Takes a plan, decision, or direction and challenges it from five lenses: problem reframing, inversion, opportunity cost, second-order effects, and upstream analysis. Produces a strategic recommendation — stay course, adjust, pivot, or stop — with evidence-backed findings and specific next actions.

**Arguments:** `$ARGUMENTS` (required) - The plan, decision, or direction to challenge

**Output:** Structured strategic analysis with findings, convergence map, recommendation, and next actions output directly to the conversation (Write is available if the user requests the output be saved to a file)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/problem-framing.md`
- `docs/skills/strategic-thinking.md`

---

## Process

### Phase 1: Ground

#### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Ask the user: "What plan, decision, or direction should I challenge?"

**Otherwise:**
- Extract the plan, decision, or direction from `$ARGUMENTS`
- Continue to Step 2

#### Step 2: Map Current Framing

Establish what the current framing IS before challenging it. Understand the direction as its proponents see it.

**Codebase analysis (if relevant):**
- Check if the topic relates to the current codebase — look for relevant code, config, docs, ADRs, or prior decisions

**Web research (if available):**
Search the web for current best practices, case studies, and documented failures related to the topic.

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and codebase analysis. Note this honestly in the Coverage field.

**Output the current framing:**

```
CURRENT FRAMING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problem as stated: <how the problem is currently framed>
Assumed solution: <what approach has been chosen or proposed>
Stated rationale: <why this approach — the arguments in favor>
Key constraints: <what's treated as fixed or given>
Investment so far: <what has already been spent — time, code, decisions, commitments>
```

**User checkpoint:** Ask how attached they are to the current direction — open to anything, directionally committed, validating, or skip — to calibrate challenge intensity.

### Phase 2: Elevate

#### Step 3: Apply Five Strategic Lenses

Apply each lens systematically. Track which lens surfaces each finding. Guard against the named antipatterns at each step.

---

**Lens A: Problem Reframing**

Challenge the problem framing itself — not the solution, but the problem definition.

1. **Restate the problem 3 different ways** using the six reframing moves (shift beneficiary, system boundary, time horizon, abstraction level, success metric, or negate the constraint). Each reframing must open a solution space the original frame excluded.
2. **Apply abstraction laddering:** Ask "Why?" twice to go up (strategic/causal), "How?" twice to go down (concrete/tactical). Find the level where creative but actionable solutions emerge.
3. **Check Wedell-Wedellsborg's questions:**
   - Get the problem definition in writing — does it reveal hidden assumptions?
   - What's missing from the problem statement?
   - Analyze positive exceptions — when does this problem NOT occur?
   - Question the objective — is there a deeper goal?
4. **Check for dissolution (Ackoff):** Could the problem be reframed so it ceases to exist entirely?


**Guard against THE COSMETIC REFRAME** — if the reframings all suggest the same solutions as the original frame, they're cosmetic. A genuine reframe opens a different solution space. Push harder.

**Guard against THE SOLUTION IN DISGUISE** — if the problem statement encodes the solution ("How do we build a better X?"), reframe to remove the embedded solution ("What problem does X solve, and are there better ways to solve it?").

---

**Lens B: Inversion**

Turn the question upside down. Design failure, then check for it.

1. **Failure inversion:** "How would we guarantee this fails?" List 5-7 specific conditions that would ensure failure. Then check: which of these conditions currently hold or are trending toward?
2. **Success inversion:** "If this succeeds perfectly, then what?" Trace the consequences of success — scale problems, lock-in, organizational ossification, competitive response.
3. **For codebase/technical topics**, apply the seven tech-specific inversion questions: catastrophic failure, silent degradation, rollback impossibility, scale breaks, dependency failures, human error, data integrity.
4. **Classify each finding:** showstopper (must address) / mitigation required (need a plan) / accepted risk (acknowledged).

**Guard against THE GALAXY BRAIN** — every failure mode must be plausible given current constraints, not hypothetical edge cases. If the inversion produces science fiction ("What if the internet goes down globally?"), it's lost contact with reality. Stay grounded.

---

**Lens C: Opportunity Cost**

What are we NOT doing? The best forgone alternative is the real cost.

1. **Identify 2-3 realistic alternatives** to the current direction — things the team could be doing instead with the same resources.
2. Search for realistic alternatives and their trade-offs.
3. **Apply the next-dollar test:** "If we hadn't spent anything yet, would we start this project today?" This separates sunk cost from switching cost.
4. **Check for default bias:** Is the current path being chosen because it's best, or because it's the path of least resistance? Would you choose this if starting fresh?

**Guard against THE SUNK COST ANCHOR** — separate investment already made (irretrievable) from switching cost (real cost of changing direction). Only switching costs should influence the decision.

---

**Lens D: Second-Order Effects**

"And then what?" Trace consequences past the intended outcome.

1. **Map three time horizons:**
   - **10 minutes** — Immediate effects. Does it work? What breaks right now?
   - **10 months** — Ecosystem responses. How do users, teams, competitors adapt?
   - **10 years** — Structural shifts. Lock-in, technical debt, organizational rigidity?
2. **Map ecosystem responses** for each affected actor:
   - Users — adopt, resist, work around, or leave?
   - Adjacent teams — new dependencies, bottlenecks, incentive misalignments?
   - Competitors or alternatives — copy, differentiate, or exploit the gap?
3. **Check for feedback loops:** Does the response amplify the original change (positive feedback → exponential) or dampen it (negative feedback → stabilizing)?
4. **Stop at 2-3 orders.** Beyond that, multiplying small probabilities produces speculation, not analysis.

**Guard against FIRST-ORDER BIAS** — if the analysis stops at "it works" or "users adopt it," it hasn't gone far enough. First-order thinking is fast and feels decisive but misses ecosystem responses.

---

**Lens E: Upstream/Downstream**

Is this intervention at the right level? Or are we treating symptoms while the cause persists?

1. **Check Heath's three barriers:**
   - **Problem blindness** — Is this problem being normalized? ("That's just how it works")
   - **Lack of ownership** — Does the pain sit with one team but the authority to fix it with another?
   - **Tunneling** — Is the team too busy reacting to invest in prevention?
2. **Rate on Meadows' leverage hierarchy** — Where does the current intervention sit? (#12 parameters through #1 paradigm transcendence). Is there a higher-leverage intervention available?
3. **Check for dissolution (Ackoff)** — Is there an upstream redesign that eliminates the need for this downstream intervention entirely?
4. **Target the sphere of influence** — Can the decision-maker actually implement the upstream fix? If not, what's the highest-leverage intervention within their authority?


**Guard against THE ARMCHAIR STRATEGIST** — every upstream insight must target the sphere of influence. "Change the industry standard" is not actionable. "Add observability to expose the hidden failure mode" is.

---

#### Step 4: Triage and Converge

Filter and organize findings from all five lenses.

1. **Rate each finding** on leverage (how much could this change the outcome?) and actionability (can something be done about it?). Focus on the high-leverage, high-actionability quadrant.
2. **Look for convergence** — when multiple lenses identify the same underlying issue from different angles, that convergence is the real signal. Three findings pointing at the same structural problem across different lenses is worth more than five independent minor findings.
3. **Drop galaxy brain findings.** If a finding requires changing human nature, industry structure, or physics, discard it.
4. **Cap at 5-8 findings.** If more survive triage, keep only the highest leverage x actionability items.

### Phase 3: Redirect

#### Step 5: Output the Analysis

Output the structured analysis directly in the conversation:

```
STRATEGIC ANALYSIS: <TOPIC>
══════════════════════════════════════════════════════════════

Coverage: <thorough | moderate | surface> — <explanation of what was and wasn't accessible>
Source: <web research | built-in knowledge | codebase analysis | mixed>

CURRENT FRAMING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problem as stated: <how the problem is currently framed>
Assumed solution: <the chosen or proposed approach>
Stated rationale: <the arguments in favor>

STRATEGIC FINDINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <TITLE>
   Lens: <which lens surfaced this — reframing / inversion / opportunity cost / second-order / upstream>
   What: <one-sentence description>
   Evidence: <what supports this — source, reasoning, or case study>
   Leverage: <high / medium / low — how much this could change the outcome>
   Implication: <what this means for the current direction>

2. <TITLE>
   Lens: <which lens>
   What: <one-sentence description>
   Evidence: <source or reasoning>
   Leverage: <high / medium / low>
   Implication: <what this means>

[...up to 5-8 findings]

CONVERGENCE MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Do multiple findings point at the same underlying issue?
 If findings from reframing, inversion, and upstream all
 converge on the same structural problem, that convergence
 is the strongest signal in the analysis.>

Lens yield:
- Problem reframing: N findings
- Inversion: N findings
- Opportunity cost: N findings
- Second-order effects: N findings
- Upstream/downstream: N findings

STRATEGIC RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recommendation: <STAY COURSE | ADJUST | PIVOT | STOP>

Rationale: <Why this recommendation — reference specific findings
and convergence patterns. This is mandatory — "it depends" is
not a valid recommendation.>

NEXT ACTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Specific actions calibrated to the recommendation level:

 STAY COURSE: minor mitigations for findings, monitoring
 ADJUST: specific changes to approach, timeline, or scope
 PIVOT: concrete alternative direction with first steps
 STOP: what to preserve, how to wind down, where to redirect

 Each action anchored to a specific finding.>

LIMITATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<What couldn't be checked. Honest assessment of coverage gaps.
 Examples: "No access to organizational politics or team dynamics,"
 "Market analysis limited to publicly available information,"
 "Opportunity cost analysis doesn't account for team morale."
 This analysis challenges the framing — it does not replace
 domain expertise or stakeholder input.>

SOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Source with URL>
```

**Quality checks before output:**
- Every finding has an Evidence field with a specific source, reasoning chain, or case study — not just an assertion
- Reframings are genuinely different frames, not cosmetic rewording — each opens a solution space the original frame excluded
- Inversion uses "guarantee failure" framing, not "might fail"
- Opportunity cost alternatives are realistic options the team could actually pursue, not strawmen
- Second-order effects trace at least 2 steps — not just "it works" but "it works, and then..."
- Upstream analysis targets the sphere of influence, not aspirational system redesigns
- Strategic recommendation is mandatory — one of the four options, not "it depends"
- Next actions are specific and calibrated to the recommendation level
- Limitations section exists and is substantive, not a token disclaimer

---

## Guidelines

- **Challenge the frame, not just the solution** — The core value of zoom-out is questioning whether the problem is correctly defined, not whether the solution is well-executed. If all findings are about execution quality, the spell isn't working.
- **Reframings must open new solution spaces** — A reframing that suggests the same solutions as the original frame is cosmetic. Each reframing must be testable: "Does this new frame suggest solutions the old frame would have excluded?" If not, push harder.
- **Use "guarantee failure," not "what could go wrong"** — Inversion's power comes from designing failure, not predicting it. "What could go wrong?" triggers hedging. "How would we guarantee failure?" triggers exhaustive thinking.
- **Separate sunk cost from switching cost** — Sunk costs (already spent, irretrievable) should not influence the decision. Switching costs (real cost of changing direction) should. Most "too late to change" arguments conflate the two.
- **Trace at least two orders** — First-order effects are obvious and usually already considered. Second-order effects (ecosystem responses, feedback loops, emergent behavior) are where strategic insight lives. Stop at three — beyond that is speculation.
- **Target the sphere of influence** — Upstream analysis that recommends "change the industry" is armchair strategy. Every finding must be actionable by someone with authority to act. If it's outside the sphere of influence, note it as a constraint, not a recommendation.
- **The recommendation is mandatory** — "It depends" is not a valid output. Commit to stay course, adjust, pivot, or stop. State the rationale. If the evidence is genuinely ambiguous, say "ADJUST — with further investigation needed on [specific question]."
- **Credit:** This spell applies problem framing (Schon 1983; Dorst 2011), abstraction laddering (Hayakawa), problem dissolution (Ackoff), inversion (Munger; Jacobi), pre-mortem analysis (Klein 1998), second-order thinking (Marks 2011; Hardin 1985), upstream thinking (Heath 2020), and systems leverage points (Meadows 1997).

---

## Example Usage

```
/spell-zoom-out our plan to rewrite the monolith as microservices
/spell-zoom-out migrating from REST to GraphQL
/spell-zoom-out building a custom auth system instead of using Auth0
/spell-zoom-out adding AI-powered code review to our CI pipeline
/spell-zoom-out switching the team from TypeScript to Rust
```
