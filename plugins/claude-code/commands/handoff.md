---
description: Write or resume from a structured handoff document
allowed-tools: Bash, Read, Write, Glob, Grep, Task, AskUserQuestion
---

## Summary

**Write a structured handoff document, or resume from one.** Two modes:

- **Generate** (default): Capture session state and promote permanent knowledge (decisions, dead ends, gotchas) to durable homes — everything the next session (or developer) needs to continue without losing ground.
- **Resume**: Consume a handoff file — verify its claims against current state, build a prioritized action plan, and delete the file (use `--keep` to preserve it).

**Arguments:** `$ARGUMENTS` (optional)
- Empty or task/feature description → Generate mode
- `resume [path] [--keep]` → Resume mode

**Output:** Structured handoff document written to `HANDOFF.md` (or user-specified path). Resume mode outputs action plan to the conversation.

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

- `docs/skills/context-transfer.md` — Shift handoff protocols (SBAR, watch turnover, ATC), context transfer in software, completeness criteria
- `docs/skills/session-continuity.md` — Session continuity for AI agents, what to capture, git state as evidence, anti-patterns, consuming a handoff (resume), context failure modes

Use **Read** to load these files from the repository root.

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

### A2: Gather Context

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
Use **AskUserQuestion** to fill them:
- "Were there any approaches you tried before this session that I should document?"
- "Are there decisions or constraints I might be missing?"
- "Anything the next person should know that isn't in the code?"

If a section is genuinely empty (e.g., no dead ends were encountered), note "None identified" — don't omit the section. A missing section looks like an oversight; an empty one shows you checked.

Note: Decisions, dead ends, and gotchas may be promoted to permanent locations in A4 rather than appearing in the handoff body. This check ensures the information was *gathered*, not that it stays here.

### A4: Promote Permanent Knowledge

Scan the decisions, dead ends, and gotchas gathered in A2–A3. Apply the **6-month heuristic**: "Would a developer joining this project in 6 months need to know this?" If yes → promote to a durable home. If it only matters for the next session → keep in the handoff.

**Discover project documentation structure:**

Use **Glob** to find existing documentation targets:
- `CLAUDE.md`, `AGENTS.md` — project-level AI guidance
- `docs/decisions/` or `docs/adr/` — Architecture Decision Records
- `docs/bpap-*` — Best-practices and antipatterns guides
- `README.md` — setup, prerequisites, getting started

If no existing targets are found, default to CLAUDE.md (creating a section if needed) or inline code comments. Do not create new documentation structures (ADR directories, BPAP files) without user confirmation — offer it as an option in the triage table.

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

Use **AskUserQuestion** to present the triage table and confirm promotions. Show each permanent item with its proposed destination:

```
PERMANENCE TRIAGE
| Item | Type | Promote to |
|------|------|-----------|
| <item summary> | Decision | <target file (section)> |
| <item summary> | Dead end | <target file or BPAP> |
| <item summary> | Gotcha | <target file (section)> |
```

Options:
- **Promote all** — Write all items to their proposed locations
- **Review individually** — Walk through each item for approval
- **Skip promotion** — Keep everything in the handoff (legacy format)

**Write confirmed items to their durable homes** using the appropriate format for that file type (inline comment, ADR section, BPAP antipattern entry, AGENTS.md bullet, etc.).

Track what was promoted — the list feeds the PROMOTED section in the handoff.

### A5: Write the Handoff

Output the structured handoff document. The handoff captures **transient session state** — where you are, what's next, what's unresolved. Permanent knowledge has already been written to durable homes in A4 and is referenced in the PROMOTED section.

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

### A6: Write to File and Offer Next Actions

**Write the handoff to a file.** Use **Write** to save to `HANDOFF.md` in the repository root (or a path based on project conventions if one is evident from existing files). Do **not** commit or push the handoff file — it is a transient artifact that will be consumed and deleted by the next session.

Then use **AskUserQuestion** to ask what to do next:
- **Done** — File is written, no further action needed
- **Adjust scope** — Go back and add or remove sections

---

## Mode B: Resume

### B1: Locate the Handoff File

Parse `$ARGUMENTS` for a path after `resume`:
- If a path is provided (e.g., `resume HANDOFF.md` or `resume docs/handoff-auth.md`), use it directly.
- If no path is provided, auto-detect:

Use **Glob** to search in order:
1. `HANDOFF.md` in the repository root
2. `*.handoff.md` in the repository root
3. `HANDOFF.md` in common locations: `docs/`, `.github/`, the current working directory

If multiple candidates are found, use **AskUserQuestion** to ask which one to consume.

If no handoff file is found, inform the user and exit.

Check for the `--keep` flag in `$ARGUMENTS`. If present, skip deletion of the handoff file in the final step.

### B2: Consume the Handoff

Use **Read** to load the handoff file.

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

Use **Bash** to run:
- `git branch --show-current` — does it match the handoff's branch?
- `git log --oneline -10` — any commits since the handoff date?
- `git status` — uncommitted changes not mentioned in the handoff?
- `git diff --stat` — current modifications

Check for discrepancies (context clash prevention):
- **Branch mismatch** — handoff describes a different branch than the current one
- **New commits** — work has happened since the handoff was written
- **Uncommitted changes** — modifications exist that the handoff doesn't mention
- **Missing files** — key files listed in the handoff no longer exist at those paths

Use **Glob** to verify that key files listed in the handoff still exist.

Flag every discrepancy explicitly. Do not silently resolve conflicts between the handoff and current state.

### B4: Build the Action Plan

**If the handoff has a PROMOTED section:** Follow each reference to load decisions, dead ends, and gotchas from their permanent homes.

Use **Read** to load each referenced file and extract the promoted items. If a referenced file has changed since the handoff was written (based on git log for that file vs. handoff date), flag the discrepancy.

**If the handoff uses the legacy format:** Extract decisions, dead ends, and gotchas directly from the handoff body.

Prioritize the consumed content:

**P1 — In-progress work:** Items the handoff marks as "in progress." These are the immediate priority — continue what was already started.

**P2 — Next steps:** The outgoing session's recommended actions, in the order given.

**P3 — Open questions:** Unresolved decisions that may need to be addressed before proceeding.

Layer the remaining sections as constraints:
- **Dead ends** → "do not attempt" list. Never re-try a documented dead end unless the constraint that caused it has changed.
- **Gotchas** → warnings to keep in mind during execution.
- **Decisions** → context to preserve. Do not reverse without understanding the original rationale and confirming the constraint no longer applies.

Use **Glob** and **Read** to verify that key files still exist and haven't changed in ways that invalidate the action plan.

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
(Include only the subsection matching the handoff format)

Promoted format:
- <N> items loaded from <M> permanent homes
- <K> items missing or changed (see DISCREPANCIES)

Legacy format:
- <N> decisions loaded
- <N> dead ends loaded (DO NOT REVISIT)
- <N> gotchas noted

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

Source: <path> | Status: consumed, pending deletion
```

### B6: Offer to Begin

**Delete the handoff file** unless `--keep` was specified in `$ARGUMENTS`. The handoff is a transient artifact — once consumed, it should not linger. With the promoted format, permanent knowledge already lives in durable homes. With legacy format, warn the user before deleting that decisions, dead ends, and gotchas embedded in the handoff body will be lost, and offer to promote them first.

Use **AskUserQuestion** to ask how to proceed:
- **Start Priority 1** — Begin working on the top in-progress item immediately
- **Review the plan** — Walk through the action plan in detail before starting
- **Load key files** — Read the key files into context before deciding
- **Resolve open questions first** — Address open questions before starting work

---

## Guidelines

### Generate (Mode A)

- **The handoff is a session bridge, not a knowledge base.** Decisions, dead ends, and gotchas are permanent system knowledge — they belong in durable locations (code comments, CLAUDE.md, AGENTS.md, ADRs, BPAPs). The handoff captures transient session state: where you are, what's next, what's unresolved. Promote permanent items during generation; reference them in the PROMOTED section.
- **The 6-month test.** Would a developer joining the project in 6 months need to know this? If yes, it's permanent — promote it. If it only matters for the next session, it belongs in the handoff.
- **Dead ends that generalize are antipatterns.** If a dead end could trap someone on a different project (Y is a general property, not a project-specific constraint), promote it as a named BPAP antipattern — not just a code comment.
- **Dead ends are the highest-value discovery.** Without them, the next session re-tries approaches that already failed. Document the approach, why it was tried, and why it was abandoned — then promote to a durable home so they survive beyond this handoff.
- **Decisions need rationale, not just the choice.** "Used PostgreSQL" is useless. "Used PostgreSQL over SQLite — Reason: need concurrent writes from multiple workers, SQLite locks on write" lets the next person understand whether the decision still applies.
- **Next steps must be specific and actionable.** "Continue working on the API" is worthless. "Add input validation to POST /users using the schema in src/types/user.ts — the endpoint currently accepts any body" gives the next session a clear starting point.
- **The document must stand alone.** The reader has zero prior context — no access to this conversation, no memory of decisions, no awareness of what was tried. Write as if the reader is starting from scratch.
- **Git state is evidence, not decoration.** The branch name, commit history, diff, and stash list are objective facts about the state of the work. Use them to ground the handoff in reality.
- **Don't omit empty sections.** A section marked "None identified" proves you checked. A missing section looks like you forgot.

### Resume (Mode B)

- **Follow PROMOTED references.** Load decisions, dead ends, and gotchas from their permanent locations. If a referenced file changed since the handoff was written, flag it — the promoted item may have been updated or superseded.
- **Resume consumes context, not just text.** Understand the handoff's intent and build an action plan — don't just reformat the content.
- **Dead ends are sacred on resume.** Never suggest a documented dead end as an approach. If "Tried X, abandoned because Y," then X is off the table unless Y has demonstrably changed. This applies whether dead ends are in the handoff body (legacy) or in permanent locations (promoted).
- **Verify before assuming.** The handoff may be stale. Check every claim against current git state before building on it.
- **Deletion is safe with promoted format.** When the handoff has a PROMOTED section, all permanent knowledge lives in durable homes — the file only contains transient state. Recommend deletion confidently. For legacy-format handoffs, warn that deletion loses permanent knowledge.
- **Watch for context poisoning.** If a handoff claim doesn't match git evidence, flag the discrepancy. Don't silently trust the handoff over observable reality.

### Both Modes

- **Credit:** This spell applies shift handoff protocols from high-reliability fields — SBAR (medicine, 1990s), watch turnover (military), and ATC handoffs (aviation) — adapted for software engineering and AI session continuity.

---

## Example Usage

```
/spell:handoff
/spell:handoff authentication refactor
/spell:handoff the billing integration work on feature/stripe-v3
/spell:handoff — session ending, capture everything
/spell:handoff resume
/spell:handoff resume HANDOFF.md
/spell:handoff resume docs/auth-handoff.md --keep
```
