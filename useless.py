from pyrogram import Client, filters
from pyrogram.types import Message

@Useless.on_message(filters.text)
async def beinng_uselezz(c: Useless, m: Message):
    await m.reply("Welcome to the Oblivion of uselessness\n© by Mr. Useless")


Useless = Client(
    "Mr_Useless",
    api_id = info.API_ID,
    api_hash = info.API_HASH,
    bot_token = info.BOT_TOKEN
)

bot = Useless()
bot.run()
