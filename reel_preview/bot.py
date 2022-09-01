import discord
import os

from reel_preview import download


intents = discord.Intents.default()
intents.message_content = True


class ReelPreviewBot(discord.Client):

    def __init__(self):
        super().__init__(intents=intents)

    async def on_ready(self):
        print("Ready")

    async def on_message(self, message):

        # Check if message is downloadable URL
        # If so, get url and video id
        state, url, id = download.check_url(message.content)

        if state:

            # Download video
            path = download.download(url, id)

            # Send it
            with open(path, "rb") as file_:
                await message.channel.send(file=discord.File(file_))

            # Delete it
            os.remove(path)

            return
