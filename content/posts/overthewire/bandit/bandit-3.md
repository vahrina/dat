---
date: '2026-09-13'
description: find nemo
draft: false
title: bandit-3
weight: 4
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit3`                                   |
| pass | `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME`                                   |

> The password for the next level is stored in a hidden file in the inhere directory.

---

## explanation

the `find` (better: [fd-find](https://crates.io/crates/fd-find)) can search the entire filesystem including hidden files

```sh
find inhere/
inhere/
inhere/...Hiding-From-You

cat inhere/./...Hiding-From-You
xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq
```
