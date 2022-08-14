git --version
touch index.html

# To initialize a folder as git folder
git init

# To set configurations
git config --global user.name "User Name"
git config --global user.email "you@example.com"


# To check above set configurations
git config user.name
git config user.email


# To stage a file
git add index.html

# To check current status of all files
git status

# To unstage a file
git rm --cached index.html

# To add all html files for staging
git add *.html

# To add all files for staging
git add .

# Commit
git commit
git commit -m 'changed app.js'

# To exclude some miles from being committed enlist them in gitignore
touch .gitignore      

# Craete a branch
git branch login
# Change to branch
git checkout login
# To merge login branch to master
git merge login

# Add remote repository
git remote add origin https://github.com/AjeetSingh02/git_tutorial.git

# Check remote repository
git remote

# Remove remote repository
git remote rm origin

# Pushing Pulling to remote repository for first time
git push -u origin master
git push --set-upstream origin master

git pull origin master


# Push and Pull
git push
git pull

# To push without ID/Password by using SSH
https://stackoverflow.com/questions/8588768/how-do-i-avoid-the-specification-of-the-username-and-password-at-every-git-push