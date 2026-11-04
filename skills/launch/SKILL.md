---
name: launch
description: Step 8 of the rh research harness. Sets up a project folder and a private GitHub repository for each approved research design.
argument-hint: [run folder]
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Run: $ARGUMENTS

Launch only the designs that the run's `state.md` records as approved. First check that `gh auth status` succeeds; if it doesn't, ask the researcher to run `gh auth login`, and stop.

For each approved design:
1. Choose a slug (2–5 words from the idea's title, kebab-case) and create `$RH_ROOT/<slug>/` with the folders `design/`, `data/raw/`, `data/clean/`, `code/`, `output/tables/`, `output/figures/`, `results/`, `review/`, `draft/` and `scratch/`.
2. Into `design/`, copy: `research_design.md` and `.html`; the idea card and its check, as `idea.md`; the venue's profile from `venues/`, as `venue.md`; the core criteria and that venue's section of `eval_rl.md`, as `rubric.md`; and `refs.bib`.
3. Write `CLAUDE.md` from `${CLAUDE_PLUGIN_ROOT}/templates/project-CLAUDE.md` and `state.md` from `${CLAUDE_PLUGIN_ROOT}/templates/project-state.md`. Write `data/README.md` listing the data the design needs: source, link, license, and status ("to download" or "to collect").
4. Write `.gitignore` with: `data/raw/`, `data/clean/`, `scratch/`, `.env`, `__pycache__/`, `.ipynb_checkpoints/`.
5. Run `git init -b main`, commit everything ("Set up project from research harness run <run>"), then `gh repo create <slug> --private --source . --push`. If the name is taken, add a short suffix.

Then record each project's folder and repository URL in the run's `state.md`, and tell the researcher to open a Claude Code session in each project folder and run `/rh:analyze` there. Projects can run in parallel, one session each.
