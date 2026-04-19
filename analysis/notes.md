# Notes from reviewing pi-mono sessions

Running observations. Goal: find workflows, prompts, and habits worth stealing into `../workflows.md` or `../prompts/`.

## Headline stats (from recon)

- 626 sessions, ~1.06B tokens, ~$643 spend, all on `/Users/badlogic/workspaces/pi-mono`.
- 15.6k assistant messages, 15.4k tool results, 2.8k user messages → avg ~25 assistant turns / ~4.5 user turns per session. Mario lets the agent run long stretches between steers.
- 833 `model_change` + 841 `thinking_level_change` events across 626 sessions → he routinely swaps models and thinking effort mid-session.
- Stop reasons: 12.9k toolUse, 2.3k stop, **333 aborted**, 75 error → frequent hard-aborts (Ctrl-C style steering).
- Tool distribution (by toolResult): bash 8187 · read 5107 · edit 1887 · write 210. Edit-heavy, write-light — matches his "don't let agents scaffold new files" posture.

## Recurring prompt templates (from extract_prompts)

55% of non-trivial first prompts fall into 5 templates:

| n | template | takeaway |
|---:|---|---|
| 70 | PR review (`You are given one or more GitHub PR URLs...`) | longest/most detailed template; worth diffing vs our `prompts/` |
| 66 + 53 + 34 | Issue analysis variants | three generations of the same prompt — the evolution itself is interesting |
| 33 | Changelog audit since last release | we don't have an equivalent; candidate for `prompts/` |

Files: `artifacts/prompts/*.md`.

## TODO — things to read in full

- [ ] Highest-cost sessions (sort `index.md` by cost desc) — where does budget actually go?
- [ ] Sessions with many `aborted` stops — how does he steer when things go wrong?
- [ ] Sessions with the most `model_change` events — which models does he hand off to, and why?
- [ ] The 3 issue-analysis template generations — diff them to see what he learned.
- [ ] Changelog audit template — lift into `../prompts/changelog.md` if useful.

## Candidate changes to this repo

(fill in as evidence accumulates)

- [ ] …
