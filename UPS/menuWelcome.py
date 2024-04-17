# =======================================Welcome Page============================================
from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import menuLogin
import menuRegistrasi
import globalVar

def printTitle():
    os.system("cls")
    print("━━━━━━━━━━━━━━━━━━━━")
    print(f"{Fore.CYAN}\n        UPS")
    print(Style.RESET_ALL)
    print("━━━━━━━━━━━━━━━━━━━━")
    print()
def welcomePage():
    while True:
        globalVar.printTitle("Welcome")
        print("[1] Login")
        print("[2] Registrasi")
        print("[3] Exit\n")
        print("="*32)

        choose = input("> ")

        if choose == "1":
            os.system("cls")
            menuLogin.menuLogin()
            break

        elif choose == "2":
            os.system("cls")
            menuRegistrasi.menuRegistrasi()

        elif choose == "3":
            print(Fore.CYAN + "\nExiting..." + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            exit()

        elif choose == "":
            print(Fore.RED + "Inputan tidak boleh kosong" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")

        else:
            globalVar.inputanInvalid()