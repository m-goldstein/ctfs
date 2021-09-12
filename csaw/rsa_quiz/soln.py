from pwn import *
from Crypto.Util.number import long_to_bytes,bytes_to_long,inverse
import owiener
from socket import socket
from telnetlib import Telnet
import time
def iroot(k,n):
    u,s = n,n+1
    while u < s:
        s = u
        t = (k-1)*s+n // pow(s,k-1)
        u = t//k
    return s
host = 'crypto.chal.csaw.io'
port = 5008
#sock = socket()
#sock.connect((host,port))
#print(sock.recv(1024))
sock = remote(host, port)
# PART 1
print(sock.recvuntil(b'!')) #sock.recv(1024).split(b'\r\n')
buf = sock.recvuntil(b'What is the plaintext?\r\n')[4:].split(b'\r\n')
N = int(buf[0].decode()[4:])
e = int(buf[1].decode()[4:])
c = int(buf[2].decode()[4:])
d = owiener.attack(e,N)
pt = long_to_bytes(pow(c,d,N))
sock.sendline(pt)
print(sock.recv(1024))

# PART 2
buf = sock.recv(1024).split(b'\r\n')
N = int(buf[0].decode()[4:])
e = int(buf[1].decode()[4:])
c = int(buf[2].decode()[4:])
p1 = abs(owiener.isqrt(N+1) - 1)
p2 = abs(-owiener.isqrt(N+1) - 1)
p1 = p1 - 1
p2 = N // p1
assert(p1*p2 == N)
print('[Success!] assertion passed')
phi = (p1-1)*(p2-1)
d = inverse(e, phi)
pt = long_to_bytes(pow(c,d,N))
sock.sendline(pt)

# PART 3
print(sock.recv(1024))
buf = sock.recv(1024).split(b'\r\n')
N = int(buf[0].decode()[4:])
e = int(buf[1].decode()[4:])
#buf = sock.recv(1024).split(b'\r\n')
buf = sock.recvuntil(b'What would you like to decrypt? (please respond with an integer)').split(b'\r\n')
c = int(buf[0].decode()[4:])
old_c = c
#print(sock.recvuntil(b'\r\n'))

asciz = [e for e in range(0x20,0x7f)]
string_builder = list()
m = 0
idx = 0
pt = 0
done = False
while not done and c >= 0:
    try:

        print(sock.recvline()) 
        #for ch in asciz:
        #string_builder[idx] = ch
        #payload = b''.join(e for e in string_builder)
        #s = pow(ch, e, N)
        pt = ''.join(str(g) for g in reversed(string_builder)) if len(string_builder) > 0 else '0'
        pt = int(pt, 2)
        ptt = pow(pt, e, N)
        payload = c+ptt#(c+ptt)
        print('trying: {}'.format(payload))
        #payload = bytes_to_long(payload)
        #payload = payload.hex().encode()
        sock.sendline(str(payload).encode())
        #time.sleep(.1)
        #print(sock.recvline())
        print(sock.recvuntil(b'with: '))
        oracle_resp = sock.recvuntil(b'\r\n')[:-2]
        print('got: {} from oracle'.format(oracle_resp))
        if oracle_resp == b'1':
            string_builder.append(1)
            #string_builder.insert(-1,1)
        elif oracle_resp == b'0':
            string_builder.append(0)
            #string_builder.insert(-1,0)
        c >>= 1
        #c = (c >> 1)
            #B = 256 * (1022)
            #if 2*B <= (m+s)%N <= 3*B:
            #    m = m + s
            #    string_builder.append(chr(ch))
        
        buf = sock.recv(1024)
        if b'(yes/no)' in buf:
            print('oracle asks us to continue...')
            sock.sendline(b'yes')
            #input()
        else:
            print('buf: {}'.format(buf))
        #print(sock.recvuntil(b'(yes/no)\r\n'))

        #input()
        if c <= 0 :
            break
    except Exception as e:
        print('Exception: {}'.format(e))
        #string_builder.append(c)
        idx += 1
        done = True
#string_builder.reverse()
aa = ''.join(str(e) for e in string_builder)
chunks = [aa[i:i+8] for i in range(0, len(aa), 8)]
chunks = [int(e,2) for e in chunks]
chars = [chr(e) for e in chunks]
print('got: {}'.format(''.join(e for e in chars)))

raa = ''.join(str(e) for e in reversed(string_builder))
rchunks = [raa[i:i+8] for i in range(0, len(raa), 8)]
rchunks = [int(e,2) for e in rchunks]
rchars = [chr(e) for e in rchunks]
print('rgot: {}'.format(''.join(e for e in rchars)))
