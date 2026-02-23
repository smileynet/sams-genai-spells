## Summary

**Survey existing solutions before building.** Systematically searches for libraries, tools, frameworks, and patterns that already solve the problem — then evaluates them with structured criteria and recommends whether to adopt, adapt, or build custom.

**Arguments:** `$ARGUMENTS` (required) - Capability, problem, or feature to survey

**Output:** Structured landscape survey with comparison and recommendation output directly to the conversation (Write is available if the user requests the output be saved to a file)

---

## Skill References

Before proceeding, load the relevant skill documents for reference:

Read the following files from the repository root:
- `docs/skills/technology-evaluation.md`
- `docs/skills/solution-landscape.md`

---

## Process

### Step 1: Parse Arguments

**If `$ARGUMENTS` is empty:**
Ask the user: "What capability or problem should I survey existing solutions for?"

**Otherwise:**
- Extract the capability, problem, or feature to survey from `$ARGUMENTS`
- Continue to Step 2

### Step 2: Define the Need

Clarify what the user actually needs — not what they think the solution is. Separate the capability from the implementation.

**Output the need:**

```
NEED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Capability:  <what you actually need to do>
Constraints: <language, platform, license, performance, etc.>
Must-haves:  <non-negotiable requirements>
Nice-to-haves: <preferred but flexible>
```

If the need is unclear or too broad, ask the user to clarify the problem, constraints, and requirements.

### Step 3: Survey the Landscape

Gather existing solutions from multiple sources:

Search the web for existing solutions: libraries, frameworks, tools, and comparison articles for the capability.

**Codebase analysis:**
- Check if the current project already uses or vendors a related solution
- Check if the project's framework provides built-in support for the capability
- Look at existing dependencies — sometimes a current dependency covers the need

**Graceful degradation:** If web search is unavailable, rely on built-in knowledge and codebase analysis. Note at the top that results are based on training knowledge with a staleness warning.

### Step 4: Evaluate Candidates

Apply structured criteria from the skill docs to each candidate:

1. **Fit** — Does it solve the actual need? Not adjacent — the real requirement.
2. **Maturity** — Stable API? Semantic versioning? Production-ready?
3. **Maintenance** — Recent commits? Responsive maintainers? Bus factor?
4. **Community** — Adoption signals? Stack Overflow presence? Docs quality?
5. **Integration** — Compatible with current stack? Reasonable dependency tree?
6. **License** — Permissive? Copyleft? Compatible with the project?

**Cap at 5-7 candidates.** If more are found, filter to the most relevant based on Fit first, then Maturity and Maintenance.

**Check the Red Flags Checklist** from the technology-evaluation skill doc for each candidate.

### Step 5: Output the Survey

Output the structured survey directly in the conversation:

```
PRIOR ART: <CAPABILITY/NEED>
══════════════════════════════════════════════════════════════

Coverage: <high | medium | low> — <explanation>
Source: <web research | built-in knowledge | codebase analysis>

NEED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Capability:  <what you need>
Constraints: <language, platform, license, etc.>
Must-haves:  <non-negotiable requirements>
Nice-to-haves: <preferred but flexible>

EXISTING SOLUTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. <NAME> — <one-line description>
   Fit: <how it addresses the need>
   Strengths: <key advantages>
   Concerns: <limitations, risks, or gaps>
   Signals: <maintenance health, adoption, maturity>

2. <NAME> — <one-line description>
   Fit: <how it addresses the need>
   Strengths: <key advantages>
   Concerns: <limitations, risks, or gaps>
   Signals: <maintenance health, adoption, maturity>

[...up to 5-7 candidates]

COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Markdown table comparing top candidates across the 6 criteria.
 Format cells as best fits the data — qualitative labels,
 brief prose, or a mix. Aim for scannability.>

RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Verdict: <adopt <name> | adapt <name> | build custom>
Rationale: <why this is the right call>
Next steps: <concrete actions to take>

If build: <what to build, informed by what was surveyed>
If adopt: <how to integrate, what to watch for>
If adapt: <what to use, what to customize>

SOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- <Source with URL>
```

**Quality checks before output:**
- Each candidate is evaluated against the stated need, not in the abstract
- Comparison table uses consistent criteria across all candidates
- Recommendation has a clear rationale tied to the evaluation
- Sources are cited for claims about maintenance health, adoption, or features
- Coverage is honest — note what you couldn't verify

---

## Guidelines

- **Evaluate fit first** — a popular library that doesn't solve your problem is irrelevant. Filter by fit before evaluating anything else.
- **Check maintenance signals, not just GitHub stars** — recent commits, issue response time, release cadence, and bus factor reveal more than star count.
- **Note bus factor** — single-maintainer projects carry risk regardless of quality. Flag it, but don't automatically disqualify.
- **Distinguish maturity from popularity** — a stable, focused tool with 500 stars may beat a trending one with 50k. Maturity is about stability, not attention.
- **Don't recommend "build" when a good solution exists** — the default should be adopt or adapt unless nothing fits. Building custom has ongoing maintenance costs that developers routinely underestimate.
- **Acknowledge staleness** — web search results may be months old. Training knowledge has a cutoff. Note this honestly; don't present uncertain information as current fact.
- **Check the current stack first** — the best dependency is one you already have. If the project's framework or an existing dependency covers the need, say so before surveying external options.
- **Credit:** This spell applies prior art search (US Patent Act, 1790), systematic review (Cochrane Collaboration, 1993), Technology Radar (ThoughtWorks, 2010), CHAOSS metrics (Linux Foundation, 2017), and build-vs-buy analysis (software engineering practice).

---

## Example Usage

```
@spell-prior-art markdown parsing in Python
@spell-prior-art real-time WebSocket framework for Node
@spell-prior-art state management for React
@spell-prior-art CLI argument parsing in Rust
```
