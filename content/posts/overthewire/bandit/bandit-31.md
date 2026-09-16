---
date: '2026-09-16'
draft: false
description: did you pull first?
title: bandit-31
weight: 32
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit31`                                   |
| pass | `82NkymblpGBYmIXG6ZQ8YldBYstHpfUf`         |


---

## explanation

same process as [before](http://dat.vah.wtf/posts/overthewire/bandit/bandit-27/), clone the repo & see what is inside

```sh
git clone ssh://bandit31-git@bandit/home/bandit31-git/repo bandit31
# Cloning into 'bandit31'...

cd bandit31 && cat README.md
# This time your task is to push a file to the remote repository.
#
# Details:
#     File name: key.txt
#     Content: 'May I come in?'
#     Branch: master
```

should not be too hard

```sh
cat > key.txt <<eof
May I come in?
eof
```

nothing seems to be tracked tho

```sh
gss
# git status --short
#
```

the current dir has 2 files & 2 git objects

```sh
l
# l='eza --icons=auto --group-directories-first --git --no-time
#  --no-filesize --classify=always -A -l --no-permissions
#  --octal-permissions --no-user --no-git'
# long alias i know haha
0755  .git/
0644 󰊢 .gitignore
0644  key.txt
0644 󰂺 README.md
```

ahaaa a [`.gitignore`](https://git-scm.com/docs/gitignore) file, which coincidentally ignores the created `keys.txt` file, so it is basically never tracked

```sh
rm .gitignore && gss
# rm: remove regular file '.gitignore'? y
# removed '.gitignore'
#  D .gitignore
# ?? key.txt
```


<details>
  <summary>git & keypairs</summary>

feel free to create a pair of [ssh keys](https://www.youtube.com/watch?v=yVP3sYgd0bY) if you haven't done so, it may prompt you for a passphrase since the initial clone was with [ssh instead of https](https://serverfault.com/questions/832899/difference-between-https-git-clone-and-ssh-git-clone#answer-832904)

```sh
grv
# grv='git remote --verbose'
origin  ssh://bandit31-git@bandit/home/bandit31-git/repo (fetch)
origin  ssh://bandit31-git@bandit/home/bandit31-git/repo (push)
#       ^^^

```
</details>

not yet tracked, but it is finally visible to git - [add](https://git-scm.com/docs/git-add.html#_options) it to the index, a nice [commit message](https://git-scm.com/docs/git-commit) & [push](https://git-scm.com/docs/git-push) to the `master` branch

```sh
gaa
# gaa='git add --all'

gcmsg 'knock knock'
# gcmsg='git commit --message'
Enter passphrase:
# [master 79cedc3] knock knock
#  2 files changed, 1 insertion(+), 1 deletion(-)
#  delete mode 100644 .gitignore
#  create mode 100644 key.txt
```

although it won't push to the origin, the remote responds with the password

```sh
bandit31-git@bandit.labs.overthewire.org's password:
# remote: ### Attempting to validate files... ####
# remote:
# remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
# remote:
# remote: Well done! Here is the password for the next level:
# remote: pWuj5jBQ6IgV0NXwiH6g1pXRF8S1YvbT
# remote:
# remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
```
