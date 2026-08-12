#!/bin/bash
# Simple TCP Port Scanner
# Educational use only — scan only hosts you own or have permission to test.

if [ -z "$1" ]; then
    echo "Usage: $0 <host> [start_port] [end_port]"
    echo "Example: $0 127.0.0.1 1 1000"
    exit 1
fi

host=$1
start_port=${2:-1}
end_port=${3:-1000}

echo "Scanning $host from port $start_port to $end_port..."

for port in $(seq $start_port $end_port); do
    timeout 1 bash -c "echo >/dev/tcp/$host/$port" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Port $port is OPEN"
    fi
done

echo "Scan complete."
