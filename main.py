from time import time
from fetch import Fetcher
from push import DingBot
import time
import urllib.parse
import argparse

def main(url):
    openId = ""
    running_status = True
    
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    openId = query_params.get("openId", [""])[0]

    bot = DingBot(webhook='', secret='')

    fetcher = Fetcher(openId)

    while running_status:
        current_time = time.time()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time))
        print(f"Fetch time: {current_time}")
        result = fetcher.full_fetch()
        
        if result == -1:
            running_status = False
            bot.send_error_message(current_time)
            break
        bot.send_status_message(current_time, result)
        print("waiting...")
        time.sleep(60)  # Add a delay of 60 seconds between requests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="传入一个 URL 给 main 函数")
    parser.add_argument("url", help="目标 URL 地址")
    args = parser.parse_args()
    main(args.url)