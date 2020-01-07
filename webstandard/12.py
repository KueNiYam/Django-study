import os
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def parse_image(data):
    soup = BeautifulSoup(data, 'html.parser')
    img_tag_list = soup.find_all('img')
    data_set = set(i.attrs['src'] for i in img_tag_list)
    return data_set

def download_image(url, data_set):
    if not os.path.exists('DOWNLOAD'):
        os.makedirs('DOWNLOAD')

    for i in sorted(data_set):
        image_url = urljoin(url, i)
        basename = os.path.basename(image_url)
        target_file = os.path.join('DOWNLOAD', basename)
        print('Downloading...', image_url)
        res = requests.get(image_url)
        with open(target_file, 'wb') as f:
            f.write(res.content)

def main():
    url = 'http://www.google.co.kr'
    res = requests.get(url)
    charset = res.encoding
    data = res.content.decode(charset)
    data_set = parse_image(data)
    print('Download Images from', url)
    download_image(url, data_set)

if __name__ == '__main__':
    main()