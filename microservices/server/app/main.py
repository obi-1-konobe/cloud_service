from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

storage = [
    {
        'datetime': '12/12/12 12:12:12',
        'heartbeats': '120',
        'temperature': '36.6'
    }
]


class Metrics(BaseModel):
    datetime: str
    heartbeats: str
    temperature: str


@app.get('/', response_model=List[Metrics])
async def index():
    return storage


@app.post('/', status_code=201)
async def add_movie(payload: Metrics):
    movie = payload.dict()
    storage.append(movie)
    return {'id': len(storage) - 1}
