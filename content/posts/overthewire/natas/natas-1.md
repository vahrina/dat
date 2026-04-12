---
date: '2026-02-15'
description: cli enthusiasts love this one
draft: false
title: natas-1
weight: 2
ShowToc: false
---

| info | value |
|:-----|------:|
| user | `natas1` |
| pass | `0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq` |
| host | `http://natas1.natas.labs.overthewire.org` |

### explanation

simply change the username, host & password respectively

```sh
curl http://natas1.natas.labs.overthewire.org \
-u natas1:0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq
```

yet again we can directly spot the password by reading the source code of the document, even if
the initial challenge wants you to open the source code via a shortcut as indicated by the hint:

```html
<div id="content">
    You can find the password for the next level on this page, but rightclicking has been blocked!
    ...
</div>
```

we have plenty of ways to open dev tools, just to name a few

| shortcut          | explanation                   |
|:------------------|------------------------------:|
| `<ctrl-shift-i>`  | dev tools (last tab)          |
| `<ctrl-shift-j>`  | console                       |
| `<ctrl-u>`        | view page source              |
| `<f12>`           | dev tools (universal)         |
| `<ctrl-shift-c>`  | dev tools (inspect element)   |

for our matter, just curling it will be more than sufficient to expose the comment from the source doc

```html
<!-- The password for natas2 is TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI -->
```
