import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def contains_will_list(data):
    if data is not None or data["status"] == 'enable':
        sampled_data = str(data[-1]["content"]).lower()
        if "will list" in sampled_data:
            return True
        return False
    return False


def contains_details(data):
    searched_word = 'Details:'
    page = requests.get(data[-1]["link"])

    soup = BeautifulSoup(
        page.content, 'html.parser'
    )
    results = soup.body.find_all(
        string = re.compile('.*{0}.*'.format(searched_word)), recursive = True
    )
    if len(results) > 0:
        return True, page
    return False


def contains_explorer(data):
    searched_word = 'Explorer'
    found_links = []
    soup = BeautifulSoup(
        data, 'html.parser'
    )
    all_a = soup.body.find_all(
        "a",
        # class_='css-cvxd88'
    )
    # results = all_a.find(
    #     string = re.compile('.*{0}.*'.format(searched_word)),
    #     recursive = True
    # )
    for a in all_a:
        # print(a.text.split('\n'))
        if searched_word in a.text.split():
            found_links.append(a.get("href"))
    return found_links


def parse_url(urls):
    token_contract_address = ''
    domain = ''

    for url in urls:
        # get the domain
        # print(urlparse(url).netloc)
        domain = urlparse(url).netloc
        # get the token
        # print(url.rsplit('/', 1)[-1])
        token_contract_address = url.rsplit('/', 1)[-1]

    if domain == 'etherscan.io':
        network_name = 'eth'
    elif domain == 'bscscan.com':
        network_name = 'bsc'
    else:
        network_name = 'trx'
    return network_name, token_contract_address
