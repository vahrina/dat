---
date: '2026-09-15'
description: bit for bit
draft: false
title: bandit-19
weight: 20
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit19`                                   |
| pass | `KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI`         |

> To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

---

## explanation

a [setuid bit](https://www.cbtnuggets.com/blog/technology/system-admin/linux-file-permissions-understanding-setuid-setgid-and-the-sticky-bit) (not to confuse with setgid or sticky bit!) can be quite beneficial, f.e. `passwd` uses a setuid to allow users to update the root owned `/etc/shadow` file securely - same speaks for `mount` or `su`. it also carries significant risk, because an ordinary user can execute programs with the file owner's privileges

as the [`stat`](https://man7.org/linux/man-pages/man1/stat.1.html) command tells us valuable information about a file/dir, we can see that the execute bit is replaced with the sticky bit (s), although the uid is set to the bandit20 user

```sh
#                v
Access: (4750/-rwsr-x---)  Uid: (11020/bandit20)   Gid: (11019/bandit19)
#                ^
```

the otw hint reveals to run it without arguments, basically making the process pretty straight forward already

```sh
./bandit20-do
# Run a command as another user.
# Example: ./bandit20-do whoami
```

aaaaaand yoink

```sh
./bandit20-do cat /etc/bandit_pass/bandit20
# 4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA
```
