import codecs
import random
from hashlib import md5
enc =  b'\x1d\x80\x1d\xe0\xa7\x89\x9d\x0f3\xa03`z\x8d\x1b\xbc\xe4\xb7\xcec9\x7f\x8d\x00\xbf\xee\xb7\xc0>js\xafa'
dec = []
s = list('ictf{')
iv = 0
idx = 0
while iv < 256:
    if chr(enc[idx] ^ iv) == s[0]:
        print('iv: {}'.format(iv))
        dec.append(chr(enc[idx] ^ iv))
        idx += 1
        break
    iv += 1
while True:
    iv = md5(bytes([iv])).digest()[0]
    if iv == 0:
        iv += 1
    dec.append(chr(enc[idx]^iv))
    idx += 1
    if (''.join(e for e in dec)).endswith('}'):
        print('flag: {}'.format(''.join(e for e in dec)))
        break
