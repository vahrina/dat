---
date: '2026-09-15'
description: i would NEVER eavasedrop
draft: false
title: bandit-20
weight: 21
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit20`                                   |
| pass | `4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA`         |

> There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

> **NOTE:** Try connecting to your own network daemon to see if it works as you think

---

## explanation

setuid was explained in the [previous](https://dat.vah.wtf/posts/overthewire/bandit/bandit-19/) post

you may want to use [tmux](https://man7.org/linux/man-pages/man1/tmux.1.html) to make it a bit more comprehendable, left side sending input right side receiving output. for this, i'll mostly utilize [job control](https://linuxcommand.org/lc3_lts0100.php) to receive the password

```sh
nc -lvp 8888 &
```

set up the listener we will receive stdout from; `&` will run it as a background process. ctrl-z will suspend it, `bg "%<id/name>"` will background it too (you may omit "%id/name", if you want to background your last suspended command)

repeat the same process for the program with the setuid bit

```sh
./suconnect 8888 &
# Connection received on localhost <some random port here>
```

lastly, foreground the netcat listener & transmit bandit20's password

```sh
fg "%nc"
4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA
# Read: 4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA
# Password matches, sending next password
# bW9kBv5WC3P4yoDyf12LSdGuNz5ka6hY
```
