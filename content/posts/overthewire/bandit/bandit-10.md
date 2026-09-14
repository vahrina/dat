---
date: '2026-09-14'
description: encoding is fun (sometimes)
draft: false
title: bandit-10
weight: 11
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit`                                   |
| pass | `B0s2khmbT9u0geKuOoVGW3JZKhndE3BG`                                   |

> The password for the next level is stored in the file data.txt, which contains base64 encoded data

---

## explanation

[base64](https://man7.org/linux/man-pages/man1/base64.1.html) & some other encoding algorithms come preinstalled on major distros, e.g. [base32](https://man7.org/linux/man-pages/man1/base32.1.html), [xxd](https://linux.die.net/man/1/xxd)/[hexdump](https://man7.org/linux/man-pages/man1/hexdump.1.html)/[od](https://man7.org/linux/man-pages/man1/od.1.html)

```sh
base64 -d data.txt
# The password is pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro
```

besides encoding algorithms (reversible), you may also be familiar with [hashing](https://www.geeksforgeeks.org/dsa/introduction-to-hashing-2/), which is a one way transformation that maps any size input to a fixed size output (digest), which cannot be reversed. while the both take input data & transform output using a deterministic algorithm, it should not be mistaken for equality
