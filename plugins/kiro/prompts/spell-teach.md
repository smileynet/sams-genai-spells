## Summary

**Dedicated entry point for learning the techniques behind the spells.** Instead of just using the spells, this command explains where they came from, why they work, and how to apply them beyond this plugin.

**Arguments:** `$ARGUMENTS` (optional) - Spell name to explain (e.g., "idiomatic", "diataxis")

---

## Process

### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Output a technique overview for all spells:

```
SAM'S SPELLS — THE TECHNIQUES
══════════════════════════════════════════════════════════════

These aren't Sam's ideas. They're well-known techniques that Sam
packaged into buttons because he got tired of re-explaining them.
Here's where they actually come from:

IDIOMATIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Origin: The concept of "idiomatic" code comes from natural language —
writing code the way native speakers of a language would write it.
Why it matters for AI: LLMs hallucinate APIs. Constraining to documented
patterns dramatically reduces this.

SOCRATIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Origin: Socratic method, ~400 BC. Socrates taught by asking questions
rather than giving answers, forcing students to reason through problems.
Why it matters for AI: AI defaults to giving answers. Flipping it to
questions makes you actually learn, not just copy-paste.

BEST PRACTICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Origin: The do's-and-don'ts format is as old as engineering itself.
The research-then-structure approach comes from technical writing.
Why it matters for AI: AI can research and synthesize faster than
you can Google. But it needs structure to avoid a wall of text.

PROGRESSIVE DISCLOSURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Origin: Coined by J.M. Keller (1983) in instructional design. Show
the simplest useful information first, reveal complexity on demand.
Why it matters for AI: AI context windows are finite. Linked files at
progressive detail levels let the AI load only what it needs.

DIATAXIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Origin: Daniele Procida's Diataxis framework (diataxis.fr). Splits
docs into four quadrants: tutorials, how-to guides, reference, explanation.
Why it matters for AI: AI struggles with docs that mix "how" and "why."
Diataxis separation makes each piece more useful as AI context.

TASK GRAPH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Origin: Critical Path Method (Kelley & Walker, 1957), PERT (U.S. Navy,
1958), Kahn's topological sort (1962). Three techniques from operations
research and graph theory, combined.
Why it matters for AI: AI can hold entire dependency graphs in memory,
compute topological sorts accurately, and generate Mermaid diagrams
natively. Structured output prevents vague "just do these in order" answers.

For deeper dives: @spell-teach <spell-name>
```

**If `$ARGUMENTS` is a spell name:**
- Continue to Step 2 with the specified spell

### Step 2: Research the Technique

Search the web for authoritative sources about the technique behind the specified spell.

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and note it.

### Step 3: Output the Deep Dive

```
TECHNIQUE: <TECHNIQUE NAME>
══════════════════════════════════════════════════════════════

ORIGIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Who created/popularized this technique, when, and in what context>

THE CORE IDEA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<2-3 paragraphs explaining the technique in plain language.
 What problem does it solve? How does it work? Why is it effective?>

WHY IT WORKS WITH AI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Specific explanation of why this technique is particularly
 useful when working with AI assistants>

HOW SAM USES IT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<How this technique got packaged into the @spell-<spell> command.
 What specific adaptation was made for the AI context?>

BEYOND THIS SPELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<How to apply this technique more broadly:
 - In other AI tools
 - In human-to-human contexts
 - Recommended reading/resources>

SOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Source 1 with URL>
- <Source 2 with URL>
```

---

## Spell-to-Technique Mapping

| Spell | Technique | Key Source |
|-------|-----------|------------|
| idiomatic | Idiomatic code / canonical patterns | Official language style guides |
| socratic | Socratic method | Plato's dialogues; modern tutoring research |
| best-practices | Structured technical writing | IEEE/ACM engineering standards |
| progressive-disclosure | Progressive disclosure (UX) | J.M. Keller, 1983; Nielsen Norman Group |
| diataxis | Diataxis documentation framework | Daniele Procida, diataxis.fr |
| task-graph | DAGs + Critical Path Method + topological sort | Kelley & Walker 1957; Kahn 1962 |

---

## Example Usage

```
@spell-teach                    # Overview of all techniques
@spell-teach idiomatic          # Deep dive on idiomatic code
@spell-teach diataxis           # Deep dive on Diataxis framework
@spell-teach socratic           # Deep dive on Socratic method
```
