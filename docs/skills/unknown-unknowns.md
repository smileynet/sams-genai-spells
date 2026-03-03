# Unknown Unknowns & Negative Space Analysis — Skill Reference for AI Assistants

> Techniques for probing beyond known knowledge boundaries. Use this reference when searching for blind spots, mapping what's missing, and importing cross-domain insights.

## The Johari Window / Rumsfeld Matrix

The Johari Window (Luft & Ingham, 1955), popularized in strategic contexts by Donald Rumsfeld's 2002 framing, divides knowledge into four quadrants:

| | **Known to self** | **Unknown to self** |
|---|---|---|
| **Known to others** | **Known knowns** — Facts you're aware of and can verify | **Blind spots** — Things others see that you don't |
| **Unknown to others** | **Hidden knowledge** — Things you know but haven't shared | **Unknown unknowns** — Nobody in the room knows to ask |

### Practical Application

- **Known knowns** → Establish a baseline. What do we know for certain about this topic?
- **Known unknowns** → List open questions. What do we know we don't know?
- **Blind spots** → Probe systematically. What perspectives, fields, or stakeholder groups might see something we're missing?
- **Unknown unknowns** → Can't be listed in advance by definition. The approach is to probe from multiple angles and build robustness, not to predict.

The blind-spot spell primarily targets the second and third quadrants — blind spots and unknown unknowns — using five distinct probing techniques.

## Negative Space Analysis

Negative space analysis identifies what's *absent* from a discussion, document, or plan — gaps that are meaningful precisely because they're missing.

### Expected-Topic Baseline

Absence is only meaningful relative to expected presence. Before identifying gaps, establish what *should* appear:

1. **Survey similar discussions** — For a technology migration, what topics do migration guides typically cover? For a product launch, what do launch checklists usually include?
2. **Build the baseline** — List the expected topics, categories, or considerations based on the survey.
3. **Compare** — What's in the baseline but absent from the current discussion? These are candidate blind spots.
4. **Validate** — For each absence, determine whether it's a genuine gap or an intentional omission. Ask: "Is this absent because it was considered and deemed irrelevant, or because nobody thought of it?"

### The Projection Trap

**AP: THE PROJECTION TRAP**
Inserting your own expectations into the negative space. Seeing absences that reflect your biases rather than genuine gaps.

Guard against this by:
- Anchoring the baseline to external sources (similar projects, industry checklists), not your own expectations
- Checking whether an absence might be intentional (the team chose not to address it) vs. accidental (nobody thought of it)
- Flagging your confidence level: "This appears absent" vs. "This is definitively missing"

## Cross-Domain Transfer

Cross-domain transfer imports solutions, patterns, or warnings from adjacent fields. It's one of the most powerful sources of blind spot detection — but also one of the most error-prone.

### Structural vs. Surface Similarity (Gentner)

Dedre Gentner's research on analogical reasoning shows that people naturally retrieve analogies based on **surface features** (same domain, same objects) rather than **structural relations** (same causal pattern, same relational structure). But structural analogies produce better transfer.

| Type | Basis | Example | Transfer quality |
|------|-------|---------|-----------------|
| **Surface** | Same domain, similar objects | "Our app is like Uber" (both are apps) | Poor — resemblance without insight |
| **Structural** | Same causal/relational pattern | "Our app has the same cold-start problem as a two-sided marketplace" (both need critical mass on both sides simultaneously) | Good — maps the mechanism |

### Validating Cross-Domain Analogies

For each cross-domain finding, check:

1. **What structural pattern maps?** — Identify the specific causal or relational structure that transfers, not just the surface resemblance.
2. **Where does the analogy break down?** — Every analogy has limits. Explicitly note where the correspondence fails.
3. **What's the actionable insight?** — "This is interesting" isn't enough. What does the cross-domain pattern tell the user to do differently?

**AP: THE SHINY ANALOGY**
Importing a pattern from another field because it *looks* similar, not because the causal structure matches. "Uber for X" thinking without checking whether the marketplace dynamics, regulatory environment, or user behavior actually transfer. Every analogy sounds compelling in a pitch deck; only structural analogies survive implementation.

## Horizon Scanning

Horizon scanning surveys emerging developments that could affect a plan, decision, or field. Used by government foresight units (UK Government Office for Science, Singapore's Centre for Strategic Futures) and corporate strategy teams.

### Three-Horizon Model

| Horizon | Timeframe | Signal type | Example |
|---------|-----------|-------------|---------|
| **H1: Current** | Now — 1 year | Established trends, known forces | "Cloud costs are increasing 15% annually" |
| **H2: Emerging** | 1-3 years | Growing trends, early adoption signals | "WebAssembly is being used for server-side plugins" |
| **H3: Frontier** | 3+ years | Weak signals, research papers, fringe experiments | "Formal verification tools are becoming usable by non-specialists" |

### Weak Signals vs. Trends

- **Trends** are established patterns with data. They extrapolate the present. Useful but rarely reveal blind spots because they're already known.
- **Weak signals** are early indicators of potential shifts. A single weak signal is noise; multiple independent weak signals pointing the same direction are worth investigating.

### Scanning Pitfalls

**AP: THE CURIOSITY CABINET**
Collecting every interesting cross-domain finding without testing strategic relevance. Produces impressive-looking but useless reports. Every finding must answer: "Specifically, how does this change what the user should do?"

**Anchor scanning to the specific topic.** Horizon scanning fails when it becomes "scan everything interesting." Each finding must be evaluated against the specific decision or plan, not collected for novelty.

## Signal-to-Noise Triage

### Plausibility/Impact Matrix

After probing, triage findings using two dimensions:

```
                    High Impact
                         │
     Worth monitoring    │  ⚠ ACT ON THESE
     (track signals)     │  (investigate now)
                         │
  Low Plausibility ──────┼──────── High Plausibility
                         │
     Discard             │  Worth noting
     (noise)             │  (low-priority action)
                         │
                    Low Impact
```

### Clustering Requirement

**BP: Cluster signals; don't rely on single data points.**

Real blind spots show up as patterns — multiple independent signals pointing the same direction. A single contrarian blog post is noise; three independent critiques raising the same structural concern is signal.

**AP: THE SINGLE SOURCE LEAP**
Treating one contrarian opinion as a confirmed blind spot. A single source that says "technology X is doomed" is an opinion. Three independent analyses identifying the same structural weakness is a pattern worth investigating. Require corroboration before escalating a finding.

### Categorization

Classify findings to help prioritize action:

| Category | Description | Action type |
|----------|-------------|-------------|
| **Hidden assumption** | Something taken for granted that may not be true | Verify or test |
| **Unexamined failure mode** | A way this could fail that hasn't been considered | Mitigate or plan contingency |
| **Missing perspective** | A stakeholder or viewpoint absent from the analysis | Consult or research |
| **Adjacent knowledge** | Cross-domain pattern that applies | Evaluate structural fit |
| **Contrarian signal** | Substantive critique with reasoning | Investigate evidence |
| **Temporal blind spot** | Something that changes over time (regulations, technology, market) | Monitor or timeline |

## Cynefin Framework

Dave Snowden's Cynefin framework (2007) categorizes situations by their causal structure, which determines the appropriate response:

| Domain | Causality | Response | Blind spot risk |
|--------|-----------|----------|-----------------|
| **Clear** | Obvious cause-effect | Sense → Categorize → Respond | Low — but complacency is a risk |
| **Complicated** | Discoverable cause-effect | Sense → Analyze → Respond | Medium — experts may have blind spots outside their specialty |
| **Complex** | Cause-effect only visible in retrospect | Probe → Sense → Respond | High — prediction is impossible; probe and adapt |
| **Chaotic** | No perceivable cause-effect | Act → Sense → Respond | Highest — stabilize first, analyze later |

**Key insight for blind spot detection:** If the situation is *complex* (not merely complicated), traditional analysis won't surface all risks. The appropriate strategy is to probe with safe-to-fail experiments, not to analyze more deeply. The blind-spot spell's multi-technique approach is itself a form of probing.

## The Completeness Illusion

**AP: THE COMPLETENESS ILLUSION**
Presenting a blind spot analysis as comprehensive. This is worse than no analysis — it creates false confidence. A thorough analysis might find 60-80% of the real blind spots. The remaining 20-40% are, by definition, the ones the methodology couldn't reach.

Every blind spot analysis must:
- State its coverage level honestly (thorough, moderate, or surface)
- Identify what it couldn't check (areas outside web search reach, tacit organizational knowledge, etc.)
- Avoid language suggesting completeness ("all risks identified," "comprehensive analysis")
- Remind the user that true unknown unknowns cannot be fully enumerated — the goal is to reduce the space, not eliminate it

## Sources

- Luft, J. & Ingham, H. (1955). "The Johari Window, a graphic model of interpersonal awareness." *Proceedings of the Western Training Laboratory in Group Development*.
- Gentner, D. (1983). "Structure-mapping: A theoretical framework for analogy." *Cognitive Science*.
- Gentner, D., Rattermann, M., & Forbus, K. (1993). "The roles of similarity in transfer." *Cognitive Psychology*.
- Taleb, N. N. (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House.
- Snowden, D. & Boone, M. (2007). "A Leader's Framework for Decision Making." *Harvard Business Review*.
- UK Government Office for Science. "Futures Toolkit: Tools for Strategic Futures for Policy-makers and Analysts."
- Curry, A. & Hodgson, A. (2008). "Seeing in Multiple Horizons: Connecting Futures to Strategy." *Journal of Futures Studies*.
