# Prior Art Search & Technology Evaluation

## The Problem

A developer needs date parsing in their Node.js app. They spend two days writing a custom parser that handles ISO 8601, relative dates, and timezone conversion. It works. Then a colleague mentions that `date-fns` already does all of this, has been maintained for eight years, has full test coverage, and handles edge cases the custom parser hasn't even considered yet. Two days of work — and the ongoing maintenance burden — could have been avoided by spending ten minutes checking what already exists.

This isn't a one-off mistake. It's a pattern. Teams adopt three different HTTP clients because nobody checked what was already in the project. A startup builds a custom authentication system when Passport.js or Auth0 would have covered it. An engineer picks a library because they saw it in a conference talk, without checking that it was abandoned six months later. The problem isn't laziness — it's that there's no systematic process for surveying existing solutions before committing to one.

AI assistants make the gap wider. Ask an AI to help you build a feature, and it'll start generating code immediately. It won't pause to ask whether something already exists that solves the problem. It won't check npm or PyPI. It won't evaluate maintenance health or license compatibility. It'll write you a custom solution because that's what you asked for — even when a better answer is "use the library that 10,000 other projects already depend on."

## How It Helps

A prior art search does four things:

1. **Surveys what exists** — systematically searches package registries, GitHub, official docs, and comparison articles instead of relying on whatever you've heard of
2. **Evaluates with structured criteria** — fit, maturity, maintenance health, community, integration compatibility, and license — not just "which has more stars"
3. **Compares fairly** — same criteria applied to all candidates in a comparison matrix, preventing anchoring to the first option found
4. **Recommends a path** — adopt (use as-is), adapt (use and customize), or build custom — with rationale tied to the evaluation

The output is a landscape survey, not a recommendation engine. It gives you the information to make a good decision, structured so you can scan it quickly and defend your choice to your team.

## Why It Works

The structured format prevents the cognitive biases that plague technology decisions:

- **Anchoring bias** — evaluating everything relative to the first option you found. The comparison matrix forces equal evaluation across all candidates.
- **Popularity bias** — choosing the most-starred option regardless of fit. Evaluating fit first means a 500-star library that solves your problem beats a 50k-star one that doesn't.
- **NIH syndrome** — building custom because "we can do it better." Including "build custom" as an explicit candidate in the comparison forces it to compete on the same criteria as existing solutions, and it usually loses on maintenance cost.
- **Recency bias** — preferring newer tools because they seem modern. The maturity assessment (Adopt/Trial/Assess/Hold) values stability over novelty.

The evaluation criteria matter too. Checking maintenance health — commit recency, issue response time, bus factor — catches the "looks great on the README but hasn't been updated in two years" problem. Checking license compatibility catches the "we shipped with AGPL code and didn't realize" problem. These aren't optional add-ons; they're the difference between a good technology choice and a future crisis.

## In Practice

**Patent prior art search.** The US Patent Act (1790) established the concept of prior art — before you can patent an invention, you must demonstrate that it doesn't already exist. Patent examiners conduct systematic searches of existing patents, publications, and products. The principle is the same in software: before you build, check what exists. The consequence of skipping it in patents is legal (your patent gets invalidated). The consequence in software is practical (you waste time building what already exists, or worse, you ship an inferior version).

**Academic literature review.** Before researchers conduct a study, they perform a systematic literature review — a structured survey of existing research to avoid duplicating work and to understand the current state of knowledge. The PRISMA methodology (Preferred Reporting Items for Systematic Reviews, 2009) standardizes this process: define the search criteria, search multiple databases, screen for relevance, extract data, synthesize findings. A prior art search for software follows the same pattern: define the need, search multiple sources, screen candidates, evaluate, recommend.

**ThoughtWorks Technology Radar.** Since 2010, ThoughtWorks has published a quarterly Technology Radar that evaluates tools, techniques, platforms, and languages across four rings: Adopt, Trial, Assess, and Hold. Each entry includes a blurb explaining why it's in that ring. The Radar is influential because it applies structured evaluation — not just "this is popular" but "this is mature enough for production" or "this has known issues, avoid for new projects." The prior-art spell adapts this ring model for individual technology decisions.

**Architecture Decision Records (ADRs).** When teams document their technology choices using ADRs, they typically include a "considered alternatives" section — a brief survey of what else was evaluated and why it was rejected. The prior-art spell produces exactly this kind of artifact: a structured comparison that explains not just what you chose, but what you considered and why you didn't choose it. This makes the decision auditable, defensible, and revisitable when circumstances change.

## The Command

The `/spell:prior-art <need>` command applies this concept by:

1. Parsing the capability or problem to survey
2. Defining the actual need — capability, constraints, must-haves, nice-to-haves — before searching
3. Surveying the landscape via web research, codebase analysis, and built-in knowledge
4. Evaluating candidates against six structured criteria (fit, maturity, maintenance, community, integration, license)
5. Producing a structured survey: need definition, candidate evaluations, comparison matrix, and recommendation (adopt, adapt, or build)

The spell checks the current project first — the best dependency is one you already have. It caps candidates at 5-7 to prevent analysis paralysis, filters by fit first to avoid popularity bias, and includes honest staleness warnings when information may be outdated.

## Background

The concept of prior art originated in patent law. The US Patent Act of 1790 required inventors to demonstrate that their invention was novel — that no "prior art" existed. This principle has been refined over two centuries and is now a core part of patent examination worldwide. The underlying idea — check what exists before claiming novelty — applies far beyond patents.

Systematic reviews in academia formalized the process of surveying existing work. The Cochrane Collaboration (1993) established rigorous methods for reviewing medical research, and the PRISMA guidelines (2009) standardized the reporting format. These methods ensure that reviews are reproducible, comprehensive, and transparent about their search strategy and limitations.

In software, ThoughtWorks introduced the Technology Radar in 2010, applying structured evaluation to technology choices. The CHAOSS project (Community Health Analytics in Open Source Software), founded by the Linux Foundation in 2017, established metrics for evaluating open source project health — contributor diversity, responsiveness, release cadence — that go beyond simple popularity measures. Build-vs-buy analysis has been a standard practice in software engineering since the industry began, though it's rarely formalized into a repeatable process.

## Further Reading

- [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar) — Quarterly technology evaluation with Adopt/Trial/Assess/Hold rings
- [CHAOSS Community](https://chaoss.community/) — Open source project health metrics and analytics
- [PRISMA Guidelines](https://www.prisma-statement.org/) — Systematic review methodology (academic, but the structure transfers)
- [Build vs. Buy](https://martinfowler.com/articles/is-quality-worth-cost.html) — Martin Fowler on why cutting corners costs more than doing it right
- [Architecture Decision Records](https://adr.github.io/) — Lightweight format for documenting technology choices
- [Choosing the Right Technology](https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/) — Joel Spolsky's counterpoint on when to build custom (the exception that proves the rule)
