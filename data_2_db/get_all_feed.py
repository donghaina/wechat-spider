#!/usr/bin/python
from datetime import datetime
import pymysql
import json
import sys
import time
import wechatsogou
import random

ws_api = wechatsogou.WechatSogouAPI()


def connect_database():
    my_database = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='root',
        database='wechat_spider'
    )
    return my_database


def get_feed_list():
    enc = sys.getdefaultencoding()
    my_db = connect_database()
    my_cursor = my_db.cursor()
    sql = "INSERT INTO feed (wx_id,wx_title,scraping_time) VALUES (%s,%s,%s)"
    with open("./profiles.txt", "rt", encoding=enc) as f:
        for x in f:
            load_dict = json.loads(x)
            wx_title = load_dict['title']
            gzh_info = ws_api.get_gzh_info(wx_title)
            print(gzh_info)
            if gzh_info:
                try:
                    my_cursor.execute(sql, (gzh_info['wechat_id'], gzh_info['wechat_name'], '23:00:00'))
                    my_db.commit()
                    print(wx_title + '插入数据库')
                except:
                    print("Something went wrong when writing to the file")
                    continue
            time.sleep(random.randint(1, 10))


get_feed_list()
# my_db = connect_database()
# print(my_db)