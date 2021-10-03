fp = open('puzzle.txt','r')
body = fp.read().split('\n')[:]
flag = ''.join(e[0] for e in body)
flag = 'ictf{'+flag+'}'
print(f'flag: {flag}')
