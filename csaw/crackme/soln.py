from hashlib import sha256
import os
outfile = 'out'
salt = b'sha256'
#fp = open('/usr/share/dict/words','r')
#fp = open('words.txt','rb') # make your own words.txt
#words = fp.read().split(b'\n')[:-1]
words = [b'cathouse']
hsh = 'a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c'
k = 0
done = False
while not done:
    try:
        for w in words:
            sh1 = sha256(w.lower() + salt).hexdigest()
            sh = sha256(salt+w.lower()).hexdigest()
            if sh == hsh or sh1 == hsh:
                print('found match\nword: {}, hash: {}'.format(w,sh))
                print('found match\nword: {}, hash: {}'.format(w,sh1))
                done = True
                break
            k += 1
            if not (k % 10000):
                print('words[{}]: {}'.format(k, w))
    except Exception as e:
        print('exception: {}'.format(e))
