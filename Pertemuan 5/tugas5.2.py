# Nama : Wahyu Ahmad Yassin
# NIM : 0110224047
# Rombel : TI10

print("""
1. Hitung luas Persegi
2. Hitung luas Lingkarang
3. Hitung luas Segitiga
""")

hitung_luas = int(input("Masukkan angka :"))

match hitung_luas :
  case 1 :
    sisi = int(input("Masukkan sisi :"))
    luas_persegi = sisi **2
    print("Jadi luas persegi adalah", luas_persegi, "cm")
  case 2 :
    r = int(input("Masukkan jari-jari :"))
    luas_lingkaran = 3.14 * r * r
    print("Jadi luas lingkaran adalah", luas_lingkaran, "cm")
  case 3 :
    a = int(input("Masukkan Alas :"))
    t = int(input("Masukkan Tinggi :"))
    luas_segitiga = 1/2 * a * t  
    print("Jadi luas segitiga adalah", luas_segitiga, "cm")
  case _ :
    print("Angka tidak valid")
    