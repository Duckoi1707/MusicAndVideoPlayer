import requests
from pyrogram import Client, filters

from config import HNDLR


@Client.on_message(filters.command(["truth"], prefixes=f"{HNDLR}"))
async def truth(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("Lagi error truth nya")


@Client.on_message(filters.command(["dare"], prefixes=f"{HNDLR}"))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("Lagi error dare nya")

@Client.on_message(filters.command(["lyrics"], prefixes=f"{HNDLR}"))
async def lyrics(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("» **give a lyric name too.**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **tìm kiếm lời bài hát...**")
        resp = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("Lỗi **không tìm thấy kết quả của lời bài hát.**\n\n» **xin vui lòng cung cấp một tên bài hát hợp lệ.**")