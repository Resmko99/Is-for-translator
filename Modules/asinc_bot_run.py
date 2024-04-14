import os
import telebot
import psycopg2
import configparser
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import asyncio

config = configparser.ConfigParser()
config.read('config.ini')

# Читаем файл config.ini
config.read(os.path.join(os.path.dirname(__file__), '..', 'Source', 'config.ini'))

# Получаем значения из файла
db_user = config.get('database', 'user')
db_password = config.get('database', 'password')
db_host = config.get('database', 'host')
db_name = config.get('database', 'name')

conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host
)
cursor = conn.cursor()
cursor.execute("SELECT bot_id FROM Teams")
bot_id = cursor.fetchone()[0]
token = bot_id

bot = AsyncTeleBot(token)

subscribers_config = configparser.ConfigParser()
subscribers_config.read('subscribers.ini')

async def read_publication():
    if 'publish.txt' not in os.listdir():
        return None
    with open('publish.txt', 'r') as fp:
        lines = fp.readlines()
    os.remove('publish.txt')
    return lines

class FileHandler(FileSystemEventHandler):
    async def on_created(self, event):
        if event.src_path.endswith('publish.txt'):
            contents = await read_publication()
            if contents is not None:
                for chat_id in subscribers_config['subscribers']:
                    await bot.send_message(chat_id, contents[0])
                    await bot.send_photo(chat_id, contents[1])

@bot.message_handler(commands=['start'])
async def start_command(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подписаться на рассылку")
    button2 = types.KeyboardButton(text="Отписаться от рассылки")
    keyboard.add(button1, button2)

    user_chat_id = str(message.chat.id)
    if user_chat_id in subscribers_config['subscribers']:
        await bot.send_message(message.chat.id,
                               'Вы уже подписаны на нашу рассылку.',
                               reply_markup=keyboard)
    else:
        await bot.send_message(message.chat.id,
                               'Вы еще не подписаны на нашу рассылку. Если хотите подписаться, просто нажмите на кнопку.',
                               reply_markup=keyboard)

async def main():
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

asyncio.run(main())