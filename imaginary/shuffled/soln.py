import random
from hashlib import md5
outfile = 'out.txt'
fp = open(outfile, 'r')
rand_fp = open('/dev/random','rb')
body = fp.read()
k = 0
"""
Fisher-Yates works by swapping certain pairs of elements. So to reverse the process you can feed the same key into the same PRNG, then run through the Fisher-Yates algorithm as if you were shuffling an array the size of your string. 

But actually you don't move anything, just record the indexes of the elements that would be swapped at each stage.

Then run through the list of swaps in reverse and apply them to your shuffled string to obtain the original plaintext.
"""
while True:
    try:
        tmp = list(body)
        #random.seed(k)
        random.seed(rand_fp.read(2))
        indices_to_swap = []
        for i in range(len(tmp)-1,-1,-1):
            j = random.randint(0, i)
            indices_to_swap.append((i,j))
        for m in range(len(indices_to_swap)-1,-1,-1):
            e,f = indices_to_swap[m]
            tmp[e],tmp[f] = tmp[f],tmp[e]
        decoded = ''.join(e for e in tmp)
        if 'cryptanalysis' in decoded:# and ' the ' in decoded:
            print('decoded: {}'.format(decoded))
            flag = '{}'.format(md5(decoded.encode()).hexdigest())
            print('flag: ictf{'+flag+'}')
            break
    except Exception as e:
        print('exception: {}'.format(e))
    finally:
        k += 1
        if not (k % 10000):
            print('k: {}'.format(k))

