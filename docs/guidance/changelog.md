# Changelog Guide

> Track what's different between releases.

Guidelines for maintaining a clear, useful changelog. Based on [Keep a Changelog](https://keepachangelog.com) specification.

## Format

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature descriptions

### Changed
- Changes to existing functionality

### Fixed
- Bug fixes

## [1.0.0] - 2026-01-21

### Added
- Initial release features

[Unreleased]: https://github.com/smileynet/sams-genai-spells/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/smileynet/sams-genai-spells/releases/tag/v1.0.0
```

## Guiding Principles

**Changelogs are for humans, not machines.**

- Include an entry for every version
- Group same types of changes
- Make versions and sections linkable
- List latest version first
- Include release date
- Follow Semantic Versioning

## Types of Changes

Use these categories consistently:

- **Added** - New features
- **Changed** - Changes to existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Now removed features
- **Fixed** - Bug fixes
- **Security** - Vulnerability fixes

## Best Practices

### Write for Humans

**Do:**
- Use plain language
- Explain what changed and why
- Highlight user benefits
- Include examples when helpful

**Don't:**
- Use technical jargon without explanation
- Dump git commit logs
- Assume technical knowledge

**Example:**
```markdown
### Added
- **prior-art** spell — survey existing solutions before building
  (libraries, tools, frameworks, and patterns)
```

### Focus on User Value

Every changelog entry should answer one of two questions: **"What can users now do?"** or **"What problem does this solve?"** Lead with the value, not the implementation.

**Do:**
- Start with what changed for the user
- Explain _why_ this matters
- Use active language ("you can now...", "no longer crashes when...")

**Don't:**
- Lead with internal mechanism names
- List implementation details without explaining user impact
- Use jargon the user would need to read source code to understand

**Before (too technical):**
```markdown
### Changed
- bpap template uses three-phase research with numbered BP/AP sections
  and cross-references in few-shot examples
```

**After (user-value-focused):**
```markdown
### Changed
- `/spell:bpap` output is clearer and more actionable — best practices
  and antipatterns are now numbered for easy reference, and cross-references
  link related items together
```

**Litmus test:** Would a plugin user notice this change while using Sam's Spells in their project? If the answer is "only if they read the source code" or "only if they contribute to Sam's Spells," exclude it.

### Keep an Unreleased Section

Track upcoming changes at the top:

```markdown
## [Unreleased]

### Added
- New prior-art spell
- Handoff resume mode

### Fixed
- Help command box-drawing alignment
```

At release time, move Unreleased content to a new version section.

### Use ISO 8601 Dates

Format: `YYYY-MM-DD` (e.g., `2026-01-21`)

- Unambiguous across regions
- Sorts chronologically
- ISO standard

### Document All Notable Changes

**Include:**
- New features (Added)
- Breaking changes (Changed with note)
- Bug fixes (Fixed)
- Deprecations (Deprecated)
- Security fixes (Security)

**Exclude:**
- Whitespace changes
- Internal refactoring (unless user-visible)
- Documentation typos
- Development tooling updates

### Audience: Plugin Users

The changelog is for **plugin users** — people who install Sam's Spells into their editor and use its spells in their own projects. Filter every entry through this lens.

**Include** (user-facing plugin functionality):
- New user-invocable spells (slash commands)
- Changes to spell behavior that users interact with directly
- New workflow capabilities users can invoke
- Breaking changes to existing user-facing features
- Bug fixes users would encounter in their workflows

**Exclude** (internal/dev tooling):
- Developer-facing documentation (guidance docs, contributor patterns)
- Template syncing or build infrastructure (sync scripts)
- New dev scripts or tooling (`dev/`, `scripts/`)
- CI/workflow changes
- Documentation updates (unless user-facing spell docs)
- .beads/ changes (sync commits, metadata updates)
- Test-only changes (new/modified tests with no user-facing code change)
- Internal refactoring with no user impact

**Examples:**

Good (user value clear):
- `/spell:diagnose` now suggests hypothesis rankings so you fix the most likely cause first
- Running `/spell:help` shows spell type (modifier vs. workflow) in the listing

Bad (too technical / internal):
- "Action-level visibility tracking every tool call during iterations"
- "README restructured following Diataxis framework"
- "Template sync script handles Kiro frontmatter edge cases"

### Highlight Breaking Changes

Make breaking changes obvious:

```markdown
## [2.0.0] - 2026-02-01

### Changed
- **BREAKING**: Config format changed from YAML to JSON.
  See migration guide in docs/migration/v2.md
```

### Link Versions

Include comparison links at bottom:

```markdown
[Unreleased]: https://github.com/smileynet/sams-genai-spells/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/smileynet/sams-genai-spells/compare/v0.9.0...v1.0.0
[0.9.0]: https://github.com/smileynet/sams-genai-spells/releases/tag/v0.9.0
```

## Anti-patterns

### Commit Log Dumps

**Bad:**
```markdown
### Changed
- fix typo
- update deps
- refactor session manager
- merge PR #42
```

**Good:**
```markdown
### Changed
- Improved session cleanup reliability
- Updated dependencies for security patches
```

### Overly Technical Language

**Bad:**
```markdown
### Changed
- Refactored the worktree manager singleton to use dependency injection
  with interface-based polymorphism
```

**Good:**
```markdown
### Changed
- Improved worktree manager testability and flexibility
```

### Ignoring Deprecations

**Bad:**
```markdown
## [2.0.0] - 2026-02-01

### Removed
- Old config format (no warning in v1.x)
```

**Good:**
```markdown
## [1.5.0] - 2026-01-15

### Deprecated
- YAML config format. Use JSON instead. YAML support will be
  removed in v2.0.0. See docs/migration.md

## [2.0.0] - 2026-02-01

### Removed
- YAML config format (deprecated in v1.5.0)
```

### Sporadic Updates

**Bad:**
- Changelog last updated 6 months ago
- Multiple versions released without changelog entries
- Users discover changes by accident

**Good:**
- Changelog updated with every release
- Unreleased section kept current
- Updates are regular and predictable

### Lack of Visibility

**Bad:**
- Changelog buried in `docs/internal/`
- Not linked from README
- Hard to find

**Good:**
- Changelog lives in project root as `CHANGELOG.md`
- Linked from README
- Referenced in release notes

### Not Highlighting Value

**Bad:**
```markdown
### Changed
- Updated UI
```

**Good:**
```markdown
### Changed
- Redesigned task status UI for faster scanning. Status indicators
  now use color and icons, reducing time to identify blocked tasks.
```

### Inconsistent Formatting

**Bad:**
```markdown
### Added
New feature X

### Changed
- Improved Y
- Updated Z

### Fixed
Fixed bug in A. Also fixed B.
```

**Good:**
```markdown
### Added
- New feature X with detailed description

### Changed
- Improved Y for better performance
- Updated Z to support new use cases

### Fixed
- Bug in A causing crashes on timeout
- Bug in B preventing cleanup
```

## Sam's Spells-Specific Guidelines

### Spell Releases

When releasing new spells:

```markdown
## [0.6.0] - 2026-02-25

### Added
- **prior-art** spell — survey existing solutions before building
  (libraries, tools, frameworks, and patterns)
- **handoff** spell — write structured handoff documents for session
  and developer transitions
- Handoff resume mode — consume, verify, and act on existing handoff files
```

### Spell Behavior Changes

For changes to existing spells:

```markdown
## [Unreleased]

### Changed
- `/spell:bpap` output restructured for clarity — numbered sections and
  cross-references between related best practices and antipatterns
```

### Breaking Changes

Always document with migration path:

```markdown
## [2.0.0] - 2026-03-01

### Changed
- **BREAKING**: Spell namespace changed from `spell:` to `spells:`.
  Update your slash command usage accordingly.
```

## Maintenance

### Regular Updates

- Update the Unreleased section with each merged PR
- Create a version section on release
- Update comparison links at the bottom of the file
- Review entries for clarity before release

### Version Numbering

Follow [Semantic Versioning](https://semver.org):

- **MAJOR** (1.0.0 -> 2.0.0): Breaking changes
- **MINOR** (1.0.0 -> 1.1.0): New features (backward compatible)
- **PATCH** (1.0.0 -> 1.0.1): Bug fixes (backward compatible)

### Yanked Releases

If a release must be pulled:

```markdown
## [1.0.5] - 2026-01-20 [YANKED]

### Fixed
- Critical issue in session management

**Note**: This version was yanked due to a critical bug. Use 1.0.6 instead.
```

## Quick Checklist

Before releasing:

- [ ] All notable changes documented
- [ ] Changes categorized correctly
- [ ] User-friendly language used
- [ ] Breaking changes highlighted
- [ ] Version number set per SemVer
- [ ] Release date formatted as ISO 8601
- [ ] Comparison links updated
- [ ] Unreleased section cleared

## References

- [Keep a Changelog](https://keepachangelog.com) - Format specification
- [Semantic Versioning](https://semver.org) - Version numbering
- [Conventional Commits](https://conventionalcommits.org) - Commit format for automation

## Related

- [Release Editor Agent](../../.claude/agents/release-editor.md) - Interactive release coordinator that drafts and reviews changelogs
