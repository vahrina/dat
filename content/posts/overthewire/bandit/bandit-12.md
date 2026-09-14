---
date: '2026-09-14'
description: lossless data compression, my favorite
draft: false
title: bandit-12
weight: 13
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit12`                                   |
| pass | `GROozWPO8QyN0mGrjUkID0WCYkZiQxrN`         |

> The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

---

## explanation

greeted with a block of cheese, there's valuable information to extract - such as the [magic byte](https://medium.com/@d.harish008/what-is-a-magic-byte-and-how-to-exploit-1e286da1c198)

about every file needs some identification about what type of file & format it is, how else would a `.jpeg` know it is a `.jpeg`? that's exactly what the first couple hex numbers in this dump below represent!

```sh
00000000: 1f8b 0808 b2f0 3b6a 0203 6461 7461 322e  ......;j..data2.
00000010: 6269 6e00 0142 02bd fd42 5a68 3931 4159  bin..B...BZh91AY
00000020: 2653 59dc 0966 8300 001a ffff dff5 c5fe  &SY..f..........
# ... and so on
```

thats also what your kernel needs to boot from a disk: in the case of linux, the bios looks for the magic byte `0xAA55` at the last two bytes of the [mbr](https://en.linuxportal.info/encyclopedia/m/mbr-master-boot-record) (on little endian systems)
> [source](https://stackoverflow.com/questions/1125025/what-is-the-role-of-magic-number-in-boot-loading-in-linux)
another analogy would be the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)#Magic_number) for shell scripting at the start of every bash script - encoding the ascii value of `#!` to `0x23 0x21`

---

going back en route, this task is primarily about decompressing the file in various formats - so let's look into the [list of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures) to find out about every compression necessary to reconstruct the original product

the first part is a [gzip signature](https://en.wikipedia.org/wiki/List_of_file_signatures#mwB4s) in plain ascii text, indicated by the magic byte `1f 8b` - so we have to reconstruct it first into its original format

```sh
xxd -r data.txt > secret.gz
```

> logically with the original extension too \
> attempting to extract a non gzip file returns an error, hence the rename to `.gz` \
> "gzip: stdin: not in gzip format"

and finally extracting it (gzip -> compress; gunzip -> decompress - awesome naming convention, right?)

```sh
gunzip secret.gz && file secret
secret: bzip2 compressed data, block size = 900k
```

great, now to repeat this a couple times more:

```sh
# 1. find magic byte
xxd secret | head -1
#         vvvv vv
00000000: 425a 6839 3141 5926 5359 dc09 6683 0000
#         ^^^^ ^^

# 2. rename
mv secret secret.bz2

# 3. extract with the right tool
bunzip2 secret.bz2 # or bzip2 -d, same story as gzip <-> gunzip

# 4. what came back?
file secret
secret: gzip compressed data, was "data4.bin", last modified: Wed Jun 24 14:58:58 2026, max compression, from Unix, original size modulo 2^32 20480

# repeated a couple of times
mv secret secret.tar && tar xvf secret.tar # decompress `data5.bin`
mv data5.bin data5.tar && tar xvf data5.tar # decompress `data6.bin`
mv data6.bin data6.tar && tar -xvf data6.tar # decompress `data8.bin`
mv data8.bin data8.gz && gunzip data8.gz
cat data8
# The password is qQYQiHOBPR8zR61qxYqX45quvihF2uzk
```

phew
