from urllib.request import Request, HTTPCookieProcessor, build_opener

url = 'http://naver.com' 

cookie_handler = HTTPCookieProcessor()
opener = build_opener(cookie_handler)

req = Request(url)
res = opener.open(req)

print(res.read().decode('utf-8'))
print(res.info())

print('------------------------------------')

data = 'language=python&framework=django'
enc_data = bytes(data, encoding='utf-8')

req = Request(url, enc_data)
res = opener.open(req)

print(res.read().decode('utf-8'))
print(res.info())
