---
date: '2026-09-16'
draft: false
description: sometimes i wonder if git or the os sees more
title: bandit-30
weight: 31
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit30`                                   |
| pass | `jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX`         |

> There is a git repository at ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

> From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

---

## explanation

same process as [before](http://dat.vah.wtf/posts/overthewire/bandit/bandit-27/), clone the repo & see what is inside

```sh
git clone ssh://bandit30-git@bandit/home/bandit30-git/repo bandit30
# Cloning into 'bandit30'...

cd bandit30 && cat README.md
# just an epmty file... muahaha
```

no new branches.. no suspicious commits.. well maybe instead list the diff directly?

> autocompletion is your best friend, just saying

```sh
gd
# gd='git diff'
HEAD           master         origin         origin/HEAD    origin/master
secret
929c564  -- [HEAD]    initial commit of README.md (3 months ago)
```

get the secret & move on!

```sh
gsps secret
# gsps='git show --pretty=short --show-signature'
82NkymblpGBYmIXG6ZQ8YldBYstHpfUf
```
