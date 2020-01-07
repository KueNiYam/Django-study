from urllib.request import urlopen, Request
from urllib.parse import urlencode

url: str = 'http://127.0.0.1:8000'
data: dict = {
    'name': '최근휘',
    'email': 'kueniyam@naver.com',
    'url': 'http://www.naver.con'
}

enc_data: str = urlencode(data)
post_data: str = bytes(enc_data, encoding='utf-8')
req: Request = Request(url, data=post_data)
req.add_header(
    'Content-Type',
    'application/x-www-form-urlencoded'
)

result = urlopen(req)
print(result.info)
print(result.read(500).decode('utf-8'))