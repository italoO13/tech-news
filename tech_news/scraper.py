import requests
from parsel import Selector
import time
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        if not response.status_code == 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    return links


# Requisito 3


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next = selector.css("span.current ~ a::attr(href)").get()
    return next


# Requisito 4
def scrape_news(html_content):
    news = {}
    selector = Selector(text=html_content)
    news["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    news["title"] = selector.css(".entry-title::text").get().strip()
    news["timestamp"] = selector.css(".meta-date::text").get()
    news["writer"] = selector.css(".author a::text").get()
    news["comments_count"] = len(selector.css(".comment-body").getall())
    news["summary"] = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    news["tags"] = selector.css("a[rel=tag]::text").getall()
    news["category"] = selector.css(".meta-category .label::text").get()
    return news


# Requisito 5
def get_tech_news(amount):
    links_new = []
    news = []
    URL = "https://blog.betrybe.com"
    while len(links_new) <= amount:
        html_content = fetch(URL)
        links_new.extend(scrape_updates(html_content))
        URL = scrape_next_page_link(html_content)
    for link in links_new:
        cont = fetch(link)
        news.append(scrape_news(cont))
    create_news(news[:amount])
    return news[:amount]
