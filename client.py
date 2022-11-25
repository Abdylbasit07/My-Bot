from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random


async def mem1(message: types.message):
    photo = open("media/mmeeemmms.webp", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def mem2(message: types.message):
    photo = open("media/haha.webp", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def mem3(message: types.message):
    photo = open("media/ooo.webp", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    call_button_1 = InlineKeyboardButton("NEXT", callback_data="call_button_1")
    markup.add(call_button_1)

    ques = "Year of release of the programming language 'Python'?"
    answer = [
        '1985',
        '1990',
        '1981',
        '1991',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=ques, 
        
        options=answer,
        correct_option_id=3,
        type="quiz",
        is_anonymous=False,
        explanation="Do you write in Python and don't know the year of release?",
        reply_markup=markup
    )

async def get_random_user(message: types.Message):
    await sql_command_random(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(mem1, commands=['mem1'])
    dp.register_message_handler(mem2, commands=['mem2'])
    dp.register_message_handler(mem3, commands=['mem3'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
