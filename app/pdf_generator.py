from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(articles, filename="daily_news.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    content = []

    for a in articles:
        content.append(Paragraph(a["title"], styles["Heading2"]))
        content.append(Paragraph(a["text"], styles["Normal"]))

    doc.build(content)
