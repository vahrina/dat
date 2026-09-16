---
date: '2026-09-16'
draft: false
description: indeed an information manager from hell
title: bandit-28
weight: 29
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit28`                                   |
| pass | `y8Yd2ssKcpHpud7UvOSOxwamRMzIGIeQ`         |

> There is a git repository at ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

> From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

---

## explanation

same process as [before](http://dat.vah.wtf/posts/overthewire/bandit/bandit-27/), clone the repo & see what is inside


```sh
git clone ssh://bandit28-git@bandit/home/bandit28-git/repo bandit28
# Cloning into 'bandit28'...

cd bandit28 && cat README.md
# # Bandit Notes
# Some notes for level29 of bandit.
#
# ## credentials
#
# - username: bandit29
# - password: xxxxxxxxxx
```

not much to go off, maybe the [log](https://man7.org/linux/man-pages/man1/git-log.1.html) can reveal anything?

> note that my shell is [zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH) where i am most familiar with [git aliases](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git), ill add the full command below the execution of the alias

```sh
gloga
# gloga='git log --oneline --decorate --graph --all'
* e2e1de5 (HEAD -> master, origin/master, origin/HEAD) fix info leak
* 2678cfa add missing data
* 9530d52 initial commit of README.md

gsps 2678cfa
# gsps='git show --pretty=short --show-signature'
commit 2678cfadd8f2a347bc23e1ea491f702e5b184709
Author: Morla Porla <morla@overthewire.org>

    add missing data

diff --git a/README.md b/README.md
index 7ba2d2f..42331d9 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials

 - username: bandit29
-- password: <TBD>
+- password: Em7eGtqaMySwNFjCpwzzHhLhospOcdt0
```

as expected, the latest [commit](https://www.reddit.com/r/learnprogramming/comments/6g3eja/what_are_git_add_and_git_commit_doing_and_how_are/) censors the password but git kept it in its history - refer to [git-filter-repo](https://github.com/newren/git-filter-repo) to properly rewrite history of sensitive data
