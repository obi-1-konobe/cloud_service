import random
import json
import requests
from datetime import datetime

date_time = "{:%d/%m/%Y %H:%M:%S}".format(datetime.now())
temperature = round(random.uniform(35.0, 37.0), 1)
heartbeat = random.randint(110, 140)

data = {
    'datetime': date_time,
    'temperature': f'{temperature}',
    'heartbeats': f'{heartbeat}'
}
data_json = json.dumps(data)
payload = {'payload': data_json}
r = requests.post('http://localhost:8000/', data=data_json)
print(r)
