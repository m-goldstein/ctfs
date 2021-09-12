from checker import encoded, up, down, right, left,encode
chunks = [encoded[i:i+8] for i in range(0,len(encoded),8)]
valid_ascii = [chr(i) for i in range(0x20,0x7f)]
idx = 0
s = ''
solved = False
while not solved:
    for e in valid_ascii:
        if encode(e) == chunks[idx]:
            #print('idx: {}, char: {}'.format(idx,e))
            s += e
            idx += 1
            if idx == 23:
                solved = True
                break
ss = list(s)
ss.reverse()
print('{}'.format(''.join(e for e in ss)))
