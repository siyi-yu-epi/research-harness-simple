---
name: outline
description: Step 12 of the rh research harness, run inside an idea's project folder once the researcher approves the results. Writes a Word scaffold of the paper - section structure, leading sentences, and where tables and figures go - for the researcher to write from.
disable-model-invocation: true
---

Read `${CLAUDE_PLUGIN_ROOT}/conventions.md` first. Tools: `${CLAUDE_PLUGIN_ROOT}/tools/`. Run this from the project folder.

If `state.md` doesn't record the researcher's approval of the results, ask for it first, then record it.

1. Run `verify_bib.py design/refs.bib`, and resolve every entry that isn't VERIFIED or URL OK before going on.
2. Launch `rh:drafter` to write `draft/outline.md`.
3. Render it to Word: `render.py draft/outline.md --bib design/refs.bib --docx`. If the renderer reports citation keys that aren't in `refs.bib`, replace them with `[source needed: ...]` notes and render again.
4. Commit and push, update `state.md`, and tell the researcher where `draft/outline.docx` is.
