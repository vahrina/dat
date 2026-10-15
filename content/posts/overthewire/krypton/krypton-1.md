---
date: '2026-10-15'
draft: false
title: krypton-1
description: not enough rotations
weight: 2
ShowToc: false
---

> The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!

---

## explanation

from the hint above, this is a rot cipher, also known as [caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) - luckily, this is one of the most commonly used ciphers, as a mere [rot 13 cipher](https://en.wikipedia.org/wiki/ROT13) was utilized

contrary to [bandit 11](https://dat.vah.wtf/posts/overthewire/bandit/bandit-11/), no linux knowledge will be necessary - simply denote it on paper if you will or throw it in an online "rot 13 decoder"

```txt
abcdefghijklmnopqrstuvwxyz
vvvvvvvvvvvvvvvvvvvvvvvvvv
nopqrstuvwxyzabcdefghijklm

YRIRY GJB CNFFJBEQ EBGGRA
vvvvv vvv vvvvvvvv vvvvvv
LEVEL TWO PASSWORD ROTTEN
```
