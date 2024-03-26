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

    # добавьте в конец файла/класса следующий код

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


@bot.message_handler(commands=['register'])
def register(message):
    msg = bot.send_message(message.chat.id, "Введите ваш логин:")
    bot.register_next_step_handler(msg, process_login_step)

def process_login_step(message):
    user_login = message.text
    try:
        cursor.execute("SELECT * FROM users WHERE login = %s", (user_login,))
        user = cursor.fetchone()
        if user:
            bot.send_message(message.chat.id, "Этот логин уже занят, попробуйте другой.")
            return
        else:
            msg = bot.send_message(message.chat.id, 'Введите ваш пароль:')
            bot.register_next_step_handler(msg, process_password_step, user_login)
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)
        bot.send_message(message.chat.id, "Произошла внутренняя ошибка при проверке логина. Попробуйте позже.")
        conn.rollback()

def process_password_step(message, user_login):
    user_password = message.text
    try:
        # Transfer ownership of `is_password_unique` to this method to check password.
        cursor.execute("SELECT password FROM users WHERE password=%s", (user_password,))
        if cursor.fetchone():
            bot.send_message(message.chat.id, "Этот пароль уже используется, попробуйте другой.")
        else:
            msg = bot.send_message(message.chat.id, 'Введите ваш email:')
            bot.register_next_step_handler(msg, process_email_step, user_login, user_password)
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при проверке уникальности пароля:", error)
        bot.send_message(message.chat.id, "Произошла внутренняя ошибка при проверке пароля. Попробуйте позже.")
        conn.rollback()

def process_email_step(message, user_login, user_password):
    user_email = message.text
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (user_email,))
        user = cursor.fetchone()
        if user:
            bot.send_message(message.chat.id, "Этот email уже занят, попробуйте другой.")
            return
        else:
            cursor.execute("INSERT INTO users (login, password, email, chat_id) VALUES (%s, %s, %s, %s)",
                           (user_login, user_password, user_email, message.chat.id,))
            conn.commit()
            bot.send_message(message.chat.id, "Вы успешно зарегистрированы!")
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)
        bot.send_message(message.chat.id, "Произошла внутренняя ошибка при записи в базу данных. Попробуйте позже.")
        conn.rollback()

bot.polling(none_stop=True)