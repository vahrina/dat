---
date: '2026-09-14'
description: good ol' grep
draft: false
title: bandit-9
weight: 10
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit9`                                   |
| pass | `EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl`                                   |

> The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

---

## explanation

upon reading the file contents, you'll see a bunch of binary nonsense - as implied by the description lol - therefore the utility `strings` comes in handy to only filter **human readable** ascii text

logically "preceded by several '=' chars" will pipe into grep

```sh
strings data.txt | grep "=="
# cL0========== the
# ========== password
# >========== is
# R========== B0s2khmbT9u0geKuOoVGW3JZKhndE3BG
```
