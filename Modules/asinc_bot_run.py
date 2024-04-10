from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiopg import create_pool
import configparser
import os

# Парсим конфигурационный файл
config = configparser.ConfigParser()
config.read(os.path.join('Source', 'config.ini'))
bot_token = config['telegram']['token']
db_user = config['database']['user']
db_password = config['database']['password']
db_host = config['database']['host']
db_name = config['database']['name']

# Создаем бота
bot = Bot(bot_token)

# Создаем диспетчер событий
dp = Dispatcher(bot)

# Startup notification
async def on_startup_notify(dp):
    # Define here the Chat ID where you want the message to be sent
    await bot.send_message(YOUR_CHAT_ID, 'Бот запущен')

# Создаем пул соединений с БД
async def on_startup(dp):
    await on_startup_notify(dp)  # Calling the startup notification function
    dp['db_pool'] = await create_pool(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
     )


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = InlineKeyboardMarkup()
    itembtn1 = InlineKeyboardButton('Регистрация', callback_data="reg")
    itembtn2 = InlineKeyboardButton('Восстановить пароль', callback_data="forgot")
    itembtn3 = InlineKeyboardButton('Создать команду', callback_data="team")
    markup.add(itembtn1, itembtn2, itembtn3)

    await bot.send_message(message.chat.id, "Ваш Chat ID: {}".format(message.chat.id))
    await bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)