# Ping Sweep Scanner

A bash script that checks which hosts on a subnet are alive by pinging every possible address — takes a subnet prefix and reports which hosts respond.

## What it does
Loops through every address in a subnet (.1 to .254) and pings each one. If a host responds, it's marked as alive and added to a list.

## How to run it
```bash
./ping_sweep.sh <subnet-prefix>
```
Example: `./ping_sweep.sh 192.168.1` (scans 192.168.1.1 to 192.168.1.254)

## The problem I ran into
My first thought was to just ping every address the normal way, but I realized that if I don't limit the wait time, a host that doesn't respond could make the script sit there way longer than needed — 254 addresses, each potentially waiting several seconds, would make the whole sweep painfully slow. I also wasn't sure how to actually collect and count which hosts responded, since I hadn't used arrays in bash before.

## How I fixed it / what I learned
I used Claude.ai for help here too. It gave me `-c 1 -W 1` for the ping command and used a bash array (`alive_hosts+=(...)`) to store the responding hosts. I asked for a breakdown since I didn't fully understand it at first, and learned that `-c 1` sends just one ping instead of the default continuous stream, and `-W 1` caps the wait time to 1 second per host so the script doesn't hang. I also learned `${#alive_hosts[@]}` counts array items and `"${alive_hosts[@]}"` loops through them — similar to `.length` and `.forEach()` in JavaScript, which helped it click faster. This also taught me the difference between a ping sweep (checks if a host exists at all, using ICMP) and a port scan (checks if a specific service is open, using TCP) — a host can be alive but show no open ports, or have open ports while ignoring pings entirely.

## Legal note
Only run this against networks you own or have explicit permission to test — even a ping sweep can be flagged as unauthorized activity on networks you don't control.
