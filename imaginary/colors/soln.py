import os
import codecs
import zlib
fname = "colors.png"
outfile = 'colors.pnm'
decomp = 'colors.txt'
os.system("pngtopnm {} > {}".format(fname, outfile))
fp = open(outfile, 'rb')
lines = fp.read()
lines = [lines[i:i+18] for i in range(0, len(lines),18)][1:]
data = (b''.join(lines[i][0:3] for i in range(0,len(lines),15)))
startidx = data.index(b'ictf{')
endidx = data[startidx:].index(b'}')
flag = data[startidx:endidx+startidx+1]
print('flag: {}'.format(flag))
