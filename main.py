from aiogram import Bot,Dispatcher,types
import asyncio
token = "Pogodaintheworld_bot"

main_m = types.ReplyKeyboardMarkup()
add_city = types.KeyboardButton(text="Добавить город")

bot = Bot(token=token)
dp = Dispatcher()


async def message_hadler(mes: types.Message):
