from reportlab.pdfgen import canvas
import ffn
import yfinance as yf
import pandas as pd
from datetime import date
from tabulate import tabulate
import os
from reportlab.lib.pagesizes import letter


def generate_pdf(portfolio=pd.DataFrame([]), username="test"):
    filename = username + "-portfolio-analysis_" + str(date.today()) + ".pdf"
    out_file_dir = '\\'.join(os.path.dirname(__file__).split("/"))
    out_file_path = os.path.join(out_file_dir, filename)
    print("RUN")
    width, height = letter
    pdf = canvas.Canvas(out_file_path, pagesize=letter)
    pdf.setFont("Times-Roman", 12)
    documentTitle = username + " Basis Project Portfolio Analysis (" + str(date.today()) + ")"
    pdf.setTitle(documentTitle)
    pdf.drawString(0, height-20, documentTitle)
    pdf.setFont("Times-Bold", 24)
    pdf.drawCentredString(width/2, height-80, "BASIS Project Portfolio Report")
    pdf.setFont("Times-Roman", 12)
    s = str(portfolio)
    pdf.drawString(20, 500, s)
    pdf.showPage()
    pdf.save()
    pass

#
# print(__name__)
#
# if __name__ == "__main__":
#
#     generate_pdf()
