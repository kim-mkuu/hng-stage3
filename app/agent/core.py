from services.newsapi_services import NewsAPIService

news_service = NewsAPIService()
news = news_service.get_latest_news("Tesla stock", max_articles=3)
for n in news:
    print(n["title"], n["url"])
