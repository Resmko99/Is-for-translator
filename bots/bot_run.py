import os
import random
import string
import psycopg2
from psycopg2 import Error
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import configparser
from telebot import TeleBot

# Парсим конфигурационный файл
config = configparser.ConfigParser()
config.read(os.path.join('src', 'config.ini'))
bot_token = config['telegram']['token']
db_user = config['database']['user']
db_password = config['database']['password']
db_host = config['database']['host']
db_name = config['database']['name']

# Создаем бота
bot = TeleBot(bot_token)

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

# Бот приветствует пользователя
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    itembtn1 = InlineKeyboardButton('Регистрация', callback_data="reg")
    itembtn2 = InlineKeyboardButton('Восстановить пароль', callback_data="forgot")
    markup.add(itembtn1, itembtn2)

    bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "forgot")
def forgot(call):
    sent = bot.send_message(call.message.chat.id, 'Введите логин вашей учетной записи:')
    bot.register_next_step_handler(sent, process_forgot_step)

def process_forgot_step(message):
    user_login = message.text
    password = get_unique_password()
    try:
        cursor.execute("UPDATE \"User\" SET password = %s WHERE login = %s", (password, user_login,))

        conn.commit()
        bot.send_message(message.chat.id, f"Ваш новый пароль: {password}")
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)
        bot.send_message(message.chat.id, "Произошла внутренняя ошибка при попытке обновить пароль. Повторите попытку.")
        conn.rollback()

def get_unique_password():
    while True:
        password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        cursor.execute("SELECT * FROM \"User\" WHERE password = %s", (password,))
        result = cursor.fetchone()
        if not result:
            return password

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "reg":
            sent = bot.send_message(call.message.chat.id, 'Введите ваш логин:')
            bot.register_next_step_handler(sent, process_login_step)

def process_login_step(message):
    user_login = message.text
    cursor.execute("SELECT * FROM \"User\" WHERE login = %s", (user_login,))
    result = cursor.fetchone()
    if result:
        bot.reply_to(message, 'Этот логин уже занят. Пожалуйста, введите другой логин.')
    else:
        sent = bot.send_message(message.chat.id, 'Введите ваш пароль:')
        bot.register_next_step_handler(sent, process_password_step, user_login)

def process_password_step(message, user_login):
    user_password = message.text
    sent = bot.send_message(message.chat.id, 'Введите адрес вашей электронной почты:')
    bot.register_next_step_handler(sent, process_email_step, user_login, user_password)

def process_email_step(message, user_login, user_password):
    user_email = message.text
    cursor.execute("SELECT * FROM \"User\" WHERE email = %s", (user_email,))
    result = cursor.fetchone()
    if result:
        bot.reply_to(message, 'Этот адрес электронной почты уже используется. Пожалуйста, введите другой.')
    else:
        cursor.execute("INSERT INTO \"User\" (login, password, email) VALUES (%s, %s, %s)",
                       (user_login, user_password, user_email,))
        conn.commit()
        bot.send_message(message.chat.id, 'Вы успешно зарегистрировались!')

bot.polling(none_stop=True)