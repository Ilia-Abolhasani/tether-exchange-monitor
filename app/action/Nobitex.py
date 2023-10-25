from app.action.Exchange import Exchange


class Nobitex(Exchange):
    def __init__(self):
        super().__init__()

    def get_price(self):
        _url = "https://api.nobitex.ir/v2/orderbook/USDTIRT"
        data = self._request(_url)
        if not data:
            return ["_", "_", "_", "_"]
        ask = data['asks'][0][0]
        bid = data['bids'][0][0]
        return [ask, bid]
