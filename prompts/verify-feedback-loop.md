---
description: Verify this repo's edit→check feedback loop is fast and observable
---
Audit this repo's feedback loop — the edit→verify cycle an agent relies on
to catch its own mistakes without asking the user. Run the checks below,
report pass/fail for each, and propose concrete fixes.

Do **not** edit files during this audit. Report first; wait for approval.

## Checks

For each: **PASS**, **FAIL**, or **N/A** (with reason) plus evidence (file,
script name, command output, grep hit).

1. **Single `check` command** — one command runs lint + typecheck + test.
   Check `package.json`, `Makefile`, `justfile`, `pyproject.toml`,
   `Taskfile.yml`, etc. Typical names: `check`, `ci`, `verify`. FAIL if
   separate scripts exist with no composite.

2. **Watch mode available** — dev server *and* typecheck (e.g. `tsc
   --watch`, `mypy --watch`, `cargo check` loop). Must be documented, not
   just present.

3. **Tests are fast and path-runnable.** Run one test file via the
   documented command. FAIL if >30s or no path-filtering documented.

4. **Errors include `file:line:col`.** Trigger or locate a recent lint,
   typecheck, and test failure. Structured JSON or `path:line:col:` both
   count. Unparseable output FAILs.

5. **Dev server logs to stdout or a tail-able file.** FAIL if logs need a
   UI, rotating daemon, or in-process buffer to read.

6. **`.env.example` covers every env var the app reads.** Grep for
   `process.env.`, `os.getenv`, `os.environ[`, `Deno.env.get`,
   `std::env::var`, etc. Diff against `.env.example`.

7. **Fresh clone comes up without manual setup.** Seed data, fixtures,
   migration bootstrap, or pre-loaded compose volumes. FAIL if a fresh
   clone + `.env.example` wouldn't produce a working dev environment.

8. **All of the above are documented in `AGENTS.md`.** A working loop the
   agent doesn't know about is still FAIL.

## Report format

```
# Feedback loop audit

## Results
1. Single check command ...... PASS  (<command> → <what it runs>)
2. Watch mode ................ FAIL  (<evidence>)
...

## Proposed fixes
- <concrete change in this repo's manifest / script format>

## Score
N / 8 passing
```

## Ground rules

- Run safe commands (`--help`, `--version`, single-file test runs,
  `npm run check`). Never run destructive or long-lived ones (migrations,
  servers, deploys).
- Match the repo's existing stack and task-runner idiom. Don't propose
  `tsc` for a Python repo or switch `npm` → `pnpm`.
- N/A is fine (e.g. no dev server in a pure library) — one line of
  justification, no padding.
- Cite exact `file:line` evidence over prose.
