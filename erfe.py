from telethon import functions, types
from telethon import events
import asyncio
from time import sleep


@borg.on(events.NewMessage(pattern=r"\.loadgif", outgoing=True))
async def _(client):
    await exit()