import requests

from config import BOT_TOKEN, CHAT_ID


def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    try:

        requests.post(url, data=data)

    except Exception as e:

        print("Telegram Error :", e)


def send_signal(pair, signal, confidence, entry_time):

    icon = "🟢" if signal == "CALL" else "🔴"

    message = f"""
𒆜◙•══‼️ <b>SB AI BOT SIGNAL</b> ‼️══•◙𒆜

┏━━━━━━━━・━━━━━━━━┓

📊 Pair : <b>{pair}</b>

🕓 Entry Time : <b>{entry_time}</b>

⏳ Expiry : <b>M1</b>

{icon} Signal : <b>{signal}</b>

📈 Confidence : <b>{confidence}%</b>

┗━━━━━━━━・━━━━━━━━┛
"""

    send_message(message)


def send_result(pair, signal, result):

    if result == "WIN":
        icon = "✅"
    else:
        icon = "❌"

    message = f"""
{icon} <b>SB AI BOT RESULT</b>

📊 Pair : <b>{pair}</b>

📈 Signal : <b>{signal}</b>

🏆 Result : <b>{result}</b>
"""

    send_message(message)