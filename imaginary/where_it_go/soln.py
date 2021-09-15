from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes,bytes_to_long
import sys
import os
from PIL import Image
datafile = 'datafile'
n_pixels = 1000
bytes_per_pixel = 4
n_bytes = n_pixels * bytes_per_pixel

fp = open(datafile, 'rb')
body = fp.read()
try:
    j = 1
    while True:
        rawbytes = [e^j for e in body][:]
        j += 1
        pxldata = [rawbytes[i:i+bytes_per_pixel] for i in range(0, len(rawbytes), bytes_per_pixel)]
        im = Image.new('RGBA', (n_pixels,len(body)//(n_bytes)))
        im.putdata([tuple(e) for e in pxldata])
        im.save('test.png')
        os.system('timeout 1s display test.png')
except Exception as e:
    print(f"Exception: {e}")
