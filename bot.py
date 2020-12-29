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


@bot.command(name = 'announce', help = '<subject> <message>: Send an announcemet of Calus', pass_context=True)
@commands.has_role("Founders")
async def announcement(ctx, subject, message):

    embed = discord.Embed(title=str(subject).title(), colour=discord.Colour(0xf5cb23), description=str(message))

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/396299187916111872/792467220059652096/1-1.jpg")
    embed.set_author(name="Emperor Calus", icon_url="https://cdn.discordapp.com/attachments/396299187916111872/792467645894361088/release-season-of-opulence.png")
    embed.set_footer(text="Clap for me or face execution, Guardian")

    getchannel = discord.utils.get(ctx.guild.channels, name="announcements-of-calus")
    channel = bot.get_channel(getchannel.id)

    await channel.send(embed=embed)

@bot.command(name = 'message', help = '<channel> <message>: Send a message to a specific channel', pass_context = True)
@commands.has_role("Founders")
async def message(ctx,channel,message):

    embed = discord.Embed(title="", colour=discord.Colour(0xf5cb23), description=str(message))

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/396299187916111872/792467220059652096/1-1.jpg")
    embed.set_author(name="Emperor Calus", icon_url="https://cdn.discordapp.com/attachments/396299187916111872/792467645894361088/release-season-of-opulence.png")
    embed.set_footer(text="Clap for me or face execution, Guardian")

    getchannel = discord.utils.get(ctx.guild.channels, name=str(channel))
    channel = bot.get_channel(getchannel.id)

    await channel.send(embed=embed)

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