---
date: '2026-09-14'
description: port scans all the way
draft: false
title: bandit-15
weight: 16
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit15`                                   |
| pass | `pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7`         |

> The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

> **Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**

---

## explanation

going through the list otw provided us with:

```md
## Commands you may need to solve this level
ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, ss
```

[ssl](https://www.reddit.com/r/ssl/comments/lmj0x5/what_exactly_is_ssl_can_someone_please_explain_in/), specifically [openssl-s_client - SSL/TLS client program](https://docs.openssl.org/4.0/man1/openssl-s_client/) seems to be the clear winner to test ssl connectivity

the docs provide a `[-connect host:port]` argument, so if we put all the pieces together:

```sh
openssl s_client -connect localhost:30001
# Connecting to 127.0.0.1
# CONNECTED(00000003)
#
# ... more data stream ...
#
# ---
# read R BLOCK
pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7 # current password
Correct!
kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V
```
