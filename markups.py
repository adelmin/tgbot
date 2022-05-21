from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton('Профиль')
btnWeather = KeyboardButton('Погода')
btnCurrency = KeyboardButton('Курс валют')
btnCharts = KeyboardButton('Чарты')
btnSub = KeyboardButton('Мои подписки')
crncyUsd = KeyboardButton('USD')
crncyEur = KeyboardButton('EUR')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile, btnWeather, btnCurrency, btnCharts, btnSub)
currencysubmenu = ReplyKeyboardMarkup(resize_keyboard = True)
currencysubmenu.add(crncyUsd, crncyEur)