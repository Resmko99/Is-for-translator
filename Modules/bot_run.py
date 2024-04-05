import os
import random
import string
import psycopg2
import uuid
from psycopg2 import Error
import telebot
import configparser
from telebot.async_telebot import AsyncTeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from telebot import TeleBot
from telebot import types
from typing import Dict, Any



# Создаем объект configparser
config = configparser.ConfigParser()

# Читаем файл config.ini
config.read(os.path.join(os.path.dirname(__file__), '..', 'Source', 'config.ini'))

# Получаем значения из файла
bot_token = config.get('telegram', 'token')
db_user = config.get('database', 'user')
db_password = config.get('database', 'password')
db_host = config.get('database', 'host')
db_name = config.get('database', 'name')

# Создаем бота
bot = AsyncTeleBot(bot_token)

# Выполняем подключение к базе данных
try:
    conn = psycopg2.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )
    cursor = conn.cursor()
except (Exception, psycopg2.Error) as error:
    print("Ошибка при подключении к PostgreSQL:", error)

user_steps: Dict[str, Dict[str, Any]] = {}

@bot.message_handler(commands=['start'])
async def start_command(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Регистрация")
    button2 = types.KeyboardButton(text="Восстановить пароль")
    button3 = types.KeyboardButton(text="Создать команду")
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=keyboard)

user_steps: Dict[str, Dict[str, Any]] = {}


@bot.message_handler(func=lambda message: True)
async def echo_all(message):
    user_chat_id = str(message.chat.id)
    if user_chat_id in user_steps:  # Если существует chat_id в user_steps
        await process_next_step(message)  # Обрабатываем следующий шаг
    else:
        if message.text == 'Регистрация':
            user_steps[user_chat_id] = {'step': 'Регистрация логин'}
            await bot.send_message(user_chat_id, 'Введите ваш логин:')
        elif message.text == 'Восстановить пароль':
            user_steps[user_chat_id] = {'step': 'Восстановить логин'}
            await bot.send_message(user_chat_id, 'Введите логин вашей учетной записи для восстановления:')
        elif message.text == 'Создать команду':
            user_steps[user_chat_id] = {'step': 'Введите логин'}
            await bot.send_message(user_chat_id, 'Пожалуйста, введите ваш логин для проверки возможности создания команды:')

async def process_next_step(message):
    user_chat_id = str(message.chat.id)
    user_info = user_steps[user_chat_id]
    user_step = user_info['step']

    if user_step == 'Восстановить логин':
        user_login = message.text
        user_info['login'] = user_login
        cursor.execute("SELECT * FROM \"User\" WHERE \"login\" = %s AND \"chat_id\" = %s",
                       (user_login, message.chat.id,))
        result = cursor.fetchone()
        if not result:
            await bot.reply_to(message,
                               'Вы не являетесь владельцем данного аккаунта или пользователя с таким логином не существует.')
        else:
            user_info['step'] = 'Восстановить email'
            await bot.send_message(user_chat_id, 'Введите адрес электронной почты, связанный с этим аккаунтом:')

    elif user_step == 'Восстановить email':
        user_email = message.text
        user_info['email'] = user_email
        cursor.execute("SELECT * FROM \"User\" WHERE \"login\" = %s AND \"email\" = %s AND \"chat_id\" = %s",
                       (user_info['login'], user_email, user_chat_id,))
        result = cursor.fetchone()
        if not result:
            await bot.reply_to(message, 'Вы не являетесь владельцем данного аккаунта.')
        else:
            password = get_unique_password()
            try:
                cursor.execute("UPDATE \"User\" SET password = %s WHERE login = %s AND chat_id = %s AND email = %s",
                               (password, user_info['login'], user_chat_id, user_email,))
                conn.commit()
                del user_steps[user_chat_id]
                await bot.send_message(user_chat_id, f"Ваш новый пароль: {password}")
            except (Exception, psycopg2.Error) as error:
                print("Ошибка при работе с PostgreSQL:", error)
                await bot.send_message(user_chat_id,
                                       "Произошла внутренняя ошибка при попытке обновить пароль. Повторите попытку.")
                conn.rollback()

    elif user_step == 'Регистрация логин':
        user_login = message.text
        cursor.execute("SELECT * FROM \"User\" WHERE login = %s", (user_login,))
        result = cursor.fetchone()
        if result:
            await bot.reply_to(message, 'Этот логин уже занят. Пожалуйста, введите другой логин.')
        else:
            user_info['login'] = user_login
            user_info['step'] = 'Регистрация пароль'
            await bot.send_message(user_chat_id, 'Введите ваш пароль:')

    elif user_step == 'Регистрация пароль':
        user_password = message.text
        user_info['password'] = user_password
        user_info['step'] = 'Регистрация email'
        await bot.send_message(user_chat_id, 'Введите адрес вашей электронной почты:')

    elif user_step == 'Регистрация email':
        user_email = message.text
        cursor.execute("SELECT * FROM \"User\" WHERE email = %s", (user_email,))
        result = cursor.fetchone()
        if result:
            await bot.reply_to(message, 'Этот адрес электронной почты уже используется. Пожалуйста, введите другой.')
        else:
            cursor.execute("INSERT INTO \"User\" (login, password, email, chat_id) VALUES (%s, %s, %s, %s)",
                           (user_info['login'], user_info['password'], user_email, user_chat_id,))
            conn.commit()
            del user_steps[user_chat_id]
            await bot.send_message(user_chat_id, 'Вы успешно зарегистрировались!')

    elif user_step == 'Введите логин':
        user_login = message.text
        cursor.execute("SELECT * FROM \"User\" WHERE \"login\" = %s", (user_login,))
        user = cursor.fetchone()
        if not user:
            await bot.send_message(user_chat_id, 'Пользователь не определен. Введите логин.')
        else:
            user_category = user[6]  # Если 'category' это седьмой столбец в таблице.
            if user_category not in [1, 2]:  # Если категория не равна 1 или 2
                await bot.send_message(user_chat_id, 'У вас нет прав на создание команды.')
            else:
                user_step = 'Создание название команды'

    elif user_step == 'Создание название команды':
        team_name = message.text
        team_id = uuid.uuid1()
        try:
            cursor.execute("INSERT INTO \"Teams\" (team_id, name_team) VALUES (%s, %s)",
                           (str(team_id), team_name))  # Преобразуйте UUID в строку
            conn.commit()
            del user_steps[user_chat_id]
            await bot.send_message(user_chat_id, f'Вы создали команду с названием "{team_name}"!')
        except (Exception, psycopg2.Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
            await bot.send_message(user_chat_id,
                                   "Произошла ошибка при попытке создать команду. Попробуйте еще раз.")

def get_unique_password():
    while True:
        password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        cursor.execute("SELECT * FROM \"User\" WHERE password = %s", (password,))
        if not cursor.fetchone():
            return password



async def main() :
    await bot.polling(none_stop=True)

if __name__ == "__main__" :
    asyncio.run(main())