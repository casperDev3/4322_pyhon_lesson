import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6477583316:AAGJ-3-vjxRhVmzAkaiFFHqkr95mtO15Hk4"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


# --- REPLY MENU MARKUP ---
def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Про нас🤭")],
            [KeyboardButton(text="Під-меню"), KeyboardButton(text="Inline Menu")]
        ],
        resize_keyboard=True
    )
    return kb


def r_sub_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Item1")],
            [KeyboardButton(text="Item2"), KeyboardButton(text="Item3")],
            [KeyboardButton(text="Item4"), KeyboardButton(text="Item5")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )
    return kb


# --- INLINE MENU ---
def i_test_menu():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Item1", callback_data="itm1"),
             InlineKeyboardButton(text="Item2", callback_data="itm2")],
            [InlineKeyboardButton(text="Show Sub Menu", callback_data="sub_menu")]
        ]
    )
    return kb


@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    chat_id = callback_query.from_user.id
    if data == "itm1":
        await bot.send_message(chat_id, "It's working!!")
    elif data == "sub_menu":
        await bot.send_message(chat_id, "This is submenu!", reply_markup=r_sub_menu())


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm live!", reply_markup=r_main_menu())


@dp.message()
async def reply_kb_handler(message: types.Message) -> None:
    msg = message.text
    cid = message.from_user.id
    if msg == "Про нас🤭":
        # await bot.send_message(cid, "Some Text")
        text = ("Adjust previously added buttons to specific row sizes.\n"
                "\n"
                "By default, when the sum of passed sizes is lower than buttons count the last one size will be used "
                "for tail of the markup. If repeat=True is passed - all sizes will be cycled when available more "
                "buttons count than all sizes")
        await message.answer(text)
    elif msg == "Під-меню":
        await message.answer("Ви перейшли в під меню!", reply_markup=r_sub_menu())
    elif msg == "Назад":
        await message.answer("Ви повернуль назад", reply_markup=r_main_menu())
    elif msg == "Inline Menu":
        await message.answer("Це приклад повідомлення з інлайн меню", reply_markup=i_test_menu())


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
