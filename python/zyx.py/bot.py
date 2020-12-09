import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)