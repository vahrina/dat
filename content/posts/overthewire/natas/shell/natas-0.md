---
date: '2026-02-14'
description: front end secrecy is fiction
draft: false
title: natas-0
weight: 1
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `natas0`                                   |
| pass | `natas0`                                   |
| host | `http://natas0.natas.labs.overthewire.org` |

---

## explanation

because the server demands authentication (obtainable from [here](https://overthewire.org/wargames/natas/natas0.html)), pass the `-u`/`--user` argument to specify `<user:password>`, otherwise we will bump into a [401](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/401)

```sh
curl http://natas0.natas.labs.overthewire.org \
-u natas0:natas0
```

the output displays the current [dom structure](https://web.dev/learn/html/document-structure), hence we can immediately spot the password
inside the html comment

```html
<!--The password for natas1 is 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq -->
```
