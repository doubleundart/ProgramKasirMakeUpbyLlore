import datetime
import random

def tampilan_awal() :
    print("="*54)
    print("|", " "*50, "|")
    print("|", "𝜗ৎ PRICELIST MAKE UP 𝜗ৎ".center(50, " "), "|")
    print("|", "by ʟʟօʀɛ".center(50, " "), "|")
    print("|", " "*50, "|")
    print("="*54)
    print("|", " "*50, "|")
    print("| 1. Graduation\t\t ────\t""\t    Rp80.000 |")
    print("|", " "*50, "|")
    print("| 2. Party\t\t ────\t""\t    Rp95.000 |")
    print("|", " "*50, "|")
    print("| 3. Bridesmaid\t\t ────\t""\t   Rp150.000 |")
    print("|", " "*50, "|")
    print("| 4. Wedding\t\t ────""\t\t Rp1.000.000 |")
    print("|", " "*50, "|")
    print("="*54, "\n")

def mengganti_pesanan(pilihan, harga1) :
    ganti = input("Apakah Ingin Mengganti Make Up Style?(y/n) :\t     ")
    print("\t")
    if ganti.lower() == 'y' :
        pilihan.pop(0)
        harga1 = 0
        while True :
            choice = int(input("Pilih Make Up Style (1/2/3/4) \t\t:\t     "))
            if choice == 1 :
                harga1 = 80000
                print("Make Up Style \t\t\t\t:   Graduation", "\n")
                pilihan.append("Graduation")
                break
            elif choice == 2 :
                harga1 = 95000
                print("Make Up Style \t\t\t\t:        Party", "\n")
                pilihan.append("Party")
                break
            elif choice == 3 :
                harga1 = 150000
                print("Make Up Style \t\t\t\t:   Bridesmaid", "\n")
                pilihan.append("Bridesmaid")
                break
            elif choice == 4 :
                harga1 = 1000000
                print("Make Up Style \t\t\t\t:      Wedding", "\n")
                pilihan.append("Wedding")
                break
            else :
                print("Pilihan Tidak Tersedia!\n")

def tambahan() :
    print("="*54)
    print("|", " "*50, "|")
    print("|", "𝜗ৎ ADD-ONS MAKE UP 𝜗ৎ".center(50, " "), "|")
    print("|", "by ʟʟօʀɛ".center(50, " "), "|")
    print("|", " "*50, "|")
    print("="*54)
    print("|", " "*50, "|")
    print("| 1. Eyelashes\t\t ────\t""\t    Rp30.000 |")
    print("|", " "*50, "|")
    print("| 2. Softlens\t\t ────\t""\t    Rp50.000 |")
    print("|", " "*50, "|")
    print("| 3. Hair Styling\t ────""\t\t   Rp150.000 |")
    print("|", " "*50, "|")
    print("| 4. Done\t\t     ""\t\t\t     |")
    print("|", " "*50, "|")
    print("="*54)

def tambahan_baru() :
    print("="*54)
    print("|", " "*50, "|")
    print("|", "𝜗ৎ ADD-ONS MAKE UP 𝜗ৎ".center(50, " "), "|")
    print("|", "by ʟʟօʀɛ".center(50, " "), "|")
    print("|", " "*50, "|")
    print("="*54)
    print("|", " "*50, "|")
    print("| 1. Eyelashes\t\t ────\t""\t    Rp30.000 |")
    print("|", " "*50, "|")
    print("| 2. Softlens\t\t ────\t""\t    Rp50.000 |")
    print("|", " "*50, "|")
    print("| 3. Hair Styling\t ────""\t\t   Rp150.000 |")
    print("|", " "*50, "|")
    print("="*54)

def booking_list() :
    book = random.sample(range(1, 31), 15)
    return book

def payment(harga) :
    global bayar, kembalian
    print("-"*54)
    print("Total Harga\t\t\t\t:  Rp", harga)
    print("")
    while True :
        bayar = int(input("Masukkan Jumlah Uang Anda\t\t: Rp "))
        if bayar < harga :
            print("Uang Anda Kurang! Silahkan Masukkan Ulang.\n")
        else :
            kembalian = bayar - harga
            print("Kembalian\t\t\t\t:\t     Rp", kembalian)
            break

def waktu() :
    print("-"*54, "\n")
    print("Thank You".center(54, " "))
    print("Kritik & Saran : +33 1 40996788".center(54, " "))
    print("Email : makeupbyllore@love.com".center(54, " "))
    print("Instagram : @makeupbyllore".center(54, " "), "\n")
    print("────────────────୨ৎ────────────────".center(54, " "), "\n")
    waktu = datetime.datetime.now()
    tanggal = f"{waktu.day}-{waktu.month}-{waktu.year}"
    jam = f"{waktu.hour}:{waktu.minute}:{waktu.second}"
    print(f"Date : {tanggal}    Time : {jam}".center(54, " "))
    print("\n", "-"*54)