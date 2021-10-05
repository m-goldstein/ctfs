from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import bytes_to_long as btl, long_to_bytes as ltb
from codecs import encode,decode
sk = open('private.pem','rb').read().rstrip()
pk = open('public.pem','rb').read().rstrip()
enc = open('enc.txt','rb').read().rstrip()
public_key = RSA.import_key(pk)
private_key = RSA.import_key(sk)
flag = ltb(pow(btl(enc), private_key.d, private_key.n))
flag = flag[flag.index(b'\x00'):].rstrip()              # take out padding
flag = decode(flag,'utf-8')                             # to properly decode b'\xe2\x80\x93' flag bytes
print(f'flag: {flag}')
