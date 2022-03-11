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

regex = re.compile("https:\/\/www\.instagram\.com\/reel\/([a-zA-Z0-9_\-]*)")

@bot.event
async def on_message(message):
    matches = re.match(regex, message.content)

    # If link is Instagram reel
    if matches:
        name = matches[1]

        # Create folder reel if it doesn't exist
        if not os.path.exists("reel"):
            os.makedirs("reel")

        # Download it
        ytdl_opts = {
            "outtmpl": "reel/{}.%(ext)s".format(name),
            "cookiefile": "cookies.txt",
            "quiet": True
        }
        with YoutubeDL(ytdl_opts) as ytdl:
            try:
                ytdl.download([matches[0]])

            except Exception as error:
                await message.channel.send(error)
                return

        # Get filename (extension is unknown)
        path = glob.glob("reel/{}.*".format(name))[0]

        # Send it
        with open(path, "rb") as file_:
            await message.channel.send(file=discord.File(file_))

        # Delete it
        os.remove(path)

        return

with open("token.txt", "r") as file_:
    token = file_.read()

bot.run(token)
