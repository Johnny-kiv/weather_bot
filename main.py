from aiogram import Bot,Dispatcher,types
import asyncio
from sql import addInBaze


token = "Pogodaintheworld_bot"

main_m = types.ReplyKeyboardMarkup()
add_city = types.KeyboardButton(text="Добавить город")
look_city = types.KeyboardButton(text="Посмотреть города")
main_m.add(add_city)

bot = Bot(token=token)
dp = Dispatcher()

async def message_hadler(mes: types.Message):
    if mes == "Добавить город":
        pass
