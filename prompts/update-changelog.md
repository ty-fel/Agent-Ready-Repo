---
description: Audit and update the changelog for all commits since the last release
argument-hint: "[since-ref]"
---
Audit changelog entries for all commits since the last release (or since `$@` if provided).

## Process

1. **Find the baseline:**
   - If an argument was given, use it as the starting ref.
   - Otherwise find the last release tag:
     ```bash
     git tag --sort=-version:refname | head -1
     ```

2. **List all commits since that ref:**
   ```bash
   git log <ref>..HEAD --oneline
   ```

3. **Read the current `[Unreleased]` section(s)** of the relevant `CHANGELOG.md` file(s).

4. **For each commit, check:**
   - Skip: changelog updates, doc-only changes, release housekeeping, generated files.
   - Determine which component(s) the commit affects (`git show <hash> --stat`).
   - Verify a changelog entry exists for any user-visible change.

5. **Report:**
   - Commits missing a changelog entry, grouped by affected component.
   - Entries that look misclassified (e.g., breaking change filed under Fixed).
   - Propose the entries to add, then apply them after confirmation.

## Changelog format

Sections, in this order:

- `### Breaking Changes` — API or behavior changes requiring migration
- `### Added` — new features
- `### Changed` — changes to existing functionality
- `### Fixed` — bug fixes
- `### Removed` — removed features

Keep entries short, imperative, and user-facing. Link to the relevant ticket or MR where applicable.

Do NOT tag a release or modify version numbers. Audit and update `[Unreleased]` only.
