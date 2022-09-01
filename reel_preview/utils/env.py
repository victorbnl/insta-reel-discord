from os import environ

from dotenv import load_dotenv


load_dotenv()


def get(key):
    return environ[f'REEL_PREVIEW_BOT_{key}']
