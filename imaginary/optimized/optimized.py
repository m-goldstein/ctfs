import sys
from unoptimized2 import keys
i = 2
w = 1
flag = ''
l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101,103,
     107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241
     ,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389]
for k in keys:
    while True:
        # just going to take this messy stuff out and use pre-calculated primes....
        
        #if((lambda f: lambda g: lambda *h: g(f(lambda g: f(g))(g))(*h))(lambda h: lambda f: lambda *g: f(h(lambda g: h(g))(f))(*g))((lambda g: lambda f: lambda h,i=2: [lambda: True, lambda: g((h % i) * f(h, i+1))][1 - (i >= h)]())(type(... is not None)))(i)):
        if True:
            p = ( r := 1) and [r := r*a for a in l[:w]][-1]
            w += 1
            # lol, gonna remove this too.

            #if ((lambda n: any([True for j in range(2,n) if (n & 1)]) or n >= 2)(p) or p <= 3):
            if p >= 2 or p < 3:
                t = (lambda *g: sum(g))(p,1)
                if (not pow(t, .5) + pow(.5, 2) == t):
                    flag += chr(k^t%50)
                    #sys.stdout.write(chr(k^t % 50))
                    #sys.stdout.flush()
            i += 1
            break
        else:
            i += 1
print('\nflag: {}'.format(flag))
