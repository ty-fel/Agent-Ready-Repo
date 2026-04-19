# Setting Up a Repo for Agent-Friendly Development

A human guide for making a repo easy for coding agents to work in.

Two files do 90% of the work: `README.md` and `AGENTS.md`. Add `docs/<topic>.md`
only when a concept keeps getting re-explained (or `AGENTS.md` crosses ~300
lines). Add `examples/` only if the repo is a library/SDK whose API consumers
write code against. Most application repos need neither.

## Setup

### 1. Seed `AGENTS.md` (human, ~5 min)

Create `AGENTS.md` at the repo root. Keep it short, imperative, specific to
this repo — not generic advice. Example shape:

```markdown
# Agent Instructions

## Purpose
<One sentence: what this repo is.>

## Conversational Style
- Short, concise, technical prose
- No emojis, no filler, no cheerful padding
- Kind but direct

## Code Quality
- Ask before removing functionality or code that looks intentional
- Do not preserve backward compatibility unless asked
- <Add rules here as they come up in review sessions>

## Commands
- After code changes, run: <check command>
- NEVER run: <long-running / destructive commands>
- If you create or modify a test file, run it and iterate until it passes

## Do not touch
<Paths the agent should never read or edit. Fill in as issues come up.>

## Git
- Never `git add -A` or `git add .` — stage specific paths
- Never commit unless asked
```

The concrete lines matter more than the section headers. If you've corrected
the agent twice on something, it belongs here — most often under `Code Quality`.

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
