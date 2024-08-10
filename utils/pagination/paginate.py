from loguru import logger
from sqlalchemy import func, select
from config import PAGES_SIZE
from keyboards import ControllPaginateKeyBoard, PaginateKeyboard
from utils.utils import pagination
from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from callback_data import PaginateAct, PaginateCallback
from sqlalchemy.ext.asyncio.session import AsyncSession


class Paginator():

    def __init__(
            self,
            enity,
            session,
            curent=None,
            custom_selection=None,
            num_entries=None,
            keyboard: PaginateKeyboard = ControllPaginateKeyBoard) -> None:
        if curent:
            self.current = curent
        else:
            self.current = 1
        self.offset = (self.current - 1) * PAGES_SIZE
        self.limit = PAGES_SIZE
        self.num_entries = num_entries
        self.enity = enity
        self.session: AsyncSession = session
        self.selected = None
        self.keyboard = keyboard
        self.custom_selection = custom_selection

    async def get(self):
        if self.num_entries:
            count = self.num_entries
        else:
            q = select(func.count(self.enity.id))
            count = await self.session.scalar(q)
        self.max_page = count // PAGES_SIZE
        if count % PAGES_SIZE:
            self.max_page += 1

        if self.custom_selection is None:
            enitities = await pagination(enity=self.enity,
                                         current=self.current,
                                         limit=self.limit,
                                         offset=self.offset)

            return enitities
        else:
            f, kwargs = self.custom_selection

            enitities = await f(limit=self.limit, offset=self.offset, **kwargs)

            return enitities

    async def process_select(self, query: CallbackQuery,
                             callback_data: PaginateCallback):
        if callback_data.act == PaginateAct.next:
            paginator = Paginator(self.enity,
                                  self.session,
                                  curent=callback_data.current + 1,
                                  num_entries=self.num_entries,
                                  custom_selection=self.custom_selection)
            enyties = await paginator.get()

            _kb = self.keyboard.get(enyties, callback_data.current + 1,
                                    paginator.max_page)
            kb = InlineKeyboardMarkup(inline_keyboard=_kb)
            await query.message.edit_reply_markup(reply_markup=kb)
            # await state.set_state(AdminStatesGroup.UsersControll.users_lsit)

        if callback_data.act == PaginateAct.prev:
            paginator = Paginator(self.enity,
                                  self.session,
                                  curent=callback_data.current - 1,
                                  num_entries=self.num_entries,
                                  custom_selection=self.custom_selection)
            enyties = await paginator.get()
            _kb = self.keyboard.get(enyties, callback_data.current - 1,
                                    paginator.max_page)
            kb = InlineKeyboardMarkup(inline_keyboard=_kb)
            await query.message.edit_reply_markup(reply_markup=kb)
            # await state.set_state(AdminStatesGroup.UsersControll.users_lsit)

        if callback_data.act == PaginateAct.set:
            await query.message.delete_reply_markup()
            await query.message.delete()
            return callback_data.set_id

    async def get_kb(self, entities=None):
        if entities is None:
            entities = await self.get()
        kb = self.keyboard.get(entities, self.current, self.max_page)

        return InlineKeyboardMarkup(inline_keyboard=kb)
