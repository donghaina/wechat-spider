#!/usr/bin/python
from datetime import datetime
import mysql.connector
import json
import sys
import time


def connect_database():
    my_database = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='root',
        database='horizon'
    )
    return my_database


def get_timestamp(date_str):
    dt_str = datetime(int(date_str[0:4]),
                      int(date_str[5:7]),
                      int(date_str[8:10]),
                      int(date_str[11:13]),
                      int(date_str[14:16]),
                      int(date_str[17:19]))
    return dt_str.timestamp()


def get_research_list():
    research_list = []
    enc = sys.getdefaultencoding()
    f = open("./posts.txt", "r", encoding=enc)
    for x in f:
        load_dict = json.loads(x)
        created_at_str = load_dict['createdAt']['$date']
        created_at = get_timestamp(created_at_str)
        research_list.append((load_dict.get('title', 'title'),
                              load_dict.get('digest', 'digest'),
                              load_dict.get('content', 'content'),
                              'ADMIN',
                              load_dict.get('link', 'link'),
                              1,
                              int(created_at),
                              int(created_at),
                              ''))

    return research_list


def insert_to_database():
    my_db = connect_database()
    my_cursor = my_db.cursor()
    data = get_research_list()
    print(data[0])
    for item in data:
        # print(item)
        sql = "INSERT INTO research (title,abstract,content,author_name,origin,is_public,created_at,published_at,keyword_id_list) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            my_cursor.execute(sql, item)
        except:
            print("Something went wrong when writing to the file")
            continue
        finally:
            pass

    my_db.commit()


start_time = time.time()
print('开始于' + str(start_time))

# my_db = connect_database()
# print(my_db)
# my_cursor = my_db.cursor()
# print(my_cursor)

# data = get_research_list()
# sql = "INSERT INTO research (title,abstract,content,author_name,origin,is_public,created_at,published_at,keyword_id_list) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# my_cursor.execute(sql, data[0])
# my_db.commit()
# print(len(data))
# print(data[1][6])
# connect_database()
insert_to_database()
end_time = time.time()
print('结束于' + str(end_time))
print('总耗时' + str(end_time - start_time) + 's')
