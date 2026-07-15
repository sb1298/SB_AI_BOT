import requests
import pandas as pd

from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

from config import TWELVE_API_KEY, TIMEFRAME


def get_market_analysis(pair):

    symbol = pair.replace("/", "")

    url = (
        f"https://api.twelvedata.com/time_series"
        f"?symbol={symbol}"
        f"&interval={TIMEFRAME}"
        f"&outputsize=150"
        f"&apikey={TWELVE_API_KEY}"
    )

    try:

        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") == "error":
            print("API Error:", data.get("message"))
            return None

        values = data.get("values")

        if not values:
            return None

        df = pd.DataFrame(values)

        df = df.astype({
            "open": float,
            "high": float,
            "low": float,
            "close": float
        })

        df = df.iloc[::-1].reset_index(drop=True)

        close = df["close"]

        df["EMA20"] = EMAIndicator(close, window=20).ema_indicator()
        df["EMA50"] = EMAIndicator(close, window=50).ema_indicator()

        df["RSI"] = RSIIndicator(close, window=14).rsi()

        macd = MACD(close)
        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()

        bb = BollingerBands(close)

        df["BB_UPPER"] = bb.bollinger_hband()
        df["BB_LOWER"] = bb.bollinger_lband()

        last = df.iloc[-1]

        trend = "Bullish" if last["EMA20"] > last["EMA50"] else "Bearish"

        return {
            "pair": pair,
            "price": round(last["close"], 5),
            "ema20": round(last["EMA20"], 5),
            "ema50": round(last["EMA50"], 5),
            "rsi": round(last["RSI"], 2),
            "macd": round(last["MACD"], 5),
            "macd_signal": round(last["MACD_SIGNAL"], 5),
            "bb_upper": round(last["BB_UPPER"], 5),
            "bb_lower": round(last["BB_LOWER"], 5),
            "trend": trend
        }

    except Exception as e:

        print("Market Analysis Error:", e)
        return None