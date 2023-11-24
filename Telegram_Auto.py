import telegram
import asyncio
import schedule
import time
from datetime import datetime
import pytz

token = "6722824989:AAFcr_3QSlHeaRG3EHSl_WFZhYpU0CRWSw0"
bot = telegram.Bot(token=token)
chat_id = "-1002143232599"

async def send_message():
    now = datetime.now(pytz.timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")
    text = f'현재 시간: {now}'
    await bot.sendMessage(chat_id=chat_id, text=text)


def job():
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    if 6 <= now.hour < 23:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_message())



schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)