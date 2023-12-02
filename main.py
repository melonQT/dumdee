import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# Handler for /start command in group chats
@app.on_message(filters.command("start") & filters.group)
def start_command_group(client, message):
    video_url = "https://graph.org/file/8f3e2528c659cff4951dd.mp4"
    text = "baby don't hurt me"

    # Send the video with the text
    message.reply_video(video_url, caption=text)



# Handler for /start command in the bot's private messages
@app.on_message(filters.command("start") & filters.private)
def start_command_pm(client, message):
    text = "Bot In Development"

    # Create the inline keyboard with the button
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Official Group", url="https://t.me/+OMUL6PhBBYJiZGY1")]])

    # Send the message with the attached button
    message.reply_text(text, reply_markup=keyboard)



@app.on_message(filters.command("kick") & filters.group)
def kick(client, message):
    chat_id = message.chat.id

    # Check if the user is an admin or creator
    if message.from_user.status not in ("administrator", "creator"):
        message.reply_text("You must be an admin or the creator of the group to use this command.")
        return

    # Check if the bot is an admin
    bot_member = app.get_chat_member(chat_id, "me")
    if bot_member.status != "administrator":
        message.reply_text("I'm not an admin. Please make me an admin for me to kick users!")
        return

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

@app.on_message(filters.command("matchmake") & filters.group)
def matchmake_command(client, message):
    chat_id = message.chat.id
    user = message.from_user

    # Get a list of group members
    group_members = app.get_chat_members(chat_id)

    # Filter out the bot and the user who sent the command
    group_members = [member for member in group_members if not member.user.is_bot and member.user.id != user.id]

    if not group_members:
        message.reply_text("No eligible users found for matchmaking.")
        return

    # Randomly select a user
    random_user = random.choice(group_members).user
    random_user_first_name = random_user.first_name

    # Generate the matchmaking message
    reply_text = f"The user {user.first_name} raped {random_user_first_name}!"

    # Reply with the matchmaking message
    message.reply_text(reply_text)

app.run()
