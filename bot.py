from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7555358150:AAHYXCXWwOcIsqqzkOsXXhoydFVmQ21QlDM"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я твой помощник. Напиши /help, чтобы узнать команды.")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("/add <дело> — добавить задачу\n/list — показать список дел")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
