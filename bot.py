import discord
from bot_logic import gen_pass
from discord.ext import commands
import random
import os
from bot_logic import get_duck_image_url
from model import clasificador

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")
@bot.command()
async def bye(ctx):
    await ctx.send("😒")
@bot.command()
async def password(ctx, longitud = 10 ):
    await ctx.send(gen_pass(longitud))@bot.group()
@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
@cool.command(name='Luciana')
async def _Luciana(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the Luciana is cool.')
@bot.command()
async def mem(ctx):
    with open('images/meme_1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def meme_aleatorio(ctx):
    meme = random.choice(os.listdir("images"))
    with open(f'images/{meme}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attatchment in ctx.message.attachments:
            file_name = attatchment.filename
            file_url = attatchment.url
            await attatchment.save(f"./images/{file_name}")
            await ctx.send(clasificador(f"./images/{file_name}"))
    else:
        await ctx.send("No attachments were found in the message")
            
bot.run("Token")
