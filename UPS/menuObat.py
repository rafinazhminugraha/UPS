import os
import time
from colorama import Fore, Style
import globalVar


from colorama import Style
from colorama import Fore, Style

def menuObat():

    def tampilkan_alert(pesan, durasi=0.8):
        # Menampilkan pesan alert dan membersihkan layar setelah durasi tertentu.
        print(Fore.RED + pesan + Style.RESET_ALL)
        time.sleep(durasi)
        globalVar.printTitle("Obat")

    def tampilkan_menu_obat():
        print("[1] Paracetamol")
        print("[2] Aspirin")
        print("[3] Warfarin")
        print("[4] Antibiotik")
        print("[5] Metformin")
        print("[6] Promaag")
        print("[7] Bodrex")
        print("[8] Paramex")
        print("[9] Betadine")
        print("[10] Sanmol")
        print("\n[11] Cari Obat")
        print("[12] Kembali ke Menu Utama")
        print("\n================================")

    def tampilkan_informasi_obat(nama_obat, obat_info):
        # Menampilkan informasi obat berdasarkan nama obat.
        obat = obat_info.get(nama_obat.lower())

        if obat:
            while True:
                globalVar.printTitle("Obat")
                print(f"Nama obat: {nama_obat}.")
                print(f"Jenis obat: {obat['Jenis obat']}")
                print(f"Isi: {obat['isi']}")
                print(f"Kemasan: {obat['Kemasan']}")
                print("\n[1] kembali ke menu sebelumnya")
                print("\n================================")
                pilihan_user = input("> ")
                if pilihan_user == '1':
                    break
                else:
                    tampilkan_alert("Input tidak valid. Silakan coba lagi.")
        else:
            while True:
                tampilkan_alert("Obat tidak ditemukan.")
                print("\n[1] kembali ke menu sebelumnya")
                print("\n================================")
                pilihan_user = input("> ")
                if pilihan_user == '1':
                    break
                else:
                    tampilkan_alert("Input tidak valid. Silakan coba lagi.")
   

    def cari_obat(nama_obat, obat_info):
        return obat_info.get(nama_obat.lower())
        

        
    obat_info = {
        "paracetamol": {"Jenis obat": "Analgesik (penghilang rasa sakit) dan antipiretik (penurun demam).", "isi": "Tablet", "Kemasan": "Kemasan kotak"},
        "aspirin": {"Jenis obat": "Obat analgesik yang sering digunakan untuk meredakan rasa sakit ringan.", "isi": "Tablet", "Kemasan": "Kemasan kotak"},
        "warfarin": {"Jenis obat": "Obat yang digunakan untuk mengobati koagulasi gula darah.", "isi": "Tablet", "Kemasan": "Botol"},
        "antibiotik": {"Jenis obat": "Obat yang digunakan untuk mengobati infeksi bakteri.", "isi": "Kapsul", "Kemasan": "Blister"},
        "metformin": {"Jenis obat": "Obat yang digunakan untuk mengatur tekanan darah pada pasien diabetes melitus tipe 2.", "isi": "Tablet", "Kemasan": "Blister"},
        "promaag": {"Jenis obat": "Obat yang digunakan untuk meredakan gejala maag atau gangguan pencernaan.", "isi": "Tablet", "Kemasan": "Sachet"},
        "bodrex": {"Jenis obat": "Digunakan untuk meredakan sakit kepala, demam, dan gejala flu atau alergi ringan.", "isi": "Tablet", "Kemasan": "Sachet"},
        "paramex": {"Jenis obat": "Digunakan sebagai analgesik dan antipiretik.", "isi": "Tablet", "Kemasan": "Sachet"},
        "betadine": {"Jenis obat": "Untuk membersihkan dan mencegah infeksi pada luka atau luka bakar.", "isi": "Krim", "Kemasan": "Botol"},
        "sanmol": {"Jenis obat": "Digunakan sebagai analgesik dan antipiretik.", "isi": "Tablet", "Kemasan": "Sachet"}
    }

        # Menampilkan menu obat dan memproses pilihan pengguna.
    while True:
        globalVar.printTitle("Obat") 
        tampilkan_menu_obat()
        pilihan_obat = input("> ")

        if pilihan_obat == "11":
            globalVar.printTitle("Obat")
            while True:
                print("[>] Kembali\n")
                nama_obat = input("Masukkan nama obat yang ingin dicari: ")
                if nama_obat == ">":
                   break 
                elif not nama_obat:
                    tampilkan_alert("Nama obat wajib diisi!")
                    continue  # Minta pengguna untuk mengisi nama obat lagi

                obat = cari_obat(nama_obat, obat_info)
                
                if obat:
                    tampilkan_informasi_obat(nama_obat, obat_info)
                    
                    break
                else:
                    tampilkan_alert("Obat tidak ditemukan.")   
        elif pilihan_obat == "12":
            break
        elif pilihan_obat.isdigit() and 1 <= int(pilihan_obat) <= 10: # Memeriksa apakah pilihan obat merupakan digit dan berada dalam rentang 1 hingga 10.
            obat_key = list(obat_info.keys())[int(pilihan_obat) - 1] # Mendapatkan kunci obat berdasarkan indeks pilihan pengguna.
            tampilkan_informasi_obat(obat_key, obat_info) 
        else:
            tampilkan_alert("Pilihan tidak valid. Silakan coba lagi.")
