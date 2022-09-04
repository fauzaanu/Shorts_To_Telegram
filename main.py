from pytube import YouTube
import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


async def download(link):
    YouTube(link).streams.get_highest_resolution().download(filename='shorts.mp4')


# working
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    linkx = update.message.text
    if "youtu" in linkx:
        if "shorts" in linkx:
            await download(linkx)

            # BAD CODE TODO
            try:
                #print("MAIN SEND")
                await context.bot.send_video(chat_id=update.effective_chat.id, video=open("shorts.mp4", 'rb'),
                                             supports_streaming=True, caption="", read_timeout=100, write_timeout=100,
                                             connect_timeout=100)
            except Exception as e:
                #print(f"MAIN SEND E{e}")

            # Send copies to admin @ -1001631461762
            os.remove("shorts.mp4")


# working part
async def commd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Add me in any group. Make me an Admin & I Will send you viewable Videos Youtube Shorts")


if __name__ == '__main__':
    token = 'TOKEN_FROM_BOT_FATHER'
    application = ApplicationBuilder().token(token).build()

    commands = CommandHandler('start', commd)
    links = MessageHandler(filters.TEXT, start)
    # on different commands - answer in Telegram
    application.add_handler(commands)
    application.add_handler(links)

    application.run_polling()
