print("Loading...")

import matplotlib.pyplot as plt
import ffn
from databases import DTable, Mailer
import json
import pandas as pd

__version__ = 1.3
__author__ = "Vinayak Mathur"


def pl(ans, st="2020-01-01"):
    try:
        price = ffn.get(ans, start=st)
        with pd.option_context("display.max_rows", None):
            print(price)
        price.rebase().plot(figsize=(10, 5))
        plt.draw()
        plt.show(block=False)
    except IndexError:
        print("No tags entered")


# cd .virtualenvs/Basis_Project-yFGBk4L_/scripts && source activate && cd ../../../documents/basis_project

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
""")

instructions = """
usage: basis [--version] [--help] [--author] [--info]


Here are some basic commands
    
    add    Add stocks to the portfolio.
    rm     Remove stocks from the portfolio.
    get    Get info about a stock(s).
    ml     Mail portfolio.
    db     View entire portfolio.
    port   Change portfolio
    exit   Exit    
"""

j = True
while j:
    port_name = input("Enter the portfolio name. Enter nothing for main database\n")
    if port_name == "":
        dt = DTable.DTable()
    else:
        dt = DTable.DTable(port_name)
    print(instructions)
    n = True
    while n:
        inp = input(port_name + " $ ").split()
        try:
            i = inp[0]
        except IndexError:
            inp = ["basis", "--help"]
            i = inp[0]
        if i == "port":
            n = False
        elif i == "add":
            if len(inp) > 1:
                ls = inp[1:]
                ver = dt.add(inp[1:])
                dictionary = dict(zip(ls, ver))
                print(json.dumps(dictionary, indent=4, sort_keys=True))

        elif i == "rm":
            if len(inp) > 1:
                dt.remove(inp[1:])
        elif i == "get":
            if len(inp) > 1:
                ans = dt.get(inp[1:])
                print(ans)
                try:
                    stdate = input("Enter start date (yyyy--mm--dd). Leave blank for YTD: ")
                    print(stdate)
                    if stdate == "":
                        pl(ans["symbol"].tolist())
                    else:
                        pl(ans["symbol"].tolist(), stdate)
                except KeyError:
                    print(inp[1] + " was not found in the portfolio.")
                    print("To add the stock to the portfolio do: get " + inp[1])
        elif i == "ml":
            # Report.generate_pdf(dt.all(), port_name)
            em = input("Enter email address: ")
            Mailer.mail(em, port_name + ".csv")

        elif i == "db":
            df = dt.all()
            with pd.option_context("display.max_rows", None):
                if df.empty is False:
                    print(df)
                else:
                    print("No stocks currently in portfolio " + port_name)
        elif i == "port":
            dt.done()
            n = False
        elif i == "exit":
            dt.done()
            n = False
            j = False
        elif i == "help":
            print(instructions)
        elif i == "basis":
            con = inp[1]
            if con == "--help":
                print(instructions)
            elif con == "--version":
                print("BASIS version" + str(__version__))
            elif con == "--author":
                print(__author__)
            elif con == "--info":
                print("""
                BASIS is a recursive acronym that stands for BASIS Automated Stock Investment Software.
                More information about BASIS can be found at https://github.com/viniemm/Basis_Project.
                """)
        else:
            print("Invalid input...")
            print("see basis --help")
