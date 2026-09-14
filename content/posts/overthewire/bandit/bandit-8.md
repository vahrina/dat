---
date: '2026-09-14'
description: uniqueness matters in this day & age
draft: false
title: bandit-8
weight: 9
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit8`                                   |
| pass | `EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl`                                   |

> The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

---

## explanation

for this task you want to dig into [sort](https://man7.org/linux/man-pages/man1/sort.1.html) & [uniq](https://man7.org/linux/man-pages/man1/uniq.1.html), as given by the task to find a **unique** string

`sort [file]` sorts alphabetically with no args & in combination with `uniq -u` report or omit repeated lines

```sh
sort data.txt | uniq -u
# EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl
```
