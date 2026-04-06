---
title: 'dmon'
date: '2026-04-05'
draft: false
description: 'in loving memory, myrient! how i made my own tiny fork'
---

### in case you live under a rock

in dear remembarance, [myrient](https://myrient.erista.me/) has officially shut down on April 1st 2026, but you may ask: what is myrient? it shut down, so.. what about it?

![ ](/img/malcolm-in-the-middle-lights-dim.gif#center)

as alexey described himself, he single-handley hosted ~390tb, and why is this a problem? shouldn't be a problem if you can use a search engine, or ask the wizards that sit in the chatgpt box on how to obtain rom x for emulator y in the language z, feel free to explore the [web archive](https://web.archive.org/web/20260331021035/https://myrient.erista.me/) yourself if you're not convinced of the maddening size & availability

> tl;dr a glimpse of what myrient provided
> - nintendo (nes-wii u)
> - sony (ps1-ps3)
> - sega
> - ^ about every rev (update/patch), region (eu, us, jp, kr, au, hk, tw)
> - insiders, leaks, 4chan crap yadayada you name it

![ ](/img/announcement.jpeg#center)

---

### the plan

weirdly enough, just a week or two before the announcement above, i began downloading a bunch of stuff, due to some weird instinct, no clue honestly. and when the announcement released, everyones download was capped to at best 50 kib for a week straight :D

30 days until the end of the most actively, reliably maintained go-to source of retro related content. to preserve a local copy, i formatted my useless ubuntu drive to store the data & added a [symlink](https://en.wikipedia.org/wiki/Symbolic_link) - git does **not** handle symlinks, hence it will not be present in the repo!

here's the approach:

- [nginx](https://nginx.org/) backend server listing
- static front end
- keep the looks (went wrong, performance 📉)
- api for whatever reason, fun to have
- subdomain name matching my 3 letter dns vah.wtf

in the meantime of learning nginx & procrastinating on the styles, i let `wget` with the necessary files/dirs i would like to preserve in the background

the nginx configuration was fairly simple, as i didn't touch anything inside `/etc/nginx/nginx.conf` and mainly replaced `/etc/nginx/sites-enabled/default` with `/etc/nginx/sites-available/emu.vah.wtf`

```sh
$ ls -l /etc/nginx/sites-enabled/emu.vah.wtf
lrwxrwxrwx 1 root nginx-dev 38 Mar 16 16:00 /etc/nginx/sites-enabled/emu.vah.wtf -> /etc/nginx/sites-available/emu.vah.wtf

$ cat /etc/nginx/sites-enabled/emu.vah.wtf                                [±master ●●●]

server {
    listen 80;
    server_name emu.vah.wtf;

    add_header Permissions-Policy "geolocation=(), microphone=(), camera=(), fullscreen=(self), interest-cohort=()" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;

    root /var/www/html;
    index index.html;

    # error pages
    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;

    location = /404.html {
        root /var/www/html/errors;
        internal;
    }

    location = /50x.html {
        root /var/www/html/errors;
        internal;
    }

    # json dir api listing
    location /api/list/ {
        alias /var/www/html/data/;
        autoindex on;
        autoindex_format json;
        autoindex_exact_size off;
        autoindex_localtime on;
        index .none;
    }

    location / {
        try_files $uri $uri/ =404;
        ssi on;
    }

    location ~* ^/assets/ {
        add_header Cache-Control "no-cache, must-revalidate";
    }
}
```

a [cloudflare tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) then resolved my local ip to a cloudflare ip with a [reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/) to safely host it with a ssl/tls connection

you're more than welcome to visit the [site](https://emu.vah.wtf/) ([source](https://github.com/vahrina/dmon))

---

### 502/1033 tunnel error?

since the data still lives on my computer & not a pi or some sort of external server, downloads are unfortunately not possible without my approval first. don't get me wrong, i will gladly turn the server on whenever i can

i didn't really think of why to create this article, i was just fairly proud of the process :>
