# Solution Landscape — Skill Reference for AI Assistants

> Methodology for surveying existing solutions before building. Use this reference when conducting a prior art search, evaluating build-vs-buy decisions, or comparing technology options systematically.

## Structuring a Technology Survey

### Define the Need Before Searching

The most common mistake in technology evaluation is searching for solutions before understanding the problem. A developer who says "I need a state management library" has already skipped the crucial step of defining what state they're managing, what constraints they have, and what behaviors they need.

**Before searching, clarify:**

1. **Capability** — What do you actually need to do? (Not what tool you think you need)
2. **Constraints** — Language, platform, license, performance requirements, bundle size limits
3. **Must-haves** — Non-negotiable requirements (if a solution doesn't have these, it's out)
4. **Nice-to-haves** — Preferred but flexible (TypeScript types, tree-shaking support, small API surface)

### Separate Requirements from Preferences

| Category | Example | Impact on evaluation |
|----------|---------|---------------------|
| **Hard constraint** | "Must run on Node 18+" | Eliminates candidates that don't meet it |
| **Must-have** | "Must support WebSocket reconnection" | Core feature — solution must have it |
| **Nice-to-have** | "TypeScript types included" | Tiebreaker between otherwise-equal options |
| **Preference** | "I've heard good things about X" | Acknowledge but don't let it bias the search |

### Scope the Search

- **Too narrow:** "Find a React hook for debounced search with TypeScript" → misses non-hook solutions that might be better
- **Too broad:** "Find a way to handle user input" → too many results to evaluate
- **Right scope:** "Debounced search input handling for a React + TypeScript app" → clear capability, clear constraints

## Search Strategy

### Where to Look

| Source | What it's good for | Limitations |
|--------|-------------------|-------------|
| **Package registries** (npm, PyPI, crates.io, Go pkg) | Finding packages by keyword, checking download stats | Popularity ≠ quality; many abandoned packages |
| **GitHub** | Source code, issues, contributor activity, stars | Stars ≠ quality; trending ≠ mature |
| **Official framework docs** | Recommended or built-in solutions | May not cover third-party alternatives |
| **Comparison blog posts** | Side-by-side evaluations, benchmarks | May be outdated, sponsored, or biased |
| **Stack Overflow** | Common solutions, known gotchas | Answers may be outdated; accepted ≠ best |
| **Awesome lists** | Curated collections by category | May be unmaintained; inclusion criteria vary |
| **Technology Radar** (ThoughtWorks) | Industry-vetted assessment of tools and techniques | Updated quarterly; may not cover niche tools |

### Forming Effective Queries

| Pattern | Example |
|---------|---------|
| `<capability> library <language>` | "markdown parsing library python" |
| `<capability> framework comparison <year>` | "WebSocket framework comparison 2025" |
| `best <capability> tool <language/platform>` | "best CLI argument parser rust" |
| `<library A> vs <library B>` | "zod vs yup validation" |
| `<capability> <language> site:github.com` | "state machine typescript site:github.com" |
| `<framework> recommended <capability>` | "django recommended authentication" |

### Search Sequence

1. **Check the current stack first** — does the framework/language already provide this capability?
2. **Search package registries** — what's available, what's popular?
3. **Search for comparisons** — has someone already evaluated the options?
4. **Check official docs** — does the framework recommend a specific approach?
5. **Evaluate top candidates** — deep-dive on the 3-5 most promising options

## Comparison Matrix Methodology

### Building a Fair Comparison

1. **Use the same criteria for all candidates** — don't evaluate Library A on features and Library B on popularity
2. **Weight criteria by importance** — Fit matters more than star count; License matters more for enterprise
3. **Avoid anchoring bias** — don't evaluate all candidates relative to the first one you found
4. **Include "build custom" as a candidate** — it's always an option; make it compete on the same criteria
5. **Note what you couldn't verify** — staleness, untested claims, missing benchmarks

### Comparison Table Format

```
| Criterion     | Candidate A | Candidate B | Candidate C | Build Custom |
|---------------|-------------|-------------|-------------|--------------|
| Fit           |             |             |             |              |
| Maturity      |             |             |             |              |
| Maintenance   |             |             |             |              |
| Community     |             |             |             |              |
| Integration   |             |             |             |              |
| License       |             |             |             |              |
```

Format cells as best fits the data — qualitative labels, brief prose, or a mix. Aim for scannability over precision.

## Build vs. Buy Decision Framework

### When to Build Custom

- **Core differentiator** — the capability is what makes your product unique; outsourcing it means outsourcing your advantage
- **Unusual requirements** — your constraints are so specific that no existing solution fits without heavy modification
- **No adequate solution exists** — you've searched thoroughly and nothing meets the must-haves
- **Maintenance is acceptable** — you have the team and time to maintain a custom solution long-term
- **Integration cost exceeds build cost** — adapting an existing solution would require more work than building from scratch

### When to Adopt (Buy / Use Existing)

- **Commodity capability** — authentication, logging, date formatting — things that aren't your competitive advantage
- **Well-served space** — multiple mature, actively maintained options exist
- **Time pressure** — shipping matters more than having a perfect custom solution
- **Small team** — you can't afford to maintain infrastructure that someone else maintains for free
- **Compliance or security** — established libraries have been audited; your custom code hasn't

### When to Adapt (Fork / Customize)

- **Good foundation but missing pieces** — a library does 80% of what you need
- **Extension points available** — the library was designed for customization (plugins, middleware, hooks)
- **Upstream is healthy** — you can pull updates and contribute back
- **The customization is well-scoped** — you're adding, not rewriting

### Decision Signals

| Signal | Suggests |
|--------|----------|
| "Every library I find is close but not quite right" | Adapt — find the closest fit and extend it |
| "There are 15 libraries and they're all good" | Adopt — this is a solved problem; pick the best fit |
| "Nothing exists for this specific combination of requirements" | Build — but verify the requirements are real, not over-specified |
| "We'd need to fork and maintain it ourselves" | Build — forking without upstreaming is just building with extra steps |
| "The existing solution works but we want more control" | Pause — is "more control" a real need or NIH syndrome? |

## Common Pitfalls

| Pitfall | Description | Mitigation |
|---------|-------------|------------|
| **Anchoring bias** | Over-weighting the first solution you find because it sets the frame of reference | Evaluate at least 3 candidates before forming a preference |
| **Popularity bias** | Choosing the most-starred/downloaded option regardless of fit | Stars measure awareness, not suitability. Evaluate fit first. |
| **Recency bias** | Preferring newer tools because they're "modern" | Newer isn't better. Maturity, stability, and ecosystem matter. |
| **Sunk cost** | Sticking with a bad choice because you've already invested time | The time is gone either way. Evaluate current options objectively. |
| **NIH syndrome** | Building custom because "we can do it better" when an adequate solution exists | Ask: would you build your own database? Your own HTTP library? Where's the line? |
| **Analysis paralysis** | Evaluating endlessly instead of choosing | Set a time box. Cap candidates at 5-7. "Good enough" beats "perfect but never chosen." |
| **Cargo culting** | Adopting because "everyone uses it" without evaluating fit | "Netflix uses it" doesn't mean you should. Your constraints are different. |

## Reporting Template

> **Note:** The spell template (`prior-art.md.template`) is the canonical source for output format. This template is a simplified reference; defer to the spell if they differ.

Use this format when reporting landscape survey results:

```
PRIOR ART: <CAPABILITY/NEED>
══════════════════════════════════════════════════════════════

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

COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<Markdown table comparing candidates>

RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Verdict: <adopt | adapt | build>
Rationale: <why>
Next steps: <what to do>
```
