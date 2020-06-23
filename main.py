import logging
import os

import falcon

from aiogram import (
    Bot,
    Dispatcher,
    executor,
    types,
)
from api.middleware import falcon_auth_middleware
from api.resources import (
    SignInResource,
    SignUpResource,
    NotiResource,
    UserResource,
    WelcomeResource,
)


def generic_error_handler(ex, req, resp, params):

    if isinstance(ex, falcon.HTTPNotFound):
        raise falcon.HTTPNotFound(description='Not Found')
    elif isinstance(ex, falcon.HTTPMethodNotAllowed):
        raise falcon.HTTPMethodNotAllowed(falcon.HTTP_405, description='Method Not Allowed')
    else:
        raise


app = falcon.API(middleware=[
    falcon_auth_middleware,
])

app.req_options.auto_parse_form_urlencoded = True

app.add_route('/', WelcomeResource())
app.add_route('/join', SignUpResource())
app.add_route('/login', SignInResource())
app.add_route('/users/me', UserResource())
app.add_route('/noti', NotiResource())
app.add_error_handler(Exception, generic_error_handler)

BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

# executor.start_polling(dp, skip_updates=True)

# async def
# message = 'Hi, This is push message!'
# await bot.send_message(470816817, message)
# logging.info(message)
