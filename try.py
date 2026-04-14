import crud
import menu1
import datetime

harga = 0
harga1 = 0
pilihan = []
pilihan2 = []

menu1.tampilan_awal()

while True :
    choice = int(input("Pilih Make Up Style (1/2/3/4) \t\t:\t     "))
    if choice == 1 :
        harga1 += 80000
        print("Make Up Style \t\t\t\t:   Graduation", "\n")
        pilihan.append("Graduation")
        break
    elif choice == 2 :
        harga1 += 95000
        pilihan.append("Party")
        print("Make Up Style \t\t\t\t:        Party", "\n")
        break
    elif choice == 3 :
        harga1 += 150000
        pilihan.append("Bridesmaid")
        print("Make Up Style \t\t\t\t:   Bridesmaid", "\n")
        break
    elif choice == 4 :
        harga1 += 1000000
        pilihan.append("Wedding")
        print("Make Up Style \t\t\t\t:      Wedding", "\n")
        break
    else :
        print("Pilihan Tidak Tersedia!\n")

menu1.mengganti_pesanan(pilihan, harga1)

jumlah_orang = int(input("Untuk Berapa Orang\t\t\t:\t     "))
print("")

harga += harga1
harga1 *= jumlah_orang

menu1.tambahan()

for i in range (1, jumlah_orang + 1) :
    harga2 = 0
    print("\t")
    people = input(f"Nama Orang ke-{i}\t\t\t\t:\t")
    with open("file.txt", "a") as file :
        file.write(f"an. {people}\n")
    while True :
        choice1 = int(input(f"Pilih Add-Ons {people} (1/2/3/4) \t\t:\t     "))
        if choice1 == 1 :
            print(f"{people} Menambahkan Eyelashes!", "\n")
            pilihan2.append("Eyelashes")
        elif choice1 == 2 :
            print(f"{people} Menambahkan Softlens!", "\n")
            pilihan2.append("Softlens")
        elif choice1 == 3 :
            print(f"{people} Menambahkan Hair Styling!", "\n")
            pilihan2.append("Hair Styling")
        elif choice1 == 4 :
            print(f"{people} Sudah Menyelesaikan Add-Ons!", "\n")
            print("─"*54)
            break
        else :
            print("Pilihan Tidak Tersedia!\n")
        
    crud.menu()
    while True :
        crud_choice = int(input("Pilih Menu Options (1/2/3/4/5) \t\t:\t     "))
        if crud_choice == 1 :
            menu1.tambahan_baru()
            print("")
            item = int(input("Masukkan Nomor Add-Ons yang Ingin Ditambahkan : "))
            if item == 1 :
                item = "Eyelashes"
            elif item == 2 :
                item = "Softlens" 
            elif item == 3 :
                item = "Hair Styling"
            crud.create(pilihan2, item)
        elif crud_choice == 2 :
            crud.read(pilihan2)
        elif crud_choice == 3 :
            index = int(input("Masukkan Index Add-Ons yang Ingin Diupdate :\t     ")) - 1
            print("")
            menu1.tambahan_baru()
            print("")
            nomor = int(input("Masukkan Nomor Add-Ons Baru \t\t:\t     "))
            if nomor == 1 :
                item = "Eyelashes"
            elif nomor == 2 :
                item = "Softlens"
            elif nomor == 3 :
                item = "Hair Styling"
            crud.update(pilihan2, index, item)
        elif crud_choice == 4 :
            index = int(input("Masukkan Nomor Add-Ons yang Ingin Dihapus  :\t     ")) - 1
            crud.delete(pilihan2, index)
        elif crud_choice == 5 :
            print("Mengakhiri Menu Edit Add-Ons!")
            break
        else :
            print("Pilihan Tidak Tersedia!\n")
    
    for j in range(len(pilihan2)) :
        if pilihan2[j] == "Eyelashes" :
            harga2 += 30000
            with open("file.txt", "a") as file :
                file.write("  + Eyelashes\n")
        elif pilihan2[j] == "Softlens" :
            harga2 += 50000
            with open("file.txt", "a") as file :
                file.write("  + Softlens\n")
        elif pilihan2[j] == "Hair Styling" :
            harga2 += 150000
            with open("file.txt", "a") as file :
                file.write("  + Hair Styling\n")

    harga += harga2
    pilihan2.clear()

while True :
    booking = int(input("\nIngin Booking Pada Tanggal Berapa       :\t    "))
    if booking in menu1.booking_list() :
        print("Tanggal Ini Sudah Ter-Booking!")
    else :
        print(f"Anda Mem-Booking Pada Tanggal\t\t\t    {booking}")
        print("")
        menu1.booking_list().append(booking)
        break

menu1.payment(harga)
with open("file.txt", "a") as file :
    file.write(f"\nTotal Harga\t\t\t\t     Rp{harga}\nKembalian\t\t\t\t     Rp{menu1.kembalian}")

print("\n", "-"*54, "\n")
print("𝜗ৎ MAKE UP by ʟʟօʀɛ 𝜗ৎ".center(54, " "))
print("(213)645 345 534".center(54, " "))
print(" Jl. Coquette, Paris".center(54, " "), "\n")
print("-"*54, "\n")
print(jumlah_orang, "x",pilihan[0], " "*25, "    Rp", harga1)
print("    Date Booking\t\t\t\t   ", booking, "\n")

with open("file.txt", "r") as file :
    print(file.read())

menu1.waktu()

with open("file.txt", "w") as file :
    file.write("")

waktu = datetime.datetime.now()
tanggal = f"{waktu.day}-{waktu.month}-{waktu.year}"
jam = f"{waktu.hour}:{waktu.minute}:{waktu.second}"

with open("file2.txt", "a") as file :
    file.write(f"{tanggal} {jam} on {booking} = Rp{harga}\n\n")