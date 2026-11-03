from scapy.all import rdpcap, UDP

packets = rdpcap("message.pcapng")

message = ""

for p in packets:
    if UDP in p:
        message += chr(p[UDP].dport)

print(message)

if "PCTF" in message:
    print("Found!!!!")