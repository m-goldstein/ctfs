import base64
fp = open('rotversing2.py','r')
body = fp.read().split('\n')
data = body[3:-1]
sigma = 'abcdefghijklmnopqrstuvwxyz'
def substitute(c):
    global sigma
    if c.isupper():
        isUpper = True
    else:
        isUpper = False
    if sigma.count(c.lower()):
        newidx = (sigma.index(c.lower()) + 13)%len(sigma)
        if isUpper:
            return sigma[newidx].upper()
        else:
            return sigma[newidx]
    else:
        return c

translated = ''
symbols =[' ','','_','?','(',')','!','=','"','h"']
for e in data:
    for c in e:
        if c.lower() in sigma:
            translated += substitute(c)
        elif c.isdigit():
            translated += str(c)
        elif c == ' ' or c == '':
            translated += ' '
        elif c in symbols:
            translated += c
flag = translated[95:-22]
print('flag is: {}'.format(base64.b64decode(base64.b64decode(flag))))
