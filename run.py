from app.cron.manager import start_jobs
from app.util.TelegramBotPublisherServer import TelegramBotPublisherServer
from app.util.FileHelper import FileHelper
import time

if __name__ == '__main__':
    bot_handler = TelegramBotPublisherServer()
    latest_message_file_handler = FileHelper("./latest_message.txt")
    start_jobs(bot_handler, latest_message_file_handler)
    while True:
        time.sleep(5)
