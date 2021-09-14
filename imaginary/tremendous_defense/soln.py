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
        resp = json.loads(r.text)
        regexp = rstr.xeger(resp['pwReq'])
        r = requests.post(host.format(port) + endpoints['token'], json={'password':regexp})
        if 'signedPassword' in r.text:
            resp = json.loads(r.text)
            pw_int = int.from_bytes(regexp.encode(), 'big')
            key = int(resp['signedPassword'])^pw_int^1337
            r = requests.post(host.format(port) + endpoints['state'],json={'signedPassword':key})
            if 'port' in r.text:
                jsonp = json.loads(r.text)
                r = requests.get(host.format(jsonp['port'])+endpoints['flag']+'?token={}'.format(jsonp['token']))
                if 'ictf' in r.text:
                    flag = r.text.split('\n')[1][4:-4]
                    print('flag: {}'.format(flag))
                    break
except Exception as e:
    print('exception: {}'.format(e))
