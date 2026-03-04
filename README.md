# Sam's Spells

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/platforms-Claude%20Code%20%7C%20OpenCode%20%7C%20Kiro-blue.svg)](#installation)
[![Spells](https://img.shields.io/badge/spells-13-purple.svg)](#the-spells)

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
| **diagnose** | Bug that keeps coming back no matter what you try? Surveys all cause categories (fishbone brainstorm), then traces the most likely chain to the root cause before suggesting any fix. |
| **cause-map** | Problem with unknown, multiple, or recurring causes? Maps ALL possible causes across categories using fishbone (Ishikawa) diagrams, surfaces systemic issues, and prioritizes investigation. |
| **deep-dive** | New to a codebase with no docs and no one to ask? Systematically explores and maps the architecture, data flow, and key abstractions. |
| **prior-art** | About to build something from scratch? Surveys what already exists — libraries, tools, frameworks — so you don't reinvent the wheel. |
| **blind-spot** | Planning a migration and worried about what you're missing? Probes from five angles to surface hidden assumptions, failure modes, and perspectives nobody thought to consider. |
| **zoom-out** | Spent weeks on a direction and not sure it's the right one? Challenges a plan from five strategic lenses — reframing, inversion, opportunity cost, second-order effects, and upstream analysis — then forces a recommendation. |
| **handoff** | Session ending with half-finished work? Captures decisions, dead ends, current state, and next steps — or resumes from a previous handoff with verified context and a prioritized action plan. |

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
| Bug that keeps coming back after you "fix" it | **diagnose** |
| Need to understand why something fails, not just suppress the error | **diagnose** |
| Recurring incidents with different symptoms but unknown common cause | **cause-map** |
| Post-mortem: mapping all contributing factors to an incident | **cause-map** |
| New to a codebase and need to understand how it works | **deep-dive** |
| Exploring an unfamiliar module before making changes | **deep-dive** |
| About to build something — not sure if a library already does it | **prior-art** |
| Evaluating which tool or framework to adopt | **prior-art** |
| Planning a migration and worried about what you're not seeing | **blind-spot** |
| Making a big decision and want to stress-test your assumptions | **blind-spot** |
| Questioning whether you're solving the right problem | **zoom-out** |
| Invested heavily in a direction and want a strategic gut-check | **zoom-out** |
| Ending a session and need to capture context | **handoff** |
| Handing off work to a colleague or another AI session | **handoff** |
| Starting a new session with a handoff file waiting | **handoff** resume |
| "What does this spell even do?" | **teach** |

## Installation

### Claude Code

**From GitHub (recommended):**

Run these two commands inside Claude Code:

```
/plugin marketplace add smileynet/sams-genai-spells
/plugin install spell@sams-genai-spells
```

Start a new session (`/clear`) and run `/spell:help` to verify.

**Local install (for development):**

```bash
git clone https://github.com/smileynet/sams-genai-spells.git
cd sams-genai-spells
./dev/sync-commands.sh
./dev/install-claude-code.sh
```

Start a new Claude Code session and run `/spell:help` to see all commands.

To update a local install:

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
/spell:diagnose TypeError: Cannot read properties of undefined
/spell:deep-dive src/api/             # Explore and map the API module
/spell:deep-dive how does auth work?  # Trace how authentication is implemented
/spell:prior-art markdown parsing     # Survey existing solutions before building
/spell:blind-spot migrating to DynamoDB  # Find what you don't know you don't know
/spell:zoom-out rewrite as microservices # Are we solving the right problem?
/spell:handoff                        # Capture session context before ending
/spell:handoff resume HANDOFF.md      # Resume from a handoff file
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
- **[Systematic Diagnosis & Root Cause Analysis](docs/tutorials/diagnose.md)** -- Bug keeps coming back after you "fix" it? Categorical brainstorming plus hypothesis-driven tracing finds the real problem.
- **[Categorical Cause Decomposition & Fishbone Analysis](docs/tutorials/cause-map.md)** -- Recurring incidents with different root causes each time? Map the full cause landscape before investigating.
- **[Codebase Exploration & Program Comprehension](docs/tutorials/deep-dive.md)** -- New to a codebase with 200 files and no docs? Top-down reading strategy produces an architecture map, not just familiarity.
- **[Prior Art Search & Technology Evaluation](docs/tutorials/prior-art.md)** -- About to build something from scratch? Systematic survey of what already exists so you adopt, adapt, or build with full knowledge of the landscape.
- **[Blind Spot Detection & Pre-Mortem Analysis](docs/tutorials/blind-spot.md)** -- Planning a migration and worried about what you can't see? Pre-mortem, assumption surfacing, and cross-domain transfer probe systematically for what you don't know you don't know.
- **[Problem Framing & Strategic Thinking](docs/tutorials/zoom-out.md)** -- Spent weeks on a direction that might be wrong? Problem reframing, inversion, and second-order thinking challenge whether you're solving the right problem.
- **[Shift Handoff Protocols & Context Transfer](docs/tutorials/handoff.md)** -- Session ending with decisions still in your head? Structured handoff protocols from medicine, aviation, and military — adapted for software and AI sessions.

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
- **Fishbone (Ishikawa) diagrams**: Kaoru Ishikawa (1968), Seven Basic Quality Tools
- **Swiss Cheese Model**: James Reason, *Human Error* (1990)
- **5 Whys**: Taiichi Ohno, Toyota Production System (1950s)
- **Systematic debugging**: Andreas Zeller, *Why Programs Fail* (2009)
- **Fault tree analysis**: Bell Labs (1961)
- **Program comprehension**: von Mayrhauser & Vans (1995), Rajlich, Ko et al.
- **Architecture recovery**: Gail Murphy, reflexion models (1995)
- **Information hiding**: David Parnas (1972)
- **SBAR handoff protocol**: Kaiser Permanente (1990s), mandated by Joint Commission (2006)
- **Shift handoff protocols**: US Navy watch turnover, ICAO ATC handoff standards
- **Prior art search**: US Patent Act (1790), codified by patent offices worldwide
- **Systematic review**: Cochrane Collaboration (1993), PRISMA guidelines
- **Technology Radar**: ThoughtWorks (2010)
- **OSS health metrics**: CHAOSS / Linux Foundation (2017)
- **Pre-mortem analysis**: Gary Klein, *Sources of Power* (1998)
- **Strategic assumption surfacing (SAST)**: Richard Mason & Ian Mitroff (1981)
- **Johari Window**: Joseph Luft & Harrington Ingham (1955)
- **Authentic dissent research**: Charlan Nemeth (2001)
- **Black Swan theory**: Nassim Nicholas Taleb (2007)
- **Cynefin framework**: Dave Snowden (2007)
- **Structure-mapping theory**: Dedre Gentner (1983)
- **Problem framing**: Donald Schon, *The Reflective Practitioner* (1983)
- **Frame innovation**: Kees Dorst (2011/2015)
- **Problem reframing**: Thomas Wedell-Wedellsborg, HBR (2017)
- **Inversion as thinking tool**: Charlie Munger, via Carl Jacobi
- **Second-order thinking**: Howard Marks, *The Most Important Thing* (2011)
- **Ecolacy**: Garrett Hardin, *Filters Against Folly* (1985)
- **Upstream thinking**: Dan Heath, *Upstream* (2020)
- **Systems leverage points**: Donella Meadows (1997/2008)
- **Problem dissolution**: Russell Ackoff (1974)

I just made commands to use them.

## Contributing

Found a bug? Have a spell idea? [Open an issue](https://github.com/smileynet/sams-genai-spells/issues) or submit a PR.

If you're contributing code, see `CLAUDE.md` for the template system, file conventions, and dev workflow.

## License

MIT
