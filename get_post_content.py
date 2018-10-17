# coding = utf-8
from bs4 import BeautifulSoup

# file_name = '2602994653214'


def get_post_content(file_name):
    html_file = open('./html/BTDDongge/' + file_name + '.html', 'r')
    html_page = html_file.read()
    soup = BeautifulSoup(html_page, 'lxml')
    post_content = soup.find_all(class_="rich_media_content")[0]
    return post_content


# print(get_post_content(file_name))
