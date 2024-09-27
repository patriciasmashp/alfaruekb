from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from loguru import logger
from sqlalchemy.ext.asyncio.session import AsyncSession
from database.models import User
from keyboards import Keyboard
import texts
from utils.utils import get_user_by_id

router = Router(name="commands")


@router.message(Command("start"))
async def start(message: Message, session: AsyncSession):
    user = await get_user_by_id(message.from_user.id)

    text = texts.welcome_msg
    if user:
        kb = Keyboard.main_menu_kb(user.is_admin)
    else:
        kb = Keyboard.main_menu_kb(False)

    if user:
        await message.answer(text, reply_markup=kb)
        return

    user = User()
    user.first_name = message.from_user.first_name
    user.tg_id = str(message.from_user.id)
    user.username = message.from_user.username
    if message.from_user.last_name:
        user.last_name = message.from_user.last_name

    session.add(user)
    await session.commit()
    await message.answer(text, reply_markup=kb)
    return
