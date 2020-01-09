import os
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def download_image(url, data):
    if not os.path.exists('DOWNLOAD'):
        os.makedirs('DOWNLOAD')

    parser = ImageParser()
    parser.feed(data)
    data_set = set(i for i in parser.result)
    
    for i in sorted(data_set):
        image_url = urljoin(url, i)
        basename = os.path.basename(image_url)
        target_file = os.path.join('DOWNLOAD', basename)

        print("Downloading...", image_url)
        urlretrieve(image_url, target_file)

def main():
    host = 'www.google.co.kr'

    conn = HTTPConnection(host)
    conn.request('GET', '')
    resp = conn.getresponse()

    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()

    print('\n>>>>>>>> Download Images from', host)
    url = urlunparse(('http', host, '', '', '', ''))
    download_image(url, data)

if __name__ == '__main__':
    main()