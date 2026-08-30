from aiogram import Bot, Dispatcher, F
import asyncio
import logging
import os
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
SITE_URL = "https://hanoi-tower-site.vercel.app"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart)
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ссылка на страницу", url=SITE_URL)]
        ]
    )

    await message.answer(
        "Привет! Я бот, который даст тебе ссылку на сайт решения ханойской башни. Жми на кнопку, чтобы перейти:",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)


if __name__=="__main__":
    asyncio.run(main())