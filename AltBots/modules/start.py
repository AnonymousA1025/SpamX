from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10
xd = "[Zen BotX](https://t.me/ZenBotX)\n[BONTEN](https://t.me/Bonten_destroyers)"

START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ZenBotX"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/QuirkySquads"
        ),
    ],
    [
        Button.url(" ʙᴏɴᴛᴇɴ ᴅᴇsᴛʀᴏʏᴇʀs", "https://t.me/Bonten_Destroyers")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʟʟᴏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nᴛʜɪs ɪs [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"✗ **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ᴢᴇɴ](https://t.me/NoobZen)**\n\n"
        TEXT += f"✗ **ᴀ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇʀs ʟɪᴋᴇ sᴘᴀᴍ,ᴘ*ʀᴍsᴘᴀᴍ,ʀᴀɪᴅ,ʀᴇᴘʟʏ ʀᴀɪᴅ,ʟᴏᴠᴇ ʀᴀɪᴅ, sʜᴀʏᴀʀɪ ʀᴀɪᴅ.**\n"
#        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT +="`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://te.legra.ph/file/0651204bbadbc8d23fae3.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
