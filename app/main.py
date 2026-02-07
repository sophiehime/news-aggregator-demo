from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.scraper import get_news
from app.pdf_generator import generate_pdf

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request, keyword: str = None):
    news = get_news()


    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "news": news,
            "keywords": KEYWORDS,
            "selected_keyword": keyword
        }
    )


@app.post("/pdf")
def create_pdf(selected_ids: list[int] = Form(...)):
    news = get_news()
    selected = [n for n in news if n["id"] in selected_ids]

    filename = "selected_news.pdf"
    generate_pdf(selected, filename)

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=filename
    )
