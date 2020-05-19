import random
import json
import requests
import time
from datetime import datetime


devices = [1, 2]
while True:
    for idx in devices:
        device_id = idx
        date_time = "{:%d/%m/%Y %H:%M:%S}".format(datetime.now())
        temperature = round(random.uniform(35.0, 37.0), 1)
        heartbeat = random.randint(110, 140)

        data = {
            'device_id': device_id,
            'datetime': date_time,
            'temperature': temperature,
            'heartbeats': heartbeat
        }
        data_json = json.dumps(data)
        # payload = {'payload': data_json}
        r = requests.post('http://89.208.228.166:8000/', data=data_json)
        print(r)
    time.sleep(10)
