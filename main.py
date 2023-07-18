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

@app.on_message(filters.command("kick"))
def kick(client, message):
    chat_id = message.chat.id

    # Check if the command is replied to a user
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        input_id = message.command[1]

        # Check if the input is @username
        if input_id.startswith("@"):
            username = input_id[1:]
            user = app.get_users(username)
            if user:
                user_id = user.id
            else:
                message.reply_text("Invalid @username.")
                return
        else:
            # Assume input_id is user ID
            user_id = input_id
    else:
        message.reply_text("Please reply to the user or provide a valid user ID.")
        return

    try:
        app.ban_chat_member(chat_id, user_id)
        app.unban_chat_member(chat_id, user_id)
        message.reply("User has been kicked")
    except Exception as e:
        message.reply(f"Could not kick user - {e}")
        print(f"Error: {str(e)}")  # Print the error message for debugging

app.run()
