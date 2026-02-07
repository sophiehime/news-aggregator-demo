import feedparser
from newspaper import Article

RSS_SOURCES = {
    "Dunya": "https://www.dunya.com/rss",
    "Karar": "https://www.karar.com/rss/ekonomi"
}

KEYWORDS = [
    "otomotiv",
    "araç",
    "otomobil",
    "elektrikli",
    "toyota",
    "tesla",
    "byd",
    "nissan"
]


def get_news():
    results = []
    seen_links = set()
    idx = 0

    for source, rss_url in RSS_SOURCES.items():
        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            link = entry.get("link")
            if not link or link in seen_links:
                continue

            seen_links.add(link)

            summary = entry.get("summary", "")
            text_lower = summary.lower()

            if not any(k in text_lower for k in KEYWORDS):
                continue

            content = summary  # fallback

            # Full text denemesi (olursa güzel olur)
            try:
                article = Article(link, language="tr")
                article.download()
                article.parse()
                if len(article.text) > 300:
                    content = article.text
            except Exception:
                pass

            results.append({
                "id": idx,
                "source": source,
                "title": entry.get("title", "Başlık yok"),
                "content": content,
                "url": link
            })
            idx += 1

    return results