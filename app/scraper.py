import requests
from bs4 import BeautifulSoup
from newspaper import Article

SOURCES = {
    "Ekonomim": "https://www.ekonomim.com",
    "Dunya": "https://www.dunya.com",
    "Karar": "https://www.karar.com"
}

KEYWORDS = [
    "otomotiv",
    "toyota",
    "tesla",
    "byd",
    "nissan"
]


def extract_links(base_url):
    """Ana sayfadan haber linklerini çeker (demo amaçlı)"""
    links = set()
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("/") and len(href) > 20:
                links.add(base_url.rstrip("/") + href)
            elif href.startswith(base_url):
                links.add(href)
    except Exception:
        pass

    return list(links)[:10]  # demo için ilk 10 link


def get_news():
    results = []
    seen = set()

    for source, base_url in SOURCES.items():
        links = extract_links(base_url)

        for link in links:
            if link in seen:
                continue
            seen.add(link)

            try:
                article = Article(link, language="tr")
                article.download()
                article.parse()

                text_lower = article.text.lower()

                if any(k in text_lower for k in KEYWORDS):
                    results.append({
                        "id": len(results),
                        "source": source,
                        "title": article.title,
                        "content": article.text,
                        "url": link
                    })
            except Exception:
                continue

    return results