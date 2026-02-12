---
description: Explore and map how a codebase or subsystem works
---

## Summary

**Codebase exploration and program comprehension.** Systematically explores a module, feature, or subsystem and produces a structured architecture map — entry points, data flow, key abstractions, and design decisions. Uses top-down reading strategy: start at entry points, trace inward.

**Arguments:** `$ARGUMENTS` (required) - File path, module name, feature description, or question (e.g., "how does auth work?")

**Output:** Structured architecture report with overview, diagram, key files, data flow, and design decisions

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Check the repository's `docs/skills/` directory for program comprehension and architecture pattern references.

---

## Process

### Step 1: Determine Scope

Parse `$ARGUMENTS` to figure out what to explore:

| Input type | Action |
|------------|--------|
| File or directory path | Explore that module — its purpose, connections, and architecture |
| Feature or component name | Find where it's implemented, trace its boundaries |
| Question ("how does X work?") | Find entry points for X, trace the implementation |
| Vague or broad | Narrow scope before proceeding (see below) |

If the scope is unclear, ask the user to specify: a file/directory path, a feature name, a question about the code, or whether they want a high-level architecture overview.

**Output the scope:**

```
SCOPE
══════════════════════════════════════════════════════════════

Subject:         <what we're exploring>
Boundary:        <what's inside vs. outside this exploration>
Starting points: <files, directories, or entry points to begin from>
```

---

### Step 2: Map the Landscape

Survey the territory before reading deeply:

Find relevant files by naming patterns, search for imports/exports/definitions and cross-references, check for README or architecture docs, and identify the module boundary.

**Scope limiting:** If the target area has more than 30 files, prompt the user to narrow scope. Comprehensive analysis of an entire large codebase isn't useful; focused analysis of a subsystem is.


**Output the landscape:**

```
LANDSCAPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Files: <count> files across <directories>
Languages: <languages and frameworks detected>
Structure:
  <directory/> — <purpose>
  <directory/> — <purpose>

Key markers:
- <README, config files, or docs found>
- <Notable patterns in naming or organization>
```

---

### Step 3: Trace the Architecture

Read the code systematically using a top-down strategy — start at entry points, follow calls inward:

Read the code starting from entry points (exports, route handlers, main functions). Trace call chains inward, track data flow, identify key abstractions and types, and note design patterns and conventions. Search the web if needed to understand unfamiliar frameworks used by the code.

**Graceful degradation:** If web search is unavailable, rely on code analysis and built-in knowledge. Note this limitation.

**Reading priorities:**
- Entry points and public APIs first — these define what the system does
- Type definitions and interfaces second — these define the system's vocabulary
- Internal implementation last — only read deep enough to answer the original question

Build the mental model for the report in Step 4.

---

### Step 4: Report

Synthesize findings into structured output:

```
DEEP DIVE: <SUBJECT>
══════════════════════════════════════════════════════════════

OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<2-3 sentence summary: what this system does, its role, its boundaries>

ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Mermaid diagram showing module/component relationships.
 Use flowchart TD with subgraphs for module boundaries.
 Show key components and their relationships.>

KEY FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <file:line> — <role in the system>
- <file:line> — <role>
[...most important files, not exhaustive]

DATA FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<How data moves through this system>
Entry → <step> → <step> → Output

DESIGN DECISIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Pattern/convention observed> — <why it matters>
  (or "No notable patterns identified")

ENTRY POINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <How to invoke/interact with this system>
- <How to test it>
```

---

## Guidelines

- **Top-down, not line-by-line.** Start at entry points and trace inward. Don't read every file from line 1.
- **Follow data, not control flow.** Understanding what data moves through a system reveals more than tracing every branch and loop.
- **Scope aggressively.** A focused analysis of 10 files beats a shallow scan of 100. When in doubt, go narrower.
- **Mermaid for architecture.** Use `flowchart TD` with subgraphs for module boundaries, solid arrows for direct dependencies, dashed arrows for indirect/event-based connections.
- **Name the patterns.** If the code follows MVC, say "MVC." If it uses event-driven architecture, say that. Named patterns are more useful than descriptions.
- **Stop when the question is answered.** Not every exploration needs to map the entire system. If the user asked "how does auth work?", stop when auth is explained.
- **Credit:** This spell applies techniques from program comprehension research (Rajlich, LaToza, Ko), architecture recovery (Murphy's reflexion models), and Parnas on rational design.

---

## Example Usage

```
/spell-deep-dive src/api/
/spell-deep-dive how does authentication work?
/spell-deep-dive the payment processing module
/spell-deep-dive src/lib/state-machine.ts
```
