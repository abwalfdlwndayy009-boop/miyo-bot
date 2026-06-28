import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = "8967421113:AAG8-DXwN82dx-gfVJxTBxC9iSMJWR_jW5k"
GROUP_ID = -1002070178350

async def send_miyo():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=GROUP_ID, text="میو")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_miyo, 'interval', seconds=360)
    scheduler.start()
    print("ربات شروع شد!")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
