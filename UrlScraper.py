import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
# from lxml import html

from config import (
    PERIOD_TIME,  # each n minutes
    BINANCE_WEB_STATIC_URL,  # page you wanna be scrape
)
from utils.main import (
    contains_will_list,
    contains_details,
    contains_explorer,
    parse_url,
)

from cakebot import (
    exchange_maker,
)

raw_data = []
have_will_list_data = []

found_links_data = []

counter = 0
while True:
    if counter == 0:
        print(
            f'{datetime.now(): }The Program is started\n'
            f'Press [ Ctrl + c ] to stop.'
        )
    page = requests.get(BINANCE_WEB_STATIC_URL)
    if page.status_code == 200:
        soup = BeautifulSoup(
            page.content, "html.parser"
        )
        first_coin = soup.find(
            "a",
            id = "link-0-0-p1"
        )
        try:
            if raw_data[-1]["content"] != first_coin.text or raw_data[-1]["status"] == 'enable':
                # print(entered to the condition')
                raw_data.append(
                    {
                        'content': first_coin.text,
                        'link': 'https://www.binance.com' + first_coin.get("href"),
                        'time': time.time(),
                        'status': 'enable'
                    }
                )
                print(f'{datetime.now()} new element found.')
        except:
            raw_data.append(
                {
                    'content': first_coin.text,
                    'link': 'https://www.binance.com' + first_coin.get("href"),
                    'time': time.time(),
                    'status': 'enable'
                }
            )
            print(f'{datetime.now()} first element found.')
        # print(raw_data)
        if contains_will_list(raw_data):
            # print(raw_data)
            have_will_list_data.append(raw_data[-1])
            print(f'{datetime.now()} will-list expression found.')
            boolean, page = contains_details(have_will_list_data)
            if boolean:
                print(f'{datetime.now()} detail expression found.')
                # do for Explorer search
                found_links_data = contains_explorer(page)
                if found_links_data is not None:
                    print(f'{datetime.now()} token contract link found.')
                    # getting token contract from the URL
                    network, token_contract = parse_url(found_links_data)
                    exchange_maker(
                        network,
                        token_contract
                    )
        counter += 1
        raw_data[-1]["status"] = 'disable'
        # print(raw_data)
        time.sleep(PERIOD_TIME)
    elif page.status_code == 403:
        print('blocked! wait for 30 seconds')
        time.sleep(30)
