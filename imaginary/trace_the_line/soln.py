import requests
import time
HOST = 'http://puzzler7.imaginaryctf.org:7000/'
data = {}
r = requests.get(HOST)
formtext = r.text[r.text.index('<form')+15:r.text.index('<form')+47]
while True:
    try:
        r = requests.get(HOST+formtext,data=data)
        if '<div style="color:green">' in r.text:
            flagtext = r.text[25+r.text.index('<div style="color:green">'):r.text.index('</div')]
            print('potential flag found: {}'.format(flagtext))
            input()
        formtext = r.text[r.text.index('<form')+15:r.text.index('<form')+47]
        flagtext = r.text[23+r.text.index('<div style="color:red">'):r.text.index('</div')]
        count    = r.text[r.text.index('button')+7:r.text.index('time(s)')]
        print('[{}] flagtext:\t {}'.format(count,flagtext))
        time.sleep(.25)
    except Exception as e:
        print('exception: {}'.format(e))
        time.sleep(1)
