# <idea title>

A research project set up by the rh research harness, targeting <venue>. Progress and decisions are in `state.md`. The harness's steps for this folder are `/rh:analyze`, `/rh:review` and `/rh:outline`.

## Where things are
- `design/research_design.md`: the approved design. Treat it as the pre-analysis plan.
- `design/venue.md` and `design/rubric.md`: the target venue's profile and standard.
- `design/refs.bib`: verified references. Cite only these keys.
- `data/raw/`: the original data, never edited. `data/README.md`: each file's source, date and license.
- `data/clean/`: built from `data/raw/` by code.
- `code/`: the analysis code. `code/run_all.py` rebuilds every output from `data/raw/`.
- `output/tables/` and `output/figures/`: written by code only.
- `results/`: `prim_res.md`, `spec_log.md`, responses to reviews and feedback, and `res_hum.md`.
- `review/round-N/`: the reviewers' reports.
- `draft/`: the paper outline.
- `scratch/`: temporary files. Safe to delete, never committed.

## Rules
- Never edit or delete anything in `data/raw/`.
- Every number in `results/` comes from a file that code wrote to `output/`. Never retype numbers.
- Log every specification you run in `results/spec_log.md`, including ones that don't make the paper, and record any deviation from the design with the reason.
- Temporary files go in `scratch/` only.
- Commit after each completed step, with a message saying what changed.
