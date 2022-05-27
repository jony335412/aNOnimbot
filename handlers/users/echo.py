from aiogram import types

from loader import dp, bot


# Echo bot

s = 622550539

@dp.message_handler()
async def bot_echo(message: types.Message):
    id = message.from_user.id
    name = message.from_user.full_name
    user_id = message.from_user.username
    await bot.send_message(s, f"id: {id}\nusername: @{user_id}\nfrom: {name}\n\n{message.text}")