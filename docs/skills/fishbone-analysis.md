# Fishbone (Ishikawa) Analysis — Skill Reference for AI Assistants

> Categorical cause decomposition for mapping all possible causes of a problem before investigating.

## History

Developed by Kaoru Ishikawa in 1968 at the University of Tokyo. Originally used for quality control at Kawasaki shipyards. One of the Seven Basic Quality Tools (ISO 9004). Also called cause-and-effect diagram, Ishikawa diagram.

## Core Mechanics

1. **Define the EFFECT** — the problem statement becomes the "head" of the fish
2. **Select CATEGORIES** — the "bones" that organize causes into domains
3. **Brainstorm causes** within each category — aim for 3-7 per bone
4. **Decompose causes** into sub-causes where useful
5. **Grade evidence** for each cause:
   - **Confirmed [C]:** Evidence exists
   - **Suspected [S]:** Plausible but unverified
   - **Speculative [Sp]:** Hypothesis only

## Standard Category Sets

### Software / Technology (default for code problems)

| Category | What it covers |
|----------|---------------|
| Code Logic | Algorithm errors, wrong conditions, off-by-one, incorrect control flow |
| Data & State | Stale state, mutation side effects, initialization order, data corruption |
| Dependencies | Version mismatches, breaking changes, missing dependencies, API drift |
| Infrastructure | Servers, networking, DNS, cloud configuration, resource limits |
| Configuration | Wrong settings, environment variables, feature flags, build config |
| Process | CI/CD issues, deployment procedures, testing gaps, review misses |
| Human Factors | Knowledge gaps, communication failures, documentation issues |

### Classic 6M (Manufacturing origin)

Man (People), Machine (Equipment), Method (Process), Material (Inputs), Measurement (Metrics), Mother Nature (Environment)

### Service / Operations

People, Process, Technology, Policy, Environment

### Custom

When the standard sets don't fit, define categories from the problem's domain. State why.

## Decomposition Technique

For each category:

1. Ask "What in [category] could cause [effect]?"
2. For each cause, ask "What specifically?" to get sub-causes
3. Grade each: Confirmed / Suspected / Speculative
4. Stop when causes are specific enough to investigate or test

## Cross-Reference Analysis

After populating all categories, scan for causes that appear in multiple categories. These are **systemic issues** — they affect the system through multiple pathways and are often the highest-value investigation targets.

## Prioritization

Rank causes using Impact x Likelihood:

| Factor | Scale | Meaning |
|--------|-------|---------|
| Impact | 1-5 | How severe if this is the cause? |
| Likelihood | 1-5 | How probable given the evidence? |

Priority = Impact x Likelihood. Investigate top 3-5 first.

## Fishbone vs. Related Techniques

| Technique | Approach | Best for |
|-----------|----------|----------|
| Fishbone / Ishikawa | Breadth-first: enumerate all possible causes across categories | Problems with unknown cause, recurring issues, multiple contributing factors |
| 5 Whys | Depth-first: trace a single causal chain to root cause | Problems with a clear starting symptom, single-chain causation |
| Fault Tree Analysis | Top-down: model failure as AND/OR logic gates | Safety-critical systems, quantitative risk analysis |

Key insight: Fishbone is for **surveying** (breadth), 5 Whys is for **tracing** (depth). Use fishbone first to identify the most likely category, then 5 Whys to trace within it.

## ASCII Fishbone Diagram Format

Use this branch-style format for text output. It scales to any terminal width and supports sub-causes:

```
           ┌─ <cause> ─── <sub-cause>
           ├─ <cause>
<Category>─┤
           ├─ <cause> ─── <sub-cause>
           └─ <cause>

           ┌─ <cause>
<Category>─┤
           └─ <cause> ─── <sub-cause>

═══════════════════════════════════════▶ <EFFECT>

           ┌─ <cause> ─── <sub-cause>
<Category>─┤
           └─ <cause>

           ┌─ <cause>
<Category>─┤
           ├─ <cause>
           └─ <cause> ─── <sub-cause>
```

Layout rules:

- Categories above the center line and below it, distributed roughly evenly
- Center line uses `═══` with arrow `▶` pointing to the EFFECT
- Each category uses `─┤` with `┌─`, `├─`, `└─` for its causes
- Sub-causes extend with `───` from their parent cause
- Evidence grade shown as suffix: `[C]`, `[S]`, `[Sp]` for Confirmed/Suspected/Speculative

## Reporting Template

> **Note:** The spell template (`cause-map.md.template`) is the canonical source for output format. This template is a simplified reference; defer to the spell if they differ.

```
CAUSE MAP
══════════════════════════════════════════════════════════════

Effect: <one-line problem statement>
Category Set: <Software/Tech | Classic 6M | Service/Ops | Custom>

FISHBONE DIAGRAM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<ASCII fishbone diagram>

CATEGORIZED CAUSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Category>:
  - <cause> [grade] — <brief explanation>
    └─ <sub-cause> [grade]

CROSS-CUTTING CAUSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Causes appearing in 2+ categories — systemic issues>

PRIORITY RANKING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| # | Cause | Impact | Likelihood | Score | Category |
```
