import requests
import json
response = requests.get('https://api.github.com/events')

json_array = json.loads(response.text)

# for item in json_array:
#     for item_key in item.keys():
#         print(item_key)

for item_key in json_array[0].keys():
    print(item_key)