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
Ask the user: "What tool or language should I be idiomatic about?"

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
Search the web for official documentation, idiomatic patterns, and current APIs for the specified tool.

**Codebase analysis:**
- Detect current usage of the tool in the codebase
- Note the version in use (from package.json, pyproject.toml, go.mod, etc.)
- Identify patterns already in use

**Linter/formatter detection:**
Search for linter and formatter configuration files in the codebase. Note which patterns are already enforced by tooling and which are not covered.

**BPAP cross-reference check:**
Search `docs/` for `bpap-*.md` files related to the tool. If found, incorporate relevant BP/AP items as constraints with their IDs.

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


No equivalent auto-loading rules path. Session constraints only. Note: "On Claude Code, use without `--no-save` to persist constraints across sessions via `.claude/rules/`."

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
@spell-idiomatic Python 3.12
@spell-idiomatic React 19 --refresh
@spell-idiomatic Tailwind CSS v4
@spell-idiomatic Go --no-save
@spell-idiomatic Rust
```
