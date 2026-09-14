---
date: '2026-09-14'
description: are we multilingual now?
draft: false
title: bandit-11
weight: 12
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit11`                                   |
| pass | `pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro`         |

> The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

---

## explanation

the [tr](https://man7.org/linux/man-pages/man1/tr.1.html) utility will come in handy when "translating" a set of characters for another, e.g.

```sh
echo "bash" | tr 'b' 'c'
# cash
```

[sed](https://man7.org/linux/man-pages/man1/sed.1.html) might ring a bell, as they are both text processing stream tools

nevertheless, with `tr` we can substitute/translate each character, basically foreshadowing the introduction of [rot ciphers](https://www.dcode.fr/rot-cipher)

```sh
tr 'a-zA-Z' 'n-za-mN-ZA-M' < data.txt
# The password is GROozWPO8QyN0mGrjUkID0WCYkZiQxrN
```

looking at the alphabet:
```sh
# abcdefghijklmnopqrstuvwxyz
# vvvvvvvvvvvvvvvvvvvvvvvvvv
# nopqrstuvwxyzabcdefghijklm
```

the reason we had to specify `n-z` instead of `n-m` is because `tr` would throw an error - "the range endpoints are in reverse collating sequence order" - meaning it would go from `n` to `m`. therefore, `n` is the new `a` & `a` is the new `z`
