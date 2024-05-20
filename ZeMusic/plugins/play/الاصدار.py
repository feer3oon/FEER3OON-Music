import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fd96f37c3371ecdd2607.jpg",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس فرعون
★᚜ اسم سورس : سورس فرعون

★᚜ نوع : ميوزك

★᚜ اللغه : اللغه العربيه ويدعم الانجليزيه 

★᚜ مجال العمل : بوتات تشغيل الموسيقى في الاتصال
★᚜ نظام التشغيل : كارولين بوت ميوزك
★᚜ الاصدار 2.0.14
★᚜ تاريخ التأسيس : 2024/2/2

★᚜ مؤسس سورس فرعون : [ 𝗙َِ𝗘َِ𝗘َِ𝗥3َِ𝗢َِ𝗢َِ𝗡 ┇ فــ͡ـࢪعـ๋͜‏ـوُن ](https://t.me/W_9_9_9)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᠻꫀꫀ𝘳3ꪮꪮꪀ ‌ 𝚂𝙾𝚄𝚁𝙲𝙴 ♟️", url=f"https://t.me/FEER3OON"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

