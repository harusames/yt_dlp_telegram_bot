#!/usr/bin/env python3
import logging
import os
import tempfile
from datetime import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# region environment variables
LOGS = os.getenv('LOGS')
BOT_TOKEN = os.getenv('YT_DLP_TELEGRAM_BOT_BOT_TOKEN')
WHITELIST_FILE = os.getenv('YT_DLP_TELEGRAM_BOT_WHITELIST_FILE')
# endregion


script_basename = os.path.basename(__file__)
basename_root = os.path.splitext(script_basename)[0]
videos_dir = os.path.join(tempfile.gettempdir(), basename_root)


def setup_logger():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_filename = os.path.join(LOGS, f'{basename_root}_{timestamp}.log')

    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create handlers
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def download_video(url: str) -> str:
    return "/e/media/replies/Mike O'Hearn Original Meme Template for TikTok (What Is Love) [tRE_3jpBEo8].mp4"


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    trace_id = (str(update.message.date.astimezone()).split('+')[0], update.message.from_user.id)
    log.info(f'{trace_id} {update.message.from_user.first_name} wrote {update.message.text}')
    video_path = download_video(update.message.text)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open(video_path, 'rb'))


log = setup_logger()
if __name__ == '__main__':
    log.info(f'Using whitelist file {WHITELIST_FILE}')

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler))
    app.run_polling()
