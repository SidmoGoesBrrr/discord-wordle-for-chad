import aiohttp
import sys

import asyncio
import time
import nextcord
from nextcord.ext import commands, tasks
import random
import os
import requests
import re
import datetime
from PIL import Image, ImageFont, ImageDraw
import math
from io import BytesIO
import typing
intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
from discord_slash import SlashCommand
from discord_slash import cog_ext, SlashContext
slash = SlashCommand(bot)

bot.remove_command('help')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")

        except commands.ExtensionError as e:
            print(f'{e.__class__.__name__}: {e}')

@bot.event
async def on_ready():
    print("Yay online")
    await bot.change_presence(activity=nextcord.Game('Lets Bully Sid N Jason')
        )
    
@bot.command()
async def reload(ctx,cog):
	bot.reload_extension(f"cogs.{cog}")
	await ctx.send("Ok nub")




    
token = "ODcwNTE0MTM3OTQyMzU1OTc4.YQN3dw.mLVpqfadffDKFo024eBLPFGmNvo"
bot.run(token)