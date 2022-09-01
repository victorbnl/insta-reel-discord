import os

from reel_preview.bot import ReelPreviewBot
from reel_preview.utils import env


# Create downloads folder if it doesn't exist
folder = 'downloads'
if not os.path.exists(folder):
    os.makedirs(folder)


# Get token
token = env.get('TOKEN')


# Run bot
bot = ReelPreviewBot()
bot.run(token)
