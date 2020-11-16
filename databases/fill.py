from DTable import DTable
from get_all_tickers import get_tickers as gt

ls = gt.get_tickers()
# or if you want to save them to a CSV file
dt = DTable()
print(ls)
j = dt.add(ls)
print(j)
dt.done()
