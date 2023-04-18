import socket #socket for ip and pc login
import getpass #getpass for username
print ("Hello ",getpass.getuser()) #take username
print ("Your login:",socket.gethostname()) #take login
print ("Your External IP:",socket.gethostbyname_ex(socket.gethostname())[-1][0]) 