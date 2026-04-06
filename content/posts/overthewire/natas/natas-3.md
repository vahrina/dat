---
date: '2026-02-15'
description: spiders follow rules, attackers read them
draft: false
title: natas-3
weight: 4
ShowToc: false
---

| info | value |
|:-----|------:|
| user | `natas3` |
| pass | `3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH` |
| host | `http://natas3.natas.labs.overthewire.org` |

### explanation
there isn't anything interesting on this page besides the comment saying

```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```

which hints at your domain having security issues in form of the [robots.txt](https://en.wikipedia.org/wiki/Robots.txt) file which contains general rules for what a [web crawler/robot](https://en.wikipedia.org/wiki/Web_crawler) is allowed to visit

without further ado, check out the `robots.txt` file for anything useful

```sh
curl http://natas3.natas.labs.overthewire.org/robots.txt \
-u natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
```

which returns

```sh
User-agent: *
Disallow: /s3cr3t/
```

may as well check out what `/s3cr3t/` is hiding from us

```sh
curl http://natas3.natas.labs.overthewire.org/s3cr3t/ \
-u natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
```

another directory exposed to leave sensitive data, yet again we discover a `users.txt` file
containing the next login data

```sh
natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
```

