import os
import random
import string
import psycopg2
import uuid
from psycopg2 import Error
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import configparser
from telebot import TeleBot
from telebot import types

# Парсим конфигурационный файл
config = configparser.ConfigParser()
config.read(os.path.join('Source', 'config.ini'))
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

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    itembtn1 = InlineKeyboardButton('Регистрация', callback_data="reg")
    itembtn2 = InlineKeyboardButton('Восстановить пароль', callback_data="forgot")
    itembtn3 = InlineKeyboardButton('Создать команду',callback_data="team")
    markup.add(itembtn1, itembtn2, itembtn3)

    bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=markup)

   #Создание комманды, для этого используем две функции:
   #def team для создания комманды, а def process_team_step для вывода об
   #успешном создании комманды, в ином случае у пользователя не будет создаваться комманда
@bot.message_handler(commands=['team'])
def team(message):

    #Берём id чата и запоминаем его
    user_chat_id = message.chat.id

    #Подхватываем пользователя из базы данных
    cursor.execute("SELECT * FROM \"User\" WHERE chat_id = %s", (user_chat_id,))
    result = cursor.fetchone()

    #Проверка зарегестрирован ли пользователь
    if not result:
        bot.reply_to(message, 'Пользователь не зарегистрирован.')
    else:
        #Индексируем столбцы
        user_category = result[3]
        if user_category == 1:
            #Если пользователь прошёл проверку и он может создать команду
            sent = bot.send_message(message.chat.id, 'Введите название команды:')

            #Вызываем следующие шаги для регистрации комманды
            bot.register_next_step_handler(sent, process_team_step)
        else:
            #Если не прошёл проверку
            bot.reply_to(message, 'У вас нет прав на создание команды.')

#Создание команды, присвоение id, названия команды и отправка сообщения об успешном создании
def process_team_step(message):
    team_name = message.text
    user_chat_id = message.chat.id

    team_id = uuid.uuid1() #Присвоение уникального id команде

    #Типичная работа с базой данных
    try:
        cursor.execute("INSERT INTO \"Teams\" (team_id, name_team) VALUES (%s, %s)",
                       (team_id, team_name))
        conn.commit()

        #Сообщение об успешном создании
        bot.send_message(message.chat.id, f'Вы создали команду с названием "{team_name}"!')
    except (Exception, psycopg2.Error) as error:
        #Если ошибка
        print("Ошибка при работе с PostgreSQL:", error)
        bot.send_message(message.chat.id,
                         "Произошла внутренняя ошибка при попытке создать команду. Попробуйте еще раз.")
        conn.rollback()

#Восстановление пароля
@bot.callback_query_handler(func=lambda call: call.data == "forgot")
def forgot(call):
    sent = bot.send_message(call.message.chat.id, 'Введите логин вашей учетной записи:')
    bot.register_next_step_handler(sent, process_forgot_login_step)

def process_forgot_login_step(message):
    global user_login
    user_login = message.text
    user_chat_id = message.chat.id
    cursor.execute("SELECT * FROM \"User\" WHERE \"login\" = %s AND \"chat_id\" = %s", (user_login, user_chat_id,))
    result = cursor.fetchone()
    if not result:
        bot.reply_to(message, 'Вы не являетесь владельцем данного аккаунта или пользователя с таким логином не существует.')
    else:
        sent = bot.send_message(message.chat.id, 'Введите адрес электронной почты, связанный с этим аккаунтом:')

def process_forgot_email_step(message):
    user_email = message.text
    cursor.execute("SELECT * FROM \"User\" WHERE \"login\" = %s AND \"email\" = %s", (user_login, user_email))
    result = cursor.fetchone()
    if not result:
        bot.reply_to(message, 'Вы не являетесь владельцем данного аккаунта.')
    else:
        process_forgot_step(message)

def process_forgot_step(message):
    user_email = message.text
    password = get_unique_password()
    try:
        cursor.execute("UPDATE \"User\" SET password = %s WHERE login = %s AND chat_id = %s AND email = %s",
                       (password, user_login, message.chat.id, user_email))

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

#Регистрация
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
        user_chat_id = message.chat.id
        cursor.execute("INSERT INTO \"User\" (login, password, email, chat_id) VALUES (%s, %s, %s, %s)",
                       (user_login, user_password, user_email, user_chat_id,))
        conn.commit()
        bot.send_message(message.chat.id, 'Вы успешно зарегистрировались!')
        
        

bot.polling(none_stop=True)