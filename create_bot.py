from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN


bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

