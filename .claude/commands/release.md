---
description: Prepare and execute a Sam's Spells release
allowed-tools: Bash, Read, Edit, Glob, Grep
---

## Summary

**Run release utilities or start an interactive release workflow.** Routes based on `$ARGUMENTS`:

- No args → pre-flight health check
- Version number → full interactive release workflow

---

## Routing

Parse `$ARGUMENTS` and follow the matching path below.

### Path A: No Arguments (health check)

If `$ARGUMENTS` is empty, run the pre-flight validation suite:

```bash
./dev/release.py --check
```

Report the results in a clear table (pass/fail per check, any warnings).

**Then fix any errors found:**

- **Working tree not clean** → Run `git status` to see what's dirty. Stage all changed files and commit them with an appropriate message describing the changes. This clears the tree for release readiness.

- **[Unreleased] section is empty** → Populate it from git history:
  1. Find the last release tag: `git describe --tags --abbrev=0`
  2. List commits since that tag: `git log <tag>..HEAD --oneline`
  3. Read `docs/guidance/changelog.md` for the full changelog style guide
  4. **Filter for user-facing changes only.** The changelog is for plugin users — people who install Sam's Spells and use its spells in their projects. Apply this litmus test: *Would a spell user notice this change?* If only contributors or maintainers would notice, exclude it.
     - **Include:** New spells, changed spell behavior, new workflow capabilities, bug fixes users encounter, breaking changes
     - **Exclude:** Dev scripts, template syncing infra, CI/workflow changes, internal refactoring, beads sync commits, docs updates (unless user-facing command docs)
  5. Categorize: `feat:` → Added, `fix:` → Fixed, `refactor:` affecting behavior → Changed
  6. Write entries that explain the **value** — what users can now do, or what problem is solved. Lead with the user experience, not the implementation mechanism. If an entry reads like a commit message describing what the code does internally, rewrite it to describe what the user experiences. Consolidate related commits into single entries.
  7. Edit `CHANGELOG.md` to add the entries under `## [Unreleased]`
  8. Commit the changelog update

- **Not on main branch** → Show current branch, suggest switching
- **Behind origin/main** → Suggest `git pull`
- **Validation script errors** → Show the specific failures and suggest fixes

**Then review [Unreleased] changelog entries.** Whether entries were just auto-populated or already existed, review them against the changelog style guide:

1. Read `CHANGELOG.md` [Unreleased] section and `docs/guidance/changelog.md`
2. Apply the litmus test to each entry: *Would a spell user notice this change?* Remove entries that fail (dev scripts, internal tooling, template sync infra, docs unless user-facing).
3. Rewrite any entries that describe implementation mechanisms to lead with user value — what users can now do, or what problem is solved.
4. Commit any changes made.

**Then investigate all warnings.** The `--check` output summarizes pass/warn/fail per script but hides details. Run each validation script individually to see full warning output:

```bash
./dev/check-plugin-health.py --skip-changelog
./dev/check-platform-parity.py
```

For each warning found:
1. Read the relevant files to understand the issue
2. Fix it if straightforward (missing parity commands, etc.)
3. If the fix is non-trivial or ambiguous, explain the warning and ask the user how to proceed
4. Commit any fixes made

After fixing errors and addressing warnings, re-run `./dev/release.py --check` to confirm a clean bill of health.

### Path B: Version Number (interactive release)

If `$ARGUMENTS` matches a version number (e.g. `0.7.0`), optionally followed by `--dry-run` or `--push`:

1. Parse the version and any flags from `$ARGUMENTS`
2. Read the release-editor agent instructions:
   ```
   Read .claude/agents/release-editor.md
   ```
3. Follow the release-editor workflow from start to finish, using the parsed version. Pass through `--dry-run` or `--push` flags when executing the release script in step 5 of that workflow.

**IMPORTANT:** Run the workflow inline in this session — do NOT spawn a subagent. The release-editor is an interactive collaborator that needs dialogue with the user (changelog review, fix suggestions, push confirmation).

### Post-Release: Sync and Install

After a successful release (commit created and pushed), sync templates and install locally:

```bash
./dev/sync-commands.sh
./dev/install-claude-code.sh
```

Report the installed version to confirm it matches the release.

### Path C: Unrecognized Arguments

If `$ARGUMENTS` doesn't match any pattern above, show usage help:

```
Usage: /release [options]

  /release              Run pre-flight health checks
  /release 0.7.0        Start interactive release for version 0.7.0
  /release 0.7.0 --dry-run   Preview release without modifying files
  /release 0.7.0 --push      Prepare and push in one step
```
