from pwn import *
import time
import base64
from owiener import attack,isqrt
from Crypto.Util.number import inverse,bytes_to_long,long_to_bytes,GCD
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morae code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2 :
                 # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    return decipher
def rot(s, k):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    s = list(s)
    for i in range(len(s)):
        e = s[i]
        is_upper = e.isupper()
        if e in [' ','.','_']:
            continue
        idx = alphabet.index(e.lower())
        new_idx = (idx+k)%len(alphabet)
        if is_upper:
            s[i] = alphabet[new_idx].upper()
        else:
            s[i] = alphabet[new_idx]
    return ''.join(e for e in s)



def iroot(k,n):
    u,s = n,n+1
    while u < s:
        s = u
        t = (k-1)*s+n // pow(s,k-1)
        u = t//k
    return s
binary = remote("crypto.chal.csaw.io", 5001)
done = False
while not done:
    try:
        print(binary.recvuntil(bytes("mean?", "utf-8")))
        more = (binary.recvuntil(bytes(">>", "utf-8"))) # Morse code
        morseCode = str(more, 'utf-8').replace('>>' ,"")
        morseCode = morseCode.replace('\n', "").replace('\r', '')
        words = morseCode.split('/')
        text = ""
        for word in words:
                text += chr(int(decrypt(word)))

        based = base64.b64decode(text).split(b'\n')
        N = int(based[0].decode()[4:])
        e = int(based[1].decode()[4:])
        c = int(based[2].decode()[4:])

        cube_root = iroot(3,c)
        root_bytes = long_to_bytes(cube_root)
        rot_bytes = rot(root_bytes.decode(),13).encode()
        binary.sendline(rot_bytes)
    except Exception as e:
        print('exception: {}'.format(e))
        done = True
binary.recvuntil(b'friends: ')
buf = binary.recvuntil(b'\r\n')[:-2].decode()
print('flag: {}'.format(buf))
