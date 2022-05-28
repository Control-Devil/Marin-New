import os
import asyncio
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Raiden.events import register
from Raiden import telethn as borg
from Raiden import SUPPORT_CHAT

MARIN = "https://telegra.ph//file/497abaa888d0eac7edb39.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"Hey [{event.sender.first_name}](tg://user?id={event.sender.id})! I'm Raiden Shogun♡\nI'm here to manage your groups so give enough rights\nFor any doubts realated to Raiden come to the support by clicking the button below.\n\n"
  TEXT += "**Thanks for adding me in your group♡**"
  BUTTON = [[Button.url("Help", "https://t.me/ShogunXRobot?start=help"), Button.url("My Home", "https://t.me/HayasakaXSupport")]]
  await borg.send_file(event.chat_id, MARIN, caption=TEXT,  buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(event):
    Nobara = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Click The Button Below To Get My Repo**\n\n"
    BUTTON = [[Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/HayasakaXSupport"), Button.url("ʀᴇᴘᴏ", "https://t.me/HayasakaXSupport")]]
    await borg.send_file(event.chat_id, file="https://telegra.ph//file/3343f0b78909dc7c8a5f8.jpg", caption=Nobara, buttons=BUTTON)
