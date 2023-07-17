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

    # Check if the user is an admin
    admin_status = client.get_chat_member(chat_id, message.from_user.id).status
    if admin_status not in ("administrator", "creator"):
        message.reply_text("You must be an admin to use this command.")
        return

    # Get the user to be kicked
    user_id = None

    # Check if the user is mentioned or if an ID is provided
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
