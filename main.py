from time import time
from fetch import Fetcher
import time

def main():
    openId = ""
    running_status = True

    fetcher = Fetcher(openId)

    while running_status:
        current_time = time.time()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time))
        print(f"Fetch time: {current_time}")
        result = fetcher.full_fetch()
        
        if result == -1:
            running_status = False
        print("waiting...")
        time.sleep(15)  # Add a delay of 15 seconds between requests


if __name__ == "__main__":
    main()