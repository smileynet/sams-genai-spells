---
description: Research and produce a structured best-practices and antipatterns document
allowed-tools: Bash, Read, Write, Glob, Grep, Task, AskUserQuestion, WebFetch, WebSearch
---

## Summary

**Research a topic and produce a structured best-practices and antipatterns document.** Combines web research, codebase analysis, and structured output into a practical guide of do's, don'ts, and named antipatterns with trap analysis.

**Arguments:** `$ARGUMENTS` (required) - Topic for best-practices and antipatterns research

**Output:** Structured best-practices and antipatterns document output directly to the conversation

---

## Process

### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Use **AskUserQuestion** to ask: "What topic should I research best practices and antipatterns for?"
Provide 3-4 contextual suggestions based on the current codebase (detected languages, frameworks, tools).

**Otherwise:**
- Extract the topic from `$ARGUMENTS`
- Continue to Step 2

### Step 2: Research the Topic

Gather best practices and antipatterns from multiple sources:

**Web research (if available):**
Use **WebSearch** to find current best practices and antipatterns. Search for:
- `"<topic> best practices" site:official-docs OR recent`
- `"<topic> common mistakes to avoid"`
- `"<topic> style guide" OR "coding standards"`
- `"<topic> antipatterns" OR "common pitfalls"`
- `"<topic> code smells" OR "named antipatterns"`

Use **WebFetch** to read the most authoritative 2-3 results.

**Codebase analysis (if relevant):**
- Search for existing usage patterns of the topic in the current codebase
- Note what the codebase already does well vs. where it deviates from best practices

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and codebase analysis. Note at the top that results are based on training knowledge, not live research.

### Step 3: Organize into Structure

Organize findings into the following structure:

```
BEST PRACTICES & ANTIPATTERNS: <TOPIC>
══════════════════════════════════════════════════════════════

Source: <web research | built-in knowledge | codebase analysis>

DO ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <Practice> — <Why>
   Example: <code or description>

2. <Practice> — <Why>
   Example: <code or description>

[...up to 7-10 items]

DON'T ✗
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <Bad practice> — <Why it's bad>
   Instead: <What to do>

2. <Bad practice> — <Why it's bad>
   Instead: <What to do>

[...up to 3-5 items]

ANTIPATTERNS ⚠
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <NAME> — <One-line description>
   Why it's tempting: <What makes this seem reasonable>
   Consequences: <What goes wrong>
   Instead: <The refactored solution>

2. <NAME> — <One-line description>
   Why it's tempting: <What makes this seem reasonable>
   Consequences: <What goes wrong>
   Instead: <The refactored solution>

[...up to 3-5 named antipatterns]

CONTEXT MATTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<2-3 items that are situational — "do this IF <condition>">

SOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Source 1 with URL if from web research>
- <Source 2>
- <Source 3>
```

### Step 4: Output the Document

Output the structured document directly in the conversation.

**Quality checks before output:**
- Each "do" and "don't" has a clear rationale (the "why")
- Examples are concrete, not abstract
- Advice is current (not deprecated patterns)
- "Context matters" section prevents cargo-culting
- Each antipattern has a recognizable name
- "Why it's tempting" explains the trap
- DON'T items and ANTIPATTERNS don't duplicate each other

---

## Guidelines

- **Be specific:** "Use `const` for values that don't change" is better than "use appropriate variable declarations"
- **Credit sources:** Link to official docs, style guides, or authoritative blog posts when available
- **Avoid truisms:** Skip obvious advice like "write clean code" or "use version control"
- **Acknowledge trade-offs:** Best practices have contexts where they don't apply — say so
- **Prioritize:** Put the highest-impact practices first
- **Name antipatterns:** Use established names when they exist (God Object, Golden Hammer). Coin descriptive names for domain-specific ones.
- **Explain the trap:** "Why it's tempting" is what distinguishes an antipattern from a don't.

---

## Example Usage

```
/spell:bpap TypeScript error handling
/spell:bpap React component testing
/spell:bpap Git commit messages
/spell:bpap REST API design
```
