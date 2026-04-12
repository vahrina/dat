---
date: '2026-02-14'
description: web security with a little twist!
draft: false
title: natas/
---

### solutions for [natas](https://overthewire.org/wargames/natas/) levels

to furthermore strengthen my awful frustration tolerance caused by ai, i will try my best to only use cli + [man pages](https://en.wikipedia.org/wiki/Man_page)/[cheatsheet](https://cht.sh)/[explainshell](https://explainshell.com) & whatever other forums online without direct provide helpful info

---

### okay that's cool, but where do we start?

personally, the best approach (& recommended by [otw/natas](https://overthewire.org/wargames/natas/)) for this would be using by utilizing [curl](https://curl.se/)

obviously, there are different tools for any use case really, such as [wget](https://www.gnu.org/software/wget/) or [zap proxy](https://www.zaproxy.org/), but as a personal learning curve i will be primarily using curl

---

### before starting out

- each level of natas consists of its own website located at `http://natasX.natas.labs.overthewire.org`
- no ssh login required, simple webbrowser access is sufficient (which i will try to avoid)
- each level has access to the password of the next level, additionally, all passwords are stored in `/etc/natas_webpass/`

typing out the user/host info every post may seem repetitive & unnecessary at most, but it's good to keep track of what you have, basically like solving a recursion task: break a big problem into sub problems

lastly, i will optionally refactor provided source codes to suit my own clarity
