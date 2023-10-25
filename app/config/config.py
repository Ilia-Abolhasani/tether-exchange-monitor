import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    # main chanel bot
    telegram_bot_server_url = os.getenv("telegram_bot_server_url")
    chat_id = os.getenv("chat_id")
