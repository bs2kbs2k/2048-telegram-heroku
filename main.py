import os
from aiogram import *

bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher(bot)

@dp.inline_handler()
async def send_game(inline_query: types.InlineQuery):
    await bot.answer_inline_query(inline_query.id,
                                  [InlineQueryResultGame(id=str(uuid4()), 
                                                         game_short_name='the2048')])

@dp.callback_query_handler(func=lambda callback_query: \
    callback_query.game_short_name == 'the2048')
async def send_welcome(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://bs2kbs2k.github.io/2048/')