## Summary

**Write a structured handoff document, or resume from one.** Two modes:

- **Generate** (default): Capture decisions, dead ends, current state, and next steps — everything the next session (or developer) needs to continue without losing ground.
- **Resume**: Consume a handoff file — verify its claims against current state, build a prioritized action plan, and delete the file by default.

**Arguments:** `$ARGUMENTS` (optional)
- Empty or task/feature description → Generate mode
- `resume [path] [--keep]` → Resume mode

**Output:** Structured handoff document (generate) or action plan (resume)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/context-transfer.md`
- `docs/skills/session-continuity.md`

---

## Process

### Step 1: Determine Mode

Parse `$ARGUMENTS` to determine which mode to operate in:

| Input | Mode |
|-------|------|
| `resume` or `resume <path>` or `resume --keep` | **Resume** |
| Any other value | **Generate** |
| Empty | **Generate** (auto-detect scope) |

---

## Mode A: Generate

### A1: Determine Scope

**If `$ARGUMENTS` is provided (and not `resume`):**
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

### A2: Gather Context

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

### A3: Assess Completeness

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

### A4: Write the Handoff

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

### A5: Offer Next Actions

Ask the user what to do with the handoff: save to file, commit and push, just review, or adjust scope.

---

## Mode B: Resume

### B1: Locate the Handoff File

Parse `$ARGUMENTS` for a path after `resume`:
- If a path is provided (e.g., `resume HANDOFF.md` or `resume docs/handoff-auth.md`), use it directly.
- If no path is provided, auto-detect:

Search for `HANDOFF.md` in the repository root, then `*.handoff.md`, then common directories. Ask the user if multiple candidates exist.

If no handoff file is found, inform the user and exit.

Check for the `--keep` flag in `$ARGUMENTS`. If present, the file will be preserved after consumption.

### B2: Consume the Handoff

Read the handoff file.

Parse all sections. The handoff may use the standard eight-section format or a non-standard layout. Extract what's available:
- Status / summary
- Decisions (with rationale)
- Dead ends (with reasons)
- Current state (completed / in progress / not started)
- Next steps
- Key files
- Gotchas
- Open questions

Note any sections that are missing — a gap in the handoff is information the resume should flag.

### B3: Verify Against Current State

Run git commands: current branch, recent log, status, diff stat.

Check for discrepancies (context clash prevention):
- **Branch mismatch** — handoff describes a different branch than the current one
- **New commits** — work has happened since the handoff was written
- **Uncommitted changes** — modifications exist that the handoff doesn't mention
- **Missing files** — key files listed in the handoff no longer exist at those paths

Verify that key files listed in the handoff still exist.

Flag every discrepancy explicitly. Do not silently resolve conflicts between the handoff and current state.

### B4: Build the Action Plan

Prioritize the consumed content:

**P1 — In-progress work:** Items the handoff marks as "in progress." These are the immediate priority — continue what was already started.

**P2 — Next steps:** The outgoing session's recommended actions, in the order given.

**P3 — Open questions:** Unresolved decisions that may need to be addressed before proceeding.

Layer the remaining sections as constraints:
- **Dead ends** → "do not attempt" list. Never re-try a documented dead end unless the constraint that caused it has changed.
- **Gotchas** → warnings to keep in mind during execution.
- **Decisions** → context to preserve. Do not reverse without understanding the original rationale and confirming the constraint no longer applies.

Verify key files still exist and haven't changed significantly.

### B5: Output the Resume

Output the structured resume:

```
RESUMING: <SUBJECT>
══════════════════════════════════════════════════════════════

STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary:   <one-sentence description of the work being resumed>
Branch:    <current branch> <✓ matches handoff | ⚠ differs from handoff>
Handoff:   <handoff date> → today (<N days/hours ago>)
New commits since handoff: <count, or "none">

CONTEXT LOADED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <N> decisions loaded
- <N> dead ends loaded (DO NOT REVISIT)
- <N> key files verified (<M> still exist, <K> missing)
- <N> gotchas noted
- <N> open questions pending

ACTION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P1 — Continue in-progress:
1. [item with file path and current status]

P2 — Next steps:
1. [item with file path and context]
2. [item]

P3 — Resolve open questions:
1. [question — who/what can answer it]

DEAD ENDS — DO NOT REVISIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Tried: [approach] — Abandoned because: [reason]
   ...

ACTIVE CONSTRAINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gotchas:
- [constraint or trap]

Decisions in effect:
- [decision] — Reason: [rationale]

⚠ DISCREPANCIES (if any)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [what the handoff claimed vs. what current state shows]

Source: <path> | Status: <consumed and deleted | kept (--keep)>
```

### B6: Delete or Keep

**Default behavior:** Delete the handoff file after consumption.

If the file is git-tracked, use `git rm`. If untracked, delete directly. Skip if `--keep` was specified.

### B7: Offer to Begin

Ask the user how to proceed: start P1 work, review the plan, load key files, or resolve open questions first.

---

## Guidelines

### Generate (Mode A)

- **Dead ends are the highest-value section.** Without them, the next session will waste time re-trying approaches that already failed. Document the approach, why it was tried, and specifically why it was abandoned.
- **Decisions need rationale, not just the choice.** "Used PostgreSQL" is useless. "Used PostgreSQL over SQLite — Reason: need concurrent writes from multiple workers, SQLite locks on write" lets the next person understand whether the decision still applies.
- **Next steps must be specific and actionable.** "Continue working on the API" is worthless. "Add input validation to POST /users using the schema in src/types/user.ts — the endpoint currently accepts any body" gives the next session a clear starting point.
- **The document must stand alone.** The reader has zero prior context — no access to this conversation, no memory of decisions, no awareness of what was tried. Write as if the reader is starting from scratch.
- **Git state is evidence, not decoration.** The branch name, commit history, diff, and stash list are objective facts about the state of the work. Use them to ground the handoff in reality.
- **Don't omit empty sections.** A section marked "None identified" proves you checked. A missing section looks like you forgot.
- **Prefer specificity over brevity.** A longer handoff that prevents two hours of rework is worth more than a terse one that looks clean. Include file paths, function names, error messages, and URLs.

### Resume (Mode B)

- **Resume consumes context, not just text.** Understand the handoff's intent and build an action plan — don't just reformat the content.
- **Dead ends are sacred on resume.** Never suggest a documented dead end as an approach. If the handoff says "Tried X, abandoned because Y," X is off the table unless Y has demonstrably changed.
- **Verify before assuming.** The handoff may be stale. Check every claim against current git state before building on it.
- **Delete is the right default.** Stale handoffs are worse than no handoff — they look authoritative while being out of date. Consume and delete unless the user explicitly requests `--keep`.
- **Watch for context poisoning.** If a handoff claim doesn't match git evidence, flag the discrepancy. Don't silently trust the handoff over observable reality.

### Both Modes

- **Credit:** This spell applies shift handoff protocols from high-reliability fields — SBAR (medicine, 1990s), watch turnover (military), and ATC handoffs (aviation) — adapted for software engineering and AI session continuity.

---

## Example Usage

```
@spell-handoff
@spell-handoff authentication refactor
@spell-handoff the billing integration work on feature/stripe-v3
@spell-handoff — session ending, capture everything
@spell-handoff resume
@spell-handoff resume HANDOFF.md
@spell-handoff resume docs/auth-handoff.md --keep
```
