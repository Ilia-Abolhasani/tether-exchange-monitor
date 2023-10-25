import json
import requests
from datetime import datetime, timezone
from app.config.config import Config
import hashlib


class TelegramBotPublisherServer:
    def __init__(self):
        self.base_url = Config.telegram_bot_server_url
        self.chat_id = Config.chat_id
        self.secret = "change me"  # todo add this part for later

    # todo complete this encrypt communication
    def _create_headers(self):
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        message = f'{timestamp}{self.secret}'
        hashed_timestamp = hashlib.sha256(message.encode()).hexdigest()

        headers = {
            'X-Request-Time': timestamp,
            'X-Hashed-Timestamp': hashed_timestamp
        }
        return headers

    def _get(self, url, query):
        headers = self._create_headers()
        response = requests.get(self.base_url + url,
                                params=query, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
        return None

    def _post(self, url, query, body):
        headers = self._create_headers()
        response = requests.post(
            self.base_url + url, params=query, json=body, headers=headers)
        if response.status_code == 201 or response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code: {response.status_code}")
        return None

    def _update(self, url, query, body):
        headers = self._create_headers()
        response = requests.put(self.base_url + url,
                                params=query, json=body, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code: {response.status_code}")
        return None

    def _delete(self, url, query):
        headers = self._create_headers()
        response = requests.delete(
            self.base_url + url, params=query, headers=headers)
        if response.status_code == 204:  # Assuming 204 is the successful status code for a successful deletion
            print("Resource deleted successfully.")
        else:
            print(f"Request failed with status code: {response.status_code}")

    def send_message(self, text):
        query = {}
        message_data = {
            "text": text
        }
        body = json.dumps(message_data)

        return self._post(f"/api/bot/{self.chat_id}/send_message", query, body)
