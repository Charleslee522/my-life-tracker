import json
import logging
import os
import asyncio

from falcon import (
    HTTP_204,
    after,
    before,
)
from aiogram import Bot

from api.hooks import (
    api_key,
    say_bye_after_operation,
)

BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)

from functools import wraps, partial

def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run 

async def func(message: str):
    user_id = 1
    await bot.send_message(user_id, message)

class NotiResource(object):

    def __init__(self):
        self.loop = asyncio.get_event_loop()

    def on_get(self, req, resp):
        logging.info('Noti')

        message = 'Hi, This is push message!'

        self.loop.run_until_complete(func(message))

        resp.status = HTTP_204

    def __del__(self):
        self.loop.close()
