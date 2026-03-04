# Ritual: Doc-Structure

**Spells:** diataxis → progressive-disclosure
**Type:** Sequential
**Plan mode:** NOT compatible (both spells produce files as primary output)

**Use when:** You need to audit/restructure documentation by purpose (Diataxis quadrants) AND by detail level (progressive disclosure). Diataxis splits by quadrant; progressive-disclosure layers by depth.

**Important:** This ritual requires edit mode — both spells generate files as their primary output. If running in plan mode, exit plan mode first.

---

## Phase 1: diataxis

Run `diataxis` with the user's topic as the argument.

**Full spell execution** — run the entire diataxis process without modification.

---

## Bridge: diataxis → progressive-disclosure

**Extract** from diataxis output:
- **QUADRANT COVERAGE** — which quadrants exist and which are missing
- **GAPS** — identified documentation gaps
- **RECOMMENDATIONS** — prioritized improvements
- **FILES** — generated files (Generate/Restructure modes) or file-to-quadrant mapping from QUADRANT COVERAGE and MIXED DOCUMENTS (Audit mode)

**Reframe** as input for progressive-disclosure:
- Topic becomes: "layer <topic> documentation by detail level, starting from the Diataxis structure"
- Context: Carry forward the quadrant assignments (so progressive-disclosure knows which files serve which purpose), the gaps (so progressive-disclosure can note which detail levels are missing for which quadrants), and the recommendations (so progressive-disclosure can incorporate them into the layering). Each Diataxis quadrant may need its own progressive-disclosure stack — a tutorial might have overview → walkthrough → deep dive, while reference might have cheatsheet → API docs → implementation notes.

**Gate check:**
- If diataxis produced a clear quadrant structure → proceed normally, progressive-disclosure will layer each quadrant by depth
- If diataxis found documentation is severely lacking (3+ empty quadrants) → reframe progressive-disclosure to focus on the one populated quadrant first, then suggest building the others
- If diataxis audit found no documentation exists → stop and report to user; generating docs from scratch should start with diataxis generate mode, then re-run the ritual

**User checkpoint:** Present the bridge content and ask:
1. Proceed with progressive-disclosure using this framing
2. Modify the framing (focus on specific quadrants)
3. Skip to synthesis (diataxis output is sufficient)
4. Redirect to a different spell

---

## Phase 2: progressive-disclosure

Run `progressive-disclosure` with the reframed topic from the bridge.

**Full spell execution** — run the entire progressive-disclosure process without modification.

---

## Synthesis

Produce a synthesis that cross-references the two outputs:

**Convergent findings:** Where Diataxis quadrant boundaries and progressive-disclosure depth levels align naturally (e.g., tutorials naturally map to the overview/walkthrough levels, reference naturally maps to the detailed/complete levels).

**Divergent findings:** Where the two frameworks tension each other (e.g., if progressive-disclosure suggests combining tutorial and reference at the overview level, but Diataxis insists they stay separate — that tension reveals a documentation design decision to make).

**Emergent insights:** Patterns visible only in combination — the combined view may reveal that some documentation serves dual purposes across both dimensions (a document that's both "explanation" quadrant and "deep dive" depth level), creating a natural entry point into the documentation system.
