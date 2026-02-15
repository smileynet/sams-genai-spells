# Changelog

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
