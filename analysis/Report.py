from reportlab.pdfgen import canvas
import ffn
import yfinance as yf
import pandas as pd
from datetime import date


class Report:
    def __init__(self, portfolio: list, username: str):
        filename = username + "-portfolio-analysis_" + str(date.today()) + ".pdf"
        self.pdf = canvas.Canvas(filename)
        documentTitle = username + " Basis Project Portfolio Analysis (" + str(date.today()) + ")"
        self.pdf.setTitle(documentTitle)
        self.pdf.drawString(270, 770, documentTitle)
        self.complete()
        pass

    def complete(self):
        self.pdf.save()


rp = Report([], "vini")
