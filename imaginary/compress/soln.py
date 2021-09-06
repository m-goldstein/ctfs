import codecs
import zlib
fname = "bytes"
fp = open(fname, "rb")
body = fp.read()[:-1]
body_enc = codecs.decode(body, 'hex')
print(zlib.decompress(body_enc))
