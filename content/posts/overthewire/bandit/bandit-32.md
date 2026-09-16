---
date: '2026-09-16'
draft: false
description: STOP SCREAMING AT ME ~ uppercase shell
title: bandit-32
weight: 33
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit32`                                   |
| pass | `pWuj5jBQ6IgV0NXwiH6g1pXRF8S1YvbT`         |


---

## explanation

log in &- what the hell is that?!

```sh
WELCOME TO THE UPPERCASE SHELL
>>
```

not a single command can be executed anymore, so my initial thought was some trickery with [environment variables](https://docs.oracle.com/cd/E19120-01/open.solaris/819-2379/userconcept-26/index.html), as these are the only uppercase relevant strings in linux - this lead me nowhere unfortunately

so i returned to a previous shell to see what's going on

```sh
grep "bandit32" /etc/passwd
# bandit32:x:11032:11032:bandit level 32:/home/bandit32:/home/bandit32/uppershell

stat /home/bandit32/uppershell && file $_
# Access: (4750/-rwsr-x---)  Uid: (11033/bandit33)   Gid: (11032/bandit32)
# ...
# /home/bandit32/uppershell: setuid regular file, no read permission
```

another [`suid`](https://www.redhat.com/en/blog/suid-sgid-sticky-bit) bit & bandit32 is in the relevant group - unfortunately that is about how much usefulness there was to leverage

after some time, i thought of bash variables & scripts - often using something like this

```sh
#!/usr/bin/env bash

# insert interesting piece of functionality here

case expression in
  pattern_1)
    # do something
    ;;
  pattern_2)
    # do something too i suppose
    ;;
  *)
    # default pattern
    echo "usage: ./$0 [pattern_1|pattern_2]"
    ;;
esac
```

> although $0 is a parameter & not an environment variable as i mentioned above - and critically, it's expanded by the shell itself rather than typed by us, so the uppercase only input filter never gets a chance to mangle it

so i figured: hold on a minute, what about `$0`? it's a special parameter that holds the name of the currently running shell/script - basically the program's own invocation name & since we are in a running process of the `upper.c` (`strings` output at the end) binary i supposeeeeee..

```sh
>>
$
```

the prompt changed!

```sh
$ id
# uid=11033(bandit33) gid=11032(bandit32) groups=11032(bandit32)
$ echo $0
# sh
```

now that we are in a **useable** shell, lets yoooooooooooooooooink one last time

```sh
$ echo $SHELL
# /home/bandit32/uppershell

$ cat /etc/bandit_pass/bandit33
# u4P2CyPOwPGLe94RdD9Uo2FxFwvnFswM
```

<details>
  <summary>some functionality of the binary</summary>

stripping off majority of the unnecessary elf boilerplate, the binary concludes about these relevant runtime strings

```sh
strings uppershell
# WELCOME TO THE UPPERCASE SHELL
# fgets
# stdin
# puts
# exit
# fflush
# system
# printf
# toupper
# setreuid
# geteuid
# libc.so.6
# /lib/ld-linux.so.2
# upper.c
```

putting these in a plausible order gives a rough picture of what's happening on each iteration - totally not obvious by the level but hey, curiosity is not harmful! (not always at least :D)

1. [`setreuid`](https://man7.org/linux/man-pages/man2/setreuid.2.html) / [`geteuid`](https://man7.org/linux/man-pages/man2/geteuid.2.html) drops/sets privileges early on which is consistent with the `4750` permissions from the `stat` output
2. [`puts`](https://man7.org/linux/man-pages/man3/puts.3.html) prints the banner ("WELCOME TO THE UPPERCASE SHELL") & the prompt (">>")
3. [`fgets`](https://man7.org/linux/man-pages/man3/fgets.3.html) reads a line of input from [`stdin`](https://man7.org/linux/man-pages/man3/stdin.3.html) into a buffer
4. [`toupper`](https://man7.org/linux/man-pages/man3/toupper.3.html) is run over that buffer - char by char
5. [`printf`](https://man7.org/linux/man-pages/man3/printf.3.html) likely echoes the (now uppercase) input back
6. [`system`](https://man7.org/linux/man-pages/man3/system.3.html) is called with that uppercased buffer as the command string
7. [`fflush`](https://man7.org/linux/man-pages/man3/fflush.3.html) / [`exit`](https://man7.org/linux/man-pages/man3/exit.3.html) handles cleanup

i assume the interesting bit happens between step 4 to 6, as `toupper` only touches the raw bytes we typed on `stdin` - so it never reaches into a string that the shell itself constructs **after** the input is handed to `system`

tl;dr typing `$0` spawns a shell as `system()` expands the parameter

> more on [parameter expansion here](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)

</details>

```
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠛⠛⠛⠿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣠⣴⣿⡟⠁⢀⣤⣀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣦⠀⠀⠀⠀
                            ⠀⠀⠀⠀⣾⡿⠿⠛⠁⣰⣿⣿⣿⡆⠀⠀⣴⣶⣶⠄⠀⢻⣿⡄⠀⠀⠀
                            ⠀⠀⣾⡿⠁⠀⠀⠀⠀⠻⣿⣿⣿⠃⠀⣼⣿⣿⣿⠀⠀⠀⢿⣷⣄⠀⠀
                            ⠀⣾⣿⠁⠀⣤⣶⡄⠀⠀⠈⠉⠁⠀⠀⠈⠛⠊⠁⠀⠀⠀⠀⠙⢿⣷⠀
                            ⠀⣿⡇⠀⢸⣿⣿⡿⡆⠀⠀⣴⣶⣶⣴⣶⣄⠀⠀⢠⣶⣿⣦⠀⠀⣿⡇
                            ⠀⣿⡇⠀⠀⠛⠙⠉⠀⣰⣿⣿⣿⣿⣿⣿⣿⣇⠀⣿⣿⣿⣿⠀⠀⣿⡇
                            ⠀⣿⣇⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣷⣿⣷⡀⠀⠉⠉⠀⠀⣸⣿⠇
                            ⠀⣿⣿⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣻⡟⠘
                            ⠀⢹⣿⠀⠀⠀⠀⠀⠉⠛⠉⠁⠉⠁⠙⠻⠿⠟⠀⠀⠀⠀⠀⣾⣿⠁⠀
                            ⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀
                            ⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
                            ⠀⠀⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
                            ⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
```
