#!/usr/bin/env python3
"""
Scrape for Monkish Space Cookie beer.

Usage:
  scrape_space_cookie.py

Notification requires a ntfy.sh account and environment variable wit the topic name:
  NTFY_TOPIC 

"""
__author__ = "Thomas Howard"
__email__ = "t@thomas-howard.com"
__license__ = "MIT - https://mit-license.org/"


import argparse
import bs4 #  import BeautifulSoup
import os
import dotenv
import requests
import time


HEADERS_FIREFOX = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Accept-Language": "en-us",
    "Accept-Encoding": "gzip, deflate",
}


def ntfy(topic:str=None, msg:str=None):
    """
    Send the `msg` to the ntfy `channel`.
    """
    requests.post(f"https://ntfy.sh/{topic}", data=msg.encode('utf-8'))


def scrape_monkish_space_cookie(session:requests.session=None):
    """
    Detect when the Monkish Space Cookie beer is available.
    session (requests.session) : a requests session.
    """
    start_time = time.time()

    # Find All Beers with class `menu-item-title`. Example:
    #   <div class="menu-item-title">Foggy Window</div>
    monkish_beer_url = "https://www.monkishbrewing.com/tastingroom-anaheim"
    response = session.get(monkish_beer_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser') # load data into bs4
    beers = soup.find_all('div', { 'class': 'menu-item-title' })

    duration = f"🕐  {(time.time() - start_time):0.3f}s"

    # Send notification?
    if os.getenv('NTFY_TOPIC', None) is not None:
        msg = f'✨🍪 Space Cookie has landed! 🍻😀\nGet it at {url}\n{duration}' if 'Space Cookie' in beers else f"🙁 No Space Cookie today.\nHere's what is available:\n"+'\n'.join(sorted(set([beer.text for beer in beers])))+f"\n{duration}"
        ntfy(os.getenv('NTFY_TOPIC'), msg)


if __name__ == "__main__":
    """
    Launched from command line
    """
    dotenv.load_dotenv() # read from .env
    session = requests.Session()
    session.headers = HEADERS_FIREFOX
    scrape_monkish_space_cookie(session)
