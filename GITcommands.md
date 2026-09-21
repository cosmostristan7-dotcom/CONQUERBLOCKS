''' GIT COMMANDS '''

- `git status -s, --short:` It shows the end (la salida) in a better short format.

- `git status -b, --branch:` It shows the very branch (rama actual) plus the following information and status.

- `git status --show-stash:` It shows if something has been saved in the stash.

- `git status --ignored:` It also shows the ignored files.

* `git add` : To add files to my git repository.
* `git add .` : That dot {.} means here. Everything inside a folder.
* `git add -A` // `git add --all`

* `git add*.txt`,
  It will add all the files endind with these .txt extention.

# To SAVE changes made onto GIT:

1. In your terminal type: git add . // press enter.

- `git status`, press enter.
- `git add .` , press enter.
- `git commit -m` "lable your text", press enter.

` If things are RED, it means you have saved the changes in your computer, but you haven't packed them into the box yet (git commit).

` If things are GREEN, they are packed into the box to be locked in (git commit).

` If is says: "nothing to commit, working tree clean": Everthing is perfectly snapshotted and up to date.

## TO UPDATE YOUR LOCAL SAVINGS INTO GITHUB:

- `git push`: "after typing git status, git add, git commit -m + _labing the change made_; I have to finally type _git push_ in order for the file on github can be finally updated."

## TO SEE your savings history:

- `git log`, press enter.

## TO SEE the same but in a cleaner and shorter view:

- `git log` --oneline

## TO SEE your timelines (branches):

- `git branch`

- `git reset --hard` = 
  This is the command that overwrites my local branch  with a remote branch. 

# WHAT TO DO WITH RED TEXT:

- `git commit -am "added whaterver files I created"`, press enter.

# git log --online: it displays your history savings.

* `git revert HEAD` =
To undo a commit that is already up on the remote reposiorty.

* `git clone url-repository`, it clones a GITHUB repository.

* `git stash`, 
  saves my current changes and clears my working directory. 

* `git stash list`, shows me a list of all my saved stashes.

* `git stash pop`, 
  removes the most recent stash from the shelf and applies it back to my code.

* `git stash apply`, 
  applies the stash back to my code BUT KEEPS a copy on the shelf (great for applying to multiple branches).

* `git stash drop`, 
  throws away a specific stash without applyimg it. 

* `git stash clear`, 
  nukes my entire stash history (use with caution).

## git stash, 
ignores new files which I haven't untracked yet. (Files I haven't run // git add // on). In case I want to stash EVERYTHING, including untraked files, i need to use `git stash -u`.

* `git checkout --file.txt --file.md`, 
  it undone changes made before doing a commit.

* `git branch -m <new-name>`, 
  when I want to rename a current branch.

* `git branch -m <old-name> <new-name`>, 
  when I want to rename a different branch from afar.

* `git branch <name-branch>`, creates a new branch's name.

* `git merge <name-branch>`, 
  it is used to combine the history of another branch into my current one. It doesn't create anything new; it merges existing work. 

* `git switch <name-branch>`, changes a branch in git.

## TO DELETE A BRANCH IN GIT there are 2 ways:

* `git branch -d <branch-name>`, 
  deletes merged branch into the main branch. In any case I haven't merged my brach, git will stop me and ask me if I want to do it.

* `git branch -D <branch-name>`,
  force deletes or discards everything on the branch.

## HEAD in git means...
it is the alias for the most recent commit on the current branch.

* `git fetch`, 
  downloads my last repository version without merging any changes made. 

* `git rebase`, 
  rewrites history to create a clean, straight line with no extra merge commits (It's linear) // `git merge` (It preserves the exact chronological history and creates a special "merge commit" to tie the brances together).

## HOW TO DO A git rebase: 
zsh... (1. git checkou feature) // (2. git rebase main), enter.

* `git cherry-pick`, 
  Allows me to hand-pick a single commit from one branch and copy it onto another branch, wihtout moving any of the other code around it.

* `git init`, starts a git repository into a Directory. 
  Example: zsh... (1. cd ADAMANTIO, enter)// (2. git init, enter).

* `git rm --cached file.md`, 
  deletes a file without deleting from the hard-drive.

* `git push origin --deleting tag name-tag`, 
  deletes a tag from aremote repository. 

* `git branch`, lists all the repository branches.

* `git config --global alias.name "command"`, 
  can configuratean alias in git to shorter commands.

* `git fetch upstream`, 
  updates a fork (A FORK IS A COPY OF SOMEONE'S ELSE REPOSITORY, that I saved to my own account); from the original repository in GitHub.

* `git reset --hard commitID`, 
  I can get to the previous commit while the newest commits are removed. 

* `git reset --soft HEAD`,
  undone the last commit without lossing any changes made.

## Because Windows and macOS are case-insensitive, Git on your computer might look right past your change and say:
nothing to commit, working tree clean.
If that happens, it means Git didn't even notice you capitalized the S - (or whatever file name). If you push right now, GitHub won't update, and your website might break when you deploy it.
If git status ignores your hard work, don't panic! Just run this one command in your terminal first to force Git to see it:

* `git config core.ignorecase false`, 
  This will make a reset in GitCore, and when I type git status, it will see the actual change made (as unsaved).

## IF THE WEBPAGE SHOWS YOU AN ERROR 404 (PAGE NO FOUND), 
follow these steps to find exactly where this exact broken path is:

`A.` Right-click anywhere on your broken webpage.
`B.` Click on Inspect (or Inspect Element) at the very bottom of the menu. A window full of code will pop up on the side or bottom of your screen.
`C.` Look at the top menu of that new window and click on the Console tab. (WHAT TO LOOK FOR?)

# Inside that Console, you will see bright red error messages.
# It will be someting like this:

`GET https://yourwebsite.com/Stlye.css net::ERR_ABORTED 404 (Not Found)`

# TO FORCE MV (move or rename) a file through Git:

* `git mv -f "file.name" "File.name"`, press Enter
Since VSCode and GIT are case-unsensitive whenever you try to rename a file.name the petition won't be done, unless you force it ny using this command. 

Internet eyes are case-sensitive, therefore if by any chance it finds a lovercase file name, it will show you a 404 error. That's why your path Name.files must be case-sensitive. 

## to be continued...


