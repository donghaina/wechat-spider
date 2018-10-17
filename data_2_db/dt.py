import json
from datetime import datetime

json_str = {
    "createdAt": {
        "$date": "2018-08-28T04:09:59.092Z"
    }
}
load_dict = json.loads(json.dumps(json_str))

created_at_str = load_dict['createdAt']['$date']

print(created_at_str)
# dt_str = datetime(2018, 8, 28, 4, 9,59)
dt_str = datetime(int(created_at_str[0:4]),
                  int(created_at_str[5:7]),
                  int(created_at_str[8:10]),
                  int(created_at_str[11:13]),
                  int(created_at_str[14:16]),
                  int(created_at_str[17:19]))
print(dt_str)
created_at = dt_str.timestamp()

print(int(created_at))
print(1535400599)