            ''' USEFUL SHORTCUTS FOR MAC CHIP M4 '''

* `CONTROL + 1BACKTICK`, to open the terminal using the VSCode.

* `CONTROL + SHIFT + 1BACKTICK`, to open a new second terminal in your VSCode.

* `COMMAND + S`, saves whatever change you have done recnetly in your VScode. 

* `To open the in-built-server`, type on the file or folder, but in the terminal area: ...python -m http.server

* `OPTION + SPACE`, opens COPILOT.

* `COMMAND + SPACE`, This is to search any app or enter to the terminal shortcut.

# USE DRANG & DROP TRICK: 
When moving files or folders using your VS Code, let's say you are inside the folder where you want to move the elementes, in your terminal, type cd + space,

Here, open finder, and drag the file or folder you want to move, RIGHT on the relative path on your terminal.

Press SPACE, then type a . dot, then enter.  
This dot . means here, the file or folder will move to where you are in your terminal.

# Pro-Tip for VS Code:
Instead of scrolling and hunting line-by-line, press Ctrl + F (Windows) or Cmd + F (Mac) inside VS Code and type in <li> `` or `. This will highlight every single spot where those rogue backticks are hiding so you can delete them or swap them out for ` tags instantly! 

* `by typing inside a file.md`, ```sql ...you add your code;```, all the code withing will be turn into SQL language.

* `CMD + R`, inside GitHub or any browser page, it refresh or reload the page.

<!-- ----------------------------------- --------------------- --> 
<!-- ----------------------------------- --------------------- -->

# SETTING UP DOCKER.-

1. On your Terminal, you have to initalize `Docker init`. Inside the folder where you have the &lt;index.html&gt;.
2. Docker will do the hard work for you. It will create what you need by automatically generating the Dockerfile, .dockerignore, and docker-compose.yml files for you!
3. Once your container is created follow these steps:
<!-- ------------------------------------------------------- -->
A. Type this command into your terminal and press Enter:
`docker compose up --build -d`
<!-- ------------------------------------------------------- -->
# What it does:
<!-- ------------------------------------------------------- -->
`--uild`: Tells Docker to build the image using the new files it just generated.
`-d`: Runs it in detached mode (in the background).
<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->
(Note: You saw a small warning about an "orphan container" html-app-1 because we changed the service name from when it was the old template. If you ever want to clean that old container up, you can just run docker compose up --build -d --remove-orphans).
<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->
# In order to stop Docker from running on the background, run this command on your Terminal:
`docker compose down`, press enter.

# To re-start the process again, run instead:
`docker compose up -d`
<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->
