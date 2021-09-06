#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import os
import random
from codecs import encode,decode
from array import array
with open("flag.txt", "rb") as f:
	flag = f.read()
key = os.urandom(16)

def encrypt(message):
	n = long_to_bytes(random.choice(key))
	cipher = AES.new(key, AES.MODE_CTR, nonce=n)
	return cipher.encrypt(message).hex()

encrypted_flag = encrypt(flag)

ct_bytes = decode(encrypted_flag, 'hex')

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
pt2 = array('B',b'ictf{' + b'\x00'*(11))
j = 5
while True:
    for c in valid_ascii:
        pt2[j] = c
        gg = ''.join(chr(e) for e in pt2)
        guess = gg.encode()
        #guess = flg.format(gg).encode()
        keystream = [ct_bytes[i] ^ guess[i] for i in range(len(flag)+offset)]
        dec = [ct_bytes[i] ^ keystream[i] for i in range(len(ct_bytes))]
        if b''.join(chr(e).encode() for e in dec[:j+1]) == flag[:j+1]:
            pt2[j] = c
            j += 1
        print('dec: {}'.format(dec))
        input()
#while True:
    #for c in valid_ascii:
        #pt += chr(c)
        #guess = flg.format(pt).encode()
        #keystream = [ct_bytes[i] ^ guess[i] for i in range(len(guess)+offset)]
        #dec = [ct_bytes[i] ^ keystream[i+offset] for i in range(len(keystream))]
        #print('dec: {}'.format(''.join(chr(e) for e in dec)))
        #pt = pt[:-1]
        #input()
#last = 0,0
"""
while True:
    nonce = guessed_nonce#long_to_bytes(guessed_nonce)
    dec_bytes = [chr(flag_bytes[i] ^ nonce) for i in range(len(flag_bytes))]
    print('decrypted: {}'.format(''.join(e for e in dec_bytes)))
    guessed_nonce += 1
    input()
    #n_bytes += 1
    #block_idx = n_bytes // 16
"""
"""
    if i == 0:
        msg[i] = 0x7b
        msg.append('')
        i += 1
        continue
    for c in valid_ascii:
        msg[i] = c
        tmp = flg.format(''.join([chr(e) for e in msg]))
        enc_msg = tmp.encode()
        enc_msg = encrypt(enc_msg)
        print('decrypted msg: {}'.format(tmp))
        print('flag: {}\tencrypted msg: {}'.format(encrypted_flag, enc_msg))
        msg_bytes = decode(enc_msg, 'hex')
        #for i in range(len(enc_msg)):
        #    if enc_msg[i] == encrypted_flag[i]:
        #        last = (i,c)
        #        continue
        #    else:
        #        msg[last[0]] = last[1]
        #        msg.append('')
        #        i += 1
        #        continue
        #print(tmp)
        input()
    msg.append('')
    i += 1
    """
#print(f"Here is the encrypted flag: {encrypt(flag)}")
#while True:
#	message = input("What would you like me to encrypt? ").encode()
#	print(encrypt(message))
#encrypted_flag = encrypt(flag)
#flag_bytes = decode(encrypted_flag, 'hex')
#more = []
#for i in range(len(key)):
#    more.append(key[i] ^ flag_bytes[i])
