import pandas as pd


class Selector:
    def __init__(self, con):
        finalCons = list()
        df = pd.read_csv("C:/Users/vinay/Documents/Basis_Project/SelectorFetcher/conditions.csv")
        print(df)
        for x in con:
            if x in df:
                pass
        for index, row in df.iterrows():
            print(index,row["tag"])