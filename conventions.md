# Conventions for the rh skills

Every rh skill follows these. The skill that sent you here names the plugin's `tools/` folder; `<tools>` below means that folder.

## Folders
- `RH_ROOT` is the folder that holds all research work, set in the researcher's user-level Claude settings (see the plugin README). Read it with `printenv RH_ROOT`. If it's empty, stop and say how to set it.
- A **run** covers Steps 1–8 for one topic: `$RH_ROOT/_runs/<YYYY-MM-DD>-<slug>/`. A run skill uses the run folder given as its argument; otherwise the most recently modified folder in `$RH_ROOT/_runs/`, and it says which one it picked.
- A **project** covers Steps 9–12 for one idea: `$RH_ROOT/<slug>/`, with its own private GitHub repository. Project skills run from inside the project folder.
- Never write research outputs into the plugin's own repository. It's public.

## Files
- Agents read and write Markdown, JSON Lines, BibTeX and CSV. Every document meant for the researcher is also rendered to HTML: `python <tools>/render.py FILE.md [--bib refs.bib] [--docx]` (`python3` if `python` isn't found).
- `state.md` in each run or project records progress, and every decision the researcher makes, with its date. Update it when a stage starts and when it ends.

## Evidence
- Cite only works in the folder's `refs.bib`, as `[@key]`. Add an entry only from a record you actually found, and keep it only once `python <tools>/verify_bib.py refs.bib` reports it VERIFIED or URL OK. Never cite from memory.
- If `verify_bib.py` reports entries as UNCHECKED (OpenAlex's free daily budget is used up), tell the researcher, list them, and carry on. They're checked again before the outline is written.
- Every fact about a venue, dataset or policy has a source link, or says "unknown" or "not published".

## Agents
- Launch the plugin's agents by name: `rh:scout`, `rh:proposer`, `rh:evaluator`, `rh:designer`, `rh:analyst`, `rh:reviewer`, `rh:drafter`. Launch agents whose work is independent in parallel, in a single message.
- Give each agent the exact files to read and to write. Agents write their results to files and return a short summary; check that the files exist before going on.

## Emailing the researcher
- Send to the address in `RH_NOTIFY_EMAIL` (`printenv RH_NOTIFY_EMAIL`) with the Gmail connector's send tool. Never write the address into any file.
- Subject: `[rh] <what's ready>: <run or project name>`. Body: what was produced, with file paths; a summary of 10 lines or fewer; and exactly what the researcher should do next.
- If the variable is empty or no Gmail tool is available, put the same message in the chat instead.
- At the researcher's checkpoints (after Steps 4, 6 and 10), email, then stop and wait.
