# Evidence: Student A

## E1 · A: git remote -v

```

F:\lantern>git remote -v
origin  https://github.com/hazem-gamal-1/lantern.git (fetch)
origin  https://github.com/hazem-gamal-1/lantern.git (push)
```

## E2 · A: status + both diffs

```
F:\lantern>git add tasks.py

F:\lantern>git status
On branch main
Your branch is behind 'origin/main' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   tasks.py


F:\lantern>git status
On branch main
Your branch is behind 'origin/main' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   tasks.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   tasks.py


F:\lantern>git diff tasks.py
diff --git a/tasks.py b/tasks.py
index c6ee9c2..1f388f9 100644
--- a/tasks.py
+++ b/tasks.py
@@ -8,4 +8,7 @@ def add_task(title):


 def list_tasks():
-    return _tasks
\ No newline at end of file
+    return _tasks
+
+
+#a comment to show the difference
\ No newline at end of file

F:\lantern>git diff --staged tasks.py
diff --git a/tasks.py b/tasks.py
new file mode 100644
index 0000000..c6ee9c2
--- /dev/null
+++ b/tasks.py
@@ -0,0 +1,11 @@
+_tasks = []
+
+
+def add_task(title):
+    task = {"title": title}
+    _tasks.append(task)
+    return task
+
+
+def list_tasks():
+    return _tasks
\ No newline at end of file
```

## E4 · A: graph

```
F:\lantern>git log --graph
*   commit a7514740dd47d51ff9980a4ad19e57c1ee791ba1 (HEAD -> main)
|\  Merge: d144429 1584445
| | Author: Hazem Gamal <hazem.ml.eng@gmail.com>
| | Date:   Wed Nov 4 17:30:02 2026 +0200
| |
| |     Merge branch 'feature/done-flag'
| |
| |     # Conflicts:
| |     #       tasks.py
| |
| * commit 15844456775855c5fcb3ba5f63913c9895945940
| | Author: Hazem Gamal <hazem.ml.eng@gmail.com>
| | Date:   Wed Nov 4 17:26:45 2026 +0200
| |
| |     feat(tasks): add done flag
| |
* | commit d14442967a92e979ad5f451222baddd5d1b887be
|/  Author: Hazem Gamal <hazem.ml.eng@gmail.com>
|   Date:   Wed Nov 4 17:25:19 2026 +0200
|
|       fix(tasks): strip whitespace from title
|
*   commit e74ae194f1102ca5420c4f129d38cdcb3510d283 (origin/main, origin/HEAD)
|\  Merge: 2df85cd 2f9b8ea
| | Author: Hazem Gamal <hazem.ml.eng@gmail.com>
| | Date:   Wed Nov 4 16:59:56 2026 +0200
| |
| |     Merge branch 'main' of https://github.com/hazem-gamal-1/lantern
| |
| * commit 2f9b8ea04fc62254e9de0985ec3312b03cdadbb0
| | Author: Abdelrahman Rady <abdo.radi225@gmail.com>
| | Date:   Wed Nov 4 16:56:24 2026 +0200
| |
| |     chore(scratch): remove scratch placeholder
| |
| * commit 97ecbd3ff07ffcd1b9c6373d2f706505c55d6071
| | Author: Abdelrahman Rady <abdo.radi225@gmail.com>
| | Date:   Wed Nov 4 16:55:55 2026 +0200
| |
| |     chore(scratch): add scratch placeholder
| |
| * commit 51012fb814d9a322c913b60702725001d55b08c1
| | Author: Abdelrahman Rady <abdo.radi225@gmail.com>
| | Date:   Wed Nov 4 16:30:20 2026 +0200
| |
| |     docs(usage): add list example
| |
| * commit 1b623d2ce6cef54160101f72b2aa715c42d68759
| | Author: Abdelrahman Rady <abdo.radi225@gmail.com>
| | Date:   Wed Nov 4 16:29:45 2026 +0200
| |
| |     docs(usage): describe commands
| |
| * commit ee5f7b7b5845755338f45133ad2d7b99e35ca13b
| | Author: Abdelrahman Rady <abdo.radi225@gmail.com>
| | Date:   Wed Nov 4 16:26:21 2026 +0200
| |
| |     feat(storage): add load and save
| |
* | commit 2df85cdd6236c27e3f71a9bf31dffd582cfc7284
|\| Merge: c9a393c 1d75b05
| | Author: Hazem Gamal <hazem.ml.eng@gmail.com>
| | Date:   Wed Nov 4 16:59:49 2026 +0200
| |
| |     Merge branch 'main' of https://github.com/hazem-gamal-1/lantern
| |
| *   commit 1d75b05a32192254aeb5378fcdfb626d1eab69b0
| |\  Merge: fbc7294 727532a
| | | Author: Abdelrahman Rady <abdo.radi225@gmail.com>
| | | Date:   Wed Nov 4 16:07:03 2026 +0200
| | |
| | |     Merge branch 'main' of github.com:hazem-gamal-1/lantern
| | |
| | |     # Conflicts:
| | |     #       README.md
| | |
| * | commit fbc72944d22594ee60e27fb5bd748d55adeb39dc
| | | Author: Abdelrahman Rady <abdo.radi225@gmail.com>
| | | Date:   Wed Nov 4 15:59:41 2026 +0200
| | |
| | |     docs(readme): add Abdelrahman Rady to team table
| | |
* | | commit c9a393cb5baa71fb4d39a9d7cf7a9f6115e6f1ed
| | | Author: Hazem Gamal <hazem.ml.eng@gmail.com>
| | | Date:   Wed Nov 4 16:23:52 2026 +0200
| | |
| | |     refactor(notes): rename draft to notes
| | |
* | | commit 3f11976eff486344436c1fa2a45772c04bba6aee
| | | Author: Hazem Gamal <hazem.ml.eng@gmail.com>
| | | Date:   Wed Nov 4 16:23:03 2026 +0200
| | |
| | |     chore(notes): add draft placeholder
| | |
* | | commit 5a1b196eb0e13bb196f16dd448b8291fa36758e8
| | | Author: Hazem Gamal <hazem.ml.eng@gmail.com>
| | | Date:   Wed Nov 4 16:21:48 2026 +0200
| | |
| | |     feat(cli): add argparse add and list
| | |
* | | commit a197d3c0712c8f85c519b02f48c30cfd0d1e6dea
| |/  Author: Hazem Gamal <hazem.ml.eng@gmail.com>
|/|   Date:   Wed Nov 4 16:20:50 2026 +0200
| |
| |       feat(tasks): add add_task and list_tasks
| |
* | commit 727532ac2aba9350feeeef9c9441e05f20440adf
|/  Author: Hazem Gamal <hazem.ml.eng@gmail.com>
|   Date:   Wed Nov 4 16:00:23 2026 +0200
|
|       docs(readme):add Hazem Gamal to team table
|
* commit 65bad5fae639a601858de61b1f741d33bba6027b
  Author: Hazem Gamal <111183931+hazem-gamal-1@users.noreply.github.com>
  Date:   Wed Nov 4 15:00:25 2026 +0200

      Initial commit
(END)

```

## E5 · A: reflog drill (a)

```
PS F:\lantern> git reflog -5
fd5438b (HEAD -> main) HEAD@{0}: commit (amend): docs(notes): add first note
9fd8fb8 HEAD@{1}: commit: docs(notes): add frist note
4559814 (origin/main, origin/HEAD) HEAD@{2}: pull: Fast-forward
0e85c3a HEAD@{3}: commit: fix(git): stop tracking .env
c33d062 HEAD@{4}: reset: moving to HEAD~1
```

## E5 · A: reflog drill (c)

```
PS F:\lantern> git reflog -5 
fd5438b (HEAD -> main) HEAD@{0}: reset: moving to HEAD~1
12d3e16 HEAD@{1}: commit: docs(notes): add second note
fd5438b (HEAD -> main) HEAD@{2}: commit (amend): docs(notes): add first note
9fd8fb8 HEAD@{3}: commit: docs(notes): add frist note
4559814 (origin/main, origin/HEAD) HEAD@{4}: pull: Fast-forward
PS F:\lantern> git reset --hard 12d3e16 
HEAD is now at 12d3e16 docs(notes): add second note
```

## E7 · A: rejected push output

```
F:\lantern>git push origin main 
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 196 bytes | 196.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: Review all repository rules at https://github.com/hazem-gamal-1/lantern/rules?ref=refs%2Fheads%2Fmain
remote: 
remote: - Changes must be made through a pull request.
remote: 
To https://github.com/hazem-gamal-1/lantern.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/hazem-gamal-1/lantern.git'

```
