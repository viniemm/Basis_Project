print("Loading...")

import pandas as pd
import matplotlib.pyplot as plt
import ffn
from databases import DTable
from getpass import getpass

# cd .virtualenvs/Basis_Project-yFGBk4L_/scripts && source activate && cd ../../../documents/basis_project && python basis_ui.py


print("""
██████╗  █████╗ ███████╗██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██╔══██╗██╔══██╗██╔════╝██║██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
██████╔╝███████║███████╗██║███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║
██╔══██╗██╔══██║╚════██║██║╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║
██████╔╝██║  ██║███████║██║███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝

""")
print("Welcome to the BASIS Project by Vini Mathur.")
print("""
BASIS is a recursive acronym that stands for BASIS Automated Stock Investment Software.
More information about BASIS can be found at https://github.com/viniemm/Basis_Project.
Enter login or register.\n
""")


def granted():
    print("Admin privilege granted. Proceeding...")

    def data():
        def to_list(s: str) -> list:
            return s.strip().split()

        def to_div(s: str) -> list:
            result = list()
            s = s.strip().split("|")
            for n in s:
                result.append(n.strip().split("&"))
            return result

        dt = DTable.DTable()

        def start():
            inp = input("""
                    What would you like to do today?
                    Get info about a stock: get
                    Add tickers to database: add
                    Remove tickers from database: rm
                    View entire database: db
                    Exit: exit
                    """)

            def pl(ans):
                try:
                    price = ffn.get(ans, start='2020-01-01')
                    # tb.show(price)
                    price.rebase().plot(figsize=(10, 5))
                    plt.draw()
                    plt.show(block=False)
                except IndexError:
                    print("No tags entered")

            if inp == "get":
                try:
                    stocks = input("Enter the stocks separated by space: ")
                    stocks = dt.get(to_list(stocks))
                    print(stocks)
                    stocks = stocks["symbol"]
                    pl(stocks)
                    start()
                except KeyError:
                    print("One of the stocks you entered is not in the database")
                    start()
            elif inp == "add":
                stocks = input("Enter the stocks to be added separated by space: ")
                stocks = dt.add(to_list(stocks))
                print(stocks)
                start()
            elif inp == "rm":
                stocks = input("Enter the stocks to be removed separated by space: ")
                stocks = dt.remove(to_list(stocks))
                print(stocks)
                start()
            elif inp == "db":
                stocks = dt.all()
                start()
            elif inp == "exit":
                print("Exiting")
            else:
                print("try again")
                start()

        start()

    data()

    def go():
        inp = input("""
        What would you like to do today?
        Make a new portfolio: np
        View your portfolio: vp
        Make changes to database / screener: db
        """)
        if inp == "db":
            data()
        else:
            print("That feature is not available yet. Enter another option.")
            go()


def enter():
    username = input("Username: ")
    password = getpass()
    if username == "vini" and password == "admin":
        granted()
    else:
        print("Incorrect username or password. Try again.\n")
        enter()


enter()
