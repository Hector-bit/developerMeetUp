# Git Procedure for contributors

Download the code by cloning with git
`git clone https://github.com/Hector-bit/DeveloperMeetUp`

Create the desired name attached to your individual contributions. (Commits)
`git config --global user.name "PeterStine"`

Confirm the name you entered.
`git config --global user.name`

Create the desired email attached to your commits.
`git config --global user.email "your email address"`

Confirm it.
`git config --global user.email`

Use helpful colors in terminal. (Optional step for CLI)
`git config --global color.ui auto`

Now you have the repository on your system and are ready to contribute to the project. At this point, please message another team member to see where help is needed most. You are also of course welcome to ask us if you'd like to add a feature you think would be useful if you have an idea for something. Once you hear back from us, you may start making changes. Communication is key!

## Do the following everytime you start a new work session

Before doing **anything**, please do a `git fetch` and a `git status`. The former updates your local computer storage with the current code on the github repo, and the latter will tell you what branch you are on and how many commits behind you are. **Please do not add code directly to the master branch**. That branch is reserved for peer-reviewed code and is meant to be the most stable version if something goes wrong with a development or testing branch. If you are in the master branch, switch to the appropriate branch as instructed by a project team member using the below command:

`git switch -c "branch-name"`

Or if instructed, create a new branch:

`git branch "branch-name"`

Use `git branch --list` to show existing branches if need be.





