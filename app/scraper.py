import requests
from bs4 import BeautifulSoup
from newspaper import Article
from urllib.parse import urljoin

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

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_article_links(source_url, limit=20):
    response = requests.get(source_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/"):
            href = urljoin(source_url, href)
        if source_url in href:
            links.append(href)

    return list(set(links))[:limit]

def scrape_article(url):
    try:
        article = Article(url, language="tr")
        article.download()
        article.parse()

        if any(k in article.text.lower() for k in KEYWORDS):
            return {
                "title": article.title,
                "text": article.text,
                "url": url
            }
    except:
        return None
