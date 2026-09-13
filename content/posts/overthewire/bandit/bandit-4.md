---
date: '2026-09-13'
description: "*arg*uing with commands is beneficial"
draft: false
title: bandit-4
weight: 5
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit4`                                   |
| pass | `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq`                                   |

> The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

---

## explanation

a human readable file is indicated by ascii text, which conveniently enough the `file` command handles

`find -exec` allows a specified command to run on each file found by `find` - the syntax is `find [path] [flags] -exec [cmd] {} \;`

<details>
  <summary>as per man page</summary>

```txt
  -exec command ;
  Execute command; true if 0 status is returned.  All
  following arguments to find are taken to be arguments to
  the command until an argument consisting of `;' is
  encountered.  The string `{}' is replaced by the current
  file name being processed everywhere it occurs in the
  arguments to the command, not just in arguments where it is
  alone, as in some versions of find.  Both of these
  constructions might need to be escaped (with a `\') or
  quoted to protect them from expansion by the shell.  See
  the EXAMPLES section for examples of the use of the -exec
  option.  The specified command is run once for each matched
  file.  The command is executed in the starting directory.
  There are unavoidable security problems surrounding use of
  the -exec action; you should use the -execdir option
  instead.

-exec command {} +
  This variant of the -exec action runs the specified command
  on the selected files, but the command line is built by
  appending each selected file name at the end; the total
  number of invocations of the command will be much less than
  the number of matched files.  The command line is built in
  much the same way that xargs builds its command lines.
  Only one instance of `{}' is allowed within the command,
  and it must appear at the end, immediately before the `+';
  it needs to be escaped (with a `\') or quoted to protect it
  from interpretation by the shell.  The command is executed
  in the starting directory.  If any invocation with the `+'
  form returns a non-zero value as exit status, then find
  returns a non-zero exit status.  If find encounters an
  error, this can sometimes cause an immediate exit, so some
  pending commands may not be run at all.  For this reason
  -exec my-command ... {} + -quit may not result in my-
  command actually being run.  This variant of -exec always
  returns true.
```

- [source](https://www.man7.org/linux/man-pages/man1/find.1.html), or your builtin manpage dummy
- see [this post](https://stackoverflow.com/questions/6085156/using-semicolon-vs-plus-with-exec-in-find) for a simplified version
</details>

combining the two yields

```sh
find inhere/ -type f -exec file {} \;
inhere/-file06: OpenPGP Public Key
inhere/-file09: Motorola S-Record; binary data in text format
inhere/-file01: data
inhere/-file08: data
inhere/-file00: data
inhere/-file03: data
inhere/-file07: ASCII text
inhere/-file02: data
inhere/-file05: data
inhere/-file04: data
```

makes it quite obvious that `-file07` holds the flag

```sh
cat inhere/-file07
6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG
```
