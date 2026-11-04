---
name: venues
description: Steps 1-2 of the rh research harness. Starts a run from a topic, target journal or research direction, and finds the five best venues to target, with acceptance rates, formatting rules and a writing template drawn from recent papers.
argument-hint: <topic, target journal, or research direction>
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Tools: `${CLAUDE_PLUGIN_ROOT}/tools/`.

Input: $ARGUMENTS

## 1. Start the run
If the input doesn't make the discipline and direction clear, ask one clarifying question first. Then create `$RH_ROOT/_runs/<YYYY-MM-DD>-<slug>/` (slug: 2–5 words from the input), copy `${CLAUDE_PLUGIN_ROOT}/templates/run-state.md` there as `state.md`, and fill in the input.

## 2. Long list and top 5
Find 15–30 candidate venues (journals and conference proceedings) that publish this kind of work. Rank them by reputation using the ranking list this field actually relies on (e.g. ABS/AJG, FT50, UTD24, CORE, JCR quartiles), and name the list. Choose the top 5 viable venues, weighing reputation against acceptance rate, review time and fit. If the researcher named a journal, it's one of the five.

## 3. Profiles (5 `rh:scout`s in parallel, one per venue)
Each scout writes `venues/<venue-slug>.md` and `venues/<venue-slug>.bib`, covering:
- Aims, scope and taste: what the venue publishes, and what it says it doesn't want.
- Acceptance rate, time to first decision and desk-rejection rate, each with a source or "not published".
- Submission rules: length limits, formatting, abstract, anonymization, data and code policy, with a link to the author guidelines.
- From at least 10 research articles published in the last 3 years, each with a verified entry in the `.bib`: typical length in words, dominant methods, section names in order with their share of the paper, and common practices (e.g. a "Figure 1" research model, a hypotheses section, an online appendix of robustness checks).
- A brief template: the section sequence, with a target word count for each.

## 4. Assemble
Write `venues.md`: the ranked long list (one line per venue), the five profiles, and a short comparison of the five on time cost against publication benefit. Merge the scouts' `.bib` files into `refs.bib` (one key per work) and run `verify_bib.py` on it. Render `venues.md` to HTML. Update `state.md`, and tell the researcher where the run folder is and that `/rh:litreview` comes next.
