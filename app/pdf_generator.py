from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(news_items, filename):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    for item in news_items:
        elements.append(Paragraph(item["title"], styles["Heading2"]))
        elements.append(Paragraph(f"Kaynak: {item['source']}", styles["Italic"]))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(item["content"], styles["Normal"]))
        elements.append(Spacer(1, 24))

    doc.build(elements)
