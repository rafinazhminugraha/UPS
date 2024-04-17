from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import globalVar
    
def menuTentangKami():

    # Menu Sejarah Poliklinik di Menu Tentang Kami
    def menusejarahpoliklinik():
        globalVar.printTitle("Tentang Kami")
        while True:
            sejarahpoliklinik = '''
Sejarah Poliklinik UPI Cibiru

Menurut SOTK ( SUSUNAN ORGANISASI TATAKERJA), Bu Gira menjabat sebagai kepala poliklinik Di UPI Cibiru. 
Poliknilik UPI Cibiru merupakan SK penanggung jawab terpisah. Bu Gira di-SK kan sebagai pengelola keperawatan berada di Bumsil. 
UPI Bumsil menyurat tugaskan Bu Gira di poliklinik UPI Cibiru dalam seminggu 2x di hari selasa dan kamis. Bagaimana dengan dana 
operasionalnya seperti pembelian obat, kasa? RAB (Rencana Anggaran Biaya) untuk poliklinik UPI Cibiru tersendiri belum ada, 
dan masih tergabung dengan RAB Bumsil. Pengelolaan keperawatan di poliklinik UPI Cibiru sekarang belum berstatus 
klinik pratama (pengelolaannya belum ditangani oleh dokter, belum memiliki perawat, farmasi, dll). 

Mengapa poliklinik UPI Cibiru pindah ke depan?
Karena akan ada dokter dari FIP, dan Sistem Informasi Pelaporan Perusahaan (SIPP) sudah keluar yang menandakan 
beliau akan praktek di UPI Cibiru pada tahun 2020. Namun yang jadi permasalahan adalah saat itu sampai saat ini 
beliau sakit sehingga tidak bisa melanjutkan.'''
            print(sejarahpoliklinik)
            print("\n[1] Kembali\n")
            print("=" * 32)
            menukembalitentangkami = input("> ")
            if menukembalitentangkami == "1":
                break
            else:
                globalVar.inputanInvalid()
                globalVar.printTitle("Tentang Kami")


    # Menu Jabatan Poliklinik di Menu Tentang Kami
    def menujabatanpoliklinik():
        globalVar.printTitle("Tentang Kami")
        while True:
            jabatanpolikninik = "Bu Gira: Pengelola dan penanggungjawab poliklinik\nBu Pone: Pengadministrasi umum\n"
            print("Struktur Poliklinik UPI Cibiru\n")
            print(jabatanpolikninik)
            print("[1] Kembali\n")
            print("=" * 32)
            menukembalitentangkami = input("> ")
            if menukembalitentangkami == "1":
                break
            else:
                globalVar.inputanInvalid()
                globalVar.printTitle("Tentang Kami")
        

    # Menu Jabatan KSR di Menu Tentang Kami
    def menujabatanksr():
        globalVar.printTitle("Tentang Kami")
        while True:
            jabatanksr = """
TIM KSR

Anggota Divisi Humas: 
• Firli RucitaInsania Kumala
• Diah Sukma, Syarifah Dwi

Anggota Divisi Pengabdian: 
• Siti Zahra
• Atikah
• Fatimah\n"""
            print(jabatanksr)
            print("[1] Kembali\n")
            print("=" * 32)
            menukembalitentangkami = input("> ")
            if menukembalitentangkami == "1":
                break
            else:
                globalVar.inputanInvalid()
                globalVar.printTitle("Tentang Kami")


    # Menu Tim Pengembang di Menu Tentang Kami
    def menuTimPengembang():
        globalVar.printTitle("Tentang Kami")
        while True:
            tim_pengembang = """
TIM PENGEMBANG

Project Manager:
• Rafi Nazhmi Nugraha

Anggota:
• Gregorius Christian Sunaryo
• Rahma Dina Ariyanti
• Satrio Waskito"""
            print(tim_pengembang)
            print("\n[1] Kembali\n")
            print("=" * 32)
            menukembalitentangkami = input("> ")
            if menukembalitentangkami == "1":
                break
            else:
                globalVar.inputanInvalid()
                globalVar.printTitle("Tentang Kami")
                
                
    while True:
        globalVar.printTitle("Tentang Kami")
        print("[1] Sejarah Poliklinik")
        print("[2] Struktur Poliklinik UPI Cibiru")
        print("[3] Tim KSR")
        print("[4] Tim Pengembang\n")
        print("[5] Kembali\n")
        print("=" * 32)

        masukkan_angka_menutentangkami = input("> ")
        if masukkan_angka_menutentangkami == "1":
            globalVar.printTitle("Tentang Kami")
            menusejarahpoliklinik()
        elif masukkan_angka_menutentangkami == "2":
            globalVar.printTitle("Tentang Kami")
            menujabatanpoliklinik()
        elif masukkan_angka_menutentangkami == "3":
            globalVar.printTitle("Tentang Kami")
            menujabatanksr()
        elif masukkan_angka_menutentangkami == "4":
            globalVar.printTitle("Tentang Kami")
            menuTimPengembang()
        elif masukkan_angka_menutentangkami == "5":
            break
        else:
            globalVar.inputanInvalid()
            globalVar.printTitle("Tentang Kami")