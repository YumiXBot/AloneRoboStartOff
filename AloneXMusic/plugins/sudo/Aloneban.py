import requests
import random
from AloneXMusic import app, userbot
from AloneXMusic.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from AloneXMusic.utils.alone_ban import admin_filter






Alone_text = [
"hey please don't disturb me.",
"who are you",    
"aap kon ho",
"aap mere owner to nhi lgte ",
"hey tum mera name kyu le rhe ho meko sone do",
"ha bolo kya kaam hai ",
"dekho abhi mai busy hu ",
"hey i am busy",
"aapko smj nhi aata kya ",
"leave me alone",
"dude what happend",    
]

strict_txt = [
"i can't restrict against my besties",
"are you serious i am not restrict to my friends",
"fuck you bsdk k mai apne dosto ko kyu kru",
"hey stupid admin ", 
"ha ye phele krlo maar lo ek dusre ki gwaand",  
"i can't hi is my closest friend",
"i love him please don't restict this user try to usertand "
]


 
ban = ["ban","boom"]
unban = ["unban",]
mute = ["mute","silent","shut"]
unmute = ["unmute","speak","free"]
kick = ["kick", "out","nikaal","nikal"]
promote = ["promote","adminship"]
demote = ["demote","lelo"]
group = ["group"]
channel = ["channel"]



# ========================================= #


@app.on_message(filters.command(["lone"], prefixes=["a", "A"]) & admin_filter)
async def restriction_app(app :app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(Alone_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")
    
    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"present {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))          
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply("𝐎ᴋʜ, 𝐁ᴀɴ 𝐊ᴀʀ 𝐃ɪʏᴀ 𝐁ᴏsᴅɪ 𝐖ᴀʟᴇ 𝐊ᴏ 𝐂ʜᴜᴛɪʏᴀ 𝐓ʜᴀ!")
                    
        for unbanned in data:
            print(f"present {unbanned}")
            if unbanned in unban:
                await app.unban_chat_member(chat_id, user_id)
                await message.reply(f"𝐎ᴋʜ, 𝐀ᴘɴᴇ 𝐁ᴏʟᴀ 𝐈sʟɪʏᴀ 𝐔ɴʙᴀɴ 𝐊ᴀʀ 𝐃ɪʏᴀ") 
                
        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("𝐆ᴇᴛ 𝐋ᴏsᴛ! 𝐁ʜᴀɢᴀ 𝐃ɪʏᴀ 𝐁ʜᴏsᴅɪ 𝐖ᴀʟᴇ 𝐊ᴏ") 
                    
        for muted in data:
            print(f"present {muted}") 
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"𝐎ᴋʜ, 𝐀ᴘɴᴇ 𝐁ᴏʟᴀ 𝐓ᴏ 𝐌ᴜᴛᴇ 𝐊ᴀʀ 𝐃ɪʏᴀ 𝐁ʜᴏsᴅɪ 𝐖ᴀʟᴇ 𝐊ᴏ") 
                    
        for unmuted in data:
            print(f"present {unmuted}")            
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"𝐇ᴜʜ 𝐔ɴᴍᴜᴛᴇ 𝐊ᴀʀ 𝐃ɪʏᴀ")   


        for promoted in data:
            print(f"present {promoted}")            
            if promoted in promote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     )
                await message.reply("𝐃ᴏɴᴇ 𝐀ᴅᴍɪɴ 𝐃ᴇ 𝐃ɪʏᴀ")

        for demoted in data:
            print(f"present {demoted}")            
            if demoted in demote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                       )
                     )
                await message.reply("𝐎ᴋʜ 𝐀ᴀᴘɴᴇ 𝐁ᴏʟᴀ 𝐓ᴏ 𝐇ᴀᴛᴀ 𝐃ɪʏᴀ 𝐀ᴅᴍɪɴ 𝐒ᴇ")


