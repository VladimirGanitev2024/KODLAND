import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    with open('images/2.jpg', 'rb') as file:
        picture = discord.File(file)
    await ctx.send(file=picture)

bot.run('MTIyNDM5ODQ4MzkxODk0NjM0NA.GyeC9f._AbSIeXRR5t2trrXDcue8mtb8AxgpvJJ_6EJ6A')