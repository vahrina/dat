---
date: '2026-09-16'
draft: false
description: i git it now
title: bandit-29
weight: 30
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit29`                                   |
| pass | `Em7eGtqaMySwNFjCpwzzHhLhospOcdt0`         |

> There is a git repository at ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

> From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

---

## explanation

same process as [before](http://dat.vah.wtf/posts/overthewire/bandit/bandit-27/), clone the repo & see what is inside

```sh
git clone ssh://bandit29-git@bandit/home/bandit29-git/repo bandit29
# Cloning into 'bandit29'...

cd bandit29 && cat README.md
# # Bandit Notes
# Some notes for bandit30 of bandit.
#
# ## credentials
#
# - username: bandit30
# - password: <no passwords in production!>
```

time to check the mail

```sh
gloga
# gloga='git log --oneline --decorate --graph --all'
* a0e9e9c (origin/sploits-dev, sploits-dev) add some silly exploit, just for shit and giggles
| * 0bf8160 (origin/dev) add data needed for development
| * 1b95ced add gif2ascii
|/
* b607fba (HEAD -> master, origin/master, origin/HEAD) fix username
* 84c16f8 initial commit of README.md
```

the master branch diverted to `sploits-dev` & `dev` diverged from `master` at `b607fba`, let's check the difference between `0bf8160` & `1b95ced`

```sh
gd 0bf8160 1b95ced
# gd='git diff'
README.md --- Text
4 ## credentials                                4 ## credentials
5                                               5
6 - username: bandit30                          6 - username: bandit30
7 - password: jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX  7 - password: <no passwords in production!>
```

---

### for the curious

there are many more ways to find out about it rather than a diff, all descriptions taken directly from the [git docs](https://git-scm.com/docs)

```sh
gsps 0bf8160
# gsps='git show --pretty=short --show-signature'
# Shows one or more objects (blobs, trees, tags and commits).

git cat-file -p 0bf8160:README.md
# Provide contents or details of repository objects

git log -p --all -S 'password' -- README.md
# grep the object db for the password pattern across all commits

gbl 0bf8160 -- README.md
# gbl='git blame -w'
# Show what revision and author last modified each line of a file

git diff-tree -p 0bf8160
# Compares the content and mode of blobs found via two tree objects
```

let alone with `git log/show` will provide so much info, the possibilities are endless because git is such a deep rabbit hole
