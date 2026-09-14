---
date: '2026-09-14'
description:
draft: false
title: bandit-17
weight: 18
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit17`                                   |
| pass | `pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2`         |


> There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

> **NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19**

---

## explanation

[diff](https://man7.org/linux/man-pages/man1/diff.1.html) (better: [difftastic](https://crates.io/crates/difftastic)) solves this taks wonderful

```sh
diff passwords.old passwords.new --color=always
42c42
< icUh23IUytZLIYhcCaXL18agiSIqymBc
---
> OQxXZjELndr90zuhOTDYBEomI0SZITXI
```

<details>
  <summary>a brief explanation of diff</summary>

  as implied by the name, "diff - compare files line by line", will report whether two files are identical to each other and where specifically

  the first line that returns is the type of change & the relevant line numbers, e.g. `42c42` reads as line 42 in file 1 (.old) is replaced by line 42 in file 2 (.new)

  the rest of the body will include various operators:
  - `a`: lines were **a**dded, e.g. `5a6,7` -> lines 6 & 7 from file 2 are inserted after line 5 in file 1
  - `d`: lines were **d**eleted, e.g. `2d1` -> line 2 in file 1 was deleted
  - `<`: lines present in file 1 (first argument passed to diff)
  - `>`: lines present in file 2 (second argument passed to diff)

---

  an easier, more similar overview (if you're familiar with git diffs) will be noticable with the `-u` flag `@@ -start,count +start, count @@` & a visible `-` (lines removed from the first file) & `+` (lines added to the second file) at the very left

</details>
