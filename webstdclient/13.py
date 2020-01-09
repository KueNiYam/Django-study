from urllib.request import urlopen
from urllib.parse import urlencode

url = 'http://127.0.0.1:8888/cgi-bin/script.py'
data = {
    'name': 'kuenhwi',
    'email': 'kueniyam@naver.com',
    'url': 'http://www.naver.com'
}
end_data = urlencode(data)
post_data = end_data.encode('ascii')

with urlopen(url, post_data) as f:
    print(f.read().decode('cp949'))