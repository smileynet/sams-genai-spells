---
description: Write a structured handoff document for the next session or developer
allowed-tools: Bash, Read, Write, Glob, Grep, Task, AskUserQuestion
---

## Summary

**Write a structured handoff document capturing session context before it evaporates.** Gathers decisions made, dead ends tried, current state, and next steps — everything the next session (or developer) needs to continue without losing ground.

**Arguments:** `$ARGUMENTS` (optional) - Task, feature, or context to focus the handoff on. If empty, auto-detects from git state and session context.

**Output:** Structured handoff document output directly to the conversation (Write is available if the user requests the output be saved to a file)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

- `docs/skills/context-transfer.md` — Shift handoff protocols (SBAR, watch turnover, ATC), context transfer in software, completeness criteria
- `docs/skills/session-continuity.md` — Session continuity for AI agents, what to capture, git state as evidence, anti-patterns

Use **Read** to load these files from the repository root.

---

## Process

### Step 1: Determine Scope

**If `$ARGUMENTS` is provided:**
- Use the arguments to focus the handoff scope (specific feature, task, or area of work)

**If `$ARGUMENTS` is empty:**
Auto-detect scope from git state:

Use **Bash** to run:
- `git status` — what's changed, staged, unstaged
- `git log --oneline -10` — recent commits on the current branch
- `git diff --stat` — summary of current changes
- `git branch --show-current` — current branch name

If git state is clean and no clear scope emerges from branch name or recent commits:
Use **AskUserQuestion** to ask: "What work should this handoff cover?"
Provide 2-3 contextual suggestions based on:
- The current branch name
- Recent commit messages
- Any open TODO/FIXME markers found in the codebase

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
Use **Bash** to run:
- `git log --oneline -20` — commit history for the work
- `git diff` — current uncommitted changes
- `git diff --cached` — staged changes
- `git stash list` — any stashed work

**Codebase markers:**
Use **Grep** to search for TODO, FIXME, HACK, and XXX markers in recently modified files. Use **Glob** to identify key files touched during this work.

**Session context (from conversation history):**
Review your own conversation history for this session and extract:
- Decisions made during the session, with the reasoning behind each
- Approaches that were tried and abandoned, with why they failed
- Open questions that came up but weren't resolved
- Gotchas or non-obvious constraints discovered during the work

**Existing docs:**
Use **Read** to check for relevant context in:
- README.md, CLAUDE.md, or similar project docs
- Any design docs or ADRs in the project
- PR descriptions if working on a branch

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
Use **AskUserQuestion** to fill them:
- "Were there any approaches you tried before this session that I should document?"
- "Are there decisions or constraints I might be missing?"
- "Anything the next person should know that isn't in the code?"

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

Use **AskUserQuestion** to ask what to do with the handoff:
- **Save to file** — Write to a file (suggest `HANDOFF.md` or a path based on the project's conventions)
- **Commit and push** — Save to file, stage, commit, and push so it's available on the branch
- **Just review** — Leave the output in the conversation for review and editing
- **Adjust scope** — Go back and add or remove sections

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
/spell:handoff
/spell:handoff authentication refactor
/spell:handoff the billing integration work on feature/stripe-v3
/spell:handoff — session ending, capture everything
```
