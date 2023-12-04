from aiogram.filters import CommandStart
from aiogram import types, Router
from loader import dp
from aiogram.utils.markdown import hbold

start_router=Router()

@start_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}')
    kb=[
        [types.KeyboardButton(text='Я робот'),
         types.KeyboardButton(text='Я не робот')],
        [types.KeyboardButton(text='Робот, но мне сказали что я не робот')]
    ]

    keyboard=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='Введите заметку')

    await message.answer(text='Привет, путник', reply_markup=keyboard)