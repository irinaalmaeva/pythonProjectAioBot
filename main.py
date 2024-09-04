import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message: Message):
 list = ['https://pazlyigra.ru/uploads/posts/2023-06/5e7e61cd7b282.jpg', 'https://www.lotlike.ru/upload/iblock/299/001.JPG', 'https://rosesforyou.ru/wa-data/public/shop/products/64/04/464/images/411/411.970.jpg']
 rand_photo = random.choice(list)
 await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
 list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
 rand_answ = random.choice(list)
 await message.answer(rand_answ)
@dp.message(F.text == "Что такое бот?")
async def aitext(message: Message):
    await message.answer("Бот это такая программа, которая может выполнять команды")

@dp.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n /start \n /help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Я бот!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())