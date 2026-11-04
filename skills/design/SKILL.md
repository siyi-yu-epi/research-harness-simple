---
name: design
description: Steps 5-7 of the rh research harness. Records the researcher's chosen ideas and stress-test questions, writes a detailed research design for each, and revises it until the researcher approves.
argument-hint: <chosen idea IDs and venues, questions or feedback, or "approve"> [run folder]
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Tools: `${CLAUDE_PLUGIN_ROOT}/tools/`.

Input: $ARGUMENTS

## 1. Record the researcher's input
Write the chosen ideas (each with its target venue), questions and feedback, dated, under Decisions in the run's `state.md`. If it's unclear which idea or venue the researcher means, ask before going on. If the researcher approves a design, record the approval and stop: `/rh:launch` comes next.

## 2. Design (one `rh:designer` per chosen idea, in parallel)
Each designer writes, or revises, `designs/<idea-id>/research_design.md`, with:
1. The research question and hypotheses, with the theory or mechanism behind them.
2. The approach and design, and why they fit the question.
3. Data: each source, where and how to get it, coverage, unit of analysis, sample construction and time frame. For new data: the instrument, sampling, sample size from a power analysis, platform and cost.
4. Measurement: the dependent, independent and control variables, and any proxies, each with its definition and source.
5. Analysis: the main specification (as an equation where it applies), the identification strategy and the assumptions it rests on, and how each assumption will be tested. For difference-in-differences, for example: the treatment and control groups, the timing of the event, and the evidence for parallel pre-trends. For machine learning: the data source, the algorithm and the validation.
6. Robustness checks, mechanism analysis and heterogeneity analysis (or, for qualitative work, validity strategies), all pre-specified.
7. Threats to validity, and how each is handled.
8. Ethics review (IRB), timeline and costs.
9. Answers to each of the researcher's questions.
10. A revision log: what changed in each round, and why.

## 3. Deliver
Render each design to HTML with `--bib refs.bib`. Update `state.md`. Email the researcher a summary of each design, the file paths, and the next step: approve (`/rh:design approve <idea-id>`) or send edits (`/rh:design <idea-id>: <feedback>`). Then stop.
