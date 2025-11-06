from app.services.newsapi_services import NewsAPIService

def test_news_fetch():
    service = NewsAPIService()
    articles = service.get_latest_news("day trading")
    assert isinstance(articles, list)
    assert len(articles) <= 5

if __name__ == "__main__":
    service = NewsAPIService()
    res = service.get_latest_news("Tesla stock")
    print(res)

