from pyrogram import Client, filters

app = Client(
    "qtpie",
    api_id=1747534,
    api_hash="5a2684512006853f2e48aca9652d83ea",
    bot_token="6342123536:AAEu_7JE_95Ah4FCW-HFyplCxru0yziSaPs"
)

@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("I'm alive!")

@app.on_message(filters.command("kick") & filters.group & filters.user("admins"))
def kick_command(client, message):
    chat_id = message.chat.id


    if client.get_chat_member(chat_id, message.from_user.id).status != "administrator":
        message.reply_text("You must be an admin to use this command.")
        return


    bot_member = client.get_chat_member(chat_id, client.get_me().id)
    if bot_member.status != "administrator" or not bot_member.can_restrict_members:
        message.reply_text("I'm not an admin in this group. Please make me an admin to use this command.")
        return


    user_id = None


    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        user_id = message.command[1]

    if user_id is None:
        message.reply_text("Please reply to the user you want to kick or provide a valid user ID.")
        return

    try:
        client.kick_chat_member(chat_id, user_id)
        message.reply_text("User has been kicked.")
    except Exception as e:
        message.reply_text(f"Failed to kick user. Error: {str(e)}")


app.run()
