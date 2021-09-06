fp = open('flag','rb')
body = fp.read()
sanitized = body.replace(b'\n',b'').replace(b'[1A',b'').replace(b'\x1b',b'')
sidx = sanitized.index(b'ictf{')
eidx = sanitized[sidx:].index(b'}')
flag = sanitized[sidx:sidx+eidx+1]
print('flag: {}'.format(flag))
