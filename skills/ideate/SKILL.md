---
name: ideate
description: Step 4 of the rh research harness. Sets the publication standard for the run's five venues, has five independent proposers write 100+ ideas, screens and checks them, picks the top 5 ideas per venue, and emails the researcher.
argument-hint: [run folder]
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Tools: `${CLAUDE_PLUGIN_ROOT}/tools/`. Run: $ARGUMENTS
Needs: `venues.md`, `lit-rev.md`, `refs.bib`.

## 1. Standard (`rh:evaluator`)
The evaluator writes `eval_rl.md`:
- **Core criteria, with weights**: importance of the question to policymakers, practitioners or the public; novelty against the literature review; soundness of the design; data availability (open data, then quick online collection such as MTurk or Prolific, then restricted data, then fieldwork); feasibility and time cost, including ethics review; size of the contribution.
- **One section per venue**: its taste, its bar, what wins there, what gets desk-rejected, and the methods it favors.
- **Calibration**: score 3 of each venue's recently published papers (from `venues/`) against that venue's section. If the rubric would reject papers the venue actually published, adjust it and note the change.

## 2. Proposals (5 `rh:proposer`s in parallel)
Give P1–P4 the grounded track, each with a different share of the strands in `lit-rev.md`; give P5 the out-of-the-box track. Each writes at least 21 cards to `ideas/P<n>.jsonl`. When all five are done, check that every line parses as JSON, merge them into `ideas.jsonl`, and delete `ideas/`. That's at least 100 ideas, about 20% of them out-of-the-box.

## 3. Screen (`rh:evaluator`)
The evaluator reads `ideas.jsonl` and writes `screen.md`: groups of near-duplicates (keeping the strongest of each), a score on each core criterion and a weighted total for every idea, and a shortlist of about 20 grounded and 5 out-of-the-box ideas.

## 4. Check the shortlist (5 `rh:scout`s in parallel, about 5 ideas each)
Each scout writes `checks/S<n>.md`, with, for each of its ideas:
- **Prior art**: has this question already been answered? Search beyond `refs.bib`, and cite what you find.
- **Data**: does the named dataset exist, can we get it, and does it have the variables the idea needs? For ideas that collect new data: a feasible sample size, a rough cost, and whether ethics review (IRB) is needed.
- **Verdict**: CLEAR, PRIOR ART or DATA PROBLEM, with a one-line reason.

## 5. Rank per venue (one `rh:evaluator` per venue, in parallel)
Each evaluator gets the core criteria, one venue's section, the shortlist and the checks, and writes `rank/<venue-slug>.md`: the venue's top 5 ideas, leaving out PRIOR ART and DATA PROBLEM ideas. One of the five slots is reserved for the best out-of-the-box idea, if one clears the venue's minimum bar. For each pick: why it fits this venue, and its main risk. An idea may be picked for several venues.

## 6. Report
Write `eval_fnl.md` and render it to HTML: the counts (proposed, distinct after merging duplicates, shortlisted, cleared by the checks), then for each venue its top 5 ideas, each with a summary (question, gap, method, data, contribution), its scores, its fit and its risk. Update `state.md`. Email the researcher the top picks per venue and the next step: run `/rh:design` with the idea(s) and venue(s) to pursue, plus any questions to stress-test them. Then stop.
