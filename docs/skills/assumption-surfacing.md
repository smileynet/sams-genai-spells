# Assumption Surfacing & Pre-Mortem Analysis — Skill Reference for AI Assistants

> Techniques for uncovering hidden assumptions and unexamined failure modes. Use this reference when probing for blind spots in a plan, decision, or research topic.

## Assumption Surfacing (SAST)

Strategic Assumption Surfacing and Testing (Mason & Mitroff, 1981) is a method for making implicit assumptions explicit, then stress-testing them.

### Core Process

1. **Surface** — List assumptions underlying a plan, decision, or belief. Ask: "What must be true for this to work?"
2. **Rate** — Score each assumption on two axes:
   - **Importance** — How much does the plan depend on this being true? (1 = peripheral, 5 = load-bearing)
   - **Certainty** — How confident are we that this is actually true? (1 = speculation, 5 = verified fact)
3. **Triage** — Focus on assumptions that are high-importance but low-certainty. These are the dangerous ones: load-bearing and unverified.
4. **Test** — For each dangerous assumption, identify what evidence would confirm or refute it, and how to gather that evidence.

### The Importance/Certainty Matrix

```
                    High Certainty
                         │
     Safe bets           │  Verified foundations
     (monitor)           │  (proceed with confidence)
                         │
  Low Importance ────────┼──────── High Importance
                         │
     Background noise    │  ⚠ DANGER ZONE ⚠
     (ignore)            │  (test immediately)
                         │
                    Low Certainty
```

The danger zone — high importance, low certainty — is where blind spots live. These assumptions are load-bearing (the plan fails without them) but unverified (nobody has checked whether they're actually true).

### Assumption Categories

When surfacing assumptions, check each of these categories systematically:

| Category | What to look for | Example |
|----------|-----------------|---------|
| **Technical** | Performance, scalability, compatibility, API stability | "The database can handle 10x current load" |
| **Organizational** | Team skills, bandwidth, buy-in, decision authority | "The team has time to learn a new framework" |
| **Market/User** | User behavior, demand, willingness to adopt | "Users will migrate from the old system voluntarily" |
| **Temporal** | Timeline feasibility, sequence dependencies, deadlines | "The API will be stable before we need to ship" |
| **Resource** | Budget, infrastructure, third-party availability | "The cloud provider's free tier covers our needs" |
| **Regulatory** | Compliance, legal, licensing, data governance | "GDPR doesn't apply to this use case" |

### Common Hiding Places for Assumptions

Assumptions hide behind:
- **Jargon and abstractions** — "We'll use microservices" (assumes: team knows how to operate them, network is reliable enough, deployment infra exists)
- **"Obviously" statements** — anything prefixed with "obviously," "clearly," or "of course" is an untested assumption wearing a disguise
- **Success stories** — "Company X did it this way" (assumes: your context matches theirs)
- **Defaults** — technology, process, or organizational choices inherited without re-evaluation

## Pre-Mortem Analysis

Developed by Gary Klein (1998), the pre-mortem is a structured exercise for imagining failure before it happens.

### Why It Works

Standard risk assessment asks "What *might* go wrong?" — a hypothetical that triggers self-censoring. People don't want to seem negative or challenge the plan.

Pre-mortem uses **prospective hindsight**: "The project *has failed*. It is a year from now, and the project was a disaster. What happened?"

This reframing:
- **Legitimizes pessimism** — you're explaining a known failure, not being negative
- **Activates different cognitive processes** — explaining a known outcome vs. predicting an unknown one uses different mental models
- **Increases failure identification by 30%** — Mitchell, Russo & Pennington (1989) demonstrated that prospective hindsight generates more plausible explanations than prospective foresight

### Protocol

1. **Frame the failure** — "It is [future date]. [The project/migration/decision] has failed spectacularly. Not a minor setback — a complete disaster."
2. **Generate explanations** — Each participant independently writes down reasons for the failure. No discussion yet.
3. **Share and collect** — Go around the room. Each person shares one reason per round. Continue until all reasons are surfaced.
4. **Consolidate** — Group similar reasons. Identify themes.
5. **Prioritize** — Which failure modes are most plausible? Which would be most damaging?
6. **Mitigate** — For the top failure modes, identify what could be done now to prevent or detect them.

### Critical Design Choices

- **Use "has failed" language, not "might fail"** — The certainty framing is the entire point. "Might fail" lets people hedge; "has failed" forces commitment to the scenario.
- **Multiple perspectives** — Klein emphasizes excluding dominant voices who discourage dissent. For AI application: explicitly adopt different stakeholder perspectives (end user, operator, maintainer, adversary, regulator) rather than analyzing from a single viewpoint.
- **Search for documented failures** — Don't just imagine failure; look for cases where similar efforts actually failed. Real failures are more convincing and more instructive than hypothetical ones.

## Red Team Thinking

Red teaming originated in military war games and was formalized by intelligence agencies (notably the CIA's Red Cell, established after 9/11) to challenge institutional assumptions.

### Authentic vs. Performative Dissent

Charlan Nemeth (2001) demonstrated that **assigned devil's advocates are dramatically less effective than authentic dissenters**:

- Assigned devil's advocates role-play opposition but don't actually believe it. The group knows this and dismisses their arguments.
- Authentic dissenters hold genuinely different views and argue with conviction. This stimulates real divergent thinking in the group.

**For AI application:** Don't generate token objections. Generate genuinely different framings with substantive reasoning. Each contrarian position must include:
- The alternative framing (not just "this might not work" but "here's a different way to see this")
- The reasoning behind it (why someone would authentically hold this view)
- What evidence would support it

### Common Antipatterns

**AP: THE POLITE BRAINSTORM**
Running a pre-mortem as "what could go wrong?" instead of "it has failed — what happened?" The hypothetical framing triggers self-censoring and produces generic, surface-level risks.

**AP: THE HIPPO EFFECT**
(Highest-Paid Person's Opinion) Single-perspective analysis where one dominant framing goes unchallenged. For AI: analyzing only from the most obvious stakeholder viewpoint without considering operators, adversaries, regulators, or end users.

**AP: THE DESIGNATED CONTRARIAN**
Performing opposition without conviction. Token objections the group dismisses because they lack substance. For AI: listing generic risks ("it might be slow," "users might not adopt it") without genuine reasoning or alternative frameworks.

**AP: THE FLAT LIST**
Surfacing assumptions without ranking by importance and certainty. Twenty unranked items produce analysis paralysis. The importance/certainty matrix exists precisely to prevent this — use it.

## Checklist: Common Blind Spot Patterns

When probing for blind spots, systematically check for these commonly overlooked areas:

- [ ] **Second-order effects** — What happens as a consequence of the primary change? (Migration succeeds, but downstream systems break)
- [ ] **Stakeholders not in the room** — Whose perspective is missing from the analysis? (Operations team, end users, security, legal)
- [ ] **Maintenance costs** — What's the ongoing cost after initial implementation? (Monitoring, updates, on-call burden)
- [ ] **Adoption barriers** — What prevents people from actually using the solution? (Learning curve, workflow disruption, incentive misalignment)
- [ ] **Regulatory changes** — What legal or compliance shifts could affect the plan? (GDPR-style regulations, licensing changes, industry standards)
- [ ] **Dependency risks** — What external systems, services, or people does the plan depend on? (Third-party APIs, key personnel, vendor stability)
- [ ] **Temporal assumptions** — What timeline assumptions are baked in? (Development speed, approval cycles, market windows)
- [ ] **Reversibility** — If this doesn't work, how hard is it to undo? (Data migrations, public API contracts, organizational changes)

## Sources

- Mason, R. & Mitroff, I. (1981). *Challenging Strategic Planning Assumptions*. Wiley.
- Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press.
- Klein, G. (2007). "Performing a Project Premortem." *Harvard Business Review*.
- Mitchell, D., Russo, J., & Pennington, N. (1989). "Back to the future: Temporal perspective in the explanation of events." *Journal of Behavioral Decision Making*.
- Nemeth, C. (2001). "Minority dissent and its hidden benefits." *New Review of Social Psychology*.
- Nemeth, C. (2018). *In Defense of Troublemakers: The Power of Dissent in Life and Business*. Basic Books.
