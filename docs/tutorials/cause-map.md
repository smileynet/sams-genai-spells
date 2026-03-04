# Categorical Cause Decomposition & Fishbone Analysis

## The Problem

A software team has a recurring production incident -- the checkout flow fails intermittently. Each time, someone traces the immediate cause: a timeout here, a null reference there, a cache miss somewhere else. Each gets patched. The incidents keep coming. After six months, someone finally draws out all the incidents on a whiteboard and notices a pattern: they're all downstream effects of the same overloaded database connection pool. But nobody saw it because everyone was tracing individual causal chains (depth-first), never mapping the full landscape of possible causes (breadth-first).

This is what happens when debugging defaults to the obvious methodology: pick a symptom, trace it backward, find a cause, fix it, move on. The approach is correct for any individual incident. It's catastrophically incomplete for systemic problems, because each investigation produces a single thread of reasoning that terminates at the first satisfying explanation. Nobody ever steps back to ask: "what are ALL the things that could cause this?"

AI assistants do 5 Whys naturally -- they trace a single chain from symptom to cause with impressive depth and rigor. But they don't survey. They don't ask "what else could cause this?" across multiple categories. They latch onto the first plausible explanation and trace it deep. This means you fix one cause while five others wait their turn to break production. The AI's depth becomes a liability because it substitutes confidence for coverage.

## How It Helps

Fishbone analysis (also called Ishikawa diagrams or cause-and-effect diagrams) inverts the debugging approach: instead of starting with a symptom and tracing backward through ONE chain, you start with the effect and systematically brainstorm ALL possible causes organized by category. It's breadth-first cause decomposition.

The process:

1. **State the effect clearly** -- this is the "head" of the fish. A vague effect produces vague causes. "Checkout fails intermittently" is better than "something's wrong with checkout."
2. **Select categories that organize the cause space** -- these are the "bones" of the fish. For software: code logic, data/state, dependencies, infrastructure, configuration, process, human factors. For hardware: materials, methods, machines, manpower, measurement, environment (the classic 6M categories).
3. **Brainstorm 3-7 possible causes per category**, grading each on evidence: Confirmed (you have proof), Suspected (you have indicators), or Speculative (plausible but uninvestigated).
4. **Look for cross-category patterns** -- causes that appear in multiple bones are systemic. If "insufficient monitoring" shows up under Infrastructure AND Process AND Human Factors, that's not three problems. That's one problem wearing three hats.
5. **Prioritize by impact x likelihood**, then investigate the top causes.

The key discipline: you populate ALL categories before investigating ANY of them. This prevents the availability bias that makes you fixate on the first plausible cause. You brainstorm broadly, then converge selectively. Breadth first, depth second.

## Why It Works

Three cognitive mechanisms explain why categorical decomposition outperforms unstructured debugging:

**Availability bias** (Tversky & Kahneman, 1973): people overweight causes that come to mind easily. If you've been debugging database issues all week, "database problem" will be your first hypothesis for every new bug -- even when the actual cause is a configuration change or a race condition in the application layer. Categories force you to search domains you wouldn't think of spontaneously. You may not have considered "human factors" until the category heading makes you ask: "could a recent team change or process modification have contributed?"

**Functional fixedness**: once you have a hypothesis, you stop generating alternatives. This is efficient when you're right and disastrous when you're wrong. Psychologists call it premature closure -- the tendency to treat the first adequate explanation as the correct one. The categorical structure requires exhaustive brainstorming before convergence, mechanically preventing premature closure by making the brainstorm phase a separate, mandatory step.

**Externalized problem space**: complex multi-cause problems exceed working memory. You can hold about four independent items in working memory simultaneously (Cowan, 2001). A serious production incident might have fifteen plausible causes across six categories. The fishbone diagram is a cognitive scaffold that holds the full cause landscape visible simultaneously, freeing your working memory for analysis instead of recall.

The quality engineering evidence reinforces these cognitive arguments. Structured brainstorming with categories generates 2-3x more candidate causes than unstructured brainstorming -- this was Ishikawa's original observation from factory quality circles, and it has been replicated across domains. Cross-reference analysis reveals systemic issues that single-chain analysis misses, because systemic issues manifest differently in each category and only become visible when you compare across bones. Evidence grading (Confirmed/Suspected/Speculative) prevents a subtle but common error: treating guesses as facts. When every cause has an explicit evidence grade, "I think it might be the cache" can't silently transform into "it's the cache" as it passes through three meetings.

## In Practice

**Ishikawa at Kawasaki shipyards.** Kaoru Ishikawa developed the fishbone diagram in 1968 at the University of Tokyo, initially applying it to quality control problems at Kawasaki Heavy Industries. Steel plate defects were being addressed one at a time -- welding temperature, material impurities, operator technique. Each fix addressed a real cause of some defects, but the overall defect rate barely moved. The fishbone mapped all cause categories simultaneously: Materials, Methods, Machines, Manpower, Measurement, Environment. The systemic finding: the inspection process itself was generating false passes, so defective plates were entering assembly. No amount of fixing individual welding parameters would have found that, because the problem wasn't in welding. It was in a different category entirely -- Measurement -- that nobody was examining because the symptoms all pointed to Manufacturing.

**Healthcare sentinel events.** The Joint Commission requires fishbone (cause-and-effect) analysis as part of root cause analysis for sentinel events in hospitals. When a patient receives the wrong medication, tracing the single chain (nurse gave wrong drug -> pharmacy labeled wrong -> doctor handwriting illegible) produces a plausible story and a plausible fix: improve the doctor's handwriting, add a label verification step. But the fishbone's categories (People, Process, Technology, Policy, Environment) force a broader examination. Staffing ratios meant the nurse was covering twice the normal patient load. Alert fatigue from too many electronic notifications caused the pharmacy tech to click through a warning. Training gaps meant a new resident didn't know the drug naming convention. The medication error wasn't caused by one thing. It was caused by holes aligning across multiple defensive layers -- which brings us to the next example.

**Swiss Cheese Model.** James Reason's model (1990) of accident causation argues that failures happen when holes in multiple defensive layers align. Each "layer" is a category: design, maintenance, training, equipment, procedure. Any single layer's hole is survivable -- the other layers catch it. Catastrophic failure requires holes in multiple layers to line up simultaneously. A fishbone diagram maps the holes in each layer, making visible the dangerous alignments that single-chain analysis misses. This is why the cross-category pattern detection in step 4 matters so much: a cause that appears in only one category is a local fix, but a cause that spans categories is a systemic vulnerability -- a Swiss cheese alignment waiting for the right trigger.

**Software incident post-mortems.** Google's SRE practices and the broader incident management community use categorical decomposition in post-mortems. The "contributing factors" section of a well-written post-mortem is essentially a fishbone: what in the code, monitoring, deployment pipeline, testing, and human process contributed to this incident? The insight, consistent across thousands of post-mortems, is that no single cause is sufficient. Production incidents are almost never caused by one thing going wrong. They're caused by multiple contributing factors aligning -- a deploy without adequate testing, plus a monitoring gap that delayed detection, plus an unclear runbook that slowed response, plus a retry storm that amplified the impact. Single-chain analysis finds one of these. Categorical decomposition finds all of them.

## The Command

The `/spell:cause-map <problem>` command applies these concepts:

1. Frames the problem as the fishbone "effect" and selects appropriate cause categories based on the domain (software, organizational, process, or custom)
2. Systematically brainstorms causes within each category, grading evidence as Confirmed, Suspected, or Speculative
3. Builds an ASCII fishbone diagram showing the full cause landscape -- all bones, all causes, all evidence grades visible simultaneously
4. Identifies cross-cutting causes (systemic issues appearing across multiple categories) and flags Swiss cheese alignments
5. Prioritizes by impact x likelihood and produces an investigation plan with specific next steps for the highest-priority causes

The output is a cause map, not a diagnosis. It tells you where to look, not what the answer is. The fishbone populates the search space; investigation narrows it. For tracing a specific cause to its root once you've identified it, follow up with `/spell:diagnose`.

## Background

Kaoru Ishikawa (1915-1989) was a Japanese organizational theorist and professor at the University of Tokyo. His 1968 fishbone diagram became one of the Seven Basic Tools of Quality (later codified in ISO 9004). Ishikawa's broader contribution was democratizing quality control -- moving it from specialist statisticians to every worker on the factory floor through simple visual tools. His philosophy was that quality is everyone's responsibility, and the tools for understanding quality problems should be accessible to everyone, not just engineers and managers. The fishbone diagram embodies this: it requires no statistical training, no special software, and no expertise beyond knowledge of the work itself.

James Reason's *Human Error* (1990) introduced the Swiss Cheese Model of accident causation, arguing that accidents result from aligned failures across multiple defensive layers rather than single causes. This framework transformed safety thinking in aviation, healthcare, nuclear power, and eventually software engineering. The model's key contribution is distinguishing between active failures (the immediate trigger) and latent conditions (the systemic weaknesses that make the trigger dangerous). Single-chain analysis finds the active failure. Categorical decomposition finds the latent conditions.

The Seven Basic Quality Tools (fishbone diagrams, check sheets, control charts, histograms, Pareto charts, scatter diagrams, stratification) were popularized by the American Society for Quality (ASQ) and remain standard in manufacturing, healthcare, and software quality. They share a design principle: each tool externalizes a specific type of analysis that's unreliable when done in your head. The fishbone externalizes cause enumeration. The Pareto chart externalizes prioritization. Together, they form a systematic quality analysis workflow that compensates for known cognitive limitations.

## Further Reading

- [Guide to Quality Control](https://en.wikipedia.org/wiki/Kaoru_Ishikawa) -- Ishikawa's original text on quality tools including the fishbone diagram
- [Human Error](https://en.wikipedia.org/wiki/Human_Error_(book)) -- James Reason's Swiss Cheese Model of accident causation
- [Seven Basic Tools of Quality](https://en.wikipedia.org/wiki/Seven_basic_tools_of_quality) -- ASQ reference for the complete quality tool set
- [Google SRE Post-Mortem Culture](https://sre.google/sre-book/postmortem-culture/) -- Categorical analysis in incident management
- [Tversky, A. & Kahneman, D. "Judgment under Uncertainty: Heuristics and Biases" (1974)](https://en.wikipedia.org/wiki/Heuristics_and_Biases) -- The research on availability bias and its effect on causal reasoning
- [Reason, J. "Managing the Risks of Organizational Accidents" (1997)](https://en.wikipedia.org/wiki/Swiss_cheese_model) -- Extended treatment of the Swiss Cheese Model applied to organizational safety
