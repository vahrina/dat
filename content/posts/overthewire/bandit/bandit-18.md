---
date: '2026-09-15'
description: not so quiet anymore heh
draft: false
title: bandit-18
weight: 19
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit18`                                   |
| pass | `OQxXZjELndr90zuhOTDYBEomI0SZITXI`         |

> The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

---

## explanation

when trying to log into the user, it seems someone's always logging us out...

```sh
ssh -v bandit18@bandit
# debug1: Next authentication method: password
# bandit18@bandit.labs.overthewire.org's password:
# Authenticated to bandit.labs.overthewire.org ([51.20.162.29]:2220) using "password".
# debug1: channel 0: new [client-session]
# ...
# Byebye !
# debug1: channel 0: free: client-session, nchannels 1
# Connection to bandit.labs.overthewire.org closed.
# Transferred: sent 2360, received 5940 bytes, in 0.1 seconds
# Bytes per second: sent 16081.1, received 40475.2
# debug1: Exit status 0
```

without revealing the trick, the reason being, are the two last lines in `.bashrc`:

```sh
echo 'Byebye !'
exit 0
```

taking a step back, what does ssh accept?

```sh
ssh destination [command [argument ...]]
```

halfway through the [man page](https://man7.org/linux/man-pages/man1/ssh.1.html), there's a section under **AUTHENTICATION**:

```txt
When the user's identity has been accepted by the server, the
server either executes the given command in a non-interactive
session or, if no command has been specified, logs into the
machine and gives the user a normal shell as an interactive
session.
```

append your desired shell commands after `ssh dst [args]`, it'll "execute the given command in a non-interactive session" - as mentioned above


```sh
ssh bandit18@bandit cat readme
KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI
```

if you're curious enough, try to launch vim with ssh to get an interactive shell :)
