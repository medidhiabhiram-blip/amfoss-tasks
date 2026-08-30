<!-- Exercise 1 -->

Git commands used: git verify

--> Used a custom-built command called git verify to complete the first task.

<!-- Exercise 2 -->

Git commands used: git add, git commit -m

git add --> It basically selects the items to be committed from the working directory.

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

<!-- Exercise 3 -->

Git commands used: git reset, git commit, git status

git status --> This command helps check which files have been added, modified, or removed. It shows the current state of the repository.

git reset --> This helps reverse git add. It removes the file from the list of files that are going to be committed.

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

<!-- Exercise 4 -->

Git commands used: git add ., touch .gitignore, git commit

touch .gitignore --> I created a file named .gitignore and added extensions like *.exe and folders using folder/ so they would be ignored while adding files for the commit.

git add --> It basically selects the items to be committed from the working directory. The . adds all the files and folders in the working directory.

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

Challenges faced: I thought adding a folder to gitignore would automatically ignore all the files inside it. It actually does, but since we are using git verify, we have to follow the instructions and also specify the extensions of the files inside the folder.

<!-- Exercise 5 -->

Git commands used: git merge

git merge --> This is used to combine two different branches into one.

<!-- Exercise 6 -->

Git commands used: git add ., git merge, git commit

git merge --> This is used to combine two different branches into one. When conflicts occur, we need to solve them manually and then use git add followed by git commit.

git add --> It basically selects the items to be committed from the working directory. The . adds all the files and folders in the working directory.

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

Challenges faced: I was going over the commit limit many times.

<!-- Exercise 7 -->

Git commands used: git add, git stash, git stash pop, git commit

git add --> It basically selects the items to be committed from the working directory. The . adds all the files and folders in the working directory.

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

git stash --> When running git stash, Git takes all of the current uncommitted changes, including modified tracked files and staged changes, and temporarily stores them away.

git stash pop --> Git takes the most recent stash and applies those changes back to the current working directory. It works in a LIFO stack format.

Challenges faced: The question instructions were confusing, so I had to try multiple times.

<!-- Exercise 8 -->

Git commands used: git rebase

git rebase --> It basically helps us move changes from one branch to another. For example, if we have a baseline commit A and a commit B on top of A, but there was a bug that we fixed by returning to A and creating another branch C, then we can use git rebase to bring the fix and features of C into B. It becomes A --> C --> B.

<!-- Exercise 9 -->

Git commands used: git rm

git rm --> At its core, git rm does two things at once: it deletes a file from the hard drive (working directory) and immediately stages that deletion for the next commit.

If we only use rm, the file is removed from the hard drive, but Git marks it as an unstaged deletion. To actually commit that deletion, we would have to run git add afterward.

--cached flag --> Git stops tracking the file but leaves it on the hard drive.

-r flag --> Deletes a folder and everything inside it.

-f --> Allows us to force a deletion.

<!-- Exercise 10 -->

Git commands used: git mv

git mv --> This command can be used to rename or move a file or directory, and the change is automatically staged for commit. We can rename a file, move it to another directory, or do both at the same time.

If we use the terminal's standard mv command to rename a tracked file, we need additional Git commands to track the new file and remove the old one.

<!-- Exercise 11 -->

Git commands used: git commit --amend

git commit --amend --> git commit --amend is a "fix-it" command. It lets us modify our most recent commit instead of creating a new one to fix a minor mistake.

It can be used to change the commit message, add forgotten files, or make changes to some files.

--no-edit flag --> This tells Git to keep the exact same commit message.

-a flag --> This can be used to automatically add the files without using git add, which skips one step.

Git does not actually edit the old commit. It completely removes the old one and replaces it with a new commit that has a new, unique ID/hash.

<!-- Exercise 12 -->

Git commands used: git commit --amend --date=""

git commit --amend --date --> You can change the date and time of a previous commit using this command with --date="YY-MM-DD HH:MM:SS".

If you want to set the time to the current time, you can use --reset-author instead of date. This changes both the committer and author date.

Note: date only changes the author date. If you want to change the committer's date, you need to specify GIT_COMMITER_DATE="date time" before the git commit --amend command.

<!-- Exercise 13 -->

Git commands used: git rebase -i, git rebase --continue, git commit --amend

git commit --amend --> git commit --amend is a "fix-it" command. It lets us modify our most recent commit instead of creating a new one to fix a minor mistake.

It can be used to change the commit message, add forgotten files, or make changes to some files.

git rebase -i --> This command opens the interactive nano mode. When using this command, the commits that have not been pushed are shown with their commit messages and hashes. If you want to edit a commit, you can change pick in front of it to edit. You can use drop if you want to delete a commit. After saving and exiting nano, Git will ask you to amend any changes you want to make.

git rebase --continue --> After you have committed the changes you wanted to make, you can use this command to continue the rebase and return to your current branch. Git will continue replaying the newer commits on top of the changes you made. When the command finishes, you will be back at the present tip of your branch. Any conflicts should be resolved before running this command again.

Note: rebase works similarly to merge, but rebase keeps the branch history cleaner than git merge.

<!-- Exercise 14 -->

Git commands used: git reflog, git reset --hard

git reflog --> It records a chronological list of every time your HEAD pointer moved. Whenever you commit, checkout a branch, rebase, amend, or reset, reflog records where you were. Unlike git log, it keeps track of commits even after an amend.

git reset --hard <hash> --> git reset is used to move the current branch pointer to a specific commit. The --hard flag tells Git to forcefully move to that commit.

<!-- Exercise 15 -->

Git commands used: git reset, git add, git commit

git reset --> We use this to change our current branch pointer to an older commit.

--hard --> Rewinds history, clears the staging area, and also changes the files to exactly match the previous branch.

--soft --> Does not delete anything and leaves the changes fully staged.

default --> Leaves the files changed but does not stage them.

git add --> It basically selects the items to be committed from the working directory. The . adds all the files and folders in the working directory.

<!-- Exercise 16 -->

Git commands used: git log, git rebase -i, git commit --amend, git rebase --continue

git log --> git log -2, for example, helps to view the last two commits.

git rebase -i --> This command opens the interactive nano mode. The commits that have not been pushed are shown with their commit messages and hashes. If you want to edit a commit, you can change pick to edit. You can use drop if you want to delete a commit. After saving and exiting nano, Git will ask you to amend the changes.

git commit --amend --> git commit --amend is a "fix-it" command. It lets us modify our most recent commit instead of creating a new one to fix a minor mistake.

It can be used to change the commit message, add forgotten files, or make changes to some files.

git rebase --continue --> When everything is done and committed, you use this command to continue the rebase and go back to your current branch.

Note: I bruteforced this exercise by completely deleting the second commit and copying its message and pasting it into the first one.

But the easier method would be to use the -s flag or squash the second commit.

An even easier method would be to use git reset --soft HEAD~2, which would automatically do the work for you.

<!-- Exercise 17 -->

Git commands used: git update-index --chmod=+x .sh, git commit -m

git update-index --chmod=+x --> We are trying to make a shell script (.sh) executable. A shell script is normally a plain text file, and this command makes it executable by a Unix shell.

git update-index --> Normally, git add is used to stage files. However, git update-index allows us to directly modify how Git tracks a file's metadata, such as its permissions.

--chmod=+x --> chmod stands for change mode, and +x means executable. Together, this tells Git to update the index and mark the file as executable, regardless of what the local computer thinks.

The above information is what we are passing to the index.

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

<!-- Exercise 18 -->

Git commands used: git add -p, git commit -m

git add -p --> When you run this command, Git compares the current working file with the last saved commit. It identifies every line that was added, modified, or deleted.

Git groups changes that are close together into a block called a hunk.

For every hunk, Git pauses and asks what you want to do with it. It gives options such as y, n, s (split), and e (edit).

-p stands for patch mode.

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

<!-- Exercise 19 -->

Git commands used: git log --oneline, git reflog, git cherry-pick, git add, git commit -m

git commit -m --> This creates a commit for the items that were added. The -m allows us to add a message explaining what we did.

git cherry-pick --> git cherry-pick allows us to take a specific commit from one branch and apply a copy of it to the current working branch. When we run git cherry-pick <commit-hash>, Git takes the changes from that specific commit and applies them to the current code.

git reflog --> It records a chronological list of every time your HEAD pointer moved. Whenever you commit, checkout a branch, rebase, amend, or reset, reflog records where you were. Unlike git log, it keeps track of commits even after an amend.

git add --> It basically selects the items to be committed from the working directory. The . adds all the files and folders in the working directory.

git log --oneline --> This is a shortcut command that gives a clean view of the branch's commit history.

Challenges faced: Cherry-pick was confusing to use, and getting the exact branch and single commits required for the exercise was challenging.

<!-- Exercise 20 -->

Git commands used: git rebase --onto <destination> <boundary>

git rebase --onto --> This basically takes the commits after the boundary branch and rebases them onto the destination branch.

<!-- Exercise 21 -->

Git commands used: git rebase -i

git rebase -i --> In this exercise, we use git rebase -i and in the interactive nano menu we switch the commits around. The top is the oldest commit and the bottom is the newest commit.

<!-- Exercise 22 -->

Git commands used: git log -S "word" file1.txt file2.txt, git rebase -i, git commit --amend -a --no-edit

git log -S --> This helps filter the commits that contain the specified word in the specified files and lists them.

git rebase -i --> We can then use interactive rebase mode and change pick to edit for the commits we found earlier.

git commit --amend -a --no-edit --> After making the changes, this command automatically adds and commits them. The --no-edit keeps the same commit message.

<!-- Exercise 23 -->

Git commands used: git bisect start, git bisect reset, bisect bad, bisect good 1.0, git bisect run sh -c "openssl enc -base64 -A -d < home-screen-text.txt | grep -v jackass"

git bisect reset --> This is the emergency stop button. If you are in the middle of a bisect search and make a mistake, this cancels the search and moves your HEAD back to exactly where it was before you started.

git bisect start --> This command starts the bisect search.

git bisect bad --> Tells Git that the commit you are currently on is broken and contains the bug. Git marks it as the "Bad" boundary.

git bisect good 1.0 --> Tells Git that the commit carrying the 1.0 tag is working correctly. Git marks it as the "Good" boundary. Now Git knows the range of commits where the bug was introduced.

git bisect run... --> Instead of manually testing every commit, this tells Git to automatically run a specific script on every commit it checks.

The decoding script:

sh -c --> Tells the terminal to open a temporary shell just to execute the commands inside the quotes.

openssl enc -base64 -A -d < home-screen-text.txt --> This takes the home-screen-text.txt file, which is encoded in base64, and uses openssl to decode it (-d) back into readable English.

| --> This is a connector. It takes the readable English from the first command and sends it to the other command.

grep -v jackass --> grep is a search tool. Normally, it searches for a word. The -v flag reverses the search. It tells the computer to return success (0) if the word "jackass" is not found, and failure (1) if it is found. Git uses these success and failure codes to know if the commit is good or bad.

Challenges faced: It was difficult to understand exactly what we had to do and also what the commands did and how they worked.

