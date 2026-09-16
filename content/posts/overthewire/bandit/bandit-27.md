---
date: '2026-09-16'
draft: false
description: git some of this
title: bandit-27
weight: 28
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit27`                                   |
| pass | `STJLJBRRphMxKB392CT4iOr5CbzPU9ER`         |

> There is a git repository at ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

> From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

---

## explanation

install "[the information manager from hell](https://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290)", [git](https://github.com/git/git)

> please refer to the [installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if you have never worked with git

clone the repo from your **local** machine & see what is inside

```sh
git clone ssh://bandit27-git@bandit/home/bandit27-git/repo bandit27
# Cloning into 'bandit27'...

cat bandit27/README
# The password to the next level is: y8Yd2ssKcpHpud7UvOSOxwamRMzIGIeQ
```
