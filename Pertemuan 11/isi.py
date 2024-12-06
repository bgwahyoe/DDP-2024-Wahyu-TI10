class Orang:
    # properti
    # nama = "Wahyu"
    # umur = 0
    # jekel = ""

    # constructor
    def __init__(self, nama, umur, jekel, alamat):
        self.nama = nama
        self.umur = umur
        self.jekel = jekel
        self.alamat = alamat 

    # method
    def ngomong(self):
        print("Saya bisa bicara,", self.jekel)

    def jalan(self):
        print("Saya bisa jalan, jadi kapan kita jalan?", self.nama)

# # membuat objek
# supir = Orang()
# print(supir.nama)

# # memanggil method ngomong
# supir.ngomong("Karena saya perempuan")

# # Menambah Mendeklarasikan supir
# supir.sim = "A"
# print("Saya punya SIM", supir.sim)

# supir.nama = "Budi"
# print("Nama saya itu", supir.nama)

# # Memanggil method jalan
# supir.jalan()