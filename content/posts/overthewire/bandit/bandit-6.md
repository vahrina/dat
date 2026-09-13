---
date: '2026-09-13'
description: im human i swear x2
draft: false
title: bandit-6
weight: 7
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit6`                                   |
| pass | `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW`                                   |

> The password for the next level is stored somewhere on the server and has all of the following properties:
> - owned by user bandit7
> - owned by group bandit6
> - 33 bytes in size

---

## explanation

same principle as before, different flags & the exception we are looking filesystem wide

```sh
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null -exec cat {} \;
# Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3
```

note that `-exec cat {}` prints the content of every file to stdout (which turns out to be 1 anyway `/var/lib/dpkg/info/bandit7.password`)
