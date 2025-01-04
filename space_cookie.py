#!/usr/bin/env python3
"""
Scrape for Monkish Space Cookie beer.

Usage:
  space_cookie.py

Notification requires a ntfy.sh account.

"""
__author__ = "Thomas Howard"
__email__ = "1@1homas.org"
__license__ = "MIT - https://mit-license.org/"


import argparse
import bs4  # BeautifulSoup
import os
import requests


HEADERS_FIREFOX = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Accept-Language": "en-us",
    "Accept-Encoding": "gzip, deflate",
}


def ntfy(topic: str = None, msg: str = None):
    """
    Send the `msg` to the ntfy `channel`.
    """
    requests.post(f"https://ntfy.sh/{topic}", data=msg.encode("utf-8"))


def scrape_space_cookie(session: requests.session = None):
    """
    Detect when the Monkish Space Cookie beer is available.
    session (requests.session) : a requests session.
    """

    # Find All Beers with class `menu-item-title`. Example:
    #   <div class="menu-item-title">Foggy Window</div>
    url = "https://www.monkishbrewing.com/tastingroom-anaheim"
    response = session.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")  # load data into bs4
    beers = soup.find_all("div", {"class": "menu-item-title"})
    beers = sorted(set([beer.text for beer in beers]))

    # Send notification?
    if "Space Cookie" in beers:
        msg = f"✨🍪 Space Cookie has landed! 🍻😀\nGet it at {url}"
    else:
        msg = "🙁 No Space Cookie today.\nHere's what is available:\n" + "\n".join(beers)

    ntfy("MonkishSpaceCookie", msg)


if __name__ == "__main__":
    """
    Launched from command line
    """
    session = requests.Session()
    session.headers = HEADERS_FIREFOX
    scrape_space_cookie(session)
