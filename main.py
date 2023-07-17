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

app.run()
