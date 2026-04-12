---
date: '2026-02-15'
description: the filesystem is gossip lol
draft: false
title: natas-6
weight: 7
ShowToc: false
---

| info | value                                      |
|:-----|--------------------------------------------|
| user | `natas6`                                   |
| pass | `0RoJwHdSKWFTYR5WuiAewauSuNaBXned`         |
| host | `http://natas6.natas.labs.overthewire.org` |

### explanation

we are presented with a `<form>` that we have to submit

```html
<form method=post>
    Input secret: <input name=secret><br>
    <input type=submit name=submit>
</form>
```

plus a helpful source code ressource

```html
<div id="viewsource">
    <a href="index-source.html">View sourcecode</a>
</div>
```

unless you want to fight [sed](https://en.wikipedia.org/wiki/Sed) (good regex practice, i promise!), you may as well simply open the page in your browser

**for the nerds**

```sh
curl http://natas6.natas.labs.overthewire.org/index-source.html \
-u natas6:0RoJwHdSKWFTYR5WuiAewauSuNaBXned \
| sed -nE '                 # -n: print only explicit matches, -E: extended regex
  /<code>/,/<\/code>/{      # operate only inside <code>...</code> block
  s/<\/?span[^>]*>//g       # remove <span> tags
  s/&lt;/</g                # decode into <
  s/&gt;/>/g                # decode into >
  s/&nbsp;/ /g              # replace non breaking spaces with normal spaces
  s/<br ?\/?>/\n/g          # convert <br> tags to real newlines
  /<\?/ , /\?>/p            # print only php block
}'

# compact version below
sed -nE '/<code>/,/<\/code>/{s/<\/?span[^>]*>//g;s/&lt;/</g;s/&gt;/>/g;s/&nbsp;/ /g;s/<br ?\/?>/\n/g;/<\?/,/\?>/p}'
```

or pipe it into [w3m](https://w3m.sourceforge.net/) unless you are a maniac & read the encoded strings line by line

```sh
.. | w3m -T text/html
```

anyways, we can find a folder of interest included in the `php` snippet

```php
include "includes/secret.inc";
```

navigate to it and find the password, then submit the post request with the `-d`/`--data` parameter

```sh
curl http://natas6.natas.labs.overthewire.org/ \
-u natas6:0RoJwHdSKWFTYR5WuiAewauSuNaBXned \
-d "secret=FOEIUWGHFEEUHOFUOIU&submit=submit"
```

after successfully submitting the post request via the two parameters `name=secret`; `submit=submit` we are able to post the request and get the password in return

```html
<div id="content">
    Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
```
