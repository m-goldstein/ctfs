fp = open('flag.txt','rb')
def bitflip(b):
    if b.count(b'1') > b.count(b'0'):
        return b'1'
    elif b.count(b'1') < b.count(b'0'):
        return b'0'
body = fp.read()
body_chunks = [body[i:i+3] for i in range(0, len(body), 3)]
bitstring = b''.join(e for e in [bitflip(e) for e in body_chunks])
body_bytes = [bitstring[i:i+8] for i in range(0,len(bitstring),8)]
body_chars = [chr(int(e,2)) for e in body_bytes]
flag = ''.join(e for e in body_chars)
print('flag is {}'.format(flag))
