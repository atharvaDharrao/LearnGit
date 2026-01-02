print("hello world")

print("byr world")

print("THIRD LINE")

"""
1. git init
2. git add . ==> (So you are telling Git:“I want all these changes to be included in the next commit.”)
3. git commit -m "Initial Commit"
4. git branch -M main ==> (Renames the branch to main, -M means force rename) 


5. git branch ==> (to check all the branches in remote repository)
**note**:
git branch -r: Lists all remote-tracking branches (the branches on the remote repository, like GitHub or GitLab) [1].
git branch -a: Lists both local and remote-tracking branches [1]. 

6. git status ==> (to check status : modified or not)
7. git log --oneline ==> (to check all the commits inside a branch)




[1] What is branch in Git ?
==> A branch is an independent line of development.
==> A separate workspace where you can work without breaking the main code.

**Imp Commands**
1. git branch feature-login ==> Create a new branch
2. git checkout feature-login / git switch feature-login ==> Switch to a branch



🧪 Working example (real workflow)
Step 1: Start from main
git checkout main
git pull

Step 2: Create feature branch
git checkout -b feature-url-validation

Step 3: Work & commit
git add .
git commit -m "Add URL validation"

Step 4: Merge back to main
git checkout main
git merge feature-url-validation

🔀 What is merging?

Merging combines changes from one branch into another.

main  ←  feature-branch
"""