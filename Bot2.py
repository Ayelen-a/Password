import discord 

from discord.ext import commands
from D import gen_d

intents = discord.Intents.default()
intents.message_content = True

bot =commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def Datos_sobre_la_contaminacion(ctx):
    await ctx.send(gen_d())

@bot.command()
async def Hola(ctx):
    await ctx.send("Hola este bot te proporciona informacion sobre la contaminacion, escribe informacion para obtener los comandos disponibles.")

@bot.command()
async def informacion(ctx):
    await ctx.send("Comandos:Datos_sobre_la_contaminacion")

bot.run("token")
