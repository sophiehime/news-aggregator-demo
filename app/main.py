from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.scraper import get_news
from app.pdf_generator import create_pdf

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    news = get_news()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "news": news}
    )


@app.post("/generate-pdf")
def generate_pdf(selected: list[str] = Form(...)):
    pdf_path = create_pdf(selected)
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="selected_news.pdf"
    )
