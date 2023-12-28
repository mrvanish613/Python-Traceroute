

### README File:
---
# Python Traceroute Script

## Description
This script implements a basic traceroute functionality using the Scapy library in Python. It sends packets with incrementing TTL (Time-To-Live) values to a specified target and listens for responses to trace the route packets take through the network to reach the target.

## Requirements
- Python 3.x
- Scapy library

To install Scapy, run:

pip install scapy


## Usage
Run the script using Python 3. When prompted, enter the hostname or IP address of the target you want to trace the route to.

## Features
- Performs a traceroute to a specified target.
- Displays each hop and its response or timeout.
- Indicates when the destination is reached.

## Limitations
- The script may not work as expected in networks where ICMP packets are filtered.
- It is a basic implementation and does not have advanced features found in dedicated traceroute tools.

---
