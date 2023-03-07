import socket
import uuid
print("Your Name?")
i = input()
print("privet, ",i)
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your IP Address : "+IPAddr)
print ("Your MAC address : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))