import urllib.request

url = 'http://www.example.com'
proxy_server = 'http://www.proxy.com:3128'

proxy_handler = urllib.request.ProxyHandler({'http':proxy_server})
proxy_handler = urllib.request.ProxyHandler({})

proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password(
    'realm',
    'host',
    'username',
    'password'
)

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

# 디폴트 오프너 지정
urllib.request.install_opener(opener)
result = urllib.request.urlopen(url)

print('geturl():', result.geturl())
print(result.read(300).decode('utf-8'))