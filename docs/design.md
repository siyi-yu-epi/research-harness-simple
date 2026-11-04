# Design

Why the harness is built the way it is. The README covers setup and use.

## Goals
- Take a topic, target journal or research direction to the scaffold of a paper, with the researcher deciding at three checkpoints (Steps 5, 7 and 11).
- Work in any discipline.
- Stay small enough to read in one sitting, so the researcher stays in control of it.

## Principles
- **Stages are contracts, not procedures.** Each skill states its inputs, its outputs, what they must contain and the bar they must clear. It doesn't script how to get there.
- **The discipline is data.** Venue norms, methods and standards are found in each run (Steps 2–4) and written into the run's files, which later stages read. Nothing field-specific is hard-coded.
- **Files are the only interface.** Stages pass work only through files, and `state.md` records progress and every decision the researcher makes. Any output can be edited by hand, and any stage re-run.
- **Agents only where they earn it**: for independent work (proposers, reviewers), to pin a model (evaluator, designer, drafter), or to keep heavy reading out of the main context (scouts, analyst). Orchestration stays in the skills, and agents can't launch agents.
- **Tools only where an instruction can't be trusted**: checking that references are real, and rendering documents.
- **Size budget**: a skill fits on about a page, and an agent definition on half a page.

## Decisions
- **Models.** Opus for judging (evaluator, designer, reviewer, drafter) and Sonnet for the work (proposer, analyst), all at max effort; Sonnet at its default effort for web research (scout).
- **One evaluator, one standard.** `eval_rl.md` holds the core criteria plus a section per venue, calibrated against papers each venue actually published. The ranking runs once per venue with only that venue's section loaded, and the same standard is the reviewers' rubric in Step 10.
- **Ideation is a funnel.** Five proposers with different lenses (four grounded, one out-of-the-box, so about 20% of ideas are out-of-the-box) write 100+ short cards. The evaluator screens them, scouts check the shortlist for prior art and for whether the data exists, and the evaluator ranks the survivors per venue, reserving one slot per venue for an out-of-the-box idea.
- **Getting the data is part of Step 9.** Studies that collect new data stop once the instrument, IRB materials and power analysis are drafted, so the researcher can field them.
- **The Step 9–10 loop is guarded.** The approved design is the pre-analysis plan, every specification is logged, and reviewers see the log. After three failed rounds in a row, the researcher decides how to proceed.
- **Reviewers have different lenses** (methods, contribution, venue fit), vote independently, and in later rounds check their earlier concerns against the analyst's response.
- **Formats.** Agents use Markdown, JSON Lines, BibTeX and CSV. The researcher gets HTML, and Word for the outline.
- **Privacy.** Research outputs never go in this public repository, and each project gets a private one. Personal settings (the email address, the root folder) live in user-level Claude settings.
- **Analysis in Python** by default; R or Stata only where Python lacks a sound implementation.
- **Sources distilled, not copied.** Creswell and Creswell's *Research Design* is paraphrased in `skills/design/design-checklist.md`, and Healy's *Data Visualization* in `skills/analyze/viz-checklist.md`.
