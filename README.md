#README.md

- Environment Setting
. git --version
. git config --global user.name 'Aaron Hon-Yu Ma'
. git config --global user.email 'hyma128@pu.edu.tw'
. git init
# browse to check a folder existed called .git

- Test File Building
. create a new file. #README.md and write something.
. save (ctrl + S)
. git add .
. git commit -m 'init readme.md'
. git status #check untracked file or folder
. git log --oneline

- push local Git to cloud GitHub
. browse GitHub
. login GitHub
. Create new repository
. copy the instruction*3 and paste to VS code terminal
. execute