# Technology Evaluation — Skill Reference for AI Assistants

> Structured criteria for evaluating libraries, tools, and frameworks. Use this reference when surveying existing solutions before building, or when comparing technology options for adoption.

## Evaluation Criteria

| Criterion | What to assess | How to check |
|-----------|---------------|--------------|
| **Fit** | Does it solve the actual need? Not adjacent — the real requirement. | Map the user's must-haves against the tool's feature list. Run a spike or read the API surface. |
| **Maturity** | Stable API? Semantic versioning? Production-ready? | Check version number, changelog, breaking change history, deprecation policy. |
| **Maintenance** | Active development? Responsive maintainers? | Recent commits, issue response time, release cadence, bus factor. See Health Signals below. |
| **Community** | Adoption signals? Help available? | npm/PyPI download counts, Stack Overflow questions, Discord/forum activity, docs quality. |
| **Integration** | Compatible with current stack? Reasonable footprint? | Check dependency tree, bundle size, required runtime, framework compatibility, migration path. |
| **License** | Permissive? Copyleft? Commercial-use compatible? | Read the LICENSE file. See License Compatibility below. |

### Weighting

Not all criteria matter equally for every decision:

- **Evaluating a core dependency** (ORM, framework) → weight Maturity, Maintenance, Integration heavily
- **Evaluating a utility** (date formatting, color conversion) → weight Fit and Integration; Maintenance matters less for stable, focused tools
- **Evaluating for a prototype** → weight Fit and ease of Integration; Maturity can be lower
- **Evaluating for regulated/enterprise use** → weight License, Maturity, and Maintenance heavily

## Maintenance Health Signals

Inspired by [CHAOSS](https://chaoss.community/) community health metrics:

| Signal | Healthy | Warning | Red flag |
|--------|---------|---------|----------|
| **Last commit** | Within 3 months | 3-12 months ago | >1 year ago |
| **Issue response time** | Maintainer responds within a week | Weeks to months | Issues pile up with no response |
| **Release cadence** | Regular releases (monthly/quarterly) | Sporadic but present | No releases in >1 year |
| **Breaking changes** | Documented in changelog, migration guide provided | Breaking changes without migration path | Frequent undocumented breaking changes |
| **Bus factor** | 3+ active contributors | 2 contributors | Single maintainer |
| **CI/CD** | Tests run on PRs, CI passing | CI exists but spotty | No CI, no tests |
| **Documentation** | API docs, guides, examples | README only | Outdated or missing docs |

### Bus Factor

A single-maintainer project isn't automatically bad — many excellent tools have one author. But it carries risk:

- If the maintainer loses interest, gets a new job, or becomes unavailable, the project stalls
- Assess whether the project is "done" (stable, feature-complete, unlikely to need changes) vs. actively evolving
- A stable, focused tool with one maintainer (e.g., a date parser) is lower risk than a rapidly evolving framework with one maintainer

## Maturity Assessment

Adapted from ThoughtWorks Technology Radar rings:

| Ring | Criteria | Implication |
|------|----------|-------------|
| **Adopt** | Production-proven, stable API, active maintenance, broad adoption, clear docs | Safe default choice. Use unless there's a specific reason not to. |
| **Trial** | Promising, some production use, API mostly stable, growing adoption | Worth using in non-critical paths. Expect minor rough edges. |
| **Assess** | Interesting approach, limited production use, API may change, small community | Investigate for future use. Don't build critical features on it yet. |
| **Hold** | Known issues, declining maintenance, better alternatives exist, or too immature | Avoid for new projects. Plan migration if already using. |

### Distinguishing Maturity from Popularity

- A tool with 50k GitHub stars and 200 open bugs may be less mature than one with 500 stars and zero open bugs
- Download counts measure adoption, not quality — popular tools can be immature, and mature tools can be niche
- Look at the ratio of issues opened to issues resolved, not just the star count

## License Compatibility Quick Reference

| License | Commercial use | Derivative work | Must share source? | Patent grant |
|---------|---------------|----------------|-------------------|-------------|
| **MIT** | Yes | Yes | No | No explicit grant |
| **Apache 2.0** | Yes | Yes | No | Yes |
| **BSD 2/3-Clause** | Yes | Yes | No | No explicit grant |
| **ISC** | Yes | Yes | No | No explicit grant |
| **GPL v2/v3** | Yes, but conditions | Must be GPL | Yes, if distributed | v3 only |
| **LGPL** | Yes | Proprietary OK if dynamically linked | Only modifications to LGPL code | No explicit grant |
| **AGPL** | Yes, but conditions | Must be AGPL | Yes, even for network use | Yes (v3) |
| **BSL / SSPL** | Restrictions apply | Varies | Varies | Varies |
| **Unlicense / CC0** | Yes | Yes | No | No |

**Quick rules:**
- MIT, Apache 2.0, BSD, ISC → generally safe for any use
- GPL → your project must also be GPL if you distribute it
- AGPL → your project must be AGPL even for server-side use
- BSL/SSPL → read the specific terms; often restrict competing services

## Red Flags Checklist

Before recommending any tool, check for these:

- [ ] **Last commit >1 year ago** — may be abandoned (unless it's a stable, "done" tool)
- [ ] **No tagged releases** — suggests informal development practices
- [ ] **No tests** — quality and reliability are unknown
- [ ] **README-only docs** — API surface may be poorly thought out
- [ ] **Single contributor + active development** — bus factor risk if the project is evolving
- [ ] **Known CVEs unfixed** — security risk; check via `npm audit`, `pip-audit`, or GitHub security advisories
- [ ] **No LICENSE file** — legally ambiguous; default copyright applies (you can't use it)
- [ ] **Massive dependency tree** — supply chain risk, bundle size, maintenance burden
- [ ] **Deprecated by author** — check README header, npm deprecation notices, PyPI classifiers

## Reporting Template

> **Note:** The spell template (`prior-art.md.template`) is the canonical source for output format. This template is a simplified reference; defer to the spell if they differ.

Use this format when reporting technology evaluation results:

```
EVALUATION: <TOOL/LIBRARY NAME>
══════════════════════════════════════════════════════════════

Fit:         <how well it addresses the stated need>
Maturity:    <Adopt | Trial | Assess | Hold>
Maintenance: <healthy | warning signs | red flags>
Community:   <adoption signals, docs quality>
Integration: <compatibility with current stack>
License:     <license name — commercial use implications>

Red flags:   <any from checklist, or "None identified">

Verdict:     <recommend | consider | avoid>
Rationale:   <why>
```
