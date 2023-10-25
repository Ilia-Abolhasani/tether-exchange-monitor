from app.action.Exchange import Exchange


class Rubex(Exchange):
    def __init__(self):
        super().__init__()

    def get_price(self):
        _url = "https://p.rabex.ir/api/v1/market/p2p/depth?symbol=USDTTMN"
        data = self._request(_url)
        if not data:
            return ["_", "_", "_", "_"]
        bid = data['data']['bids'][0]['price']
        ask = data['data']['asks'][0]['price']
        return [bid, ask]
