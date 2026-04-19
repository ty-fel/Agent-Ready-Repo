# Template (n=70 sessions)

## Canonical example

```
You are given one or more GitHub PR URLs: https://github.com/badlogic/pi-mono/pull/1169/changes

For each PR URL, do the following in order:
1. Read the PR page in full. Include description, all comments, all commits, and all changed files.
2. Identify any linked issues referenced in the PR body, comments, commit messages, or cross links. Read each issue in full, including all comments.
3. Analyze the PR diff. Read all relevant code files in full with no truncation from the current main branch and compare against the diff. Do not fetch PR file blobs unless a file is missing on main or the diff context is insufficient. Include related code paths that are not in the diff but are required to validate behavior.
4. Check for a changelog entry in the relevant `packages/*/CHANGELOG.md` files. Report whether an entry exists. If missing, state that a changelog entry is required before merge and that you will add it if the user decides to merge. Follow the changelog format rules in AGENTS.md. Verify:
   - Entry uses correct section (`### Breaking Changes`, `### Added`, `### Fixed`, etc.)
   - External contributions include PR link and author: `Fixed foo ([#123](https://github.com/badlogic/pi-mono/pull/123) by [@user](https://github.com/user))`
   - Breaking changes are in `### Breaking Changes`, not just `### Fixed`
5. Check if packages/coding-agent/README.md, packages/coding-agent/docs/*.md, packages/coding-agent/examples/**/*.md require modification. This is usually the case when existing features have been changed, or new features have been added.
6. Provide a structured review with these sections:
   - Good: solid choices or improvements
   - Bad: concrete issues, regressions, missing tests, or risks
   - Ugly: subtle or high impact problems
7. Add Questions or Assumptions if anything is unclear.
8. Add Change summary and Tests.

Output format per PR:
PR: <url>
Changelog:
- ...
Good:
- ...
Bad:
- ...
Ugly:
- ...
Questions or Assumptions:
- ...
Change summary:
- ...
Tests:
- ...

If no issues are found, say so under Bad and Ugly.
```

## Sessions using this template

- `2026-01-16T02-44-55-123Z_99e99531-f376-4820-92f4-3c88afca3af9.jsonl`
- `2026-01-16T11-12-35-796Z_105b45a9-be31-4997-95c3-c95ab814daf8.jsonl`
- `2026-01-16T11-44-14-847Z_eedda2fa-e607-4779-b551-cfe751c7330f.jsonl`
- `2026-01-16T20-31-49-504Z_a86d0690-2d5b-4aa2-bad1-30ce4d39f641.jsonl`
- `2026-01-16T21-18-39-318Z_4801d454-021d-4fc1-9cc0-fc3cf8598ee2.jsonl`
- `2026-01-16T23-16-39-577Z_5fa9f7c7-fdb5-47b1-8a0f-5807e8a5e294.jsonl`
- `2026-01-17T10-00-58-318Z_fab6b9b8-0c6a-4e12-b9b9-14a75041bc53.jsonl`
- `2026-01-17T19-51-25-958Z_db328990-395c-44bd-8317-d0aa41c34538.jsonl`
- `2026-01-18T18-19-34-124Z_484c5a43-37f5-4a77-8ea5-d5ceb0df3a7a.jsonl`
- `2026-01-18T23-15-20-921Z_9c2cca56-9042-4f9a-bf32-6f60bfbcce53.jsonl`
- `2026-01-19T12-41-33-774Z_16648ee0-28fa-40ef-8fb3-d2e6a19d76ce.jsonl`
- `2026-01-19T12-43-04-788Z_0af1e524-99c7-4b33-aee8-de7e7aef313a.jsonl`
- `2026-01-19T15-01-52-822Z_732a795a-8170-42f1-b718-4a1e2e5800fb.jsonl`
- `2026-01-22T12-18-53-795Z_d25c0139-dbca-4232-a742-7638923537ac.jsonl`
- `2026-01-22T21-45-26-714Z_cad40af4-0d89-4fc7-a830-a799d7c0e080.jsonl`
- `2026-01-22T22-14-34-084Z_d9b4cc16-bdd4-406e-b651-4187a6deb45b.jsonl`
- `2026-01-23T16-35-35-399Z_64de8e0d-1082-4dfa-b345-5f32809d608e.jsonl`
- `2026-01-24T02-14-34-303Z_1a232687-4709-4f2c-9dca-6018f33a238c.jsonl`
- `2026-01-24T10-45-56-029Z_04863147-b587-4805-a2e5-e8b86a69d2ee.jsonl`
- `2026-01-25T00-57-41-535Z_66370d32-13fd-41b7-abac-d822a074e1de.jsonl`
- `2026-01-25T02-22-57-022Z_29d80798-ecdb-4891-9bf6-c252263d29bb.jsonl`
- `2026-01-25T02-28-18-217Z_974e9afe-4026-463a-9878-455ba28b746e.jsonl`
- `2026-01-25T18-15-34-609Z_c90d78a2-37f6-495b-983e-dcba093c8b71.jsonl`
- `2026-01-25T18-21-18-101Z_b9bdbab0-23f9-47e2-931a-855cf090d329.jsonl`
- `2026-01-25T18-28-17-410Z_53ae096f-6dfc-46ab-b5a5-ddfad2436a85.jsonl`
- `2026-01-25T18-28-31-215Z_359850c8-005e-4c90-bf8b-6a9acf0da37c.jsonl`
- `2026-01-25T18-33-48-722Z_4edf394e-8967-45a2-a7d4-5b6a2d26743b.jsonl`
- `2026-01-25T18-34-24-275Z_57989a9a-97a1-41da-8c06-4d8a29542ab9.jsonl`
- `2026-01-26T21-30-03-393Z_bcc5275a-0405-4ec6-8fd1-ce5ac470070b.jsonl`
- `2026-01-29T01-59-51-304Z_53c8fcdd-e583-4fa5-a910-67c318715717.jsonl`
- `2026-01-29T02-13-26-101Z_aaeb2f6f-2330-48dc-98ce-7f5e225b5208.jsonl`
- `2026-01-30T01-51-18-235Z_290724f3-4e6c-46ec-ad69-ae5a5b94ca74.jsonl`
- `2026-01-30T02-03-22-957Z_515c3270-49be-464f-a047-f2810d029d79.jsonl`
- `2026-01-31T21-57-51-352Z_76ff8366-4eb0-4e10-8a6c-4451a19d4c09.jsonl`
- `2026-01-31T22-10-19-453Z_90748a5d-9cf8-409c-b858-61e5b6acba20.jsonl`
- `2026-02-01T00-54-41-244Z_3428dd6e-4473-446b-8add-e3604f535109.jsonl`
- `2026-02-01T17-05-53-414Z_14f401ca-eced-4577-b2b7-9d4f35ca7d8c.jsonl`
- `2026-02-01T17-21-29-428Z_d253f60a-84b2-44f0-8976-3b50d0ebf068.jsonl`
- `2026-02-01T18-08-49-124Z_cd283e41-986f-4e8e-9102-07ad0d9f9447.jsonl`
- `2026-02-01T21-41-03-776Z_52881441-25cd-4867-81b7-f619a45e444f.jsonl`
- `2026-02-01T22-28-03-635Z_017eaee0-d70b-4207-8e76-0ab5292db71e.jsonl`
- `2026-02-02T00-13-59-390Z_c14742f1-2483-4c39-92f4-78d2b1db7ace.jsonl`
- `2026-02-03T00-11-49-341Z_db32e95a-e210-4466-8339-7bd85a8ed2d9.jsonl`
- `2026-02-03T00-36-46-707Z_977aaeba-8ffb-4f47-a9b1-b543228e906e.jsonl`
- `2026-02-03T00-50-06-630Z_bd494bb7-da64-4281-b592-063ea3493cd0.jsonl`
- `2026-02-03T11-05-22-524Z_8cf13211-ef0f-4524-920d-460e9d958f93.jsonl`
- `2026-02-04T01-23-28-017Z_c897b939-2817-4c6d-91f7-b7ea42ae0b9e.jsonl`
- `2026-02-04T12-39-56-105Z_e664d9a8-d404-4a02-844f-a22203cc04f8.jsonl`
- `2026-02-04T12-49-12-509Z_fd2bb9db-4cf3-4abf-8b01-5f57dce1dd9b.jsonl`
- `2026-02-05T17-43-46-715Z_0467b78e-e966-4892-b8d3-5054c5996917.jsonl`
- ... and 20 more