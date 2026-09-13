---
date: '2026-09-13'
description: im human i swear
draft: false
title: bandit-5
weight: 6
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit5`                                   |
| pass | `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG`                                   |

> The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
> - human-readable
> - 1033 bytes in size
> - not executable

---

## explanation

explore the [find man page](https://www.man7.org/linux/man-pages/man1/find.1.html) to discover what flags are necessary

applying the exec flag to retrieve human readable files will turn out in a ton of files to look through - luckily the file **size** is provided

```sh
find inhere/ -size 1033c -exec file {} \;
inhere/maybehere07/.file2: ASCII text, with very long lines (1000)

cat inhere/maybehere07/.file2
pXa26xhMWaC2SvDotA4r9EgZkulOeSBW
```
