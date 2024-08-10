from create_bot import bot, dp
import logging
import sys
import asyncio

from database.base import generate_tables
from database.create_engine import engine, sessionmaker

from middleweare import DbSessionMiddleware
from routes.commands import router as commands_router
# from utils import init_menu_helper
from config import DEBUG
from utils.utils import register_routers


# Генерация таблиц
# asyncio.run(generate_tables(engine))

# Загрузка данных
# asyncio.run(load_data())
async def main():

    register_routers()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))

    await dp.start_polling(bot)


if __name__ == "__main__":
    if DEBUG == 1:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    else:
        logging.basicConfig(level=logging.INFO, filename="logs.log")
    asyncio.run(main())
