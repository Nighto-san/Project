from aiogram import Bot, Dispatcher, types

BOT_TOKEN = '6357485166:AAH0es0RiWJXp8gPOqI4jeFlLlzbKbXl5B8'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.on_message(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Это команда /start')

@dp.on_message()
async def echo_message(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)