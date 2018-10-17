#!/usr/bin/python

import mysql.connector
import json

research_list = []
with open("./document.json", "r") as load_f:
    load_dict = json.load(load_f)
    research_list = load_dict['data']

# print(research_list[0])
my_db = mysql.connector.connect(
    host='10.10.10.2',
    user='root',
    passwd='8ik,.lo9',
    database='horizon'
)

my_cursor = my_db.cursor(prepared=True)

# sql = sql = "INSERT INTO research (title,abstract,content,author_name,origin) VALUES (%s,%s,%s,%s,%s)"
# val = ('title', 'abstract', 'content', 'author_name', 'origin')
#
# my_cursor.execute(sql, val)
for index in range(len(research_list)):
    sql = "INSERT INTO research (title,abstract,content,author_name,origin) VALUES (%s,%s,%s,%s,%s)"
    val = (research_list[index]['title'], research_list[index]['digest'], research_list[index]['content'],
           research_list[index]['author_name'], research_list[index]['origin'])
    my_cursor.execute(sql, val)

my_db.commit()
