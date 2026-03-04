## Summary

**Analyze existing documentation for gaps, mixed concerns, and structural issues.** Applies three lenses: Diataxis (purpose classification), progressive disclosure (depth layering), and ROT analysis (content quality). Read-only — produces an audit report, not file changes.

**Arguments:** `$ARGUMENTS` (required) - Path to docs directory or files to audit

**Output:** Structured audit report with inventory, coverage analysis, and prioritized recommendations output directly to the conversation

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/diataxis-framework.md`
- `docs/skills/progressive-disclosure-framework.md`

---

## Process

### Step 1: Inventory (Quantitative)

Find all markdown files in the target path. Read each file.

Build a content inventory:
- File count, total lines, average lines per file
- File names and paths
- Which files link to which (inbound/outbound link map)

**If `$ARGUMENTS` is empty:**
Ask the user what documentation path to audit.

**If no markdown files found:** Report "No documentation found at this path" and stop.

**Output the inventory:**

```
DOC AUDIT
══════════════════════════════════════════════════════════════

Path: <target path>
Files: <count> markdown files
Total lines: <count>
Average: <count> lines/file

INVENTORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<filename>    <lines> lines
<filename>    <lines> lines
...
```

---

### Step 2: Classify by Purpose (Diataxis Lens)

For each document, classify into Diataxis quadrants using the signals from the skill reference:

| Quadrant | Classification signals |
|----------|----------------------|
| **Tutorial** | Step-by-step, "follow along," builds from zero, every step produces a result |
| **How-to** | "How to X," goal-oriented, assumes basics, task-focused |
| **Reference** | API signatures, tables, exhaustive, organized for lookup |
| **Explanation** | "Why," context, architecture, trade-offs, opinionated |

Flag documents that mix quadrants — these are candidates for splitting.

**Output the quadrant coverage grid:**

```
QUADRANT COVERAGE (Diataxis)
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

<quadrant>: <file1>, <file2>
<quadrant>: <file3>
Missing: <empty quadrants>
```

---

### Step 3: Assess Depth Layering (Progressive Disclosure Lens)

Check for progressive disclosure structure using the skill reference criteria:

- **Entry point:** Does an overview or index exist?
- **Depth levels:** Are there clear levels from simple to complex, or is everything at the same detail?
- **Navigation:** Do files link to each other? Can you navigate from overview to any topic?
- **File sizing:** Are files within the 200–500 line target? Flag files over 500 lines (too large for context windows) and under 50 lines (potentially too thin).
- **Standalone readability:** Can each file be understood without reading the others?

**Output the depth assessment:**

```
DEPTH LAYERING (Progressive Disclosure)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry point:     <file or "MISSING">
Depth levels:    <count identified>
Navigation:      <"linked" / "partial" / "none">
File sizing:     <count> within target, <count> oversized, <count> undersized
Standalone:      <assessment>

Level mapping:
  L1 Overview:    <file or "—">
  L2 Getting Started: <file or "—">
  L3 Guides:      <files or "—">
  L4 Reference:   <files or "—">
  L5 Deep Dives:  <files or "—">
```

---

### Step 4: ROT Analysis (Content Strategy Lens)

Scan for content quality issues:

- **Redundant:** Overlapping docs covering the same ground. Multiple files explaining the same concept or process.
- **Outdated:** Stale references (deprecated APIs, old version numbers, dead links, dates more than 2 years old), instructions that reference removed features.
- **Trivial:** Filler content with no actionable value — placeholder docs, "TODO: write this" files, docs that restate the obvious without adding information.


**Output the ROT findings:**

```
ROT ANALYSIS (Redundant / Outdated / Trivial)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Redundant:
  <file1> ↔ <file2> — both cover <topic>

Outdated:
  <file>:<line> — <what's stale>

Trivial:
  <file> — <why it's filler>

(or "No ROT issues found")
```

---

### Step 5: Structural Health

Check for structural issues:

- **EPPO compliance** (Every Page is Page One): Can each doc be entered from search without prior context?
- **Orphan docs:** Files with no inbound links from any other file
- **Missing index:** No central entry point linking to all docs
- **Inconsistent naming:** Mixed naming conventions across files

**Output structural findings:**

```
STRUCTURAL HEALTH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Standalone readability: <assessment>
Orphan docs: <files with no inbound links>
Index/entry point: <exists / missing>
Naming consistency: <assessment>
```

---

### Step 6: Output Audit Report

Compile all findings into the final report with prioritized recommendations:

```
MIXED-CONCERN DOCS (candidates for splitting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<file> — mixes <quadrant1> + <quadrant2>
  Suggestion: split into <recommended files>

GAPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Missing quadrants, depth levels, or structural elements>

RECOMMENDATIONS (prioritized)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Critical (blocks users):
  1. <most impactful fix>

Important (creates friction):
  2. <second fix>
  3. <third fix>

Nice-to-have:
  4. <improvement>

NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• To reorganize these docs: @spell-doc-restructure <path>
• To create missing docs: @spell-doc-generate <topic>
• To run audit + restructure together: @spell-ritual doc-structure <path>

GOVERNANCE NOTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This audit is a snapshot. Consider re-running after major feature
additions or quarterly to catch drift.
```

---

## Guidelines

- **Inventory ≠ Audit** — Listing docs is not evaluating them. The spell must classify AND assess quality, not just catalog.
- **Vanity Metrics** — "500 pages audited" means nothing. Focus on actionable findings: task completion gaps, mixed-concern docs, missing quadrants. Every metric must answer "can this lead to a decision?"
- **Audit Everything at Once** — For large doc sets (50+ files), scan all but deep-audit a representative sample. Don't create analysis paralysis.
- **Ghost Audit** — Auditing without audience context misses real problems. Ask who reads these docs and what they're trying to accomplish. Technically accurate docs that don't answer user questions still fail.
- **The Perfect Docs Fallacy** — Not all issues are equal. Separate critical (blocks users) from important (creates friction) from nice-to-have. Fix critical first. 20% of fixes give 80% of benefit.
- **One-Off Audit** — The report should suggest ongoing governance, not just a snapshot fix list.

---

## Example Usage

```
@spell-doc-audit docs/
@spell-doc-audit docs/api/
@spell-doc-audit README.md docs/getting-started.md docs/reference.md
```
