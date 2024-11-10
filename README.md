import discord, random
from bot_log import gen_pass
from bot_e import gen_emodji 
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

@bot.command()
async def emodji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
   
    image_url = get_duck_image_url()
    await ctx.send(image_url)
   


bot.run("token")

