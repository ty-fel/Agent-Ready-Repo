# agent-repo-guide

A personal template for making repos easy to work in with coding agents, plus the prompts I use to set them up and maintain them.

Built around [pi](https://github.com/badlogic/pi-mono) and modeled loosely on [pi-mono](https://github.com/badlogic/pi-mono)'s conventions.

## Guides

- [repo-setup.md](./repo-setup.md)
- [workflows.md](./workflows.md)

## How to use

Two independent paths — use either or both.

**Set up a new repo.** Read [repo-setup.md](./repo-setup.md), seed an `AGENTS.md` in your repo using the template there, then run [`/setup-agent-rules`](./prompts/setup-agent-rules.md) in a pi session at the repo root.

**Install the prompts.** Copy `prompts/` into `~/.pi/agent/prompts/` (global) or your repo's `.pi/prompts/` (per-repo override).

## Prompts

- [`/setup-agent-rules`](./prompts/setup-agent-rules.md) — one-time pass to scaffold `README.md` and extend `AGENTS.md` with commands and conventions.
- [`/review-session`](./prompts/review-session.md) — fold corrections back into `AGENTS.md` and surface repo changes that would make the agent more effective.
- [`/verify-feedback-loop`](./prompts/verify-feedback-loop.md) — audit the edit→check cycle.
- [`/delegate`](./prompts/delegate.md) — scaffold scope and evaluation criteria before handing a task to an agent.
- [`/wrap`](./prompts/wrap.md) — finalize a delegated task: summarize, evaluate, resist scope creep.
- [`/feature`](./prompts/feature.md), [`/bug`](./prompts/bug.md) — task templates.

## Design principles

- **Scale to the repo.** Most repos are not pi-mono. Default to `README.md` + `AGENTS.md` only; grow `docs/` or `examples/` only under pressure.
- **General, not repo-specific.** Anything in this template should apply to any repo. Repo-specific rules live in the consuming repo's `AGENTS.md`, not here.
- **`AGENTS.md` evolves.** The seed is a floor. `/review-session` is how it grows — add a rule when you've corrected the agent on the same thing twice.
- **Not a pi-mono fork.** pi-mono's PR/issue workflows, contribution gates, and multi-package structure are intentionally omitted. Reference pi-mono for ideas, not as a spec.

## Resources

- Mario Zechner — [Thoughts on slowing the fuck down](https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/)
- Mario Zechner — [Building pi in a World of Slop](https://www.youtube.com/watch?v=RjfbvDXpFls)
- Lucas Meijer — [A Love Letter to Pi](https://www.youtube.com/watch?v=fdbXNWkpPMY)
- [pi-mono](https://github.com/badlogic/pi-mono)
