# Sam's Spells

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/platforms-Claude%20Code%20%7C%20OpenCode%20%7C%20Kiro-blue.svg)](#installation)
[![Spells](https://img.shields.io/badge/spells-8-purple.svg)](#the-spells)

> Real-world concepts from programming, education, and design — packaged as AI commands.

These aren't prompt engineering techniques I invented. They're established concepts from real fields — idiomatic code (programming), the Socratic method (education), progressive disclosure (UX design), Diataxis (documentation theory), task graphs (operations research), systematic debugging (reliability engineering), program comprehension (software engineering). I just got tired of re-explaining them every session and made commands to use them.

## What It Looks Like

**Modifier** -- you invoke it once, and it changes the whole session:

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

**Workflow** -- does research and gives you something concrete:

```
> /spell:bpap Git commit messages

BEST PRACTICES & ANTIPATTERNS: GIT COMMIT MESSAGES
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

ANTIPATTERNS ⚠
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE KITCHEN SINK — Unrelated changes lumped into one commit
   Why it's tempting: You're "almost done" and don't want to split work
   Consequences: Impossible to revert one change without losing others
   Instead: One logical change per commit, use interactive staging
```

## The Spells

**Modifiers** change how the AI behaves for the rest of the session. You invoke one, then keep working. The constraints stick.

| Spell | What it does |
|-------|-------------|
| **idiomatic** | AI keeps hallucinating APIs that don't exist? Sets session constraints based on real docs and canonical patterns, not guesswork. |
| **socratic** | Want to actually learn, not just get an answer? Flips the AI into question-mode so you reason through problems yourself. |

**Workflows** do research and produce actual output. They'll ask you questions first, then go do the work.

| Spell | What it does |
|-------|-------------|
| **bpap** | Need a quick reference for what to do and not do? Researches a topic and produces structured do's, don'ts, and named antipatterns with trap analysis. |
| **progressive-disclosure** | Docs too big for AI context, or too disorganized for anyone? Breaks them into linked files at progressive detail levels. |
| **diataxis** | Docs that try to be everything at once? Audits, restructures, or generates docs using the four-quadrant Diataxis framework. |
| **task-graph** | Twelve tasks and no idea what to start first? Maps dependencies into execution order with parallel waves and critical path analysis. |
| **debug** | Bug that keeps coming back no matter what you try? Traces the causal chain to the root cause before suggesting any fix. |
| **deep-dive** | New to a codebase with no docs and no one to ask? Systematically explores and maps the architecture, data flow, and key abstractions. |

### Meta

| Command | What it does |
|---------|-------------|
| **help** | Lists all spells with descriptions and usage tips. |
| **teach** | Learn the real-world concept behind any spell — where it comes from, where you already see it, how the spell applies it. |

### When to Use Which

| Situation | Spell |
|-----------|-------|
| Starting work with an unfamiliar framework | **idiomatic** |
| AI keeps hallucinating APIs that don't exist | **idiomatic** |
| Want to actually learn something, not just get an answer | **socratic** |
| Onboarding someone (including yourself) to a new topic | **socratic** |
| Need a quick reference for what to do and not do | **bpap** |
| Writing docs for a codebase that has none | **progressive-disclosure** or **diataxis** |
| Existing docs are a mess and need restructuring | **diataxis** |
| Planning a project with lots of moving parts | **task-graph** |
| Need to figure out what to parallelize | **task-graph** |
| Bug that keeps coming back after you "fix" it | **debug** |
| Need to understand why something fails, not just suppress the error | **debug** |
| New to a codebase and need to understand how it works | **deep-dive** |
| Exploring an unfamiliar module before making changes | **deep-dive** |
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
/spell:bpap TypeScript                # Get a structured best-practices and antipatterns guide
/spell:progressive-disclosure src/    # Break docs into linked files
/spell:diataxis audit docs/           # Audit docs against Diataxis framework
/spell:task-graph design, implement, test, deploy  # Map task dependencies
/spell:task-graph process for code review          # Diagram a workflow
/spell:debug TypeError: Cannot read properties of undefined
/spell:deep-dive src/api/             # Explore and map the API module
/spell:deep-dive how does auth work?  # Trace how authentication is implemented
/spell:teach diataxis                 # Learn the concept behind Diataxis
```

## Learn the Concepts

These spells aren't magic. They're packaging. Each one applies an established concept from a real field — and the concepts are worth knowing whether you use this plugin or not. The [tutorials](docs/) go deep:

- **[Idiomatic Code](docs/tutorials/idiomatic.md)** -- AI hallucinating APIs? Code that compiles but fails review? Constraining to documented patterns fixes both.
- **[The Socratic Method](docs/tutorials/socratic.md)** -- Keep asking the AI the same question because you never learned the answer? Guided questions build understanding that sticks.
- **[Best Practices & Antipatterns](docs/tutorials/bpap.md)** -- Team knowledge trapped in Slack threads and tribal memory? The do/don't format plus named antipatterns make it scannable, durable, and transferable.
- **[Progressive Disclosure](docs/tutorials/progressive-disclosure.md)** -- Docs too big for AI context, or too disorganized for anyone? Layered files let readers (and AI) load only what they need.
- **[The Diataxis Framework](docs/tutorials/diataxis.md)** -- Docs that try to be everything at once and serve nobody? Four quadrants separate tutorials, how-tos, reference, and explanation.
- **[Task Graphs, Critical Paths, and Topological Sort](docs/tutorials/task-graph.md)** -- Twelve tasks and no idea what to start first? DAGs and critical paths turn chaos into execution order.
- **[Systematic Debugging & Root Cause Analysis](docs/tutorials/debug.md)** -- Bug keeps coming back after you "fix" it? Hypothesis-driven debugging traces the causal chain to the real problem.
- **[Codebase Exploration & Program Comprehension](docs/tutorials/deep-dive.md)** -- New to a codebase with 200 files and no docs? Top-down reading strategy produces an architecture map, not just familiarity.

Or just run `/spell:teach <spell-name>` and let the AI explain it.

## Credits

I didn't invent any of these techniques. Credit where it's due:
- **Idiomatic code**: every programming language community ever
- **Socratic method**: Socrates, ~400 BC. Refined by educators for millennia.
- **Best practices documentation**: the entire field of technical writing
- **Antipatterns**: Brown, Malveau, McCormick & Mowbray, *AntiPatterns* (1998)
- **Progressive disclosure**: J.M. Keller (1983), popularized by Nielsen Norman Group
- **Diataxis**: Daniele Procida ([diataxis.fr](https://diataxis.fr/))
- **Critical Path Method**: James Kelley & Morgan Walker (1957, DuPont)
- **Topological sorting**: Arthur Kahn (1962)
- **5 Whys**: Taiichi Ohno, Toyota Production System (1950s)
- **Systematic debugging**: Andreas Zeller, *Why Programs Fail* (2009)
- **Fault tree analysis**: Bell Labs (1961)
- **Program comprehension**: von Mayrhauser & Vans (1995), Rajlich, Ko et al.
- **Architecture recovery**: Gail Murphy, reflexion models (1995)
- **Information hiding**: David Parnas (1972)

I just made commands to use them.

## Contributing

Found a bug? Have a spell idea? [Open an issue](https://github.com/smileynet/sams-genai-spells/issues) or submit a PR.

If you're contributing code, see `CLAUDE.md` for the template system, file conventions, and dev workflow.

## License

MIT
