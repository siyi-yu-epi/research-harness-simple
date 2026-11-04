---
name: review
description: Steps 10-11 of the rh research harness, run inside an idea's project folder. Three independent reviewers vote on whether the results meet the venue's bar; a failed round goes back to the analyst automatically, up to three failures in a row. On a pass, writes res_hum.html and emails the researcher.
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Tools: `${CLAUDE_PLUGIN_ROOT}/tools/`. Run this from the project folder.

## A round
Round N is one more than the last round in `state.md`. Launch three `rh:reviewer`s in parallel, each writing `review/round-N/R<k>.md`:
- R1: identification and methods
- R2: contribution and theory
- R3: fit with the target venue, read as its editor would
From round 2 on, give each reviewer its own report from the previous round and `results/response_round-<N-1>.md`.

Read the last line of each report. The round passes with two or more `VOTE: PASS`. Record the round, the three votes and the verdict in `state.md`, and commit.

## If the round fails
Count the failed rounds in a row since the researcher last gave feedback or approval. If there are fewer than three, launch `rh:analyst` to address every major concern from this round: log new specifications, update `results/prim_res.md`, write `results/response_round-N.md` (each concern, what was done, and where), run `code/run_all.py`, then commit and push. Then start the next round.

After the third failure in a row, stop: email the researcher the reviewers' major concerns and ask how to proceed.

## If the round passes (Step 11)
Write `results/res_hum.md` and render it with `--bib design/refs.bib`: a brief abstract of the findings; the key tables and figures from `output/`, each with its interpretation; the concerns of any reviewer who voted FAIL; and open issues. Commit and push, and update `state.md`. Email the researcher a summary and the next step: approve (then `/rh:outline`), or send edits (then `/rh:analyze <edits>`, followed by `/rh:review`). Then stop.
