---
description: Write or resume from a structured handoff document
---

## Summary

**Write a structured handoff document, or resume from one.** Two modes:

- **Generate** (default): Capture session state and promote permanent knowledge (decisions, dead ends, gotchas) to durable homes — everything the next session (or developer) needs to continue without losing ground.
- **Resume**: Consume a handoff file — verify its claims against current state, build a prioritized action plan, and offer to clean up the file.

**Arguments:** `$ARGUMENTS` (optional)
- Empty or task/feature description → Generate mode
- `resume [path] [--keep]` → Resume mode

**Output:** Structured handoff document or action plan output directly to the conversation (Write is available if the user requests the output be saved to a file)

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

Note: Decisions, dead ends, and gotchas will be triaged in A4 — they may be promoted to permanent locations rather than appearing as handoff sections. The check here ensures the information was *gathered*, not that it will appear in the handoff body.

### A4: Promote Permanent Knowledge

Scan the decisions, dead ends, and gotchas gathered in A2–A3. Apply the **6-month heuristic**: "Would a developer joining this project in 6 months need to know this?" If yes → permanent knowledge that belongs in a durable home, not the handoff. If it only matters for the next session → transient, stays in the handoff.

**Discover project documentation structure:**

Search for existing documentation targets: CLAUDE.md, AGENTS.md, docs/decisions/, docs/bpap-*, README.md.

If no existing documentation targets are found, default permanent items to CLAUDE.md (creating a section if needed) or inline code comments. Do not create new documentation structures (ADR directories, BPAP files) without user confirmation — offer it as an option in the triage table.

**Classify each item using the promotion target heuristics:**

| Item type | Natural durable home |
|-----------|---------------------|
| Decision reflected in config/code | Inline comment above the relevant line |
| Decision with architectural rationale | ADR (if `docs/decisions/` exists) or CLAUDE.md/AGENTS.md |
| Dead end revealing a system constraint | AGENTS.md or code comment near the chosen approach |
| Dead end revealing a reusable pattern | BPAP antipattern (if `docs/bpap-*` exist or the pattern warrants one) |
| Gotcha about system/infra behavior | AGENTS.md (gotchas section) |
| Gotcha about build/deploy/setup | CLAUDE.md or README (prerequisites) |
| Gotcha in specific code | Inline comment near the trap |

**Dead end → BPAP antipattern mapping:** Not every dead end warrants a BPAP antipattern — only those that generalize beyond the specific instance. The heuristic: "Could someone on a different project hit this same trap?" If yes → BPAP antipattern. If no → code comment or AGENTS.md.

When promoting a dead end to a BPAP antipattern, use the named antipattern format:
```
**AP-N: <Name>.** <What it looks like.>

Why it's tempting: <reason the approach looks good>
Consequences: <what goes wrong>
Instead: <what to do instead>
```

**Present the triage to the user:**

Present the triage table showing each permanent item and its proposed destination. Ask the user to confirm: promote all, review individually, or skip promotion.

**Write confirmed items to their durable homes.** For each promoted item, write it to the confirmed location using the appropriate format for that file type (inline comment, ADR section, BPAP antipattern entry, AGENTS.md bullet, etc.).

Track what was promoted — the list feeds the PROMOTED section in the handoff.

### A5: Write the Handoff

Output the structured handoff document. The handoff captures **transient session state** — where you are, what's next, what's unresolved. Permanent knowledge (decisions, dead ends, gotchas) has already been written to durable homes in A4 and is referenced in the PROMOTED section.

```
HANDOFF: <SUBJECT>
══════════════════════════════════════════════════════════════

STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary: <one-sentence description of the work and where it stands>
Branch:  <branch name>
State:   <in progress | blocked | ready for review | paused>
Date:    <today's date>

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

OPEN QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Unresolved decision or uncertainty]
- [Question that needs stakeholder input]
   ...

PROMOTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
N decisions, N dead ends, N gotchas written to durable locations:
- <item summary> → <file:line or file (section)>
- <item summary> → <file (section)>
   ...
(or "No permanent items identified — all context is session-specific")
```

If the user chose "Skip promotion" in A4, use the legacy eight-section format instead (STATUS, DECISIONS MADE, DEAD ENDS, CURRENT STATE, NEXT STEPS, KEY FILES, GOTCHAS, OPEN QUESTIONS).

### A6: Offer Next Actions

Ask the user what to do with the handoff: save to file, commit and push, just review, or adjust scope.

---

## Mode B: Resume

### B1: Locate the Handoff File

Parse `$ARGUMENTS` for a path after `resume`:
- If a path is provided (e.g., `resume HANDOFF.md` or `resume docs/handoff-auth.md`), use it directly.
- If no path is provided, auto-detect:

Search for `HANDOFF.md` in the repository root, then `*.handoff.md`, then common directories. Ask the user if multiple candidates exist.

If no handoff file is found, inform the user and exit.

Check for the `--keep` flag in `$ARGUMENTS`. If present, skip offering deletion in the final step.

### B2: Consume the Handoff

Read the handoff file.

Parse all sections. The handoff may use the promoted format (5 transient sections + PROMOTED), the legacy eight-section format, or a non-standard layout. Extract what's available:

**Promoted format** (STATUS, CURRENT STATE, NEXT STEPS, KEY FILES, OPEN QUESTIONS + PROMOTED):
- Status / summary
- Current state (completed / in progress / not started)
- Next steps
- Key files
- Open questions
- Promoted items (with references to durable locations)

**Legacy format:**
- Status / summary
- Decisions (with rationale)
- Dead ends (with reasons)
- Current state / Next steps / Key files / Gotchas / Open questions

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

**If the handoff has a PROMOTED section:** Follow each reference to load decisions, dead ends, and gotchas from their permanent homes.

Read each referenced file to load promoted items. Flag any files that changed since the handoff date.

**If the handoff uses the legacy format:** Extract decisions, dead ends, and gotchas directly from the handoff body.

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
From permanent homes (if PROMOTED section present):
- <N> items loaded from <M> files
- <K> items missing or changed (see DISCREPANCIES)

From handoff body (legacy sections, if any):
- <N> decisions loaded
- <N> dead ends loaded (DO NOT REVISIT)
- <N> gotchas noted

Always:
- <N> key files verified (<M> still exist, <K> missing)
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

Promoted reference issues (if any):
- [item referenced at <file:section> — file exists but section not found]
- [item referenced at <file:line> — file modified since handoff date]

Source: <path> | Status: consumed
```

### B6: Offer to Begin

Ask the user how to proceed: start P1 work, review the plan, load key files, resolve open questions first, or delete the handoff file (recommended — with promoted format, deletion is always safe since permanent knowledge lives in durable homes). If `--keep` was specified, omit the deletion option. If the handoff used legacy format, warn that deletion will lose embedded permanent knowledge.

---

## Guidelines

### Generate (Mode A)

- **The handoff is a session bridge, not a knowledge base.** Decisions, dead ends, and gotchas are permanent system knowledge — they belong in durable locations (code comments, CLAUDE.md, AGENTS.md, ADRs, BPAPs). The handoff captures transient session state: where you are, what's next, what's unresolved. Write permanent items to their final homes during generation; the handoff references them in the PROMOTED section.
- **The 6-month test.** Would a developer joining the project in 6 months need to know this? If yes, it's permanent — promote it. If it only matters for the next session, it belongs in the handoff.
- **Dead ends that generalize are antipatterns.** If a dead end could trap someone on a different project ("Tried X, failed because Y" where Y is a general property, not a project-specific constraint), it's a candidate for BPAP promotion as a named antipattern — not just a code comment.
- **Dead ends are the highest-value discovery.** Without them, the next session will waste time re-trying approaches that already failed. Document the approach, why it was tried, and specifically why it was abandoned — then promote them to a durable home so they survive beyond this handoff.
- **Decisions need rationale, not just the choice.** "Used PostgreSQL" is useless. "Used PostgreSQL over SQLite — Reason: need concurrent writes from multiple workers, SQLite locks on write" lets the next person understand whether the decision still applies.
- **Next steps must be specific and actionable.** "Continue working on the API" is worthless. "Add input validation to POST /users using the schema in src/types/user.ts — the endpoint currently accepts any body" gives the next session a clear starting point.
- **The document must stand alone.** The reader has zero prior context — no access to this conversation, no memory of decisions, no awareness of what was tried. Write as if the reader is starting from scratch.
- **Git state is evidence, not decoration.** The branch name, commit history, diff, and stash list are objective facts about the state of the work. Use them to ground the handoff in reality.
- **Don't omit empty sections.** A section marked "None identified" proves you checked. A missing section looks like you forgot.

### Resume (Mode B)

- **Follow PROMOTED references.** Load decisions, dead ends, and gotchas from their permanent locations. If a referenced file has changed since the handoff was written, flag the discrepancy — the promoted item may have been updated or superseded.
- **Resume consumes context, not just text.** Understand the handoff's intent and build an action plan — don't just reformat the content.
- **Dead ends are sacred on resume.** Never suggest a documented dead end as an approach. If the handoff says "Tried X, abandoned because Y," X is off the table unless Y has demonstrably changed. This applies whether dead ends are in the handoff body (legacy) or in permanent locations (promoted).
- **Verify before assuming.** The handoff may be stale. Check every claim against current git state before building on it.
- **Deletion is safe with promoted format.** When the handoff has a PROMOTED section, all permanent knowledge lives in durable homes — the handoff file only contains transient session state. Recommend deletion confidently. For legacy-format handoffs, warn that deletion loses permanent knowledge.
- **Watch for context poisoning.** If a handoff claim doesn't match git evidence, flag the discrepancy. Don't silently trust the handoff over observable reality.

### Both Modes

- **Credit:** This spell applies shift handoff protocols from high-reliability fields — SBAR (medicine, 1990s), watch turnover (military), and ATC handoffs (aviation) — adapted for software engineering and AI session continuity.

---

## Example Usage

```
/spell-handoff
/spell-handoff authentication refactor
/spell-handoff the billing integration work on feature/stripe-v3
/spell-handoff — session ending, capture everything
/spell-handoff resume
/spell-handoff resume HANDOFF.md
/spell-handoff resume docs/auth-handoff.md --keep
```
