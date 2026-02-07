from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(selected_articles):
    pdf_path = "selected_news.pdf"

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    elements = []

    for article in selected_articles:
        elements.append(Paragraph(article, styles["Normal"]))

    doc.build(elements)

    return pdf_path
