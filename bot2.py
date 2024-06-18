import main
import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Cześć!')

@bot.command()
async def bye(ctx):
    await ctx.send("\\U0001f642")
@bot.command()
async def haslo(ctx,lenght):
    await ctx.send (main.gen_pass(lenght))
@bot.command()
async def memes(ctx):
    nazwy- os.listdir("memes")
    nazwy = random.choise(nazwy)
    with open("images/"+'nazwy', 'rb') as f:
        picture = discord.File(f)
    with open ("memes/meme1.jpg","rb") as f:
        picture =discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def pomoc(ctx):
    await ctx.send ("możesz zacząć oszczędzać wodę","zbieraj śmieci w parkach lub rzekach w wolnym czasie","segreguj śmieci","oszczędzaj energie i wode","nie śmieć")
    random.choice (pomoc)
