#!/usr/bin/env python3
import logging
import os
from datetime import datetime

script_basename = os.path.basename(__file__)

LOGS = os.getenv('LOGS')
BOT_TOKEN = os.getenv('YT_DLP_TELEGRAM_BOT_BOT_TOKEN')
WHITELIST_FILE = os.getenv('YT_DLP_TELEGRAM_BOT_WHITELIST_FILE')


def setup_logger():
    basename_root = os.path.splitext(script_basename)[0]
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


log = setup_logger()
if __name__ == '__main__':
    log.info(f'Using whitelist file {WHITELIST_FILE}')
    print()
