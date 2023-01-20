from tech_news.database import search_news

# Requisito 6


def search_by_title(title):
    title_and_url = []
    QUERY = {"title": {"$regex": f"{title}/i"}}
    news = search_news(QUERY)
    for new in news:
        title_and_url.append((new["title"], new["url"]))
    return title_and_url


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
