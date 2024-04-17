from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import re
import menuProfile
import globalVar

# def printTitle():
#     os.system("cls")
#     print("━━━━━━━━━━━━━━━━━━━━")
#     print(f"{Fore.CYAN}\n        UPS")
#     print(Style.RESET_ALL)
#     print("━━━━━━━━━━━━━━━━━━━━")
#     print()

# user = None
def menuProfile():
    
    def judul_menuProfile():
        os.system("cls" if os.name == "nt" else "clear")

        panjang_bingkai = 30

        title_length = len("UPS")
        penyesuaian_judul_kiri = (panjang_bingkai - title_length) // 2
        penyesuaian_judul_kanan = penyesuaian_judul_kiri if title_length % 2 == 0 else penyesuaian_judul_kiri + 1

        menu_length = len("Profile")
        penyesuaian_menu_kiri = (panjang_bingkai - menu_length) // 2
        penyesuaian_menu_kanan = penyesuaian_menu_kiri if menu_length % 2 == 0 else penyesuaian_menu_kiri + 1

        print("╔" + "═" * panjang_bingkai + "╗")
        print("║" + " " * panjang_bingkai + "║")
        print(f"║{' ' * penyesuaian_judul_kiri}{Fore.CYAN}{Style.BRIGHT}{"UPS"}{Style.RESET_ALL}{' ' * penyesuaian_judul_kanan}║")
        print("║" + " " * panjang_bingkai + "║")
        print("╚" + "═" * panjang_bingkai + "╝")
        print()
        print("=" * (panjang_bingkai + 2))
        print(f"{' ' * penyesuaian_menu_kiri}{"Profile"}{' ' * penyesuaian_menu_kanan}")
        print("=" * (panjang_bingkai + 2))
        print()
        
    def editProfile():
        time.sleep(1)
        judul_menuProfile()
        print("[>] Kembali\n")

    # ====================Input Nama Baru====================
        nama_baru = input("Nama Lengkap: ")
        while True:
            if nama_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                nama_baru = input("Nama Lengkap: ")

            elif nama_baru == '>':
                os.system("cls")
                return
            
            elif re.match("^[a-zA-Z]+(?: [a-zA-Z]+)*$", nama_baru):
                break

            else:
                print(Fore.RED + "Nama berupa huruf" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                nama_baru = input("Nama Lengkap: ")
        
    # ====================Input NIM Baru====================
        nim_baru  = input("NIM: ")
        while True:
            search_ada_ = os.path.isfile(f"Storage/{nim_baru}.txt")
            if search_ada_ and nim_baru != globalVar.nomor_induk_mahasiswa:
                print(Fore.RED + "NIM sudah terdaftar" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                nim_baru = input("NIM: ")

            elif nim_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                nim_baru  = input("NIM: ")

            elif nim_baru == '>':
                os.system("cls")
                return

            elif len(nim_baru) < 7 or len(nim_baru) > 7:
                print(Fore.RED + "NIM salah" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                nim_baru  = input("NIM: ")

            elif nim_baru.isdigit():
                break

            else:
                print(Fore.RED + "NIM salah" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                nim_baru  = input("NIM: ")
                
    # ====================Input Password Baru====================
        input_password_baru = input("Password (minimal 8 karakter): ")
        while True:
            if input_password_baru == '>':
                os.system("cls")
                return
            
            elif 1 <= len(input_password_baru) < 8:
                print(Fore.RED + "Password minimal 8 karakter" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                input_password_baru = input("Password (minimal 8 karakter): ")

            elif input_password_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                input_password_baru = input("Password (minimal 8 karakter): ")

            else:
                break

    # ====================Jenis Kelamin Baru====================
        print("Jenis Kelamin: ")
        print(""*10, "[1] Laki-laki")
        print(""*10, "[2] Perempuan")
        pilih_jeniskelamin_baru = input("> ")
        data_jeniskelamin_baru = None

        while True:
            if pilih_jeniskelamin_baru == "1":
                data_jeniskelamin_baru = "Laki-laki"
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                break

            elif pilih_jeniskelamin_baru == "2":
                data_jeniskelamin_baru = "Perempuan"
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                break

            elif pilih_jeniskelamin_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print("Jenis Kelamin: ")
                print(""*10, "[1] Laki-laki")
                print(""*10, "[2] Perempuan")
                pilih_jeniskelamin_baru = input("> ")
              

            elif pilih_jeniskelamin_baru == '>':
                os.system("cls")
                return

            else:
                print(Fore.RED + "Inputan tidak valid" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print("Jenis Kelamin: ")
                print(""*10, "[1] Laki-laki")
                print(""*10, "[2] Perempuan")
                pilih_jeniskelamin_baru = input("> ")

    # ====================Alamat Saat Ini Baru====================
        alamatSaatIni_baru = input("Alamat Saat Ini: ")
        while True:
            if alamatSaatIni_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                alamatSaatIni_baru = input("Alamat Saat Ini: ")

            elif alamatSaatIni_baru == '>':
                os.system("cls")
                return

            else:
                break

    # ====================Alamat Asal Baru====================
        alamatAsal_baru = input("Alamat Asal: ")
        while True:
            if alamatAsal_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                print(f"Alamat Saat Ini: {alamatSaatIni_baru}")
                alamatAsal_baru = input("Alamat Asal: ")

            elif alamatAsal_baru == '>':
                os.system("cls")
                return

            else:
                break

    # ====================No. Telepon Baru====================
        noTelp_baru = input("No. Telepon (Contoh: 083152445609): ")
        while True:          
            if noTelp_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                print(f"Alamat Saat Ini: {alamatSaatIni_baru}")
                print(f"Alamat Asal: {alamatAsal_baru}")
                noTelp_baru = input("No. Telepon (Contoh: 083152445609): ")

            elif noTelp_baru == '>':
                os.system("cls")
                return
                
            elif 1 <= len(noTelp_baru) < 10 or len(noTelp_baru) > 13:
                print(Fore.RED + "Nomor telepon salah" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                print(f"Alamat Saat Ini: {alamatSaatIni_baru}")
                print(f"Alamat Asal: {alamatAsal_baru}")
                noTelp_baru = input("No. Telepon (Contoh: 083152445609): ")

            elif noTelp_baru.isdigit():
                break

            else:
                print(Fore.RED + "Nomor telepon salah" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                print(f"Alamat Saat Ini: {alamatSaatIni_baru}")
                print(f"Alamat Asal: {alamatAsal_baru}")
                noTelp_baru = input("No. Telepon (Contoh: 083152445609): ")

    # ====================Riwayat Penyakit Baru====================
        riwayat_baru = input("Riwayat Penyakit (Jika tidak ada isi (-) saja): ")
        while True:
            if riwayat_baru == "":
                print(Fore.RED + "Wajib di isi" + Style.RESET_ALL)
                time.sleep(1)
                os.system("cls")
                judul_menuProfile()
                print("[>] Kembali\n")
                print(f"Nama Lengkap: {nama_baru}")
                print(f"NIM: {nim_baru}")
                print(f"Password (minimal 8 karakter): {input_password_baru}")
                print(f"Jenis Kelamin: {data_jeniskelamin_baru}")
                print(f"Alamat Saat Ini: {alamatSaatIni_baru}")
                print(f"Alamat Asal: {alamatAsal_baru}")
                print(f"No. Telepon (Contoh: 083152445609): {noTelp_baru}")
                riwayat_baru = input("Riwayat Penyakit (Jika tidak ada isi (-) saja): ")

            elif riwayat_baru == '>':
                os.system("cls")
                return
            
            else:
                break

    # Memasukan inputan ke data dictionary
        data_user = {
            "Nama Lengkap": nama_baru,
            "NIM": nim_baru,
            "Password": input_password_baru,
            "Jenis Kelamin": data_jeniskelamin_baru,
            "Alamat Saat ini": alamatSaatIni_baru,
            "Alamat Asal": alamatAsal_baru,
            "No. Telepon": noTelp_baru,
            "Riwayat Penyakit": riwayat_baru
        }
        
    # Menyimpan hasil registrasi ke file txt
        with open(f"Storage/{globalVar.nomor_induk_mahasiswa}.txt", "w") as file:
            for kunci, nilai in data_user.items():
                file.write(f'{kunci}: {nilai}\n')
                
    #mengubah nama
        nim_lama = globalVar.nomor_induk_mahasiswa
        os.rename(f"Storage/{nim_lama}.txt", f"Storage/{nim_baru}.txt")
        globalVar.nomor_induk_mahasiswa = nim_baru
        
        print(f"{Fore.GREEN}\nBiodata Pengguna Berhasil Di Update.")
        print(Style.RESET_ALL)
        time.sleep(1)

    while True:
        judul_menuProfile()
        with open(f"Storage/{globalVar.nomor_induk_mahasiswa}.txt", "r") as file:
            for baris in file:
                key, value = baris.strip().split(":")
                print(f"{key:<16} : {value}")
        
        print("\n[1] Edit Profile")
        print("[2] Kembali Ke Menu Utama\n")
        print("=" * 32)

        pilih_menuProfile = input("> ")
        if pilih_menuProfile == "1":
            editProfile()

        elif pilih_menuProfile == "2":
            os.system("cls")
            return

        elif pilih_menuProfile == "":
            print(Fore.RED + "Inputan tidak valid" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            menuProfile()
        
        else:
            print(Fore.RED + "Inputan tidak valid" + Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            menuProfile()
        