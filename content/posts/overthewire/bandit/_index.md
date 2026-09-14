---
date: '2026-02-14'
description: what the sHell?!
draft: false
title: bandit/
---

used to hate the shell & avoided whenever i can, but forcing myself to use i/o only - instead of relying on mouse clicks - made it sooo much more fun

every [bandit level](https://overthewire.org/wargames/bandit/) concludes of a hint, helpful commands & reading material. although i'll include it, all credit goes to [otw](https://overthewire.org/)

i'll mostly comment out the stuff that came back from the server's side - so it's easier to distinguish between in- & output

---

### helpful stuff before beginning

because the host:port stays the same, i encourage you to save it to your [ssh config](https://linux.die.net/man/5/ssh_config). unlike the [natas](https://dat.vah.wtf/posts/overthewire/natas/shell/) levels, i will not provide the host in every table

```sh
Host bandit
    HostName bandit.labs.overthewire.org
    Port 2220
```

this makes connecting more convenient

```sh
ssh bandit<id>@bandit.labs.overthewire.org -p 2220 # without config
ssh bandit<id>@bandit # with config
```

obviously the user changes every subsequent level - to maximize efficiency you could additionally do either or:

- learn [bash shortcuts](https://kapeli.com/cheat_sheets/Bash_Shortcuts.docset/Contents/Resources/Documents/index)
- peep my [zsh inline edit](https://github.com/vahrina/.dot/blob/x86-64-wsl/home/.config/zsh/keybind.zsh#L2-L4) with whatever your preferred editor is set to (`ctrl-x e` on a [buffered input](https://how-terminals-work.vercel.app/#input-modes), section 06)
- stick to arrow key navigation/delete char by char, sicko..
