import bs4
import requests
from aiogram import Bot,Dispatcher,types,executor
import sqlite3

conn = sqlite3.connect("pogoda")
cur = conn.cursor()

token = "5964365949:AAHCk4qPSpRkhLEkZ10CjPswy_gpBeb2ksk"
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands=['start'])
async def message_hadler(mes: types.Message):
    await bot.send_message(mes.from_user.id,text="Привет! Напиши город")
@dp.message_handler()
async def message_hadler(mes: types.Message):
    src = bs4.BeautifulSoup(requests.get(f"https://translate.yandex.ru/?from=tableau_yabro&source_lang=ru&target_lang=en&text={mes}").text)
    await bot.send_message(mes.from_user.id,src)



if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
