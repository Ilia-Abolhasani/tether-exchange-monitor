def create_message(rubex_price, nobitex_price):
    message = ""
    ask = rubex_price[0]
    bid = rubex_price[1]
    message += f"<b>رابکس:</b>\n"
    message += f"<b>خریدار {ask}    فروشنده {bid} </b>\n\n"
    ask = nobitex_price[0]
    bid = nobitex_price[1]
    if ask != "_":
        ask = str(int(ask) // 10)
    if bid != "_":
        bid = str(int(bid) // 10)
    message += f"<b>نوبیتکس:</b>\n"
    message += f"<b>خریدار {ask}    فروشنده {bid} </b>\n    "
    message += "‌"
    return message
