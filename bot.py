from aiogram import executor
from dispatcher import dp
import handlers

from db import BotDB

BotDB = BotDB("AAccountant.db")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
