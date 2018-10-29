from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner
import requests
import jieba
from jieba import analyse
import time


# 获取网页
def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url=url, headers=headers, timeout=5)
    return response.content


# 获取HTML正文
def get_post_content(html_page):
    soup = BeautifulSoup(html_page, 'lxml')
    post_content = soup.find_all(class_="rich_media_content")[0]
    return post_content


# 获取HTML正文纯文本
def get_post_content_text(html):
    raw = html.text.replace('\n', '').replace(' ', '')
    return raw


def get_post_keywords(text):
    textrank = analyse.textrank
    keyword_list = textrank(text, topK=30)
    return ','.join(keyword_list)


target_post_list = [
    {'title': '健身者，你吃饭别太矫情！', 'url': 'https://mp.weixin.qq.com/s?__biz=MjM5NzUxNTc0Mw==&mid=2654737217&idx=1&sn=23f78547d0cee05de2484b6bbf73e231&chksm=bd106bf18a67e2e7178c43d2ee29d6674c3338236f8927eb7bd8e81b9f52c0f7d70ef967cb42&scene=0&ascene=7&devicetype=android-19&version=26060739&nettype=WIFI&abtest_cookie=AwABAAoACwATAAMAJJceAFaZHgBimR4AAAA%3D&lang=zh_CN&pass_ticket=tDkxizCisX4ysZWvOKq%2FjECDfYgTV7ChNAAcBPY71bmVAfJaU%2BoIBNiiP3L8UbxH&wx_header=1', 'published_at': '2015-11-03'}]

for target_post in target_post_list:
    target_url = target_post['url']
    target_html = get_html(target_url)
    html_content = get_post_content(target_html)
    text_content = get_post_content_text(html_content)
    start_time = time.time()
    keywords = get_post_keywords(target_post['title'] + text_content)
    print(keywords)
    end_time = time.time()
    print('提取关键词耗时：', end_time - start_time)
