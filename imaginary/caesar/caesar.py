import os
fp = open('caesar.txt','r')
buf = fp.read().lower()
buf = list(buf)
sigma = list('abcdefghijklmnopqrstuvwxyz')
d = {}
d['q'] = 'i'
d['k'] = 'c'
d['b'] = 't'
d['n'] = 'f'
s = ''
i = 0
keys = [k for k in d.keys()]
j = 0
"""
while True:
    cidx = sigma.index(keys[j])
    pidx = sigma.index(d[keys[j]])
    if cidx == (pidx+i) % 26:
        print(i)
        input()
        i+=1
        j+=1
    else:
        i+=1
"""
for c in buf:
    if c in d:
        s += d[c]
    elif c == '_' or c == '{' or c == '}':
        s += c
    else:
        try:
            idx = sigma.index(c)
            idx = (idx-8)%26
            s += sigma[idx]
        except:
            pass 
print(s)

