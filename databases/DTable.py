import pandas as pd
import numpy as np
import matplotlib as plt
import yfinance as yf
from tqdm import tqdm, trange
import os
import regex as re
import multiprocessing as mp

"""
        try:
            t = trange(len(tickers) - 1, desc='Bar desc', leave=True)
            for i in t:
                t.set_description(tickers[i])
                t.refresh()
                result.append(self.__add_single(tickers[i]))
            self.done()
            return result
        except AttributeError:
            return result
"""


def to_list(s: str) -> list:
    return s.strip().split(" ")


class DTable:
    def __init__(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'BasisDB.csv')
        self.db = pd.read_csv(my_file)
        self.col = self.db.columns

    def get(self, tickers: list) -> list:
        db = self.db

        def get_single(ticker: str) -> dict:
            try:
                return db.loc[db["symbol"] == ticker.upper()].to_dict(orient="records")
            except IndexError:
                print("No such stock in database: " + ticker.upper())

        try:
            stocks = list()
            for tick in tickers:
                try:
                    tk = get_single(tick)[0]
                    stocks.append(tk)
                except IndexError:
                    print("No such stock in database: " + tick.upper())

            return stocks
        except AttributeError:
            return []

    def __add_single(self, new_ticker: str, result: list):
        try:
            stk = yf.Ticker(new_ticker).info
            row = list()
            for field in self.col:
                row.append(stk[field])
            df = dict(zip(self.col, row))
            self.db = self.db.append(df, ignore_index=True)
            # return new_ticker + ": True"
            t = df
        except:
            t = False
            # return new_ticker + ": False"
        if t != False:
            result.append(t)

    def add(self, tickers: list) -> list:
        result = list()
        processes = list()
        if __name__ == "__main__":
            t = trange(len(tickers), desc='Bar desc', leave=True)
            for i in t:
                tick = tickers[i]
                t.set_description(tick)
                t.refresh()  # to show immediately the update
                p = mp.Process(target=self.__add_single, args=(tick, result))
                x = p.start()
                processes.append(p)
            for process in processes:
                process.join()
        return self.db.concat(result)

    def __remove_single(self, old_ticker: str) -> bool:
        self.db = self.db.drop(old_ticker.upper())
        return True

    def remove(self, tickers: list) -> list:
        result = list()
        try:
            for ticker in tickers:
                result.append(self.__remove_single(ticker))
            self.done()
            return result
        except AttributeError:
            return []

    def replace(self, old_tickers: list, new_tickers: list) -> list:
        result = list()
        removal = self.remove(old_tickers)
        addition = self.add(new_tickers)
        result.append(removal)
        result.append(addition)
        return result

    def __find(self, conditions: str) -> list:
        result = list()
        for index, row in tqdm(self.db.iterrows(), desc="Loading..."):
            if conditions in (row["longBusinessSummary"].lower() +
                              row["sector"].lower() +
                              row["industry"].lower() +
                              row["shortName"].lower()):
                result.append(row["symbol"])
        return result

    def screen(self, conditions: str) -> list:
        result = list()
        conditions = to_list(conditions)
        for cond in conditions:
            result.extend(self.__find(cond))
        return result

    def all(self) -> pd.DataFrame:
        return self.db

    def done(self):

        self.db = self.db.drop_duplicates("symbol")
        self.db = self.db.sort_values("symbol")
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'BasisDB.csv')
        self.db.to_csv(my_file, index=False)
