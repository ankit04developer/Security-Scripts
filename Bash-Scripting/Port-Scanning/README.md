# Port Scanner

A simple TCP port scanner written in bash — takes a host and a port
range, and reports which ports are open.

## What it does
Loops through a range of ports and tries to open a TCP connection to 
each one using bash's `/dev/tcp`. If the connection succeeds, the port 
is open.

## How to run it
​```bash
./portScanning-file.sh <host> <startPort> <endPort>
​```

## The problem I ran into
My first version that i have made had no timeout — when it hit a filtered port (one 
that doesn't respond at all), the script just hung for a long time 
per port, making a full scan painfully slow. I didn't understand why 
at first, since "open" and "closed" both responded fast, but 
"filtered" ports don't respond at all.

## How I fixed it / what I learned
I use Claude.ai for the help. So It make a complete script but i didn't understand the script. So, I ask for breakdown the code then i understand that wrapping the connection attempt in `timeout 1` forces it 
to give up after 1 second instead of waiting indefinitely. This taught 
me the difference between open, closed, and filtered ports — and why 
real tools like Nmap treat "no response" as its own category instead 
of just "closed."

## Legal note
Only run this against hosts you own or have permission to test.
