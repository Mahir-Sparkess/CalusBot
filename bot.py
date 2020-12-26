# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = str(os.getenv('PREFIX'))

bot = commands.Bot(command_prefix=PREFIX)

@bot.command(help='pong!')
async def ping(ctx: commands.Context):
    await ctx.send('Pong!')


@bot.command(name = 'announce', help = 'announce <message>: Send an announcemet of Calus')
async def announcement(ctx, message):
    await ctx.send(message)

@bot.event
async def on_ready():
    
    for guild in bot.guilds:
        if guild.id == GUILD:
            break
        
    print(
        f'{bot.user} has connected to the following guild: '
        f'{guild.name}(id: {guild.id})'
    )

bot.run(TOKEN)