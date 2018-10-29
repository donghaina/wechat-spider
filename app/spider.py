from .models import Feed
from .models import FeedSchema
from .models import Post
from .models import PostSchema
from app import db
import requests
import os
import time
import pymysql


# 获取整个页面的HTML
def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url=url, headers=headers, timeout=5)
    return response.content


# 保存HTML页面到对应的文件夹
def save_html(file_path, file_content):
    with open(file_path + '.html', 'wb') as target_file:
        target_file.write(file_content)


# 指定目录创建文件夹
def mkdir(file_path):
    # 去除首位空格
    file_path = file_path.strip()
    # 去除尾部\符号
    file_path = file_path.rstrip('\\')
    # 判断路径是否存在
    is_exists = os.path.exists(file_path)

    if not is_exists:
        print(file_path + '创建成功')
        os.makedirs(file_path)
        return True
    else:
        print(file_path + '目录已存在')
        return False


def mk_target_dir(target_feed_list):
    os.chdir('app')
    os.chdir('html')
    dir_name = time.strftime('%Y-%m-%d', time.localtime())
    print(os.getcwd())
    mkdir(dir_name)
    os.chdir(dir_name)

    for item in target_feed_list:
        mkdir(item['wx_id'])

    path = os.path.dirname(__file__)
    for target_feed in target_feed_list:
        target_url = 'http://chuansong.me/account/' + target_feed['wx_id']
        target_html = get_html(target_url)
        target_path = path + '/html/' + dir_name + '/' + target_feed['wx_id']
        save_html(target_path, target_html)


def get_feed_list():
    feed_list = Feed.query.order_by(Feed.scraping_time).all()
    feed_schema = FeedSchema(many=True)
    target_feed_list = feed_schema.dump(feed_list)
    # mk_target_dir(target_feed_list)
    get_today_data(target_feed_list)
    print(target_feed_list)


def get_today_data(target_feed_list):
    from bs4 import BeautifulSoup
    dir_name = time.strftime('%Y-%m-%d', time.localtime())
    base_path = os.path.dirname(__file__) + '/html/' + dir_name + '/'
    for item in target_feed_list:
        html_file = open(base_path + item['wx_id'] + '.html', 'r', encoding="utf-8")
        html_page = html_file.read()
        soup = BeautifulSoup(html_page, 'lxml')
        last_post_published_at = soup.select('.feed_body .timestamp')[0].string.strip()
        print(item['wx_title'] + '最后更新：' + last_post_published_at)
        if last_post_published_at == dir_name:
            posts = soup.select('.feed_item_question')
            post_list = []
            for post in posts:
                post_title = post.select('.question_link')[0].string.strip()
                post_url = 'http://chuansong.me' + post.select('.question_link')[0]['href']
                post_published_at = post.select('.timestamp')[0].string.strip()
                if post_published_at == last_post_published_at:
                    post_list.append({'title': post_title,
                                      'url': post_url,
                                      'published_at': post_published_at,
                                      'wx_id': item['wx_id']})

            print(post_list)
            feed_record_list = []
            for record in post_list:
                feed_record_list.append(Post(title=record['title'], url=record['url'], wx_id=record['wx_id'], published_at=time.time()))
            db.session.add_all(feed_record_list)
            db.session.commit()


get_feed_list()
