from tracemalloc import stop


print("=== KALKULATOR ===\n")
print("Pilihan Menu: ")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = int(input("Masukkan Pilihan Anda: "))

while pilihan != "Q":
    pertama = int(input("Bilangan Pertama: "))
    kedua = int(input("Bilangan Kedua: "))
    if pilihan == 1:
        tambah = pertama + kedua
        print(tambah)
    elif pilihan == 2:
        kurang = pertama - kedua
        print(kurang)
    elif pilihan == 3:
        kali = pertama * kedua
        print(kali)
    elif pilihan == 4:
        bagi = pertama / kedua
        print(bagi)
    else:
        stop
