from eventregistry import EventRegistry, QueryArticlesIter, QueryItems
from app.config import NEWSAPI_AI_KEY

class NewsAPIService:
    def __init__(self):
        # Only fetch recent news; free users can't use archive
        self.er = EventRegistry(apiKey=NEWSAPI_AI_KEY, allowUseOfArchive=False)

    def get_latest_news(self, query: str, lang: str = "eng", max_articles: int = 5):
        # Build a query that uses the correct keyword structure
        q = QueryArticlesIter(
            keywords = QueryItems.OR([query]),
            lang = lang
        )
        articles = []
        # Use the execQuery method to fetch articles
        try:
            for art in q.execQuery(self.er, sortBy="date", maxItems=max_articles):
                articles.append({
                    "title": art.get("title"),
                    "source": art.get("source", {}).get("title"),
                    "published": art.get("dateTime"),
                    "url": art.get("url"),
                    "description": art.get("body")
                })
            return articles
        except Exception as e:
            print(f"NewsAPI ERROR: {e}")
            return []
