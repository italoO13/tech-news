from tech_news.database import search_news
from datetime import datetime


# Requisito 6


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    try:
        date_formated = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news = search_news({"timestamp": {"$eq": date_formated}})
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
