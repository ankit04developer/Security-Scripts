#!/bin/bash
# Ping Sweep Scanner
# Checks which hosts on a subnet are alive (respond to ping).
# Educational use only — scan only networks you own or have permission to test.

if [ -z "$1" ]; then
    echo "Usage: $0 <subnet-prefix>"
    echo "Example: $0 192.168.1"
    echo "(This will scan 192.168.1.1 to 192.168.1.254)"
    exit 1
fi

subnet=$1
echo "Sweeping $subnet.1 to $subnet.254 ..."
echo ""

alive_hosts=()

for i in $(seq 1 254); do
    host="$subnet.$i"
    # -c 1: send 1 packet, -W 1: wait max 1 second for reply
    ping -c 1 -W 1 "$host" &>/dev/null
    if [ $? -eq 0 ]; then
        echo "$host is UP"
        alive_hosts+=("$host")
    fi
done

echo ""
echo "Sweep complete."
echo "Alive hosts found: ${#alive_hosts[@]}"
for h in "${alive_hosts[@]}"; do
    echo " - $h"
done
