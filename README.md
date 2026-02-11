# Sam's Spells

> Prompt engineering techniques packaged as reusable multi-platform AI commands.

Sam is not a prompt engineering genius. Sam just keeps stumbling into smart things other people figured out — idiomatic code, the Socratic method, Diataxis documentation — and has the good sense to write them down. These "spells" are well-known techniques that Sam packaged into buttons because he got tired of re-explaining them every session.

## The Spells

### Modifiers (change how the AI behaves)

| Spell | What it does |
|-------|-------------|
| **idiomatic** | "Don't make stuff up — use canonical patterns." Sets session constraints for a tool or language based on real docs, not hallucinated APIs. |
| **socratic** | "Teach through questions, not answers." Flips the AI from answer-mode to question-mode for actual learning. |

### Workflows (produce artifacts)

| Spell | What it does |
|-------|-------------|
| **best-practices** | Researches a topic and produces a structured do's-and-don'ts guide with sources. |
| **progressive-disclosure** | Breaks docs into linked files at progressive detail levels, sized for AI context windows. |
| **diataxis** | Generates, restructures, or audits documentation using Daniele Procida's four-quadrant framework. |

### Meta

| Command | What it does |
|---------|-------------|
| **help** | Lists all spells with descriptions and usage tips. |
| **teach** | Explains the technique behind any spell — who invented it, why it works, how to use it beyond this plugin. |

## Installation

### Claude Code

```bash
# Local install (from this repo)
./dev/sync-commands.sh
./dev/install-claude-code.sh
```

Then start a new Claude Code session and use `/spell:help` to see all commands.

### OpenCode

Copy the `plugins/opencode/` directory to your OpenCode plugins folder. Commands are prefixed with `spell-` (e.g., `/spell-help`).

### Kiro

Copy the `plugins/kiro/prompts/` directory to your Kiro project. Commands are prefixed with `@spell-` (e.g., `@spell-help`).

## Usage

```
/spell:help                           # See all spells
/spell:idiomatic Python 3.12          # Set idiomatic Python constraints
/spell:socratic React hooks           # Learn React hooks through questions
/spell:best-practices TypeScript      # Get a structured best-practices guide
/spell:progressive-disclosure src/    # Break docs into linked files
/spell:diataxis audit docs/           # Audit docs against Diataxis framework
/spell:teach diataxis                 # Learn about the Diataxis technique
```

## How It Works

Each spell is a markdown template in `core/templates/commands/`. The sync script (`dev/sync-commands.sh`) generates platform-specific versions for Claude Code, OpenCode, and Kiro — handling namespace differences, conditional blocks, and frontmatter.

```
core/templates/commands/       → Single source of truth
  ↓ dev/sync-commands.sh
plugins/claude-code/commands/  → /spell:command
plugins/opencode/commands/     → /spell-command
plugins/kiro/prompts/          → @spell-command
```

## Learning the Techniques

These spells aren't magic — they're packaging. If you want to understand why they work (and use the techniques beyond this plugin), check out:

- `docs/tutorials/idiomatic.md` — Idiomatic code and why AI needs constraints
- `docs/tutorials/socratic.md` — The Socratic method, from 400 BC to AI tutoring
- `docs/tutorials/best-practices.md` — Structured technical writing
- `docs/tutorials/progressive-disclosure.md` — J.M. Keller's progressive disclosure in docs
- `docs/tutorials/diataxis.md` — Daniele Procida's documentation framework

Or just run `/spell:teach <spell-name>` and let the AI explain it.

## Credits

Sam didn't invent any of these techniques. Credit goes to:
- The concept of **idiomatic code** — every programming language community ever
- **Socratic method** — Socrates (~400 BC), refined by educators for millennia
- **Best practices documentation** — the entire field of technical writing
- **Progressive disclosure** — J.M. Keller (1983), popularized by Nielsen Norman Group
- **Diataxis** — Daniele Procida ([diataxis.fr](https://diataxis.fr/))

Sam just put them in buttons.

## License

MIT
