import bangundatar as bd
import bangunruang as br

print("===================================")
print("Pilih Operasi yang mau dilakukan : ")
print("1. Bangun Datar")
print("2. Bangun Ruang")
pilihan = int(input("Masukkan Pilihan : "))

if pilihan == 1 :
    print("1. Persegi Panjang")
    print("2. Persegi")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Trapesium")
    pilihan2 = int(input("Masukkan Pilihan : "))
    if pilihan2 == 1 :
        panjang = int(input("Masukkan panjang : "))
        luas = int(input("Masukkan Luas : "))
        bd.luas_persegi_panjang(panjang, luas)
    elif pilihan2 == 2 :
        sisi = int(input("Masukkan sisi : "))
        bd.luas_persegi(sisi)
    elif pilihan2 == 3 :
        alas = int(input("Masukkan Alas : "))
        tinggi = int(input("Masukkan Tinggi : "))
        bd.luas_segitiga(alas, tinggi)
    elif pilihan2 == 4 :
        jari_jari = int(input("Masukkan Jari Jari :"))
        bd.luas_lingkaran(jari_jari)
    elif pilihan2 == 5 :
        diagonal1 = int(input("Masukkan Diagonal 1 : "))
        diagonal2 = int(input("Masukkan Diagonal 2 : "))
        bd.luas_belah_ketupat(diagonal1, diagonal2)
    else :
        print("Pilihan tidak valid")

elif pilihan == 2 :
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Bola")
    print("5. Kerucut")
    pilihan3 = int(input("Masukkan Pilihan : "))
    if pilihan3 == 1 :
        sisi = int(input("Masukkan Sisi : "))
        br.volume_kubus(sisi)
    elif pilihan3 == 2 :
        panjang = int(input("Masukkan Panjang : "))
        lebar = int(input("Masukkan Lebar : "))
        tinggi = int(input("Masukkan Tinggi : "))
        br.volume_balok(panjang, lebar, tinggi)
    elif pilihan3 == 3 :
        jari_jari = int(input("Masukkan Jari Jari : "))
        tinggi = int(input("Masukkan Tinggi : "))
        br.volume_tabung(jari_jari, tinggi)
    elif pilihan3 == 4 :
        jari_jari = int(input("Masukkan Jari Jari : "))
        br.volume_bola(jari_jari)
    elif pilihan3 == 5 :
        jari_jari = int(input("Masukkan Jari Jari : "))
        sudut = int(input("Masukkan Sudut Pelukis : "))
        br.luas_kerucut(jari_jari, sudut)
    else :
        print("Pilihan tidak valid")

else :
    print("Pilihan tidak valid")