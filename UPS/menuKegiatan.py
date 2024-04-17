from colorama import init, Style
from colorama import init, Fore, Style

import os
import time
import globalVar

def menuKegiatan():
    def tampilkan_alert(pesan, durasi=0.8):
        # Menampilkan pesan alert dan membersihkan layar setelah durasi tertentu.
        print(Fore.RED + pesan + Style.RESET_ALL)
        time.sleep(durasi)
        globalVar.printTitle("Kegiatan")


    def tampilkan_menu_kegiatan():
        print("Menu Kegiatan:")
        print("[1] Donor Darah")
        print("[2] Senam Sehat")
        print("[3] Vaksin Booster")
        print("\n[4] Kembali ke Menu Utama")
        print("\n================================")


    def donor_darah():
        globalVar.printTitle("Kegiatan")
        while True:
            teks_donor_darah = """
DONOR DARAH

Apa itu Donor Darah
Donor darah adalah tindakan sukarela dimana seseorang dengan sukarela memberikan 
sebagian kecil darahnya untuk disumbangkan kepada yang membutuhkan. 
Darah yang didonorkan ini kemudian digunakan dalam berbagai prosedur medis, 
seperti operasi, pengobatan penyakit, dan pemulihan pasien.

Manfaat Donor Darah
1. Menyelamatkan Nyawa:
Donor darah adalah pahlawan tanpa kostum. Darah yang diberikan dapat menyelamatkan 
nyawa pasien yang membutuhkan transfusi darah darurat.

2. Mengatasi Kekurangan Persediaan Darah:
Kekurangan persediaan darah adalah masalah serius di banyak rumah sakit. 
Dengan berpartisipasi dalam donor darah, kita dapat membantu menjaga persediaan 
darah tetap mencukupi untuk kebutuhan medis.

3. Meningkatkan Kesehatan Pribadi:
Rutin mendonorkan darah telah terbukti memiliki manfaat kesehatan untuk donor. 
Ini dapat membantu mengurangi risiko penyakit jantung dan 
meningkatkan kesehatan umum.

Donor darah adalah kegiatan mulia yang dapat menyelamatkan nyawa. Anda dapat berkontribusi
dengan mendonorkan darah Anda untuk membantu orang-orang yang membutuhkan. Proses donor darah
aman dan dilakukan oleh tenaga medis berpengalaman. Yuk, jadilah pahlawan bagi sesama!"""

            print(teks_donor_darah)
            print("\n[1] kembali ke menu sebelumnya")
            print("\n================================")
            pilihan_user = input("> ")
            if pilihan_user == '1':
                break
            else:
                tampilkan_alert("Input tidak valid. Silakan coba lagi.")
                globalVar.printTitle("Kegiatan")
        

    def senam_sehat():
        globalVar.printTitle("Kegiatan") 
        while True:
            teks_senam_sehat ="""
SENAM SEHAT

Merupakan kegiatan yang baik untuk kesehatan tubuh Anda.
Dengan rutin berolahraga, Anda dapat menjaga kebugaran fisik dan mental. 
Ikuti gerakan senam sehat untuk meningkatkan energi dan kebahagiaan dalam kehidupan sehari-hari!

1.Tujuan Utama:
Senam sehat bertujuan untuk meningkatkan kebugaran fisik, termasuk kekuatan otot, keuletan, dan keseimbangan.
Melibatkan aktivitas aerobik yang dapat meningkatkan denyut jantung dan pernapasan, serta meningkatkan sirkulasi darah.

2. Manfaat Kesehatan:
    1). Fisik:
        a. Meningkatkan kekuatan otot dan keuletan.
        b. Membantu mengontrol berat badan dan meningkatkan metabolisme.
        c. Meningkatkan keseimbangan dan koordinasi.

    2). Mental dan Emosional:
        a. Mengurangi stres dan kecemasan.
        b. Meningkatkan suasana hati dan energi.
        c. Memperbaiki kualitas tidur.

    3). Kardiovaskular:
        a. Meningkatkan kapasitas paru-paru dan efisiensi jantung.
        b. Menurunkan risiko penyakit jantung dan tekanan darah tinggi.

3. Berbagai Jenis Senam Sehat:
    1). Senam Aerobik: Melibatkan gerakan berulang dan ritmis, seperti berlari, berjalan cepat, atau mengikuti rutinitas latihan berirama.
    2). Senam Kebugaran: Kombinasi latihan kekuatan, fleksibilitas, dan kardiovaskular untuk meningkatkan kebugaran secara menyeluruh.
    3). Senam Yoga: Kombinasi gerakan tubuh, pernapasan, dan meditasi untuk meningkatkan kesehatan fisik dan mental.
    4). Senam Zumba: Kombinasi gerakan tarian dan latihan kardiovaskular dengan musik berirama.

4. Cara Melakukan Senam Sehat:
    1). Pilih jenis senam yang sesuai dengan kondisi fisik dan preferensi Anda.
    2). Lakukan pemanasan sebelum memulai aktivitas untuk mencegah cedera.
    3). Ikuti petunjuk dan teknik yang benar untuk setiap gerakan.
    4). Lakukan latihan secara teratur, idealnya beberapa kali seminggu."""
            print(teks_senam_sehat)
            print("\n[1] kembali ke menu sebelumnya")
            print("\n================================")
            pilihan_user = input("> ")
            if pilihan_user == '1':
                break
            else:
                tampilkan_alert("Input tidak valid. Silakan coba lagi.")
                globalVar.printTitle("Kegiatan")
        

    def vaksin_booster():
        globalVar.printTitle("Kegiatan")
        while True:
            teks_vaksin =""" 
VAKSIN BOOSTER

adalah dosis tambahan dari vaksin tertentu yang diberikan
setelah dosis-dosis sebelumnya. Tujuan dari vaksin booster 
adalah untuk meningkatkan atau memperpanjang perlindungan 
yang diberikan oleh vaksin sebelumnya. Vaksin booster umumnya 
diberikan setelah beberapa waktu pasca vaksinasi awal.

Vaksinasi awal sering kali melibatkan dua atau lebih dosis 
untuk membangun kekebalan tubuh yang optimal. Namun, 
seiring berjalannya waktu, kekebalan tubuh terhadap penyakit 
tertentu bisa menurun. Dalam beberapa kasus, mungkin diperlukan 
dosis tambahan untuk meningkatkan kekebalan tersebut.

Contoh dari vaksin yang sering memerlukan dosis booster 
adalah vaksin difteri, tetanus, dan pertussis (DTP), 
vaksin hepatitis, dan vaksin polio. Pada beberapa vaksin, 
seperti vaksin COVID-19, vaksin booster dapat diperlukan 
untuk melawan varian-varian baru dari virus.

Pemberian vaksin booster biasanya direkomendasikan oleh otoritas 
kesehatan setelah dilakukan penelitian dan evaluasi terhadap efikasi 
dan keamanan vaksin. Pemberian booster juga dapat menjadi bagian 
dari upaya melawan penyebaran penyakit menular dan memperkuat imunitas kelompok.

"Vaksinasi Booster adalah langkah positif untuk melindungi diri,
keluarga, dan teman-teman. Jadilah pahlawan kesehatan!"""
            print(teks_vaksin)
            print("\n[1] kembali ke menu sebelumnya")
            print("\n================================")
            pilihan_user = input("> ")
            if pilihan_user == '1':
                break
            else:
                tampilkan_alert("Input tidak valid. Silakan coba lagi.")
                globalVar.printTitle("Kegiatan")

            
    #Menampilkan menu kegiatan dan memproses pilihan pengguna.
    while True:
        globalVar.printTitle("Kegiatan") 
        tampilkan_menu_kegiatan()
        pilihan_kegiatan = input("> ")

        if pilihan_kegiatan == "1":
            globalVar.printTitle("Kegiatan")
            donor_darah()

        elif pilihan_kegiatan == "2":
            globalVar.printTitle("Kegiatan")
            senam_sehat()
            
        elif pilihan_kegiatan == "3":
            globalVar.printTitle("Kegiatan")
            vaksin_booster()
           
        elif pilihan_kegiatan == "4":
            break
        else:
            tampilkan_alert("Pilihan tidak valid. Silakan coba lagi.")
            globalVar.printTitle("Kegiatan")
