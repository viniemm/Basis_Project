import pandas as pd

dow = pd.read_csv("dow30.csv")
port = dict()
t = ["mei","tech"]
def __init__(tags):
    i = 0
    while i<dow.size:
        for x in tags:
            if x in dow["Tags"][i]:
                print(x)
        i+=1

__init__(t)