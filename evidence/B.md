# Student B — Lantern Evidence

> Replace every `[PASTE ...]` placeholder with your **actual terminal output**.
> Do not invent or edit command output. Capture each item when the assignment says to;
> some evidence (especially commit object information and the stash listing) is easiest
> to lose if collected later.

## E1 — Remote configuration (Requirement 1)

**Purpose:** Prove that Student B's clone uses SSH.

Run:

```bash
git remote -v
```

Example format (your username and repository path will differ):

```text
origin  git@github.com:YOUR-USERNAME/lantern.git (fetch)
origin  git@github.com:YOUR-USERNAME/lantern.git (push)
```

Paste your actual output:

```text
[PASTE ACTUAL `git remote -v` OUTPUT HERE]
```

## E3 — Git commit and tree objects (Requirement 2)

**Purpose:** For two consecutive commits on `main`, show both commit hashes, both root tree hashes, one file whose blob object is identical in both commits, and one file whose blob object differs.

First identify two consecutive commits on `main`:

```bash
git log --oneline --decorate -n 5
```

Set the older and newer commit SHAs (replace the examples):

```bash
OLDER=OLDER_COMMIT_SHA
NEWER=NEWER_COMMIT_SHA
```

Show each commit and its root tree:

```bash
git show -s --format='commit %H%nroot tree %T%nsubject %s' "$OLDER"
git show -s --format='commit %H%nroot tree %T%nsubject %s' "$NEWER"
```

Compare a file unchanged between the two commits (example: `README.md`):

```bash
git rev-parse "$OLDER:README.md"
git rev-parse "$NEWER:README.md"
```

The two blob hashes should be identical.

Compare a file changed between the two commits (choose a file that really changed, for example `docs/usage.md`):

```bash
git rev-parse "$OLDER:docs/usage.md"
git rev-parse "$NEWER:docs/usage.md"
```

The two blob hashes should differ.

Paste all actual output and identify which file is unchanged and which is changed:

```text
[PASTE ACTUAL COMMIT HASHES, ROOT TREE HASHES, AND FILE BLOB HASHES HERE]
```

If your chosen files do not produce the required identical/different results, choose suitable files from those same two commits. Do not claim a file is unchanged or changed unless its object hashes prove it.

## E4 — Branch and merge history (Requirement 3)

**Purpose:** Show the fast-forward merge and the conflict-resolving merge commit.

After both merges and branch deletions, run:

```bash
git log --oneline --graph --decorate --all
```

Paste the actual output:

```text
[PASTE ACTUAL OUTPUT HERE]
```

Also useful for checking the merge commit and its parents:

```bash
git show --no-patch --pretty=raw YOUR_MERGE_COMMIT_SHA
```

## E5(b) — Wrong-branch recovery (Requirement 5)

**Purpose:** Show the reflog evidence for moving the accidental `main` commit onto
`docs/usage-heading`, then merging that branch into `main`.

During/after the drill, run:

```bash
git reflog -n 15 --date=local
git log --oneline --graph --decorate --all -n 15
git status
```

Paste the actual output:

```text
[PASTE ACTUAL OUTPUT HERE]
```

Useful commands for the drill (adapt to your current state):

```bash
git branch docs/usage-heading
git reset --hard origin/main
git switch docs/usage-heading
git switch main
git merge docs/usage-heading
git push origin main
```

Do not run this sequence blindly. In particular, create the branch while the accidental
commit is still reachable, and verify the branch contains that commit before resetting
local `main`.

## E6 — Named stash before it is reapplied (Requirement 7)

**Purpose:** Show the named stash entry while the unfinished `list --sort` work is parked.

With your unfinished changes in the working tree, run:

```bash
git stash push -m "list-sort-work"
git stash list
```

Paste the actual stash listing **before applying the stash**:

```text
[PASTE ACTUAL `git stash list` OUTPUT HERE]
```

Then continue the bug-fix branch and pull request. When ready to resume the parked work:

```bash
git stash apply stash@{0}
git stash list
```

Check that the restored changes are correct before dropping the stash. The assignment asks
you to preserve the listing from before it was reapplied.

---

## Final checklist

- [ ] E1 — SSH remote output
- [ ] E3 — two commit hashes, two root tree hashes, identical blob, different blob
- [ ] E4 — history graph after Requirement 3
- [ ] E5(b) — wrong-branch reflog evidence
- [ ] E6 — named stash listing captured before applying it
- [ ] Actual outputs pasted; no placeholders remain
