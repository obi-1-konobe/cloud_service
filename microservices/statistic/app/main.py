import requests
from fastapi import FastAPI
from . import stat


app = FastAPI()


@app.get('/statistic/{device_id}')
async def get_device_indicators(device_id: int):
    # response = requests.get(f'http://89.208.228.166:8080/items/{device_id}/indicators')
    response = requests.get(f'http://localhost:8080/items/{device_id}/indicators')
    res_payload_dict = response.json()
    result = stat.count_stat(res_payload_dict)
    return result
