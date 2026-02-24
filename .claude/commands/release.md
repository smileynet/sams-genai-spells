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
  3. **Filter for user-facing changes only.** The changelog is for plugin users — people who install Sam's Spells and use its commands. Apply this litmus test: *Would a spell user notice this change?* If only contributors or maintainers would notice, exclude it.
     - **Include:** New spells, changed spell behavior, new workflow capabilities, bug fixes users encounter, breaking changes
     - **Exclude:** Dev scripts, template syncing infra, CI/workflow changes, internal refactoring, beads sync commits, docs updates (unless user-facing command docs)
  4. Categorize: `feat:` → Added, `fix:` → Fixed, `refactor:` affecting behavior → Changed
  5. Write entries that explain the **value** — what users can now do, or what problem is solved. Consolidate related commits into single entries.
  6. Edit `CHANGELOG.md` to add the entries under `## [Unreleased]`
  7. Commit the changelog update

- **Not on main branch** → Show current branch, suggest switching
- **Behind origin/main** → Suggest `git pull`

After fixing errors and addressing warnings, re-run `./dev/release.py --check` to confirm a clean bill of health.

### Path B: Version Number (interactive release)

If `$ARGUMENTS` matches a version number (e.g. `0.6.0`), optionally followed by `--dry-run` or `--push`:

1. Parse the version and any flags from `$ARGUMENTS`
2. Run `./dev/release.py --check` first to verify readiness
3. If check fails, fix errors (follow Path A error handling)
4. Review the `[Unreleased]` section in `CHANGELOG.md`:
   - Is it complete? Are entries user-friendly?
   - Suggest improvements if needed, ask user to approve
5. Execute the release:
   ```bash
   ./dev/release.py <version> [--dry-run] [--push] --yes
   ```
6. Report what happened (versions updated, changelog transformed, commit created)

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
  /release 0.6.0        Start interactive release for version 0.6.0
  /release 0.6.0 --dry-run   Preview release without modifying files
  /release 0.6.0 --push      Prepare and push in one step
```
