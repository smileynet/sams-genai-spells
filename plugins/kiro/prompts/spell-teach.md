## Summary

**Dedicated entry point for learning the concepts behind the spells.** Each spell applies an established idea from a real field — programming, education, UX design, documentation theory, or operations research. This command explains what the concept is, where you already encounter it, and how the spell applies it.

**Arguments:** `$ARGUMENTS` (optional) - Spell name to explain (e.g., "idiomatic", "diataxis")

---

## Process

### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Output a concept overview for all spells:

```
SAM'S SPELLS — THE CONCEPTS
══════════════════════════════════════════════════════════════

<!-- SYNC NOTE: The capsules below must stay in sync with the
     spell summaries in each template and the help listing.
     When adding, renaming, or modifying a spell, update all three:
     this file, help.md.template, and the spell template itself. -->

Each spell applies a concept from a real field — programming,
education, UX design, documentation theory, or operations
research. These ideas are worth knowing whether you use this
plugin or not.

IDIOMATIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: Every programming language has a "native" way of
doing things — patterns the community converges on. Idiomatic
code follows these conventions instead of reinventing them.
Where you see it: Style guides, code review, linter rules,
"Effective <Language>" books.
The spell: Constrains the AI to documented, canonical patterns
so it stops hallucinating APIs.

SOCRATIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: People learn better by discovering answers through
guided questions than by being told. Active reasoning beats
passive consumption.
Where you see it: Law school classrooms, coaching, pair
programming, technical interviews.
The spell: Flips the AI from "answer mode" to "question mode"
so you build understanding instead of dependency.

BPAP (BEST PRACTICES & ANTIPATTERNS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: Every field accumulates hard-won knowledge about
what works and what doesn't. Best practices are the do's and
don'ts; antipatterns are the named traps — patterns that look
reasonable but lead to problems, with emphasis on why people
fall into them.
Where you see it: Engineering standards, OWASP Top 10, Google
Engineering Practices, Brown et al.'s AntiPatterns book.
The spell: Uses AI to research and synthesize a structured
do's, don'ts, and named antipatterns guide with sources.

PROGRESSIVE DISCLOSURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: Show the simplest useful information first, reveal
complexity only when someone asks for it. Don't overwhelm
beginners; don't hide power features from experts.
Where you see it: iPhone settings, CLI --help vs man pages,
textbook chapter ordering, FAQ pages.
The spell: Breaks docs into linked files at progressive detail
levels, sized for AI context windows.

DIATAXIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: Documentation fails when it tries to do too many
things at once. Splitting it into four quadrants — tutorials,
how-to guides, reference, explanation — lets each piece do its
job well.
Where you see it: Django docs, Stripe API docs, any well-organized
documentation site.
The spell: Audits, restructures, or generates docs using the
Diataxis four-quadrant framework.

TASK GRAPH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: When tasks have dependencies, model them as a directed
graph. Topological sort gives you execution order, and the longest
path through the graph (the critical path) shows the bottleneck.
Where you see it: Build systems (Make, Bazel), package managers
(npm, pip), spreadsheet recalculation, CI/CD pipelines.
The spell: Maps task dependencies into execution order with
parallel waves, critical path, and Mermaid diagrams.

DEBUG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: Bugs have root causes, not just symptoms. Fixing
the symptom (add a null check, wrap in try/catch) hides the
real problem. Hypothesis-driven debugging — observe, hypothesize,
predict, test — finds the actual cause.
Where you see it: NTSB crash investigations, Toyota's 5 Whys,
git bisect, post-mortem analysis, reliability engineering.
The spell: Forces the AI to trace the causal chain before
suggesting fixes, producing a structured diagnosis instead
of a quick patch.

DEEP DIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The concept: Developers spend most of their time reading code,
not writing it. Expert developers read systematically — starting
at entry points, tracing data flow, identifying key abstractions
— while novices read line by line and get lost.
Where you see it: Onboarding at new jobs, open source contribution,
code review, legacy system archaeology, architecture recovery.
The spell: Applies top-down reading strategy to systematically
explore a codebase and produce a structured architecture map
with diagrams, data flow, and design decisions.

For deeper dives: @spell-teach <spell-name>
```

**If `$ARGUMENTS` is a spell name:**
- Continue to Step 2 with the specified spell

### Step 2: Research the Concept

Search the web for authoritative sources about the concept behind the specified spell.

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and note it.

### Step 3: Output the Deep Dive

```
CONCEPT: <CONCEPT NAME>
══════════════════════════════════════════════════════════════

WHAT IT IS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Open with a concrete, recognizable example or scenario that
 demonstrates the concept in action. Then explain the concept
 in plain language: what problem does it solve, how does it work,
 why is it effective. 2-4 paragraphs.>

WHERE YOU SEE IT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Real-world applications across multiple fields. This is the
 main content section — show breadth:
 - In software/engineering
 - In design/UX
 - In education/communication
 - In other AI tools
 - In day-to-day work>

WHY IT MATTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Broader value of this concept. Why is it worth knowing?
 AI is one beneficiary among several, not the main point.>

HISTORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Who created/popularized this concept, when, and in what context.
 Brief — serves the concept, not the other way around.>

THE SPELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Brief: how the @spell-<spell> command applies this concept.
 What specific adaptation was made? This is one application,
 not the whole story.>

SOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Source 1 with URL>
- <Source 2 with URL>
```

---

## Spell-to-Concept Mapping

| Spell | Concept | Field | Key Source |
|-------|---------|-------|------------|
| idiomatic | Idiomatic code / canonical patterns | Programming | Official language style guides |
| socratic | Socratic method | Education | Plato's dialogues; modern tutoring research |
| bpap | Best practices & antipatterns | Engineering | IEEE/ACM standards; Google Engineering Practices; Brown et al. AntiPatterns |
| progressive-disclosure | Progressive disclosure | UX Design | J.M. Keller, 1983; Nielsen Norman Group |
| diataxis | Diataxis documentation framework | Documentation theory | Daniele Procida, diataxis.fr |
| task-graph | DAGs + Critical Path Method + topological sort | Operations research | Kelley & Walker 1957; Kahn 1962 |
| debug | 5 Whys + fault tree analysis + scientific method | Reliability engineering | Ohno 1950s; Zeller 2009; Bell Labs 1961 |
| deep-dive | Program comprehension + architecture recovery | Software engineering | Rajlich, LaToza, Ko; Murphy 1995; Parnas 1972 |

---

## Example Usage

```
@spell-teach                    # Overview of all concepts
@spell-teach idiomatic          # Deep dive on idiomatic code
@spell-teach diataxis           # Deep dive on Diataxis framework
@spell-teach socratic           # Deep dive on Socratic method
```
