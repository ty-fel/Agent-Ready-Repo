# Setting Up a Repo for Agent-Friendly Development

A human guide for making a repo easy for coding agents to work in.

Two files do 90% of the work: `README.md` and `AGENTS.md`. Add `docs/<topic>.md`
only when a concept keeps getting re-explained (or `AGENTS.md` crosses ~300
lines). Add `examples/` only if the repo is a library/SDK whose API consumers
write code against. Most application repos need neither.

## Setup

### 1. Seed `AGENTS.md` (human, ~5 min)

Copy the [template](./AGENTS.md.template) into `AGENTS.md` and then prune it based on the needs and complexity of your repository. Keep it short, imperitive, and specific to the repo. Start minimal and add as needed.

```bash
cp AGENTS.md.template AGENTS.md
```

### 2. Run `/setup-agent-rules` (agent)

Invoke [`/setup-agent-rules`](./prompts/setup-agent-rules.md) in a
session at the repo root. It inventories the repo, scaffolds `README.md` if
missing, extends `AGENTS.md` with commands and inferred conventions, and
adds a Changelog block only if a `CHANGELOG.md` already exists. It will not
create `docs/` or `examples/`.

Review the diff.

### 3. Fill in what only you know (human)

Review the agent's `Still owed by human` summary and fill those in —
invariants, "do not touch" paths, architecture purpose, team conventions,
recurring gotchas. The agent can't infer these.

### Maintenance

- After a session where you corrected the agent, run
  [`/review-session`](./prompts/review-session.md) to fold those
  corrections back into `AGENTS.md`.
- Run [`/verify-feedback-loop`](./prompts/verify-feedback-loop.md)
  once you have a `check` command, to confirm the agent can actually observe
  its own mistakes.

To install, copy `prompts/` from this repo into `~/.pi/agent/prompts/`
(global) or `<repo>/.pi/prompts/` (per-repo override).

## Target layout

Minimum viable — an agent cold-starts in ~2 reads:

```
repo/
├── README.md          # what this is + quick-start commands
├── AGENTS.md          # rules, commands, invariants (auto-loaded)
├── package.json
├── src/
└── tests/
```

Grow `docs/` or `examples/` only when `AGENTS.md` or `README.md` starts
bloating. Rules if you do:

- `README.md` links out to `docs/` rather than inlining detail.
- `AGENTS.md` points at `docs/`; it's rules + pointers, not a second copy.
- First mention of a concept links to its doc.
- One topic per file, <300 lines, flat (no nesting).
- No `notes.md` / `misc.md` dumping grounds.
