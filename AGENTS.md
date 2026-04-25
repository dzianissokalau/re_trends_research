# AGENTS.md

## Git Safety Rules

- Treat `.gitignore` as a safety boundary. Do not stage, commit, or push files that match it.
- Do not use `git add -f` or any other override for ignored files unless the user explicitly names the file and approves it.
- Do not push to `main` or `master` without explicit approval.
- Do not amend, rebase, force-push, or otherwise rewrite published history without explicit approval.
- Before any push, state exactly which files are being pushed.
- Prefer feature branches and pull requests over direct pushes to protected branches.

## Hook Setup

This repository ships guardrail hooks in `.githooks/`.

Enable them in a local clone with:

```bash
git config core.hooksPath .githooks
```

The shipped hooks currently block:

- commits that include ignored files
- pushes to `main` or `master`
- pushes whose target commit tree contains ignored files
- non-fast-forward branch updates
