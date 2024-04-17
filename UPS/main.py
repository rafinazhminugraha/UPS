from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import menuUtama
import menuWelcome
import globalVar

def printTitle():
    os.system("cls")
    print("━━━━━━━━━━━━━━━━━━━━")
    print(f"{Fore.CYAN}\n        UPS")
    print(Style.RESET_ALL)
    print("━━━━━━━━━━━━━━━━━━━━")
    print()

while True:
    if not globalVar.status_login:
        menuWelcome.welcomePage()
    else:
        menuUtama.menuUtama()