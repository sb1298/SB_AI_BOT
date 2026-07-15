import time
from datetime import datetime

from config import PAIRS
from market_analysis import get_market_analysis
from report_formatter import format_report
from telegram_sender import send_message


def wait_until_next_5min():
    while True:
        now = datetime.now()

        if now.minute % 5 == 0 and now.second == 0:
            return

        time.sleep(1)


def run_analysis():

    print("=" * 40)
    print("Starting Market Analysis...")
    print("=" * 40)

    for pair in PAIRS:

        print(f"Analyzing {pair}...")

        data = get_market_analysis(pair)

        if data is None:
            print(f"Failed to analyze {pair}")
            continue

        report = format_report(data)

        if report:
            send_message(report)
            print(f"{pair} report sent.")

        time.sleep(2)

    print("Analysis Complete.\n")


print("=" * 40)
print("SB AI MARKET BOT STARTED")
print("Waiting for next 5-minute candle...")
print("=" * 40)

while True:

    wait_until_next_5min()

    run_analysis()

    # একই সেকেন্ডে দুইবার না চালানোর জন্য
    time.sleep(2)