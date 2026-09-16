---
date: '2026-09-16'
draft: false
description: i don't recommend anyone to learning vim, i enforce it
title: bandit-26
weight: 27
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit26`                                   |
| pass | `jHdv2ELQhT22BkprMNDjybZDAkw1zeBJ`         |

> Good job getting a shell! Now hurry and grab the password for bandit27!

---

## explanation

using prior knowledge from [bandit-25](https://dat.vah.wtf/posts/overthewire/bandit/bandit-25/) (as the level stops after obtaining the flag in that sense), commence exploring and you eventually come across a binary in the home dir of bandit26

```sh
:!ls
# bandit27-do  text.txt

:!file bandit27-do
# bandit27-do: setuid ELF 32-bit LSB executable, Intel i386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=55720343cddb2e256343bc366b061e1a71764f51, for GNU/Linux 3.2.0, not stripped

:!cat text.txt
 #  _                     _ _ _   ___   __
 # | |                   | (_) | |__ \ / /
 # | |__   __ _ _ __   __| |_| |_   ) / /_
 # | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 # | |_) | (_| | | | | (_| | | |_ / /| (_) |
 # |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
# seems that my theory from earlier was right
```

`bandit27-do` (as the name implies) is an executable binary that we can execute as follows

```sh
:!./bandit27-do
# Run a command as another user.
#   Example: ./bandit27-do id
```

as well as making sure bandit27 executes it (totally not obvious by the `setuid` part of the `file` output)

```sh
:!stat bandit27-do
# ...      vvvvvvvvvvvv                  vvvvvvvvv
# Access: (4750/-rwsr-x---)  Uid: (11027/bandit27)   Gid: (11026/bandit26)
# ...     ^^^^^^^^^^^^^                 ^^^^^^^^^
```

<details>
  <summary>useful information (no bait)</summary>

because we cannot see the source of compiled binaries & we are not a professional reverse engineer yet, we can at least reveal a tad bit with the [`strings`](https://man7.org/linux/man-pages/man1/strings.1.html) command if your system has it (not a shell builtin)

> **always be cautious with foreign software!**

```sh
:!strings bandit27-do
# tdL
# .%cC
# qvOQ/lib/ld-linux.so.2
# _IO_stdin_used
# exit
# __libc_start_main
# execv
# printf
# libc.so.6
# GLIBC_2.0
# GLIBC_2.34
# __gmon_start__
# Run a command as another user.
#   Example: %s id
# /usr/bin/env
# ;*2$"(
# GCC: (Ubuntu 15.2.0-16ubuntu1) 15.2.0
# crt1.o
# __wrap_main
# __abi_tag
# crtstuff.c
# deregister_tm_clones
# __do_global_dtors_aux
# completed.0
# __do_global_dtors_aux_fini_array_entry
# frame_dummy
# __frame_dummy_init_array_entry
# bandit27.c
# __FRAME_END__
# _DYNAMIC
# __GNU_EH_FRAME_HDR
# _GLOBAL_OFFSET_TABLE_
# __libc_start_main@GLIBC_2.34
# __x86.get_pc_thunk.bx
# printf@GLIBC_2.0
# _edata
# _fini
# __data_start
# __gmon_start__
# exit@GLIBC_2.0
# __dso_handle
# _IO_stdin_used
# execv@GLIBC_2.0
# _end
# _dl_relocate_static_pie
# _fp_hw
# __bss_start
# __TMC_END__
# _init
# .symtab
# .strtab
# .shstrtab
# .note.gnu.build-id
# .interp
# .gnu.hash
# .dynsym
# .dynstr
# .gnu.version
# .gnu.version_r
# .rel.dyn
# .rel.plt
# .init
# .text
# .fini
# .rodata
# .eh_frame_hdr
# .eh_frame
# .note.ABI-tag
# .init_array
# .fini_array
# .dynamic
# .got
# .got.plt
# .data
# .bss
# .comment
```

stuff like a shared library reference (e.g. [`libc`](https://man7.org/linux/man-pages/man7/libc.7.html)) can be found near the top, as well as these & many more snippets

```sh
# Run a command as another user.
#   Example: %s id
# /usr/bin/env
# ;*2$"(
# GCC: (Ubuntu 15.2.0-16ubuntu1) 15.2.0
```

- example usage: it reads in a full argument & passes it to [`execv`](https://linux.die.net/man/3/execv), specifically targeting `/usr/bin/env`
- various versioning for fingerprinting/hardening
  - gcc
  - glibc
- imported lib functions after `__libc_start_main@GLIBC_2.34`
  - `execv@GLIBC_2.0`
  - `printf@GLIBC_2.0`
  - `exit@GLIBC_2.0`

the rest is unrelated [elf/abi](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) boilerplate

so it's somewhat safe to assume that the program takes a positional argument & hands it to `execv("/usr/bin/env", [arg, ...])`

</details>

don't mind if i do aaaaaaaaaaaaaaaaaand yyyyyyyyyoink

```sh
:!./bandit27-do cat /etc/bandit_pass/bandit27
# STJLJBRRphMxKB392CT4iOr5CbzPU9ER
```

(btw, after getting into less, you had the chance to zoom out to make it look readable again.. all the way back, but here i am telling you at the very end oops)
