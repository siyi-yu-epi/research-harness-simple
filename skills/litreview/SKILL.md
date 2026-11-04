---
name: litreview
description: Step 3 of the rh research harness. Reviews the run topic's literature strand by strand, identifies research gaps, and records every reference in a verified refs.bib.
argument-hint: [run folder]
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Tools: `${CLAUDE_PLUGIN_ROOT}/tools/`. Run: $ARGUMENTS
Needs: `venues.md`.

This is a narrative review of the main strands, not a systematic review. Don't download papers.

## 1. Map the strands
From the run's input and `venues.md`, identify 4–8 strands of literature the paper would speak to, each with a slug and a one-sentence scope. Give weight to recent work in the five target venues: that's the conversation the paper joins. Record the strands in `state.md`.

## 2. Review each strand (one `rh:scout` per strand, in parallel)
Each scout writes `lit/<strand-slug>.md` and `lit/<strand-slug>.bib`, covering:
- The key topics and themes, and the papers that define them.
- The popular research methods, and how methods have changed over time.
- Current gaps and future directions: what's unresolved, and why it matters.
Citations are `[@key]`, and every key is in that strand's `.bib`, which passes `verify_bib.py`.

## 3. Assemble
- Merge the strands' `.bib` files and the existing `refs.bib` (one key per work, updating citations to match) and run `verify_bib.py refs.bib > refs.check.md`. Fix or remove every failing entry, along with its citations.
- Write `lit-rev.md`: an overview, one section per strand, and a closing section on the gaps that cut across strands. Render it with `--bib refs.bib` to `lit-rev.html`.
- Update `state.md`, and tell the researcher what's in `lit-rev.html` and that `/rh:ideate` comes next.
