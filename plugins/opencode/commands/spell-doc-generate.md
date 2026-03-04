---
description: Research a topic and create structured docs
---

## Summary

**Research a topic and create structured documentation from scratch.** Starts with audience analysis, researches the topic, then generates docs organized by purpose (Diataxis quadrants) and depth (progressive disclosure levels). Each doc stands alone, is sized for AI context windows, and follows quadrant-specific writing rules.

**Arguments:** `$ARGUMENTS` (required) - Topic name, codebase area, or feature to document

**Output:** Structured documentation with index, navigation, and coverage summary output directly to the conversation (Write is available if the user requests the output be saved to files)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/diataxis-framework.md`
- `docs/skills/progressive-disclosure-framework.md`

---

## Process

### Step 1: Audience Analysis

Before deciding structure, identify the audience. This determines which quadrants matter and what depth is needed.

Ask the user who will read this documentation: new users, working developers, both, or internal maintainers.

**If `$ARGUMENTS` is empty:**
Ask the user what to create documentation for: a topic, codebase area, or feature.

Determine:
- **Who** reads this (personas, skill level)
- **What** they're trying to accomplish (jobs-to-be-done)
- **What** they already know (prerequisite knowledge)

---

### Step 2: Research

Research the topic via web search (official docs, tutorials, API references) and codebase analysis (existing docs, usage patterns, configuration).

**Graceful degradation:** If web search is unavailable, rely on codebase analysis and built-in knowledge. Note this limitation.

**Quality gate:** Flag uncertainty. Don't present unverified claims as fact. "I believe this is correct but could not verify" is better than confident fiction.

---

### Step 3: Plan Structure

Based on audience analysis, choose which Diataxis quadrants to populate:

- **Not everything needs all four.** A simple tool may only need tutorial + reference. A complex platform needs all four.
- Plan progressive disclosure depth levels within each quadrant.
- Target **4–7 total files** at **200–500 lines each**.

Show the planned structure to the user and ask for confirmation before generating.

**Output the plan:**

```
DOC GENERATE: <TOPIC>
══════════════════════════════════════════════════════════════

Audience: <who reads this>
Goal: <what they're trying to accomplish>

PLANNED STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<filename>  (<quadrant> / <depth level>)  — <one-line description>
<filename>  (<quadrant> / <depth level>)  — <one-line description>
...

Total: <count> files, estimated <count> lines
```

---

### Step 4: Generate Content

For each document, follow the quadrant-specific writing rules from the diataxis skill reference:

**Tutorials (learning + practical):**
- Step-by-step, numbered instructions
- Start from zero — assume no prior knowledge
- Every step produces a visible result
- "By the end of this tutorial, you will have..."

**How-to guides (working + practical):**
- Goal-oriented: "How to [accomplish X]"
- Assume the reader knows the basics
- Numbered steps, more concise than tutorials
- Multiple guides for different tasks

**Reference (working + theoretical):**
- Exhaustive and accurate
- Tables, function signatures, configuration options
- No opinions — just facts
- Alphabetical or logical ordering

**Explanation (learning + theoretical):**
- Context and background
- "Why" questions: why does this work this way?
- Architecture decisions, trade-offs, history
- Can be opinionated

**Style conventions for all quadrants:**
- Active voice, second person where appropriate
- Conversational tone, concrete examples over abstract descriptions
- Code blocks liberally — show, don't just tell
- Single-idea paragraphs, heading hierarchy (H1–H4 max)
- Each doc stands alone (EPPO) — enough context to enter from search
- Navigation links at top and bottom of each document

**Fill the auto-doc gap:** Tools like JSDoc/Sphinx generate API reference but miss narrative flow, conceptual explanation, worked examples, and common pitfalls. Explicitly fill these gaps.

Output each document to the conversation under a clear heading.

---

### Step 5: Generate Index

Create a hub page with:
- Quadrant coverage grid
- Reading-order guidance
- Audience map (who should read what)
- Cross-quadrant links for related topics

```
## Index: <Topic>

### Start Here
- [Overview](./00-overview.md) — What this is, who it's for

### Tutorials
- [Getting Started](./tutorials/01-getting-started.md) — Zero to working in 10 minutes

### How-to Guides
- [How to <task>](./how-to/01-<task>.md) — <description>

### Reference
- [API Reference](./reference/01-api.md) — Complete API documentation

### Explanation
- [Architecture](./explanation/01-architecture.md) — Why it's designed this way

### Who Should Read What
| If you're... | Start with | Then read |
|--------------|-----------|-----------|
| Brand new | Overview → Getting Started | Tutorials |
| Need to do X | How-to: X | Reference for details |
| Want to understand why | Explanation | Reference for specifics |
```

---

### Step 6: Quality Check and Summary

Verify generated content:
- No hallucinated APIs or broken references
- Claims trace to authoritative sources (official docs, source code)
- Each doc stands alone
- Navigation links are consistent

**Output the summary:**

```
DOC GENERATE SUMMARY: <TOPIC>
══════════════════════════════════════════════════════════════

Generated <N> documents

QUADRANT COVERAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

               ┌─────────────┬─────────────┐
               │  PRACTICAL  │  THEORETICAL│
  ┌────────────┼─────────────┼─────────────┤
  │ LEARNING   │ Tutorials   │ Explanation │
  │            │ ✓ <count>   │ ✓ <count>   │
  ├────────────┼─────────────┼─────────────┤
  │ WORKING    │ How-to      │ Reference   │
  │            │ ✓ <count>   │ ✓ <count>   │
  └────────────┴─────────────┴─────────────┘

CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Index                    — Entry point with quadrant links
<filename>               — <description>
...

SOURCES CONSULTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <source with URL>
- <source with URL>
(or "Based on codebase analysis and built-in knowledge")

SAVE TO FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
To save this documentation, request file output. Suggested structure:
  docs/<topic>/index.md
  docs/<topic>/<filename>.md
  ...

FRESHNESS NOTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated: <today's date>
Update triggers: <what changes would make this docs stale>
```

---

## Guidelines

- **The Curse of Knowledge** — You (the AI) have full context. The reader doesn't. Include foundational context that feels obvious. Test: would someone with the target audience's background understand this without extra Googling?
- **The Hallucination Factory** — Never present unverified claims as fact. Every technical claim must trace to an authoritative source (official docs, source code, verified API). Flag uncertainty explicitly. "I believe this is correct but could not verify" is better than confident fiction.
- **The Completeness Trap** — Documenting everything makes nothing findable. Focus on what the audience needs for their task. Signal-to-noise ratio matters more than volume. If a section isn't answering a real question, cut it.
- **The Wall of Text** — Dense paragraphs kill docs. Use heading hierarchy (H1–H4 max), single-idea paragraphs, bullet lists for sequences, code blocks liberally. Whitespace is structure.
- **Copy-Paste Documentation** — Link to shared content instead of duplicating. When the same info appears in 3+ places, one will go stale. Apply DRY to docs (but don't over-abstract — clarity beats consolidation).
- **Write It and Forget It** — Every generated doc set should note its freshness date and what triggers a needed update. Docs without a maintenance plan are documentation debt waiting to happen.
- **Wrong Doc Type** — Don't write reference when tutorials are needed (or vice versa). Diataxis quadrants exist for a reason: tutorials need narrative progression, references need predictable structure. Mixing them serves neither purpose.

---

## Example Usage

```
/spell-doc-generate Kubernetes networking
/spell-doc-generate src/auth/
/spell-doc-generate our payment processing system
/spell-doc-generate React hooks
```
