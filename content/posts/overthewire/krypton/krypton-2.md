---
date: '2026-10-15'
draft: false
title: krypton-2
description: most overused cipher since 100 bc
weight: 3
ShowToc: false
---

> ROT13 is a simple substitution cipher.
>
> Substitution ciphers are a simple replacement algorithm. In this example of a substitution cipher, we will explore a ‘monoalphebetic’ cipher. Monoalphebetic means, literally, “one alphabet” and you will see why.
>
> This level contains an old form of cipher called a ‘Caesar Cipher’. A Caesar cipher shifts the alphabet by a set number. For example:
>
> plain:  a b c d e f g h i j k ... \
> cipher: G H I J K L M N O P Q ...
>
> In this example, the letter ‘a’ in plaintext is replaced by a ‘G’ in the ciphertext so, for example, the plaintext ‘bad’ becomes ‘HGJ’ in ciphertext.
>
> The password for level 3 is in the file krypton3. It is in 5 letter group ciphertext. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a program that will encrypt anything you wish to give it using the key. If you think logically, this is completely easy.
>
> One shot can solve it!
>
> Have fun.
>
> Additional Information:
>
> The encrypt binary will look for the keyfile in your current working directory. Therefore, it might be best to create a working direcory in /tmp and in there a link to the keyfile. As the encrypt binary runs setuid krypton3, you also need to give krypton3 access to your working directory.
> Here is an example:
```sh
krypton2@melinda:~$ mktemp -d
/tmp/tmp.Wf2OnCpCDQ
krypton2@melinda:~$ cd /tmp/tmp.Wf2OnCpCDQ
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ ln -s /krypton/krypton2/keyfile.dat
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ ls
keyfile.dat
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ chmod 777 .
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ /krypton/krypton2/encrypt /etc/issue
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ ls
ciphertext  keyfile.dat
```

---

## explanation

ssh into the server & follow along

```sh
cd $(mktemp -d); ln -s /krypton/krypton2/keyfile.dat; chmod 777 .
```

my first instinct was, since key `k` is inaccessible (making the equation `p = ( c - k) mod 26` impossible), but can freely encrypt anything we want - plus we know it is a [monoalphebetic cipher](https://www.geeksforgeeks.org/computer-networks/what-is-monoalphabetic-cipher/), why not just encrypt the whole alphabet?


```sh
echo "abcdefghijklmnopqrstuvwxyz" > abc
/krypton/krypton2/encrypt abc && diff $_ ciphertext
# 1c1
# < abcdefghijklmnopqrstuvwxyz 0123456789
# ---
# > MNOPQRSTUVWXYZABCDEFGHIJKL
```

this should give a general idea what character encodes to what & using this knowledge, not even the secret is safe anymore:

```txt
OMQEMDUEQMEK
vvvvvvvvvvvv
CAESARISEASY
```
