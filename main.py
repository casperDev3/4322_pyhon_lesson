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
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6477583316:AAGRySJYkGA1fS5x_2mO-agnp9GoPps3NoU"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


# --- REPLY MENU MARKUP ---
def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Про нас🤭")],
            [KeyboardButton(text="test2"), KeyboardButton(text="test3")]
        ],
        resize_keyboard=True
    )
    return kb


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


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
