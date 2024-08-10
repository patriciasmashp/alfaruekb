from aiogram.types import InlineKeyboardButton, \
    InlineKeyboardMarkup, \
    KeyboardButton, \
    ReplyKeyboardMarkup
from loguru import logger
from callback_data import PaginateCallback, PaginateAct


class PaginateKeyboard():

    def get(
        enitities,
        page=1,
        max_page=1,
    ) -> list:
        inline_kb = []

        for enity in enitities:
            inline_kb.append([
                InlineKeyboardButton(
                    text=str(enity),
                    callback_data=PaginateCallback(act=PaginateAct.set,
                                                   set_id=enity.id).pack())
            ])

        if max_page != 1:
            if page == max_page:
                inline_kb.append([
                    InlineKeyboardButton(text="←",
                                         callback_data=PaginateCallback(
                                             act=PaginateAct.prev,
                                             current=page).pack()),
                    InlineKeyboardButton(text=f"{page}/{max_page}",
                                         callback_data="_"),
                ])
            elif page == 1:
                inline_kb.append([
                    InlineKeyboardButton(text=f"{page}/{max_page}",
                                         callback_data="_"),
                    InlineKeyboardButton(text="→",
                                         callback_data=PaginateCallback(
                                             act=PaginateAct.next,
                                             current=page,
                                         ).pack()),
                ])
            else:
                inline_kb.append([
                    InlineKeyboardButton(text="←",
                                         callback_data=PaginateCallback(
                                             act=PaginateAct.prev,
                                             current=page,
                                         ).pack()),
                    InlineKeyboardButton(text=f"{page}/{max_page}",
                                         callback_data="_"),
                    InlineKeyboardButton(text="→",
                                         callback_data=PaginateCallback(
                                             act=PaginateAct.next,
                                             current=page,
                                         ).pack()),
                ], )
        return inline_kb


class ControllPaginateKeyBoard(PaginateKeyboard):

    def get(enitities, page=1, max_page=1):

        kb = PaginateKeyboard.get(enitities, page, max_page)
        kb.append([InlineKeyboardButton(text="Добавить", callback_data="add")])
        return kb


class Keyboard():

    def main_menu_kb(admin: bool = False):
        kb = [
            [
                KeyboardButton(text="Ассортимент")
                
            ],
            [
                KeyboardButton(text="Ассортимент ")
            ],
        ]
        if admin:
            kb.append([KeyboardButton(text="Админ панель")])

        greet_kb = ReplyKeyboardMarkup(resize_keyboard=False, keyboard=kb)
        return greet_kb

    def order_service():
        inline_kb = [[
            InlineKeyboardButton(text="Заказать услугу",
                                 callback_data=f"order_service")
        ]]

        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb

    def send_phone():
        kb = [
            [
                KeyboardButton(text="Отправить номер телефона",
                               request_contact=True)
            ],
        ]

        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
        return greet_kb

    def faq_kb(faqs):

        kb = []

        for question in faqs:
            kb.append([KeyboardButton(text=question.name)])

        kb.append([KeyboardButton(text="Назад")])
        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
        return greet_kb

    def starts():
        inline_kb = [[
            InlineKeyboardButton(text="1️⃣", callback_data=f"1"),
            InlineKeyboardButton(text="2️⃣", callback_data=f"2"),
            InlineKeyboardButton(text="3️⃣", callback_data=f"3"),
            InlineKeyboardButton(text="4️⃣", callback_data=f"4"),
            InlineKeyboardButton(text="5️⃣", callback_data=f"5")
        ]]

        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb

    def y_n_kb():
        inline_kb = [[
            InlineKeyboardButton(text="Да", callback_data=f"y"),
            InlineKeyboardButton(text="Нет", callback_data=f"n"),
        ]]

        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb

    def admin_menu():
        kb = [[
            KeyboardButton(text="Опубликовать новость"),
            KeyboardButton(text="Обратная связь")
        ],
              [
                  KeyboardButton(text="Управление услугами"),
                  KeyboardButton(text="Просмотр заказов"),
              ],
              [
                  KeyboardButton(text="Блокировка пользователя"),
                  KeyboardButton(text="Написать пользователю")
              ],
              [
                  KeyboardButton(text="Вопросы FAQ"),
                  KeyboardButton(text="Назад")
              ]]

        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
        return greet_kb

    def services_controll():
        inline_kb = [[
            InlineKeyboardButton(text="Удалить", callback_data=f"delete"),
            InlineKeyboardButton(text="Добавить фото",
                                 callback_data=f"add_photos"),
        ]]

        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb

    def news_is_ready():
        inline_kb = [
            [
                InlineKeyboardButton(text="Опубликовать",
                                     callback_data=f"publish")
            ],
            [InlineKeyboardButton(text="Отменить", callback_data=f"cancel")],
        ]

        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb

    def orders_list(
        orders,
        page=1,
        max_page=1,
    ):
        inline_kb = []

        for order in orders:
            # user = await se
            inline_kb.append([
                InlineKeyboardButton(text=order.user_obj.username,
                                     callback_data=f"set_order={order.id}")
            ])

        if max_page != 1:
            if page == max_page:
                inline_kb.append([
                    InlineKeyboardButton(text="←",
                                         callback_data=f"orders_prev_page"),
                    InlineKeyboardButton(text=f"{page}/{max_page}",
                                         callback_data=f"_"),
                ])
            elif page == 1:
                inline_kb.append([
                    InlineKeyboardButton(text=f"{page}/{max_page}",
                                         callback_data=f"_"),
                    InlineKeyboardButton(text="→",
                                         callback_data=f"orders_next_page"),
                ])
            else:
                inline_kb.append([
                    InlineKeyboardButton(text="←",
                                         callback_data=f"orders_prev_page"),
                    InlineKeyboardButton(text=f"{page}/{max_page}",
                                         callback_data=f"_"),
                    InlineKeyboardButton(text="→",
                                         callback_data=f"orders_next_page"),
                ], )
        inline_kb.append(
            [InlineKeyboardButton(text="Назад", callback_data=f"back")])
        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb

    def back():
        inline_kb = [
            [InlineKeyboardButton(text="Назад", callback_data=f"back")],
        ]

        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb

    def categories_kb(categories):
        kb = []

        for category in categories:
            kb.append([
                InlineKeyboardButton(text=category.name,
                                     callback_data=category.name)
            ])

        # kb.append([InlineKeyboardButton(text="Назад", callback_data="back")])
        greet_kb = InlineKeyboardMarkup(inline_keyboard=kb)
        return greet_kb

    def categories_controll_kb(categories):
        kb = []

        for category in categories:
            kb.append([
                InlineKeyboardButton(text=category.name,
                                     callback_data=category.name)
            ])

        kb.append([
            InlineKeyboardButton(text="Добавить категорию",
                                 callback_data="add")
        ])

        greet_kb = InlineKeyboardMarkup(inline_keyboard=kb)
        return greet_kb

    def delete_button():
        inline_kb = [[
            InlineKeyboardButton(text="Удалить", callback_data=f"delete")
        ]]

        greet_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        return greet_kb
