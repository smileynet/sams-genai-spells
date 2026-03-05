---
description: Research and produce a structured best-practices and antipatterns document
---

## Summary

**Research a topic and produce a structured best-practices and antipatterns document.** Combines web research, codebase analysis, and structured output into a practical guide with numbered best practices (BP) and named antipatterns (AP).

**Arguments:** `$ARGUMENTS` (required) - Topic for best-practices and antipatterns research. Optional flag: `--no-save` (output to conversation only, don't write file)

**Output:** Structured best-practices and antipatterns document output to the conversation and saved to `docs/bpap-<topic-slug>.md` by default. Use `--no-save` to output to conversation only.

---

## Process

### Phase 1: Extract

**Step 1: Parse Arguments**

**If `$ARGUMENTS` is empty:**
Ask the user: "What topic should I research best practices and antipatterns for?"

**Otherwise:**
- Extract the topic from `$ARGUMENTS`
- Parse optional flag: `--no-save` — output to conversation only, don't write file
- Generate a slug from the topic: lowercase, spaces and special characters replaced with hyphens (e.g., "Git commit messages" -> "git-commit-messages")
- Determine scope: **narrow** (1-3 concerns) or **broad** (3+ distinct subtopics)

**Step 2: Research**

Gather best practices and antipatterns from multiple sources:

**Web research (if available):**
Search the web for current best practices, antipatterns, common mistakes, and style guides for the topic.

**Codebase analysis (if relevant):**
- Search for existing usage patterns of the topic in the current codebase
- Note what the codebase already does well vs. where it deviates from best practices

**Scan for existing bpap files:**
- Search `docs/` for `bpap-*.md` or `*bpap*.md` files — note related topics for the Cross-References section

**Scan for existing idiomatic files:**
- Search for any idiomatic constraint files related to the topic for cross-referencing

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and codebase analysis. Note at the top that results are based on training knowledge, not live research.

### Phase 2: Compose

**Step 3: Choose Structure**

Pick one of two structures based on scope:

- **Flat** (narrow topic, 1-3 concerns): Single `## Best Practices` section followed by `## Antipatterns`. Items numbered `BP-1`, `BP-2`... and `AP-1`, `AP-2`...
- **Sectioned** (broad topic, 3+ subtopics): Multiple `## N. Section Title` headings, each with `### Best Practices` and `### Antipatterns` subsections. Items numbered `BP-N.1`, `BP-N.2`... and `AP-N.1`, `AP-N.2`...

**Decision rule:** If the topic has 3+ distinct subtopics that each warrant their own best practices, use sectioned. Otherwise use flat.

**Step 4: Compose the Document**

Apply the output format below. For each item:
- **Best Practice:** Imperative title + what to do and why + rationale with evidence or source
- **Antipattern:** Named pattern + what it looks like + why it's tempting + consequences + what to do instead

**Decision rule for antipatterns vs. best practices:** An antipattern has a name, a temptation, and consequences. If you can't fill all three fields, fold it into a best practice as a "don't" with rationale.

### Phase 3: Verify

**Step 5: Self-Check**

Before presenting the document, verify against this quality rubric:

- [ ] Every BP has a rationale with evidence or source
- [ ] Every AP has a name + trap analysis ("why it's tempting")
- [ ] BPs and APs don't duplicate each other
- [ ] Cross-refs use BP-X.Y/AP-X.Y IDs when referencing other bpap docs
- [ ] "When to Break These Rules" has 2-3 specific items (not blanket disclaimers)
- [ ] Sources section exists (even if "Based on training knowledge")
- [ ] Advice is specific, not truistic ("use `const`" not "use appropriate declarations")
- [ ] Freshness metadata present (date, source, review-after)
- [ ] AI Rules Distillation appendix included
- [ ] Idiomatic cross-references added (if files exist)

Fix any issues before presenting the output.

**Step 6: Save**

**Default behavior (no `--no-save` flag):**
- Use the slug generated in Step 1
- Write the document to `docs/bpap-<topic-slug>.md`
- If the file already exists: warn the user, note what changed, and overwrite (recoverable via git)
- Confirm: "Saved to `docs/bpap-<topic-slug>.md`"

**If `--no-save` flag present:**
- Output to conversation only
- Note: "Not saved. Run again without `--no-save` to persist for cross-referencing."

---

## Output Format

Use standard markdown only. Do not use Unicode box-drawing characters. Do not add explanatory text outside the structured sections. Only use headers and sections specified in this format.

### Flat structure (narrow topics)

```markdown
# Best Practices and Antipatterns: <Topic>

<1-2 sentence scope statement.>

**Generated:** <YYYY-MM-DD> | **Source:** <web research | training knowledge>
**Review after:** <+6 months from generation>

---

## Best Practices

**BP-1: <Imperative title>.** <What to do and why.>

**Rationale:** <Evidence or reasoning.>

**BP-2: <Imperative title>.** <What to do and why.>

**Rationale:** <Evidence or reasoning.>

## Antipatterns

**AP-1: <Named pattern>.** <What it looks like.>

Why it's tempting: <What makes this seem reasonable.>
Consequences: <What goes wrong.>
Instead: <The better approach.>

---

## When to Break These Rules

- **BP-1** -- <Specific condition when breaking it is correct>
- **AP-1** -- <Specific context where this pattern is actually appropriate>

## Cross-References

- [Related doc title (BP-X.Y)](./bpap-related.md) -- <relevance>
<Include idiomatic cross-reference only if .claude/rules/idiomatic-*.md files exist:>
- [Idiomatic <tool> constraints](.claude/rules/idiomatic-<tool>.md) -- auto-loading AI constraints

## Sources

- [Title](URL) -- <what this source contributed>

## AI Rules Distillation

> Terse constraint block for AI rules files (.claude/rules/, AGENTS.md).
> Not a replacement for the full guide.

```
USE:
- <terse pattern from BP-1>
- <terse pattern from BP-2>

AVOID:
- <terse anti-pattern from AP-1>
- <terse anti-pattern from AP-2>
```
```

### Sectioned structure (broad topics)

```markdown
# Best Practices and Antipatterns: <Topic>

<1-2 sentence scope statement.>

**Generated:** <YYYY-MM-DD> | **Source:** <web research | training knowledge>
**Review after:** <+6 months from generation>

---

## 1. <Section Title>

<2-3 sentence context paragraph framing the core tension.>

### Best Practices

**BP-1.1: <Imperative title>.** <What to do and why.>

**Rationale:** <Evidence or reasoning.>

### Antipatterns

**AP-1.1: <Named pattern>.** <What it looks like.>

Why it's tempting: <What makes this seem reasonable.>
Consequences: <What goes wrong.>
Instead: <The better approach.>

## 2. <Section Title>

...same pattern...

---

## When to Break These Rules

- **BP-1.1** -- <Specific condition when breaking it is correct>
- **AP-2.1** -- <Specific context where this pattern is actually appropriate>

## Cross-References

- [Related doc title (BP-X.Y)](./bpap-related.md) -- <relevance>
<Include idiomatic cross-reference only if .claude/rules/idiomatic-*.md files exist:>
- [Idiomatic <tool> constraints](.claude/rules/idiomatic-<tool>.md) -- auto-loading AI constraints

## Sources

- [Title](URL) -- <what this source contributed>

## AI Rules Distillation

> Terse constraint block for AI rules files (.claude/rules/, AGENTS.md).
> Not a replacement for the full guide.

```
USE:
- <terse pattern from BP-1.1>
- <terse pattern from BP-2.1>

AVOID:
- <terse anti-pattern from AP-1.1>
- <terse anti-pattern from AP-2.1>
```
```

---

## Examples

### Flat example: Git Commit Messages

```markdown
# Best Practices and Antipatterns: Git Commit Messages

Conventions for writing useful commit messages. Based on web research and established style guides.

**Generated:** 2025-03-15 | **Source:** web research
**Review after:** 2025-09-15

---

## Best Practices

**BP-1: Use imperative mood in the subject line.** Write "Add feature" not "Added feature" or "Adds feature." The imperative matches git's own generated messages (`Merge branch`, `Revert`).

**Rationale:** The Git project itself uses imperative mood. A commit message completes the sentence "If applied, this commit will _____."

**BP-2: Limit the subject line to 50 characters.** Short subjects display fully in `git log --oneline`, GitHub PR lists, and notification emails without truncation.

**Rationale:** GitHub truncates at 72. The 50-char guideline keeps subjects scannable in dense logs.

**BP-3: Separate subject from body with a blank line.** Tools like `git log --oneline`, `git shortlog`, and email-based review depend on this separation.

**Rationale:** Git's own documentation specifies this format. Omitting the blank line causes the body to merge into the subject in many tools.

## Antipatterns

**AP-1: The Novel.** Commit messages that tell the full story of how you arrived at the change, including dead ends and debugging steps.

Why it's tempting: You just spent two hours debugging and want to document the journey.
Consequences: Future readers need the *what* and *why*, not the narrative. Long messages get skipped.
Instead: Put the conclusion in the commit message. Put the journey in a PR description or ADR.

**AP-2: The Shotgun Commit.** One commit touching 15 files across 4 unrelated concerns.

Why it's tempting: You're in flow and don't want to stop to commit.
Consequences: Can't revert one change without reverting all. Blame becomes useless. Review is painful.
Instead: Use `git add -p` to stage related hunks. One logical change per commit.

---

## When to Break These Rules

- **BP-1** -- Automated commits (changelogs, version bumps) often use past tense by convention
- **BP-2** -- Monorepo scope prefixes (`packages/auth: `) may push past 50 chars; 72 is the hard limit

## Cross-References

None -- standalone guide.

## Sources

- [How to Write a Git Commit Message](https://cbea.ms/git-commit/) -- Chris Beams' canonical guide
- [Git documentation](https://git-scm.com/docs/git-commit) -- Official format specification

## AI Rules Distillation

> Terse constraint block for AI rules files (.claude/rules/, AGENTS.md).
> Not a replacement for the full guide.

```
USE:
- Imperative mood in commit subjects ("Add feature" not "Added feature")
- 50-char subject limit, 72-char hard limit
- Blank line between subject and body
- One logical change per commit

AVOID:
- Narrative commit messages (put the journey in PRs/ADRs, not commits)
- Multi-concern commits touching unrelated files (use `git add -p`)
```
```

### Sectioned example (abbreviated): React Component Architecture

```markdown
# Best Practices and Antipatterns: React Component Architecture

Patterns for structuring React components in production applications. Based on web research and React documentation.

**Generated:** 2025-03-15 | **Source:** web research
**Review after:** 2025-09-15

---

## 1. Component Composition

Choosing how to split UI into components and how they communicate.

### Best Practices

**BP-1.1: Prefer composition over prop drilling.** Pass components as children or render props instead of threading data through intermediate layers.

**Rationale:** React docs recommend composition as the primary pattern. Prop drilling couples intermediate components to data they don't use.

### Antipatterns

**AP-1.1: The Mega-Component.** A single component file exceeding 500 lines handling layout, data fetching, state management, and rendering.

Why it's tempting: Extracting components feels like premature abstraction when you're building fast.
Consequences: Impossible to test individual concerns. Every change risks regressions across unrelated behavior.
Instead: Extract when a component has more than one reason to change -- that's the single responsibility signal.

## 2. State Management

...

---

## When to Break These Rules

- **BP-1.1** -- One level of prop passing is fine; composition overhead isn't worth it for parent->child

## Cross-References

- [Testing best practices (BP-3)](./bpap-testing.md) -- component testability patterns

## Sources

- [React documentation: Composition vs Inheritance](https://react.dev/learn/passing-data-deeply-with-context) -- Official guidance

## AI Rules Distillation

> Terse constraint block for AI rules files (.claude/rules/, AGENTS.md).
> Not a replacement for the full guide.

```
USE:
- Composition over prop drilling (children, render props)
- Single responsibility per component
- Colocate state with the components that use it

AVOID:
- Mega-Components (500+ line files mixing concerns)
- Deep prop drilling through intermediate components
```
```

---

## Guidelines

- **Be specific:** "Use `const` for values that don't change" is better than "use appropriate variable declarations"
- **Credit sources:** Link to official docs, style guides, or authoritative blog posts when available
- **Avoid truisms:** Skip obvious advice like "write clean code" or "use version control"
- **Acknowledge trade-offs:** Best practices have contexts where they don't apply — say so in "When to Break These Rules"
- **Prioritize:** Put the highest-impact practices first
- **Name antipatterns:** Use established names when they exist (God Object, Golden Hammer). Coin descriptive names for domain-specific ones.
- **Explain the trap:** "Why it's tempting" is what distinguishes an antipattern from a simple don't. If you can't explain the temptation, it's a don't — fold it into a best practice.
- **Save for cross-referencing:** The document is most useful as a file that other spells can discover. Conversation-only is for exploration.
- **AI Rules Distillation is compressed, not authoritative:** It exists for copy-pasting into rules files. The full guide with rationale is the source of truth.

---

## Example Usage

```
/spell-bpap Git commit messages
/spell-bpap React component testing
/spell-bpap REST API design
/spell-bpap TypeScript error handling --no-save
```
