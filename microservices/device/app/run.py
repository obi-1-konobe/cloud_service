import random
import json
import requests
import time
from datetime import datetime, timedelta
import numpy as np
from patients import patients as p
import pandas as pd


# patient_ids = list()
# names = list()
# genders = list()
# doctors = list()
# wards = list()
# bunks = list()
# date_ins = list()
# date_times = list()
# temperatures = list()
# heartbeats = list()
# pressures = list()
# nrms = list()

# a = datetime(2020,6,3,0,1,2)

# for _ in range(1000):
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
        # date_time = "{:%d/%m/%Y %H:%M:%S}".format(a)

        temperature = round(random.uniform(35.0, 37.0), 1)
        heartbeat = int(np.random.normal(80, 5))
        pressure = int(np.random.normal(110, 5))
        nrm = int(np.random.normal(16, 2))

        # patient_ids.append(patient_id)
        # names.append(name)
        # genders.append(gender)
        # doctors.append(doctor)
        # wards.append(ward)
        # bunks.append(bunk)
        # date_ins.append(date_in)
        # date_times.append(date_time)
        # temperatures.append(temperature)
        # heartbeats.append(heartbeat)
        # pressures.append(pressure)
        # nrms.append(nrm)

    # a += timedelta(0, 60)

# result = pd.DataFrame()
# result['patient_id'] = patient_ids
# result['name'] = names
# result['gender'] = genders
# result['doctor_name'] = doctors
# result['ward'] = wards
# result['bunk'] = bunks
# result['date_in'] = date_ins
# result['date_time'] = date_times
# result['temperature'] = temperatures
# result['heartbeat'] = heartbeats
# result['pressure'] = pressures
# result['nrm'] = nrms
#
# result.to_excel('indicators.xls')

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
        r = requests.post('http://localhost:8000/', data=data_json)
        print(r)
    time.sleep(3600)

