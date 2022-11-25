from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from keyboards.client_kb import submit_markup, cancel_markup, direction_markup
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    name = State()
    id2 = State()
    direction = State()
    age = State()
    groupp = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in ADMINS:
            await FSMAdmin.name.set()
            await message.answer("Keep your name: ",
                                 reply_markup=cancel_markup)
        else:
            await message.answer("You're not my administrator!")
    else:
        await message.answer("Write to the PM")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Enter your ID: ")


async def load_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id2'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Your direction: ", reply_markup=direction_markup)
    except:
        await message.answer("Write clearly!")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("How old are you?")


async def load_age(message: types.Message, state: FSMContext):
    try:
        if 14 < int(message.text) < 50:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Your group?")
        else:
            await message.answer("Your age is not suitable!")
    except:
        await message.answer("Write clearly!")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['groupp'] = message.text
        await message.answer(
            f"Name - {data['name']}\n"
            f"ID - {data['id2']}\n"
            f"Direction - {data['direction']}\n"
            f"Age - {data['age']}\n"
            f"Group - {data['groupp']}\n"
            f"{data['username']}")
    await FSMAdmin.next()
    await message.answer("Is that right? Answer options: yes, no", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "yes":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Registration completed successfully!")
    elif message.text.lower() == "no":
        await state.finish()
        await message.answer("Cancel")
    else:
        await message.answer("Your answer is not accepted!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Cancel", reply_markup=submit_markup)


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_id, state=FSMAdmin.id2)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.groupp)
    dp.register_message_handler(submit, state=FSMAdmin.submit)