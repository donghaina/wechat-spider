# coding = utf-8
import time
import os
import time
# import sys

from bs4 import BeautifulSoup

# reload(sys)
# sys.setdefaultencoding('utf-8')
target_feed_list = ['BTDDongge', 'oh-hard', 'SXM-Capital', 'wallstreetcn']
# dir_name = time.strftime('%Y-%m-%d', time.localtime())
dir_name = '2018-10-20'
os.chdir('html')
# os.mkdir(dir_name)
os.chdir(dir_name)
for item in target_feed_list:
    html_file = open(item + '.html', 'r', encoding="utf-8")
    html_page = html_file.read()
    soup = BeautifulSoup(html_page, 'lxml')
    last_post_published_at = soup.select('.feed_body .timestamp')[0].string.strip()
    print(item+'最后更新：'+last_post_published_at)
    # today = time.strftime("%Y-%m-%d", time.localtime())
    today = '2018-10-20'
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
