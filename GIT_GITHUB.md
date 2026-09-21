### GIT:

It is a software that allows your projects to be updated in a enfficiency way.

It allows you to work with remotly consoles across any country.

Let's portriat this case, let's say our coding softwares is a very long horizontal line, where we have a couples of updating sets we had done in the past. If we cannot remember our first update for example, and there is no way we can get there, using GIT, specifically using COMMIT concept, we could easily get there. We could move backwards or foward on every update we did in the past.

Without GIT we would have to erase the entire coding line, or wait 'til we finish it in order to check where our mistake is.

GIT can be divided into several branches; while we can focus on dectecting and fix an error in our code, this change at then same time while using GIT, won't affect certain functionalities. Basically, GIT allows us to work in parallellism. GIT allows several web developers to work in a specifict projetc without affecting each individual rearrangements.

## Where does GITHUB takes place?

GITHUB is like the esambling system that allows us to work as a team with more tha a million individuals, remotly or not. And yet this interactions won't entangled. GITHUB will host our code and thus, will allow us to interact with it on different ways (on a cloud).

## GIT PREPARING MY PROJECT:

Initialize GIT: type: "get init" (This create a hidden folder that tracks every change I made).

Check the status: type: "git status" (This shows you which files are new or have been changed).

## SAVE MY CHANGES:

In GIT, saving isn't just pressing "SAVE". I have to add the files to a staging area and then "commit" them with a message.

ADD FILES: type: git add (The dot . means "add everything in this folder")

COMMIT (SAVE): type: git commit -m "First commit of my Course List Project" (This -m stands for "message". Always describe what you changed).

### CONNECT TO GITHUB.

To put my code "in the cloud" GITHUB, I need to link my local folder to a GITHUB repository.

1. Create a new repository on the GITHUB website.
2. Link it in my terminal: type: git remote add origin
   [https://github.com/yoursuername/your-repository.git]

### UPLOAD MY CODE: (these /// are not part of the code).

Now I can push my code from my macOS to GITHUB.
PUSH THE CODE: type: /// git push -u origin main /// (After I do this once, I usually only need to type: /// git push /// in the future).

# COMMAND AND WHAT IS DOES: remember to code this on a file.html and add this to your GITHUB projects.

COMMANDS:

1. git log (shows a history of all my "commits" //saves//).
2. git diff (shows exactly what lines of code I changed).
3. git pull (downloads the latest version from GITHUB to my computer).
4. git init (starts my new proyect, but I have to be within the main folder for that specific project).

## GIT CONFIGURATION:

5. git config --global init.defaultBranch main //Press ENTER//
   (I can change/modify my name).
6. git config --global user.email
   (I can set my email address).
7. git config --global core.editor
   "code --wait"

# WE CHECK THIS OUT BY TYPING:

8. git config --global -e

# TO CHECK IF I HAVE A GIT REPOSITORY, TYPE THIS COMMAND:

git status . // press enter.

GRAMMAR POINT:
Use ON for the machine: I have GIT ON my MacBook.
Use IN for the terminals/files: I am typing commads IN the terminal.

# To SAVE changes made onto GIT:

1. In your terminal type: git add . // press enter.

2. Seal and label the box, always in your terminal: git commit -m "your description here" // press enter.

3. Check your work, type: git status // press enter.

` If things are RED, it means you have saved the changes in your computer, but you haven't packed them into the box yet (git commit).

` If things are GREEN, they are packed into the box to be locked in (git commit).

` If is says: "nothing to commit, working tree clean": Everthing is perfectly snapshotted and up to date.

## WORK AREA:

It's the local directory where all the files are created and then modified.

## STAGIN AREA (AREA DE PREPARACION).

It's an in between area where all the working files are placed and pending to be worked out.

## COMMIT AREA OR LOCAL REPOSITORY.

This repository must be created in the local place. and in here all the modified files will be saved. From this local place, they will be moved to the remote repository.

## REMOTE REPOSITORY.

This repository is out from our local cpu. And here you will find all the files confirmed and modified. It is possible to set a sync between the local cpu and the remote.

HEAD: It is a pointer that aims to a specific change or photo we have done at some point in our main file.

# HOW TO ADD NEW REPOSITORIES:
1. Create a repository on GitHub
2. Go to GitHub.com in your browser and log in.
3. Click the green "New" button to create a new repository.
4. Name it Dioramas1 (matching your local folder).
Leave "Initialize this repository with" blank (don't check README, .gitignore, or license, since you already made those files locally).
5. Click Create repository.

`Link your Mac folder to GitHub`
Type these 1 line at a time: 
1. git remote add origin https://github.com/YOUR_USERNAME/Dioramas1.git
2. git branch -M main
3. git push -u origin main
   
   