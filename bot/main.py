import requests
from .config import SENDER_TOKEN, CHAT_ID


def send_message(text):
    requests.get(f"https://pi.telegram.org/bot{SENDER_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}")

