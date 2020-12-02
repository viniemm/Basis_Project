import pandas as pd
import yfinance as yf
from tqdm import tqdm, trange
import os
import csv


class DTable:

    # initializer that sets the dataframe (FINAL READY)

    def __init__(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'BasisDB.csv')
        self.db = pd.read_csv(my_file)
        self.col = self.db.columns
        self.sym = self.db["symbol"].tolist()

    # verification of removal and addition (TESTING REQUIRED)

    def verify(self, stocks: list):
        resFal = []
        resTru = []
        for stock in stocks:
            if stock[1]:
                resTru.append(stock[0])
            else:
                resFal.append(stock[0])
        print("Success: ".join(resTru))
        print("Failure: ".join(resFal))

    # gets dataframe of given stocks (FINAL READY)

    def get(self, tickers: list) -> pd.DataFrame:
        db = self.db

        def __get_single(ticker: str) -> dict:
            try:
                return db.loc[db["symbol"] == ticker.upper()].to_dict(orient="records")
            except IndexError:
                print("No such stock in database: " + ticker.upper())

        try:
            stocks = list()
            for tick in tickers:
                try:
                    tk = __get_single(tick)[0]
                    stocks.append(tk)
                except IndexError:
                    print("No such stock in database: " + tick.upper())

            return pd.DataFrame(stocks)
        except AttributeError:
            return pd.DataFrame([])

    # subroutine for add() (FINAL READY)

    def __add_single(self, new_ticker: str):
        j = True
        try:
            if new_ticker not in self.sym:
                stk = yf.Ticker(new_ticker).info
                row = list()
                for field in self.col:
                    row.append(stk[field])
                df = dict(zip(self.col, row))
                self.db = self.db.append(df, ignore_index=True)
                self.sub_done()
        except:
            j = False
        return [new_ticker, j]

    # addition of a new row (FINAL READY)

    def add(self, tickers: list):
        result = list()
        try:
            t = trange(len(tickers), desc='Bar desc', leave=True)
            for i in t:
                result.append(self.__add_single(tickers[i]))
                t.set_description(tickers[i] + ": " + str(i))
                t.refresh()
                self.done()
            self.verify(result)
            return result
        except AttributeError:
            return result

    # subroutine for remove() (TESTING REQUIRED)

    def __remove_single(self, old_ticker: str) -> list:
        j = True
        try:
            old_ticker = old_ticker.upper()
            if old_ticker in self.db.columns:
                self.db[self.db["symbol"] != old_ticker]
                self.sub_done()
        except:
            j = False
        return [old_ticker, j]

    # removal of row (TESTING REQUIRED)

    def remove(self, tickers: list) -> list:
        result = list()
        try:
            t = trange(len(tickers), desc='Bar desc', leave=True)
            for i in t:
                result.append(self.__remove_single(tickers[i]))
                t.set_description(tickers[i] + ": " + str(i))
                t.refresh()
                self.done()
            self.verify(result)
            return result
        except AttributeError:
            return result

    # encapsulates addition and removal simultaneously (TESTING REQUIRED)

    def replace(self, old_tickers: list, new_tickers: list):
        removal = self.remove(old_tickers)
        addition = self.add(new_tickers)
        print("Removal: ")
        self.verify(removal)
        print("Addition: ")
        self.verify(addition)

    # subroutine for screen() (TESTING REQUIRED)

    def __find(self, conditions: list) -> list:
        result = list()
        for index, row in tqdm(self.db.iterrows(), desc="Loading..."):
            if all(x in (row["longBusinessSummary"].lower() +
                         row["sector"].lower() +
                         row["industry"].lower() +
                         row["shortName"].lower()) for x in conditions):
                result.append(row["symbol"])
        return result

    # MAJOR stock screener (TESTING REQUIRED)

    def screen(self, conditions: list) -> list:
        result = list()
        try:
            for condition in conditions:
                result.append(self.__find(condition))
            return result
        except AttributeError:
            return result

    # prints the entire (readable) database and returns a dataframe of the entire database (FINAL READY)

    def all(self) -> pd.DataFrame:
        df = self.db.drop(["longBusinessSummary", "logo_url"], axis=1)
        print(df.to_string())
        return self.db

    # done will sort and delete duplicates (FINAL READY)

    def done(self):
        self.db = self.db.drop_duplicates("symbol")
        self.db = self.db.sort_values("symbol")
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'BasisDB.csv')
        self.db.to_csv(my_file, index=False)

    # IMPORTANT sub_done after every addition/removal (FINAL READY)

    def sub_done(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'BasisDB.csv')
        self.db.to_csv(my_file, index=False)
