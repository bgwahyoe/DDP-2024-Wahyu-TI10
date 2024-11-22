# Pendeklarasi fungsi
def hello():
    print("Hello ini adalah fungsi helo")
    print("selamat datang di nurul fikri")

# Panggil Fungsi Hello
hello()
hello()

def cetak(kata):
    print(kata)

cetak("ini adalah fungsi cetak")
cetak(1+2)

def biodata(nama = "Ahmad", alamat = "Jakarta", umur = 20):
    cetak("nama saya adalah " + nama)
    cetak("alamat saya adalah " + alamat)
    cetak("umur saya adalah " + str(umur))

biodata("wahyu", "depok", 20)
# biodata("siti", "bogor")
biodata()

def perkalian(a, b):
    print(a * b)

perkalian(2, 3)
perkalian(5, 10)

def luas_persegi(sisi):
    print(sisi * sisi)

luas_persegi(5)
luas_persegi(10)

# arbitrary *args
def arbitrary(*nama):
    print("Nama saya adalah " + nama[2])

arbitrary("wahyu", "siti", "salman")

#return 
def bilangan1(x):
    return x * 4

def bilangan2(y):
    return y * y

cetak(bilangan1(2) + bilangan2(3))