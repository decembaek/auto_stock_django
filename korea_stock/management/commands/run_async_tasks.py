from django.core.management.base import BaseCommand
import asyncio
from korea_stock.views import fetch_data

# async def fetch_data():
#     while True:
#         # 비동기로 데이터를 가져오고 DB에 저장하는 로직
#         print("Fetching data...")
#         await asyncio.sleep(1)


class Command(BaseCommand):
    help = "Runs async tasks"

    def handle(self, *args, **options):
        asyncio.run(self.run_async_tasks())

    async def run_async_tasks(self):
        await fetch_data()  # 여기에서 fetch_data는 앞서 정의한 비동기 함수
