from animal import *

class Bird(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    def info_bird(self):
        super().info_animal()
        print("Warna \t\t\t:", self.warna,
              "\nJenis Paruh \t\t:", self.paruh,
              "\n=====================")

# objek 1
gagak = Bird("Gagak", "Daging", "Udara", "Bertelur", "Hitam", "Tajam")
gagak.info_bird()

# objek 2
merpati = Bird("Merpati", "Biji-bijian", "Udara", "Bertelur", "Putih", "Pendek")
merpati.info_bird()

# objek 3
beo = Bird("Burung Beo", "Biji-bijian", "Udara", "Bertelur", "Hijau", "Panjang")
beo.info_bird()
