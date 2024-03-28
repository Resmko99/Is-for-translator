import discord
from discord.ext import commands

# Префикс для обращения к боту
bot = commands.Bot(command_prefix="!")

@bot.command()
async def broadcast(ctx, *, message):
    # Список всех на сервере
    members = ctx.guild.members

    # Отправляем всем сообщение
    for member in members:
        if member != bot.user and not member.bot: # Исключаем бота из списка
            try:
                await member.send(message)
            except:
                print(f"Не получилось прислать сообщение пользователю: {member}")
                continue

# Запускаем бота
bot.run("Сюды токен бота")