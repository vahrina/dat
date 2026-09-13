---
date: '2026-09-13'
description: to grep or not grep, that is the question
draft: false
title: bandit-7
weight: 8
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit7`                                   |
| pass | `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`                                   |

> The password for the next level is stored in the file data.txt next to the word millionth

---

## explanation

grep (better: [ripgrep](https://crates.io/crates/ripgrep)) can be utilized to ["print lines that match patterns"](https://man7.org/linux/man-pages/man1/grep.1.html)

as per usual - like many other commands - grep reads from stdin with the syntax `grep [pattern] [path]`

```sh
grep "millionth" data.txt
# millionth       VR1ljMayciFxbnUokuQmJFw6QC9VKtub
```

> honorable mention: a historical analysis by [lauriewired](https://www.youtube.com/watch?v=iQZ81MbjKpU)
