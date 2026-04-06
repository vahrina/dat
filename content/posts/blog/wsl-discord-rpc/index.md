---
date: '2026-02-26'
description: love-hate relationship with this crap
draft: false
title: wsl discord rpc
---

### recap

over the past few years of visiting university i've always appreciated a friend's discord status, showcasing the most classic vim exit joke ![ ](/img/how_to_exit_vim.png#center)
[unpaid sponsorship](https://lvk.one/)

---

### so.. how did it all start?

been a while on wsl (ubuntu 24.04) with arch on my laptop & it's been bugging my mind to not have a proper (at this point in time, a non-ai driven) editor. i was always open to try new things (np++, mousepad, helix, nano you name it). tl;dr i enjoy vim controls & what it offers for its minimality being installed on majority of distros. recently also picked up on [lazyvim](https://www.lazyvim.org/) after being glued to [primeagen's barebone nvim config](https://www.youtube.com/watch?v=w7i4amO_zaE), hence i thought showing it off in discord, like every arch glazer, would be cool

done some digging and i came across two fantastic articles
- [andweeb/presence.nvim](https://github.com/andweeb/presence.nvim/wiki/Rich-Presence-in-WSL)
  - "WSL 2 is not supported :( ❌" 

- [vyfor/cord.nvim](https://neovimcraft.com/plugin/vyfor/cord.nvim/)

  - "Works with different Discord setups (Snap, Flatpak, [WSL](https://github.com/vyfor/cord.nvim/wiki/Special-Environments#-running-inside-wsl), and even the <s>[browser](https://github.com/vyfor/cord.nvim/wiki/Special-Environments#using-discord-in-a-browser)</s>)."

with a little configuration i was able to get the passthrough to work ![ ](/img/nvim-passthrough.png#center)

---

### first things first, the **prerequisites**

- [socat](http://www.dest-unreach.org/socat/) - multipurpose, bidirectional socket relay
- [npipereleay](https://github.com/jstarks/npiperelay/releases) - bridges windows named pipes to unix domain sockets
- [openssh-server/client](https://www.openssh.org/) - transpots unix socket across namespaces
- a compatible [plugin](https://neovimcraft.com/plugin/vyfor/cord.nvim/) to display it on discord

> below is an automatic install of all dependencies on ubuntu 24.04

```sh
# packages
sudo apt install socat openssh-server openssh-client -y

# npiperelay
cd /tmp
wget https://github.com/jstarks/npiperelay/releases/download/v0.1.0/npiperelay_windows_amd64.zip
unzip -j npipe* npiperelay.exe
chmod +x /tmp/npiperelay.exe
sudo mv /tmp/npiperelay.exe /usr/local/bin/
```

verify that the exe is in the correct path with execution permissions (`--x`)

```sh
ls -l "$(command -v npiperelay.exe)" 
-rwxr-xr-x 1 vah vah 1872384 Jul  2  2020 /usr/local/bin/npiperelay.exe
```

> the [ipc](https://tldp.org/LDP/tlk/ipc/ipc.html) path varies depending on the environment you are using (see [here](https://carlosbecker.com/posts/discord-rpc-ssh/) or below)
> - ios: `/var/run/discord-ipc-0`
> - macos: `$TMPDIR/discord-ipc-0`
> - windows: `[[\\.\pipe\]]discord-ipc-0`
> - linux: `$XDG_RUNTIME_DIR/discord-ipc-0`

please adjust the socket path below to match your os if you are **not** on wsl

```sh
# socat forwards its byte stream to npiperelay,
# which attaches to the windows named pipe \\.\pipe\discord-ipc-0
socat UNIX-LISTEN:/tmp/discord-ipc-0,fork \
EXEC:"npiperelay.exe -ei -s //./pipe/discord-ipc-0",nofork &

# verify it exists + socket (s) bit
ls -l /tmp/discord-ipc-0
srwxr-xr-x 1 vah vah 0 Feb 27 17:13 /tmp/discord-ipc-0
```

obviously running this manually every time gets annoying, so we can wrap it inside our shell config (`bash`, `zsh`, etc.)

```sh
# credits: https://gist.github.com/mousebyte/af45cbecaf0028ea78d0c882c477644a#aliasing-nvim)
# slightly modified by me
nvim () {
  if ! pgrep -f "UNIX-LISTEN:/tmp/discord-ipc-0" >/dev/null; then
    [ -e /tmp/discord-ipc-0 ] && rm -f /tmp/discord-ipc-0
    socat UNIX-LISTEN:/tmp/discord-ipc-0,fork \
      EXEC:"npiperelay.exe -ei -s //./pipe/discord-ipc-0",nofork &
  fi
  command nvim "$@"
}

# optional aliases if you prefer typing 'v'/'vim' over 'nvim'
alias v="nvim"
alias vim="nvim"
```

this function intends to shadow the `nvim` binary, ensuring the alias facilitates the consistent loading of the ipc mechanism upon startup

don't forget to reload your shell / source it

```sh
source ~/.zshrc
```

---

### forwarding the socket over ssh

onwards, i will partially follow [this post](https://carlosbecker.com/posts/discord-rpc-ssh/) with minor adjustments to properly compile with wsl

the relay created earlier exposes `/tmp/discord-ipc-0`, however, nvim expecets the discord ipc socket in the linux user runtime directory (`/run/user/1000/`)

to bridge this namepsace gap, we installed `openssh`, which conveniently enough is capable of unix domain socket forward via `RemoteForward`

this effectively maps:

```
/tmp/discord-ipc-0    ->    /run/user/1000/discord-ipc-0
(wsl relay socket)          (linux runtime socket)
```

firstly, get your wsl instance ip

```sh
ip a | grep 'inet '
```

add the following snippet to `~/.ssh/config`

```sh
Match host <wsl-ip> exec "mkdir -p /tmp && touch /tmp/discord-ipc-0"
  Host <wsl-ip>
  User <your-user>
  RemoteForward /run/user/1000/discord-ipc-0 /tmp/discord-ipc-0
```

then create a directory for `discord.conf` & enable `StreamLocalBindUnlink`

```sh
sudo mkdir -p /etc/ssh/sshd_config.d
echo "StreamLocalBindUnlink yes" | sudo tee -a /etc/ssh/sshd_config.d/discord.conf
sudo systemctl restart ssh
```

lastly, establish the loopback ssh session from within ssh

```sh
ssh -v <wsl-ip>
socat -u OPEN:/dev/null UNIX-CONNECT:/run/user/1000/discord-ipc-0
```

if there is no error, you're good to go to install the [plugin](https://neovimcraft.com/plugin/vyfor/cord.nvim/)

---

### the actual plugin-part

if you're using [lazyvim](https://lazy.folke.io/), follow along, otherwise tweak it from the [plugin](https://neovimcraft.com/plugin/vyfor/cord.nvim/) installation reference depending on your nvim distro

```lua
return {
  "vyfor/cord.nvim",
  opts = {
    -- additional config
  }
}
```

sync with your package manager (`:Lazy sync`) & relaunch nvim

that's pretty much it!

in case you want to troubleshoot, simply run `:checkhealth cord` inside your nvim distro to see what could be missing

---

### ok so.. wtf is happening?

```
discord exposes windows named pipe
|
└─ \\.\pipe\discord-ipc-0     # discord binds to this socket on windows
    |
    └─ npiperelay.exe         # bridges windows pipe to the wsl unix socket
      |
      └─ /tmp/discord-ipc-0   # wsl unix socket
          |
          └─ ssh remoteforward
              |
              └─ /run/user/1000/discord-ipc-0   # forward runtime socket
                  |
                  └─ nvim rpc plugin   # cord.nvim
```

wsl2 runs a real linux kernel inside a lightweight [vm](https://en.wikipedia.org/wiki/Virtual_machine), therefore windows applications cannot directly access its unix domain socket -> nvim expects a unix domain socket

the solution inserts a bidirectional relay that translates between these ipc primitives & forwards the stream into the linux user runtime space
