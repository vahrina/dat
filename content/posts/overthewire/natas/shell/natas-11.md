---
date: '2026-04-12'
description: average php security
draft: false
title: natas-11
weight: 12
ShowToc: false
---

| info | value                                       |
|:-----|--------------------------------------------:|
| user | `natas11`                                   |
| pass | `VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd`          |
| host | `http://natas11.natas.labs.overthewire.org` |

![ ](https://media1.tenor.com/m/W89JGWHhX6wAAAAd/php.gif#center)

## explanation

the source for this may be a bit overwhelming at first but let's go through it bit by bit

```php
$defaultdata = array("showpassword" => "no", "bgcolor" => "#ffffff");

function xor_encrypt($in) {
  $key = '<censored>';
  $text = $in;
  $outText = '';

  for ($i = 0; $i < strlen($text); $i++) {
  $outText .= $text[$i] ^ $key[$i % strlen($key)];
  }

  return $outText;
}

function loadData($def) {
  global $_COOKIE;
  $mydata = $def;

  if (array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);

    if (is_array($tempdata) &&
    array_key_exists("showpassword", $tempdata) &&
    array_key_exists("bgcolor", $tempdata)) {

      if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
      }
    }
  }
  return $mydata;
}

function saveData($d) {
  setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if (array_key_exists("bgcolor", $_REQUEST)) {
  if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
      $data['bgcolor'] = $_REQUEST['bgcolor'];
  }
}

saveData($data);

if ($data["showpassword"] == "yes") {
    print "pass: <censored>";
}
```

now for the execution order:

1. initialize `$defaultdata` & declare following functions
  - `xor_encrypt()`
  - `loadData()`
  - `saveData()`
2. load state `$data = loadData($defaultdata);`: \
  if `$_COOKIE` with the `data` field exists, run: `json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);` \
  rest is validation logic to input valid hex colors, if valid: overwrite defaults
3. persist state `saveData($data);`: which is the reverse logic to encode the data

strip down the code to only the necessary parts, rewrite for some clarity (personally rewriting variables makes me comprehend what i am seeing) & comment what's going on

```php
$defaultdata = array("showpassword" => "no", "bgcolor" => "#ffffff");

function xor_encrypt($input) {
  $key = '<censored>'; # currently unknown
  $output = '';

  for ($i = 0; $i < strlen($input); $i++) {
    $output .= $input[$i] ^ $key[$i % strlen($key)];
    # append to output: every char in $input xor every char in $key mod len($key)
    # ^ reads like a math equation from left to right
  }
  return $output;
}

function loadData(...) {
  # vars
  if (array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
  }
  # validation logic
}

if ($data["showpassword"] == "yes") {
    print "pass";
}
```

since 2 out of the 3 components are required to generate (as well as reconstruct) xor output, we can rearrange the equation in the same manner of applying the [commutative law](https://www.mathsisfun.com/associative-commutative-distributive.html)

> [101 refresher](#xor-101), if you're unfamiliar with reversing xor

now that we know there's a bunch of encodings with our cookie, let's actually retrieve the cookie & see what happens after changing the `bgcolor` value. an explanation about the cookie fields can be found [down below](#curl-cookie-fields-interpretation)

```sh
curl http://natas11.natas.labs.overthewire.org \
-u natas11:VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd \
--data-urlencode "bgcolor=#ffffff" \ # <-- change this value
-c -                                 # <-- cookie will differ

# natas11.natas.labs.overthewire.org      FALSE  /FALSE   0       data
# EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D

```

> while the `-d` flag works here, `--data-urlencode` is preferred, as it auto encodes reserved characters like `#`; `-d` requires manual encoding, f.e. `bgcolor=%23cccccc`

now to get a glimpse of what `k` could be, we first need to obtain the other two components, the **c**ipher `c` & message `m`:

```php
# ciphertext c
json_encode(array("showpassword" => "no", "bgcolor" => "#ffffff"));

# {"showpassword":"no","bgcolor":"#ffffff"}
```

> as of September 2026, some levels have been changed, hence this cookie will differ from time to time. in the current change, please **do not** url/b64 decode the retrieved cookie - as this was the way to go before!

```sh
# message m
EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D
```

with this knowledge we should be able to craft a payload with a short trip to hell:

```php
function xor_encrypt() {
  $key = json_encode([
    "showpassword" => "no",
    "bgcolor" => "#ffffff"
  ]);
  $cookie = base64_decode("EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D");
  $out = '';

  for ($i = 0; $i < strlen($cookie); $i++) {
    $out .= $cookie[$i] ^ $key[$i % strlen($key)];
  }

  print $out;
}

xor_encrypt();
```

and voila, the first 4 bits of `kBSwkBSwkBSwkBSwkBSwkBSwkBZ{G��vF��"R��)#�` are repeating: `kBSw` - now `k` can be used to forge a cookie where `showpassword => yes`

```php
function xor_encrypt($in) {
  $key = 'kBSw';
  $out = '';

  for ($i = 0; $i < strlen($in); $i++) {
  $out .= $in[$i] ^ $key[$i % strlen($key)];
  }

  return $out;
}

print base64_encode(
  xor_encrypt(
    json_encode(
      ["showpassword" => "yes", "bgcolor" => "#ffffff"]
    )
  )
);

# EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
```

lastly, send the forged cookie to the server

```sh
curl http://natas11.natas.labs.overthewire.org \
-u natas11:VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd \
-b "data=EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/"
```
leverage the password & move on asap for your own well being (¬_¬")

```txt
The password for natas12 is EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng
```

---

### xor 101

firstly, xor is like an upgraded logical "or" operation, where if both bits differ, it becomes 1, else 0

| a | b | a ^ b |
|---|---|:-----:|
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

picture a message `m = 0110 1001 (105)` with chosen key `k = 10 (2)`

remember that `k` wraps around `m` until they are the same length, hence the modulo `%` operator in the function prior. otherwise, not every single character of `m` would get encrypted, hence `k` must repeat itself

> note that binary doesn't include spaces, but for clarity i will split mid byte (also called a [nibble](https://en.wikipedia.org/wiki/Nibble))

```m
0110 1001 = m (105)
1010 1010 = k (170)
- - - - -
1100 0011 = c (195)
```

<details>
  <summary>what happens without modulo?</summary>

if `k` would **not** repeat itself, the key will only apply to a fraction of the output. in this case we apply the modulo `%` operator to cover all bits of `m`

```m
0110 1001 = m (105)
0000 0010 = k (010)
- - - - -
0110 1011 = c (107)
```

</details>

to prove we can we reverse xor by knowing 2/3 parts, and because xor consists of mere addition, applying the [commutative law](https://www.mathsisfun.com/associative-commutative-distributive.html) yields the same output

```m
0110 1001 = m (105)
1100 0011 = c (195)
- - - - -
1010 1010 = k (170)
```

---

### curl cookie fields interpretation

source: [curl.se](https://curl.se/docs/http-cookies.html)

| field      | value | meaning                     |
|------------|:-----:|----------------------------:|
| domain     | otw   | cookie scope                |
| sub        | FALSE | include subdomains          |
| path       | /     | valid url path              |
| secure     | FALSE | https only                  |
| expiry     | 0     | cookie persistance          |
| name       | data  | cookie identifier           |
| value      | ..%3D | cookie value                |
