---
date: '2026-10-14'
draft: false
description: my math isn't mathing aaaaaaaaaaaah
title: krypton/
ShowToc: false
---

although math isn't my strongest, favorite subject, i'm trying my best!! crypto luckily is much more interesting than trying to factually prove why `420/69 = 6,0869565217` & not `69,420`

at the beginning of each level, i will leave the necessary readme/hints from [otw/krypton](https://overthewire.org/wargames/krypton/) respectively (already talking like a mathematician aren't i huehueehu), as per usual

every level consists of a file to decipher, sometimes a binary/hint & a readme in `/krypton/krypton<id>/`

> bonus points for doing it on paper!

---

## make your life easier, please!

typing out the same hostname over and over is tiring, add this to your [ssh config](https://www.man7.org/linux/man-pages/man5/ssh_config.5.html) (`~/.ssh/config`)

```sh
Host krypton
    HostName krypton.labs.overthewire.org
    Port 2231
```

enabling you the superpower of only replacing `?` to the respective id, e.g. krypton1, krypton2, etc.:

```sh
ssh krypton?@krypton
# instead of
ssh krypton?@krypton.labs.overthewire.org -p 2231
```

you may also get all necessary files with your favorite ssh transfer tool

```sh
rsync -avh --progress krypton?@krypton:/krypton/krypton?
```
