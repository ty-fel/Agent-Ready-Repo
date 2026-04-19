# pi-mono session analysis

Tooling for reviewing Mario Zechner's [pi-mono](https://huggingface.co/datasets/badlogicgames/pi-mono) sessions as input for updates to `workflows.md` and `prompts/`.

## Setup

```
uv sync
```

Sessions are loaded from the HuggingFace cache (populated once by `recon.py`).

## Scripts

- `scripts/recon.py` — schema + aggregate stats across all 626 sessions.
- `scripts/dump_sessions.py` — renders each session as markdown under `sessions/`, writes `index.md`.
- `scripts/extract_prompts.py` — clusters recurring first-user prompts into reusable templates under `artifacts/prompts/`, writes `prompt_templates.md`.

Run in order:

```
uv run python scripts/recon.py
uv run python scripts/dump_sessions.py
uv run python scripts/extract_prompts.py
```

## Layout

```
index.md                  # browsable table of all sessions
prompt_templates.md       # table of recurring prompt templates
sessions/*.md             # one rendered transcript per session (gitignored)
artifacts/prompts/*.md    # deduped prompt templates + which sessions used them
notes.md                  # rolling observations → feed back into ../workflows.md
```

## Workflow for reviewing

1. Start with `prompt_templates.md` — these are the reusable prompts Mario runs most often.
2. Skim `index.md`, sort by cost/tokens to find sessions worth reading in full.
3. `rg 'pattern' sessions/` for keyword searches across transcripts.
4. Log findings in `notes.md`; promote anything reusable to `../prompts/` or `../workflows.md`.
