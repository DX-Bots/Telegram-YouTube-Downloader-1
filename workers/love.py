"""
█████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░░░░░▄▀░░░░░░█░░░░▄▀░░██░░▄▀░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀▄▀░░▄▀▄▀░░███
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░░░▄▀▄▀▄▀░░░░███
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░█████████░░▄▀▄▀▄▀░░█████
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███████░░▄▀░░███████░░░░▄▀▄▀▄▀░░░░███
█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░███████░░▄▀▄▀░░▄▀▄▀░░███
█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░██░░▄▀░░░░░░█████░░▄▀░░█████░░░░▄▀░░██░░▄▀░░░░█
███░░░░▄▀░░░░███░░▄▀░░██░░▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀░░██░░▄▀▄▀░░█
█████░░░░░░█████░░░░░░██░░░░░░░░░░█████░░░░░░█████░░░░░░░░██░░░░░░░░█
█████████████████████████████████████████████████████████████████████
ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ
"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["love"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("💋LOVE💋:", url="https://t.me/vrtxmusic")],
    ])
    Aww = f"""Hey <b>{message.from_user.first_name}</b>
If you liked my project and want to be a GitHub contributor then:
- 📧You may email me at **mastermindvrtx@gmail.com**
- 📬You can personal message me in Telegram **@mastermindvrtx**   
- ✨Star & Fork my GitHub acct. and/or repo.\n

If you liked my project and want and just want to make me happy then you can:
- 🌹share my bot and make me happy 🌹
    
**<b>{message.from_user.first_name}</b> 😁Thanks a lot for using my bot🍰**

[ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ](https://telegra.ph/file/3f287a7ff7bd6d63fbd60.jpg)
"""
       
    await message.reply_text(Aww, reply_markup=joinButton)
    raise StopPropagation
