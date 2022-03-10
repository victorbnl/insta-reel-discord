#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import discord
import re
from yt_dlp import YoutubeDL
import glob
import os

bot = discord.Client()

@bot.event
async def on_ready():
    print("Ready")

@bot.event
async def on_message(message):
    matches = re.match("https:\/\/www\.instagram\.com\/reel\/(\w*)", message.content)

    # If link is Instagram reel
    if matches:
        name = matches[1]

        # Create folder reel if it doesn't exist
        if not os.path.exists("reel"):
            os.makedirs("reel")

        # Download it
        with YoutubeDL({"outtmpl": "reel/{}.%(ext)s".format(name)}) as ytdl:
            ytdl.download([matches[0]])

        # Get filename (extension is unknown)
        path = glob.glob("reel/{}.*".format(name))[0]

        # Send it
        with open(path, "rb") as file_:
            await message.channel.send(file=discord.File(file_))

        # Delete it
        os.remove(path)

with open("token.txt", "r") as file_:
    token = file_.read()

bot.run(token)
