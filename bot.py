
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


def main_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="🌐 WARP", callback_data="warp")
    kb.button(text="🛡 AmneziaWG", callback_data="awg")
    kb.button(text="⚙️ Настройки", callback_data="settings")
    kb.adjust(1)
    return kb.as_markup()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Привет! Это WARP Config Bot.\n\n"
        "Выбери нужный раздел:",
        reply_markup=main_keyboard()
    )


@dp.callback_query(F.data == "warp")
async def warp(callback: CallbackQuery):
    await callback.message.answer(
        "🌐 Раздел WARP\n\n"
        "Генерация настоящих рабочих конфигураций пока не подключена."
    )
    await callback.answer()


@dp.callback_query(F.data == "awg")
async def awg(callback: CallbackQuery):
    await callback.message.answer(
        "🛡 AmneziaWG\n\n"
        "Генератор конфигураций пока не подключён."
    )
    await callback.answer()


@dp.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery):
    await callback.message.answer(
        "⚙️ Настройки\n\n"
        "DNS и дополнительные параметры добавим следующим этапом."
    )
    await callback.answer()


async def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN в переменных окружения")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
