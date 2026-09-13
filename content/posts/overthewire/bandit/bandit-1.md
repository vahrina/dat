---
date: '2026-09-13'
description: stdin? no thanks
draft: false
title: bandit-1
weight: 2
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit1`                                   |
| pass | `6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR`                                   |

> The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

---

## explanation

because commands like cat, vim, less etc. interpret a leading `-` as a flag for [stdin](https://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr), you must specify the full path, e.g. `./` in the current dir or `/home/bandit1/-`

```sh
cat ./-
PK8fYLZg2hnHSz83plBL1iEPKdD3QToB
```
