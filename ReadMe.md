# Scraping

For scraping a few random pages, use the [requests](https://requests.readthedocs.io/) library with [beautifulsoup](https://beautiful-soup-4.readthedocs.io/). If you need to build a web spider or crawler, use [Scrapy](https://scrapy.org/). But if you need to scrape sites with complex logins, cookies, tokens, and data hidden by JavaScript then you will need a browser driver like [Selenium](https://www.selenium.dev/).

## Setup

```sh
pipenv shell
pipenv install -r requirements.txt
```

## scrape_space_cookie.py

I wanted to be notified when [Monkish Brewing](https://www.monkishbrewing.com/) released their annual drop of their phenomenal double milkshake IPA, [Space Cookie](https://untappd.com/b/monkish-brewing-co-space-cookie/2150752). But I don't do IG so I needed another way to get the *scoop*.

A cronjob runs once per day to invoke the intermediate `scrape_space_cookie.sh` which runs `scrape_space_cookie.py` after initializing its virtual environment (and `.env`) to scrape their website in search of 'Space Cookie' among the available items. Push notifications to my phone and computer are handled via the wonderful and free [ntfy.sh](https://ntfy.sh) service with the topic name specified in a `.env` file:

```sh
NTFY_TOPIC=your_topic_name
```

My crontab file for running daily at 11:05am with logging `stdout` and `stderr` going to `crontab_log.txt`:

```crontab
# ┌───────────── minute (0 - 59)
# │  ┌───────────── hour (0 - 23)
# │  │  ┌───────────── day of month (1 - 31)
# │  │  │  ┌───────────── month (1 - 12)
# │  │  │  │  ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │  │  │  │  │
  5 11  *  *  * /path/to/scraping/scrape_space_cookie.sh >> /path/to/scraping/crontab_log.txt 2>&1
```


