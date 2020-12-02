

print("Loading...")
import os
import pandas as pd
import matplotlib.pyplot as plt
import ffn
from databases.DTable import DTable
from analysis.Report import Report
from portfolio.Portfolio import Portfolio
from getpass import getpass
dt = DTable()
rep = Report()


# cd .virtualenvs/Basis_Project-yFGBk4L_/scripts && source activate && cd ../../../documents/basis_project && py cli.py

class User:

    def __init__(self, s: bool):
        self.logs = pd.read_csv("./databases/users.csv")
        self.email = ""
        self.port = ""
        self.name = ""
        if s:
            t = False
            while not t:
                t = self.login()
        else:
            self.register()
            t = False
            while not t:
                t = self.login()

    def get_port(self):
        return self.port

    def done(self):
        self.logs = self.logs.drop_duplicates("email")
        self.logs = self.logs.sort_values("email")
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'users.csv')
        self.logs.to_csv(my_file, index=False)

    def make_user(self, password):
        pass




    def login(self) -> bool:
        logs = self.logs
        self.email = input("Email: ")
        password = getpass()
        flag = False
        for index, row in logs.iterrows():
            if row["email"] == self.email and row["password"] == password:
                self.port = row["stockinfo"]
                flag = True
                break
        return flag
        pass

    def register(self):
        logs = self.logs
        while True:
            email = input("Email: ")
            if "@" in email and "." in email:
                self.email = email
                break
            else:
                print("Invalid email. Try again...")
        self.name = input("Name: ")
        while True:
            pass1 = getpass()
            print("Confirm password: ")
            pass2 = getpass()
            if pass1 == pass2:
                self.make_user(pass1)
                print("Registration Success. Redirected to login.")
                break
            else:
                print("Password does not match. Try again...")
        pass














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
inp = input("Enter login or register \n")



print("""
Here are instructions to manage the database.

add: Add stocks to the database.
db: view entire database.
get: Get info about a stock(s).
rm: Remove stocks from the database.
rp: Replace stocks.
sc: Start stock screener
port: 




""")




