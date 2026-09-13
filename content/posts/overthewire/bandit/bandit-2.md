---
date: '2026-09-13'
description: bash LOVES quotes
draft: false
title: bandit-2
weight: 3
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit2`                                   |
| pass | `PK8fYLZg2hnHSz83plBL1iEPKdD3QToB`                                   |

> The password for the next level is stored in a file called --spaces in this filename-- located in the home directory

---

## explanation

same story as previous level, there are quite a few ways to do it

```sh
cat "./--spaces in this filename--"
7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME

# just for the sake of it
cat -- --spaces\ in\ this\ filename--
cat ./--spaces\ in\ this\ filename--
cat './--spaces in this filename--'
```
