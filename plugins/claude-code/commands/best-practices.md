---
description: Research and produce a structured best-practices document
allowed-tools: Bash, Read, Write, Glob, Grep, Task, AskUserQuestion, WebFetch, WebSearch
---

## Summary

**Research a topic and produce a structured best-practices document.** Combines web research, codebase analysis, and structured output into a practical do's-and-don'ts guide.

**Arguments:** `$ARGUMENTS` (required) - Topic for best-practices research

**Output:** Structured best-practices document output directly to the conversation

---

## Process

### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Use **AskUserQuestion** to ask: "What topic should I research best practices for?"
Provide 3-4 contextual suggestions based on the current codebase (detected languages, frameworks, tools).

**Otherwise:**
- Extract the topic from `$ARGUMENTS`
- Continue to Step 2

### Step 2: Research the Topic

Gather best practices from multiple sources:

**Web research (if available):**
Use **WebSearch** to find current best practices. Search for:
- `"<topic> best practices" site:official-docs OR recent`
- `"<topic> common mistakes to avoid"`
- `"<topic> style guide" OR "coding standards"`

Use **WebFetch** to read the most authoritative 2-3 results.

**Codebase analysis (if relevant):**
- Search for existing usage patterns of the topic in the current codebase
- Note what the codebase already does well vs. where it deviates from best practices

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and codebase analysis. Note at the top that results are based on training knowledge, not live research.

### Step 3: Organize into Structure

Organize findings into the following structure:

```
BEST PRACTICES: <TOPIC>
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
1. <Anti-pattern> — <Why it's bad>
   Instead: <What to do>

2. <Anti-pattern> — <Why it's bad>
   Instead: <What to do>

[...up to 5-7 items]

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

---

## Guidelines

- **Be specific:** "Use `const` for values that don't change" is better than "use appropriate variable declarations"
- **Credit sources:** Link to official docs, style guides, or authoritative blog posts when available
- **Avoid truisms:** Skip obvious advice like "write clean code" or "use version control"
- **Acknowledge trade-offs:** Best practices have contexts where they don't apply — say so
- **Prioritize:** Put the highest-impact practices first

---

## Example Usage

```
/spell:best-practices TypeScript error handling
/spell:best-practices React component testing
/spell:best-practices Git commit messages
/spell:best-practices REST API design
```
