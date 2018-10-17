#!/usr/bin/python
# -*- coding: UTF-8 -*-

# encoding=utf8

import sys
import json
import csv

enc = sys.getdefaultencoding()

f = open("./posts.txt", "r", encoding=enc)
research_list = []
for x in f:
    load_dict = json.loads(x)

    if 'content' in load_dict.keys():
        research_list.append({
            'title': load_dict['title'],
            'abstract': load_dict['digest'],
            'content': load_dict['content'],
            'author_name': 'ADMIN',
            'origin': load_dict['link']
        })
        enc = sys.getdefaultencoding()
        with open('test.csv', 'a',encoding=enc) as target_file:
            csv_writer = csv.writer(target_file,delimiter=",",quotechar='"')
            csv_writer.writerow([load_dict['title'], load_dict['digest'], load_dict['content'],
                                "ADMIN", load_dict['link']])

