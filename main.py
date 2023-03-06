from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import json

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! Raw Explorer is a Telegram bot that allows you to obtain the raw data of any message you have sent or received. This includes information such as the message ID, timestamp, and the IDs of the sender and receiver. You can use this data for analysis and to gain transparency.")


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def echo(message: types.Message):
    jsoninfo = (json.loads(str(message)))
    await message.answer(json.dumps(jsoninfo, sort_keys=True, indent=8))


if __name__ == '__main__':
    executor.start_polling(dp)
