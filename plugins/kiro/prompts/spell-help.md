## Summary

**Show available spells with descriptions and usage examples.** Helps users discover and understand Sam's Spells.

**Arguments:** `$ARGUMENTS` (optional) - Spell name for detailed help

---

## Process

### Step 1: Check for Detailed Help Request

**If `$ARGUMENTS` provided:**
- Show detailed help for that specific spell
- Skip to Step 3

**Otherwise:**
- Show the full spell listing

### Step 2: Output Spell Listing

Output the help display:

```
╔════════════════════════════════════════════════════════════╗
║  SAM'S SPELLS - Quick Reference                           ║
╚════════════════════════════════════════════════════════════╝

MODIFIERS (change how the AI behaves)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@spell-idiomatic <tool>  Don't make stuff up — use canonical patterns
@spell-socratic [topic]  Teach through questions, not answers

WORKFLOWS (produce artifacts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@spell-bpap <topic>                     Structured do's, don'ts, and named antipatterns
@spell-progressive-disclosure <topic>   Break docs into linked files (by detail level)
@spell-diataxis <topic>                 Four-quadrant documentation (by purpose)
@spell-task-graph <tasks or process>    Map dependencies or diagram a workflow
@spell-debug <symptom>                 Systematic root cause analysis
@spell-deep-dive <path or question>   Explore and map how code works

META
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@spell-teach [spell]    Learn the concept behind any spell
@spell-help [spell]     You are here

TIPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Modifiers set session behavior — invoke once and keep working
• Workflows produce files — they'll ask questions, research, then output
• Use @spell-teach <spell> to learn the concept behind a spell
• Most spells accept arguments, or ask interactively if you skip them

For detailed help: @spell-help <spell>
```

### Step 3: Output Detailed Help (If Spell Specified)

**If `$ARGUMENTS` is a spell name:**

Read the command file to get its summary and process.

Output format for detailed help:

```
╔════════════════════════════════════════════════════════════╗
║  @spell-<spell> - <description>                       ║
╚════════════════════════════════════════════════════════════╝

WHAT IT DOES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Summary section from spell file>

USAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@spell-<spell> <arguments>

EXAMPLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Example invocations>

LEARN MORE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@spell-teach <spell>  — Learn the concept behind this spell

Back to overview: @spell-help
```

**Spell not found:**

```
Spell not found: <argument>

Available spells:
  Modifiers: idiomatic, socratic
  Workflows: bpap, progressive-disclosure, diataxis, task-graph, debug, deep-dive
  Meta: teach, help

Run @spell-help for overview.
```

---

## Spell Descriptions

| Spell | Type | Description |
|-------|------|-------------|
| `@spell-idiomatic` | Modifier | Set session constraints to use canonical, documented patterns for a tool or language |
| `@spell-socratic` | Modifier | Shift the AI into Socratic teaching mode — questions instead of answers |
| `@spell-bpap` | Workflow | Research and produce a structured best-practices and antipatterns document for a topic |
| `@spell-progressive-disclosure` | Workflow | Break documentation into linked, AI-friendly files at progressive detail levels |
| `@spell-diataxis` | Workflow | Generate or audit documentation using the four-quadrant Diataxis framework |
| `@spell-task-graph` | Workflow | Map task dependencies or diagram a workflow using DAGs and critical path analysis |
| `@spell-debug` | Workflow | Systematic root cause analysis — find the real bug before attempting fixes |
| `@spell-deep-dive` | Workflow | Explore and map how a codebase or subsystem works — architecture, data flow, and key abstractions |
| `@spell-teach` | Meta | Learn the real-world concept behind any spell — where it comes from, where you see it, how the spell applies it |
| `@spell-help` | Meta | Show this listing, or detailed help for a specific spell |

---

## Example Usage

```
@spell-help                    # Show all spells
@spell-help idiomatic          # Detailed help for idiomatic spell
@spell-help bpap                # Detailed help for bpap spell
```
