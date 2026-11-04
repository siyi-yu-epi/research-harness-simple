# research-harness-simple

A simpler research harness that adapts to a broad discipline.

It's a [Claude Code](https://code.claude.com) plugin, `rh`, that takes a topic, target journal or research direction to the scaffold of a paper in 12 steps. You decide at three checkpoints: which ideas to pursue, when a research design is ready, and whether the results are. Nothing about any one discipline is built in. Each run finds out its own field's venues, norms and standards, and the later steps work from those.

## The pipeline

| Step | Run | You get |
|---|---|---|
| 1–2 | `/rh:venues <topic, journal or direction>` | `venues.md`: the top 5 venues, with acceptance rates, formatting rules and a writing template from recent papers |
| 3 | `/rh:litreview` | `lit-rev.html`, organized by strand, and `refs.bib`, with every reference checked |
| 4 | `/rh:ideate` | `eval_fnl.html`: the top 5 ideas for each venue, out of 100+ proposals. Emailed to you. |
| 5–7 | `/rh:design <your picks and questions>` | `research_design.html` for each idea. Repeat with your feedback until you approve. Emailed to you. |
| 8 | `/rh:launch` | a project folder and a private GitHub repository for each approved idea |
| 9 | `/rh:analyze` | `results/prim_res.md`: descriptives, main analysis, robustness, mechanisms and heterogeneity |
| 10–11 | `/rh:review` | three independent reviewer votes; on a pass, `results/res_hum.html`, emailed to you |
| 12 | `/rh:outline` | `draft/outline.docx`: section structure, leading sentences, and where tables and figures go |

Run Steps 9–12 from inside each project's folder, one Claude Code session per project, so projects can move in parallel.

## Setup

Do this once, on the computer where you'll run the harness.

1. Install Python 3, pandoc, git and the GitHub CLI. On Windows:

   ```powershell
   winget install Python.Python.3.13
   winget install JohnMacFarlane.Pandoc
   winget install Git.Git
   winget install GitHub.cli
   ```

   Then sign in to GitHub with `gh auth login`. The analyst installs the Python packages each project needs and records them in that project's `requirements.txt`.

2. Install the plugin. In Claude Code:

   ```
   /plugin install rh --marketplace siyi-yu-epi/research-harness-simple
   ```

   On Claude Code versions before 2.1.275, use two steps instead: `/plugin marketplace add siyi-yu-epi/research-harness-simple`, then `/plugin install rh@research-harness-simple`.

3. Add your settings to your **user-level** Claude settings file, `~/.claude/settings.json` (on Windows, `C:\Users\<you>\.claude\settings.json`), never to a repository:

   ```json
   {
     "env": {
       "RH_ROOT": "C:/Users/<you>/Dropbox/<path>/AI-related",
       "RH_NOTIFY_EMAIL": "<the address the harness should email>",
       "OPENALEX_API_KEY": "<optional: your free OpenAlex key>"
     }
   }
   ```

   Use forward slashes in the path. `OPENALEX_API_KEY` is optional. Without it, reference checks share a small daily OpenAlex budget with everyone on your network, and references it can't settle are marked UNCHECKED.

4. For the emails, the harness uses the Gmail connector in your claude.ai account. Claude Code can use it when you're signed in with that same account (`/login`); check that Gmail is listed under `/mcp`. Without it, the harness puts its messages in the chat instead.

## Where your work goes

- **Runs** (Steps 1–8, one per topic) go in `RH_ROOT/_runs/<date>-<topic>/`: the venues, literature review, ideas and designs, plus `state.md`, the record of progress and of your decisions.
- **Projects** (Steps 9–12, one per idea) go in `RH_ROOT/<idea>/`, each with a private GitHub repository.
- Nothing from your research is written to this repository, which is public.

## How it's built

- `skills/`: one skill per stage. Each states what goes in, what comes out, and the bar it must clear. It doesn't script the steps.
- `agents/`: seven agents. Opus at max effort judges (`evaluator`, `designer`, `reviewer`, `drafter`); Sonnet at max effort does the work (`proposer`, `analyst`); Sonnet does the web research (`scout`). The `opus` and `sonnet` aliases move to newer models automatically.
- `tools/verify_bib.py` checks every reference against OpenAlex, Crossref and doi.org. `tools/render.py` turns Markdown into the HTML and Word files you read.
- `conventions.md`: the rules every skill shares. `templates/`: starting files for runs and projects.
- `docs/design.md`: why it's built this way.

## Contributing

Issues and pull requests are welcome. Please open an issue first to discuss larger changes.

## License

Released under the [MIT License](LICENSE).
