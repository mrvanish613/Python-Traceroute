from scapy.all import IP, ICMP, sr1

def traceroute(target):
    # Initialize Time-To-Live (TTL) value
    ttl = 1
    while True:
        # Create an IP/ICMP packet with the target IP address and current TTL
        packet = IP(dst=target, ttl=ttl) / ICMP()
        # Send the packet and wait for a reply
        reply = sr1(packet, verbose=False, timeout=1)
        if reply is None:
            # No reply received within the timeout period
            print(f"{ttl} ::: No reply ")
        elif reply.type == 11:
            # Received a Time Exceeded message
            print(f"{ttl} ::: Reply from {reply.src}")
        elif reply.type == 0:
            # Received an Echo Reply message, indicating destination reached
            print(f"{ttl} ::: Destination reached: {reply.src}")
            break
        ttl += 1

if __name__ == '__main__':
    # Get target host from user input
    target = input("[Host] ::: ")
    traceroute(target)
