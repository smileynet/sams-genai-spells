## Summary

**Reorganize existing documentation by purpose and detail level.** Applies topic-based authoring (each doc = self-contained module), Diataxis (quadrant separation), progressive disclosure (depth layering), and EPPO (each page stands alone). Restructures incrementally using the strangler fig approach — piece by piece, not all at once.

**Arguments:** `$ARGUMENTS` (required) - Path to docs to restructure

**Output:** Restructured documentation with navigation, index, and change summary output directly to the conversation (Write is available if the user requests the output be saved to files)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/diataxis-framework.md`
- `docs/skills/progressive-disclosure-framework.md`

---

## Process

### Step 1: Scan and Classify

Find all markdown files in the target path. Read each file.

For each document, classify along two dimensions:

**Diataxis quadrant:** Tutorial, How-to, Reference, or Explanation (flag mixed-quadrant docs)
**Progressive disclosure level:** Overview (L1), Getting Started (L2), Guide (L3), Reference (L4), Deep Dive (L5)

Also assess the current navigation patterns: Are files linked? Is there an entry point? What's the reading order?

**If `$ARGUMENTS` is empty:**
Ask the user what documentation path to restructure.

**Output the classification:**

```
DOC RESTRUCTURE
══════════════════════════════════════════════════════════════

Path: <target path>
Files: <count> markdown files

CURRENT CLASSIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<filename> — <quadrant> / <depth level> (<lines> lines)
<filename> — <quadrant1 + quadrant2> (MIXED) / <depth level> (<lines> lines)
...
```

---

### Step 2: Plan Restructuring

Design the new structure applying:
- **Topic-based authoring:** Each doc = self-contained module on one topic
- **EPPO:** Each page stands alone — enough context to be entered from any direction
- **Diataxis:** Separate quadrants into distinct files or directories
- **Progressive disclosure:** Layer by depth within each quadrant, 200–500 lines per file

Plan navigation design:
- **Hub-and-spoke index:** Central entry point linking to all docs
- **Hierarchical nav within quadrants:** Organized by depth level
- **Cross-links between related topics:** How-to links to relevant reference, tutorial links to explanation

Show the restructuring plan to the user and ask for confirmation before proceeding.

**Output the restructuring plan:**

```
RESTRUCTURING PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Target structure:
  <new-path>/<filename>  ← <source file(s)>  (<action: keep/split/merge/move>)
  ...

Navigation:
  Index: <hub page location>
  Cross-links: <planned linking strategy>

Changes:
  Keep as-is:   <count> files
  Split:        <count> files → <count> new files
  Merge:        <count> files → <count> files
  Move/rename:  <count> files
```

---

### Step 3: Restructure Incrementally

Apply the strangler fig approach — transform piece by piece, not all at once:

1. **Split mixed-concern docs:** Separate content by quadrant. Each resulting file should cover one topic from one angle.
2. **Assign to structure:** Place files in quadrant directories with numbered prefixes (`00-`, `01-`, etc.) for reading order within each section.
3. **Add navigation links:** Header/footer navigation + breadcrumbs showing position in the structure.
4. **Enforce sizing:** Split files over 500 lines. Flag files under 50 lines for merging.
5. **Ensure standalone context:** Each restructured doc includes enough context to be entered from search without reading anything else first.

Output each restructured document to the conversation, under clear headings. Include navigation links at top and bottom of each section.

---

### Step 4: Generate Index

Create a hub page mapping the full structure:

- Organized by quadrant with progressive-disclosure depth within each
- Cross-quadrant links for related topics
- Audience guidance: who should read what

```
## Index

### Tutorials (Learning + Practical)
- [Getting Started](./tutorials/01-getting-started.md) — First steps, zero to working
- [Walkthrough: <topic>](./tutorials/02-walkthrough.md) — Guided hands-on exercise

### How-to Guides (Working + Practical)
- [How to <task>](./how-to/01-<task>.md) — <one-line description>

### Reference (Working + Theoretical)
- [API Reference](./reference/01-api.md) — Complete API documentation
- [Configuration](./reference/02-config.md) — All configuration options

### Explanation (Learning + Theoretical)
- [Architecture](./explanation/01-architecture.md) — Why it's designed this way
```

---

### Step 5: Output Summary

```
RESTRUCTURE SUMMARY
══════════════════════════════════════════════════════════════

Files: <original count> → <new count>

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

CHANGES MADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Preserved: <files kept with minimal changes>
Split:     <source file> → <new file 1>, <new file 2>
Merged:    <file 1> + <file 2> → <merged file>
Added:     <new files created (e.g., index)>

REMAINING GAPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Quadrants or depth levels still missing content>
• To create missing content: @spell-doc-generate <topic>

BACKWARD COMPATIBILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Moved/renamed files that may need redirects or link updates>
```

---

## Guidelines

- **The Architect's Cathedral** — Elegant structure nobody can use. Limit hierarchy to 3–4 levels max. If you're adding more than 2–3 categories per level, you haven't understood user tasks. Test structure against real user goals, not architectural purity.
- **Empty Taxonomy** — Never create categories without content. Design with real content, not theoretical slots. If a category has fewer than 2 items, merge or eliminate it.
- **Big Bang Migration** — Don't move everything at once. Restructure section by section, validate each before proceeding. Preserve rollback capability. The strangler fig pattern exists because big bang migrations fail catastrophically.
- **Organizing by Internal Structure** — Structure docs by user mental models, not by how the product or team is organized. If your doc structure mirrors your org chart, you've made this mistake.
- **Restructuring as Procrastination** — Rearranging docs isn't the same as improving them. Set explicit goals tied to user outcomes ("users failing to find X"), not "percent reorganized."
- **Vague Information Scent** — Labels must predict what's behind them. "Explore" and "Discover" tell users nothing. Use task-oriented labels that match user language.
- **Ignoring Backward Compatibility** — Plan redirects for every changed URL/path. Broken bookmarks destroy trust. Old links should work for 6+ months minimum.

---

## Example Usage

```
@spell-doc-restructure docs/
@spell-doc-restructure docs/api/
@spell-doc-restructure src/docs/
```
