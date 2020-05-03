import json
from typing import List
import requests
from fastapi import FastAPI
from models import IndicatorsIN, IndicatorsOUT

app = FastAPI()

# storage = [
#     {
#         'device_id': '12',
#         'datetime': '12/12/12 12:12:12',
#         'heartbeats': '120',
#         'temperature': '36.6'
#     }
# ]


@app.get('/', response_model=List[IndicatorsIN])
async def index():
    response = requests.get(f'http://localhost:8080/indicators')
    res_payload_dict = response.json()
    return res_payload_dict


@app.post('/', status_code=201)
async def save_indicators(payload: IndicatorsOUT):
    indicators = payload.dict()
    data = {
        'datetime': indicators["datetime"],
        'temperature': indicators["temperature"],
        'heartbeats': indicators["heartbeats"]
    }
    data_json = json.dumps(data)
    requests.post(f'http://localhost:8080/items/{indicators["device_id"]}/indicators', data=data_json)
    # return {'id': len(storage) - 1}


@app.get('/device/{device_id}', response_model=List[IndicatorsIN])
async def get_device_indicators(device_id: int):
    response = requests.get(f'http://localhost:8080/items/{device_id}/indicators')
    res_payload_dict = response.json()
    return res_payload_dict
