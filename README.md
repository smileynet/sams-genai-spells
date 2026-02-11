# Sam's Spells

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/platforms-Claude%20Code%20%7C%20OpenCode%20%7C%20Kiro-blue.svg)](#installation)
[![Spells](https://img.shields.io/badge/spells-6-purple.svg)](#the-spells)

> Prompt engineering techniques packaged as reusable multi-platform AI commands.

Sam is not a prompt engineering genius. Sam just keeps stumbling into smart things other people figured out — idiomatic code, the Socratic method, Diataxis documentation — and has the good sense to write them down. These "spells" are well-known techniques that Sam packaged into buttons because he got tired of re-explaining them every session.

## What It Looks Like

**Modifier** — invoke once, changes the session:

```
> /spell:idiomatic Python 3.12

IDIOMATIC MODE: PYTHON 3.12
══════════════════════════════════════════════════════════════

Version: 3.12
Source: https://docs.python.org/3.12/

SESSION CONSTRAINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE (canonical patterns):
• pathlib.Path over os.path — modern path handling
• match/case for structural pattern matching — added in 3.10
• f-strings over .format() — cleaner, faster
• type hints with built-in generics (list[int] not List[int]) — PEP 585

AVOID (deprecated or non-idiomatic):
• os.path.join() → Use pathlib.Path / operator instead
• typing.List, typing.Dict → Use built-in list[], dict[] generics
• implicit string concatenation → Use f-strings or explicit +

These constraints are active for the rest of this session.
```

**Workflow** — runs research, produces structured output:

```
> /spell:best-practices Git commit messages

BEST PRACTICES: GIT COMMIT MESSAGES
══════════════════════════════════════════════════════════════

Source: Built-in knowledge + https://cbea.ms/git-commit/

DO ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Use imperative mood in subject line — "Add feature" not "Added feature"
2. Keep subject to 50 characters — forces concise summary
3. Separate subject from body with blank line — tools depend on this
4. Wrap body at 72 characters — readable in terminal and git log

DON'T ✗
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Don't end subject with period — it's a title, not a sentence
2. Don't use "fix bug" or "update code" — say what and why
3. Don't put everything in the subject — use the body for detail
```

## The Spells

**Modifiers** change how the AI behaves for the rest of the session. Invoke once, then keep working — the constraints stick.

| Spell | What it does |
|-------|-------------|
| **idiomatic** | "Don't make stuff up — use canonical patterns." Sets session constraints for a tool or language based on real docs, not hallucinated APIs. |
| **socratic** | "Teach through questions, not answers." Flips the AI from answer-mode to question-mode for actual learning. |

**Workflows** run research and produce structured artifacts. They ask clarifying questions, do the work, and output results.

| Spell | What it does |
|-------|-------------|
| **best-practices** | Researches a topic and produces a structured do's-and-don'ts guide with sources. |
| **progressive-disclosure** | Breaks docs into linked files at progressive detail levels, sized for AI context windows. |
| **diataxis** | Generates, restructures, or audits documentation using Daniele Procida's four-quadrant framework. |
| **task-graph** | Maps task dependencies into execution order, or diagrams process workflows. Uses DAGs, topological sort, and critical path analysis. |

### Meta

| Command | What it does |
|---------|-------------|
| **help** | Lists all spells with descriptions and usage tips. |
| **teach** | Explains the technique behind any spell — who invented it, why it works, how to use it beyond this plugin. |

### When to Use Which

| Situation | Spell |
|-----------|-------|
| Starting work with an unfamiliar framework | **idiomatic** |
| AI keeps hallucinating APIs that don't exist | **idiomatic** |
| Want to actually learn something, not just get an answer | **socratic** |
| Onboarding someone (including yourself) to a new topic | **socratic** |
| Need a quick reference for what to do and not do | **best-practices** |
| Writing docs for a codebase that has none | **progressive-disclosure** or **diataxis** |
| Existing docs are a mess and need restructuring | **diataxis** |
| Planning a project with lots of moving parts | **task-graph** |
| Need to figure out what to parallelize | **task-graph** |
| "What does this spell even do?" | **teach** |

## Installation

### Claude Code

```bash
# Clone the repo
git clone https://github.com/smileynet/sams-genai-spells.git
cd sams-genai-spells

# Sync templates and install
./dev/sync-commands.sh
./dev/install-claude-code.sh
```

Start a new Claude Code session and run `/spell:help` to see all commands.

To update later:

```bash
cd sams-genai-spells && git pull && ./dev/sync-commands.sh && ./dev/install-claude-code.sh
```

### OpenCode

```bash
git clone https://github.com/smileynet/sams-genai-spells.git
```

Copy the `plugins/opencode/` directory to your OpenCode plugins folder. Commands are prefixed with `spell-` (e.g., `/spell-help`).

### Kiro

```bash
git clone https://github.com/smileynet/sams-genai-spells.git
```

Copy the `plugins/kiro/prompts/` directory to your Kiro project. Commands are prefixed with `@spell-` (e.g., `@spell-help`).

## Usage

```
/spell:help                           # See all spells
/spell:idiomatic Python 3.12          # Set idiomatic Python constraints
/spell:socratic React hooks           # Learn React hooks through questions
/spell:best-practices TypeScript      # Get a structured best-practices guide
/spell:progressive-disclosure src/    # Break docs into linked files
/spell:diataxis audit docs/           # Audit docs against Diataxis framework
/spell:task-graph design, implement, test, deploy  # Map task dependencies
/spell:task-graph process for code review          # Diagram a workflow
/spell:teach diataxis                 # Learn about the Diataxis technique
```

## Learn the Techniques

These spells aren't magic — they're packaging. If you want to understand why they work (and use the techniques beyond this plugin), the [tutorials](docs/) go deep:

- **[Idiomatic Code](docs/tutorials/idiomatic.md)** — Why "the community's way" beats "your way," and why AI especially needs guardrails
- **[The Socratic Method](docs/tutorials/socratic.md)** — From 400 BC Athens to AI tutoring: teaching through questions
- **[Best Practices](docs/tutorials/best-practices.md)** — The art of writing down what works (and what doesn't) so nobody has to learn it twice
- **[Progressive Disclosure](docs/tutorials/progressive-disclosure.md)** — J.M. Keller's insight: show the simple thing first, reveal complexity on demand
- **[Diataxis](docs/tutorials/diataxis.md)** — Daniele Procida's framework that makes you feel foolish for not thinking of it yourself
- **[Task Graphs](docs/tutorials/task-graph.md)** — DAGs, critical paths, and the 1957 DuPont method that shaved months off construction schedules

Or just run `/spell:teach <spell-name>` and let the AI explain it.

## Credits

Sam didn't invent any of these techniques. Credit goes to:
- The concept of **idiomatic code** — every programming language community ever
- **Socratic method** — Socrates (~400 BC), refined by educators for millennia
- **Best practices documentation** — the entire field of technical writing
- **Progressive disclosure** — J.M. Keller (1983), popularized by Nielsen Norman Group
- **Diataxis** — Daniele Procida ([diataxis.fr](https://diataxis.fr/))
- **Critical Path Method** — James Kelley & Morgan Walker (1957, DuPont)
- **Topological sorting** — Arthur Kahn (1962)

Sam just put them in buttons.

## Contributing

Found a bug? Have a spell idea? [Open an issue](https://github.com/smileynet/sams-genai-spells/issues) or submit a PR.

If you're contributing code, see `CLAUDE.md` for the template system, file conventions, and dev workflow.

## License

MIT
