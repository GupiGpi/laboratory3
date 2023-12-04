from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.handlers import message
from aiogram.utils.keyboard import InlineKeyboardBuilder

user_input_message = message.text

notes_router=Router()
@notes_router.message(Command('note'))
async def cmd_note(message:types.Message):
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='Заметка 1', callback_data='Click')
    )
    await message.answer('Чтобы изменить заметку, напишите ее в сообщении. Чтобы показать заметку, нажмите на кнопку:',reply_markup=builder.as_markup())

@notes_router.callback_query(F.data=='Click')
async def cmd_note(message:types.Message) -> None:
    await message.answer(user_input_message)