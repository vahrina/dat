---
date: '2026-09-16'
draft: false
description: less is more
title: bandit-25
weight: 26
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit25`                                   |
| pass | `SoHfqMOEqIX2IYKVciZxvgpR9a2Djx4P`         |

> Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

> **NOTE:** if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.

---

> creds to the description by [kai lentit](https://youtu.be/9n1dtmzqnCU?t=139)

## explanation

greeted with a private key upon logging in

```sh
rsync -avh --progress bandit25@bandit:bandit26.sshkey bandit26
# yooooooooooooooink
```

it always throws you right back out when using the key to log in

```sh
Enjoy your stay!
  _                     _ _ _   ___   __
  | |                   | (_) | |__ \ / /
  | |__   __ _ _ __   __| |_| |_   ) / /_
  | '_ \ / _` | '_ \ / _` | | __| / / '_ \
  | |_) | (_| | | | | (_| | | |_ / /| (_) |
  |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
Connection to bandit.labs.overthewire.org closed.
```

appending a command to ssh doesn't really work either, it just hangs

<details>
 <summary>see some of the useful debug log</summary>

```sh
ssh -vi bandit26 bandit26@bandit vi
# ...
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Offering public key: bandit26 RSA
  SHA256:WTr5/2jG+sBn33VnPPcUJ/C6+Ftef7zFIn5sSTUm0Xc explicit agent
debug1: Server accepts key: bandit26 RSA
  SHA256:WTr5/2jG+sBn33VnPPcUJ/C6+Ftef7zFIn5sSTUm0Xc explicit agent
Authenticated to bandit.labs.overthewire.org
  ([51.20.162.29]:2220) using "publickey".
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: filesystem
debug1: client_input_global_request: rtype
  hostkeys-00@openssh.com want_reply 0
# ...
debug1: Sending environment.
debug1: channel 0: setting env LANG = "C.UTF-8"
debug1: Sending command: vi
```

</details>

a [heredoc](https://linuxize.com/post/bash-heredoc/) (multiline) reveals a little more insight, but not really the full picture

```sh
ssh -T -i bandit26 bandit26@bandit <<eof
  id
eof
#
#                          _                     _ _ _
#                         | |__   __ _ _ __   __| (_) |_
#                         | '_ \ / _` | '_ \ / _` | | __|
#                         | |_) | (_| | | | | (_| | | |_
#                         |_.__/ \__,_|_| |_|\__,_|_|\__|
#
#
#                       This is an OverTheWire game server.
#             More information on http://www.overthewire.org/wargames
#
# backend: gibson-0
# id
# ::::::::::::::
# /home/bandit26/text.txt
# ::::::::::::::
#   _                     _ _ _   ___   __
#  | |                   | (_) | |__ \ / /
#  | |__   __ _ _ __   __| |_| |_   ) / /_
#  | '_ \ / _` | '_ \ / _` | | __| / / '_ \
#  | |_) | (_| | | | | (_| | | |_ / /| (_) |
#  |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
```

so.. it is opening a connection & accepting the key.. what is the issue then?

let us reconsider the hint we received first, "what shell does user bandit26 use?" log back into bandit25 and check

```sh
grep "bandit26" /etc/passwd
# bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
```

that is not right..? `/usr/bin/showtext` is literally just the ascii art in the details dropdown above

---

### a little retroperspective

welllll it is a bit more sophisticated than that & you will probably quit out furiously if you've been stuck on this for a while - i get it

ever encountered when [`less`](https://man7.org/linux/man-pages/man1/less.1.html) (or whatever [pager](https://www.both.org/?p=4701) you have) turns your buffered tty into raw mode? (more on cooked vs raw mode [here](https://how-terminals-work.vercel.app/#input-modes), section 06) that is.. mostly it.. let me explain

a screen, that is too little to render the full output all at once, (contrary to [`cat`](https://man7.org/linux/man-pages/man1/cat.1.html), which prints everything to stdout no matter how much your terminal can visually display at once), will utilize a [pager](https://www.both.org/?p=4701) to let you navigate it at your own pace

if you believe you have NEVER used a pager (nor ever dared to open the man pages, wtf are you doing..?!) `man <literally any shell builtin>` & voila!

---

### back to the topic

zoom into your current shell so much until [`less`](https://man7.org/linux/man-pages/man1/less.1.html) opens & interrupts kicking you out of the session, you should see a bunch of dashes, underscores; pipelines etc. pp. & at the very bottom
`--More--(83%)`

now to do anything, basic motions of less are:
- `j`/`k` to navigate
- `ctrl-d`/`ctrl-u` to jump **d**own/**u**p half a page
- `q` to quit
- `v` to go into **v**isual mode
- `/`/`?` to forward/backward search (`n`/`N` for **n**ext/previous match)

with that concluded, hit `v` & it should send you into the **v**isual editor, in this case [`vi`](https://man7.org/linux/man-pages/man1/vi.1p.html), your favorite editor

inside `vi`, we can bring up vim's built-in commands by hitting `:` which leads to the next step, changing the shell: `:set shell=/bin/bash` & now you're able to execute ACTUAL commands via `:!`, f.e. `:!echo hi`

```sh
:!cat /etc/bandit_pass/bandit26
# jHdv2ELQhT22BkprMNDjybZDAkw1zeBJ
```

not that the password is any beneficial (it wont fix the wrong shell, surprise surprise :D), move onto [bandit-27](https://dat.vah.wtf/posts/overthewire/bandit/bandit-27/) since this seems to be done for the level - i would've included the rest for completion in here but oh well
