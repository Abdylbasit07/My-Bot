from aiogram import Dispatcher, types
from config import bot, ADMINS
from random import choice

emoji = choice('⚽,''🏀,''🎲,''🎯,''🎳,''🎰')



async def extra(message: types.Message):
    if message.text == "game":
        if message.from_user.id not in ADMINS:
            await message.answer("You're not an admin!")
        else:
            await bot.send_dice(message.chat.id, emoji=emoji)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(extra)