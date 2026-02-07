from newspaper import Article

SOURCES = [
    "https://www.ekonomim.com",
    "https://www.dunya.com",
    "https://www.karar.com"
]

KEYWORDS = [
    "otomotiv",
    "toyota",
    "tesla",
    "byd",
    "nissan"
]


def get_news():
    results = []
    idx = 0

    for url in SOURCES:
        try:
            article = Article(url, language="tr")
            article.download()
            article.parse()

            text_lower = article.text.lower()

            if any(keyword in text_lower for keyword in KEYWORDS):
                results.append({
                    "id": str(idx),
                    "title": article.title,
                    "content": article.text
                })
                idx += 1

        except Exception:
            continue

    return results