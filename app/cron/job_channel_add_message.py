from app.util.Message import create_message
from app.action.Rubex import Rubex
from app.action.Nobitex import Nobitex
rubex = Rubex()
nobitex = Nobitex()


def start(bot_handler, latest_message_file_handler):
    try:
        rubex_price = rubex.get_price()
        nobitex_price = nobitex.get_price()
        message = create_message(rubex_price, nobitex_price)
        latest_message = latest_message_file_handler.read()
        if message == latest_message:
            return
        result = bot_handler.send_message(message)
        latest_message_file_handler.write(message)
    except Exception as error:
        print(error)
