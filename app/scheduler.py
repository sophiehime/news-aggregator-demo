from apscheduler.schedulers.background import BackgroundScheduler
from app.scraper import SOURCES, get_article_links, scrape_article
from app.pdf_generator import generate_pdf

scheduler = BackgroundScheduler()

def update_news():
    articles = []

    for source, url in SOURCES.items():
        links = get_article_links(url)
        for link in links:
            article = scrape_article(link)
            if article:
                articles.append(article)

    if articles:
        generate_pdf(articles)

def start_scheduler():
    scheduler.add_job(update_news, "interval", hours=2)
    scheduler.start()
