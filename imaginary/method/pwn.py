import requests as req
from hyper import HTTPConnection
HOST = 'http://method.max49.repl.co'


conn = HTTPConnection(HOST)
conn.request('GET','/')
c =  conn.get_response()
r = req.get(HOST)
