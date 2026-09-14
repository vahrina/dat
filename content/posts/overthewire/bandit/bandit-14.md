---
date: '2026-09-14'
description: net**cat** meow
draft: false
title: bandit-14
weight: 15
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit14`                                   |
| pass | `aaWecNkG4FhxJQxz07uiwzVP6bJiYS65`                                   |

> The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

---

## explanation

recall from the previous level, that passwords are stored under `/etc/bandit_pass/bandit<id>` & that the password for `bandit14` can only be read by `bandit14`?

```sh
#            vvvvvvvv
-r-------- 1 bandit14 bandit14 33 Jun 24 14:58 /etc/bandit_pass/bandit14
#            ^^^^^^^^
```

so we grab the password

```sh
cat /etc/bandit_pass/bandit14
# aaWecNkG4FhxJQxz07uiwzVP6bJiYS65
```

and to submit it on localhost:30000, utilize [netcat](https://linux.die.net/man/1/nc) or [ncat](https://unix.stackexchange.com/questions/368155/what-are-the-differences-between-ncat-nc-and-netcat) ([same idea, but from the Nmap project](https://unix.stackexchange.com/questions/368155/what-are-the-differences-between-ncat-nc-and-netcat#368160))

```sh
# syntax: `ncat [OPTIONS...] [hostname] [port]`
ncat localhost 30000
aaWecNkG4FhxJQxz07uiwzVP6bJiYS65 # bandit14's password
Correct!
pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7
```

think of a hotel (localhost) with a line of doors (ports) you can knock on, but looking specifically at a certain one (localhost:30000), so you knock there & supply the secret to enter

<details>
  <summary>digging into what's listening on port 30000</summary>

a shell script? a binary? tl;dr no clue! D:

although the service is invisible to `ss`, `netstat`, `systemctl`; `/proc/net/tcp` etc. pp. from inside the shell (meaning the listener runs in a separate, isolated namespace), tracing the connection gives some insight to the tcp handshake, followed by the validation upon input

```sh
strace -f -e trace=network nc localhost 30000 <<< "aaWecNkG4FhxJQxz07uiwzVP6bJiYS65"
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 3
connect(3, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (No such file or directory)
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 3
connect(3, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (No such file or directory)
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 3
connect(3, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (No such file or directory)
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 3
connect(3, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (No such file or directory)
socket(AF_INET, SOCK_STREAM|SOCK_NONBLOCK, IPPROTO_TCP) = 3
connect(3, {sa_family=AF_INET, sin_port=htons(30000), sin_addr=inet_addr("127.0.0.1")}, 16) = -1 EINPROGRESS (Operation now in progress)
getsockopt(3, SOL_SOCKET, SO_ERROR, [0], [4]) = 0
shutdown(3, SHUT_RD)                    = 0
Correct!
pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7

+++ exited with 0 +++
```

supplying an incorrect password, e.g. `<<< "test"` yields the opposite result (as expected lol) with the same control flow

```sh
Wrong! Please enter the correct current password.
+++ exited with 0 +++
```

additionally, a sub ~5ms response time strongly suggests that there is a daemon running, so it would rule out a fork/exec-per-connection wrapper - indicated by the following latency probe

```sh
for i in {1..5}; do time (printf 'test\n' | nc localhost 30000); done
Wrong! Please enter the correct current password.

real    0m0.004s
user    0m0.001s
sys     0m0.002s
Wrong! Please enter the correct current password.

real    0m0.004s
user    0m0.003s
sys     0m0.000s
Wrong! Please enter the correct current password.

real    0m0.003s
user    0m0.000s
sys     0m0.003s
Wrong! Please enter the correct current password.

real    0m0.006s
user    0m0.000s
sys     0m0.003s
Wrong! Please enter the correct current password.

real    0m0.009s
user    0m0.000s
sys     0m0.003s
```

</details>
