from pwn import *
filename= './aibophobia'
# break right after the random number generator and replace the random number with 0s so the key
# isn't obfuscated.
io = gdb.debug(filename, """
        b *main+90
        define sn
        p $eax = 0x0
        p $edx = 0x0
        c
        end
        {}
        detach
        quit
        """.format('sn\n'*50))
print(io.recv())
io.sendline(b'  '*50)
buf = io.recvuntil(b'not:\n')
print('flag: {}'.format(io.recv()))
