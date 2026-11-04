---
name: analyze
description: Step 9 of the rh research harness, run inside an idea's project folder. Gets the data, runs the descriptive, main, robustness, mechanism and heterogeneity analyses in the approved design, and writes up results/prim_res.md. Also revises the analysis after the researcher's feedback.
argument-hint: [feedback to address]
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Tools: `${CLAUDE_PLUGIN_ROOT}/tools/`. Run this from the project folder.

Feedback: $ARGUMENTS

If there's feedback, record it under Decisions in `state.md` and give `rh:analyst` the revision task. Otherwise give it the main task.

## Main task for `rh:analyst`
0. **Data.** Get every source in `data/README.md` that isn't in hand. Open data: download it into `data/raw/` with a script in `code/`, and record the source, date and license in `data/README.md`. Data that has to be collected (e.g. a questionnaire): draft the instrument (`design/instrument.md`), the IRB materials (`design/irb.md`) and the power analysis, then stop and report.
1. **Descriptives.** A descriptive statistics table for the dependent, independent and control variables, to the standard of a top journal, and figures that show the main descriptive patterns.
2. **Main analysis.** As the design specifies. Report the estimating equation or algorithm, the results in clear tables, and coefficient plots where they help.
3. **Robustness, mechanisms, heterogeneity.** The checks the design pre-specifies, plus any the results call for, logged as additions.
4. **Write-up.** `results/prim_res.md`: the question and design in brief; then, for each analysis, its specification, its tables and figures (embedded from `output/`, never retyped) and a plain-language interpretation; then limitations and open issues. Check that `python code/run_all.py` rebuilds everything from `data/raw/` without errors, empty `scratch/`, then commit and push.

## Revision task for `rh:analyst`
Address each point of the feedback: log new specifications, update `results/prim_res.md`, and write `results/response_feedback-<YYYY-MM-DD>.md` listing each point, what was done and where. Run `code/run_all.py`, empty `scratch/`, then commit and push.

## When the analyst returns
- If it stopped for data collection: email the researcher that the instrument, IRB materials and power analysis are ready, update `state.md`, and stop. Run `/rh:analyze` again once the data is in `data/raw/`.
- Otherwise, confirm that `results/prim_res.md` exists and that the analyst reported a clean run of `run_all.py`. Render `prim_res.md` to HTML with `--bib design/refs.bib`, update `state.md`, and say that `/rh:review` comes next.
