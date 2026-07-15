from datetime import datetime


def format_report(data):

    if data is None:
        return None

    time_now = datetime.now().strftime("%H:%M:%S")

    message = f"""
📊 <b>SB AI MARKET ANALYSIS</b>

━━━━━━━━━━━━━━━━━━

💱 Pair : <b>{data['pair']}</b>

🕒 Time : <b>{time_now}</b>

💲 Price : <b>{data['price']}</b>

📈 Trend : <b>{data['trend']}</b>

━━━━━━━━━━━━━━━━━━

📊 EMA 20 : <b>{data['ema20']}</b>

📊 EMA 50 : <b>{data['ema50']}</b>

📉 RSI : <b>{data['rsi']}</b>

📈 MACD : <b>{data['macd']}</b>

📈 MACD Signal : <b>{data['macd_signal']}</b>

━━━━━━━━━━━━━━━━━━

⬆️ Bollinger Upper : <b>{data['bb_upper']}</b>

⬇️ Bollinger Lower : <b>{data['bb_lower']}</b>

━━━━━━━━━━━━━━━━━━

🤖 SB AI MARKET BOT
"""

    return message