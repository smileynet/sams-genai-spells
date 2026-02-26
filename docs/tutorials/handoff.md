# Shift Handoff Protocols & Context Transfer

## The Problem

It's 3 AM in the ICU. A nurse finishing a 12-hour shift briefs the incoming nurse: "Room 4 is stable, Room 7 needs monitoring." The incoming nurse nods, the outgoing nurse leaves. Two hours later, the patient in Room 7 has a crisis — but the incoming nurse doesn't know that the patient's medication was changed an hour ago, that the previous dose caused an allergic reaction, or that the attending physician wanted to be called if blood pressure dropped below a specific threshold. None of that was in the handoff. The outgoing nurse knew all of it, and now that knowledge is gone.

This isn't a hypothetical. The Joint Commission identified communication failures during shift handoffs as the leading root cause of sentinel events (unexpected deaths or serious injuries) in hospitals. Not misdiagnosis. Not wrong medication. The information was available — it just didn't transfer.

The same pattern plays out in software, with lower stakes but identical mechanics. A developer spends four hours debugging an authentication issue, tries three approaches that don't work, discovers the real problem is a race condition in the token refresh logic, and starts implementing a fix. Then the session ends — they close the laptop, the AI context window fills up, or a colleague takes over the next morning. The fix is half-written. The three failed approaches aren't documented anywhere. The reasoning behind the current approach exists only in the developer's head (or in a conversation that's already been compressed away). The next person — or the next session — starts from scratch, tries the same three approaches, and wastes the same four hours.

## How It Helps

A structured handoff captures exactly the information that informal transitions lose:

1. **Status** — what's happening right now, grounded in evidence (git state, test results), not assertions ("it's almost done")
2. **Decisions with rationale** — not just what was chosen, but why, and what alternatives were considered
3. **Dead ends** — approaches that were tried and abandoned, with the specific reason each failed
4. **Current state** — what's completed, what's in progress, what hasn't started
5. **Next steps** — specific, actionable items with file paths and context
6. **Key files** — which files matter for this work and why, so the next person doesn't search the whole codebase
7. **Gotchas** — non-obvious constraints that will bite you if you don't know about them
8. **Open questions** — unresolved decisions that need input

The dead-ends section is the highest-value part of any handoff. The code shows what was kept — it doesn't show what was tried and thrown away. Without documenting dead ends, the next session will re-discover them the hard way, one at a time, burning identical time on identical failures.

## Why It Works

Structured handoffs work for the same reason checklists work in aviation: they prevent omission errors under time pressure. When a nurse is exhausted at the end of a 12-hour shift, they'll forget things. When a developer is wrapping up a session, they'll skip context that seems obvious (it won't be obvious tomorrow). The structure ensures completeness even when the person creating the handoff is tired, rushed, or doesn't realize what the next person needs.

The specific sections matter:

- **Decisions without rationale** get reversed. If the handoff says "using PostgreSQL" without explaining why, the next person might switch to SQLite for simplicity — not realizing the decision was made because the app needs concurrent writes from multiple workers.
- **Dead ends without reasons** get retried. If the handoff doesn't mention that native `fetch` was tried and abandoned because of missing timeout support in Node 18, the next session will try it, spend 30 minutes, and reach the same conclusion.
- **Vague next steps** waste time. "Continue working on the API" forces the next person to figure out what needs doing. "Add input validation to POST /users using the schema in src/types/user.ts" lets them start immediately.

## In Practice

**SBAR in medicine.** The SBAR framework — Situation, Background, Assessment, Recommendation — was developed at Kaiser Permanente in the 1990s, adapted from the US Navy's communication protocol for nuclear submarines. When you can't afford miscommunication (reactors, patients), you standardize the format. The Joint Commission mandated structured handoff protocols in 2006 after research showed that communication failures during transitions were the leading cause of sentinel events. SBAR gives every handoff the same shape, so nothing falls through the cracks — regardless of who's doing the handoff or how tired they are.

**Watch turnover in the military.** When a naval watch officer hands off duty, the protocol requires specific items: status of all active tasks, pending actions, known hazards, and standing orders. The key principle is that the outgoing officer must make the incoming officer's mental model match reality. You can't hand off "everything's fine" — you hand off specifics. The military learned this the hard way: vague handoffs during the Cold War led to situations where the incoming watch didn't know about ongoing operations, standing orders, or active threats.

**ATC handoffs in aviation.** Air traffic controllers hand off aircraft between sectors with a standardized protocol: aircraft identification, position, altitude, heading, speed, and any special instructions. The critical constraint is that once the aircraft switches to the new frequency, the receiving controller can't ask follow-up questions from the previous one. The handoff must be complete and self-contained — exactly the constraint that applies to AI session transitions, where the previous session's context is gone.

**ADRs in software engineering.** Architecture Decision Records capture technology choices with their context: what was decided, what alternatives were considered, and why this option was chosen. They solve one part of the handoff problem — decisions with rationale — but don't capture dead ends, current state, or next steps. A handoff document includes the ADR-style "considered alternatives" section while also covering everything else the next person needs.

**PR descriptions.** Good pull request descriptions partially serve as handoff documents — they explain what changed, why, and what to watch for. But they describe completed work, not in-progress sessions. A handoff captures the messy middle: half-finished implementations, unresolved questions, and the context that hasn't made it into a commit yet.

## The Command

The `/spell:handoff` command applies shift handoff protocols by:

1. Auto-detecting scope from git state (or accepting explicit arguments)
2. Gathering context from multiple sources: git history, codebase markers, session memory, and existing docs
3. Assessing completeness against eight criteria before writing
4. Producing a structured document with all eight sections: status, decisions, dead ends, current state, next steps, key files, gotchas, and open questions
5. Offering next actions: save to file, commit and push, review, or adjust scope

The spell is entirely introspective — it uses git state and session context rather than web research. Arguments are optional by design: the AI already has the session context, and git state provides evidence. This makes it the fastest spell to invoke — just run it at the end of a session.

## Resuming from a Handoff

Writing a handoff captures context. Resuming from one restores and activates it.

The `/spell:handoff resume` command completes the context transfer loop. It reads a handoff file, verifies its claims against the current git state, builds a prioritized action plan, and deletes the file by default. The deletion is deliberate — a consumed handoff has served its purpose, and leaving it around creates context rot risk. Stale handoff files are worse than no handoff at all, because they look authoritative while being out of date.

The verify-before-act step is what separates a good resume from a naive one. A handoff is a snapshot from the past. The branch may have changed, new commits may have landed, files may have moved. The resume checks for these discrepancies before trusting the handoff's claims — the same way an air traffic controller accepting a handoff confirms the aircraft's position and altitude rather than trusting the previous controller's last report blindly.

Use `--keep` when the handoff is still needed — pausing work rather than completing a transfer, or when multiple sessions will consume the same handoff.

## Background

The concept of structured handoffs originates in high-reliability organizations — fields where the cost of communication failure is measured in lives, not just lost time.

SBAR was developed at Kaiser Permanente in the 1990s, adapted from military communication protocols. It was designed for situations where a nurse needed to communicate critical information to a physician quickly and completely. The framework spread through healthcare after the Joint Commission's 2006 National Patient Safety Goal requiring standardized handoff communication. Studies showed that implementing SBAR reduced communication-related adverse events by 30-50%.

Military watch turnover protocols evolved over centuries of naval operations, formalized in standing orders that require specific categories of information to transfer at each watch change. The US Navy's Engineering Duty Officer manual, for instance, specifies exactly what must be communicated: equipment status, ongoing operations, pending maintenance, safety hazards, and any deviations from normal procedures.

Air traffic control handoff protocols were standardized by the International Civil Aviation Organization (ICAO) and national aviation authorities. The protocols evolved from incidents where context loss during sector transitions contributed to near-misses and accidents. The key design constraint — the handoff must be complete because the previous controller becomes unavailable — maps directly to AI session transitions.

In software engineering, the concept appears in fragments: ADRs capture decisions, PR descriptions capture changes, design docs capture architecture. But no standard format captures the full context of a work session. The emerging pattern of AI session handoff documents — visible in tools like claude-code-handoff and discussions in the AI coding community — is converging on the same structured approach that high-reliability fields settled on decades ago.

## Further Reading

- [SBAR Communication](https://www.ihi.org/resources/Pages/Tools/SBARToolkit.aspx) — Institute for Healthcare Improvement's SBAR toolkit
- [Joint Commission Handoff Requirements](https://www.jointcommission.org/resources/patient-safety-topics/sentinel-event/) — Patient safety goals that mandated structured handoffs
- [Architecture Decision Records](https://adr.github.io/) — Lightweight format for capturing technology decisions with rationale
- [The Checklist Manifesto](https://atulgawande.com/book/the-checklist-manifesto/) — Atul Gawande on structured protocols in high-stakes environments
- [Crew Resource Management](https://en.wikipedia.org/wiki/Crew_resource_management) — Aviation's approach to structured team communication
