import yfinance as yf
import pandas as pd
dow = pd.read_csv("dow30.csv")
li = list()
for x in dow["Symbol"]:
    ticker = yf.Ticker(x)
    li.append(ticker.info)
df = pd.DataFrame(li)
df.to_csv("test.csv")
print(df)