from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner
import requests

url = 'http://www.csh.com.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

html = requests.get(url, headers=headers).content
cleaner = Cleaner(style=True, scripts=True, comments=True, javascript=True, page_structure=False, safe_attrs_only=False)
content = cleaner.clean_html(html.decode('utf-8')).encode('utf-8')
raw = BeautifulSoup(content, "lxml").text

print(raw.replace('\n', '').replace(' ', ''))
