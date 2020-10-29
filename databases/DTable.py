import pandas as pd
import numpy as np
import matplotlib as plt
import yfinance as yf


class DTable:
    def __init__(self):
        self.db = pd.read_csv("BasisDB.csv")
        self.col = self.db.columns

    def get_single(self, ticker: str) -> dict:
        return self.db.loc[self.db["symbol"] == ticker.upper()].to_dict(orient="records")

    def get(self, tickers: str) -> list:
        tickers = tickers.strip().split()
        stocks = list()
        for tick in tickers:
            stocks.append(self.get_single(tick))
        return stocks

    def add_single(self, new_ticker):
        stk = yf.Ticker(new_ticker).info
        row = list()
        for field in self.col:
            row.append(stk[field])
        df = dict(zip(self.col, row))
        self.db = self.db.append(df, ignore_index=True)

    def add(self, tickers: str):
        tickers = tickers.strip().split()
        for ticker in tickers:
            self.add_single(ticker)

    def remove_single(self, old_ticker: str):
        self.db.drop(self.db[self.col[0]] == old_ticker)

    def remove(self, tickers: str):
        tickers = tickers.strip().split()
        for ticker in tickers:
            self.remove_single(ticker)

    def replace(self, old_tickers: str, new_tickers: str):
        self.remove(old_tickers)
        self.add(new_tickers)

    def done(self):
        df = self.db.drop_duplicates()
        df.to_csv("BasisDB.csv", index=False)
