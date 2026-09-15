---
date: '2026-09-15'
description: cron WHO?
draft: false
title: bandit-21
weight: 22
---

| info | value                                      |
|:-----|-------------------------------------------:|
| user | `bandit21`                                   |
| pass | `bW9kBv5WC3P4yoDyf12LSdGuNz5ka6hY`         |

> A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

---

## explanation

firstly, what's crontab? or rather, **cron**? 

cron in itself is a ["daemon to execute scheduled commands"](https://man7.org/linux/man-pages/man8/cron.8.html) - basically the background processes that checks every x min/hour/day/week/etc., more about daemons [here](https://www.reddit.com/r/linux/comments/83ao1z/comment/dvh7jx2/)

contrary to crontrab, (short for CRON TABle), is a configuration file where users define the schedule & commands for cron to execute

think of an automated backup, which is usually a shell script handling the actions, f.e. leveraging [borgbackup](https://www.borgbackup.org/) or [restic](https://restic.net/) (plain simple rsync will do too) & now someone needs to automatically start this program every start of the month:

```sh
# syntax is provided upon executing:
crontab -e

# example:
*/45 * * * * /path/to/backup.sh
# ^ run every 45 minutes
```

> [tl;dr](https://askubuntu.com/questions/2368/how-do-i-set-up-a-cron-job#answer-2369)

examining what the cron job for bandit21 does

```sh
cat /etc/cron.d/cronjob_bandit22
# @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
# * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

and the script it executes

```sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

aaand yoink

```sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
# RYVux2rHEm9tiXHmLFzuR7Vhx6AZQMEz
```
