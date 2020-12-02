import pandas as pd
import yfinance as yf
from tqdm import tqdm, trange
import os
import csv


class DTable:

    # initializer that sets the dataframe (FINAL READY)

    def __init__(self, fname="BasisDB"):
        self.fname = fname + ".csv"
        print(self.fname)
        this_folder = os.path.dirname(os.path.abspath(__file__))
        self.my_file = os.path.join(this_folder, self.fname)
        t = os.path.exists(self.my_file)
        if not t:
            self.template = os.path.join(this_folder, "dbtester.csv")
            df = pd.read_csv(self.template)
            df.to_csv(self.my_file, index=False)
        self.db = pd.read_csv(self.my_file)
        self.col = self.db.columns
        self.sym = self.db["symbol"].tolist()

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
        return j

    # addition of a new row (FINAL READY)

    def add(self, tickers: list):
        result = list()
        try:
            t = trange(len(tickers), desc='Bar desc', leave=True)
            for i in t:
                t.set_description(tickers[i] + ": " + str(i))
                t.refresh()
                result.append(self.__add_single(tickers[i]))
                self.done()
            return result
        except AttributeError:
            return result

    # removal of a row (FINAL READY)

    def remove(self, tickers: list) -> list:
        result = list()
        for i in range(len(tickers)):
            tickers[i] = tickers[i].upper()
        result = list()
        df2 = pd.DataFrame()
        df = self.db
        deletion = list()
        deleted = list()
        for index, row in df.iterrows():
            if row["symbol"] in tickers:
                deleted.append(row["symbol"])
                deletion.append(index)
        df2 = df.drop(deletion)
        self.db = df2
        self.sub_done()
        result = list()
        for n in tickers:
            if n in deleted:
                result.append(True)
            else:
                result.append(False)
        return result

    # prints the entire (readable) database and returns a dataframe of the entire database (FINAL READY)

    def all(self) -> pd.DataFrame:
        df = self.db.drop(["longBusinessSummary", "logo_url"], axis=1)
        return df

    # done will sort and delete duplicates (FINAL READY)

    def done(self):
        self.db = self.db.drop_duplicates("symbol")
        self.db = self.db.sort_values("symbol")
        self.db.to_csv(self.my_file, index=False)

    # IMPORTANT sub_done after every addition/removal (FINAL READY)

    def sub_done(self):
        self.db.to_csv(self.my_file, index=False)


# dt = DTable()
# dt.remove(["msft", "googl"])
# dt.add(["msft", "googl"])
# dt.get(["msft"])
# dt.done()
# dt.all()
