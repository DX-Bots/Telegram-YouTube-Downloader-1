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


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⛓**𝔾𝕣𝕠𝕦𝕡**⛓:", url="https://t.me/musicvrtx")],
        [InlineKeyboardButton("⚙️**⚙𝕌𝕡𝕕𝕒𝕥𝕖_ℂ𝕙𝕒𝕟𝕟𝕖𝕝**⚙️:", url="https://t.me/vrtxwork")],
        [InlineKeyboardButton("📨**𝔾𝕚𝕥ℍ𝕦𝕓**📨", url="https://t.me/vrtxwork")],
        [InlineKeyboardButton("🧬**𝕆𝕨𝕟𝕖𝕣**🧬", url="https://t.me/mastermindvrtx")],
    ])
    welcomed = f"""
    🎈Dear,
        Sir,Ma'am  <b>{message.from_user.first_name}</b>
    Use the below button or type /help for More info.
    [📥](https://telegra.ph/file/62e3a57990afe2d6da431.jpg)
    """
    
    
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
