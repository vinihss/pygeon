import requests
from .messenger import Messenger

class TelegramMessenger(Messenger):
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/sendMessage"

    def send_message(self, recipient, message):
        payload = {
            'chat_id': recipient,
            'text': message
        }

        response = requests.post(self.base_url, json=payload)
        return response.json()
