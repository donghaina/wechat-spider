# -*- coding=UTF-8 -*-
import requests
import json
import sys

enc = sys.getdefaultencoding()
with open("./posts.json", "rt", encoding=enc) as f:
    data = json.load(f)
    r = requests.post('http://ufutx.horizon/api/wx/research', data)

    response_text = json.loads(r.text)
    if response_text['code'] == 1:
        print(response_text['msg'])
    else:
        print(response_text['msg'])