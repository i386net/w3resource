# 55. Write a Python to find local IP addresses using Python's stdlib

import subprocess
import socket

#print(socket.gethostbyname_ex(socket.gethostname()))
#print(subprocess.run('ipconfig'))

for address in socket.gethostbyname_ex(socket.gethostname())[2]:
    print(address)