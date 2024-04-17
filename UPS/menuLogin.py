# ===========================================Program Login==============================================
from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import menuWelcome
import globalVar


def printTitle():
    os.system("cls")
    print("━━━━━━━━━━━━━━━━━━━━")
    print(f"{Fore.CYAN}\n        UPS")
    print(Style.RESET_ALL)
    print("━━━━━━━━━━━━━━━━━━━━")
    print()
    
user = None

def menuLogin():
    global user
    global status_login
    def judul_login():
        os.system("cls" if os.name == "nt" else "clear")

        panjang_bingkai = 30

        title_length = len("UPS")
        penyesuaian_judul_kiri = (panjang_bingkai - title_length) // 2
        penyesuaian_judul_kanan = penyesuaian_judul_kiri if title_length % 2 == 0 else penyesuaian_judul_kiri + 1

        menu_length = len("Login")
        penyesuaian_menu_kiri = (panjang_bingkai - menu_length) // 2
        penyesuaian_menu_kanan = penyesuaian_menu_kiri if menu_length % 2 == 0 else penyesuaian_menu_kiri + 1

        print("╔" + "═" * panjang_bingkai + "╗")
        print("║" + " " * panjang_bingkai + "║")
        print(f"║{' ' * penyesuaian_judul_kiri}{Fore.CYAN}{Style.BRIGHT}{"UPS"}{Style.RESET_ALL}{' ' * penyesuaian_judul_kanan}║")
        print("║" + " " * panjang_bingkai + "║")
        print("╚" + "═" * panjang_bingkai + "╝")
        print()
        print("=" * (panjang_bingkai + 2))
        print(f"{' ' * penyesuaian_menu_kiri}{"Login"}{' ' * penyesuaian_menu_kanan}")
        print("=" * (panjang_bingkai + 2))
        print()
        print("[>] Kembali")
        print()

    # status_login = False
    judul_login()

# Input NIM yang terdaftar saat registrasi
    nim_login = input("NIM: ")
    while True:
        berkas_ada = os.path.isfile(f"Storage/{nim_login}.txt")
        if berkas_ada:
            break

        elif nim_login == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_login()
            nim_login = input("NIM: ")

        elif nim_login == ">":
            os.system("cls")
            return

        else:
            print(Fore.RED + "NIM salah" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_login()
            nim_login = input("NIM: ")
    globalVar.nomor_induk_mahasiswa = nim_login

# Mengubah file txt menjadi data list
    list_data = []
    file_txt = (f"Storage/{nim_login}.txt")
    if os.path.exists(file_txt):
        with open(file_txt, "r") as file:
            lines = file.readlines()
            
        for line in lines:
            newLine = line.strip().split(":")
            list_data.append(newLine)

        for item in list_data:
            break
 
# Input nama user yang terdaftar saat registrasi      
    nama_akun = input("Nama Akun: ")
    while True:
        if nama_akun == list_data[0][1].strip():
            break

        elif nama_akun == "":
            print(Fore.RED + "Masukan nama akun Anda" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_login()
            print(f"NIM: {nim_login}")
            nama_akun = input("Nama Akun: ")

        elif nama_akun == ">":
            os.system("cls")
            return

        else: 
            print(Fore.RED + "Pengguna tidak ditemukan" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_login()
            print(f"NIM: {nim_login}")
            nama_akun = input("Nama Akun: ")

# Input password yang terdaftar saat registrasi
    login_password = input("Password: ")
    while True:
        if login_password == list_data[2][1].strip():
            print(Fore.GREEN + "\nLogin Berhasil" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            globalVar.status_login = True
            break
            
        elif login_password == "":
            print(Fore.RED + "Masukan password Anda" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_login()
            print(f"NIM: {nim_login}")
            print(f"Nama Akun: {nama_akun}")
            login_password = input("Password: ")
            
        elif login_password == ">":
            os.system("cls")
            return
    
        else:
            print(Fore.RED + "Password salah!" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_login()
            print(f"NIM: {nim_login}")
            print(f"Nama Akun: {nama_akun}")
            login_password = input("Password: ")
            