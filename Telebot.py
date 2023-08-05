from typing import final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    filters,
    ContextTypes,
    MessageHandler,
)


TOKEN = final = "6434740241:AAGYXIM_q6-AislKONrZfPccN1WpoSUWJTo"
BOT_USERNAME: final = "@in_for_mationbot"


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thank for chatting with me! I am a bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I am a bot! Please type something so I can respand..."
    )


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")


# Responses


def handle_responses(text: str) -> str:
    processt: str = text.lower()

    if "hello" in processt:
        return "Hey there!"

    if "hi" in processt:
        return "Hey there"

    if "how are you" in processt:
        return "I'm good!"

    if "i love python" in processt:
        return "Me to..."

    if "mmdreza" in processt:
        return "91020267203"

    return "I don't undrestand what you wrote..."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, " ").strip()
            response: str = handle_responses(new_text)

        else:
            return

    else:
        response: str = handle_responses(text)

    print("Bot", response)

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("Srarting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the Bot
    print("Polling...")
    app.run_polling(poll_interval=3)
