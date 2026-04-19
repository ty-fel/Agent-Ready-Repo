# Working with Agents

## Deciding What to Delegate
- Scope: guaranteed to find all the things it needs to do a good job. Modularize the codebase
- Closed loop: evaluate its own work
- Non mission critical
- Boring stuff, or things you'd never have the time to try
- Reproduction cases for issues
- Rubber duck in lieu of human

Do not delegate:
- Architecture and APIs
- Critical code (or at least review it)

## Before Delegation
How will you evaluate them? Tell the agent how you will evaluate it. Make it as efficient as possible to evaluate (e.g., screenshots, videos, tests) which also helps the agent evaluate itself. Put onus on agent for evaluation.

Use [`/delegate <task>`](./prompts/delegate.md) to scaffold this — it forces restating scope, evaluation criteria, and self-evaluation before the agent starts.

## After Completion
- Evaluate, take what's reasonable, and finalize
- Try using HTML as output form factor

Use [`/wrap`](./prompts/wrap.md) to finalize: summarize changes, run the agreed evaluation, produce a short report, and resist scope creep.

## Principles
- Think about what you're building and why before writing code
- Learn to say no; fewer features, polished
- Cap generated code; review every line of critical code
- Write architecture and APIs by hand
- Pair with agents, don't outsource — add friction so you learn

## Example Workflow

Think about *why* → [`/bug`](./prompts/bug.md) or [`/feature`](./prompts/feature.md) → add your thoughts and eval criteria → [`/delegate`](./prompts/delegate.md) → [`/wrap`](./prompts/wrap.md) → [`/review-session`](./prompts/review-session.md).
