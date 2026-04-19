---
description: Review the current session for doc gaps, tooling gaps, and other feedback
---

Review the current session for places the agent went the wrong direction,
then recommend what could have been added to the repo (docs, tooling, prompts,
extensions) to reach the goal faster.

"Session" means the current conversation context. Do not read
`.pi/sessions/` or `git log` — only what's already in scope.

## What to look for

**Docs gaps** — anything the agent had to ask, guess, or discover by
trial-and-error that a line in `AGENTS.md` / `README.md` / `docs/` would
have fixed. Corrections I made, rule-preventable mistakes, and new
surface area (scripts, env vars, endpoints) introduced without docs all
count.

**Tooling gaps** — recurring or error-prone work that a custom tool,
script, alias, skill, prompt template, or third-party install would
remove. Also flag cases where a better tool existed but the agent didn't
reach for it. For third-party installs, include the install command.

**Other feedback** — confusing prompt behavior, guardrails worth adding,
context-window waste, anything else.

## How to report

Three sections: **Docs**, **Tooling**, **Other feedback**.

For each docs finding: short title, one-line evidence from the session,
target file, and a concrete diff.

For each tooling finding: short title, kind (custom tool / install /
skill / prompt / script / extension), one-line evidence, one–three
sentence proposal, and the friction it removes.

Other feedback: short bullets.

Keep proposed additions short, imperative, bulleted. Prefer linking into
`docs/` over inlining prose. Flag speculative findings with `(maybe)`.
Group by target file so I can apply in batches.

## Ground rules

- Do not edit files. Propose diffs only, then wait for approval.
- If a section has nothing meaningful, say so in one line. Don't pad.
