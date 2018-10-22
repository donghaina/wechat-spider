import os
import time

target_feed_list = ['BTDDongge', 'html', 'SXM-Capital', 'wallstreetcn']
dir_name = time.strftime('%Y-%m-%d',time.localtime())

os.mkdir(dir_name)
os.chdir(dir_name)

for item in target_feed_list:
    os.mkdir(item)
