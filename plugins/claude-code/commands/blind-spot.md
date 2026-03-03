---
description: Find what you don't know you don't know — surface hidden assumptions, failure modes, and missing perspectives
allowed-tools: Bash, Read, Write, Glob, Grep, Task, AskUserQuestion, WebFetch, WebSearch
---

## Summary

**Systematic blind spot detection.** Takes a topic — a plan, decision, technology, or research question — and probes it from five angles to surface hidden assumptions, unexamined failure modes, missing perspectives, and cross-domain insights. Produces a structured analysis with honest coverage assessment.

**Arguments:** `$ARGUMENTS` (required) - Topic, plan, decision, or question to probe for blind spots

**Output:** Structured blind spot analysis with findings, pattern map, limitations, and specific next steps output directly to the conversation (Write is available if the user requests the output be saved to a file)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

- `docs/skills/assumption-surfacing.md` — SAST methodology, importance/certainty matrix, pre-mortem protocol, red team thinking, common blind spot checklist
- `docs/skills/unknown-unknowns.md` — Johari Window, negative space analysis, cross-domain transfer validation, horizon scanning, signal-to-noise triage, Cynefin categorization

Use **Read** to load these files from the repository root.

---

## Process

### Phase 1: Frame

#### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Use **AskUserQuestion** to ask: "What topic, plan, or decision should I probe for blind spots?"
Provide 3-4 contextual suggestions based on the current codebase or recent conversation context.

**Otherwise:**
- Extract the topic, plan, decision, or question from `$ARGUMENTS`
- Continue to Step 2

#### Step 2: Map Known Territory

Establish a baseline of what is already known before probing for what's missing.

**Web research (if available):**
Use **WebSearch** to survey the current state of knowledge on the topic:
- `"<topic> challenges problems"`
- `"<topic> risks considerations"`
- `"<topic> lessons learned"`
- `"<topic> failure" OR "<topic> postmortem"`

Use **WebFetch** on the most authoritative 2-3 results.

**Codebase analysis (if relevant):**
- Check if the topic relates to the current codebase — look for relevant code, config, docs, ADRs, or prior decisions
- Identify what the project already handles and what it doesn't

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and codebase analysis. Note this honestly in the Coverage field.

**Output the baseline:**

```
KNOWN TERRITORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Known knowns: <what is well-established about this topic>
Known unknowns: <open questions the community already recognizes>
```

**User checkpoint:** Use **AskUserQuestion** to ask:

"What's your familiarity with **<topic>**? This helps me calibrate the analysis."

Options:
- **New to this** — "I'm exploring this topic for the first time"
- **Know the basics** — "I understand the fundamentals but want to go deeper"
- **Experienced** — "I know this well — focus on non-obvious angles"
- **Skip** — "Just run the analysis"

### Phase 2: Probe

#### Step 3: Systematic Blind Spot Detection

Apply five probing techniques. Each technique attacks the topic from a different angle. Track which technique surfaces each finding for the pattern map.

---

**Technique A: Assumption Surfacing**

Surface the implicit assumptions underlying the topic, plan, or decision.

1. Ask: "What must be true for this to work?" List every assumption, including ones that feel obvious.
2. Check each assumption category systematically: technical, organizational, market/user, temporal, resource, regulatory.
3. Rate each assumption on **importance** (1-5: how load-bearing?) and **certainty** (1-5: how verified?).
4. Flag assumptions in the danger zone: importance ≥ 4 AND certainty ≤ 2. These are load-bearing and unverified.
5. For dangerous assumptions, identify what evidence would confirm or refute them.

**Guard against THE FLAT LIST** — do not surface assumptions without rating them. Twenty unranked items are useless. The importance/certainty matrix is mandatory.

---

**Technique B: Pre-Mortem**

Use prospective hindsight to surface failure modes.

1. **Frame the failure in past tense:** "It is one year from now. [The topic/plan/decision] has failed spectacularly. Not a minor setback — a complete disaster. What happened?"
2. **Adopt multiple stakeholder perspectives** — do not analyze from a single viewpoint:
   - End user / customer
   - Operator / maintainer
   - Adversary / competitor
   - Regulator / compliance
   - Adjacent team / upstream-downstream dependency
3. For each failure mode, search for **documented cases** where similar efforts actually failed.

**Critical:** Use "has failed" language, not "might fail." The certainty framing is the entire technique. "What might go wrong?" triggers self-censoring; "What went wrong?" activates different cognitive processes and increases failure identification by 30% (Mitchell et al., 1989).

**Guard against THE POLITE BRAINSTORM** — if the failure modes all sound generic and inoffensive ("it might be slow," "users might not adopt it"), the framing isn't working. Push for specific, vivid, plausible disaster scenarios.

---

**Technique C: Cross-Domain Transfer**

Import patterns, warnings, and solutions from adjacent fields.

1. Use **WebSearch** to find how adjacent fields have dealt with structurally similar problems:
   - `"<structural pattern> in <adjacent field>"`
   - `"<topic> analogy" OR "<topic> parallels"`
   - `"lessons from <adjacent field> for <topic domain>"`
2. Use **WebFetch** on the most relevant 1-2 results.
3. For each cross-domain finding, validate:
   - **What structural pattern maps?** Identify the specific causal or relational structure that transfers.
   - **Is this structural or surface similarity?** Flag explicitly. "Both are apps" = surface. "Both face the cold-start problem of two-sided markets" = structural.
   - **Where does the analogy break down?** Every analogy has limits — note them.
   - **What's the actionable insight?** "Interesting" isn't enough. What should the user do differently?

**Guard against THE SHINY ANALOGY** — reject findings based on surface resemblance. "Uber for X" thinking without structural validation produces impressive-sounding but misleading analogies.

---

**Technique D: Negative Space Analysis**

Identify what's conspicuously *absent* from the discussion.

1. **Build an expected-topics baseline:** Survey what similar discussions, plans, or decisions typically cover. Use web research on comparable topics, industry checklists, or established frameworks.
2. **Compare the topic against the baseline:** What topics appear in the baseline but are absent from the current discussion?
3. **Validate each absence:**
   - Is this absent because it was considered and deemed irrelevant (intentional omission)?
   - Or because nobody thought of it (genuine blind spot)?
   - Flag your confidence level for each.

**Guard against THE PROJECTION TRAP** — anchor the baseline to external sources (similar projects, industry standards, published checklists), not your own expectations. Absences that reflect your biases rather than genuine gaps are worse than useless — they distract from real blind spots.

---

**Technique E: Contrarian Search**

Find substantive critiques and dissenting views.

1. Use **WebSearch** to find authentic criticism:
   - `"<topic> criticism" OR "<topic> problems" OR "<topic> overrated"`
   - `"<topic> failed" OR "<topic> mistake" OR "<topic> regret"`
   - `"why not <topic>" OR "<topic> alternatives"`
2. Use **WebFetch** on the most substantive 1-2 critiques (not clickbait — look for reasoning).
3. For each contrarian finding, require:
   - **The alternative framing** — not just "this is bad" but "here's a different way to see this"
   - **The reasoning** — why someone would authentically hold this view
   - **Supporting evidence** — what facts or examples back the critique
4. **Cluster independent signals.** A single contrarian blog post is noise. Three independent critiques raising the same structural concern is a pattern worth investigating.

**Guard against THE DESIGNATED CONTRARIAN** — token objections without substance are useless. If the contrarian findings all sound like "well, some people say it's bad," the search isn't working. Push for critiques with genuine reasoning and evidence.

**Guard against THE SINGLE SOURCE LEAP** — do not treat one contrarian opinion as a confirmed blind spot. Require corroboration from independent sources before escalating.

---

#### Step 4: Triage and Categorize

Filter and organize findings from all five techniques.

1. **Rate each finding** on plausibility (how likely is this real?) and impact (how much does it matter?). Focus on the high-plausibility, high-impact quadrant.
2. **Categorize** each finding:
   - **Hidden assumption** — something taken for granted that may not be true
   - **Unexamined failure mode** — a way this could fail that hasn't been considered
   - **Missing perspective** — a stakeholder or viewpoint absent from the analysis
   - **Adjacent knowledge** — cross-domain pattern that applies
   - **Contrarian signal** — substantive critique with reasoning
   - **Temporal blind spot** — something that changes over time (regulations, technology, market)
3. **Drop unsupported speculation.** If a finding rests on a single source with no corroboration and no structural reasoning, discard it.
4. **Cap at 7-10 findings.** If more survive triage, keep only the highest plausibility × impact items. More than 10 findings produces analysis paralysis.

### Phase 3: Report

#### Step 5: Output the Analysis

Output the structured analysis directly in the conversation:

```
BLIND SPOT ANALYSIS: <TOPIC>
══════════════════════════════════════════════════════════════

Coverage: <thorough | moderate | surface> — <explanation of what was and wasn't accessible>
Source: <web research | built-in knowledge | codebase analysis | mixed>

KNOWN TERRITORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Known knowns: <what is well-established>
Known unknowns: <open questions the community already recognizes>

BLIND SPOTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <TITLE> [category]
   What: <one-sentence description>
   Evidence: <what supports this — source, reasoning, or cross-domain analogy>
   Impact: <what happens if this blind spot materializes>
   Probe: <which technique surfaced this>

2. <TITLE> [category]
   What: <one-sentence description>
   Evidence: <what supports this — source, reasoning, or cross-domain analogy>
   Impact: <what happens if this blind spot materializes>
   Probe: <which technique surfaced this>

[...up to 7-10 findings]

PATTERN MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Cluster analysis — do multiple findings converge on the same theme?
 If three findings point at the same underlying issue from different
 angles, that convergence is the real signal.>

Technique yield:
- Assumption surfacing: N findings
- Pre-mortem: N findings
- Cross-domain transfer: N findings
- Negative space: N findings
- Contrarian search: N findings

LIMITATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<What couldn't be checked. Honest assessment of coverage gaps.
 Examples: "No access to internal organizational knowledge,"
 "Web search limited to English-language sources,"
 "Cross-domain transfer limited to fields in training data."
 This analysis reduces the space of unknown unknowns — it does
 not eliminate it.>

NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Specific action per finding — not "investigate further" but
 what to investigate, where to look, and who to ask.
 Each next step must be anchored to a specific finding.>

SOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Source with URL>
```

**Quality checks before output:**
- Every finding has an Evidence field with a specific source, reasoning chain, or cross-domain analogy — not just an assertion
- Findings from cross-domain transfer explicitly note structural vs. surface similarity
- Assumptions include importance/certainty ratings, not just a flat list
- Pre-mortem used "has failed" framing, not "might fail"
- No single-source unsupported findings survived triage
- Coverage level is honest — not "thorough" if web search was unavailable
- Limitations section exists and is substantive, not a token disclaimer
- Next steps are specific actions anchored to findings, not generic advice
- The analysis does not claim to be comprehensive

---

## Guidelines

- **Use "has failed," not "might fail"** — The pre-mortem's power comes from prospective hindsight. Certainty framing activates different cognitive processes. Hypothetical framing ("what could go wrong?") triggers self-censoring and produces generic risks.
- **Adopt multiple perspectives, not one** — Analyzing from a single viewpoint (usually the most obvious stakeholder) is the HIPPO EFFECT. Explicitly switch between end user, operator, maintainer, adversary, and regulator perspectives.
- **Require reasoning, not just opposition** — Token contrarian positions that lack substance get dismissed. Every dissenting view must include an alternative framing, reasoning, and evidence.
- **Validate analogies structurally** — Cross-domain findings must map causal/relational structure, not surface features. Note explicitly whether the analogy is structural or superficial, and where it breaks down.
- **Build baselines before identifying absences** — Negative space analysis is meaningless without an expected-topics baseline from external sources. Absences are only significant relative to expected presence.
- **Cluster signals; don't rely on singles** — A single contrarian source is noise. Multiple independent signals pointing the same direction is a pattern. Require corroboration before escalating.
- **Rate on two axes, not one** — Assumptions rated on importance alone or certainty alone are a flat list. The importance × certainty matrix is what identifies the dangerous ones.
- **Be honest about coverage** — State what couldn't be checked. Avoid language suggesting completeness. A blind spot analysis that claims to be comprehensive is worse than no analysis — it creates false confidence.
- **Anchor next steps to findings** — "Investigate further" is not a next step. "Talk to the ops team about finding #3 (maintenance cost assumptions)" is.
- **Credit:** This spell applies pre-mortem analysis (Klein, 1998), strategic assumption surfacing (Mason & Mitroff, 1981), the Johari Window (Luft & Ingham, 1955), cross-domain analogical reasoning (Gentner, 1983), horizon scanning (UK Government Office for Science), red team thinking (Nemeth, 2001), and Cynefin categorization (Snowden, 2007).

---

## Example Usage

```
/spell:blind-spot migrating from PostgreSQL to DynamoDB
/spell:blind-spot our plan to adopt microservices
/spell:blind-spot launching a developer API for our product
/spell:blind-spot switching the team from Scrum to Kanban
/spell:blind-spot using LLMs for automated code review
```
