---
description: Map all possible causes of a problem using fishbone (Ishikawa) categorical decomposition
---

## Summary

**Breadth-first cause decomposition for problems with unknown, multiple, or recurring root causes.** Maps ALL possible causes across categories (fishbone diagram) before investigating any of them. Surfaces systemic issues, cross-cutting causes, and Swiss cheese alignments that single-chain analysis misses.

**Arguments:** `$ARGUMENTS` (required) - Problem statement, symptom, recurring issue, or incident description

**Output:** Structured cause map with ASCII fishbone diagram, categorized causes with evidence grades, cross-cutting analysis, and prioritized investigation plan output directly to the conversation (Write is available if the user requests the output be saved to a file)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/fishbone-analysis.md`
- `docs/skills/root-cause-analysis.md`

---

## Process

### Phase 1: Frame

#### Step 1: Parse the Problem Statement

Extract the **effect** — the specific problem that needs cause mapping. This becomes the "head" of the fishbone.

| Input type | Action |
|------------|--------|
| Specific problem statement | Use directly as the effect. |
| Recurring incident | Frame as the pattern, not a single occurrence (e.g., "Checkout flow fails intermittently" not "Checkout failed at 3pm"). |
| Vague description | Clarify before proceeding (see below). |

**If the problem is unclear:**
Ask the user to describe the problem they want to map causes for: what keeps happening, how often, what's been tried.

**Output the effect statement:**

```
EFFECT
══════════════════════════════════════════════════════════════

Problem: <clear, specific statement of the effect>
Context: <when it occurs, frequency, scope, impact>
```

#### Step 2: Select Category Set

Choose the category set that best fits the problem domain:

| Category set | When to use |
|--------------|-------------|
| **Software / Technology** (default) | Code bugs, system failures, performance issues, integration problems |
| **Classic 6M** | Manufacturing, hardware, physical processes |
| **Service / Operations** | Service delivery, organizational, operational issues |
| **Custom** | When standard sets don't fit — define categories from the problem's domain |

**Software / Technology categories:**

| Category | Covers |
|----------|--------|
| **Code Logic** | Algorithm errors, wrong conditions, off-by-one, incorrect control flow |
| **Data & State** | Stale state, mutation side effects, initialization order, data corruption |
| **Dependencies** | Version mismatches, breaking changes, missing dependencies, API drift |
| **Infrastructure** | Servers, networking, DNS, cloud configuration, resource limits |
| **Configuration** | Wrong settings, environment variables, feature flags, build config |
| **Process** | CI/CD issues, deployment procedures, testing gaps, review misses |
| **Human Factors** | Knowledge gaps, communication failures, documentation issues |


---

### Phase 2: Decompose

#### Step 3: Populate Categories

For each category, brainstorm 3-7 possible causes that could contribute to the effect.

Examine relevant code, configuration, git history, and web resources to find evidence for or against each candidate cause.

**For each cause, assign an evidence grade:**
- **Confirmed** [C] — evidence directly supports this as a contributing cause
- **Suspected** [S] — plausible given the evidence, but not yet verified
- **Speculative** [Sp] — hypothesis only, no supporting evidence yet

**Decompose further where useful:**
For causes that are broad, ask "What specifically?" to get sub-causes. Stop when causes are specific enough to investigate or test.

**Skip categories that clearly don't apply.** The goal is thoroughness where it matters, not forced completeness. But document why you skipped — "Infrastructure: skipped, problem is purely algorithmic" — so the reader knows it was considered.

**Graceful degradation:** If web search is unavailable, rely on code analysis and built-in knowledge. Note this limitation.

#### Step 4: Build Fishbone Diagram

Render the cause map as an ASCII fishbone diagram using branch-style layout:

```
           ┌─ <cause> [C] ─── <sub-cause>
           ├─ <cause> [S]
<Category>─┤
           ├─ <cause> [S] ─── <sub-cause>
           └─ <cause> [Sp]

           ┌─ <cause> [C]
<Category>─┤
           └─ <cause> [S] ─── <sub-cause>

═══════════════════════════════════════▶ <EFFECT>

           ┌─ <cause> [S] ─── <sub-cause>
<Category>─┤
           └─ <cause> [Sp]

           ┌─ <cause> [C]
<Category>─┤
           ├─ <cause> [S]
           └─ <cause> [Sp] ─── <sub-cause>
```

**Layout rules:**
- Distribute categories above and below the center line, roughly evenly
- Center line uses `═══` with arrow `▶` pointing to the EFFECT
- Each category uses `─┤` with `┌─`, `├─`, `└─` for its causes
- Sub-causes extend with `───` from their parent cause
- Evidence grades shown as suffix: `[C]`, `[S]`, `[Sp]`

#### Step 5: Cross-Reference Analysis

Scan for causes that appear in multiple categories. These are **systemic issues** — they affect the system through multiple pathways and are the highest-value investigation targets.

**What to look for:**
- Same cause appearing under different names in different categories
- Causes that are upstream of other causes across categories
- Patterns that suggest a common organizational or architectural weakness

**Output cross-cutting causes:**

```
CROSS-CUTTING CAUSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<description of systemic issue>
  Appears in: <Category 1>, <Category 2>, ...
  Evidence: <what connects these appearances>
  Significance: <why this matters — Swiss cheese alignment, force multiplier, etc.>
```

---

### Phase 3: Prioritize

#### Step 6: Rank and Report

Score each cause on two dimensions:
- **Impact** (1-5): How much does this contribute to the effect if confirmed?
- **Likelihood** (1-5): How probable is this cause given current evidence?
- **Priority** = Impact × Likelihood

**Output the full cause map report:**

```
CAUSE MAP
══════════════════════════════════════════════════════════════

Effect: <one-line problem statement>
Category Set: <Software/Tech | Classic 6M | Service/Ops | Custom>

FISHBONE DIAGRAM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<ASCII fishbone diagram from Step 4>

CATEGORIZED CAUSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Category>:
  - <cause> [grade] — <brief explanation>
    └─ <sub-cause> [grade]
  - <cause> [grade] — <brief explanation>

<Category>:
  - <cause> [grade] — <brief explanation>

(Categories skipped: <list> — <reason>)

CROSS-CUTTING CAUSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<systemic issues from Step 5, or "None identified">

PRIORITY RANKING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| # | Cause                | Impact | Likelihood | Score | Category     |
|---|----------------------|--------|------------|-------|--------------|
| 1 | <top cause>          |   5    |     4      |  20   | <category>   |
| 2 | <second cause>       |   4    |     4      |  16   | <category>   |
| 3 | <third cause>        |   4    |     3      |  12   | <category>   |
...

INVESTIGATION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For the top 3-5 causes:
1. <cause> — <specific investigation steps>
2. <cause> — <specific investigation steps>
3. <cause> — <specific investigation steps>

NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• To trace the #1 cause to its root: /spell-diagnose <top cause>
• To map causes AND trace the top one in sequence: /spell-ritual investigate <problem>
• To check for causes outside these categories: /spell-blind-spot <problem>
```

---

## Antipatterns

| Name | Description | Signal | Fix |
|------|-------------|--------|-----|
| **THE FLAT BONE** | No sub-causes — stopped decomposition too early. Every cause is a vague category-level statement. | "Code issues" instead of "off-by-one in pagination loop" | Ask "What specifically?" until causes are testable or investigable |
| **THE ORPHAN BONE** | Force-fitting causes into categories for completeness. Categories exist to guide brainstorming, not to be filled uniformly. | Strained, implausible causes in categories that don't fit the problem | Skip categories that clearly don't apply. Document the skip. |
| **THE BLAME BONE** | Human Factors category full of individual blame ("Bob didn't test it") instead of systemic enablers ("testing step missing from deployment checklist") | Named individuals as causes | Reframe as: "What systemic condition allowed the error?" |
| **THE PET CAUSE** | Anchoring on a pre-existing theory and giving uneven attention across categories. One bone has 7 detailed causes, others have 1 each. | Dramatic imbalance in cause counts across categories | Ensure minimum 2-3 candidates per relevant category before going deeper on any |
| **THE INFINITE FISHBONE** | >40 causes total, analysis paralysis instead of actionable insight | Diagram too large to scan, no clear priorities | Cap at 5-7 causes per category. Merge similar causes. Prioritize ruthlessly. |

---

## Guidelines

- **Breadth before depth.** Populate ALL relevant categories before investigating ANY cause. The fishbone is for surveying, not tracing.
- **Grade everything.** Every cause gets an evidence grade. No cause enters the diagram as assumed fact.
- **Skip honestly.** Categories that don't apply should be noted as skipped, not ignored silently.
- **Cross-reference is the payoff.** The most valuable output is often the cross-cutting causes — systemic issues visible only when you compare across categories.
- **Cap and prioritize.** A fishbone with 50 causes is noise. Target 15-30 total, prioritize ruthlessly, investigate top 3-5.
- **Credit:** This spell applies Ishikawa's fishbone diagram (1968), Reason's Swiss Cheese Model (1990), and principles from the Seven Basic Quality Tools (ASQ/ISO 9004).

---

## Example Usage

```
/spell-cause-map checkout flow fails intermittently — different error each time
/spell-cause-map CI pipeline takes 45 minutes, used to take 10
/spell-cause-map users reporting data inconsistencies across dashboard views
/spell-cause-map post-mortem: production outage on 2024-01-15
```
