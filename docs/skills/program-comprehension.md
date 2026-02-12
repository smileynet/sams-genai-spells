# Program Comprehension — Skill Reference for AI Assistants

> Techniques for reading and understanding code systematically. Use this reference when exploring unfamiliar codebases, mapping module architecture, or answering questions about how code works.

## Reading Strategies

### Top-Down (Recommended Default)

Start at the highest level of abstraction and drill down as needed.

1. **Find entry points** — Exports, public APIs, route handlers, main functions, CLI commands
2. **Read the public surface** — What does this module expose? What can callers do with it?
3. **Follow calls inward** — Trace from public API through internal modules. Stop when you understand enough to answer the question.
4. **Read implementation only as needed** — Internal helper functions, utility code, and private methods only when the call chain passes through them.

**Best for:** Exploring unfamiliar code, answering "how does X work?" questions, onboarding to a new codebase.

**Why it works:** Entry points are the system's contract with the outside world. Understanding the contract first gives you a framework to organize everything else you learn.

### Bottom-Up

Start at a specific location and trace outward.

1. **Start at the code in question** — A specific file, function, or class
2. **Trace callers** — Who calls this? Find all references.
3. **Trace callees** — What does this depend on? Follow imports.
4. **Build outward** — Expand the boundary until you understand the module's role in the system.

**Best for:** Debugging a specific function, understanding a single file's role, change impact analysis.

### As-Needed (Opportunistic)

Read only what's required to answer a specific question.

1. **Define the question precisely** — "What happens when a user clicks 'submit'?"
2. **Find the starting point** — The submit handler
3. **Trace only the relevant path** — Ignore branches that don't relate to the question
4. **Stop when answered** — Don't explore further than the question requires

**Best for:** Targeted questions, code review of specific changes, quick investigations.

## Expert vs. Novice Code Reading

| Dimension | Novice Pattern | Expert Pattern |
|-----------|---------------|----------------|
| **Starting point** | Starts at line 1, reads sequentially | Starts at entry points, reads selectively |
| **Navigation** | Follows file order | Follows call chains and data flow |
| **Focus** | Reads every line | Skips implementation details, focuses on structure |
| **Abstraction** | Tries to understand every function | Identifies key abstractions, treats others as black boxes |
| **Mental model** | Builds bottom-up from details | Builds top-down from architecture |
| **Questions** | "What does this line do?" | "What role does this module play?" |
| **Stopping** | Reads until done or overwhelmed | Reads until the question is answered |

## Mental Model Building

### What to Identify First

In priority order:

1. **Entry points** — How does the outside world interact with this system?
2. **Data types** — What are the key types, interfaces, or schemas? These define the system's vocabulary.
3. **Module boundaries** — What's inside this system vs. outside? What are the dependencies?
4. **Data flow** — Where does data enter, how is it transformed, where does it go?
5. **Control flow** — What triggers what? Events, callbacks, middleware chains.
6. **Invariants** — What must always be true? Constraints, validations, type guards.

### Signals That Reveal Architecture

| Signal | What it reveals |
|--------|-----------------|
| Directory structure | Module boundaries, feature organization, layer separation |
| Import patterns | Dependency direction, coupling between modules |
| Naming conventions | Roles (Controller, Service, Repository), patterns (Handler, Factory, Middleware) |
| Type definitions | The system's vocabulary, data shapes, contracts between modules |
| Configuration files | Frameworks, build tools, environment requirements |
| Test structure | What the developers consider units vs. integration, what's tested heavily |
| README / docs | Intended architecture, setup instructions, design decisions |
| Package.json / Cargo.toml / go.mod | External dependencies, project metadata |

## Scope Limiting

### When to Go Deeper

- The entry point delegates to an internal module you don't understand
- A key data transformation happens in a function you haven't read
- The control flow branches in a way that affects the answer to the original question
- A type definition is central to understanding the system

### When to Stop

- You can explain what the system does, how it's organized, and how data flows through it
- The remaining unread code is implementation detail that doesn't change the high-level picture
- You've answered the original question
- Going deeper would require understanding a separate system (follow-up exploration, not this one)

### Scope Thresholds

| File count | Recommendation |
|------------|---------------|
| 1-10 files | Read all of them. Comprehensive analysis is feasible. |
| 10-30 files | Read entry points and key abstractions. Skim the rest. |
| 30+ files | Narrow scope. Ask the user which subsystem to focus on. |

## Reporting Template

Use this structure for exploration results:

```
DEEP DIVE: <SUBJECT>
══════════════════════════════════════════════════════════════

OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<2-3 sentence summary>

ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Mermaid diagram>

KEY FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <file:line> — <role>

DATA FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Entry → <step> → <step> → Output

DESIGN DECISIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Pattern> — <why it matters>

ENTRY POINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <How to invoke/test>
```
