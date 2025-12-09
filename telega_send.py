import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    r = requests.post(url, data=data)
    print("status:", r.status_code, r.text)


if __name__ == "__main__":
    try:
        with open("some_txt.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print("Ошибка чтения:", e)
        sys.exit(1)

    send_message(content)
