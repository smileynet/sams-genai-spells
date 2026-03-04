# Changelog

## [Unreleased]

### Added
- **doc-audit** spell — analyze existing docs for gaps, mixed concerns, and structural issues using Diataxis, progressive disclosure, and ROT analysis
- **doc-restructure** spell — reorganize existing docs by purpose (Diataxis quadrants) and detail level (progressive disclosure) using incremental strangler fig approach
- **doc-generate** spell — research a topic and create structured documentation with audience analysis, quadrant-specific writing rules, and quality gates
- Skill reference: `docs/skills/diataxis-framework.md` — four-quadrant classification framework
- Skill reference: `docs/skills/progressive-disclosure-framework.md` — depth layering framework

### Changed
- **doc-structure ritual** updated: now sequences `doc-audit → doc-restructure` (was `diataxis → progressive-disclosure`), now plan-mode compatible
- **progressive-disclosure** and **diataxis** demoted from spells to skill references — their frameworks now inform the three new doc spells

### Removed
- **progressive-disclosure** spell — replaced by doc-audit, doc-restructure, and doc-generate
- **diataxis** spell — replaced by doc-audit, doc-restructure, and doc-generate

## [0.7.0] - 2026-03-03
### Added
- **blind-spot** spell — surface hidden assumptions, failure modes, and missing perspectives you haven't considered
- **zoom-out** spell — challenge a plan or direction from five strategic lenses before committing to implementation
- **cause-map** spell — map all possible causes of a problem using fishbone (Ishikawa) categorical decomposition with evidence grading and cross-reference analysis

### Changed
- **debug → diagnose** — renamed to avoid conflict with Claude Code's built-in `/debug` command
- **diagnose** spell now surveys all plausible cause categories before drilling into the most likely chain, giving a broader view of potential root causes
- **bpap** output is clearer and more actionable — best practices and antipatterns are now numbered for easy reference, and cross-references link related items together

## [0.6.0] - 2026-02-25
### Added
- **prior-art** spell — survey existing solutions before building (libraries, tools, frameworks, and patterns)
- **handoff** spell — write structured handoff documents for session and developer transitions
- Handoff resume mode — consume, verify, and act on existing handoff files
- Remote install instructions in README for one-liner setup

### Fixed
- Help command box-drawing alignment across all platforms
- Missing debug and deep-dive rows in Kiro README

## [0.5.1] - 2026-02-14

### Fixed
- **OpenCode & Kiro reliability** — debug, deep-dive, and task-graph spells now load skill files by explicit path instead of vague directory hints, fixing failures on non-Claude-Code platforms
- **Help descriptions** — progressive-disclosure and diataxis one-liners now clearly distinguish the two spells
- **Help command** — replaced fragile bash script for command lookup with plain English instructions

### Changed
- **bpap** — documented that output can be saved to a file on request
- **Install script** — uses official Claude Code CLI for marketplace registration and plugin install

## [0.5.0] - 2026-02-11

### Added
- **deep-dive** spell — codebase exploration and program comprehension using top-down reading strategy, architecture mapping, and structured reporting
- Skill reference docs for program comprehension and architecture patterns (`docs/skills/`)
- Tutorial for deep-dive concept (`docs/tutorials/deep-dive.md`)

## [0.4.0] - 2026-02-11

### Added
- **debug** spell — systematic root cause analysis using 5 Whys, fault tree analysis, and hypothesis-driven debugging
- Skill reference docs for root cause analysis and debugging antipatterns (`docs/skills/`)
- Tutorial for debug concept (`docs/tutorials/debug.md`)

## [0.3.0] - 2026-02-11

### Changed
- **best-practices → bpap** — renamed spell to Best Practices & Antipatterns
- Added ANTIPATTERNS section with named patterns, trap analysis ("Why it's tempting"), consequences, and refactored solutions
- Reduced DON'T items from 5-7 to 3-5 to make room for the richer antipattern format
- Added antipattern-specific web search queries to research step
- Updated tutorial with "Antipatterns vs. Don'ts" section and Brown et al. reference

## [0.2.0] - 2026-02-10

### Added
- **task-graph** spell — maps task dependencies (DAG + topological sort + critical path) or diagrams process workflows (Mermaid flowcharts)
- Skill reference docs in `docs/skills/` — reusable AI knowledge for DAG analysis, topological sorting, and Mermaid flowcharts
- Tutorial for task-graph concept (`docs/tutorials/task-graph.md`)

## [0.1.0] - 2026-02-10

First release. Sam finally stopped re-typing the same prompting tricks and made them into buttons.

### Added
- **idiomatic** spell — sets session constraints for canonical tool/language patterns
- **socratic** spell — shifts AI into Socratic questioning mode
- **best-practices** spell — researches and produces structured do's-and-don'ts guides
- **progressive-disclosure** spell — breaks docs into linked files at progressive detail levels
- **diataxis** spell — generates, restructures, or audits documentation using the Diataxis framework
- **help** command — lists all spells with descriptions
- **teach** command — explains the concept behind any spell
- Multi-platform support: Claude Code (`/spell:command`), OpenCode (`/spell-command`), Kiro (`@spell-command`)
- Template sync pipeline (`dev/sync-commands.sh`)
- Local Claude Code install script (`dev/install-claude-code.sh`)
- Tutorial docs for all five concepts (`docs/tutorials/`)

[Unreleased]: https://github.com/smileynet/sams-genai-spells/compare/v0.7.0...HEAD
[0.7.0]: https://github.com/smileynet/sams-genai-spells/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/smileynet/sams-genai-spells/compare/v0.5.1...v0.6.0
[0.5.1]: https://github.com/smileynet/sams-genai-spells/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/smileynet/sams-genai-spells/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/smileynet/sams-genai-spells/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/smileynet/sams-genai-spells/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/smileynet/sams-genai-spells/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/smileynet/sams-genai-spells/releases/tag/v0.1.0
