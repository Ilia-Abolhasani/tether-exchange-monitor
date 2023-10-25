import time
import requests


class Exchange:
    def __init__(self):
        self.ask_price = 0
        self.bid_price = 0

    def _request(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(
                    f"Request failed with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_price(self):
        pass
