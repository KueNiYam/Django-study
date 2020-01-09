from urllib.request import HTTPBasicAuthHandler, build_opener

url = 'http://127.0.0.1:8000/auth/'
auth_handler: HTTPBasicAuthHandler = HTTPBasicAuthHandler()
auth_handler.add_password(
    realm='ckh', 
    user='kuenhwi',
    passwd='rmdmdmdmdsl',
    uri=url
)
opener = build_opener(auth_handler)
response = opener.open(url)
print(response.read().decode('utf-8'))