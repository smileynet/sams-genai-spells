---
description: Run a multi-spell ritual — orchestrated sequences that combine spells for greater effect
allowed-tools: Bash, Read, Write, Glob, Grep, Task, AskUserQuestion, WebFetch, WebSearch
---

## Summary

**Orchestrate multiple spells into a ritual — a sequenced workflow where each spell's output feeds the next.** Rituals preserve each spell's full process while automating the bridge between them. Each spell runs at full strength; the ritual adds selective context transfer and synthesis.

**Arguments:** `$ARGUMENTS` (required) - Ritual name followed by topic. Use `list` to see available rituals.

---

## Process

### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty or `$ARGUMENTS` is `list`:**
Output the ritual listing and stop:

```
SPELL RITUALS
══════════════════════════════════════════════════════════════

Rituals combine spells for greater effect. Each spell runs at
full strength — the ritual adds context bridges and synthesis.

SEQUENTIAL (A's output feeds B)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/spell:ritual landscape <topic>       prior-art → bpap
  Survey solutions, then codify practices from findings

/spell:ritual architect <path/topic>  deep-dive → task-graph
  Map architecture, then plan work on it

/spell:ritual investigate <problem>   cause-map → diagnose
  Map all causes, then trace the top one to root

/spell:ritual doc-structure <topic>   diataxis → progressive-disclosure
  Audit docs by purpose, then layer by detail level
  ⚠ Requires edit mode (both spells produce files)

PARALLEL (independent analyses, then synthesize)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/spell:ritual challenge <plan>        blind-spot + zoom-out
  Comprehensive stress-test from two angles

/spell:ritual survey <topic>          prior-art + deep-dive
  External solutions + internal architecture

TRIPLES (parallel + sequential)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/spell:ritual full-landscape <topic>  prior-art + deep-dive → bpap
  Complete picture: external, internal, then codify

/spell:ritual risk-map <plan>         blind-spot + zoom-out → cause-map
  Stress-test, then map all risks found

TIPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Each spell runs its full process — rituals don't dilute spells
• Bridge checkpoints let you approve, modify, or skip between steps
• Synthesis identifies convergence, divergence, and emergent insights
• Use individual spells when you need one perspective, rituals when you need the combination
```

**If `$ARGUMENTS` starts with a ritual name:**
- Extract the ritual name and the remaining topic
- Continue to Step 2

**Valid ritual names:** `landscape`, `architect`, `investigate`, `doc-structure`, `challenge`, `survey`, `full-landscape`, `risk-map`

**If the ritual name is not recognized:**

```
Unknown ritual: <name>

Available rituals: landscape, architect, investigate, doc-structure,
challenge, survey, full-landscape, risk-map

Run /spell:ritual list for descriptions.
```

**If the topic is empty after the ritual name:**
Use **AskUserQuestion** to ask: "What topic should this ritual analyze?"
Provide 2-3 contextual suggestions based on the current codebase.

### Step 2: Load Ritual Definition

Use **Read** to load the ritual definition file from the plugin's ritual directory. The file is at `core/rituals/<ritual-name>.md` relative to the repository root.

If running from an installed plugin, check these paths in order:
1. `core/rituals/<ritual-name>.md` (repo development)
2. The `rituals/` directory that is a sibling to the `commands/` directory containing this command file

If the ritual definition file cannot be found, report the error and stop.

### Step 3: Check Plan Mode Compatibility

Read the **Plan mode** field from the ritual definition.

**If the ritual is NOT plan-mode compatible** (currently only `doc-structure`):
Report to the user:

```
⚠ The <ritual-name> ritual requires edit mode.

<Explanation from the ritual definition about why — e.g., both spells produce files>

To proceed:
1. Exit plan mode
2. Re-run /spell:ritual <ritual-name> <topic>
```

Stop execution.

**Otherwise:** Continue.

### Step 4: Announce and Begin

Output the ritual header:

```
RITUAL: <NAME>
══════════════════════════════════════════════════════════════

Topic: <user's topic>
Spells: <spell sequence from ritual definition>
Type: <sequential | parallel | triple>

Starting Phase 1...
```

### Step 5: Execute the Ritual

Follow the ritual definition's phases exactly:

---

**For sequential rituals** (landscape, architect, investigate, doc-structure):

1. **Phase 1:** Execute spell A with the user's topic
   - Run the spell's full process as if the user invoked it directly
   - The spell template is loaded via Read from the commands directory
   - Do NOT modify the spell's behavior — it runs identically to standalone invocation

2. **Bridge:** After spell A completes:
   - Extract the specific sections named in the bridge definition
   - Reframe the extracted content as input for spell B
   - Apply the gate check — if the gate condition triggers a stop, report and stop
   - **User checkpoint:** Present the bridge content to the user
   Use **AskUserQuestion** with the checkpoint options from the ritual definition:
   - "Proceed" — Continue with spell B using the bridge framing
   - "Modify" — User adjusts the framing before continuing
   - "Skip to synthesis" — Skip spell B, synthesize from spell A alone
   - "Redirect" — User chooses a different spell instead

3. **Phase 2:** Execute spell B with the reframed topic from the bridge
   - Run the spell's full process as if the user invoked it directly

4. **Synthesis:** After spell B completes, produce the ritual synthesis (Step 6)

---

**For parallel rituals** (challenge, survey):

1. **Phase 1:** Execute both spells sequentially with the user's topic (their inputs are independent, but execution is one at a time)
   - Run spell A's full process first
   - Then run spell B's full process
   - Each spell receives the original topic directly — no bridging between them

2. **Synthesis:** After both spells complete, produce the ritual synthesis (Step 6)

---

**For triple rituals** (full-landscape, risk-map):

1. **Phase 1:** Execute the independent spells sequentially (independent inputs, serial execution)
   - Run spell A's full process first
   - Then run spell B's full process
   - Each receives the original topic directly

2. **Bridge:** After both parallel spells complete:
   - Extract the specific sections named in the bridge definition from BOTH outputs
   - Reframe the combined extracted content as input for spell C
   - Apply the gate check
   - **User checkpoint:** Present the bridge content (same options as sequential)

3. **Phase 2:** Execute spell C with the reframed topic from the bridge
   - Run the spell's full process as if the user invoked it directly

4. **Synthesis:** After spell C completes, produce the ritual synthesis (Step 6)

---

### Step 6: Synthesis

After all spells complete, produce the ritual synthesis following the synthesis section of the ritual definition.

**Output format:**

```
RITUAL SYNTHESIS: <NAME>
══════════════════════════════════════════════════════════════

Topic: <user's topic>
Spells completed: <list of spells that ran>

CONVERGENT FINDINGS (same conclusion, different angles = strong signal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• <finding from spell A> ↔ <finding from spell B>
  Why this convergence matters: <explanation>

• <finding> ↔ <finding>
  Why this convergence matters: <explanation>

(If no convergent findings: "No convergent findings — the spells produced complementary rather than overlapping insights.")

DIVERGENT FINDINGS (tensions requiring resolution)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• <spell A says X> vs <spell B says Y>
  Implication: <what the tension reveals>
  Resolution: <suggested way to resolve, or "requires user decision">

(If no divergent findings: "No divergent findings — the spells are consistent.")

EMERGENT INSIGHTS (visible only in combination)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• <insight neither spell alone could produce>

COMBINED VERDICT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<One clear recommendation synthesizing all spell outputs.
 Not "it depends" — commit to a direction with caveats.>

NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Unified, deduplicated action list from all spells.
 Each action anchored to a specific finding.
 Ordered by priority, not by source spell.>
```

**Synthesis quality checks:**
- Convergent findings cite specific sections from each spell's output — not vague "both found issues"
- Divergent findings identify the actual tension, not just that the outputs differ
- Emergent insights are genuinely novel — they couldn't be produced by either spell alone
- Combined verdict makes a clear recommendation, not a restatement of individual outputs
- Next steps are deduplicated — don't repeat the same action because two spells suggested it

---

## Guidelines

- **Spells are ritual-agnostic.** Never modify a spell's template or behavior for ritual compatibility. If a spell needs to change, that change should work for standalone invocation too.
- **Bridges extract, they don't summarize.** Pull specific named sections and reframe them as input. Don't compress spell outputs into vague summaries.
- **Gate checks protect quality.** If a spell's output doesn't support continuation, stop early rather than producing low-quality downstream output.
- **User checkpoints are mandatory.** Always present bridge content and let the user approve, modify, skip, or redirect. Rituals are long — the user should stay in control.
- **Synthesis is additive.** It appears AFTER all spells, not instead of them. The synthesis adds cross-referencing value; the individual spell outputs remain the primary artifacts.
- **Context management.** Spell outputs stay in the conversation. Bridges compress aggressively: extract only the specific named sections the next spell needs. This prevents context rot without requiring file I/O.
- **One ritual at a time.** Don't nest rituals or chain them. If the user needs more analysis after a ritual, they should invoke another spell or ritual separately.

---

## Example Usage

```
/spell:ritual list
/spell:ritual landscape state management for React
/spell:ritual architect src/api/
/spell:ritual investigate CI pipeline takes 45 minutes
/spell:ritual challenge our plan to rewrite in Rust
/spell:ritual survey real-time WebSocket framework
/spell:ritual full-landscape authentication for our Node API
/spell:ritual risk-map migrating to microservices
```
