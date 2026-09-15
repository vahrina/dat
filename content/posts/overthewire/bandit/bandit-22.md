---
date: '2026-09-15'
description: a cron j*b is actually a good thing
draft: false
title: bandit-22
weight: 23
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit22`                                   |
| pass | `RYVux2rHEm9tiXHmLFzuR7Vhx6AZQMEz`         |

> A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

> **NOTE:** Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

---

## explanation

cron was briefly explained in the [previous](http://dat.vah.wtf/posts/overthewire/bandit/bandit-21/) post

same story as before

```sh
cat /etc/cron.d/cronjob_bandit23
# @reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
# * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```

plus the script

```sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

dissecting it:
1. save "bandit22" into the `myname` variable
2. `mytarget`:
  - 2.1 pipe `echo I am user $(whoami)` into [`md5sum`](https://man7.org/linux/man-pages/man1/md5sum.1.html) yields `8169b67bd894ddbb4412f91573b38db3`
  - 2.2 [`cut`](https://man7.org/linux/man-pages/man1/cut.1.html) splits on space (`-d ' '`, a **d**elimiter) & `-f 1` yields the first field. because `md5sum`'s output format is `hash -`, a trailing ` -` would be included in the digest
3. save `mytarget` as `/tmp/<hash>`
4. copy `bandit22`'s password into `/tmp/<hash>`

now the problem is, although `bandit23` created the file, it's executing & copying the password from our current user `bandit22`

```sh
# Access: (0750/-rwxr-x---)  Uid: (11023/bandit23)   Gid: (11022/bandit22)
```

the clue is in the cron job itself, every (re)boot it launches the script as `bandit23`, but the next problem is we can't look into `/tmp` at all - second guessing or tab completion is prohibited:

```sh
# File: /tmp
# Access: (1773/drwxrwx-wt)  Uid: (    0/    root)   Gid: (    0/    root)
```

the sticky bit `t` in the others category is set, which means:
- 1 (sticky): restrict file renaming / deletion; only the file/dir owner (or root) are privileged
- 7 (owner): grants the owner rwx perms
- 7 (group): grants the group rwx perms
- 3 (other): grants other users wx perms

butttt hashes are deterministic: the same input produces the same output, e.g. `echo cat | md5sum` will always yield `54b8617eca0e54c7d3c8e6732c6b687a` plus trailing dash

and because the script reveals the logic, we could just uhhhh

```sh
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
# 8ca319486bfbbc3663ea0fbe81326349
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
# gKXDTAXnIz3OBxiPjRZ2uqutUlPZrBsw
```
