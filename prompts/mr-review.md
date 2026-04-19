---
description: Review a merge request from a commit SHA or branch name using git only
argument-hint: "<commit-sha-or-branch> [target-branch]"
---
MR ref: $1
Target branch: $2 (default to `main` if empty)

Review this merge request using only the `git` CLI.

1. Resolve the ref and identify the diff range:
   ```bash
   git fetch --all --prune
   git log -1 $1                 # confirm the ref exists
   git merge-base $1 $2          # compute the base to diff against
   git log --oneline <merge-base>..$1
   git diff <merge-base>..$1 --stat
   ```
2. Read the full diff (`git diff <merge-base>..$1`) and every commit message in the range (`git log <merge-base>..$1`).
3. Read all relevant code files **in full** from the target branch and compare against the diff. Include related code paths not in the diff but required to validate behavior.
4. Check whether docs, README, or examples need updates given the change. Report missing updates.
5. Check whether tests cover the change. Report gaps.

Provide a structured review:

- **Good**: solid choices or improvements
- **Bad**: concrete issues, regressions, missing tests, or risks
- **Ugly**: subtle or high-impact problems
- **Questions or Assumptions**: anything unclear
- **Change summary**: what this MR actually does, in your own words
- **Tests**: what is covered, what is missing

If no issues are found in a section, say so explicitly.

Do NOT push changes or approve. Review and report only.
