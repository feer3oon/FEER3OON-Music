import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["فرعون","المبرمج فرعون","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fd96f37c3371ecdd2607.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝗙َِ𝗘َِ𝗘َِ𝗥3َِ𝗢َِ𝗢َِ𝗡 ┇ فــ͡ـࢪعـ๋͜‏ـوُن](https://t.me/FEER3OON)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @FEER3OON ❫
◉ 𝙸𝙳      : ❪ `6308685423` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@FEER3OON) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗙َِ𝗘َِ𝗘َِ𝗥3َِ𝗢َِ𝗢َِ𝗡 ┇ فــ͡ـࢪعـ๋͜‏ـوُن", url=f"https://t.me/FEER3OON"), 
                 ],[
                   InlineKeyboardButton(
                        "ᠻꫀꫀ𝘳3ꪮꪮꪀ ‌ 𝚂𝙾𝚄𝚁𝙲𝙴 ♟️", url=f"https://t.me/FEER3OON"),
                ],

            ]

        ),

    )
