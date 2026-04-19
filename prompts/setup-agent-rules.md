---
description: One-time setup pass to make a repo agent-friendly
---
Set up this repo for agent-friendly development. Scale effort to the repo's
actual complexity — do not invent structure it doesn't need.

## Ground rules

- Read `AGENTS.md` first. If missing, stop and ask the human to seed it with
  purpose, "do not touch" paths, and critical invariants.
- If `AGENTS.md` is present, treat its "do not touch" paths and invariants as
  hard constraints. If it's minimal, *extend* it — don't restructure.
- Use `read`, `grep`, `ls` generously before writing. Do not invent commands,
  conventions, file paths, invariants, or gotchas.
- Never overwrite a non-empty `README.md` or `AGENTS.md` without showing a
  diff first. Extend rather than rewrite when they look maintained.
- Prefer linking over duplicating: `AGENTS.md` points at `README.md`, not a
  copy of it.
- Default to `README.md` + `AGENTS.md` only. Do not create `docs/`,
  `examples/`, or empty topic-doc stubs. If the repo is complex enough that
  `docs/` would clearly help, or it's a library/SDK where `examples/` would
  show API shape, mention it in the final summary for the human to decide.
  When in doubt, don't.
- Do not sprinkle `(confirm?)` / `(inferred)` markers through output files.
  If something is uncertain, mention it once in the final summary.

## Do

1. **Inventory.** List the top-level layout, existing docs, and scripts in
   `package.json` / `Makefile` / `pyproject.toml`. Note any `AGENTS.md` or
   `CLAUDE.md` already present, and whether a `CHANGELOG.md` exists.

2. **README scaffold.** If `README.md` is missing or thin, create/extend it
   with: project name, one-line description (from the manifest), a
   repo-layout tree, and a quick-start listing the install / test / lint
   commands from step 1. Do not invent commands.

3. **Extend `AGENTS.md`** with:
   - *Commands* — the ones you found in step 1 (build, check, test, lint).
     Be specific: exact invocation, when to run it.
   - *Conventions* — patterns visible in existing code (test file naming,
     import style, formatter config, error handling shape). Only include
     ones you can point at a concrete example for.
   - *Where to look* — short pointers into `README.md` and any existing
     `docs/`.
   - *Changelog* — only if a `CHANGELOG.md` already exists. Add a short
     block: location, "new entries go under `## [Unreleased]`", "never
     modify released version sections."

   Keep it short, imperative, bulleted. No prose paragraphs. No empty
   section headers.

4. **Single `check` command.** If the project has separate lint/typecheck/
   test scripts but no single "is everything OK?" command, add one (e.g.
   `npm run check`) that composes them. Skip if one already exists. Do not
   change the underlying scripts.

## Final summary

When done, print:

```
## Summary
- Created: <files>
- Modified: <files>
- Uncertainties: <things the human should verify>
- Still owed by human: invariants, "do not touch" paths, architecture
  narrative, team commit conventions, recurring gotchas
- Blocked on: <anything you couldn't do and why>
```
