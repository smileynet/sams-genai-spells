---
description: Set idiomatic constraints for a tool or language — use canonical patterns, not hallucinated APIs
allowed-tools: Bash, Read, Write, Glob, Grep, Task, AskUserQuestion, WebFetch, WebSearch
---

## Summary

**Set session constraints to use canonical, documented patterns.** This modifier tells the AI to prefer real, documented APIs and idiomatic patterns over hallucinated or outdated ones. It researches the tool/language and establishes ground rules for the rest of the session.

**Arguments:** `$ARGUMENTS` (required) - Tool, language, or framework name (e.g., "Python", "React 19", "Tailwind CSS v4"). Optional flags: `--no-save` (session only, don't write rules file), `--refresh` (force fresh research even if rules file exists; Claude Code only)

**Type:** Modifier (sets session behavior AND saves to auto-loading rules file by default; `--no-save` for session only)

**Output:** Session constraints applied immediately. On Claude Code, also saved to
`.claude/rules/idiomatic-<tool-slug>.md` for automatic loading in future sessions.
Use `--no-save` for session-only constraints. Use `--refresh` to update an existing file.

---

## Process

### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Use **AskUserQuestion** to ask: "What tool or language should I be idiomatic about?"
Provide 3-4 suggestions based on the current codebase (detected from file extensions, package.json, imports, etc.).

**Otherwise:**
- Extract the tool/language/framework from `$ARGUMENTS`
- If a version is specified (e.g., "React 19", "Python 3.12"), note it for version-specific constraints
- Parse optional flags:
  - `--no-save` — session constraints only, don't write rules file
  - `--refresh` — force fresh research even if rules file exists and is recent
- Generate a slug from the tool name: lowercase, spaces and special characters replaced with hyphens (e.g., "React 19" -> "react-19", "Tailwind CSS v4" -> "tailwind-css-v4")
- Continue to Step 2

### Step 2: Research Current Idioms

Gather canonical patterns for the specified tool:

**Web research (if available):**
Use **WebSearch** to find:
- `"<tool> official documentation"`
- `"<tool> idiomatic patterns" OR "style guide"`
- `"<tool> changelog" OR "what's new"` (if version specified)

Use **WebFetch** on the official docs to verify current APIs and patterns.

**Codebase analysis:**
- Detect current usage of the tool in the codebase
- Note the version in use (from package.json, pyproject.toml, go.mod, etc.)
- Identify patterns already in use

**Linter/formatter detection:**
Use **Glob** to search for linter and formatter configs:
- `.eslintrc*`, `eslint.config.*`, `.prettierrc*`, `biome.json`, `biome.jsonc`
- `ruff.toml`, `pyproject.toml` (check for `[tool.ruff]` or `[tool.pylint]` sections)
- `.golangci.yml`, `.golangci.yaml`
- `rustfmt.toml`, `clippy.toml`
- `.stylelintrc*`, `.editorconfig`

If configs found, **Read** them and note:
- Which idiomatic patterns are already enforced by tooling
- Which patterns are NOT covered by existing linters (these are the most valuable constraints)

**BPAP cross-reference check:**
Use **Glob** to search `docs/` for `bpap-*.md` files related to the tool/language.
If found, **Read** them and incorporate relevant BP/AP items as constraints. Reference specific BP-X.Y/AP-X.Y IDs in the output.

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge. Output a prominent warning:

```
**No web access:** All constraints below are from training knowledge only.
Training data has a cutoff and may not reflect <tool>'s current version.
Verify against official docs before relying on these for production code.
```

### Step 3: Establish Session Constraints

Output a clear set of constraints that will govern the rest of the session:

```
IDIOMATIC MODE: <TOOL/LANGUAGE>
══════════════════════════════════════════════════════════════

Generated: <YYYY-MM-DD>
Source: <web research | training knowledge (verify against current docs)>
Tool version: <detected | specified | unknown>

<If degraded mode, add:>
**WARNING:** Constraints based on training knowledge only. Verify against current docs.

SESSION CONSTRAINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

USE (canonical patterns):
* <Pattern 1> -- <brief rationale>
* <Pattern 2> -- <brief rationale>
* <Pattern 3> -- <brief rationale>
[...5-8 key patterns]

AVOID (deprecated or non-idiomatic):
* <Anti-pattern 1> -> Use <replacement> instead
* <Anti-pattern 2> -> Use <replacement> instead
* <Anti-pattern 3> -> Use <replacement> instead
[...3-5 items]

KEY APIS & IMPORTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<List the correct import paths, API names, and signatures
 that are most commonly hallucinated or confused>

CODEBASE NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Notes about how this tool is already used in the current codebase,
 if applicable. "Not detected in codebase" if not found.>

LINTER/FORMATTER COVERAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Already enforced by tooling:
* <rule> -- enforced by <linter> (<config file>)

Not enforced (constraint only):
* <pattern> -- consider adding <linter rule>

<If no linters detected, replace with: "No linter configs detected.">

RELATED BPAP GUIDES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Incorporating findings from:
* docs/bpap-<tool>.md -- BP-1.2, AP-2.1

<If no bpap files found, omit this section entirely.>

<Footer — depends on mode and platform:>
<Claude Code, default:> Active for this session. Saved to `.claude/rules/idiomatic-<tool-slug>.md` -- constraints will auto-load in future sessions.
<Claude Code, --no-save:> Active for this session only. Use without `--no-save` to persist across sessions.
<OpenCode/Kiro:> Active for this session only. On Claude Code, run without `--no-save` to persist constraints across sessions.
```

### Step 4: Save to Rules File

**Default behavior (no `--no-save` flag):**

Check if `.claude/rules/idiomatic-<tool-slug>.md` already exists:

**No existing file:** Write constraints to `.claude/rules/idiomatic-<tool-slug>.md`. The rules file must be **concise** — include only the USE, AVOID, and KEY APIS blocks. Do NOT include CODEBASE NOTES, LINTER COVERAGE, or RELATED BPAP GUIDES (those are session-only context). Target **under 30 instruction lines** to respect the instruction budget.

Add a metadata comment header at the top of the rules file:

```markdown
<!-- Generated by /spell:idiomatic on YYYY-MM-DD -->
<!-- Source: web research | training knowledge -->
<!-- Tool version: detected | specified | unknown -->
<!-- Refresh: /spell:idiomatic <tool> --refresh -->

# Idiomatic <Tool>

USE:
- <Pattern 1> -- <brief rationale>
- <Pattern 2> -- <brief rationale>
...

AVOID:
- <Anti-pattern 1> -> Use <replacement> instead
- <Anti-pattern 2> -> Use <replacement> instead
...

KEY APIS:
- <Correct import/API> (not <commonly hallucinated alternative>)
...

## Local Overrides

<!-- Add project-specific overrides below this line. This section is preserved on --refresh. -->
```

**File exists + `--refresh`:** Read the existing file. Regenerate with fresh research. Write the updated file, but **preserve** any content under `## Local Overrides`. Report what changed.

**File exists (no `--refresh`):** Note the file already exists and is auto-loading. Display its constraints as the session output. Check the `Generated` date in the metadata comment — if older than 6 months, suggest: "This rules file is over 6 months old. Run `/spell:idiomatic <tool> --refresh` to update with current patterns."

**If `--no-save`:** Skip file writing entirely. Session constraints only.


### Step 5: Confirm Activation

After outputting constraints, confirm the modifier is active:

```
Idiomatic mode active for <tool>. I'll follow these constraints
for the rest of this session. If you see me drift, say "be idiomatic"
and I'll self-correct.
```

---

## Guidelines

- **Specificity matters:** "Use `pathlib.Path` instead of `os.path`" is better than "use modern Python"
- **Version-aware:** If a version is specified or detected, constrain to that version's APIs
- **Import paths are key:** Many hallucinations involve wrong import paths — list the correct ones
- **Don't over-constrain:** 5-8 key patterns is enough; don't list every API in the language
- **Acknowledge the codebase:** If the codebase uses a pattern that contradicts best practice, note it and suggest a migration path rather than ignoring it
- **`--no-save` for one-off tasks:** Writing a one-off script in a language you rarely use? `--no-save` avoids cluttering the rules directory.
- **Keep rules files lean:** The auto-loading rules file contains USE/AVOID/KEY APIS only — no codebase notes or linter coverage. Those are session context, not persistent rules. Target <30 instruction lines.
- **Linters beat rules files:** If a pattern can be enforced by a linter, recommend adding the linter rule. Linter enforcement is deterministic; rules file influence is probabilistic.

---

## Example Usage

```
/spell:idiomatic Python 3.12
/spell:idiomatic React 19 --refresh
/spell:idiomatic Tailwind CSS v4
/spell:idiomatic Go --no-save
/spell:idiomatic Rust
```
