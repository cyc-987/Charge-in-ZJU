from time import time
from fetch import Fetcher
from push import DingBot
from datetime import datetime, timezone, timedelta
import time
import urllib.parse
import argparse

def main(url):
    openId = ""
    
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    openId = query_params.get("openId", [""])[0]

    bot = DingBot(webhook='', secret='')

    fetcher = Fetcher(openId)

    while True:
        tz_utc_8 = timezone(timedelta(hours=8))
        current_time = datetime.now(tz_utc_8).strftime("%Y-%m-%d %H:%M:%S")
        print(f"Fetch time: {current_time}")        
        current_hour = datetime.now(tz_utc_8).hour
        if 0 <= current_hour < 6:
            print("Night time (00:00-06:00), skipping fetch...")
            time.sleep(600)
            continue
        result = fetcher.full_fetch()
        
        if result == -1:
            bot.send_error_message(current_time)
            time.sleep(600)  # Add a delay of 600 seconds before retrying
            fetcher.status = True  # Reset status for the next attempt
            continue
        bot.send_status_message(current_time, result)
        print("waiting...")
        time.sleep(60)  # Add a delay of 60 seconds between requests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="传入一个 URL 给 main 函数")
    parser.add_argument("url", help="目标 URL 地址")
    args = parser.parse_args()
    main(args.url)