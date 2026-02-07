import feedparser
from newspaper import Article


RSS_SOURCES = {
    "Reuters": "https://www.reuters.com/rssFeed/automotiveNews"
}

KEYWORDS = [
    "automotive",
    "car",
    "vehicle",
    "electric",
    "tesla",
    "toyota",
    "nissan",
    "byd"
]


def get_news():
    results = []
    seen_links = set()
    idx = 0

    for source, rss_url in RSS_SOURCES.items():
        feed = feedparser.parse(rss_url)

        # RSS boş gelirse hiçbir şey eklenmez
        for entry in feed.entries:
            link = entry.get("link")
            if not link or link in seen_links:
                continue

            seen_links.add(link)

            title = entry.get("title", "").strip()
            summary = entry.get("summary", "").strip()

            combined_text = f"{title} {summary}".lower()

            # Anahtar kelime filtresi
            if not any(k in combined_text for k in KEYWORDS):
                continue

            content = summary  # minimum garanti içerik

            # Full text denemesi (olursa)
            try:
                article = Article(link, language="en")
                article.download()
                article.parse()
                if article.text and len(article.text) > 300:
                    content = article.text
            except Exception:
                pass

            results.append({
                "id": idx,
                "source": source,
                "title": title,
                "content": content,
                "url": link
            })
            idx += 1

    return results
