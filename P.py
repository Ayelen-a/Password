import discord, random
from bot_log import gen_pass
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios

bot =commands.Bot(command_prefix="$",intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("HI!")

@bot.command()
async def bye(ctx):
    await ctx.send("😊")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))


bot.run("MTI5Njk4MzY1ODQyNjUzMTg0MA.GeTRXU._pmeNHey6gkM8g_jCHh7mJfGPUgEKY7mqR5Hvg")
