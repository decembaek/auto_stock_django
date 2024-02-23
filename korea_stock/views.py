from django.shortcuts import render

# Create your views here.
from korea_stock.tasks import my_task, add
import asyncio


async def fetch_data():
    while True:
        # 비동기로 데이터를 가져오고 DB에 저장하는 로직
        print("Fetching data...")
        await asyncio.sleep(1)


fetch_data()
