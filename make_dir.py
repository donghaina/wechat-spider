import requests
import os
import time

target_feed_list = ['BTDDongge', 'oh-hard', 'SXM-Capital', 'wallstreetcn']
dir_name = time.strftime('%Y-%m-%d', time.localtime())


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url=url, headers=headers, timeout=5)
    return response.content


def save_html(file_path, file_content):
    with open(file_path + '.html', 'wb') as target_file:
        target_file.write(file_content)


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


os.chdir('html')
mkdir(dir_name)
os.chdir(dir_name)

for item in target_feed_list:
    mkdir(item)

path = os.path.dirname(__file__)
for target_feed in target_feed_list:
    target_url = 'http://chuansong.me/account/' + target_feed
    target_html = get_html(target_url)
    target_path = path + '/html/' + dir_name + '/' + target_feed
    save_html(target_path, target_html)
