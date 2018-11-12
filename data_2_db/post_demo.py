# -*- coding=UTF-8 -*-
import requests
import json
import sys

r = requests.post('http://ufutx.horizon/api/wx/keyword', {
    'keyword': '神经网络'
})

# print(r.text)
response_text = json.loads(r.text)
if response_text['code'] == 1:
    print(response_text['msg'])
