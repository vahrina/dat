---
date: '2026-04-12'
description: 
draft: true
title: natas-11
weight: 12
ShowToc: false
---

| info | value                                       |
|:-----|--------------------------------------------:|
| user | `natas11`                                   |
| pass | `UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk`          |
| host | `http://natas11.natas.labs.overthewire.org` |

## explanation

the source for this may be a bit overwhelming at first but let's go through it bit by bit

```php
$defaultdata = array("showpassword" => "no", "bgcolor" => "#ffffff");

function xor_encrypt($in) {
  $key = '<censored>';
  $text = $in;
  $outText = '';

  for ($i = 0; $i <strlen($text); $i++) {
  $outText .= $text[$i] ^ $key[$i % strlen($key)];
  }

  return $outText;
}

function loadData($def) {
  global $_COOKIE;
  $mydata = $def;

  if (array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);

    if (is_array($tempdata) && array_key_exists("showpassword", $tempdata) &&
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
```
