from aiogram import Dispatcher, types
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete, sql_command_get_all_ids
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def pin(message: types.Message):
    if message.chat.type == "supergroup":
        if message.from_user.id not in ADMINS:
            await message.answer("Hey baby, you're not an admin yet!")
        else:
            await bot.pin_chat_message(message.chat.id,
                                       message.message_id,
                                       message.reply_to_message)

async def dice(message: types.Message):
    a = await bot.send_dice(message.from_user.id, emoji='🎲')
    b = await bot.send_dice(message.from_user.id, emoji='🎲')
    if a.dice.value > b.dice.value: await bot.send_message(message.from_user.id, "You lost, and the bot won 😔")
    elif a.dice.value == b.dice.value: await bot.send_message(message.from_user.id, "Draw 😳")
    else: await bot.send_message(message.from_user.id, "You win 🥳")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(dice, commands=['dice'])