import telebot
import asyncio
from telebot.async_telebot import AsyncTeleBot

BOT_TOKEN = '6403947351:AAHJ6BluQ2BvbI6cxomuImBpQmJqrLFmvH8'

bot = AsyncTeleBot('Сюда токен')

@bot.message_handler(commands=['start'])
async def start_command(message):
    welcome_msg = f"Привет, я бот для рассыки команд {message.from_user.first_name}!"
    await bot.send_message(message.chat.id, welcome_msg)


if __name__ == "__main__":
    asyncio.run(bot.polling(none_stop=True))