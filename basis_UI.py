"""
import databases as db
import SelectorFetcher as sf
import blackbox as bb
"""
from databases import DTable
from tqdm import tqdm
import time
from getpass import getpass

print("""
██████╗  █████╗ ███████╗██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██╔══██╗██╔══██╗██╔════╝██║██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
██████╔╝███████║███████╗██║███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║
██╔══██╗██╔══██║╚════██║██║╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║
██████╔╝██║  ██║███████║██║███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝

""")
time.sleep(1)
for i in tqdm(range(10), desc="Loading..."):
    time.sleep(0.1)
print("""Welcome to the BASIS Project by Vini Mathur.""")
time.sleep(1)
print("""
BASIS is a recursive acronym that stands for BASIS Automated Stock Investment Software.
More information about BASIS can be found at https://github.com/viniemm/Basis_Project.
Please enter username and password.\n
""")


def granted():
    print("Admin access granted. Proceeding...")
    dt = DTable.DTable()
    print(dt.find(["financial"]))
    pass


def enter():
    username = input("Username: ")
    password = getpass()
    if username == "vini" and password == "admin":
        granted()
    else:
        print("Incorrect username or password. Try again.\n")
        enter()


time.sleep(1)
enter()
