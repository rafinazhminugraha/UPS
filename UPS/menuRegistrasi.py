# ===============================Program Registrasi===================================
from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import re
import menuWelcome

def printTitle():
    os.system("cls")
    print("━━━━━━━━━━━━━━━━━━━━")
    print(f"{Fore.CYAN}\n        UPS")
    print(Style.RESET_ALL)
    print("━━━━━━━━━━━━━━━━━━━━")
    print()


def menuRegistrasi():
    def judul_reg():
        os.system("cls" if os.name == "nt" else "clear")

        panjang_bingkai = 30

        title_length = len("UPS")
        penyesuaian_judul_kiri = (panjang_bingkai - title_length) // 2
        penyesuaian_judul_kanan = penyesuaian_judul_kiri if title_length % 2 == 0 else penyesuaian_judul_kiri + 1

        menu_length = len("Registrasi")
        penyesuaian_menu_kiri = (panjang_bingkai - menu_length) // 2
        penyesuaian_menu_kanan = penyesuaian_menu_kiri if menu_length % 2 == 0 else penyesuaian_menu_kiri + 1

        print("╔" + "═" * panjang_bingkai + "╗")
        print("║" + " " * panjang_bingkai + "║")
        print(f"║{' ' * penyesuaian_judul_kiri}{Fore.CYAN}{Style.BRIGHT}{"UPS"}{Style.RESET_ALL}{' ' * penyesuaian_judul_kanan}║")
        print("║" + " " * panjang_bingkai + "║")
        print("╚" + "═" * panjang_bingkai + "╝")
        print()
        print("=" * (panjang_bingkai + 2))
        print(f"{' ' * penyesuaian_menu_kiri}{"Registrasi"}{' ' * penyesuaian_menu_kanan}")
        print("=" * (panjang_bingkai + 2))
        print()
        print("[>] Kembali")
        print()

    judul_reg()

# ====================Input Nama====================
    nama = input("Nama Lengkap: ")
    while True:
        if nama == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            nama = input("Nama Lengkap: ")

        elif nama == '>':
            os.system("cls")
            return
        
        elif re.match("^[a-zA-Z]+(?: [a-zA-Z]+)*$", nama):
            break

        else:
            print(Fore.RED + "Nama berupa huruf" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            nama = input("Nama Lengkap: ")
    
# ====================Input NIM====================
    nim  = input("NIM: ")
    while True:
        search_ada = os.path.isfile(f"Storage/{nim}.txt")
        if search_ada:
            print(Fore.RED + "Tidak dapat melakukan registrasi, \nNIM Anda sudah terdaftar" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            nim  = input("NIM: ")
        
        elif nim == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            nim  = input("NIM: ")

        elif nim == '>':
            os.system("cls")
            return

        elif len(nim) < 7 or len(nim) > 7:
            print(Fore.RED + "NIM salah" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            nim  = input("NIM: ")

        elif nim.isdigit():
            break

        else:
            print(Fore.RED + "NIM salah" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            nim  = input("NIM: ")

# ====================Input Password====================
    input_password = input("Password (minimal 8 karakter): ")
    while True:
        if input_password == '>':
            os.system("cls")
            return
        
        elif 1 <= len(input_password) < 8:
            print(Fore.RED + "Password minimal 8 karakter" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            input_password = input("Password (minimal 8 karakter): ")

        elif input_password == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            input_password = input("Password (minimal 8 karakter): ")

        elif input_password == '>':
            os.system("cls")
            return

        else:
            break

# ====================Jenis Kelamin====================
    print("Jenis Kelamin: ")
    print(""*10, "[1] Laki-laki")
    print(""*10, "[2] Perempuan")
    pilih_jeniskelamin = input("> ")
    data_jeniskelamin = None

    while True:
        if pilih_jeniskelamin == "1":
            data_jeniskelamin = "Laki-laki"
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            break

        elif pilih_jeniskelamin == "2":
            data_jeniskelamin = "Perempuan"
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            break

        elif pilih_jeniskelamin == '>':
            os.system("cls")
            return
        
        elif pilih_jeniskelamin == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print("Jenis Kelamin: ")
            print(""*10, "[1] Laki-laki")
            print(""*10, "[2] Perempuan")
            pilih_jeniskelamin = input("> ")

        else:
            print(Fore.RED + "Inputan tidak valid" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print("Jenis Kelamin: ")
            print(""*10, "[1] Laki-laki")
            print(""*10, "[2] Perempuan")
            pilih_jeniskelamin = input("> ")

# ====================Alamat Saat Ini====================
    alamatSaatIni = input("Alamat Saat Ini: ")
    while True:
        if alamatSaatIni == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            alamatSaatIni = input("Alamat Saat Ini: ")

        elif alamatSaatIni == '>':
            os.system("cls")
            return

        else:
            break

# ====================Alamat Asal====================
    alamatAsal = input("Alamat Asal: ")
    while True:
        if alamatAsal == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            print(f"Alamat Saat Ini: {alamatSaatIni}")
            alamatAsal = input("Alamat Asal: ")

        elif alamatAsal == '>':
            os.system("cls")
            return

        else:
            break

# ====================Alamat No. Telepon====================
    noTelp = input("No. Telepon (Contoh: 083152445609): ")
    while True:          
        if noTelp == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            print(f"Alamat Saat Ini: {alamatSaatIni}")
            print(f"Alamat Asal: {alamatAsal}")
            noTelp = input("No. Telepon (Contoh: 083152445609): ")
            
        elif noTelp == '>':
            os.system("cls")
            return

        elif 1 <= len(noTelp) < 10 or len(noTelp) > 13:
            print(Fore.RED + "Nomor telepon salah" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            print(f"Alamat Saat Ini: {alamatSaatIni}")
            print(f"Alamat Asal: {alamatAsal}")
            noTelp = input("No. Telepon (Contoh: 083152445609): ")

        elif noTelp.isdigit():
            break

        else:
            print(Fore.RED + "Nomor telepon salah" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            print(f"Alamat Saat Ini: {alamatSaatIni}")
            print(f"Alamat Asal: {alamatAsal}")
            noTelp = input("No. Telepon (Contoh: 083152445609): ")

# ====================Riwayat Penyakit====================
    riwayat = input("Riwayat Penyakit (Jika tidak ada isi (-) saja): ")
    while True:
        if riwayat == "":
            print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            judul_reg()
            print(f"Nama Lengkap: {nama}")
            print(f"NIM: {nim}")
            print(f"Password (minimal 8 karakter): {input_password}")
            print(f"Jenis Kelamin: {data_jeniskelamin}")
            print(f"Alamat Saat Ini: {alamatSaatIni}")
            print(f"Alamat Asal: {alamatAsal}")
            print(f"No. Telepon (Contoh: 083152445609): {noTelp}")
            riwayat = input("Riwayat Penyakit (Jika tidak ada isi (-) saja): ")

        elif riwayat == '>':
            os.system("cls")
            return
        
        else:
            break
    print(Fore.GREEN + "\nRegistrasi berhasil, silahkan login" + Style.RESET_ALL)
    time.sleep(1)
    os.system("cls")

# Memasukan inputan ke data dictionary
    data_user = {
        "Nama Lengkap": nama,
        "NIM": nim,
        "Password": input_password,
        "Jenis Kelamin": data_jeniskelamin,
        "Alamat Saat ini": alamatSaatIni,
        "Alamat Asal": alamatAsal,
        "No. Telepon": noTelp,
        "Riwayat Penyakit": riwayat
    }

# Menyimpan hasil registrasi ke file txt
    with open(f"Storage/{nim}.txt", "w") as file:
        for kunci, nilai in data_user.items():
            file.write(f'{kunci}: {nilai}\n')