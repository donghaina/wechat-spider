import requests


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url=url, headers=headers, timeout=5)
    return response.content


def save_html(file_name, file_content):
    # with open('./html/' + file_name + '.html', 'wb') as target_file:
    with open('./html/BTDDongge/' + file_name + '.html', 'wb') as target_file:
        target_file.write(file_content)


target_feed_list = ['BTDDongge', 'html', 'SXM-Capital', 'wallstreetcn']

for target_feed in target_feed_list:
    target_url = 'http://chuansong.me/account/' + target_feed
    target_html = get_html(target_url)
    save_html(target_url.split('/').pop(), target_html)

target_post_list = [{'title': '全球区块链早讯（10.17）', 'url': 'http://chuansong.me/n/2602994653214', 'published_at': '2018-10-17'}]

for target_post in target_post_list:
    target_url = target_post['url']
    target_html = get_html(target_url)
    save_html(target_url.split('/').pop(), target_html)