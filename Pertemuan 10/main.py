import arimatika as art

def hitungan_arimatika():
    print("\nPilih Operasi Arimatika yang ingin dilakukan : ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    pilihan = int(input("Masukkan Pilihan : "))

    if pilihan == 1:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print("Hasil penjumlahan dari", a, "dan", b, "adalah", art.tambah(a, b))
    elif pilihan == 2:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print("Hasil pengurangan dari", a, "dan", b, "adalah", art.kurang(a, b))
    elif pilihan == 3:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print("Hasil perkalian dari", a, "dan", b, "adalah", art.kali(a, b))
    elif pilihan == 4:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print("Hasil pembagian dari", a, "dan", b, "adalah", art.bagi(a, b))
    elif pilihan == 5:  
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        print("Hasil pangkat dari", a, "dan", b, "adalah", art.pangkat(a, b))    
    else:
        print("Pilihan tidak valid")    

if __name__ == "__main__" :
    hitungan_arimatika() 