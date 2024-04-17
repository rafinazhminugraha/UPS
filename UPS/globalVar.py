from colorama import init, Style
from colorama import init, Fore, Style

import os
import time

init()

status_login = False
nomor_induk_mahasiswa = None

def inputanInvalid():
    print(f"{Fore.RED}Inputan tidak valid")
    print(Style.RESET_ALL)
    time.sleep(1)
def printTitle(menu):
    os.system("cls" if os.name == "nt" else "clear")

    panjang_bingkai = 30

    title_length = len("UPS")
    penyesuaian_judul_kiri = (panjang_bingkai - title_length) // 2
    penyesuaian_judul_kanan = penyesuaian_judul_kiri if title_length % 2 == 0 else penyesuaian_judul_kiri + 1

    menu_length = len(menu)
    penyesuaian_menu_kiri = (panjang_bingkai - menu_length) // 2
    penyesuaian_menu_kanan = penyesuaian_menu_kiri if menu_length % 2 == 0 else penyesuaian_menu_kiri + 1

    print("╔" + "═" * panjang_bingkai + "╗")
    print("║" + " " * panjang_bingkai + "║")
    print(f"║{' ' * penyesuaian_judul_kiri}{Fore.CYAN}{Style.BRIGHT}{"UPS"}{Style.RESET_ALL}{' ' * penyesuaian_judul_kanan}║")
    print("║" + " " * panjang_bingkai + "║")
    print("╚" + "═" * panjang_bingkai + "╝")
    print()
    print("=" * (panjang_bingkai + 2))
    print(f"{' ' * penyesuaian_menu_kiri}{menu}{' ' * penyesuaian_menu_kanan}")
    print("=" * (panjang_bingkai + 2))
    print()

printTitle("kegiatan")