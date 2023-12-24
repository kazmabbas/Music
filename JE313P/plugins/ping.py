import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://graph.org/file/74485f30f6b76b038146e.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Repethone"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/Repethone")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
