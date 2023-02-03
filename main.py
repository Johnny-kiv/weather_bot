from aiogram import Bot,Dispatcher,types,executor
import sqlite3

conn = sqlite3.connect("pogoda")
cur = conn.cursor()

token = "5964365949:AAHCk4qPSpRkhLEkZ10CjPswy_gpBeb2ksk"

main_m = types.ReplyKeyboardMarkup()
add_city = types.KeyboardButton(text="Добавить город")
look_city = types.KeyboardButton(text="Посмотреть города")
main_m.add(add_city,look_city)

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def message_hadler(mes: types.Message):
    await bot.send_message(mes.from_user.id,text="Привет",reply_markup=main_m)

@dp.message_handler()
async def message_hadler(mes: types.Message):
    if mes.text == "Добавить город":
        await bot.send_message(mes.from_user.id,text="Напишите название города",reply_markup=main_m)
        choice_city(mes=mes.text)
def choice_city(mes):
    cur.execute(f"SELECT lat,lon from cities WHERE name = '{mes}'")
    res = cur.fetchall()
    print(res)
    #ot.send_message(mes.from_user.id, text=res, reply_markup=main_m)


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
