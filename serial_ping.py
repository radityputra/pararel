import os, re
import time

start = time.time()
receieved_packet = re.compile(r"(\d) received")
status = ("no respomse", "alive but loses", "alive")

for suffix in range(5,213):
    ip="192.168.0" + str(suffix)
    print_out = os.popen("ping " + ip, "-n 2 r")
    print ("ping -q -c2 " + ip, "r")
    print ("...pinging ",  ip)

    while True:
        line = ping_out.readline()
        if not line: break
        n_received = received_packet.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

end = time.time()
print(end-start)
