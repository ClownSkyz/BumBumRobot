import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/10e1db9efda97bfc232c3.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), this 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭.** \n\n"
  TEXT += "💠 **I'm Working Management Groups!** \n\n"
  TEXT += f"💠 **Bot Maker : [Randov](https://t.me/FvckMiaw)** \n\n"
  TEXT += f"💠 **Library Version :** `{telever}` \n\n"
  TEXT += f"💠 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"💠 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me.. I Will Safety Your Groups ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/MusicTv_Bot?start=help"), Button.url("Support", "https://t.me/Grup_Cari_Teman_Virtual")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
