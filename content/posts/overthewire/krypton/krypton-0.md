---
date: '2026-10-14'
draft: false
title: krypton-0
description: base this base that, how about you base some bi-
weight: 1
ShowToc: false
---

> Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:
>
> S1JZUFRPTklTR1JFQVQ=
>
> Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2231. You can find the files for other levels in /krypton/

---

## explanation

should be fairly straightforward:

```sh
echo S1JZUFRPTklTR1JFQVQ= | base64 -d
# KRYPTONISGREAT
```
