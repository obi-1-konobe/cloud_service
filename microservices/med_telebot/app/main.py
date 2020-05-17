from fastapi import FastAPI

from microservices.med_telebot.app.med_bot import run_bot

app = FastAPI()


@app.get('/{device_id}')
async def send_alarm(device_id: int):
    run_bot(device_id)
    return None