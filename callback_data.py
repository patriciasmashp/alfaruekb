from enum import Enum
from typing import Optional
from aiogram.filters.callback_data import CallbackData


class PaginateAct(str, Enum):
    next = "next_page"
    prev = "prev_page"
    set = "set"
    add = "add"


class PaginateCallback(CallbackData, prefix="paginate"):
    act: PaginateAct
    set_id: Optional[int] = None
    current: Optional[int] = None
    max_page: Optional[int] = None
    offset: Optional[int] = None
    # limit: int = None
