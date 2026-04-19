# Template (n=33 sessions)

## Canonical example

```
Audit changelog entries for all commits since the last release.

## Process

1. **Find the last release tag:**
   ```bash
   git tag --sort=-version:refname | head -1
   ```

2. **List all commits since that tag:**
   ```bash
   git log <tag>..HEAD --oneline
   ```

3. **Read each package's [Unreleased] section:**
   - packages/ai/CHANGELOG.md
   - packages/tui/CHANGELOG.md
   - packages/coding-agent/CHANGELOG.md

4. **For each commit, check:**
   - Skip: changelog updates, doc-only changes, release housekeeping
   - Skip: changes to generated model catalogs (for example `packages/ai/src/models.generated.ts`) unless accompanied by an intentional product-facing change in non-generated source/docs.
   - Determine which package(s) the commit affects (use `git show <hash> --stat`)
   - Verify a changelog entry exists in the affected package(s)
   - For external contributions (PRs), verify format: `Description ([#N](url) by [@user](url))`

5. **Cross-package duplication rule:**
   Changes in `ai`, `agent` or `tui` that affect end users should be duplicated to `coding-agent` changelog, since coding-agent is the user-facing package that depends on them.

6. **Add New Features section after changelog fixes:**
   - Insert a `### New Features` section at the start of `## [Unreleased]` in `packages/coding-agent/CHANGELOG.md`.
   - Propose the top new features to the user for confirmation before writing them.
   - Link to relevant docs and sections whenever possible.

7. **Report:**
   - List commits with missing entries
   - List entries that need cross-package duplication
   - Add any missing entries directly

## Changelog Format Reference

Sections (in order):
- `### Breaking Changes` - API changes requiring migration
- `### Added` - New features
- `### Changed` - Changes to existing functionality
- `### Fixed` - Bug fixes
- `### Removed` - Removed features

Attribution:
- Internal: `Fixed foo ([#123](https://github.com/badlogic/pi-mono/issues/123))`
- External: `Added bar ([#456](https://github.com/badlogic/pi-mono/pull/456) by [@user](https://github.com/user))`
```

## Sessions using this template

- `2026-01-16T23-26-15-892Z_79258f4c-347d-446e-bd6b-d98a48c5697d.jsonl`
- `2026-01-18T19-26-05-852Z_09517659-75bd-41e4-83dd-3cce63021752.jsonl`
- `2026-01-18T23-19-54-131Z_be960e8e-60c6-494e-8a46-d2806b5032bc.jsonl`
- `2026-01-19T15-10-53-158Z_e600a390-da4d-4c9f-868e-9c0394f5869c.jsonl`
- `2026-01-21T22-25-59-585Z_ec7037ba-c439-4af4-abdd-b0c60b2416c2.jsonl`
- `2026-01-22T00-36-13-233Z_c4df8d74-00e6-431f-aa21-27c351d30d65.jsonl`
- `2026-01-29T02-13-34-718Z_8a6762b0-1d65-4bc7-b909-553e5b02228d.jsonl`
- `2026-01-29T03-13-29-636Z_dd381ffd-6d0f-445e-9183-3ae19bbb801d.jsonl`
- `2026-01-30T02-14-38-031Z_36d2b570-84f8-43a2-8d7e-06be316cde03.jsonl`
- `2026-01-30T20-43-32-957Z_4f4c19f5-63c0-4acf-9356-a7e5c941e9b1.jsonl`
- `2026-01-30T20-47-28-022Z_a9b95d2a-b8f8-4c7f-ab96-7bb7704c7fcd.jsonl`
- `2026-02-01T01-02-09-622Z_99b9cb3a-1351-430d-99b6-dbd39ec7bc92.jsonl`
- `2026-02-01T18-16-03-558Z_8c5b2a40-7691-4169-a2cd-e056a7b1e676.jsonl`
- `2026-02-01T22-44-07-153Z_9c96693a-19b8-46c7-84b4-9bf1a0207715.jsonl`
- `2026-02-02T18-28-39-488Z_bd3dc502-9b4d-490a-bc00-ce522cbf64e1.jsonl`
- `2026-02-03T01-08-14-501Z_4a418f85-7bfc-4ae5-8000-9f0e7c32677f.jsonl`
- `2026-02-03T16-25-14-740Z_b1ff5494-a717-45c9-8833-e39553db936f.jsonl`
- `2026-02-04T13-20-12-553Z_695384fb-c828-4fad-9004-15d062381b52.jsonl`
- `2026-02-06T17-58-25-520Z_b07683da-56e5-47c8-8894-c6121fd338dd.jsonl`
- `2026-02-06T20-23-49-680Z_054481ca-81a0-41e7-8b28-25698f0ef632.jsonl`
- `2026-02-07T16-39-37-147Z_df6fd2f3-4be9-4e46-bd77-ab261c036bc7.jsonl`
- `2026-02-08T23-13-33-020Z_61cd39d4-46c6-4917-90a2-f6a5a32c19fc.jsonl`
- `2026-02-25T22-25-35-369Z_71e335d1-6ac7-4260-b256-5ede61528488.jsonl`
- `2026-03-02T22-01-21-835Z_eb18e984-e9b3-4045-8ed5-c523894a28d1.jsonl`
- `2026-03-07T13-39-28-333Z_fdd991b5-4997-4718-a3de-338c97db9ee3.jsonl`
- `2026-03-07T23-52-51-966Z_aa96a451-fe5a-4658-8f68-b343b4a95859.jsonl`
- `2026-03-14T11-25-06-176Z_ec150599-cc89-407c-b6eb-71e0a2528218.jsonl`
- `2026-03-18T02-16-43-303Z_388222c9-97d4-41f7-bacd-45414bc020ea.jsonl`
- `2026-03-18T02-30-37-961Z_7b0076be-97d7-45bc-b11f-b296eefb1eab.jsonl`
- `2026-03-20T19-04-58-517Z_8ebb6a40-7364-4306-b18c-a641ffd8f6aa.jsonl`
- `2026-03-23T00-49-45-875Z_f792de29-9efc-4f06-99da-7243ea304782.jsonl`
- `2026-03-23T01-35-14-771Z_9af6fdab-c1ed-45eb-87cc-c13b017edfbb.jsonl`
- `2026-04-05T21-44-58-245Z_c117d62c-b716-4c59-bfb8-3bffcfec71e9.jsonl`