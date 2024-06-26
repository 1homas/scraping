# Scraping

For scraping a few random pages, use the [requests](https://requests.readthedocs.io/) library with [beautifulsoup](https://beautiful-soup-4.readthedocs.io/). If you need to build a web spider or crawler, use [Scrapy](https://scrapy.org/). But if you need to scrape sites with complex logins, cookies, tokens, and data hidden by JavaScript then you will need a browser driver like [Selenium](https://www.selenium.dev/).

## Setup

```sh
pipenv shell
pipenv install -r requirements.txt
```

## space_cookie.py

I wanted to be notified when [Monkish Brewing](https://www.monkishbrewing.com/) made their annual drop of the phenomenal double milkshake IPA, [Space Cookie](https://untappd.com/b/monkish-brewing-co-space-cookie/2150752). But I don't do IG so I needed another way to *get the scoop*.

Push notifications to my phone and computer are handled via the wonderful and free [ntfy.sh](https://ntfy.sh) service with the topic name [MonkishSpaceCookie](https://ntfy.sh/MonkishSpaceCookie).

A cronjob runs once per day to invoke the intermediate `space_cookie.sh` which runs `space_cookie.py` after initializing its virtual environment (and `.env`) to scrape their website in search of 'Space Cookie' among the available items. My crontab file for running daily at 11:15am with logging `stdout` and `stderr` going to `crontab_log.txt`:

```crontab
# ┌───────────── minute (0 - 59)
# │  ┌───────────── hour (0 - 23)
# │  │  ┌───────────── day of month (1 - 31)
# │  │  │  ┌───────────── month (1 - 12)
# │  │  │  │  ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │  │  │  │  │
 15 11  *  *  * /path/to/scraping/space_cookie.sh >> /path/to/scraping/crontab_log.txt 2>&1
# An empty line is required at the end of this file for a valid cron file!

```

## selenium_hello.py

A simple adaptation of Selenium's [`hello_selenium.py`](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/hello/hello_selenium.py) with some random URLs to use as a starting template.

## selenium_ddg.py

Use Selenium to open Firefox to [DuckDuckGo](https://duckduckgo.com) and perform an Internet search for *[python web scraping](https://duckduckgo.com/?t=h_&q=python+web+scraping)*. A simple test of filling a form/field and submitting data.
