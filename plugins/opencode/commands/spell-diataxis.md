---
description: Generate or audit documentation using the Diataxis four-quadrant framework
---

## Summary

**Create, restructure, or audit documentation using the Diataxis framework.** Diataxis splits documentation into four quadrants: tutorials (learning-oriented), how-to guides (task-oriented), reference (information-oriented), and explanation (understanding-oriented). This spell operates in three modes depending on input.

**Arguments:** `$ARGUMENTS` (required) - Topic, docs path, or "audit"

**Output:** Diataxis-structured documentation (files or audit report)

---

## Process

### Step 1: Determine Mode

Parse `$ARGUMENTS` to determine which mode to operate in:

| Input | Mode | What happens |
|-------|------|--------------|
| `audit` or `audit <path>` | **Audit** | Analyze existing docs against Diataxis, report gaps |
| A file/directory path | **Restructure** | Reorganize existing docs into four quadrants |
| A topic name | **Generate** | Create new Diataxis-structured docs from research |

**If `$ARGUMENTS` is empty:**
Ask the user whether they want to audit, restructure, or generate docs.

---

### Mode A: Audit

Analyze existing documentation against the four Diataxis quadrants.

**Step A1: Scan existing docs**
- Find all markdown files in the target path
- Read each file and classify its content

**Step A2: Classify each document**

For each document, determine which quadrant(s) it belongs to:

| Quadrant | Characteristics |
|----------|----------------|
| **Tutorial** | Step-by-step, learning-oriented, "follow along", hands-on |
| **How-to** | Task-oriented, "how do I...", assumes knowledge, goal-focused |
| **Reference** | Information-oriented, API docs, configuration tables, exhaustive |
| **Explanation** | Understanding-oriented, "why", context, background, architecture |

Flag documents that mix quadrants (e.g., a tutorial that also tries to be a reference).

**Step A3: Output audit report**

```
DIATAXIS AUDIT
══════════════════════════════════════════════════════════════

Scanned: <N> documents in <path>

QUADRANT COVERAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

               ┌─────────────┬─────────────┐
               │  PRACTICAL  │  THEORETICAL│
  ┌────────────┼─────────────┼─────────────┤
  │ LEARNING   │ Tutorials   │ Explanation │
  │            │ <count>     │ <count>     │
  ├────────────┼─────────────┼─────────────┤
  │ WORKING    │ How-to      │ Reference   │
  │            │ <count>     │ <count>     │
  └────────────┴─────────────┴─────────────┘

GAPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<List quadrants with 0 documents or notable gaps>

MIXED DOCUMENTS (need splitting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<List documents that mix quadrants, with suggestions>

RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <Most impactful improvement>
2. <Second improvement>
3. <Third improvement>
```

---

### Mode B: Restructure

Reorganize existing documentation into the four Diataxis quadrants.

**Step B1: Read and classify existing content**
Same as Audit Step A1-A2, but also extract the content.

**Step B2: Plan the restructuring**
Show the restructuring plan to the user and ask for confirmation.

**Step B3: Generate restructured files**

Create the following directory structure:
```
docs/<topic>/
├── tutorials/
│   └── <tutorial-files>.md
├── how-to/
│   └── <guide-files>.md
├── reference/
│   └── <reference-files>.md
├── explanation/
│   └── <explanation-files>.md
└── index.md
```

The `index.md` links to all four quadrants with descriptions.

**Step B4: Output summary** (same format as Generate mode)

---

### Mode C: Generate

Create new Diataxis-structured documentation from research.

**Step C1: Research the topic**
Research the topic via web search and codebase analysis.

**Step C2: Plan the four quadrants**

For each quadrant, determine:
- What content belongs here
- What the reader needs to know vs. do
- How long each document should be

Show the plan to the user and ask for confirmation before generating.

**Step C3: Generate the documentation**

Write each quadrant following its specific rules:

**Tutorials:**
- Step-by-step, numbered instructions
- Start from zero — assume no prior knowledge
- Every step should produce a visible result
- "By the end of this tutorial, you will have..."

**How-to guides:**
- Goal-oriented: "How to <accomplish X>"
- Assume the reader knows the basics
- Numbered steps, but more concise than tutorials
- Multiple guides for different tasks

**Reference:**
- Exhaustive and accurate
- Tables, function signatures, configuration options
- No opinions — just facts
- Alphabetical or logical ordering

**Explanation:**
- Context and background
- "Why" questions: why does this work this way?
- Architecture decisions, trade-offs, history
- Can be opinionated

**Step C4: Output summary**

```
DIATAXIS DOCUMENTATION: <TOPIC>
══════════════════════════════════════════════════════════════

Created <N> files in docs/<topic>/

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

FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
index.md                           — Entry point with quadrant links
tutorials/<name>.md                — <description>
how-to/<name>.md                   — <description>
reference/<name>.md                — <description>
explanation/<name>.md              — <description>

Start here: docs/<topic>/index.md
```

---

## Guidelines

- **Respect the quadrants:** The whole point of Diataxis is separation. Don't let tutorials become reference docs.
- **Index page is key:** The index.md should clearly explain what each quadrant offers and when to read it.
- **Not everything needs all four:** A simple tool might only need a tutorial and reference. That's fine — note the gaps but don't force content.
- **200-500 lines per file:** Same sizing as progressive-disclosure. Split large quadrants into multiple files.
- **Link between quadrants:** A tutorial can say "see the reference for all options" without duplicating the reference content.

---

## Example Usage

```
/spell-diataxis audit docs/
/spell-diataxis docs/api/
/spell-diataxis Kubernetes networking
/spell-diataxis React hooks
```
