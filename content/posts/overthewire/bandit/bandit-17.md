---
date: '2026-09-14'
description: "**diff**erent but the same"
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

[diff](https://man7.org/linux/man-pages/man1/diff.1.html) (better: [difftastic](https://crates.io/crates/difftastic)) solves this task wonderful

```sh
diff passwords.old passwords.new --color=always
42c42
< icUh23IUytZLIYhcCaXL18agiSIqymBc
---
> OQxXZjELndr90zuhOTDYBEomI0SZITXI
```

because `passwords.new` (duh) has the new entry `OQxXZjELndr90zuhOTDYBEomI0SZITXI`, that'll be the password for bandit 18. a bit of color (if your term supports it) is always appreciated & much easier on the eyes :D

if you're confused about the output, (f.e. why not `icUh23IUytZLIYhcCaXL18agiSIqymBc`?), read below

<details>
  <summary>a brief explanation of diff</summary>

  as implied by the name, "diff - compare files line by line", will report whether two files are identical to each other and where specifically

  the first line that returns is the type of change & the relevant line numbers, e.g. `42c42` reads as line 42 in file 1 (`passwords.old`) is replaced by line 42 in file 2 (`passwords.new`)

  the rest of the body will include various operators:
  - `a`: lines were **a**dded, e.g. `5a6,7` -> lines 6 & 7 from file 2 are inserted after line 5 in file 1
  - `d`: lines were **d**eleted, e.g. `2d1` -> line 2 in file 1 was deleted
  - `<`: lines present in file 1 (first argument passed to diff)
  - `>`: lines present in file 2 (second argument passed to diff)

---

  an easier, more similar overview (if you're familiar with git diffs) will be noticeable with the unified `-u` flag, which prints a more convenient, easy to read diff with:

  ### file headers

  ```sh
  --- original      <timestamp>
  +++ modified      <timestamp>
  ```

  ### hunk headers

- `@@ -start,count +start, count @@`
- `-`: lines removed from the first file
- `+`: lines added to the second file

  ```sh
  @@ -1,3 +1,4 @@
   Line 1   # (unchanged)
  -Line 2   # (removed)
  +Line 2b  # (added)
  +Line 2c  # (added)
   Line 3   # (unchanged)
  ```

</details>
