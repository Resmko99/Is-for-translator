import os
import telebot
import configparser
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import asyncio
import chardet


config = configparser.ConfigParser()
config.read('config.ini')

bot = AsyncTeleBot('6465024310:AAEIV_rs8fNU-ecfyULfSr0X2Zpi5NSNgdQ')

subscribers_config = configparser.ConfigParser()
subscribers_config.read('subscribers.ini')
path_to_watch = "C:\\Flud\\Is-for-translator\\front"
filename = os.path.join(path_to_watch, 'publish.txt')


def get_subscribers():
    return [item[0] for item in subscribers_config.items('subscribers')]


async def read_publication():
    filename = os.path.join(path_to_watch, 'publish.txt')
    if os.path.exists(filename):
        rawdata = open(filename, 'rb').read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']

        with open(filename, 'r', encoding=encoding) as fp:
            lines = fp.readlines()

        os.remove(filename)
        return lines
    else:
        print("Файл не найден.")
        return None


class FileHandler(FileSystemEventHandler):
    def __init__(self, loop):
        self.loop = loop

    def on_created(self, event):
        if event.src_path.endswith('publish.txt'):
            print("Обнаружен файл publish.txt")
            self.loop.create_task(self.handle_file())

    async def handle_file(self):
        contents = await read_publication()
        if contents is not None:
            print(f"Содержимое файла: {contents}")

            original_contents = contents.copy()
            upperCaseIndexes = [i for i, c in enumerate(contents[0]) if c.isupper() or c == "Ё"]
            contents[0] = contents[0].lower().replace("Ё", "ё")

            sent_message = ''.join(c.upper() if i in upperCaseIndexes else c for i, c in enumerate(contents[0]))

            for chat_id in get_subscribers():
                print(f"Отправка сообщения для {chat_id}")
                try:
                    with open(original_contents[1], 'rb') as photo:
                        await bot.send_message(chat_id, sent_message)
                        await bot.send_photo(chat_id, photo)
                except Exception as e:
                    print(f'Ошибка при отправке сообщения: {str(e)}')

        else:
            print("Файл пустой или не может быть прочитан")


@bot.message_handler(commands=['start'])
async def start_command(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подписаться на рассылку")
    button2 = types.KeyboardButton(text="Отписаться от рассылки")
    keyboard.add(button1, button2)

    user_chat_id = str(message.chat.id)
    if user_chat_id in get_subscribers():
        await bot.send_message(message.chat.id, 'Вы уже подписаны на нашу рассылку.', reply_markup=keyboard)
    else:
        await bot.send_message(message.chat.id,
                               'Вы еще не подписаны на нашу рассылку. Если хотите подписаться, просто нажмите на кнопку.',
                               reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Подписаться на рассылку')
async def subscribe_user(message):
    user_chat_id = str(message.chat.id)
    if user_chat_id in get_subscribers():
        await bot.send_message(message.chat.id, 'Вы уже подписаны на рассылку.')
    else:
        subscribers_config.set('subscribers', user_chat_id, '')
        with open('subscribers.ini', 'w') as configfile:
            subscribers_config.write(configfile)
        await bot.send_message(message.chat.id, 'Вы успешно подписались на рассылку.')


@bot.message_handler(func=lambda message: message.text == 'Отписаться от рассылки')
async def unsubscribe_user(message):
    user_chat_id = str(message.chat.id)
    if user_chat_id not in get_subscribers():
        await bot.send_message(message.chat.id, 'Вы уже отписаны от рассылки.')
    else:
        subscribers_config.remove_option('subscribers', user_chat_id)
        with open('subscribers.ini', 'w') as configfile:
            subscribers_config.write(configfile)
        await bot.send_message(message.chat.id, 'Вы успешно отписались от рассылки.')


async def main():
    loop = asyncio.get_running_loop()
    file_observer = Observer()
    file_observer.schedule(FileHandler(loop), path_to_watch)
    file_observer.start()

    try:
        await bot.polling(none_stop=True)
    finally:
        file_observer.stop()
        file_observer.join()


if __name__ == "__main__":
    asyncio.run(main())