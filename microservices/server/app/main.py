import json
from typing import List
import requests
from fastapi import FastAPI
from models import IndicatorsIN, IndicatorsOUT

app = FastAPI()


@app.get('/', response_model=List[IndicatorsIN])
async def index():
    response = requests.get(f'http://89.208.228.166:8080/indicators')
    # response = requests.get(f'http://localhost:8080/indicators')
    res_payload_dict = response.json()
    return res_payload_dict


@app.post('/', status_code=201)
async def save_indicators(payload: IndicatorsOUT):
    print(123)
    indicators = payload.dict()
    # data = {
    #     'datetime': indicators["datetime"],
    #     'temperature': indicators["temperature"],
    #     'heartbeats': indicators["heartbeats"]
    # }
    data_json = json.dumps(indicators)
    requests.post(f'http://89.208.228.166:8080/items/{indicators["patient_id"]}/indicators', data=data_json)
    # requests.post(f'http://localhost:8080/items/{indicators["patient_id"]}/indicators', data=data_json)
    return None


@app.get('/patient/{patient_id}', response_model=List[IndicatorsIN])
async def get_device_indicators(patient_id: int):
    response = requests.get(f'http://89.208.228.166:8080/items/{patient_id}/indicators')
    # response = requests.get(f'http://localhost:8080/items/{patient_id}/indicators')
    res_payload_dict = response.json()
    return res_payload_dict


@app.get('/patient/{patient_id}/statistic')
async def get_devise_stat(patient_id: int):
    response = requests.get(f'http://89.208.228.166:8008/statistic/{patient_id}')
    # response = requests.get(f'http://localhost:8008/statistic/{patient_id}')
    res_payload_dict = response.json()
    return res_payload_dict
