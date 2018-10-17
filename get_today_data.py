# coding = utf-8
import time
from bs4 import BeautifulSoup

html_file = open('./html/BTDDongge.html', 'r')
html_page = html_file.read()

soup = BeautifulSoup(html_page, 'lxml')

last_post_published_at = soup.select('.feed_body .timestamp')[0].string.strip()
print(last_post_published_at)
today = time.strftime("%Y-%m-%d", time.localtime())
if last_post_published_at == today:
    posts = soup.select('.feed_item_question')
    post_list = []
    for post in posts:
        post_title = post.select('.question_link')[0].string.strip()
        post_url = 'http://chuansong.me' + post.select('.question_link')[0]['href']
        post_published_at = post.select('.timestamp')[0].string.strip()
        if post_published_at == last_post_published_at:
            post_list.append({'title': post_title, 'url': post_url, 'published_at': post_published_at})

    print(post_list)
