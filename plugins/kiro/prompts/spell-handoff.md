## Summary

**Write a structured handoff document capturing session context before it evaporates.** Gathers decisions made, dead ends tried, current state, and next steps — everything the next session (or developer) needs to continue without losing ground.

**Arguments:** `$ARGUMENTS` (optional) - Task, feature, or context to focus the handoff on. If empty, auto-detects from git state and session context.

**Output:** Structured handoff document output directly to the conversation (Write is available if the user requests the output be saved to a file)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/context-transfer.md`
- `docs/skills/session-continuity.md`

---

## Process

### Step 1: Determine Scope

**If `$ARGUMENTS` is provided:**
- Use the arguments to focus the handoff scope (specific feature, task, or area of work)

**If `$ARGUMENTS` is empty:**
Auto-detect scope from git state:

Run git commands to gather: status, recent log, diff stat, current branch.

If git state is clean and no clear scope emerges from branch name or recent commits:
Ask the user: "What work should this handoff cover?"

**Output the scope:**

```
HANDOFF SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subject: <what this handoff covers>
Branch:  <current branch>
Status:  <in progress | blocked | ready for review | paused>
```

### Step 2: Gather Context

Collect information from multiple sources:

**Git state (evidence):**
Run git commands: full log for the branch, diff (staged and unstaged), stash list.

**Codebase markers:**
Search for TODO, FIXME, HACK, and XXX markers in recently modified files.

**Session context (from conversation history):**
Review your own conversation history for this session and extract:
- Decisions made during the session, with the reasoning behind each
- Approaches that were tried and abandoned, with why they failed
- Open questions that came up but weren't resolved
- Gotchas or non-obvious constraints discovered during the work

**Existing docs:**
Check README.md, CLAUDE.md, design docs, and ADRs for relevant project context.

### Step 3: Assess Completeness

Before writing the handoff, verify you have material for each required section:

| Section | Have content? |
|---------|--------------|
| Status summary | |
| Decisions made (with rationale) | |
| Dead ends (with reasons) | |
| Current state (completed / in progress / not started) | |
| Next steps (specific and actionable) | |
| Key files (with context) | |
| Gotchas | |
| Open questions | |

If critical gaps exist — especially decisions or dead ends that you observed during the session but can't fully reconstruct:
Ask the user to fill gaps — especially decisions, dead ends, and gotchas that may not be visible in the code.

If a section is genuinely empty (e.g., no dead ends were encountered), note "None identified" — don't omit the section. A missing section looks like an oversight; an empty one shows you checked.

### Step 4: Write the Handoff

Output the structured handoff document:

```
HANDOFF: <SUBJECT>
══════════════════════════════════════════════════════════════

STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary: <one-sentence description of the work and where it stands>
Branch:  <branch name>
State:   <in progress | blocked | ready for review | paused>
Date:    <today's date>

DECISIONS MADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Decision] — Reason: [why this was chosen over alternatives]
2. [Decision] — Reason: [why]
   ...

DEAD ENDS (DO NOT REVISIT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Tried: [approach] — Abandoned because: [specific reason]
2. Tried: [approach] — Abandoned because: [specific reason]
   ...

CURRENT STATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Completed:
- [item]

In progress:
- [item] — <where it stands>

Not started:
- [item]

NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Specific, actionable step with file paths and context]
2. [Next step]
3. [Next step]
   ...

KEY FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <path> — <what this file does and why it matters for this work>
- <path> — <context note>
   ...

GOTCHAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Non-obvious constraint, quirk, or trap]
- [Thing that will bite you if you don't know about it]
   ...

OPEN QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Unresolved decision or uncertainty]
- [Question that needs stakeholder input]
   ...
```

### Step 5: Offer Next Actions

Ask the user what to do with the handoff: save to file, commit and push, just review, or adjust scope.

---

## Guidelines

- **Dead ends are the highest-value section.** Without them, the next session will waste time re-trying approaches that already failed. Document the approach, why it was tried, and specifically why it was abandoned.
- **Decisions need rationale, not just the choice.** "Used PostgreSQL" is useless. "Used PostgreSQL over SQLite — Reason: need concurrent writes from multiple workers, SQLite locks on write" lets the next person understand whether the decision still applies.
- **Next steps must be specific and actionable.** "Continue working on the API" is worthless. "Add input validation to POST /users using the schema in src/types/user.ts — the endpoint currently accepts any body" gives the next session a clear starting point.
- **The document must stand alone.** The reader has zero prior context — no access to this conversation, no memory of decisions, no awareness of what was tried. Write as if the reader is starting from scratch.
- **Git state is evidence, not decoration.** The branch name, commit history, diff, and stash list are objective facts about the state of the work. Use them to ground the handoff in reality.
- **Don't omit empty sections.** A section marked "None identified" proves you checked. A missing section looks like you forgot.
- **Prefer specificity over brevity.** A longer handoff that prevents two hours of rework is worth more than a terse one that looks clean. Include file paths, function names, error messages, and URLs.
- **Credit:** This spell applies shift handoff protocols from high-reliability fields — SBAR (medicine, 1990s), watch turnover (military), and ATC handoffs (aviation) — adapted for software engineering and AI session continuity.

---

## Example Usage

```
@spell-handoff
@spell-handoff authentication refactor
@spell-handoff the billing integration work on feature/stripe-v3
@spell-handoff — session ending, capture everything
```
