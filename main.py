import discord
import sys
import random
import platform
import time
import json
from datetime import datetime
import signal
import os
from discord.ext import commands

client = discord.Client()
date = datetime.now()
timestamp = date.strftime("%D - %H:%M:%S")

with open("config.json", "r+") as config:
  data = json.load("config")
  TOKEN = data["token"]

os.system("cls")
@client.event
async def on_ready():
    print("-------------------")
    print("Logged in as {}".format(client.user))
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} server & {len(client.users)} user || Prefix: s!"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
      await message.channel.send("Hi!")
        
client.run(TOKEN)