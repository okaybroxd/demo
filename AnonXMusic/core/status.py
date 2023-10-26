import os
import asyncio
import datetime
import pytz
import config
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.errors import FloodWait

load_dotenv()

app = Client(name="st_userbot",
             api_id=config.API_ID,
             api_hash=config.API_HASH,
             session_string=str(config.STRING1)

bot = Client(name="st_bot",
             api_id=config.API_ID,
             api_hash=config.API_HASH,
             bot_token=config.BOT_TOKEN

BOT_LIST = [x.strip() for x in os.getenv("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = config.SUPPORT_CHANNEL
MESSAGE_ID = config.SUPPORT_CHAT
TIME_ZONE = "DL/In"

OWNER_ID = None
if id:=config.OWNER_ID:
    OWNER_ID = int(id)

bot.start()


async def main():
    print("Status Checker Bot Started")
    async with app:
        while True:
            TEXT = "This is the live bot status of all Bots 🤖"
            for bots in BOT_LIST:
                ok = await app.get_users(f"@{bots}")
                try:
                    await app.send_message(bots, "/statusbot")
                    await asyncio.sleep(2)
                    messages = app.get_chat_history(bots, limit=1)
                    async for x in messages:
                        msg = x.text
                    if msg == "/statusbot":
                        TEXT += f"\n\n🤖 - **[{ok.first_name}](tg://openmessage?user_id={ok.id}): ❌ Offline**"
                        if OWNER_ID:
                            await bot.send_message(OWNER_ID, f'Alert {ok.first_name} is offline 💀')
                    else:
                        TEXT += f"\n\n🤖 - **[{ok.first_name}](tg://openmessage?user_id={ok.id}): ✅ Online**\n ┗ **{msg}**"
                    await app.read_chat_history(bots)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            date = time.strftime("%d %b %Y")
            time = time.strftime("%I:%M: %p")
            TEXT += f"\n\n--Last checked on--: \n{date}\n{time} ({TIME_ZONE})\n\n**Refreshes Automatically After Every 15 Min.**"
            await bot.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID,
                                        TEXT)
            await asyncio.sleep(900)


bot.run(main())
