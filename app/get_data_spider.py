from .models import Feed
from .models import FeedSchema
from .models import Post
from .models import PostSchema
from app import db
import requests
import os
import time
import pymysql
from lxml.html.clean import Cleaner
import jieba
from jieba import analyse
from bs4 import BeautifulSoup
import re


# 获取网页
def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url=url, headers=headers, timeout=5)
    return response.content


# 获取HTML正文
def get_post_content(html_page):
    cleanr = re.compile('<.*?>')
    soup = BeautifulSoup(html_page, 'lxml')
    post_content = str(soup.find('div', class_="rich_media_content"))
    post_content_text = re.sub(cleanr, '', post_content)
    return post_content, post_content_text


# 提取文章关键词
def get_post_keywords(text):
    textrank = analyse.textrank
    keyword_list = textrank(text, topK=30)
    return ','.join(keyword_list)


# 获取所有的公众号
def get_feed_list():
    feed_list = Feed.query.order_by(Feed.scraping_time).all()
    feed_schema = FeedSchema(many=True)
    target_feed_list = feed_schema.dump(feed_list)
    get_today_data(target_feed_list)


# 获取今天所有公众号更新的文章
def get_today_data(target_feed_list):
    # today = time.strftime('%Y-%m-%d', time.localtime())
    today = '2018-10-26'

    for item in target_feed_list:
        html_page = get_html('http://chuansong.me/account/' + item['wx_id'])
        soup = BeautifulSoup(html_page, 'lxml')
        last_post_published_at = soup.select('.feed_body .timestamp')[0].string.strip()
        if last_post_published_at == today:
            posts = soup.select('.feed_item_question')
            post_list = []
            for post in posts:
                post_published_at = post.select('.timestamp')[0].string.strip()
                if post_published_at == last_post_published_at:
                    post_title = post.select('.question_link')[0].string.strip()
                    post_url = 'http://chuansong.me' + post.select('.question_link')[0]['href']
                    post_content = get_post_content(get_html(post_url))
                    html_content = post_content[0]
                    text_content = post_content[1]
                    keywords = get_post_keywords(post_title + text_content)
                    post_list.append({'title': post_title,
                                      'url': post_url,
                                      'text': text_content,
                                      'html': html_content,
                                      'keywords': keywords,
                                      'wx_id': item['wx_id']})
            print('post_list', len(post_list))
            save_to_db(post_list)
            return post_list


# 将数据保存到数据库
def save_to_db(post_list):
    record_list = []
    for record in post_list:
        record_list.append(
            Post(title=record['title'],
                 url=record['url'],
                 text=record['text'],
                 html=record['html'],
                 keywords=record['keywords'],
                 wx_id=record['wx_id'],
                 published_at=time.time()))
    print('record_list', len(record_list))
    db.session.add_all(record_list)
    db.session.commit()


start_time = time.time()
get_feed_list()
end_time = time.time()
print('获取今日数据总耗时：', end_time - start_time)
