from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
conn.request('HEAD', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)
data = resp.info()
print(data)