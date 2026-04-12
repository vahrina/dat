---
date: '2026-04-11'
description: encoding != encryption
draft: false
title: natas-8
weight: 9
ShowToc: false
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `natas8`                                   |
| pass | `xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q`         |
| host | `http://natas8.natas.labs.overthewire.org` |

## explanation

on this page we are greeted with a form input, which is commonly used to collect
user data, plus the source code, how nice of them

```html
<form method="post">
  Input secret: <input name="secret"><br>
  <input type="submit" name="submit">
</form>

<div id="viewsource">
  <a href="index-source.html">source</a>
</div>
```

presented with the following php snippet

```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if (array_key_exists("submit", $_POST)) {
    if (encodeSecret($_POST['secret']) == $encodedSecret) {
    print "pass:<censored>";
    } else {
    print "wrong";
    }
}
```

we got:

- an encoded secret that will be encoded
- a function with the encoding process (conveniently enough)
- a conditional that checks whether the key exists and secret equals the hardcoded secret

so our task is to fulfill the conditional in line 8 \
luckily the decoding process is straight forward: \
`from hex > reverse > base64 decode`

since we work with cli only, ta-da:

```sh
printf "3d3d516343746d4d6d6c315669563362" | xxd -r -p | rev | base64 -d
oubWYf2kBq
```

now we only need to submit it into the previously mentioned input form with the name of the input field

```sh
curl http://natas8.natas.labs.overthewire.org \
-u natas8:xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q \
-d "secret=oubWYf2kBq&submit="
```

```html
<div id="content">
Access granted. The password for natas9 is ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
```
