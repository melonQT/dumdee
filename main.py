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
    user_id = message.text.split()[1]

    try:
        app.kick_chat_member(chat_id, user_id)
        message.reply("User has been kicked")
    except Exception as e:
        message.reply(f"Could not kick user - {e}")
        print(f"Error: {str(e)}")  # Print the error message for debugging

app.run()
