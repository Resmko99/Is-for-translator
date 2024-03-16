import os
import random
import string
import psycopg2
from psycopg2 import Error
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import configparser
from telebot import TeleBot

config = configparser.ConfigParser()
config.read(os.path.join('src', 'config.ini'))
bot_token = config['telegram']['token']
db_user = config['database']['user']
db_password = config['database']['password']
db_host = config['database']['host']
db_name = config['database']['name']

bot = TeleBot(bot_token)

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

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Сообщите мне свой логин, если вы забыли пароль.")

def is_password_unique(password: str) -> bool:
    try:
        cursor.execute("SELECT password FROM users WHERE password=%s", (password,))
        if cursor.fetchone():
            return False
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)
        conn.rollback()

    return True


def generate_password():
    while True:
        password_length = 12
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(symbols),
        ]

        all_chars = letters + digits + symbols
        for i in range(3, password_length):
            password.append(random.choice(all_chars))

        random.shuffle(password)
        password = ''.join(password)

        if is_password_unique(password):
            return password


def handle_text(message):
    user_login = message.text
    new_password = generate_password()
    try:
        cursor.execute("SELECT * FROM users WHERE login = %s", (user_login,))
        user = cursor.fetchone()
        if user:
            cursor.execute("UPDATE users SET password = %s WHERE login = %s", (new_password, user_login))
            conn.commit()
            bot.send_message(message.chat.id, f"Ваш новый пароль: {new_password}")
        else:
            bot.send_message(message.chat.id,
                           "Пользователь с таким логином не найден. Пожалуйста, проверьте ваш логин.")
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)
        conn.rollback()


bot.polling(none_stop=True)