
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart
from aiogram.types import Message
import requests


from config import TOKEN, API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_weather(city: str, api_key: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Отправь мне название города, и я покажу тебе текущую погоду.")

# Обработчик текстовых сообщений для получения прогноза погоды
@dp.message(F.text)
async def weather_report(message: Message):
    city = message.text.strip()
    weather_data = get_weather(city, API_KEY)

    if weather_data.get("cod") != 200:
        await message.answer("Не удалось получить данные о погоде. Пожалуйста, убедитесь, что вы ввели правильное название города.")
        return

    city_name = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"].capitalize()


    weather_report = (
        f"Погода в городе {city_name}:\n"
        f"Температура: {temperature}°C\n"
        f"Описание: {description}\n"

    )

    await message.answer(weather_report)
# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

