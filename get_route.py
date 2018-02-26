import json
import requests

zufang = 'http://127.0.0.1:5000/zufang/'
rrr = requests.get(zufang)
route_list = rrr.json().get('GIO').get('gio_list')[1:]

route = dict()
[route.update(dict(x=x)) for x in route_list]

with open('route_list', 'w') as f:
    f.write(json.dumps(route))
