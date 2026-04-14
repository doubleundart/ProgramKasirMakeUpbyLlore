def menu() :
    print("\nMenu Edit Add-Ons :")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Done Editing Add-Ons \n")

def create(pilihan2, item) :
    pilihan2.append(item)
    print("Add-Ons Berhasil Ditambahkan!")
    print("") 

def read(pilihan2) :
    print("Add-Ons yang Dipilih :")
    for i in range(len(pilihan2)) :
        print(f"{i + 1}. {pilihan2[i]}")
    print("")

def update(pilihan2, index, item) :
    pilihan2[index] = item
    print("Add-Ons Berhasil DiUpdate.")
    print("")

def delete(pilihan2, index) :
    del pilihan2[index]
    print("Add-Ons Berhasil Dihapus.")
    print("")