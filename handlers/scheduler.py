from aiogram import Bot, Dispatcher
import datetime
from database.bot_db import sql_command_get_id_name
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from config import bot


async def birthday_day(bot:Bot):
    users = await sql_command_get_id_name()
    for user in users:
        await bot.send_message(user[0],f'День рождение твоего друга {user[1]}')


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
        birthday_day,
        trigger=DateTrigger(
            run_date=datetime.datetime(
                year=2023,month=3,day=27,hour=20,minute=39,second=0
            )
        ),
        kwargs={'bot':bot}
    )
    scheduler.start()
