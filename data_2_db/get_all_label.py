import json
import sys
import requests


def get_keyword_list():
    enc = sys.getdefaultencoding()
    with open("./lablel.txt", "rt", encoding=enc) as f:
        for x in f:
            load_dict = json.loads(x)
            r = requests.post('https://www.aikepler.com/api/wx/keyword', {
                'keyword': load_dict['title']
            })
            response_text = json.loads(r.text)
            if response_text['code'] == 1:
                print(response_text['msg'])
            else:
                print(response_text['msg'])
                continue


get_keyword_list()
