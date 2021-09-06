def rules(n):
    if n % 2 == 0:
        n = (n >> 1)
    elif n%2 != 0 and n % 5 == 0:
        n = (n//5)
    elif n%2 != 0 and n%5 !=0 and n%3 ==0:
        n = (n+8)
    return n
data = [328125, 309375, 3712, 3264, 384375, 221875, 1536, 1536, 3200, 296875, 2752, 303125, 3648, 153125, 303125, 3136, 3456, 159375, 296875, 2496, 303125, 340625, 159375, 359375, 296875, 2624, 296875, 2688, 3328, 159375, 328125, 3648, 296875, 1536, 371875, 3520, 296875, 2624, 159375, 371875, 303125, 3648, 3200, 390625]
count = 0
while 'ictf' not in ''.join([chr(e) for e in data]):
    for i in range(len(data)):
        data[i] = rules(data[i])
    count += 1
soln = ''.join([chr(e) for e in data])
print('flag: {}'.format(soln))
