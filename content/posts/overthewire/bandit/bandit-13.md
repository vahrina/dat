---
date: '2026-09-14'
description: ssh, or, how i like to call it, 🤫
draft: false
title: bandit-13
weight: 14
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit13`                                   |
| pass | `qQYQiHOBPR8zR61qxYqX45quvihF2uzk`                                   |

> The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level. \
> If you need help with this level: a hint file can be found in the home directory. \
> Make sure to read the error messages as they are informative.

---

> creds to the description by [kai lentit](https://youtu.be/9n1dtmzqnCU?t=30)

## explanation

as mentioned in the description, bandit13 is only a placeholder since we will use the private key to log into bandit14

```sh
-rw-r-----   1 bandit14 bandit13  467 Jun 24 14:59 HINT
-rw-r-----   1 bandit14 bandit13 2602 Jun 24 14:59 sshkey.private
```

log out & copy the key over with your favorite ssh based file transfer tool

```sh
rsync -avh --progress bandit13@bandit:sshkey.private bandit14
# plain scp is sufficient enough too
```

and because the permissions are still too open (`640`/`-rw-r-----`), this key needs adjusting before ssh will use it

<details>
  <summary>ssh warning</summary>

```sh
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0640 for 'bandit14' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "bandit14": bad permissions
```

</details>

```sh
chmod 0600 bandit14 # or chmod go-rwx
# supply the file to ssh with the -i flag
ssh -i bandit14 bandit14@bandit
```

in the real world, this key would be [compromised](https://www.quora.com/What-happens-if-my-SSH-private-key-is-compromised) & needs to be rotated asap
