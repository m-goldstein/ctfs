from telnetlib import Telnet
from socket import socket
host = 'puzzler7.imaginaryctf.org'
port = 5555
sock = socket()
sock.connect((host,port))
print(sock.recv(1024))
sock.send(b'tic culprit\n')
resp = sock.recv(1024)
resp = resp.decode()

print(resp)
resp = resp[resp.find('ictf'):resp.find('}')+1]
print('flag: {}'.format(resp))
