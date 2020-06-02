import random
import json
import requests
import time
from datetime import datetime
import numpy as np
from patients import patients as p


while True:
    for idx in p:
        patient_id = p[idx]['id']
        name = p[idx]['name']
        gender = p[idx]['gender']
        doctor = p[idx]['doctor_name']
        ward = p[idx]['ward']
        bunk = p[idx]['bunk']
        date_in = p[idx]['date_in']
        date_time = "{:%d/%m/%Y %H:%M:%S}".format(datetime.now())
        temperature = round(random.uniform(35.0, 37.0), 1)
        heartbeat = np.random.normal(80, 5)
        pressure = np.random.normal(110, 5)
        nrm = np.random.normal(16, 2)

        data = {
            'patient_id': patient_id,
            'name': name,
            'gender': gender,
            'doctor': doctor,
            'ward': ward,
            'bunk': bunk,
            'date_in': date_in,
            'date_time': date_time,
            'temperature': temperature,
            'heartbeat': heartbeat,
            'pressure': pressure,
            'nrm': nrm,
        }
        data_json = json.dumps(data)
        print(data_json)
        # payload = {'payload': data_json}
        # r = requests.post('http://89.208.228.166:8000/', data=data_json)
        r = requests.post('http://localhost:8000/', data=data_json)
        print(r)
    time.sleep(3600)
