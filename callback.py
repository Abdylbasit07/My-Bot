from aiogram import Dispatcher, types
from config import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    call_button_2 = InlineKeyboardButton("NEXT", callback_data='call_button_2')
    markup.add(call_button_2)


    ques = "By whom invented Python?"
    answer = [
        'Bjorn Stroustrup',
        'Guido Van Rossum',
        'Scott Wiltamut and Anders Heilsberg',
        'James Gosling',
        'Mitchell Reznik',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        correct_option_id=1,
        type="quiz",
        is_anonymous=False,
        explanation="Do you write in Python and don't know the founder of the language?",
        reply_markup=markup
    )

async def quiz3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    call_button_3 = InlineKeyboardButton("NEXT", callback_data="call_button_3")
    markup.add(call_button_3)

    ques = "When is Abdylbasit's birthday?"
    answer = [
        'February 30',
        'January 1st',
        'December 15th',
        'September 23',
        'May 8th',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        correct_option_id=2,
        type='quiz',
        is_anonymous=False,
        open_period=10,
        reply_markup=markup
    )
 


 
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    call_button_4 = InlineKeyboardButton("NEXT", callback_data="call_button_4")
    markup.add(call_button_4)

    ques = "How long did World War 1 last?"
    answer = [
        '4 years',
        '3 years',
        '7 years',
        '1 year',
        '10 years',
        '5 years',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        correct_option_id=0,
        type='quiz',
        is_anonymous=False,
        open_period=20,
        reply_markup=markup
    )

async def quiz5(call: types.CallbackQuery):

    ques = "Who was the first President of Kyrgyzstan?"
    answer = [
        'Ishenbai Kadyrbekov',
        'Sadyr Zhaparov',
        'Kanatbek Isaev',
        'Roza Otunbayeva',
        'Almazbek Atambayev',
        'Askar Akayev',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        correct_option_id=5,
        type='quiz',
        is_anonymous=False,
        open_period=10
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz4, lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(quiz5, lambda call: call.data == "button_call_4")