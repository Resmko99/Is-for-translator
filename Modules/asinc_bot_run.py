import configparser
from telebot.async_telebot import AsyncTeleBot
from telebot import types

config = configparser.ConfigParser()
config.read('config.ini')
token = config.get('Team_token', 'token')

bot = AsyncTeleBot(token)

subscribers_config = configparser.ConfigParser()
subscribers_config.read('subscribers.ini')

user_steps = {}


@bot.message_handler(commands=['start'])
async def start_command(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подписаться на рассылку")
    button2 = types.KeyboardButton(text="Отписаться от рассылки")
    keyboard.add(button1, button2)

    user_chat_id = str(message.chat.id)
    if user_chat_id in subscribers_config['subscribers']:
        await bot.send_message(message.chat.id,
                               'Вы уже подписаны на нашу рассылку. Если вы хотите отписаться, просто нажмите на кнопку.',
                               reply_markup=keyboard)
    else:
        await bot.send_message(message.chat.id,
                               'Вы еще не подписаны на нашу рассылку. Если хотите подписаться, просто нажмите на кнопку.',
                               reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
async def process_user_reply(message):
    user_chat_id = str(message.chat.id)
    if message.text == 'Подписаться на рассылку':
        if user_chat_id not in subscribers_config['subscribers']:
            await add_subscriber(user_chat_id)
            await bot.send_message(user_chat_id, 'Вы подписались на рассылку.')
        else:
            await bot.send_message(user_chat_id, 'Вы уже подписаны на рассылку.')

    elif message.text == 'Отписаться от рассылки':
        if user_chat_id in subscribers_config['subscribers']:
            await remove_subscriber(user_chat_id)
            await bot.send_message(user_chat_id, 'Вы отписались от рассылки.')
        else:
            await bot.send_message(user_chat_id, 'Вы уже отписаны от рассылки.')


async def add_subscriber(chat_id):
    subscribers_config.set('subscribers', chat_id, '')
    with open('subscribers.ini', 'w') as configfile:
        subscribers_config.write(configfile)


async def remove_subscriber(chat_id):
    subscribers_config.remove_option('subscribers', chat_id)
    with open('subscribers.ini', 'w') as configfile:
        subscribers_config.write(configfile)

bot.polling(none_stop=True)