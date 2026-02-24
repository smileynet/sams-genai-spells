# Context Transfer — Skill Reference for AI Assistants

> Shift handoff protocols from high-reliability fields, adapted for software engineering. Use this reference when writing handoff documents that must transfer context across session or team boundaries.

## Shift Handoff Protocols

### SBAR (Medicine)

Developed at Kaiser Permanente in the 1990s, adopted by the US Navy, and mandated by the Joint Commission (2006) for patient safety:

| Component | What it covers | Software analog |
|-----------|---------------|-----------------|
| **Situation** | What's happening right now | Current state of the work — branch, status, what's changed |
| **Background** | Relevant context and history | Decisions made, approaches tried, project constraints |
| **Assessment** | Your analysis of the situation | What's working, what's not, blockers and risks |
| **Recommendation** | What you think should happen next | Specific, actionable next steps |

SBAR works because it forces structured completeness. Informal handoffs lose information proportional to how rushed they are. Structured handoffs lose less because each section acts as a checklist.

### Watch Turnover (Military)

When a naval watch officer hands off duty, the protocol requires:

1. **Status of all active tasks** — not "everything's fine" but specific items
2. **Pending actions** — what was started but not completed
3. **Known hazards** — conditions the next watch needs to be aware of
4. **Standing orders** — constraints and rules still in effect

The key insight: the outgoing watch officer must make the **incoming officer's mental model match reality**. Anything left out becomes a gap that only reveals itself during a crisis.

### ATC Handoffs (Aviation)

Air traffic controllers hand off aircraft between sectors. The protocol includes:

- Aircraft identification, position, altitude, heading, speed
- Any special instructions or restrictions
- Communication frequency for the new sector

ATC handoffs prioritize **zero ambiguity**. The receiving controller cannot ask follow-up questions once the aircraft has switched frequency. The handoff must be complete and self-contained.

## Context Transfer in Software

### What Gets Lost at Boundaries

When a session ends or work transfers between people, these categories of context reliably disappear:

| Category | Example | Cost of losing it |
|----------|---------|-------------------|
| **Decisions** | "We chose REST over GraphQL because the team has no GraphQL experience" | Next person may reverse the decision without understanding why it was made |
| **Dead ends** | "Tried using the native fetch API but it doesn't support request cancellation in our Node version" | Next person wastes time re-trying the same failed approach |
| **Mental model** | "The auth flow goes through three services: gateway → auth → user-service" | Next person reads code bottom-up instead of understanding the architecture |
| **Gotchas** | "The test suite requires Docker running — CI handles this but local dev doesn't" | Next person spends 30 minutes debugging test failures before realizing |
| **Open questions** | "We need product to decide whether deleted users are soft-deleted or hard-deleted" | Next person makes an assumption instead of escalating the question |

### Existing Formats

| Format | Scope | Captures dead ends? | Captures decisions? | Stands alone? |
|--------|-------|---------------------|---------------------|---------------|
| PR description | Single change | Rarely | Sometimes | Partially |
| ADR | Single decision | No | Yes (its purpose) | Yes |
| Design doc | Feature/system | Sometimes | Yes | Yes |
| Commit messages | Per-commit | No | Briefly | No |
| Session handoff | Work session | Yes | Yes | Yes |

A handoff document fills the gap that other formats leave — it captures the full context of a work session including dead ends, gotchas, and in-progress state.

## Completeness Criteria

A handoff document is complete when a reader with **zero prior context** can:

1. **Understand what the work is** without asking "what are you working on?"
2. **Continue where you left off** without re-discovering the current state
3. **Avoid your dead ends** without re-trying failed approaches
4. **Understand your decisions** without reversing them unknowingly
5. **Know the next steps** without figuring out what to do first
6. **Find the relevant files** without searching the whole codebase
7. **Avoid known traps** without falling into them first
8. **Escalate open questions** without making unauthorized assumptions

If any of these eight criteria aren't met, the handoff has a gap.

## Quality Signals

**Good handoff indicators:**
- Dead ends include *why* the approach failed, not just that it was tried
- Decisions include *rationale* — what alternatives were considered and why this was chosen
- Next steps reference specific files, functions, or endpoints
- Status uses evidence (git state, test results) not just assertions

**Bad handoff indicators:**
- "Continue working on the feature" (vague next steps)
- Missing dead-ends section (looks like nothing was tried)
- Decisions without rationale ("Using PostgreSQL" — but why?)
- Assumes reader context ("as we discussed" — discussed where?)
