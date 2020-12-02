print("Loading...")


import matplotlib.pyplot as plt
import ffn
from databases import DTable


def pl(ans, st="2020-01-01"):
    try:
        price = ffn.get(ans, start=st)
        price.rebase().plot(figsize=(10, 5))
        plt.draw()
        plt.show(block=False)
    except IndexError:
        print("No tags entered")


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
    Here are instructions to manage the database.
    
    add: Add stocks to the database.
    rm: Remove stocks from the database.
    get: Get info about a stock(s).
    an: View analysis.
    db: view entire database.
    port: Change portfolio
    exit: To exit
    help: Show instructions
    """

j = True
while j:
    inp = input("Enter the portfolio name. Enter nothing for main database\n")
    if inp == "":
        dt = DTable.DTable()
    else:
        dt = DTable.DTable(inp)
    print(instructions)
    n = True
    while n:
        i = input()
        if i == "port":
            n = False
        elif i == "add":
            inp = input("add: ")
            inp = inp.split()
            dt.add(inp)
        elif i == "get":
            inp = input("get: ")
            ans = dt.get(inp.split())
            print(ans)
            pl(ans["symbol"].tolist())
        elif i == "an":
            print("Still in production.")
        elif i == "db":
            print(dt.all())
        elif i == "port":
            dt.done()
            n = False
        elif i == "exit":
            dt.done()
            n = False
            j = False
        elif i == "help":
            print(instructions)
        else:
            print("Invalid input...")