#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import os
import random
from codecs import encode,decode
from array import array
from socket import socket
from telnetlib import Telnet
host = 'puzzler7.imaginaryctf.org'
port = 6666
sock = socket()
sock.connect((host,port))
buf = sock.recv(1024)
enc_flag = buf[buf.find(b'encrypted flag: ')+len(b'encrypted flag: '):buf.find(b'\n')]
flag_bytes = decode(enc_flag, 'hex')

ct_bytes = flag_bytes
flag = b'0'*16
valid_ascii = [i for i in range(0x20, 0x7e)]
flg = 'ictf{}'
msg = ['']
guessed_nonce = 0
block_idx = 0
n_bytes = 0
keystream = []
decrypted = []
offset = 0
pt = '{'
fack = b'ictf{c7rypt0gr4Phy_1s_th3_b3st_7yp3_0f_crYpt0gR4pHy}'
pt2 = array('B',fack + b'\x00'*(len(flag_bytes)-len(fack)))
j = len(fack)
count = 0
while True:
    try:
        for c in valid_ascii:
            pt2[j] = c
            gg = ''.join(chr(e) for e in pt2)
            guess = gg.encode()
            count += 1
            if not count % 1000:
                print('\t[DEBUG] current guess: {}'.format(gg))
                count = 1
            keystream = [ct_bytes[i] ^ guess[i] for i in range(len(guess)+offset)]
            dec = [ct_bytes[i] ^ keystream[i] for i in range(len(ct_bytes))]
            mm = b''.join(chr(e).encode() for e in dec)
            sock.send(mm + b'\n')
            buf = sock.recv(1024)
            resp = buf[:buf.find(b'\n')]
            if decode(resp, 'hex')[:j+1] == flag_bytes[:j+1]:
                pt2[j] = c
                print('built: {}'.format(''.join(chr(e) for e in pt2)))
                j += 1
    except Exception as e:
        print('\t[RESET] exception: {}'.format(e))
        print('\tcurrent guess: {}'.format(''.join(chr(e) for e in pt2)))
        sock = socket()
        sock.connect((host,port))
        sock.recv(1024)
