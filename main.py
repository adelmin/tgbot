import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from db import Database

TOKEN = "5152226735:AAGWnW_LvBrVXKI0MWxrwxqBkulViEeJexk"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваш ник")
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!", reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Профиль':
            user_nickname = "Ваш ник: " + db.get_nickname(message.from_user.id)
            await bot.send_message(message.from_user.id, user_nickname)
        elif message.text == 'Погода':
            await bot.send_message(message.from_user.id, "Погода", reply_markup=nav.mainMenu)
            pass
        elif message.text == 'Курс валют':
            await bot.send_message(message.from_user.id, "Курс валют", reply_markup=nav.currencysubmenu)
            pass
        elif message.text == 'Чарты':
            await bot.send_message(message.from_user.id, "Выберете", reply_markup=nav.mainMenu)
            pass
        elif message.text == 'Мои подписки':
            await bot.send_message(message.from_user.id, "Ваши подписки", reply_markup=nav.mainMenu)
            pass
        else:
            if db.get_signup(message.from_user.id) == "setnickname":
                if (len(message.text) > 15):
                    await bot.send_message(message.from_user.id, "Дли никнейма не должна превышать 15 символов")
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрещённый символ")
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, "done")
                    await bot.send_message(message.from_user.id, "Регистрация прошла успешно", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "Привет!", reply_markup=nav.mainMenu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
