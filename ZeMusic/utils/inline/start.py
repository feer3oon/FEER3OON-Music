from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=" 𓆩  ضيفني 𓆪 ", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=" 𓆩  الدعم 𓆪 ", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=" 𓆩  ضيفني 𓆪 ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=" 𓆩  **الـاوامر** 𓆪 ", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=" 𓆩  👤 مطور البوت 𓆪 ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text=" 𓆩  الدعم 𓆪 ", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=" 𓆩  قناة المطور 𓆪 ", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=" 𓆩  قناة السورس 𓆪 ", url=f"https://t.me/FEER3OON"),
        ],
    ]
    return buttons
