---
date: '2026-09-14'
description: my dumbass did level 16 mistakingly, wondering why level 15 is not working
draft: false
title: bandit-16
weight: 17
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit16`                                   |
| pass | `kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V`         |


> The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

> **Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**

--- 

## explanation

concluding the port scan between the range of 31000-32000, there is one place of interest in particular:

```sh
nmap -sV -p 31000-32000 localhost
PORT      STATE SERVICE     VERSION
31790/tcp open  ssl/unknown
# ... and many more
```

unlike previous level, whenever entering the password, we are greeted with a key update message, used to update the cryptographic keys for the current connection without performing a full handshake, see [here](https://docs.openssl.org/4.0/man1/openssl-s_client/#connected-commands-basic)

> "When used interactively (which means neither -quiet nor -ign_eof have been given), and neither of -adv or -nocommands are given then "Basic" command mode is entered. In this mode certain commands are recognized which perform special operations. These commands are a letter which must appear at the start of a line. All further data after the initial letter on the line is ignored. The commands are listed below."

because the server keeps issuing a key update, we want to pass the `-nocommands`, `-quiet` or `ign_eof` argument. reason being, the password starts with `k`, which issues the `k` flag from the [**CONNECTED COMMANDS**](https://docs.openssl.org/4.0/man1/openssl-s_client/#connected-commands-basic) section

```sh
openssl s_client -connect localhost:31790 -nocommands
# ---
# read R BLOCK
kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V
# Correct!
# -----BEGIN OPENSSH PRIVATE KEY-----
#      < insert contents here >
# -----END OPENSSH PRIVATE KEY-----
#
# closed
```

another private key successfully compromised :D
